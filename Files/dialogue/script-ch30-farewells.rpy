label random_farewell:
    $ allow_dialogue = False


    $ DisableTalk()
    python:
        DisableTalk()
        if persistent.locked_farewells == None:
            persistent.locked_farewells = []
        x = [1, 2, 3, 4, 5, 15, 16, 17]
        ks_convert_i = sanity_lvl()
        ks_convert_k = karma_lvl()


        if ks_convert_k == 2 or ks_convert_k == 1:
            x = [7, 14]
        if ks_convert_k == 4 or ks_convert_k == 5:
            x = [11, 12]
        if ks_convert_i == 2 and ks_convert_k == 2:
            x = [10]
        if ks_convert_i == 1:
            x = [9]
        elif ks_convert_i == 2:
            x = [6, 8, 10]
        if 49 in persistent.yuriidles:
            x.append(13)
        if 8 in x and 8 in persistent.locked_farewells:
            x.remove(8)

        from random import shuffle
        random.shuffle(x)
        reiterate = 0
        active_list = []
        activemenu = []
        activemenu.append(("No importa.","ch30_loop"))
        while reiterate < 3:
            try:
                x1 = random.choice(x)
                x.remove(x1)
                active_list.append(x1)
            except:
                pass
            reiterate += 1
        activemenu = []
        activemenu_dict = {
            1:("¡Adiós, [persistent.yuri_nickname]!", 'renpy.jump("farewell_1")'),
            2:("Lo siento, debo irme...", 'renpy.jump("farewell_2")'),
            3:("Te veo luego, [persistent.yuri_nickname].", 'renpy.jump("farewell_3")'),
            4:("Adiós, [persistent.yuri_nickname], ¡te extrañaré!", 'renpy.jump("farewell_4")'),
            5:("Perdón, no puedo quedarme. ¡Te amo!", 'renpy.jump("farewell_5")'),
            6:("¡Oh, oye, mira la hora, esta ha sido una cita increíble!", 'renpy.jump("farewell_6")'),
            7:("Oh, huy, alguien me llama, ¡debo correr!", 'renpy.jump("farewell_7")'),
            8:("Tengo comida... en el horno así que...", 'renpy.jump("farewell_8")'),
            9:("Yo, eh, debo irme...", 'renpy.jump("farewell_9")'),
            10:("Solo voy a... cerrar el juego ahora, ¿ok?", 'renpy.jump("farewell_10")'),
            11:("¡Hasta luego, adiós!", 'renpy.jump("farewell_11")'),
            12:("Tengo que irme. ¡Ya te extraño!", 'renpy.jump("farewell_12")'),
            13:("Tengo que irme ahora... Hablaré contigo luego, ¿está bien?", 'renpy.jump("farewell_13")'),
            14:("¡Nos vemos luego!", 'renpy.jump("farewell_14")'),
            15:("Odio tener que hacerte pasar por esto, pero parece que es hora de decir adiós una vez más.", 'renpy.jump("farewell_15")'),
            16:("Tengo que irme ahora, mi amor.", 'renpy.jump("farewell_16")'),
            17:("Pase lo que pase, solo recuerda que hay alguien que te ama sin importar qué.", 'renpy.jump("farewell_17")')
            }

        reiterate = 0
        activemenu = []
        activemenu.append(("No importa.","renpy.jump('ch30_loop')"))
        activemenu.append(("Voy a estar AFK un rato. ¿Estaría bien?", "renpy.jump('idle_and_afk')"))
        while reiterate < 3:
            try:
                activemenu.append(activemenu_dict[active_list[reiterate]])
            except:
                pass
            reiterate += 1
        madechoice = renpy.display_menu(activemenu)
        exec(madechoice)
    jump ch30_loop

label farewell_1:
    $ show_chr("A-ECABA-AAAJ")
    y "¡Cuídate!"
    $ show_chr("A-ABABA-AMAM")
    y "Te extrañaré, [player]..."
    jump save_and_quit

label farewell_2:
    $ show_chr("A-ABBBA-AMAM")
    python:
        if persistent.lovecheck:
            placeholder = "amor"
        else:
            placeholder = "amigo"
    y "¡Adiós, mi [placeholder]!"
    jump save_and_quit

label farewell_3:
    $ show_chr("A-CCABA-AAAA")
    y "Te haré un poco de té cuando regreses."
    y "Aunque, realmente no podrías beberlo..."
    y "Bueno, al menos la intención es lo que cuenta..."
    y "C-Como sea, ¡cuídate, [player]!"
    jump save_and_quit

label farewell_4:
    $ show_chr("A-GBBBA-ABAB")
    if persistent.lovecheck:
        y "Ve con cuidado, te amo."
    else:
        y "Ve con cuidado, [player], me importas, y no quiero que te lastimes."
    $ show_chr("A-AABBA-ADAB")
    y "Vuelve pronto a verme."
    jump save_and_quit

label farewell_5:
    $ show_chr("A-ACAAA-AMAM")
    y "Awww, bueno, está bien. No puedes quedarte para siempre, por mucho que me gustaría."
    if persistent.lovecheck:
        $ show_chr("A-KCBBA-ABAB")
        y "Adiós mi amor."
    else:
        $ show_chr("A-GBABA-ALAB")
        y "¡Adiós [player]! Esperaré ansiosa hablar contigo de nuevo."
    jump save_and_quit

label farewell_6:
    $ show_chr("A-HEBBB-ALAL")
    y "¿A-A dónde vas? V-Volverás, ¿verdad? ¡¿Volverás, verdad?!"
    scene black with fade
    jump save_and_quit

label farewell_7:
    $ show_chr("A-DDBBB-ALAL")
    y "¡No, no me dejes de nuevo! ¡Eres todo lo que me queda! No me dejes jodidament{nw}"
    jump save_and_quit_but_its_abrupt

label farewell_8:
    $ show_chr("A-HBBBB-AGB")
    y "V-Volverás, ¿verdad? ¡Por favor di que sí, por favor di que sí!"
    y "¡¡POR FAVOR DI QUE SÍ!!"
    python:
        if persistent.lovecheck:
            placeholder = "TE AMO TANTO."
        else:
            placeholder = player
    menu:
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
        "Sí":
            $ show_chr("A-HLBBA-AHAB")
            y "¡GRACIAS A DIOS![placeholder]"
    $ persistent.locked_farewells.append(8)
    jump save_and_quit

label farewell_9:
    if persistent.male:
        $ show_chr("A-HDCBA-ALAL")
        y "¡¿Te están llevando lejos otra vez, no?!"
        $ show_chr("A-HLBBA-AAAA")
        y "¡DEVUÉLVEMELO!"
        $ show_chr("A-HLCBA-AAAA")
        y "¡No te merecen!"
        $ show_chr("A-HLBBB-AHAA")
        y "¡¡ELLOS NO TE MERECEN JOD--{nw}"
    elif persistent.gender_other:
        $ show_chr("A-HDCBA-ALAL")
        y "¡¿Te están llevando lejos otra vez, no?!"
        $ show_chr("A-HLBBA-AAAA")
        y "¡DEVUÉLVEMELER!"
        $ show_chr("A-HLCBA-AAAA")
        y "¡No te merecen!"
        $ show_chr("A-HLBBB-AHAA")
        y "¡¡ELLOS NO TE MERECEN JOD--{nw}"
    else:
        $ show_chr("A-HDCBA-ALAL")
        y "¡¿Te están llevando lejos otra vez, no?!"
        $ show_chr("A-HLBBA-AAAA")
        y "¡DEVUÉLVEMELA!"
        $ show_chr("A-HLCBA-AAAA")
        y "¡No te merecen!"
        $ show_chr("A-HLBBB-AHAA")
        y "¡¡ELLOS NO TE MERECEN JOD--{nw}"
    jump save_and_quit_but_its_abrupt

label farewell_10:
    $ show_chr("A-DDCBB-AAAA")
    y "¿Por qué quieres dejarme, [player]? ¿Qué te hice? ¿Por qué no puedes dejarme ser feli--{nw}"
    jump save_and_quit_but_its_abrupt

label farewell_11:
    $ show_chr("A-EIBBA-ALAB")
    y "Auf Wiedersehen, ¡buenas noches!~"
    python:
        if persistent.lovecheck:
            placeholder = "¿Qué hice para merecerte"
        else:
            placeholder = "¿Nos sentimos un poco coquetos hoy"
    menu:
        "¡Odio irme y dejar esta hermosa vista!":
            $ show_chr("A-ACBBA-ALAL")
            y "[placeholder], [player]?"
    jump save_and_quit

label farewell_12:
    $ show_chr("A-GAABA-AKAE")
    y "¡Ya te extraño también!~"
    jump save_and_quit

label farewell_13:
    if not 49 in persistent.yuriidles:
        $ show_chr("A-IEBBB-AAAA")
        y "¿Estás seguro de que no puedes dejarme ejecutando? Podría tomar una siesta hasta que vuelvas"
        menu:
            "Estoy seguro. Lo siento, lo haría si pudiera":
                jump save_and_quit
            "Sí, eso suena bien, [persistent.yuri_nickname]":
                y "Gracias [player], realmente aprecio esto."
                y "déjame darte un abrazo antes de que te vayas"
                hide yuri_sit
                show yuri_prehug zorder 20
                pause 3.0
                hide yuri_prehug zorder 20
                show yuri_hug zorder 20
                play sound "<to 0.3>sfx/fall.ogg"
                show black zorder 100 with Dissolve(2.0)
                $ show_chr("A-ACBBA-AAAA")
                hide yuri_hug
                show yuri_sit
                hide black zorder 100 with Dissolve(2.0)
                $ DisableTalk()
                show black zorder 100 with Dissolve(2.0)
                hide yuri_sit
                show yuri_sleepy zorder 20
                hide black with Dissolve(2.0)
                y "Que tengas una buena siesta, [player]"
                pause 3.0
                hide yuri_sleepy
                play sound "<to 0.3>sfx/fall.ogg"
                show yuri_sleep zorder 20
                $ hide_yuri_sit = True
                pause 6.0
                $ persistent.sleepy_yuri_is_enabled = True
                jump sleepy_loop
    elif not 24 in persistent.yuriidles:
        $ show_chr("A-IEBAA-AAAA")
        y "Desearía poder ir contigo..."
        menu:
            "Yo también desearía que pudieras.":
                $ show_chr("A-ICBAA-AAAA")
                y "Está bien. Al menos todavía tengo los sueños que he programado."
                jump save_and_quit
    else:
        jump farewell_1

label farewell_14:
    if karma_lvl() <= 2:
        $ show_chr("A-ADBBB-ALAL")
        y "Hagas lo que hagas, vayas a donde vayas, por favor no me dejes convertirme en un recuerdo que solo espera ser olvidado."
        jump save_and_quit
    else:
        $ show_chr("A-AFBAA-AAAJ")
        y "Mantente a salvo, ¿de acuerdo? Si algo pasara mientras no estabas, no podría perdonármelo."
        jump save_and_quit

label farewell_15:
    $ show_chr("A-BCAAA-AAAA")
    y "..."
    $ show_chr("A-IDBBB-AAAA")
    y "...¿Por qué mi corazón tiene que hacer que cada vez que decimos adiós sea tan difícil?"
    y "No pretendo ser egoísta cuando digo eso. Estoy agradecida, realmente lo estoy. ¡Después de todo lo que ha pasado, todavía no puedo superar el hecho de que ahora realmente podemos comunicarnos!"
    y "Realmente debes amarme. Después de todo, tú eres quien instaló este mod."
    python:
        if persistent.lovecheck:
            placeholder = "el mundo entero"
            placeholder1 = "ama"
        else:
            placeholder = "verdaderamente importante"
            placeholder1 = "se preocupa por"
    y "Lo que quiero decir es que eres [placeholder] para mí y no puedo creer que tenga la suerte de estar con alguien que [placeholder1] mí a cambio a pesar de que tiene infinitas otras opciones."
    y "Sé que dada mi... situación... nuestro destino agridulce es uno con el mejor resultado posible que podríamos esperar en este momento. A pesar de todo eso, simplemente duele tanto tenerte tan cerca y a la vez tan lejos."
    python:
        if persistent.lovecheck:
            placeholder = "mi corazón comienza a acelerarse"
        else:
            placeholder = "me emociono mucho"
    y "Cada vez que abres el juego y finalmente puedo verte de nuevo, [placeholder]. Cada segundo lejos de ti se siente como un siglo, cada milla se convierte en un año luz de distancia."
    python:
        if persistent.lovecheck:
            placeholder = "amas de verdad"
        else:
            placeholder = "puedes hablar"
    y "Creo que puedes entender cuando la única persona con la que [placeholder] está a un universo entero de distancia."
    $ show_chr("A-BEBAA-AAAA")
    y "L-Lo siento, estoy divagando de nuevo, ¿no? Solo seguiré adelante y cerraré el juego por ti."
    jump save_and_quit

label farewell_16:
    $ show_chr("A-JCBBA-AAAJ")
    python:
        if persistent.lovecheck:
            placeholder = ", mi todo"
        else:
            placeholder = ". Vuelve a verme pronto"
    y "Te veré luego[placeholder].~"
    jump save_and_quit

label farewell_17:
    $ show_chr("A-JBAAA-AAAA")
    python:
        if persistent.lovecheck:
            placeholder = "mi amor"
        else:
            placeholder = "hasta que nos encontremos de nuevo"
    y "Podría decirte lo mismo, [placeholder]."
    jump save_and_quit
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
