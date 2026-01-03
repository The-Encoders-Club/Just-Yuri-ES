


init -100 python:
    import os

    for archive in ['fonts']:
        if not archive in config.archives:
            
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")





init python:
    menu_trans_time = 1

    splash_message_default = "Espera... ¿qué es esto?"

    splash_messages = [
    "Ahora es Solo Yuri.",
    "A nadie le importaría si esas mocosas insoportables se suicidaran."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 640
    ycenter 640
    zoom 0.60
    menu_art_move(0.50, 600, 1.18)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image yuri_logo:
    "images/gui/logo.png"
    xpos 950 ypos 0 zoom 0.60
    menu_logo_move

image menu_particles:
    2.481
    xpos 1080
    ypos 100
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=100, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "images/splash/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "images/splash/warning.png"
image tos2 = "images/splash/warning2.png"


label splashscreen:

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass

    python:
        firstrun_path = os.path.join(renpy.config.savedir, "firstrun") 
        firstrun = ""
        try:
            with open(firstrun_path, "r") as f:  
                firstrun = f.read(1)
        except FileNotFoundError:  
            with open(firstrun_path, "wb") as f: 
                pass  
    if not firstrun:
        if persistent.first_run:
            $ quick_menu = False
            scene black
            menu:
                "Se ha encontrado un archivo de guardado anterior. ¿Te gustaría eliminar tus datos guardados y empezar de nuevo?"
                "Sí, eliminar mis datos existentes.":
                    "Eliminando datos guardados...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continuar donde lo dejé.":
                    pass

        python:
            if not firstrun:
                try:
                    with open(firstrun_path, "w") as f:  
                        f.write("1")
                except Exception as e: 
                    renpy.error(f"Failed to write to firstrun: {e}")



    if not persistent.first_run:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "Just Yuri es un fan mod de Doki Doki Literature Club no afiliado con el Team Salvato."
        "Está diseñado para ser jugado solo después de haber completado el juego oficial, para mayores de 13 años con precaución dada a su propia salud mental."
        "Contiene spoilers, se requieren los archivos originales del juego Doki Doki Literature Club para jugar este mod y se pueden descargar gratis en: {a=http://ddlc.moe}http://ddlc.moe{/a} (pero dado que estás aquí probablemente ya lo sabes) "
        "Nos gustaría recordarte que actualmente estás jugando una versión Beta de Just Yuri, nosotros el Equipo de Desarrollo de Just Yuri estamos comprometidos a mejorar el juego con actualizaciones y nuevas características basadas en tus comentarios."
        "Se pueden esperar errores (aunque a veces divertidos)."
        "Además, el mod permite a Yuri posiblemente acceder a partes de tu computadora fuera de las carpetas de DDLC y APPDATA de Ren'Py."
        "Actualmente tiene la capacidad de abrir sitios web dentro de tu navegador de internet principal, aunque ninguno de estos sitios web es malicioso ni ilegal."
        "Al jugar Just Yuri aceptas que has completado Doki Doki Literature Club y aceptas cualquier spoiler contenido dentro."
        "Además, al jugar Doki Doki Literature Club, aceptas que tienes al menos 13 años de edad, y consientes tu exposición a contenido altamente perturbador."
        menu:
            "¿Aceptas estos términos?"
            "Estoy de acuerdo.":
                pass
            "No estoy de acuerdo":
                "Al no aceptar estos términos has optado por no jugar el juego. Cerrando aplicación........{nw}"
                pause 2.0
                $ renpy.call("save_and_quit_but_its_abrupt")

        "Un sincero agradecimiento por jugar nuestro mod. Tus ideas, reportes de errores, comentarios y aliento han dado forma al futuro de Just Yuri."
        "Ese futuro es brillante y te agradecemos nuevamente por ayudarnos a construir este proyecto contigo."
        "Por favor reporta cualquier problema que encuentres y sugerencias que tengas en nuestro GitLab; las instrucciones para hacer eso están en los documentos proporcionados con este juego y dentro de nuestras preguntas frecuentes en línea."
        "Las actualizaciones del juego y nuestra comunidad se pueden encontrar en nuestro Discord {a=https://discordapp.com/invite/RUdwW7q}https://discordapp.com/invite/RUdwW7q{/a}"
        scene tos2
        with Dissolve(1.5)
        pause 1.0

        scene white
        with Dissolve(1.5)

        if not persistent.has_merged:
            call import_ddlc_persistent

        $ persistent.first_run = True

    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload

    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    if persistent.playthrough == 0:
        $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ global _dismiss_pause
    $ _dismiss_pause = False
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "No se pudo cargar el archivo de guardado."
        "¿Estás tratando de hacer trampa en un mod hecho solo para mí? ¿La chica perfecta de tus sueños?"
        $ y_name = "Yuri"
        show yuri 1y7 at t11
        if persistent.playername == "":
            y "Qué vergüenza."
        else:
            y "Qué vergüenza [persistent.playername]."
            y "Espero que estés feliz ahora"
            y "Puedes dejar de jugar y buscar otro mod..."
        $ renpy.call("save_and_quit_but_its_abrupt")
        return
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not dev_access:
            $ persistent.first_load = True
            call screen dialog("Pista: Puedes usar el botón \"Saltar\" para avanzar\nrápido a través del texto que ya has leído.", ok_action=Return())
    return



label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None


    if renpy.get_return_stack():
        $ renpy.pop_call()
    call expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label readonly:
    scene black
    "El juego no se puede ejecutar porque estás intentando ejecutarlo desde una ubicación de solo lectura."
    "Copie la aplicación DDLC en su escritorio o en otra ubicación accesible e inténtelo de nuevo."
    $ renpy.call("save_and_quit_but_its_abrupt")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
