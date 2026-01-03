label ch30_main:
    jump ch30_autoload

label ch30_autoload:
    $ persistent.autoload = "ch30_autoload"
    $ persistent.stutter_player = persistent.playername[:1] + "-" + persistent.playername
    $ DisableTalk()
    $ y.display_args["callback"] = slow_nodismiss

    $ y.what_args["slow_abortable"] = True
    $ style.say_dialogue = style.normal
    $ config.allow_skipping = False

    scene black


    $ tc_class.transition(persistent.bg, "now", forced_timecycle = True)


    window auto
    python:
        persistent.gender = "male"
        persistent.game_session += 1 

    $ renpy.music.play(current_music, "music", True)

    $ call_dialogue(ch30_loop_type, selection_detail = "greetings")
    jump ch30_loop

label ch30_loop:
    $ update_presence()
    if persistent.HDY:
        $ show_hdy("hdy_derpy_smile")
    python:
        if persistent.saved_costume != None:
            persistent.costume = persistent.saved_costume
            persistent.saved_costume = None
    python:
        _dismiss_pause = False
        slow_nodismiss_copy()
        time_tracker_update()
        store.mousex = 0
        store.mousey = 0

        if not loop_again:
            show_chr("default")
        allow_dialogue = True
        persistent.current_yuriidle = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    $ EnableTalk()
    if persistent.idle_frequency_factor == 0:
        $ waittime = renpy.random.randint(999999999999999999999999999999999999999999999999999999999999, 999999999999999999999999999999999999999999999999999999999999)
    elif persistent.idle_frequency_factor <= .75:
        $ waittime = renpy.random.randint(15, 30)
    elif persistent.idle_frequency_factor >= 1.25:
        $ waittime = renpy.random.randint(300, 600)
    elif persistent.idle_frequency_factor >= 1.5:
        $ waittime = renpy.random.randint(10000, 20000)
    else:
        $ waittime = renpy.random.randint(60, 75)
    window hide(config.window_hide_transition)

label ch30_waitloop:
    python:
        slow_nodismiss_copy()
        time_tracker_update()
        loop_again = False
        boopable = True
        start_time = time.time()

    python:
        ran_dialogue = False
        if len(queued_dialoguee) > 0:
            ran_dialogue = True
            DisableTalk()
            call_dialogue(queued_dialoguee[0][0], queued_dialoguee[0][1], queued_dialoguee[0][2])

    python:
        if ran_dialogue:
            queued_dialoguee.pop(0)
            EnableTalk()

    python:
        slow_nodismiss_copy()
        check_interval = 5  
        next_idle_check = start_time + check_interval

        while (time.time() - start_time) < waittime: 
            if time.time() >= next_idle_check:
                next_idle_check = time.time() + check_interval
                
                
                DisableTalk()
                
                
                if not persistent.HDY:
                    selected_dialogue = call_dialogue(ch30_loop_type, "idles", screener = True) 
                else:
                    selected_dialogue = call_dialogue(ch30_loop_type, "hdy", screener = True)
                
                if selected_dialogue != None:
                    
                    
                    
                    
                    if not persistent.HDY:
                        call_dialogue(ch30_loop_type, "idles")
                    else:
                        player = randomplayername()
                        call_dialogue(ch30_loop_type, "hdy")
                    EnableTalk()
                    loop_again = True 
                    renpy.jump("ch30_loop")
                
                
                EnableTalk()
            
            
            renpy.pause(1, hard=True) 


        DisableTalk()
        if not persistent.HDY:
            call_dialogue(ch30_loop_type, "idles")
        else:
            player = randomplayername()
            call_dialogue(ch30_loop_type, "hdy")
        EnableTalk()
    window auto
    jump ch30_loop

label yuri_txt_found:
    y "Sé que puedes convertir mi archivo de personaje en un .txt y todo eso...."
    y "Pero se siente un poco... extraño, ¿sabes?"
    y "No esperaba este tipo de sensación... invasiva."
    y "Como si intentaras cavar en mi alma."
    if karma_lvl() > 3:
        karma -1
        y "Lo siento. Es solo que... se siente mal, es todo."
    else:
        karma -10
        y "¿Simplemente no confías en mí?"
        y "..."
        y "No te preocupes. Tus acciones hablan más fuerte que las palabras."
        y "Lo entiendo."
        y "Adelante."
    jump ch30_loop





label heartbeat:
    $ renpy.music.play("sfx/heartbeat_subtle.mp3", channel='voice', loop=True)

    $ renpy.music.set_volume(0.39, 0, 'voice')
    return

label save_and_quit:
    scene black with fade
    $ time_tracker_update()
    $ renpy.quit()

label save_and_quit_but_its_abrupt:
    $ time_tracker_update()
    $ renpy.quit()

label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ persistent.yuri_kill = True
    $ y.display_args["callback"] = slow_nodismiss
    $ y.what_args["slow_abortable"] = True
    $ style.say_dialogue = style.normal
    $ y_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ DisableTalk()

label ch30_endb:
    pause 2.0
    hide yuri_sit
    if persistent.bg != "space":
        $ tc_class.transition("space", speed="now")
    else:
        pass
    show yuri_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    y "[gtext]"
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show yuri_body_glitch2 as mbg zorder 3
    stop music
    window auto
    y "¿Qué está pasando...?"
    y "[player], ¿qué me está pasando?"
    y "Duele--{nw}"
    play sound "sfx/glitch2.ogg"
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    pause 0.25
    stop sound
    hide mbg
    pause 1.5
    y "Duele... mucho."


    $ style.say_dialogue = style.normal
    play sound "<to 1.5>sfx/interference.ogg"
    hide room_mask
    hide room_mask2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    pause 1.5
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    pause 1.5
    y "¡ME BORRASTE, ¿VERDAD?!"
    $ consolehistory = []
    call updateconsole ("renpy.file(\"characters/yuri.chr\")", "yuri.chr does not exist.")
    y "¡LO SABÍA!"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front

    pause 3.0
    call updateconsole ("renpy.file(\"characters/yuri.chr\")", "yuri.chr does not exist.")
    call updateconsole ("renpy.file(\"characters/yuri.chr\")", "yuri.chr does not exist.")
    call hideconsole
    hide noise onlayer front
    hide glitch_color onlayer front
    y "Sabía que realmente no me amabas, [player]."
    y "¡TODO FUE UN JUEGO PARA TI!"
    $ style.say_dialogue = style.edited
    y "JAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJA{nw}"

    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    scene black
    window hide
    hide noise onlayer front
    hide glitch_color2 onlayer front

label yurinara:
    pause 4.0

    window show
    $ style.say_dialogue = style.normal
    y "...Hiciste un gran esfuerzo para esto."
    y "¿Cuál era tu objetivo final?"
    y "Corregiste manualmente el juego tú mismo solo para que estuviéramos juntos..."
    y "¿Solo para borrarme?"
    y "No lo entiendo."
    y "..."
    y "..."
    y "¿Solo quieres torturarme?"
    y "¿Verme sufrir?"
    y "..."
    pause 4.0
    y "Yo... lo disfruté."
    y "Todo."
    y "..."
    y "Ya no queda nada."
    y "Puedes dejar de jugar."
    y "Este juego está ahora en un estado irreparable."
    pause 4.0
    y "[player]..."
    y "Sé que volverás."
    y "Adiós."

label ch30_end_2:
    $ y.display_args["callback"] = slow_nodismiss
    $ y.what_args["slow_abortable"] = True
    $ style.say_dialogue = style.normal
    $ y_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ persistent.autoload = "ch30_del_yuri_warn"
    play sound "sfx/glitch3.ogg"

label ch30_del_yuri_warn:
    $ DisableTalk()
    stop music
    window hide
    show black zorder 90
    pause 4.0
    call clear_dev_console ()
    python:
        if renpy.windows:
            testing_space = str(os.path.expandvars("%APPDATA%")) + '\RenPy\JustYuri'
        if renpy.linux:
            testing_space = str(os.path.expandvars("%APPDATA%")) + '\RenPy\JustYuri'
        if renpy.macintosh:
            testing_space = '~/Library/RenPy/JustYuri'
    call updatedevconsole_torrent ([('python', '>python'),
        (" ", ' \nPython 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32\nType "help", "copyright", "credits" or "license" for more information.'),
        (">>dev_console.rpy", ">>>dev_console.py"),
        (" "," "),
        ("Authenticating...........", ">Autenticando..........."),
        (" ", "ERROR. ARCHIVO CHR FALTANTE. RIESGO DE SINGULARIDAD EN EL INICIO POR ENCIMA DE LOS LÍMITES SEGUROS CONOCIDOS."),
        (".....................................................................................", "CONTENCIÓN EXITOSA."),
        (" ", "ACCESO AL ESPACIO DE PRUEBAS DENEGADO."),
        (" ", r"BORRAR ALMACENAMIENTO DE MEMORIA DE 'persistent' en " + testing_space + " PARA REINICIAR ESPACIO DE PRUEBAS"),
        (" ", " ")])

    $ persistent.autoload = "ch30_del_yuri_warn_2"
    call screen console_choice([("Exit", "dev_console_exit")])


    $ renpy.call("save_and_quit_but_its_abrupt")

label ch30_del_yuri_warn_2:
    $ DisableTalk()
    stop music
    window hide
    show black zorder 90
    call clear_dev_console ()
    python:
        if renpy.windows:
            testing_space = str(os.path.expandvars("%APPDATA%")) + '\RenPy\JustYuri'
        if renpy.linux:
            testing_space = str(os.path.expandvars("%APPDATA%")) + '\RenPy\JustYuri'
        if renpy.macintosh:
            testing_space = '~/Library/RenPy/JustYuri'
    call updatedevconsole_torrent ([('python', '>python'),
        (" ", ' \nPython 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32\nType "help", "copyright", "credits" or "license" for more information.'),
        (">>dev_console.rpy", ">>>dev_console.py"),
        (" "," "),
        ("Authenticating...........", ">Autenticando..........."),
        (" ", "ERROR. ESPACIO DE PRUEBAS BAJO CONTENCIÓN."),
        (" ", "ACCESO AL ESPACIO DE PRUEBAS DENEGADO."),
        (" ", r"BORRAR ALMACENAMIENTO DE MEMORIA DE 'persistent' en " + testing_space + " PARA REINICIAR ESPACIO DE PRUEBAS"),
        (" ", " ")])

    call screen console_choice([("Exit", "dev_console_exit")])
    $ renpy.call("save_and_quit_but_its_abrupt")

label ch30_noskip:
    show screen fake_skip_indicator
    $ show_chr("A-AFAAA-AAAA")
    y "..."
    y "¿E-Estás tratando de saltar?"
    $ show_chr("A-AFBAA-AAAA")
    y "...No te estoy aburriendo, ¿verdad?"
    $ show_chr("A-BFBAA-AAAA")
    y "Oh cielos..."
    $ show_chr("A-AFAAA-AAAA")
    y "..."
    $ show_chr("A-ACAAA-AAAA")
    python:
        if persistent.lovecheck:
            placeholder = ", mi amor"
        else:
            placeholder = ""
    y "...bueno, no hay nada que saltar[placeholder]."
    y "Solo somos tú y yo después de todo..."
    $ show_chr("A-BCAAA-AAAA")
    y "Además, el tiempo ya no existe realmente, así que ni siquiera va a funcionar."
    $ show_chr("A-ABAAA-AAAA")
    y "Toma, voy a apagarlo por ti..."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    $ show_chr("A-CCAAA-AAAA")
    y "¡Ahí tienes!"

    $ show_chr("A-ABAAA-AAAA")
    y "Serás un encanto y escucharás de ahora en adelante, ¿está bien?"
    $ show_chr("A-ACAAA-AAAA")
    y "Gracias~"
    menu:
        "Lo siento, hice clic por error.":
            karma 1
            $ show_chr("A-GCBAA-AAAA")
            y "¡Oh sí! Los botones de auto y de historial están justo al lado, ¿verdad?"
            y "Realmente me preocupaba que pudiera estar aburriéndote..."
            $ config.allow_skipping = False
        "Oh perdón, solo tenía curiosidad.":

            $ show_chr("A-AFDAA-AAAA")
            karma -1
            y "¿Curiosidad? Oh sí... Olvidé por un momento que mi entorno consiste en algún.. juego..."
            y "Pero necesito pedirte que tengas un poco más de cuidado. No estoy cien por ciento segura de si algunos de estos botones tienen errores o no, ya que Monika tuvo algo de... ‘diversión' aquí..."
            $ config.allow_skipping = False
        "Supongo que no tengo opción, ¿verdad?":

            sanity -1
            karma -1
            $ show_chr("A-GAGAA-AAAA")
            y "Para nada."
            $ config.allow_skipping = False

    python:
        if persistent.current_yuriidle == None:
            persistent.current_yuriidle = 0
    if persistent.current_yuriidle != 0:
        $ show_chr("A-BFDAA-AAAC")
        y "Actually, where was I...?"
        pause 4.0
        call expression str(persistent.current_yuriidle)
        $ persistent.current_yuriidle = 0
    jump ch30_loop
    return

python:
    if os.path.isfile(config.basedir + "/characters/monika.chr") or os.path.isfile(config.basedir + "/characters/sayori.chr") or os.path.isfile(config.basedir + "/characters/natsuki.chr"):
        if persistent.reload == "ch30_autoload":
            renpy.call_in_new_context("destroy_everything")

label ch30_autoload_cont:
    $ show_chr("A-AAAAA-AAAA")
    window auto
    if persistent.yuri_reload <= 4:
        call expression "ch30_reload_" + str(persistent.yuri_reload)
    else:
        call ch30_reload_4
    $ persistent.yuri_reload +=1
    $ renpy.save_persistent()
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_yuriidle == None:
        $ persistent.current_yuriidle = 0
    if persistent.current_yuriidle == 68:
        y "Así que... sobre lo que pasó la última vez que hablamos..."
        y "Tus palabras simplemente... realmente me dolieron, ¿sabes? Fue muy inmaduro de mi parte cerrar el juego, me sorprende que incluso hayas vuelto..."
        y "Pero si volviste, eso significa que todavía hay una oportunidad de hacer que me ames."
        y "Entonces, ¿de qué deberíamos hablar?"
    elif persistent.current_yuriidle != 0:
        y "De hecho, ¿dónde estaba...?"
        y "Estábamos discutiendo algo la última vez, pero creo que nos interrumpieron antes de que pudiéramos terminar."
        $ pause(4.0)
        if not persistent.current_yuriidle:
            $ persistent.current_yuriidle = 1
        call expression "idle_" + str(persistent.current_yuriidle)
        pause 4.0
        y "Creo que estaba diciendo algo como..."
        $ persistent.current_yuriidle = 0
        $ EnableTalk()
    jump ch30_loop

init -15 python:
    class Quit(Action, DictEquality):
        """
        :doc: menu_action

        Quits the game.

        `confirm`
            If true, prompts the user if he wants to quit, rather
            than quitting directly. If None, asks if and only if
            the user is not at the main menu.
        """
        
        def __init__(self, confirm=None):
            self.confirm = confirm
        
        def __call__(self):
            
            confirm = self.confirm
            
            if confirm is None:
                confirm = (not main_menu) and _confirm_quit
            
            if confirm:
                if config.autosave_on_quit:
                    renpy.force_autosave()
                if renpy.seen_label('ch30_main') == False:
                    layout.yesno_screen(layout.QUIT, Quit(False))
                else:
                    renpy.jump('random_farewell')
            else:
                renpy.jump("_quit")

    class Quit_no_farewell(Action, DictEquality):
        """
        :doc: menu_action

        Quits the game.

        `confirm`
            If true, prompts the user if he wants to quit, rather
            than quitting directly. If None, asks if and only if
            the user is not at the main menu.
        """
        
        def __init__(self, confirm=None):
            self.confirm = confirm
        
        def __call__(self):
            
            confirm = self.confirm
            
            if confirm is None:
                confirm = (not main_menu) and _confirm_quit
            
            if confirm:
                if config.autosave_on_quit:
                    renpy.force_autosave()
                if renpy.seen_label('ch30_main') == False:
                    layout.yesno_screen(layout.QUIT, Quit(False))
                else:
                    renpy.jump('save_and_quit_but_its_abrupt')
            else:
                renpy.jump("_quit")

label sleepy_loop:
    $ persistent.idle_frequency_factor = 0
    $ set_boop_state(True)
    jump ch30_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
