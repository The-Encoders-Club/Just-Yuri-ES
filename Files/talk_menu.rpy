style talkbutton_vbox is vbox
style talkbutton_button is button
style talkbutton_button_text is button_text
define gui.talkbutton_button_width = 120

style talkbutton_vbox:
    xalign 0.5
    ypos 270
    yalign 0.95
    yanchor 0.5

    spacing 0

style talkbutton_button is default:
    properties gui.button_properties("talkbutton_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    idle_background "gui/talk_button_idle.png"
    hover_background "gui/talk_button_hover.png"

style talkbutton_button_text is default:
    properties gui.button_text_properties("talkbutton_button")
    xalign 0.5

style talkbutton_button_text is button_text
define gui.distalkbutton_button_width = 120

screen distalkbutton():
    vbox:
        textbutton "nothing.png" action NullAction()

init python:
    def DisableTalk():
        
        
        if persistent.talk_visible == None:
            persistent.talk_visible = False
        try:
            config.overlay_screens.remove("talkbutton")
        except:
            pass
        renpy.hide_screen("talkbutton")
        persistent.talk_visible = False
    def EnableTalk():
        
        
        if persistent.talk_visible == True:
            persistent.talk_visible = True
        if not persistent.talk_visible:
            config.overlay_screens.append("talkbutton")
            renpy.show_screen("talkbutton")
        else:
            pass
        persistent.talk_visible = True
    def ShowTalk():
        if persistent.talk_visible == None:
            persistent.talk_visible = True
        try:
            config.overlay_screens.append("untalkbutton")
            renpy.show_screen("untalkbutton")
        except:
            pass
        persistent.talk_visible = True
    def HideTalk():
        if persistent.talk_visible == True:
            persistent.talk_visible = False
        try:
            config.overlay_screens.remove("untalkbutton")
        except:
            pass
        renpy.hide_screen("untalkbutton")
        persistent.talk_visible = False


label prompt_menu:


    python:
        allow_dialogue = False
        DisableTalk()
        boopable = False

        talk_menu = []
        if dev_access:
            talk_menu.append((_("Panel de Control."), "renpy.jump(\"control_panel\")"))
        talk_menu.append((_("Haz una pregunta."), "call_dialogue(\"pool\", \"actives\")"))
        if "last_compliment_time" in persistent.memory:
            if (datetime.datetime.now() - persistent.memory["last_compliment_time"]) >= datetime.timedelta(seconds = 900): 
                talk_menu.append((_("Cumplido."), "renpy.jump(\"compliment_menu\")"))
                talk_menu.append((_("Insultar."), "renpy.jump(\"insult_menu\")"))
            else:
                print_debug(datetime.datetime.now() - persistent.memory["last_compliment_time"])
        else:
            talk_menu.append((_("Cumplido."), "renpy.jump(\"compliment_menu\")"))
            talk_menu.append((_("Insultar."), "renpy.jump(\"insult_menu\")"))
        talk_menu.append((_("Dormir."), "renpy.jump('sleepy_yuri')"))

        talk_menu.append((_("Adiós."), "call_dialogue(\"pool\", \"farewells\")"))
        talk_menu.append((_("Olvídalo."),"renpy.jump('ch30_loop')"))

        randomnum = renpy.random.randint(0,6)
        ran_response = [
            _("Hmm, ¿qué pasa?"),
            _("¿Sí, " + str(player) + "?"),
            _("¿Sí, mi amor?"),
            _("Hola."),
            _("¿De qué te gustaría hablar?"),
            _("¿Sí, cariño?"),
            _("¿Hmm?")]
        renpy.say(y, ran_response[randomnum], interact=False)
        madechoice = renpy.display_menu(talk_menu)
        exec(madechoice)
    python:
        EnableTalk()
        renpy.jump("ch30_loop")



screen talkbutton():
    if not persistent.HDY and hide_yuri_sit==False:
        vbox xalign 0.03 yalign 0.1:
            style_prefix "talkbutton"
            textbutton "Sueños":
                action Call("talk_slow_no_dismiss", "dream_menu")




            if renpy.android:
                if persistent.lovecheck and persistent.bg != "laboratory":
                    textbutton "Citas":
                        action Call("talk_slow_no_dismiss", "dates_menu")
                textbutton "Música":
                    action Call("talk_slow_no_dismiss", "change_music")
            else:
                if persistent.lovecheck and persistent.bg != "laboratory":
                    textbutton "Citas":
                        action Call("talk_slow_no_dismiss", "dates_menu")
                textbutton "Música":
                    action Call("talk_slow_no_dismiss", "change_music")
                if renpy.seen_label("a_tetris"):
                    textbutton "Juegos":
                        action Call("talk_slow_no_dismiss", "games_menu")


        vbox xalign 0.50 yalign 0.99:
            style_prefix "talkbutton"
            textbutton "Hablar":
                action Call("talk_slow_no_dismiss", "prompt_menu")
    elif hide_yuri_sleep==True:
        $ allow_dialogue = False
        vbox xalign 0.97 yalign 0.99:
            style_prefix "talkbutton"
            textbutton "Despertar":
                action Call("yuriwakeup")

    else:
        vbox xalign 0.50 yalign 0.99:

            textbutton "Volver a Yuri":
                action Call("changeoutfit")



label games_menu:
    $ DisableTalk()
    $ Dream_type = "game"
    $ boopable = False
    $ show_chr("A-ABAAA-ALAL")
    y "¿Te apetece una partida, [player]?"
    $ show_chr("A-CCAAA-ALAL")
    y "Por favor, echa un vistazo a los juegos que tengo disponibles para nosotros actualmente. ¿Te parece atractivo alguno?"
    menu:
        "Tetris":
            jump tetris
        "Ajedrez":


            jump chess
        "Olvídalo":




            jump ch30_loop

screen untalkbutton():
    vbox xalign 0.03 yalign 0.1:
        style_prefix "talkbutton"
        textbutton "Sueños":
            action NullAction()




        if persistent.lovecheck:
            textbutton "Citas":
                action NullAction()
        textbutton "Música":
            action NullAction()

    vbox xalign 0.50 yalign 0.99:
        style_prefix "talkbutton"
        if persistent.alpha_save or renpy.seen_label("a_games") or renpy.seen_label("featuregreetings"):
            textbutton "juegos":
                action NullAction()
            null height 10



        textbutton "Hablar":
            action NullAction()

label talk_slow_no_dismiss(jumper):
    $ slow_nodismiss_copy()
    $ renpy.jump(jumper)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
