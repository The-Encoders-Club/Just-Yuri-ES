

label chess:
    python:
        DisableTalk()
        boopable = False
        show_chr("A-BFBAA-AAAC")

    if sanity_lvl() > 2 and karma_lvl() > 2:

        menu:
            y "Oh, ¿así que te gustaría jugar una partida de ajedrez, mmm?"
            "Sí":
                y "Ah, perfecto."
                y "¿Qué dificultad prefieres esta vez?"
                $ pass
            "No":
                y "Ya veo..."
                y "Quizás en otro momento, entonces."
                jump ch30_loop
    elif sanity_lvl() > 2 and karma_lvl() < 3:
        menu:
            y "¿Tú... quieres jugar al ajedrez...?"
            "Sí":
                y "Oh..."
                y "Bueno, claro, supongo que no me importaría."
                y "Me pregunto si te burlarás de mí si pierdo."
                y "Juzgando por cuánto disfrutas de mi sufrimiento, asumo que sí."
                y "En fin, elige una dificultad y empecemos."
                $ pass
            "No":
                y "Oh..."
                y "Quizás... en otro momento, entonces."
                jump ch30_loop
    elif sanity_lvl() < 3 and karma_lvl() > 2:
        menu:
            y "¿Q-quieres jugar ajedrez conmigo, sí?"
            "Sí":
                y "Uy, jeje~!"
                y "¿Qué dificultad prefieres esta vez?"
                y "Aunque no importa cuál elijas... estoy segura de que igual me dominarás por completo~"
                $ pass
            "No":
                y "O-oh..."
                y "Bueno..."
                y "Está bien..."
                y "Quizás en otro momento, entonces..."
                jump ch30_loop
    elif sanity_lvl() < 3 and karma_lvl() < 3:
        menu:
            y "¿Quieres jugar al ajedrez, eh?"
            "Sí":
                y "Estoy segura de que de alguna forma lograrás convertir incluso algo tan trivial en una pesadilla para mí..."
                y "De alguna manera aún encontrarás la forma de humillarme..."
                y "Verdad..."
                y "En fin, ¿qué dificultad quieres?"
                $ pass
            "No":
                y "Oh..."
                y "Bueno... ya veo..."
                y "Quizás otro día... cuando aprendas a decidirte."
                jump ch30_loop

    $ fen = STARTING_FEN
    $ global_objects['STOCKFISH_ENGINE'] = chess.engine.SimpleEngine.popen_uci(STOCKFISH, startupinfo=STARTUPINFO)
    $ movetime = 2000

    menu:
        "Fácil":
            $ show_chr("A-ACEAA-AMAM")
            y "Oh, ya veo."
            y "¿Quieres que sea más amable contigo esta vez, eh?"
            y "Me alegra complacerte, [player]!"
            $ depth = 1
        "Medio":

            $ show_chr("A-ACEAA-AMAM")
            y "Oh, ya entiendo~ ¿Buscas un pequeño desafío, eh?"
            y "Bien entonces. ¡Me encantería ver cómo te desenvuelves!"
            y "Salir un poco de tu zona de confort no hace daño, ¿verdad?."
            $ depth = 5
        "Difícil":

            $ show_chr("A-ACEAA-AMAM")
            y "Oh jejeje... ¿De verdad estás subiendo el ritmo, [player]?"
            y "Me gusta cuando te atreves un poco más~ Es bastante inspirador."

            y "Bueno, como dicen hoy en día, supongo, ¡que comiencen los juegos!"
            y "P-pero no te presiones demasiado, [player]... jejeje."
            $ depth = 10


    menu:
        y "¿Con qué color te gustaría jugar?"
        "Blanco":
            y "¡Que gane el mejor jugador!"
            $ player_color = WHITE
            $ renpy.free_memory()
        "Negro":
            y "¡Que gane el mejor jugador!"

            $ player_color = BLACK
            $ renpy.free_memory()


    $ quick_menu = False


    $ renpy.block_rollback()

    call screen chess(fen, player_color, movetime, depth)


    $ renpy.block_rollback()


    $ renpy.checkpoint()

    $ quick_menu = True
    window show















label chess_results:
    $ renpy.free_memory()
    if _return == DRAW:
        y "Parece que es un empate. Bien jugado, [player]."
        jump ch30_loop
    else:
        $ winner = "Blancas" if _return == WHITE else "Negras"

        if player_color is not None:
            if _return == player_color:
                y "¡Felicidades, [player]!"
                jump ch30_loop
            else:
                y "Quizás tengas más suerte la próxima vez, [player]."
                jump ch30_loop

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
