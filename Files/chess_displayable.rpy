



define THIS_PATH = '00-chess-engine/'
define IMAGE_PATH = 'images/'
define AUDIO_PATH = 'audio/'
define BIN_PATH = 'bin/'
define CHESSPIECES_PATH = THIS_PATH + IMAGE_PATH + 'chesspieces/'


define IMG_CHESSBOARD = THIS_PATH + IMAGE_PATH + 'chessboard.png'
define AUDIO_MOVE = THIS_PATH + AUDIO_PATH + 'move.wav'
define AUDIO_CAPTURE = THIS_PATH + AUDIO_PATH + 'capture.wav'
define AUDIO_PROMOTION = THIS_PATH + AUDIO_PATH + 'promotion.wav'
define AUDIO_CHECK = THIS_PATH + AUDIO_PATH + 'check.wav'
define AUDIO_CHECKMATE = THIS_PATH + AUDIO_PATH + 'checkmate.wav'
define AUDIO_DRAW = THIS_PATH + AUDIO_PATH + 'draw.wav'
define AUDIO_FLIP_BOARD = THIS_PATH + AUDIO_PATH + 'flip_board.wav'


define CHESS_SCREEN_WIDTH = 598
define CHESS_SCREEN_HEIGHT = 318
define CHESS_BOARD_SIDE_LEN = CHESS_SCREEN_HEIGHT


define LOC_LEN = 42


define INDEX_MIN = 0
define INDEX_MAX = 7

define FILE_LETTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

define PROMOTION_RANK_WHITE = 6
define PROMOTION_RANK_BLACK = 1

define COLOR_HOVER = '#90ee90aa'
define COLOR_SELECTED = '#40e0d0aa'
define COLOR_LEGAL_DST = '#afeeeeaa'
define COLOR_PREV_MOVE = '#6a5acdaa'
define COLOR_WHITE = '#fff'

define TEXT_SIZE = 8
define TEXT_BUTTON_SIZE = 20
define TEXT_WHOSETURN_COORD = (-260, 40)
define TEXT_STATUS_COORD = (-260, 80)


define PIECE_TYPES = ('p', 'r', 'b', 'n', 'k', 'q')


define NUM_HISTORY = 5


define MIN_MOVETIME = 100
define MAX_MOVETIME = 3000
define MIN_DEPTH = 1
define MAX_DEPTH = 20


define STARTING_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'



define WHITE = True
define BLACK = False


define INCHECK = 1
define THREEFOLD = 2
define FIFTYMOVES = 3

define DRAW = 4
define CHECKMATE = 5
define STALEMATE = 6






style game_status_text is text:
    font 'DejaVuSans.ttf'
    color COLOR_WHITE
    size TEXT_SIZE

style promotion_piece is button
style promotion_piece_text is text:
    font 'DejaVuSans.ttf'
    size TEXT_BUTTON_SIZE
    color '#aaaaaa'
    hover_color '#555555'
    selected_color COLOR_WHITE



style control_button is button
style control_button_text is text:
    font 'DejaVuSans.ttf'
    size TEXT_BUTTON_SIZE
    color '#aaaaaa'
    hover_color COLOR_WHITE





screen chess(fen, player_color, movetime, depth):

    modal False

    default hover_displayable = HoverDisplayable()
    default chess_displayable = ChessDisplayable(
        fen=fen, 
        player_color=player_color, 
        depth=depth
        )





    fixed xpos 20 ypos 390 spacing 30:
        vbox:
            showif chess_displayable.whose_turn == WHITE:
                text 'Whose turn: White' style 'game_status_text'
            else:
                text 'Whose turn: Black' style 'game_status_text'



            showif chess_displayable.game_status == CHECKMATE:
                text 'Checkmate' style 'game_status_text'
            elif chess_displayable.game_status == STALEMATE:
                text 'Stalemate' style 'game_status_text'
            elif chess_displayable.game_status == INCHECK:
                text 'In Check' style 'game_status_text'




            text 'Most recent moves' style 'game_status_text' xalign 0.5
            for move in chess_displayable.history:
                text move.uci() style 'game_status_text' xalign 0.5




    fixed xpos 200 ypos 390:
        vbox:
            hbox spacing 5:
                text 'Resign' color COLOR_WHITE size 13 yalign 0.5
                textbutton '⚐':
                    action [Confirm('Would you like to resign?',
                        yes=[
                        Play('sound', AUDIO_DRAW),
                        
                        Return(not chess_displayable.whose_turn),
                        Jump("chess_results")  
                        ])]
                    style 'control_button' yalign 0.5

            hbox spacing 5:
                text 'Undo move' color COLOR_WHITE size 13 yalign 0.5
                textbutton '⟲':
                    action [Function(chess_displayable.undo_move)]
                    style 'control_button' yalign 0.5

            hbox spacing 5:
                text 'Flip board view' color COLOR_WHITE size 13 yalign 0.5
                textbutton '↑↓':
                    action [Play('sound', AUDIO_FLIP_BOARD),
                    ToggleField(chess_displayable, 'bottom_color'),
                    SetField(chess_displayable, 'has_flipped_board', True)]
                    style 'control_button' yalign 0.5


    fixed xpos 20 ypos 20:
        add Image(IMG_CHESSBOARD)
        fixed xpos 11 ypos 10:
            add chess_displayable
            add hover_displayable
        if chess_displayable.game_status == CHECKMATE:

            timer 4.0 action [
            Return(chess_displayable.winner),
            renpy.jump("chess_results")  
            ]
        elif chess_displayable.game_status == STALEMATE:
            timer 4.0 action [
            Return(DRAW),
            renpy.jump("chess_results")  
            ]


    showif chess_displayable.show_promotion_ui:
        text 'Select promotion piece type' xpos 20 ypos 550 color COLOR_WHITE size 18


        textbutton '♜' xpos 40 ypos 575:
            action SetField(chess_displayable, 'promotion', 'r') style 'promotion_piece'
        textbutton '♝' xpos 90 ypos 575:
            action SetField(chess_displayable, 'promotion', 'b') style 'promotion_piece'
        textbutton '♞' xpos 140 ypos 575:
            action SetField(chess_displayable, 'promotion', 'n') style 'promotion_piece'
        textbutton '♛' xpos 190 ypos 575:
            action SetField(chess_displayable, 'promotion', 'q') style 'promotion_piece'



init python:



    import os
    import sys
    import pygame
    from collections import deque 

    import_dir = os.path.join(renpy.config.gamedir, THIS_PATH, 'python-packages')
    sys.path.append(import_dir)
    global_objects = {}

    import chess
    import chess.engine
    import subprocess 


    stockfish_bin = None
    STARTUPINFO = None
    if renpy.android:
        stockfish_bin = 'stockfish-10-armv7' 
    elif renpy.ios:
        stockfish_bin = 'stockfish-11-64' 
    elif renpy.linux:
        stockfish_bin = 'stockfish_20011801_x64'
    elif renpy.macintosh:
        stockfish_bin = 'stockfish-11-64'
    elif renpy.windows:
        stockfish_bin = 'stockfish_20011801_x64.exe'
        STARTUPINFO = subprocess.STARTUPINFO()
        STARTUPINFO.dwFlags = subprocess.STARTF_USESHOWWINDOW
    else:
        raise Exception('No stockfish binary found for your system')


    stockfish_dir = os.path.join(renpy.config.gamedir, THIS_PATH, BIN_PATH)
    build.executable(os.path.join(stockfish_dir, 'stockfish-11-64')) 
    build.executable(os.path.join(stockfish_dir, 'stockfish_20011801_x64')) 

    STOCKFISH = os.path.join(stockfish_dir, stockfish_bin)

    class HoverDisplayable(renpy.Displayable):
        """
        Highlights the hovered loc in green
        """
        def __init__(self):
            super(HoverDisplayable, self).__init__()
            self.hover_coord = None
            self.hover_img = Solid(COLOR_HOVER, xsize=LOC_LEN, ysize=LOC_LEN)
        
        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            if self.hover_coord:
                render.place(self.hover_img, 
                    x=self.hover_coord[0], y=self.hover_coord[1], 
                    width=LOC_LEN, height=LOC_LEN)
            return render
        
        def event(self, ev, x, y, st):
            
            if 0 < x < CHESS_BOARD_SIDE_LEN and 0 < y < CHESS_BOARD_SIDE_LEN and ev.type == pygame.MOUSEMOTION:
                self.hover_coord = round_coord(x, y)
                renpy.redraw(self, 0)                

    class ChessDisplayable(renpy.Displayable):
        """
        The main displayable for the chess minigame
        If player_color is None, use Player vs. Player mode
        Else, use Player vs. Stockfish mode
        player_color: None, WHITE, chess.BLACK
        """
        def __init__(self, fen=STARTING_FEN, player_color=None, depth=10):
            super(ChessDisplayable, self).__init__()
            self.board = chess.Board(fen)
            
            self.whose_turn = WHITE
            self.has_flipped_board = False 
            
            self.history = deque([], NUM_HISTORY)
            
            self.player_color = player_color
            
            if self.player_color is None: 
                self.bottom_color = WHITE 
                self.uses_stockfish = False 
            
            else: 
                self.bottom_color = self.player_color 
                self.uses_stockfish = True
                
                self.engine = global_objects['STOCKFISH_ENGINE']
                self.engine_limit = chess.engine.Limit(depth=depth)
                
                
                depth = depth if MIN_DEPTH <= depth <= MAX_DEPTH else MAX_DEPTH
            
            
            self.selected_img = Solid(COLOR_SELECTED, xsize=LOC_LEN, ysize=LOC_LEN)
            self.legal_dst_img = Solid(COLOR_LEGAL_DST, xsize=LOC_LEN, ysize=LOC_LEN)
            self.highlight_img = Solid(COLOR_PREV_MOVE, xsize=LOC_LEN, ysize=LOC_LEN)
            self.piece_imgs = self.load_piece_imgs()
            
            
            self.src_coord = None
            
            self.legal_dsts = []
            
            self.highlighted_squares = []
            
            
            self.show_promotion_ui = False
            self.promotion = None
            
            self.game_status = None
            
            self.winner = None 
        
        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            
            
            if self.src_coord:
                render.place(self.selected_img, 
                    x=self.src_coord[0], y=self.src_coord[1], 
                    width=LOC_LEN, height=LOC_LEN)
            
            
            for file_idx, rank_idx in self.legal_dsts:
                square_coord = indices_to_coord(file_idx, rank_idx, bottom_color=self.bottom_color)
                render.place(self.legal_dst_img, x=square_coord[0], y=square_coord[1])
            
            for file_idx, rank_idx in self.highlighted_squares:
                square_coord = indices_to_coord(file_idx, rank_idx, bottom_color=self.bottom_color)
                render.place(self.highlight_img, x=square_coord[0], y=square_coord[1])
            
            
            for file_idx in range(INDEX_MIN, INDEX_MAX + 1):
                for rank_idx in range(INDEX_MIN, INDEX_MAX + 1):
                    
                    piece = self.board.piece_at(chess.square(file_idx, rank_idx))
                    if piece and piece.symbol() in self.piece_imgs: 
                        piece_coord = indices_to_coord(file_idx, rank_idx, bottom_color=self.bottom_color)
                        render.place(self.piece_imgs[piece.symbol()], 
                            x=piece_coord[0], y=piece_coord[1])
            
            renpy.restart_interaction() 
            
            return render
        
        def event(self, ev, x, y, st):
            
            if self.game_status in [CHECKMATE, STALEMATE, DRAW]:
                return
            
            
            if self.uses_stockfish and self.whose_turn != self.player_color:
                result = self.engine.play(self.board, self.engine_limit)
                self.make_move(result.move)
                return
            
            
            
            
            
            
            if dev_access:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_p]: 
                    self.show_promotion_ui = not self.show_promotion_ui 
                    renpy.restart_interaction()
                elif keys[pygame.K_c]: 
                    self.show_claim_draw_ui() 
            
            
            if self.has_flipped_board:
                self.has_flipped_board = False
                
                self.src_coord = None
                self.legal_dsts = []
                renpy.redraw(self, 0)
                renpy.restart_interaction()
            
            
            if 0 < x < CHESS_BOARD_SIDE_LEN and 0 < y < CHESS_BOARD_SIDE_LEN and ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                
                
                if self.src_coord is None:
                    src_coord = round_coord(x, y)
                    src_file, src_rank = coord_to_square(src_coord, bottom_color=self.bottom_color)
                    
                    piece = self.board.piece_at(chess.square(src_file, src_rank))
                    if piece and piece.color == self.whose_turn:
                        self.src_coord = src_coord
                        
                        self.get_legal_dsts(src_file, src_rank)
                        
                        if self.has_promoting_piece(src_file, src_rank):
                            self.show_promotion_ui = True
                            self.promotion = None
                        
                        renpy.redraw(self, 0)
                
                
                else:
                    dst_coord = round_coord(x, y)
                    dst_file, dst_rank = coord_to_square(dst_coord, bottom_color=self.bottom_color)
                    src_file, src_rank = coord_to_square(self.src_coord, bottom_color=self.bottom_color)
                    
                    
                    if dst_file == src_file and dst_rank == src_rank:
                        self.src_coord = None
                        self.show_promotion_ui = False
                        self.legal_dsts = []
                        renpy.redraw(self, 0)
                        return
                    
                    
                    piece = self.board.piece_at(chess.square(dst_file, dst_rank))
                    if piece and piece.color == self.whose_turn:
                        
                        
                        self.src_coord = dst_coord
                        src_file, src_rank = dst_file, dst_rank
                        self.get_legal_dsts(src_file, src_rank)  
                        
                        if self.has_promoting_piece(src_file, src_rank):
                            self.show_promotion_ui = True
                        else:
                            self.show_promotion_ui = False
                        self.promotion = None
                        renpy.redraw(self, 0)
                        return
                    
                    
                    move = chess.Move(
                        chess.square(src_file, src_rank),
                        chess.square(dst_file, dst_rank),
                        self.promotion
                        )
                    
                    
                    if self.show_promotion_ui and not move.promotion:
                        renpy.notify('Please select a piece type to promote to')
                    
                    if move in self.board.legal_moves:
                        self.make_move(move)
        
        
        
        
        def load_piece_imgs(self):
            
            piece_imgs = {}
            
            for piece in PIECE_TYPES:
                white_path = os.path.join(CHESSPIECES_PATH, 'w' + piece + '.png')
                black_path = os.path.join(CHESSPIECES_PATH, 'b' + piece + '.png')
                white_piece, black_piece = piece.upper(), piece
                piece_imgs[white_piece] = Image(white_path)
                piece_imgs[black_piece] = Image(black_path)
            
            return piece_imgs
        
        def has_promoting_piece(self, file_idx, rank_idx):
            
            
            piece = self.board.piece_at(chess.square(file_idx, rank_idx))
            if not piece or not piece.symbol() in ['p', 'P'] or not piece.color == self.whose_turn:
                return False
            if piece.color == WHITE:
                return rank_idx == PROMOTION_RANK_WHITE
            else:
                return rank_idx == PROMOTION_RANK_BLACK
        
        def play_move_audio(self, move):
            if move.promotion: 
                renpy.sound.play(AUDIO_PROMOTION)
            else:
                
                if self.board.is_capture(move):
                    renpy.sound.play(AUDIO_CAPTURE)
                else:
                    renpy.sound.play(AUDIO_MOVE)
        
        def check_game_status(self):
            """
            Check if is checkmate, in check, or stalemate
            and update status text display accordingly
            """
            
            if self.board.is_checkmate():
                self.game_status = CHECKMATE
                renpy.sound.play(AUDIO_CHECKMATE)
                
                
                
                renpy.notify('Checkmate! The winner is %s' % ('black' if self.whose_turn else 'white'))
                self.winner = not self.whose_turn
                return
            
            if self.board.is_stalemate():
                self.game_status = STALEMATE
                renpy.sound.play(AUDIO_DRAW)
                renpy.notify('Stalemate')
                return
            
            
            if self.board.can_claim_threefold_repetition():
                self.game_status == THREEFOLD
                self.show_claim_draw_ui(reason='Threefold repetition rule: ')
            if self.board.can_claim_fifty_moves():
                self.game_status == FIFTYMOVES
                self.show_claim_draw_ui(reason='Fifty moves rule: ')
            
            
            if self.board.is_check():
                self.game_status = INCHECK 
                renpy.sound.play(AUDIO_CHECK)
            else:
                self.game_status = None
        
        def show_claim_draw_ui(self, reason=''):
            """
            reason: a string indicating the reason to claim the draw, directly prepended to message
            """
            renpy.show_screen('confirm', 
                message=reason + 'Would you like to claim draw?', 
                yes_action=[
                    Hide('confirm'),
                    Play('sound', AUDIO_DRAW),
                    Return(DRAW)
                ], 
                no_action=Hide('confirm'))
            renpy.restart_interaction()
        
        def add_highlight_move(self, move):
            src_file = chess.square_file(move.from_square)
            src_rank = chess.square_rank(move.from_square)
            dst_file = chess.square_file(move.to_square)
            dst_rank = chess.square_rank(move.to_square)
            self.highlighted_squares = [(src_file, src_rank), (dst_file, dst_rank)]
        
        
        def get_legal_dsts(self, src_file, src_rank):
            """
            filter the destination squares from the legal moves
            """
            self.legal_dsts = []
            legal_moves = self.board.legal_moves
            for move in legal_moves:
                move_src_file = chess.square_file(move.from_square)
                move_src_rank = chess.square_rank(move.from_square)
                move_dst_file = chess.square_file(move.to_square)
                move_dst_rank = chess.square_rank(move.to_square)
                
                if move_src_file == src_file and move_src_rank == src_rank:
                    self.legal_dsts.append((move_dst_file, move_dst_rank))
        
        def make_move(self, move):
            """
            1. play the corresponding move audio
            2. communicate the move to the subprocess
            3. highlight the src and dst squares of the move
            4. append the move to history
            5. 
            """
            self.play_move_audio(move)
            self.board.push(move)
            self.add_highlight_move(move)
            
            self.history.append(move)
            self.src_coord = None
            self.legal_dsts = []
            renpy.redraw(self, 0)
            
            self.whose_turn = not self.whose_turn 
            self.check_game_status()
            self.show_promotion_ui = False
            self.promotion = None
        
        def undo_move(self):
            """
            inverse of make_move, proceed only if there is something in history
            1. play the audio for making a move
            2. communicate the undoing to the subprocess
            3. remove the move from the history      
            """
            if not self.history or (self.uses_stockfish and len(self.history) < 2):
                return
            renpy.sound.play(AUDIO_MOVE)
            if self.uses_stockfish: 
                self.board.pop()
                self.board.pop()
                self.history.pop()
                self.history.pop()
            
            else: 
                self.board.pop()
                self.history.pop()
                self.whose_turn = not self.whose_turn 
            
            self.src_coord = None
            self.legal_dsts = []
            self.highlighted_squares = []
            renpy.redraw(self, 0)
            
            self.check_game_status()
            self.show_promotion_ui = False
            self.promotion = None




    def coord_to_square(coord, bottom_color=WHITE):
        """
        bottom_color: if chess.BLACK, flip the coordinate calculation
        """
        x, y = coord
        if bottom_color == WHITE:
            file_idx = x // LOC_LEN
            rank_idx = INDEX_MAX - (y // LOC_LEN)
        else: 
            file_idx = INDEX_MAX - x // LOC_LEN
            rank_idx = y // LOC_LEN
        return int(file_idx), int(rank_idx)

    def indices_to_coord(file_idx, rank_idx, bottom_color=WHITE):
        assert INDEX_MIN <= file_idx <= INDEX_MAX and INDEX_MIN <= file_idx <= INDEX_MAX
        if bottom_color == WHITE:
            x = LOC_LEN * file_idx
            y = LOC_LEN * (INDEX_MAX - rank_idx)
        else: 
            x = LOC_LEN * (INDEX_MAX - file_idx)
            y = LOC_LEN * rank_idx
        return (x, y)

    def round_coord(x, y):
        """
        for drawing, computes cursor coord rounded to the upperleft coord of the current loc
        """
        x_round = x // LOC_LEN * LOC_LEN
        y_round = y // LOC_LEN * LOC_LEN
        return (x_round, y_round)

    def square_to_file_rank(square):
        """
        has promotion if len(square) == 3
        """
        assert len(square) == 2 or len(square) == 3
        square = square[:2] 
        file_idx = ord(square[0]) - ord('a')
        rank_idx = int(square[1]) - 1
        return file_idx, rank_idx
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
