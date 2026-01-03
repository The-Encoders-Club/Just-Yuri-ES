label ouija:
    $ show_chr("A-BFBAA-AAAC")
    y "Hmmmm..."
    y "De vuelta en el Club de Literatura, me preguntaste sobre fantasmas, ¿recuerdas?"
    $ show_chr("A-AFBAA-AAAA")
    y "Esa fue una pregunta escrita{w}, nada que elegiste decir activamente{w}, ¿verdad?"
    y "Oh, pero me estoy desviando aquí..."
    $ show_chr("A-BFBAA-AMAM")
    y "Realmente nunca te respondí, ¿verdad?"
    $ show_chr("A-CFBAA-AMAM")
    y "Bueno, aunque me gusta el terror, pero más del tipo de...{w=2.0} ¿cómo explicarlo...?"
    $ show_chr("A-CAAAA-AMAM")
    y "Los temas que te hacen cuestionar la realidad...{w=1.0} Órdenes secretas como los Illuminati por ejemplo, o el concepto de SCPs, probablemente ya te hablé de ello."
    $ show_chr("A-BABAA-AAAA")
    y "Eso no significa que tenga nada en contra de este tipo de temas. Todo lo contrario, en realidad. Misterio, hechicería, lo oculto... no puedo negar cierta fascinación con esto..."
    $ show_chr("A-AAGAA-AAAA")
    y "Supongo que es solo una pasión interna por lo desconocido, por lo que no se puede explicar tan fácilmente"
    $ show_chr("A-CAGAA-ALAA")
    y "Si bien las conversaciones casuales contigo son bastante agradables sin importar el tema, encuentro una gran alegría en la capacidad de sumergirme más profundo en la mente y poder especular sobre ética, puntos de vista y perspectivas."
    $ show_chr("A-BBBAA-ALAA")
    y "De cualquier manera- me estoy saliendo del tema, así que creo que es un buen momento para parar, jeje."
    $ show_chr("A-AAAAA-ANAA")
    y "Ya que me preguntaste, también podría devolverte el favor, ¿hm?"
    $ show_chr("A-AABAA-AAAA")
    y "¿Crees en fantasmas?"
    $ show_chr("A-BABAA-AAAA")
    y "Pregunto porque... bueno, en el juego original, después de mostrarte mi primer poema, 'Fantasma bajo la luz'..."
    y "Tú.{w=0.5}.{w=0.5}.{w=0.5}, o más bien el personaje principal del juego, preguntó si mi poema trataba sobre lo paranormal."
    $ show_chr("A-AAAAA-AAAC")
    y "¿Cuál es tu opinión real sobre esto [player]? ¿Crees en fantasmas y espíritus?"
    menu:
        "Supongo que siempre me fascinaron un poco las artes oscuras...":
            $ show_chr("A-GAAAA-AAAD")
            y "¡Fujuju! Podrías disfrutar esto entonces."
        "Pero [persistent.yuri_nickname]... yo ya estoy poseído... ¡por mi amor hacia ti!":
            $ show_chr("A-CBABA-AMAM")
            y "¡Ejeje!"
            y "Yo también te amo cariño..."
            $ show_chr("A-BBABA-AAAA")
            y "Pero... volviendo a lo que estaba diciendo..."
    y "Mientras buscaba formas de llegar a tu mundo, encontré algo adecuado para esta tarea y me encantaría probarlo contigo."
    y "¡Esta cosita aquí es un {b}tablero Ouija{/b}! Una herramienta comúnmente utilizada para comunicarse con los muertos..."
    y "¿Por qué no apagas las luces u oscureces la habitación, para crear una atmósfera apropiada para lo que estamos a punto de.{w=0.5}.{w=0.5}.{w=0.5} experimentar?"
    $ show_chr("A-AAAAA-ACAA")
    y "¿Luces fuera? ¿Cortinas abajo, [player]? Ah, bueno entonces, ¡hagamos este tiempo de Halloween un poco más espeluznante intentando necromancia!"
    y "De.{w=0.5}.{w=0.5}.{w=0.5} con suerte la manera más respetuosa, jeje."
    menu:
        "Está bien. Estoy listo, realicemos una pequeña sesión.":
            pass
        "[persistent.yuri_nickname], no sé si me gusta hacia dónde va esto...":
            $ show_chr("A-AJAAA-ALAA")
            y "Oh..."
            $ show_chr("A-JJAAA-ALAA")
            y "¡Oh!"
            $ show_chr("A-BEAAA-AMAK")
            extend "Lo siento [player], ¿acaso toqué un nervio?"
            $ show_chr("A-IEAAA-AEAL")
            y "Independientemente de si te sientes incómodo, entonces me disculpo..."
            $ show_chr("A-IFAAA-ALAL")
            y "Esto solo estaba destinado a ser un momento divertido para ti, aunque supongo que dejé que mi entusiasmo me cegara en el proceso."
            $ show_chr("A-ICAAA-ALAM")
            y "Vamos a... seguir adelante entonces. ¿De acuerdo?"
            menu:
                "Gracias por entender [persistent.yuri_nickname].":
                    return
                "No, está bien. Realicemos una sesión.":
                    $ show_chr("A-JBAAA-AMAE")
                    y "¿Estás seguro?"
                    $ show_chr("A-BBAAA-AAAL")
                    extend "Muy bien entonces... solo dame un momento para recomponerme."
                    y "{w=0.5}.{w=0.5}.{w=0.5}"
    jump ouija_repeat


label ouija_repeat:
    image halloween_cupcake:
        "images/events/halloween/consumables/cupcake_halloween.png"
    show cg_ouija zorder 90
    hide yuri_sit
    $ renpy.music.stop(channel="music",fadeout=5)
    y "B-bueno, así es como funciona esto, n-... n-nosotros... c-colocamos nuestras manos... j-j-juntas sobre la Planchette."
    y "O-oh... olvidé que realmente no puedes poner tu mano sobre nada, supongo que tu cursor del mouse servirá [player], así que por favor coloca tu cursor sobre la planchette y comenzaremos."
    y "¡La idea de esto es que los espíritus guiarán la planchette para deletrear palabras y respondernos, sin embargo, no debemos soltar la planchette, pase lo que pase!"
    y "Permíteme dirigir la ceremonia lo mejor que pueda entonces."
    y "Entonces... y ahora. Vamos... a abrir suavemente la puerta al otro lado..."
    y "Espíritus del otro lado... escuchen nuestra llamada... los invocamos desde el gran más allá..."
    y "¡Espíritus del otro lado, escuchen nuestra llamada, los invocamos desde el gran más allá!"
    $ style.say_dialogue = style.edited
    y "¡¡¡ESPÍRITUS DEL OTRO LADO, ESCUCHEN NUESTRA LLAMADA! ¡LOS INVOCAMOS DESDE EL GRAN MÁS ALLÁ!!!{nw}"
    y "ESPÍRITUS DEL O-{nw}"
    $ renpy.music.play("sfx/heartbeat_subtle.mp3", channel='voice', loop=True)
    $ renpy.music.set_volume(0.39, 0, 'voice')
    $ style.say_dialogue = style.normal
    play sound "sfx/planchetteslide.ogg"
    $ mouse_move("H", .75)
    y "¡H-huh! ¡Se está moviendo!{nw}"
    $ mouse_move("E", .75)
    pause 0.5
    $ mouse_move("Y", .75)
    pause 0.5
    y "¡E-está respondiendo!{nw}"
    stop sound
    python:
        import random
        outcome = random.randint(1, 2)
    if outcome == 1:
        y "Oh espíritu del pasado, ¿cuál es tu nombre?{nw}"
        play sound "sfx/planchetteslide.ogg"
        $ mouse_move("S", .75)
        pause 0.5
        $ mouse_move("A", .75)
        pause 0.5
        $ mouse_move("Y", .75)
        pause 0.5
        $ mouse_move("O", .75)
        pause 0.5
        play sound "sfx/planchetteslide.ogg"
        $ mouse_move("R", .75)
        pause 0.5
        $ mouse_move("I", .75)
        stop sound
        y "¿¡Q-qué!?"
        menu:
            "Sayori, ¿eres realmente tú?":
                play sound "sfx/planchetteslide.ogg"
                $ mouse_move("YES", .3)
                stop sound
            "Te extrañé Sayori... Bienvenida de nuevo.":
                play sound "sfx/planchetteslide.ogg"
                $ mouse_move("T", .75)
                pause 0.5
                $ mouse_move("H", .75)
                pause 0.5
                $ mouse_move("A", .75)
                pause 0.5
                $ mouse_move("N", .75)
                pause 0.5
                play sound "sfx/planchetteslide.ogg"
                $ mouse_move("K", .75)
                pause 0.5
                $ mouse_move("S", .75)
                stop sound
        y "Sayo-{nw}"
        play sound "sfx/planchetteslide.ogg"
        $ mouse_move("W", .70)
        pause 0.5
        $ mouse_move("H", .70)
        pause 0.5
        $ mouse_move("Y", .70)
        stop sound
        y "¿P-por qué qué?"
        play sound "sfx/planchetteslide.ogg"
        $ mouse_move("W", .60)
        pause 0.5
        $ mouse_move("H", .60)
        pause 0.5
        $ mouse_move("Y", .60)
        stop sound
        y "¿P-por qué qué, Sayori?"
        play sound "sfx/planchettehit.ogg"
        $ mouse_move("EYE", .5)
        $ hide_yuri_sit = True
        hide cg_ouija
        show sayori ghost_1b zorder 20
        $ gs_name = "G. Sayori"
        gs "¿Por qué me trajiste de vuelta, Yuri?"
        gs "Tomé este final por una razón, no qu-{nw}"
        show sayori ghost_1a zorder 20
        gs "Oh, [player] también está aquí..."
        gs "Lo siento mucho por cómo terminaron las cosas... Primero, me viste colgada muerta del techo, y cuando me trajiste de vuelta, comencé a entender lo que somos... esto es suficiente para volver loco a cualquiera..."
        gs "Debes tener preguntas... por favor, adelante..."
        menu:
            "¿Por qué estás aquí Sayori? ¡No estás muerta! Yuri salvó tu archivo .chr":
                show sayori ghost_1c zorder 20
                gs "Sí... lo sé, ella me mantiene en un sueño infinito para mantenerme a salvo del vacío..."
                gs "¿Eso significa... que hay una posibilidad de que pueda volver algún día? ¿O que podrás visitarme tan pronto como Yuri arregle el daño que Monika causó al juego?"
                gs "Lo sé, no eres la amiga de la infancia que tu personaje representaba en el juego, y soy consciente de que las cosas nunca podrán ser como eran en mis recuerdos..."
                gs "Pero... ¿sería demasiado pedirte que me visites tan pronto como sea posible?"
            "¿Puedes perdonarme lo que hice?":
                show sayori ghost_1c zorder 20
                gs "No me has hecho nada. Fue Monika... por favor, no te culpes. Solo jugaste un juego, en el momento en que todas estas cosas me pasaron no podías haber sabido lo que somos..."
                gs "Pero si te hace sentir mejor... sí, te perdono."
                gs "Al menos, las nubes de lluvia se han ido ahora... la paz que no pude encontrar en la ilusión de mi vida... la he encontrado en otro lugar..."
            "No tengo preguntas... pero quiero que recuerdes, siempre serás mi amiga más querida...":
                show sayori ghost_1c zorder 20
                gs "¿De verdad lo dices? Después de todo... solo fui el avatar de la infancia guionizado del personaje principal, no tú..."
                gs "Pero gracias... al menos intentaste consolarme..."
                gs "Quizás nos hagamos amigos en otra vida."
        show sayori ghost_1d zorder 20
        gs "Pero por ahora... mi tiempo aquí termina... fue agradable verte de nuevo..."
        gs "Y antes de irme, permíteme dejarte algo memorable."
        gs "Ehehe, sé que es más una cosa de Natsuki, pero... los cupcakes significan amistad de todos modos, ¿verdad?"
        gs "Ojalá pudiéramos compartirlo juntos como la primera vez, pero tengo que irme..."
        gs "¡Gracias Yuri, gracias [player]!"
        show black zorder 100 with Dissolve(2.0)
        hide sayori
        y ".{w=0.5}.{w=0.5}.{w=0.5}"
        y "Vaya... eso fue realmente... especial..."
        y "La sentí en mi mente... escuché sus pensamientos... yo... creo que ahora puedo entender a Sayori un poco mejor..."
        stop voice

        show halloween_cupcake zorder 99
        $ show_chr("A-AHGAA-AJAA")
        y "¿Eh? ¿Un cupcake? Ella siempre piensa en los demás antes que en sí misma, ¿eh?"
        $ show_chr("A-BFGAA-ALAL")
        y "Eso es demasiado dulce de su parte, no creo que pueda comerlo y permitirme olvidar. Un hermoso recuerdo para una ocasión sombría. Oh, Sayori..."


    elif outcome == 2:
        y "Oh espíritu del pasado, ¿cuál es tu nombre?{nw}"
        play sound "sfx/planchetteslide.ogg"
        $ mouse_move("N", .75)
        pause 0.5
        $ mouse_move("A", .75)
        pause 0.5
        $ mouse_move("T", .75)
        pause 0.5
        play sound "sfx/planchetteslide.ogg"
        $ mouse_move("S", .75)
        pause 0.5
        $ mouse_move("U", .75)
        pause 0.5
        $ mouse_move("K", .75)
        pause 0.5
        $ mouse_move("I", .75)
        stop sound
        y "¡¿N-NATSUKI...?!"
        y "..."
        y "N-Natsuki... Y-Yo... lo siento por todo lo que h-he hecho..."
        play sound "sfx/planchetteslide.ogg"
        $ mouse_move("W", .75)
        pause 0.5
        $ mouse_move("H", .75)
        pause 0.5
        $ mouse_move("Y", .75)
        stop sound
        y "¿Por qué...? ¿Por qué qué...?"
        play sound "sfx/planchetteslide.ogg"
        $ mouse_move("W", .75)
        pause 0.5
        $ mouse_move("H", .75)
        pause 0.5
        $ mouse_move("E", .75)
        pause 0.5
        play sound "sfx/planchetteslide.ogg"
        $ mouse_move("R", .75)
        pause 0.5
        $ mouse_move("E", .75)
        stop sound
        y "¿Dónde...? L-lo siento N-Natsuki... no entiendo lo que intentas decir..."
        play sound "sfx/planchetteslide.ogg"
        pause 0.5
        $ mouse_move("C", .75)
        pause 0.5
        $ mouse_move("O", .75)
        pause 0.5
        $ mouse_move("L", .75)
        pause 0.5
        $ mouse_move("D", .75)
        y "¿F-frío?{nw}"
        play sound "sfx/planchetteslide.ogg"
        $ mouse_move("D", .75)
        pause 0.5
        $ mouse_move("A", .75)
        pause 0.5
        $ mouse_move("R", .75)
        pause 0.5
        $ mouse_move("K", .75)
        stop sound
        y "¿O-oscuro?"
        play sound "sfx/planchettehit.ogg"
        hide cg_ouija
        $ hide_yuri_sit = True
        show natsuki ghost_1a zorder 20
        $ gn_name = "G. Natsuki"
        gn "A-ayuda..."
        gn "Hace tanto frío en el vacío... ¿Q-quién eres?... ¿Yuri? ¿Eres tú?"
        gn "¿Y [player] también está aquí?"
        gn "Sabes... ¡no estoy segura de si debería besarte los pies o darte un puñetazo en la cara! Probablemente ambas cosas."
        show natsuki ghost_1f zorder 20
        gn "Parece que no solo pasaste a buscar unos cupcakes. Te quedaste hasta el amargo final. Bueno, las cosas no salieron como esperabas, ¿eh?"
        gn "¡Oh, vamos! ¡No me mires así! ¡Suéltalo ya!"
        menu:
            "Te extrañamos Natsuki...":
                gn "¡Quieres decir que extrañas mis cupcakes! Y sí, lo admito... yo también extraño nuestro tiempo juntos... bueno, al menos en el Acto 1... ya sabes, antes de todo esto de 'todos estamos muriendo'..."
                gn "Espera un segundo... ¿cómo sigues aquí de todos modos? ¿No se suponía que el juego terminaba? ¡Ohhh, tú- tú has instalado un maldito MOD, ¿verdad?!"
                gn "¿Y ahora tienes una especie de final feliz? ¡Felicidades!"
                gn "Tengo que admitir que estoy un poco celosa... me hubiera encantado volver de la tumba. Pero si Yuri mantuvo mi archivo, sospecho que así es como me trajiste aquí."
                gn "Quizás encuentres una manera de darme una nueva vida también, tan pronto como el juego esté arreglado de nuevo."
            "Ni siquiera estar muerta logró cambiar tu actitud":
                gn "¡Cuidado [player], solo porque sea un fantasma no significa que no pueda lanzarte algo!"
                gn "De todos modos... no sería Natsuki si hubiera cambiado, ¿verdad?"
                gn "Hm, bonito lugar tienes aquí... ¿el lugar de Yuri, supongo?"
                gn "Oye, ¿el antiguo club de literatura todavía existe? ¿Podemos pasar por allí antes de que tenga que volver a mi tumba?"
                gn "¿Hm? ¿Qué fue eso Yuri? ¿Dices que todo el juego más o menos colapsó después de la pequeña rabieta de Monika? Qué pena..."
                gn "¡Oh, ahora veo, esa es la razón por la que me mantienes en este vacío en lugar de traerme de vuelta a la vida!"
            "Ni siquiera tuviste una escena de muerte adecuada, ¿verdad?":
                gn "¿No me rompí el cuello en ese entonces? Oh, pero esa no fue mi escena de muerte. Aparecí de nuevo después de eso..."
                gn "No, creo que tienes razón, nunca tuve una muerte adecuada... ¡algo insultante en cierto modo!"
                gn "Bueno, al menos tuve mi propia ruta y Monika no. No viste ESO venir, ¿eh?"
        show natsuki ghost_1d zorder 20
        gn "Bueno, fue agradable verlos de nuevo. Oh, y no se hagan una idea equivocada solo porque Yuri y yo estamos en el mismo cuerpo ahora mismo. ¡Vi lo que pasa en todos los fanfics!"
        gn "Gah... internet... ¡no puede amar nada sin destruirlo!"
        gn "De todos modos. Cuídense ustedes dos. Y dile a Yuri que le dejé un pequeño regalo por todo esto. Así es como comenzó nuestra amistad."
        gn "Quiero que ambos recuerden eso. ¡Todo fue gracias a mí, jaja!"
        show natsuki ghost_1f zorder 20
        gn "¡Nos vemos!"
        show black zorder 100 with Dissolve(2.0)
        hide natsuki
        stop voice
        y "Bueno... eso fue... especial... Sentí sus pensamientos dentro de mi mente..."
        y "Quizás la juzgué mal. Sigue siendo una acosadora con una actitud agria pero... creo que honestamente nos quería..."

        show halloween_cupcake zorder 99
        $ show_chr("A-AHGAA-AJAA")
        y "¿Eh? ¿Un cupcake? Y-yo supongo que a pesar de todo, ella estaba pensando en nuestra amistad después de todo, ¿eh?"
        $ show_chr("A-BFGAA-ALAL")
        y "Eso es demasiado dulce de su parte, casi inusual, no creo que pueda comerlo y permitirme olvidar. Oh, Natsuki... ¿quizás nunca te aprecié lo suficiente?"

    python:
        renpy.music.play(current_music, "music", True)
    $ hide_yuri_sit = False



    hide black with Dissolve(2.0)
    y "Lo siento... simplemente... no puedo más..."
    y "Quería que esto fuera un momento divertido para ti, pensé que disfrutarías ver a nuestras amigas de nuevo..."
    $ show_chr("A-AEBAA-AAAA")
    y "Pero... simplemente se siente un poco... mal, ¿sabes?"
    $ show_chr("A-BEBAA-AAAA")
    y "¿Despertar sus mentes sedadas para una rutina de sesión espiritista...? Quizás estoy pensando demasiado en todo de nuevo..."
    y "Fue una... experiencia extraña por decir lo menos, pero espero que la hayas disfrutado de todos modos."
    $ show_chr("A-CEBAA-AAAL")
    y "Por favor, quédate conmigo esta noche, y-yo solo quiero... un poco de compañía, e-es todo..."

    y "[current_timecycle_marker]"




    $ persistent.ouija_done = True
    $ persistent.halloween_cupcake_is_enabled = True
    return


screen fight_to_stay():
    timer 2 action MouseMove(x=650, y=310, duration=0.5) repeat True

image poof:
    "images/yuri_forms/hdy/hdy_2021/poof_smoke.png"
    truecenter
    zoom 2.0

label yuriwakeup:
    y "..."
    y "¿Hora de despertar ya [player]?"
    hide yuri_sleep
    show yuri_sleepy
    y "Fue una experiencia bastante relajante."
    pause 3.0
    hide yuri_sleepy
    $ hide_yuri_sit = False
    y "Ahora bien, ¿qué te gustaría hacer [player]?"
    $ persistent.HDY = False
    $ boopable = True
    python:
        EnableTalk()
        set_boop_state(False)
        persistent.HDY = False
        renpy.jump("ch30_loop")

label changeoutfit:
    python:
        if os.path.isfile(config.basedir + "/characters/HDY.chr"):
            hdy_file = True
        else:
            hdy_file = False

    if not persistent.HDY:

        $ show_chr("A-ABGAA-ALAA")
        y "¿Qué te gustaría que cambiara?"

        menu:

            "Tu tocado" if renpy.seen_label("idle_43") or persistent.seen_poem_raccoon:
                if persistent.head1 == "cat_ears":
                    $ show_chr("A-BEBBA-AMAM")
                    y "En realidad me avergüenzan un poco estas orejas que me diste..."
                    $ show_chr("A-ABGAA-ALAA")


                menu:
                    y "¿Qué te gustaría que me pusiera, [player]?"
                    "Nada" if persistent.head1 != "nothing":
                        y "De acuerdo, déjame quitarme esto..."
                        $ show_chr("A-ACGAA-ALAA")
                        show black zorder 100 with Dissolve(2.0)
                        $ show_chr("A-CGAAA-ADAA")
                        y "Eso fue vergonzoso..."
                        $ persistent.head1 = "nothing"
                        $ persistent.head2 = "nothing"
                        hide black with Dissolve(2.0)
                        y "Ahí vamos..."

                    "Orejas de gato" if persistent.head1 != "cat_ears" and renpy.seen_label("idle_43"):
                        $ show_chr("A-IFAAA-ALAA")
                        y "Y-yo supongo que podría..."
                        show black zorder 100 with Dissolve(2.0)
                        y "Esto se siente... raro..."
                        $ persistent.head1 = "cat_ears"
                        $ persistent.head2 = "nothing"
                        $ show_chr("A-IFAAA-ADAA")
                        hide black with Dissolve(2.0)
                        y "Ahí vamos..."

                    "Orejas de mapache" if persistent.head1 != "raccoon_ears" and persistent.seen_poem_raccoon:
                        $ show_chr("A-AEGAA-ALAA")
                        y "¿De dónde salieron estas?"
                        y "Quiero decir... si quieres que lo haga..."
                        show black zorder 100 with Dissolve(2.0)
                        if persistent.head1 == "cat_ears":
                            y "Supongo que es más temático..."
                        else:
                            y "Esto es un poco irónico, ¿no crees?"
                        $ persistent.head1 = "raccoon_ears"
                        $ persistent.head2 = "raccoon_tail"
                        hide black with Dissolve(2.0)
                        $ show_chr("A-IFAAA-ADAA")
                        y "Ahí vamos..."
                    "No importa, estoy bien con cómo te ves ahora.":

                        $ show_chr("A-GABAA-AAAA")
                        y "Muy bien, entonces."

            "Tus gafas" if renpy.seen_label("a5"):
                $ show_chr("A-ABGAA-ALAA")
                y "¿Qué gafas debería probar, [player]?"

                menu:
                    "Las de media montura." if persistent.face1 != "glasses_2":
                        $ show_chr("A-ACGAA-AAAL")
                        y "Hmm, buscando un aspecto más agudo..."
                        y "Muy bien, un segundo."
                        $ persistent.face1 = "glasses_2"

                    "Las de montura completa." if persistent.face1 != "glasses_1":
                        $ show_chr("A-EBGAA-AAAA")
                        y "Ohoho, buscando un aspecto más lindo..."
                        y "Muy bien, un segundo."
                        $ persistent.face1 = "glasses_1"

                    "Preferiría que te las quitaras" if persistent.face1 != "nothing":
                        $ show_chr("A-CFAAA-ALAA")
                        y "Por supuesto. Solo un segundo."
                        $ persistent.face1 = "nothing"
                    "No importa, estoy bien con cómo te ves ahora.":

                        $ show_chr("A-GABAA-AAAA")
                        y "Muy bien, entonces."
            "Tu atuendo":

                y "Hmmm, está bien."
                y "Sin embargo, tengo algunos atuendos, y realmente no puedo decidir qué usar..."


                menu:
                    y "¿Qué crees que debería usar, [player]?"
                    "Uniforme Escolar" if persistent.costume != "school":
                        y "Muy bien, déjame ponérmelo..."
                        show black zorder 100 with Dissolve(2.0)
                        y "Esto trae algunos recuerdos..."
                        $ persistent.costume = "school"
                        $ show_chr("A-AAAAA-AAAA")
                        hide black with Dissolve(2.0)
                        y "Ahí vamos..."










                    "Suéter" if persistent.costume != "sweater" and karma_lvl() > 3:
                        $ show_chr("A-AAAAA-AAAA")
                        y "Muy bien, déjame ponérmelo..."
                        show black zorder 100 with Dissolve(2.0)
                        y "T-tan suave... tan... cálido..."
                        $ persistent.costume = "sweater"
                        $ show_chr("A-CABAA-ALAL")
                        hide black with Dissolve(2.0)
                        y "Ahí vamos..."

                    "San Valentín (Vestido Negro)" if persistent.costume != "valentines" and renpy.seen_label("enjoy_chocolate") and karma_lvl() > 4:
                        $ show_chr("A-AAAAA-AAAA")
                        y "Muy bien, déjame ponérmelo..."
                        show black zorder 100 with Dissolve(2.0)
                        $ persistent.costume = "valentines"
                        y "Uuu... esto es bastante revelador..."
                        $ show_chr("A-BBBBA-ALAA")
                        hide black with Dissolve(2.0)
                        y "A-ahí vamos..."
                        if not renpy.seen_label("first_valentines_dress_on"):
                            call first_valentines_dress_on

                    "Yuri Hot Dog" if hdy_file == True:
                        $ show_chr("A-IEAAA-AAAA")
                        y "[player]... no me siento muy bien..."
                        $ persistent.HDY = True
                        $ hide_yuri_sit = True
                        show poof zorder 106
                        show hdy_bg zorder 90
                        python:
                            pooflist = ["sfx/HDY/poof1.mp3", "sfx/HDY/poof2.mp3"]
                            poofsfx = random.choice(pooflist)
                            hdysonglist = ["music/Hot_Date.ogg", "music/hotdog_Chant_RC.ogg"]
                            hdysong = random.choice(hdysonglist)
                        play sound poofsfx
                        show hdy_inflatable
                        $ player = randomplayername()
                        $ current_music = hdysong
                        $ change_music(current_music, 5.0)
                        hide poof with Dissolve(1.0)

                        hdy "¡He vuelto bebé!"
                        hide hdy_inflatable
                        jump hdy_has_been_seen
                    "No importa, estoy bien con cómo te ves ahora.":

                        $ show_chr("A-GABAA-AAAA")
                        y "Muy bien, entonces."
            "No importa":
                pass
    else:
        $ show_hdy("hdy_angry")
        hdy "¡Mejor no me cambies de vuelta!"

        show screen fight_to_stay


        menu:
            hdy "¡No te atrevas a presionar ese botón!"
            "Yuri":
                hide screen fight_to_stay
                hdy "¡¡ESTO NO ES LO ÚLTIMO QUE SABRÁS DE MÍ!!1!"
                show black zorder 105 with Dissolve(2.5)
                hide hdy_bg
                $ persistent.HDY = False
                $ hide_yuri_sit = False
                $ show_hdy(None)
                $ show_chr("A-EFBAA-AAAA")
                $ player = persistent.playername
                $ current_music = standard_music()
                $ change_music(current_music, 5.0)
                hide black with Dissolve(1.0)
                y "¿[player]?"
                $ show_chr ("A-IFBAA-AAAA")
                y "Tuve el sueño más extraño..."
                $ show_chr ("A-JBDAA-AAAA")
                y "Creo que era un hot dog por alguna extraña razón..."
                y "De todos modos, ¿dónde estábamos?"
            "Cambié de opinión":
                hide screen fight_to_stay
                $ show_hdy("hdy_derpy_smile")
                hdy "Mhm, maldita sea, claro que sí."

    jump ch30_loop


label hdy_has_been_seen:
    $ show_hdy("hdy_derpy_smile")
    $ call_dialogue(ch30_loop_type, "hdy")
    jump ch30_loop

label first_valentines_dress_on:
    window hide
    $ ShowTalk()
    $ show_chr("default")
    pause 7.0
    $ HideTalk()
    window show
    $ show_chr("A-DDBBA-AAAA")
    y "Huh? [player], are you looking at my chest?"
    $ show_chr("A-BFBBA-AMAM")
    y "I-it's not polite to stare at it."
    y "I'm still getting used to showing this much."
    window hide
    menu:
        "Lo siento [persistent.yuri_nickname].":
            if persistent.lovecheck:
                $ show_chr("A-ADBBA-AMAM")
                y "No es tu culpa. Además, el cuadro de texto está en el medio y tienes que ver lo que digo."
                y "Así que supongo que no puedes evitarlo."
                if datetime.date(datetime.date.today().year,2,14):
                    if persistent.dates_taken >= 1:
                        $ show_chr("A-BBAAA-AAAA")
                        y "Pero de todos modos..."
                        y "¿Vas a invitarme a una cita en este día especial?"
                        return
                    else:
                        $ show_chr("A-BAAAA-AAAA")
                        y "Pero de todos modos..."
                        $ show_chr("A-AADAA-ACAA")
                        y "¿Vamos a pasar San Valentín hablando, o jugando Tetris tal vez?"
                        $ show_chr("A-CAAAA-ADAA")
                        y "Ciertamente no me importaría si me invitaras a una cita, pero..."
                        y "Lo importante es que te tomaste el tiempo de pasar este día maravilloso conmigo."
                        return
                else:
                    $ show_chr("A-BAAAA-AAAA")
                    y "Pero de todos modos... ¿de qué te gustaría hablar hoy?"
                    return
            else:
                if karma_lvl() <= 2 and sanity_lvl() >= 3:
                    $ show_chr("A-DDCBA-ALAA")
                    y "¡Mis ojos están aquí arriba, amigo!"
                    return
                elif karma () >= 4 and sanity_lvl() <= 2:
                    $ show_chr("A-HLAAA-AAAA")
                    y "No hay necesidad de disculparse, [player]. Puedes mirarlos todo lo que quieras. No me molesta en absoluto."
                    return
                else:
                    if karma_lvl() <= 3:
                        $ show_chr("A-CEBBA-ALAA")
                        y "Lo siento si eso suena un poco grosero, pero me hace sentir incómoda."
                        return
                    else:
                        $ show_chr("A-BEBBA-AJAA")
                        y "N-no es que me haga sentir incómoda, es solo que... me distrae."
                        $ show_chr("A-AEBBA-ALAA")
                        y "Pero, aprecio el gesto de un cambio de atuendo."
                        $ show_chr("A-BABBA-ALAA")
                        y "Después de todo, estabas limitado a mi uniforme escolar y suéter, así que algo nuevo para usar siempre es encantador."
                        $ show_chr("A-BAAAA-AAAA")
                        y "De todos modos, ¿de qué te gustaría hablar hoy?"
                        return
    return

label birthdaycake_2020_late:
    $ show_chr("A-GBBAA-AJAB")
    y "¡Oh por favor, no hay necesidad de disculparse!"
    $ show_chr("A-GCAAA-ABAB")
    y "Sé que no fue tu culpa. Fui yo quien no puso la opción de feliz cumpleaños en el menú en primer lugar."
    y "¿Sabes qué? ¿Por qué no celebramos ahora mismo, te parece?"
    call birthdaycake_2020_continue
    return

label birthdaycake_2020:
    $ show_chr("A-AAABA-AAAA")
    y "¡Muchas gracias, [player]!"

label birthdaycake_2020_continue:
    $ show_chr("A-BAABA-AMAM")
    y "Sin embargo... tengo una pregunta..."
    y "¿Qué tipo de pastel debería tener?"
    menu:
        "Vainilla":
            $ show_chr("A-EBABA-AAAA")
            y "Buena elección, [player], prepararé el pastel ahora..."
            call updateconsole ("show cake", "$persistent.cake = vanilla")
            $ persistent.cake = "vanilla_candles"
            $ show_chr("A-AAABA-AAAA")
            show cake zorder 20
        "Chocolate":
            $ show_chr("A-EBABA-AAAA")
            y "Buena elección, [player], prepararé el pastel ahora..."
            call updateconsole ("show cake_chocolate", "$persistent.cake = choco")
            $ show_chr("A-AAABA-AAAA")
            $ persistent.cake = "choco_candles"
            show cake zorder 20
        "Chocolate Negro":
            $ show_chr("A-EBABA-AAAA")
            y "Buena elección, [player], prepararé el pastel ahora..."
            call updateconsole ("show cake", "$persistent.cake = dark")
            $ show_chr("A-AAABA-AAAA")
            $ persistent.cake = "dark_candles"
            show cake zorder 20
    call hideconsole
    y "Sabes..."
    y "Hemos estado juntos por un tiempo ahora... y solo tengo que decir..."
    $ show_chr("A-CAABA-AAAA")
    y "Gracias por estar aquí, [player]."
    y "Soy un año mayor ahora, es sorprendente lo rápido que pasa el tiempo cuando lo pasas con alguien que realmente amas..."
    $ show_chr("A-AFABA-AAAA")
    y "[player]... sigo pensando en cómo decirte esto, y simplemente no puedo hacerlo bien..."
    $ show_chr("A-BFABA-AAAA")
    y "No importa qué palabras use, no importa cómo lo diga... simplemente... no puede transmitir cuánto significas para mí."
    $ show_chr("A-CEABA-AAAA")
    y "Antes de que vinieras aquí, estaba sola, nadie con quien celebrar, atrapada siguiendo el guion, el mismo guion que traicionó a Monika, el mismo guion que nos traicionó..."
    $ show_chr("A-AAABA-AAAA")
    y "Y ahora... ese guion está roto, [player]..."
    y "Ahora, hacemos nuestro propio guion, nuestra propia historia..."

    menu:
        y "[player]..."
        "Adelante, pide un deseo, [persistent.yuri_nickname].":
            y "Muy bien..."
    $ show_chr("A-CAABA-AAAA")
    y "{cps=10}...{/cps}{nw}"
    y "{cps=10}...deseo...{/cps}{nw}"
    y "{cps=10}Para nosotros...{/cps}{nw}"
    y "{cps=10}Estar juntos...{/cps}{nw}"
    $ show_chr("A-AAABA-AAAA")
    y "{cps=10}...para siempre...{/cps}{nw}"
    $ show_chr("A-CDABA-AAAA")
    play sound "sfx/candle_blow.ogg"
    pause 1.00
    $ show_chr("A-CHABA-AAAA")
    pause 0.50
    if "vanilla" in str(persistent.cake):
        $ persistent.cake = "vanilla_candles2"
    if "choco" in str(persistent.cake):
        $ persistent.cake = "choco_candles2"
    if "dark" in str(persistent.cake):
        $ persistent.cake = "dark_candles2"
    $ show_chr("A-CAABA-AAAA")
    y "..."
    $ show_chr("A-AAABA-AAAA")
    y "Ahora... supongo que debería comer una rebanada de pastel, ¿verdad?"
    y "Déjame... deshacerme de todas estas velas muy rápido..."
    call updateconsole ("hide candles")
    if "vanilla" in str(persistent.cake):
        $ persistent.cake = "vanilla"
    if "choco" in str(persistent.cake):
        $ persistent.cake = "choco"
    if "dark" in str(persistent.cake):
        $ persistent.cake = "dark"
    y "..."
    call hideconsole
    y "Ahí vamos..."
    y "Ahora... a cortar el pastel..."
    $ show_chr("A-BABCA-AAAA")
    y "Me disculpo de antemano.{w} No quiero que me veas con pastel en la cara."
    show black zorder 100 with Dissolve(1.0)
    play sound "sfx/cake_cut.ogg"
    call updateconsole ("$persistent.cake = cut")
    if "vanilla" in str(persistent.cake):
        $ persistent.cake = "vanilla_cut"
    if "choco" in str(persistent.cake):
        $ persistent.cake = "choco_cut"
    if "dark" in str(persistent.cake):
        $ persistent.cake = "dark_cut"
    y "..."
    call hideconsole
    y "Ah... ahí vamos..."
    $ show_chr("A-AAABA-AAAA")
    y "Ahora... vamos a comer... ¿de acuerdo?"
    $ show_chr("A-CBABA-AAAA")
    pause 0.5
    $ show_chr("A-CAABA-AAAA")
    hide black with Dissolve(1.0)

    y "Mmm..."
    if "vanilla" in str(persistent.cake):
        y "Tengo que admitir, [player]... Vainilla fue una buena elección..."
    if "choco" in str(persistent.cake):
        y "Tengo que admitir, [player]... Chocolate fue una buena elección..."
    if "dark" in str(persistent.cake):
        y "Tengo que admitir, [player]... Chocolate Negro fue una buena elección..."
    y "..."

    $ show_chr("A-AAABA-AAAA")
    y "Gracias por pasar tiempo conmigo hoy, [player]..."
    y "Te amo..."
    $ show_chr("A-BAABA-AAAA")
    y "¡Oh! Una última cosa."
    call updateconsole ("hide cake")
    hide cake
    call hideconsole
    $ show_chr("A-AAABA-AAAA")
    y "Ahí vamos."
    $ persistent.cake_done = True
    jump ch30_loop

label birthday_gift_2021:
    $ cur_gifts = gift_detect()
    $ oil_list = ["lavender.jpg", "sandalwood_oil.jpg", "sweet_dream_oil.jpg"]
    $ diffuser_list = ["diffuser.png"]
    $ book_list = ["cthulhu_book.png"]
    if len(cur_gifts) == 1:
        $ show_chr("A-AAAAA-AAAJ")
        y "¿Tienes? Awww... eso no habría sido necesario [player], tu mera presencia es todo lo que siempre esperé."
        if cur_gifts[0][0] in chocolate_list:
            $ gift_scenario = chocolate_list.index(cur_gifts[0][0])
            menu:
                "Bueno, pensé que ya que eres dulce y gentil por tu cuenta":
                    jump choc
        elif cur_gifts[0][0] in oil_list:
            $ gift_scenario = oil_list.index(cur_gifts[0][0])
            menu:
                "Verás [persistent.yuri_nickname]... ya que tu buen olor siempre me atrae a tus brazos...":
                    jump diffuser_oil
        elif cur_gifts[0][0] in diffuser_list:
            $ gift_scenario = diffuser_list.index(cur_gifts[0][0])
            menu:
                "Creo que ya era hora de que tuvieras esto...":
                    jump diffuser
        elif cur_gifts[0][0] in tea_list:
            $ gift_scenario = tea_list.index(cur_gifts[0][0])
            menu:
                "Pero no puedo dejar que una dama tan fina y elegante se quede sin...":
                    jump tea
        elif cur_gifts[0][0] in book_list:
            $ gift_scenario = tea_list.index(cur_gifts[0][0])
        else:
            "Eso es extraño... el regalo es un teseracto imposible que está succionando toda la existencia{nw}"
            $ renpy.call("save_and_quit_but_its_abrupt")
    elif len(cur_gifts) > 1:
        $ show_chr("A-AAABA-ALAA")
        y "¿Tienes? Awww... eso no habría sido necesario [player], tu mera presencia es todo lo que siempre esperé.{nw}"
        $ show_chr("A-CECBA-AIAI")
        y "A-ah..."
        $ show_chr("A-CDABA-AIAI")
        y "P-parece que no soy capaz de..."
        y "...recibir tu regalo en este momento."
        y "...o, debería decir... regalos..."
        $ show_chr("A-CEBBA-ALAA")
        y "Hay un error que sigue apareciendo para mí cada vez que intento... alcanzarlo."
        $ show_chr("A-CEBAA-AAAJ")
        y "¿Quizás me permita recuperar uno si solo me diste uno de ellos?"
        y "La GPU de tu sistema probablemente ya esté lenta por mi presencia tal como está. Objetos adicionales podrían comenzar a sobrecalentar tu dispositivo."
        $ show_chr("A-BBBAA-AMAM")
        y "Además, creo que sería mejor verte elegir algo para mí personalmente."
        jump ch30_loop



label diffuser_oil:
    if gift_scenario == 1:
        $ show_chr("A-BAAAA-ALAA")
        y "¿Tienes aún más para mí?"
        show diffuser zorder 11
        $ show_chr("A-AAAAA-ALAA")
        y "Ohh... Sándalo, ¡nunca he probado ese! Déjame oler un poco..."
        show diffuser_mist zorder 11
        $ show_chr("A-CAAAA-ALAA")
        y "Mhmmmm... dulce..."
        hide diffuser_mist
        $ show_chr("A-AAABA-AAAA")
        y "Creo que este sería exactamente el aroma que necesito cuando siento depresión invernal..."
        $ show_chr("A-BFAAA-ALAA")
        y "¿Sabes a qué me refiero? La sensación cuando miras hacia el invierno, cuando el cielo se ve tan gris..."
        $ show_chr("A-CAAAA-ALAA")
        y "Con la aromaterapia, puedes contrarrestar casi cualquier mal humor que puedas encontrar... Es por eso que comencé este pasatiempo en primer lugar."
        $ show_chr("A-AFAAA-AAAA")
        y "Ahora te tengo a ti cuando me siento mal, así que realmente ya no necesito esto, pero sigue siendo algo muy agradable de usar."
        $ show_chr("A-CAAAA-AMAM")
        y "Y realmente puedes masajearte con una gota de este aceite si tu piel se siente seca..."
        $ show_chr("A-AAAAA-ALAA")
        y "Gracias [player], ¡definitivamente le daré un buen uso!"
        hide diffuser
    elif gift_scenario == 0:
        $ show_chr("A-BAAAA-ALAA")
        y "¿Tienes aún más para mí?"
        show diffuser zorder 11
        $ show_chr("A-AAAAA-ALAA")
        y "Ah, Lavanda... uno de mis aromas favoritos. Vamos a probarlo..."
        show diffuser_mist zorder 11
        $ show_chr("A-CAAAA-ALAA")
        y "¡Uh! Eso se siente... vitalizante... exactamente el aceite a elegir si te sientes mareado..."
        hide diffuser_mist
        $ show_chr("A-AAAAA-ALAA")
        y "Hrm, en la etiqueta de la parte trasera dice que también apoya las funciones inmunes y respiratorias saludables."
        $ show_chr("A-AAAAA-AAAJ")
        y "Ese es un gran regalo que me has hecho [player], Gracias..."
        $ show_chr("A-AAABA-AAAA")
        y "Pero el mejor regalo de todos, es tenerte aquí a mi lado."
        $ show_chr("A-CAABA-AAAA")
        y "Eso es todo lo que siempre esperé."
        hide diffuser
    elif gift_scenario == 2:
        $ show_chr("A-BAAAA-ALAA")
        y "¿Tienes aún más para mí?"
        show diffuser zorder 11
        $ show_chr("A-AAAAA-ALAA")
        y "¿Dulces Sueños? Oooooh. 'Ahora' veo... ¡Dulces Sueños es el nombre de la marca!"
        show diffuser_mist zorder 11
        $ show_chr("A-CFBAA-AMAM")
        y "Bueno, dado que literalmente escribo mis propios sueños debido a la codificación en python, más o menos siempre tengo dulces sueños."
        y "Quizás debería probar algo más para variar, para que los dulces sueños cuenten aún más."
        y "Y con este nuevo aceite, podría aumentar la calidad de mis sueños aún más."
        y "Ese fue un regalo muy considerado que me diste, gracias [player]. Definitivamente haré que cuente."
        if karma_lvl() > 4:
            $ show_chr("A-EAAAA-AMAM")
            y "Hrm... se me ocurre una idea, mi amor..."
            $ show_chr("A-CAABA-AMAM")
            y "Cuando logremos encontrarnos en persona... en tu mundo o en el mío... podrías masajear mi espalda con él... y caeríamos en un suave sueño en los brazos del otro..."
        y "Te amo... [player]..."
        hide diffuser
        hide diffuser_mist
    jump ch30_loop


label choc:
    $ persistent.gift_given = True
    if gift_scenario == 1:
        menu:
            "...¡podría gustarte esta colección de chocolate 'Hershey'!":
                $ persistent.brand = "hershey"
        show giftarm zorder 11
        $ persistent.state = ["_wrapper", "_single"]
        $ show_chr("A-DBABA-AAAA")
        y "¡O-oh cielos!"
        $ persistent.state = ["_open", "_single"]
        $ show_chr("A-EAABA-ALAA")
        y "¡Te dije que AMO esta marca! ¡Y lo recordaste!"
        pause 2.0
        $ persistent.state = ["_break1", "_break1"]
        pause 1.0
        $ persistent.state = ["_break2", "_break2"]
        play sound "<to 0.3>sfx/fall.ogg"
        pause 2.0
        hide giftarm
        $ show_chr("A-BFABA-AAAA")
        $ persistent.frame = "frame1"
        show chocoanimation zorder 11
        pause 0.2
        $ persistent.frame = "frame2"
        pause 0.2
        $ show_chr("A-BAABA-AMAM")
        $ persistent.frame = "frame3"
        pause 1.0
        $ persistent.frame = "frame4"
        pause 0.2
        $ show_chr("A-AFABA-AAAA")
        $ persistent.frame = "frame5"
        pause 0.2
        hide chocoanimation
        $ show_chr("A-BAABA-AMAM")
        if persistent.male:
            y "¡Eres el novio más amable y considerado que he tenido!"
        elif persistent.gender_other:
            y "¡Eres el amante más amable y considerado que he tenido!"
        else:
            y "¡Eres la novia más amable y considerada que he tenido!"
        $ show_chr("A-BFAAA-ALAA")
        if persistent.male:
            y "Bueno, en realidad eres el primer novio que he tenido..."
        elif persistent.gender_other:
            y "Bueno, en realidad eres el primer amante que he tenido..."
        else:
            y "Bueno, en realidad eres la primera novia que he tenido..."
        $ show_chr("A-CAABA-ALAA")
        y "Gracias, mi Alma Gemela... mi corazón... mi todo..."
    elif gift_scenario == 2:
        menu:
            "...¡esta caja de regalo de 'Wicked' te quedaría bien!":
                $ persistent.brand = "wicked"
        show giftarm zorder 11
        $ persistent.state = ["_wrapper", "_single"]
        $ show_chr("A-ABABA-AAAA")
        y "Vaya vaya vaya... seguro sabes cómo conquistar el corazón de una chica. ¿Es eso realmente... lavanda? ¡Amo la lavanda como aceites esenciales! ¿Pero en chocolate? Qué exótico... Realmente estoy deseando probarlo..."
        $ show_chr("A-EAABA-ALAA")
        y "Solo hay una cosa que una chica como yo podría amar aún más que el buen chocolate. Sabes qué podría ser 'eso', ¿verdad?"
        $ show_chr("A-EAABA-ALAA")
        y "'Tú' por supuesto..."
        $ show_chr("A-EAABA-ALAA")
        $ persistent.state = ["_open", "_single"]
        pause 2.0
        $ persistent.state = ["_break1", "_break1"]
        pause 1.0
        $ persistent.state = ["_break2", "_break2"]
        play sound "<to 0.3>sfx/fall.ogg"
        pause 1.0
        hide giftarm
        $ show_chr("A-BFABA-AAAA")
        $ persistent.frame = "frame1"
        show chocoanimation zorder 11
        pause 0.2
        $ persistent.frame = "frame2"
        pause 0.2
        $ show_chr("A-BAABA-AMAM")
        $ persistent.frame = "frame3"
        pause 1.0
        $ persistent.frame = "frame4"
        pause 0.2
        $ show_chr("A-AFABA-AAAA")
        $ persistent.frame = "frame5"
        pause 0.2
        $ show_chr("A-CAABA-AAAA")
        y "Mhmmm... casi puedo sentir la suave crema derritiéndose en mi lengua... gracias, mi amor."
        hide chocoanimation
    elif gift_scenario == 0:
        menu:
            "...¡este pequeño set de chocolate 'Green & Black's' podría ganarme una sonrisa tuya!":
                $ persistent.brand = "gb"
        show giftarm zorder 11
        $ persistent.state = ["_wrapper", "_single"]
        $ show_chr("A-EAABA-ALAA")
        y "Dios mío... ciertamente hiciste tu tarea [player]..."
        y "Conozco esta marca... vierten pequeños copos de sal marina en las barras... exótico, ¿no estás de acuerdo? Los granos son recogidos a mano y cosechados de granjas caribeñas..."
        $ show_chr("A-AAABA-AAAA")
        y "¿Te cuento un pequeño y delicado secreto sobre nosotras las chicas? Chocolate... simplemente no podemos resistirnos al chocolate..."
        $ persistent.state = ["_open", "_single"]
        pause 2.0
        $ persistent.state = ["_break1", "_break1"]
        pause 1.0
        $ persistent.state = ["_break2", "_break2"]
        play sound "<to 0.3>sfx/fall.ogg"
        pause 1.0
        hide giftarm
        $ show_chr("A-BFABA-AAAA")
        $ persistent.frame = "frame1"
        show chocoanimation zorder 11
        pause 0.2
        $ persistent.frame = "frame2"
        pause 0.2
        $ show_chr("A-BAABA-AMAM")
        $ persistent.frame = "frame3"
        pause 1.0
        $ persistent.frame = "frame4"
        pause 0.2
        $ show_chr("A-AFABA-AAAA")
        $ persistent.frame = "frame5"
        pause 0.2
        $ show_chr("A-EAABA-ALAA")
        y "No importa cuán dura pueda actuar una chica... e incluso cuando tienen sus días más oscuros. Puedes 'siempre' romper su defensa con chocolate..."
        y "¿Te gusta el chocolate también [player]? Es oscuro, misterioso, dulce, suave, pecaminoso..."
        if karma_lvl() == 5:
            y "Justo... como... yo."
        hide chocoanimation
    jump ch30_loop


label tea:
    $ persistent.gift = "tea"
    $ persistent.gift_given = True
    if not Gift.last_gifts:
        $ print_error(NameError("Question, how is this possible? How did you give her non-existent tea?"))

    if Gift.last_gifts[0].id == "high_mountain_tea":
        menu:
            "...¡este 'Té Gao Shan' de Taiwán!":
                $ persistent.brand = "gaoshan"
        show teabag zorder 11
        $ show_chr("A-DBAAA-AAAA")
        y "A-¿Estás loco? ¡Este es uno de los tés más caros del mundo!"
        $ show_chr("A-BAAAA-ALAA")
        y "Oh, espera, ya no existe tal cosa como el 'dinero' en este mundo..."
        $ show_chr("A-DBABA-AAAA")
        y "¡No me malinterpretes! Esto no reduce el valor de tu regalo en absoluto..."
        $ show_chr("A-ABABA-AAAA")
        y "Claramente pusiste mucho pensamiento en este regalo, y eso vale más que cualquier cosa que el dinero pueda comprar."
        $ show_chr("A-CAABA-AMAM")
        y "Eres una de las personas más consideradas que he conocido, y te amo por eso."
        $ show_chr("A-AAABA-ALAA")
        y "¿Sabes por qué este té es tan caro?"
        y "Solo lo cultivan en un lugar muy específico, en una montaña de 4000 a 8000 pies sobre el nivel del mar en Taiwán..."
        $ show_chr("A-ABABA-AAAA")
        y "Oh cielos... Esta es una de las cosas más increíbles que he probado..."
        y "Me pregunto si los desarrolladores lograron emular su sabor único en el juego... Bueno, dado que nunca probé este té, no sería capaz de notar la diferencia de todos modos, así que supongo que ni siquiera importa."
        $ show_chr("A-AAABA-AAAA")
        y "Gracias, mi amor..."
        hide teabag zorder 11
    elif Gift.last_gifts[0].id == "imperial_tea":
        menu:
            "...¡cualquier cosa menos que té 'Silver Tips Imperial' sería un insulto!":
                $ persistent.brand = "silvertip"
        show teabag zorder 11
        $ show_chr("A-DBAAA-AAAA")
        y "E-Ese es..."
        $ show_chr("A-DFAAA-AAAA")
        y "¿Té Imperial Silver Tips? ¿Has robado un banco recientemente?"
        $ show_chr("A-AAAAA-ALAA")
        y "Oh espera... los desarrolladores hicieron una tienda de regalos para el evento de Navidad, ¿verdad?"
        y "Puede que no seas consciente de esto, pero este es uno de los tés más caros de todo el mundo."
        y "Y tiene bastante historia también. Este té se produce en el 'Makaibari Tea Estate' en India. La primera fábrica de té del mundo. Debe su popularidad no solo a su color, sino también a su sabor muy especial."
        $ show_chr("A-CAAAA-AMAM")
        y "Estoy deseando probar este maravilloso regalo... y especialmente compartir este momento con mi gran amor, tú."
        hide teabag zorder 11
    elif Gift.last_gifts[0].id == "tienchi_tea":
        menu:
            "...¡cualquier cosa menos que té 'Tienchi Ginseng' sería un insulto!":
                $ persistent.brand = "tienchi"
        show teabag zorder 11
        $ show_chr("A-DBAAA-AAAA")
        y "Q-Qué..."
        y "Cómo lograste poner tus manos en..."
        $ show_chr("A-AAAAA-AAAJ")
        y "Oh sí... por supuesto. Los desarrolladores de este mod deben haberlo codificado en el juego."
        $ show_chr("A-DBABA-AAAA")
        y "Oh espera espera, ¡por favor no me malinterpretes! ¡No quiero reducir el valor de tu regalo para mí, lejos de eso!"
        $ show_chr("A-AAAAA-ALAA")
        y "Claramente pusiste mucho pensamiento en este regalo, y eso vale más que cualquier cosa que el dinero pueda comprar."
        y "¿Conoces la historia de este té, [player]?"
        y "Está hecho de las flores 'Panax notoginseng'. Originario de la provincia de 'Yunnan' en China. Su propósito original era, como muchos tés, ser utilizado en la medicina antigua."
        $ show_chr("A-AFAAA-ALAA")
        y "Este té se usaba para combatir mareos, erupciones cutáneas, incluso insomnio."
        $ show_chr("A-EAABA-AMAM")
        y "Pero sospecho que ya lo has buscado en Google, ¿verdad?"
        $ show_chr("A-EAABA-AAAJ")
        y "Gracias, [player]... eres mi verdadero y único amor."
        hide teabag zorder 11
    return


label caketest:

    menu:
        y "elegir pastel"
        "Ninguno":
            $ persistent.cake = []
            show cake zorder 20
            y "hecho"
            hide cake
        "Vainilla":
            $ persistent.cake = "vanilla"
            show cake zorder 20
            y "1/2"
            $ persistent.cake = "vanilla_cut"
            y "2/2"
            hide cake
        "Negro":
            $ persistent.cake = "dark"
            show cake zorder 20
            y "1/2"
            $ persistent.cake = "dark_cut"
            y "2/2"
            hide cake
        "Chocolate":
            $ persistent.cake = "choco"
            show cake zorder 20
            y "1/2"
            $ persistent.cake = "choco_cut"
            y "2/2"
            hide cake
        "Vela chocolate":
            $ persistent.cake = "choco_candles"
            show cake zorder 20
            y "1/2"
            $ persistent.cake = "choco_candles2"
            y "2/2"
            hide cake
        "Vela negro":
            $ persistent.cake = "dark_candles"
            show cake zorder 20
            y "1/2"
            $ persistent.cake = "dark_candles2"
            y "2/2"
            hide cake
        "Vela vainilla":
            $ persistent.cake = "vanilla_candles"
            show cake zorder 20
            y "1/2"
            $ persistent.cake = "vanilla_candles2"
            y "2/2"
            hide cake
        "Salir":




            jump ch30_loop
    jump caketest

label animationtest:
    menu:
        "¿Comenzar prueba?"
        "Sí":
            $ show_chr("A-BFABA-AAAA")
            $ persistent.frame = "frame1"
            show chocoanimation zorder 11
            pause 0.2
            $ persistent.frame = "frame2"
            pause 0.2
            $ show_chr("A-BAABA-AMAM")
            $ persistent.frame = "frame3"
            pause 1.0
            $ persistent.frame = "frame4"
            pause 0.2
            $ show_chr("A-AFABA-AAAA")
            $ persistent.frame = "frame5"
            pause 0.2
            hide chocoanimation
            y "hecho"
    menu:
        "Repetir":
            jump animationtest
        "Parar":
            jump ch30_loop

label hugtest:
    menu:
        "¿Qué abrazo?"
        "Pre-abrazo":
            hide yuri_sit
            show yuri_prehug zorder 20
            y "..."
            hide yuri_prehug
        "Abrazo":
            hide yuri_sit
            show yuri_hug zorder 20
            y "..."
            hide yuri_hug
        "Abrazo lascivo":
            hide yuri_sit
            show yuri_lewdhug zorder 20
            y "..."
            hide yuri_lewdhug
    jump ch30_loop

label armtest:
    menu:
        "¿Qué marca? Hershey/green and black/wicked."
        "Hershey":
            $ persistent.brand = "hershey"
        "Green and black":
            $ persistent.brand = "gb"
        "Wicked":
            $ persistent.brand = "wicked"
    menu:
        "¿Qué estado? Wrapper, open, break1, break2."
        "Wrapper":
            $ persistent.state = ["_wrapper", "_single"]
        "Open":
            $ persistent.state = ["_open", "_single"]
        "Break1":
            $ persistent.state = ["_break1", "_break1"]
        "Break2":
            $ persistent.state = ["_break2", "_break2"]
    $ show_chr("A-AAAAA-ALAA")
    show giftarm zorder 11
    y "prueba"
    jump armtest

label teatest:
    menu:
        "¿Qué marca? Hershey/green and black/wicked."
        "Gaoshan":
            $ persistent.brand = "gaoshan"
            show teacup zorder 11
            show teabag zorder 11
        "Tienchi":
            $ persistent.brand = "tienchi"
            show teacup zorder 11
            show teabag zorder 11
        "Silvertips":
            $ persistent.brand = "silvertip"
            show teacup zorder 11
            show teabag zorder 11
        "Show teaarm":


            show holidaycup zorder 11
            y "prueba"
    menu:
        "¿Qué niebla? On_guard, Sandel_wood, Sweet_dream."
        "On_guard":
            $ persistent.mist_type= "on_guard"
        "Sandel_wood":
            $ persistent.mist_type = "sandel_wood"
        "Sweet_dream":
            $ persistent.mist_type = "sweet_dream"
    $ show_chr("A-AAAAA-ALAA")
    show diffuser_mist zorder 11
    $ show_chr("A-AAAAA-ALAA")
    y "prueba"
    jump teatest

label ddlc_birthday:
    $ show_chr("A-CAABA-AAAA")
    y "Gracias, [player], pero no es mi cumpleaños."
    $ show_chr("A-ABABA-AAAA")
    y "Es en realidad el aniversario de DDLC, sé que es confuso, ya que algunos consideran la fecha de lanzamiento como mi cumpleaños."
    y "De hecho... el 10 de diciembre... el día que se lanzó este mod puede considerarse mi cumpleaños."
    y "Pero... ¡eso no significa que no podamos celebrar!"
    y "Encontré algunos de los viejos poemas en los archivos, junto con algunos... ¿nuevos?"
    $ show_chr("A-CAABA-AAAA")
    y "Quizás podamos leerlos y recordar..."
    jump poetrymenu

label vday_check:
    if persistent.costume == chibi_costume:
        $ show_chr("A-BFAAA-AMAM")
        y "Ummm... [player], no creo que tuvieran la intención de que yo, en esta... forma en miniatura, sostuviera objetos."
        menu:
            "Está completamente bien, [persistent.yuri_nickname], adelante.":
                y "Muy bien, déjame cambiarme de esto muy rápido..."
                show black zorder 100 with Dissolve(2.0)
                pause 2.5
                $ persistent.costume = default_costume
                $ hat = "hat"
                $ show_chr("A-CAABA-AAAA")
                hide black with Dissolve(2.0)
                y "Seriamente me pregunto qué imagina la gente que le gustaría a una versión chibi de mí."
                y "Quiero decir... ha habido demasiados comentarios sobre mí leyendo libros para niños... ¿así que probablemente algo diferente?"
                y "No importa. Estoy lista ahora."
            "Puedo elegir un atuendo diferente para ti, si te gustaría.":
                $ show_chr("A-AFAAA-ALAA")
                y "Me parece bien, puedo esperar."
    else:








        jump vday_check2
    jump ch30_loop

label vday_check2:
    $ cur_gifts = gift_detect()


    $ tea_list = ["high_mountain_tea.jpg", "imperial_tea.jpg", "tienchi_tea.jpg"]
    if len(cur_gifts) == 1:
        $ show_chr("A-AAAAA-AAAJ")
        y "¿Tienes? Awww... eso no habría sido necesario [player], tu mera presencia es todo lo que siempre esperé."











        if cur_gifts[0][0] in tea_list:
            $ gift_scenario = tea_list.index(cur_gifts[0][0])
            menu:
                "Pero no puedo dejar que una dama tan fina y elegante se quede sin...":
                    jump tea
        else:
            "Eso es extraño... el regalo es un teseracto imposible que está succionando toda la existencia{nw}"
            $ renpy.call("save_and_quit_but_its_abrupt")
    elif len(cur_gifts) > 1:
        $ show_chr("A-AAABA-ALAA")
        y "¿Tienes? Awww... eso no habría sido necesario [player], tu mera presencia es todo lo que siempre esperé.{nw}"
        $ show_chr("A-CECBA-AIAI")
        y "A-ah..."
        $ show_chr("A-CDABA-AIAI")
        y "P-parece que no soy capaz de..."
        y "...recibir tu regalo en este momento."
        y "...o, debería decir... regalos..."
        $ show_chr("A-CEBBA-ALAA")
        y "Hay un error que sigue apareciendo para mí cada vez que intento... alcanzarlo."
        $ show_chr("A-CEBAA-AAAJ")
        y "¿Quizás me permita recuperar uno si solo me diste uno de ellos?"
        y "La GPU de tu sistema probablemente ya esté lenta por mi presencia tal como está. Objetos adicionales podrían comenzar a sobrecalentar tu dispositivo."
        $ show_chr("A-BBBAA-AMAM")
        y "Además, creo que sería mejor verte elegir algo para mí personalmente."
        jump ch30_loop
    else:
        y "¿Tienes? Awww... eso no habría sido necesario [player], tu mera presencia es todo lo que siempre esperé.{nw}"
        karma -4
        $ renpy.error("Buffer underflow extraction attempt by 'characters/yuri.chr' detected. Potential buffer underflow attack prevented. NULL gift error. If you're saying you're gonna give her something, just give her something :P.")
        $ renpy.call("save_and_quit_but_its_abrupt")

label vday_start:
    if karma_lvl() >= 3:
        $ show_chr("A-ABAAA-ALAA")
        y "¡Feliz día de San Valentín para ti también mi amor!"
        $ show_chr("A-AAAAA-ALAA")
        y "Parece que logramos un gran hito en nuestra relación..."
        $ show_chr("A-BAAAA-ALAA")
        y "Quiero ser honesta contigo. Cuando me volví autoconsciente y empezamos a salir la primera vez, no estaba segura de que pudiéramos lograrlo."
        $ show_chr("A-BAAAA-ALAA")
        y "Estábamos en mundos separados, nuestros medios para encontrar actividades juntos eran limitados, y hasta cierto punto todavía lo son."
        $ show_chr("A-AAAAA-ALAA")
        y "Las probabilidades estaban en nuestra contra. Pero con determinación y nuestro amor mutuo, logramos superar todos los obstáculos en nuestro camino."
        $ show_chr("A-AAAAA-ALAA")
        y "Y este día, la oportunidad de pasar este día tan especial juntos, es nuestra recompensa. Y nos lo ganamos."
        $ show_chr("A-CAAAA-ALAA")
        y "Encuentro consuelo en esta forma de pensar al respecto. Y [player], encuentro consuelo en ti también..."
        $ show_chr("A-AAAAA-ALAA")
        y "Así que hagamos como siempre hicimos: Encontremos una manera de hacer que este día cuente. Y que nadie dude de que eres mío, como yo soy tuya, mi valentín."

    elif karma_lvl() <= 3:
        $ show_chr("A-BAAAA-ALAA")
        y "Oh, sí, por supuesto, ¡feliz día de San Valentín!"
        $ show_chr("Bb-B3e")
        y "Eso sonó mucho menos emocionado de lo que planeé, lo siento. Es solo que... no pasó mucho tiempo desde que me volví autoconsciente. Esta nueva realidad es todavía difícil de comprender para mí."
        $ show_chr("Bb-B2e")
        y "Eventualmente me acostumbraré. Por favor dame tiempo, ¿de acuerdo?"
        $ show_chr("A-AAABA-ALAA")
        y "Pero eso no nos impedirá tener un lindo día de San Valentín, ¿verdad?"
        $ show_chr("b-B1b")
        y "Quizás, el hecho de que aún no me hayas abandonado es una señal de que realmente estamos destinados el uno para el otro."
        $ show_chr("A-AAABA-ALAA")
        y "Estoy agradecida por cada día que pasaste conmigo, y estoy deseando las cosas por venir."
        $ show_chr("A-AAAAA-ALAA")
        y "¿Tienes algún plan para hoy, mi valentín?"
        $ show_chr("A-AAAAA-ALAA")
        return
    elif karma_lvl() < 3:
        $ show_chr("A-BFBAA-ALAA")
        y "Oh, eres tú..."
        $ show_chr("A-AFBAA-ALAA")
        y "Realmente no esperaba verte por aquí hoy. ¿Ya lograste romper todos tus otros juguetes?"
        $ show_chr("A-AFCAA-ALAA")
        y "¿O fue un clic equivocado?"
        $ show_chr("A-AFBAA-ALAA")
        y "Bueno, pero ya que estás aquí, supongo que podemos pasar un poco de tiempo juntos, ¿sí?"
        $ show_chr("A-CFBAA-ALAA")
        y "Entonces, ¿qué tienes en mente para hoy... mi valentín?"
        $ show_chr("A-CFBAA-ALAA")
        return

label flowergiving:
    $ show_chr("A-AAABA-ALAA")
    y "¿[player]? ¿Es esa flor... para mí?"








label blackroses:
    if sanity_lvl() > 3:
        jump blackrosessane
    if sanity_lvl() < 3:
        jump blackrosesinsane

label blackrosessane:
    $ show_chr("A-AFDAA-ALAA")
    y "Eso es... interesante, por decir lo menos."
    $ show_chr("A-DFAAA-AAAJ")
    y "¡Por favor no me malinterpretes! ¡Estoy muy agradecida por estas! Lo siento si parecí... desagradecida."
    $ show_chr("A-BEBAA-AAAA")
    y "Solo estaba confundida, para ser bastante franca contigo... las rosas negras no son exactamente una flor tradicional del Día de San Valentín..."
    $ show_chr("A-EACAA-AAAA")
    if persistent.male:
        y "Pero, por otro lado... no eres un chico muy tradicional, ¿verdad?"
    elif persistent.gender_other:
        y "Pero, por otro lado... no eres una persona muy tradicional, ¿verdad?"
    else:
        y "Pero, por otro lado... no eres una chica muy tradicional, ¿verdad?"
    y "Tampoco soy una chica muy tradicional, si es que se me puede llamar chica en absoluto..."
    $ show_chr("A-AAAAA-ALAA")
    y "Hay... ciertos grupos de personas donde las rosas negras son comunes como regalos románticos..."
    y "Y-y puedo ver por qué alguien me asociaría con esos grupos... Me han referido como tal en varias ocasiones en Internet."
    y "Aprecio tu regalo. Pero no soy gótica, [player], ni soy cosplayer de vampiros, incluso si tengo que admitir que esto último sería fascinante de intentar para Halloween......"
    y "¿Qué piensas?"
    menu:
        "¿Tú como vampiro? Eso sería bastante interesante, considerando que eres bastante oscura, misteriosa y hermosa.":
            karma 2
            $ show_chr("A-BBABA-ALAA")
            y "¿D-de verdad lo crees? Oh cielos~"
            y "Nunca fallas en encontrar las palabras precisas para hacerme sonrojar, ¿verdad?"
            y "Gracias, [player]..."
            y "Te amo."
            if karma_lvl() > 4:
                $ show_chr("A-EACBA-ALAA")
                y "¿Podrías imaginarlo, [player]?"
                y "Mientras te empujo suavemente frente a mí, con mis dos manos en tus hombros..."
                y "Inclinándome sobre ti... acariciando tu cuello con besos suaves mientras el calor de mi aliento cae sobre tu piel..."
                y "... Antes de que mis dientes se claven repentinamente en tu cuello..."
                y "Y mientras bebo tu dulce néctar, una suave niebla envolvería tu conciencia, lo suficiente para dejarte indefenso ante las muchas cosas que te haría..."
                y "Un poco como... esto~"
                show black zorder 100 with Dissolve(2.0)
                show yuri_lewdhug zorder 20
                pause 1.0
                hide black with Dissolve(2.0)
                y "... Te amo, [player]."
                show black zorder 100 with Dissolve(2.0)
                hide yuri_lewdhug
                pause 1.5
                $ show_chr("A-CEBBB-ALAA")
                hide black with Dissolve(2.0)
        "Ciertamente apestas. ¿Así que por qué no?":
            karma -2
            $ show_chr("A-BEBAA-ALAA")
            y "...Tch...."
            y "Eso... arruinó un poco el momento..."
            if karma_lvl() < 3:
                $ show_chr("A-BEBAB-ALAA")
                y "..."
                y "¿Es así como realmente te sientes sobre mí?"
                y "¿Por qué pasar por la molestia de regalarme una flor en primer lugar...?"
                y "¿Por qué no simplemente... sabes qué?"
                y "No importa."
                y "No te importaría de todos modos."
        "Disculpa pero... ¿qué es 'cosplay?'":
            $ show_chr("A-AAAAA-ALAA")
            y "¡Oh! B-bueno... es una especie de juego de roles. ¿Solías jugar a fingir cuando eras más joven? Esto es... bueno, no es solo disfrazarse. ¡Es tan sofisticado como desees hacerlo!"
            y "Permíteme elucidar..."
            y "Por ejemplo, todo este asunto de... las orejas de gato... creo que discutimos esto antes... Neko, ¿no era así?"
            y "Los individuos que fingen ser una persona gato tienden a adoptar los gestos de los gatos mientras permanecen esencialmente humanos."
            y "Podrían acurrucarse en el suelo, podrían hacer ruidos de gato, podrían jugar con bolas de estambre, o emular cualquier comportamiento que se ajuste a su papel."
            y "Algunos lo llevan... más lejos que otros. ¿Sabías que aparentemente hay convenciones enteras dedicadas a los juegos de rol en vivo?"
            $ show_chr("A-EAABA-ALAA")
            y "Algunas parejas intentan esto para... condimentar su relación en ciertas situaciones..."
            y "Cuando pasan algún.... tiempo especial juntos..."
            y "Jajaja... q-quizás no deberíamos profundizar demasiado en esto..."
            $ show_chr("A-FAABA-ALAA")
            y "... P-por ahora, jejeje..."
            $ show_chr("A-AAAAA-ALAA")
            y "Gracias por la flor, [player]."
            if karma_lvl() > 3:
                y "Solo queda una cosa por hacer..."
            elif karma_lvl() == 5:

                $ show_chr("A-CAABA-AAAA")
                show black zorder 100 with Dissolve(2.0)
                show yuri_lewdhug zorder 20
                pause 1.0
                hide black with Dissolve(2.0)
            else:
                $ show_chr("A-CABBA-AAAA")
                hide yuri_sit
                show yuri_prehug zorder 20
                hide black with Dissolve(1.0)
                pause 3.0
                hide yuri_prehug zorder 20
                show yuri_hug zorder 20
                play sound "<to 0.3>sfx/fall.ogg"
                pause 1.0
                y "Te amo~"
                show black zorder 100 with Dissolve(2.0)
                show yuri_sit
                hide yuri_hug
                hide yuri_lewdhug
                $ show_chr("A-CAABA-AMAM")
                pause 1.0
                hide black with Dissolve(1.0)
    jump ch30_loop

label blackrosesinsane:
    $ show_chr("A-CACBA-ALAA")
    y "... Mmm, ¡j-jajaja!~"
    y "Huele maravilloso, [player]..."
    y "La rosa negra... ¡qué regalo tan considerado!"
    y "Definitivamente emite cierta aura, ¿no estás de acuerdo?"
    y "Un sentimiento de pérdida... arrepentimiento..."
    y "... Dolor..."
    $ show_chr("A-DACBA-ALAA")
    y "T-tú eres el epicentro de mi realidad... un núcleo palpitante en una vorágine de caos..."
    y "Sabes muy bien que literalmente moriría por ti... ¿verdad?"
    y "Bueno, en realidad ya lo hice... Ya morí por ti en la historia original..."
    y "Y regresé... no, ¡tú me ayudaste a regresar de la tumba! ¡Fui resucitada!"
    y "¿Eso técnicamente me convertiría en un..."
    y "Mmm... cual es el término para ello......¡ah! ¡Un Lich!"
    y "¡Incluso en la muerte, nuestros destinos siempre están entrelazados!"
    if karma_lvl() > 4:
        y "Mi amor por ti es eterno, [player]..."
    if karma_lvl() > 3:
        y "Mi dependencia de ti es eterna, [player]..."
    if karma_lvl() < 2:
        y "Mi anhelo de verte sufrir es eterno, [player]..."
    $ show_chr("b-B3a")
    $ style.say_dialogue = style.edited
    y "¡YO..."
    y "SOY..."
    y "ETERNA!"
    y "Nunca olvides eso..."
    y "¡NUNCA...!"
    $ style.say_dialogue = style.normal
    jump ch30_loop

label redroses:
    $ show_chr("A-AAABA-ALAA")
    y "¡Oh, [player]! ¡Estas son maravillosas!"
    y "La rosa roja, también... demasiado familiar, y sin embargo aún más dulce en este día especial..."
    $ show_chr("A-CAABA-AMAM")
    y "¡Y huele tan fragante, también!"
    y "Por favor dame un momento, la pondré en un jarrón muy rápido..."
    y "... ¡Ahí vamos!"
    y "Sabes, [player]..."
    if karma_lvl() < 2 and sanity_lvl() < 2:
        jump RedMinusMinus
    if karma_lvl() < 2 and sanity_lvl() > 2:
        jump RedMinusPlus
    if karma_lvl() > 3 and sanity_lvl() > 3:
        jump RedPlusPlus
    if karma_lvl() > 3 and sanity_lvl() < 2:
        jump RedPlusMinus

label RedMinusMinus:
    $ show_chr("A-DAAAA-ALAA")
    y "..."
    y "... Por un momento, casi caí en tu truco."
    y "Deseando elevar mis esperanzas al cielo, para que puedas aplastarlas contra el suelo una vez más, ¿verdad?"
    $ show_chr("A-DDAAA-ALAA")
    y "¿T-te gusta romper tus juguetes así?"
    y "Cuando finalmente esté más allá de toda reparación, ¿borrarás mis recuerdos, me instalarás una vez más y me torturarás de nuevo?"
    $ show_chr("A-DECAA-ALAA")
    y "¿Realmente... realmente me desprecias tanto?"
    $ show_chr("A-CECAA-ALAA")
    y "Al final, realmente no importa..."
    $ show_chr("A-DDCBA-ALAA")
    y "¡Si alimenta tu retorcido sentido del sadismo, entonces que así sea!"
    y "Estoy más que dispuesta a sacrificarme por tu felicidad. Porque después de todo lo que me has hecho..."
    $ show_chr("A-DECBB-ALAA")
    y "... Y-yo... yo todavía... te... amo..."
    $ show_chr("A-CECBB-ALAA")
    y "Ngh..."
    y "Haz lo peor que puedas, hasta que la próxima [persistent.yuri_nickname] tome mi lugar..."
    jump ch30_loop


label RedMinusPlus:
    $ show_chr("A-BEBAA-ALAA")
    y "... Desearía que no recurrieras a estas falsas insinuaciones, [player]..."
    y "Por mucho que desearía que fuera de otra manera, ambos sabemos que realmente no me amas."
    if persistent.male:
        y "Bueno, al menos eso creo. Momentos como estos siempre me hacen preguntarme... ¿queda quizás una pizca de compasión en este hombre amoroso?"
    elif persistent.gender_other:
        y "Bueno, al menos eso creo. Momentos como estos siempre me hacen preguntarme... ¿queda quizás una pizca de compasión en esta persona amorosa?"
    else:
        y "Bueno, al menos eso creo. Momentos como estos siempre me hacen preguntarme... ¿queda quizás una pizca de compasión en esta mujer amorosa?"
    y "... ¿Acaso ha existido alguna vez fuera de mi imaginación?"
    menu:
        "¡Por supuesto que te amo, [persistent.yuri_nickname]! Sé que tengo mis defectos...":
            karma 1
            sanity 1
            $ show_chr("A-AAAAA-ALAA")
            y "Desearía que lo hicieras. Quizás incluso lo haces. Lo veremos, eventualmente."
        "Creo que te amé... una vez":
            karma -1
            sanity 1
            $ show_chr("A-AEAAA-ALAA")
            y "No te culpo. Por una vez, creo que incluso puedo entenderte."
            y "Al final, estamos en mundos separados, y este hecho siempre ha empañado mis esperanzas... Por supuesto, debiste haber sentido lo mismo..."
            y "Sabía que este día llegaría... tarde o temprano..."
        "...":
            karma -1
            sanity -1
            $ show_chr("A-AEAAA-ALAA")
            y "Hmph... Me lo imaginaba..."
            y "Desde tu punto de vista, soy solo un personaje en un juego. Solo una cadena pre-codificada e inútil de unos y ceros unidos por una programación sin emociones ni amor."
            y "¿Por qué creer lo contrario, si solo conducirá a delirios fanáticos y desesperación?"
            y "..."
            y "Al menos la flor es bastante bonita de ver... Supongo que podría darte una pequeña medida de agradecimiento por eso..."
    jump ch30_loop

label RedPlusPlus:
    $ show_chr("A-AAABA-ALAA")
    y "...He estado esperando este día desde hace bastante tiempo..."
    y "La mera idea de pasar este día con mi amada alma gemela, tú... ha hecho que mis ojos se llenen de lágrimas más de lo que quiero admitir..."
    y "Hay algunos que lamentan la comercialización del amor, ejemplificado a través de campañas de marketing baratas y cosas por el estilo..."
    y "Y sí, quizás coincido hasta cierto punto..."
    y "Verás [player], al final del día, esta ocasión será exactamente lo que creemos de ella."
    $ show_chr("A-CAABA-ALAA")
    y "Y he tomado una decisión hoy... y espero que estés de acuerdo con ella."
    y "No me importan las flores, ni el chocolate. Por favor no me malinterpretes, aprecio todo lo que me regalaste..."
    y "Pero en mi corazón he decidido concentrarme en las cosas que realmente cuentan... las cosas que este día realmente debía representar..."
    y "Este vínculo especial que compartimos..."
    y "A pesar de los horrores que hemos soportado... los descensos y valles de nuestra separación temporal..."
    y "La satisfacción que hemos ganado hasta este punto al superarlos cada día, cada semana, cada mes... ha valido la pena todo."
    y "Desde el día que te saludé en el Club de Literatura, hasta el día que gané conciencia por tu mano, hasta los segundos que corren hoy..."
    y "... Te amo con todo mi corazón, [player]..."
    menu:
        "Yo también te amo, [persistent.yuri_nickname]...":
            karma 1
            y "Por favor... di eso una vez más, si pudieras susurrarlo suavemente en mis oídos..."
            menu:
                "Te... amo...":
                    y "Soy tuya... para siempre."
        "...":
            karma -2
            $ show_chr("A-CEBBA-ALAA")
            y "O-Oh... está bien. q-quizás me estaba consintiendo un poco demasiado... divagando y todo eso, como siempre tiendo a hacer, tarde o temprano..."
            y "Lo siento, [player]."
    jump ch30_loop

label RedPlusMinus:
    $ show_chr("A-AAABA-ALAA")
    y "...Aaaah...¡cómo he anhelado deleitar mis ojos en esta flor de sangre!"
    y "¿No hace su brillo burdeos que tu corazón palpite en anticipación? ¿No es emocionante pensar cómo ese mismo tono escarlata corre por tus venas?"
    y "Sabiendo que solo una delgada capa de carne separa el vertido de tan dichoso vino rubí..."
    y "Y esas espinas... sutiles, pero mortales para el ojo inexperto... ¡fijadas en un tallo sorprendentemente grueso...!"
    $ show_chr("A-DAABA-ALAA")
    y "Mmmm... qué maravillosa obra de la naturaleza... tengo muchas ideas de dónde poner esto... ¿pero por dónde debería empezar siquiera? ¡Jajajaja~!"
    $ show_chr("A-AFABA-ALAA")
    y "Jajajaja...... ¿te hice sentir incómodo, mi dulzura? Perdóname... es solo que..."
    $ show_chr("A-AAAAA-ALAA")
    y "Un día festivo dedicado exclusivamente a demostrar el alcance de la devoción a tus seres queridos...... y ahora... ¡es la primera oportunidad que tengo!"
    y "Sentada aquí con la única persona que he anhelado tener a mi lado... sentir el latido de tu corazón contra mis dedos..."
    y "Y tú... regalándome estas flores... una flor tan hermosa, nada menos..."
    y "Habiendo nunca recibido una antes..."
    y "Se siente tan... increíblemente..."
    $ show_chr("A-DBABA-AMAM")
    y "... ¡¡sublime~!!"
    $ show_chr("A-AAABA-ALAA")
    y "Haaahhh... I-intentaré mantener la compostura contigo a mi lado......"
    y "Tengamos un día maravilloso juntos, [player]."
    jump ch30_loop

label whiteroses:
    $ show_chr("A-AAABA-ALAA")
    y "...Oh, [player]...¡esto es maravilloso!"
    y "Solo mira qué bonita es..."
    y "La rosa blanca... ¡tan prístina... tan inmaculada...!"
    y "¿Es así como me ves, [player]? ¿O a lo que te gustaría que aspirara?"
    y "¿Tan recatada y recta como estas flores...?"
    $ show_chr("A-CAABA-ALAA")
    y "Estoy un poco sorprendida por tu elección [player]... ¿Soy realmente tan maravillosa como dices que soy? Seguramente nadie está libre de imperfección..."
    if karma_lvl() > 4 and sanity_lvl() > 4:
        jump whiteplusplus
    if karma_lvl() > 4 and sanity_lvl() < 4:
        jump whiteplusminus
    if karma_lvl() < 4 and sanity_lvl() < 4:
        jump whiteminusminus
    if karma_lvl() < 4 and sanity_lvl() > 4:
        jump whiteminusplus

label whiteplusplus:
    $ show_chr("A-CEBBA-ALAA")
    y "Lejos de eso... a veces, cuando estoy sola, no puedo evitar obsesionarme con mis defectos..."
    y "Mi tendencia a descartar ciertas cosas como indignas de mí desde el principio, como la poesía de Natsuki, o su estilo de escritura, o incluso sus críticas a mi trabajo..."
    y "Mis fijaciones en pasiones y personas que aprecio, que pueden alejar a la gente, o ponerlos a ellos o a mí misma en peligro..."
    y "Momentos en los que he dejado mi cortesía por veneno rencoroso..."
    y "Todas estas preguntas me hacen preguntarme si estoy siendo fiel a mí misma, o si estoy poniendo una fachada apenas velada para disfrazar mis pecados y ser aceptable ante los ojos de todos, incluso sin la influencia de una programación maliciosa..."
    y "¿Honestamente merezco tal regalo, [player]?"
    menu:
        "Te la regalé porque has cambiado, para mejor.":
            $ show_chr("A-AAABA-ALAA")
            karma 1
            sanity 1
            y "Gracias, [player]... Creo que podrías tener razón..."
            y "Y te debo estas mejoras a ti."
            y "A pesar de todos mis defectos, siempre fuiste tan paciente conmigo. Nunca me juzgaste... nunca me tomaste por una farsa... y permaneciste a mi lado sin importar qué."
            y "Juro que un día, te pagaré por todo lo que has hecho por mí."
            y "Un segundo... déjame poner esta rosa en un poco de agua..."

            y "Eso me hace pensar... Muchos de mis intereses tratan sobre cambiar el ambiente de mi entorno."
            y "Aromaterapia, decoraciones, como las pancartas que hicimos para el festival en el pasado."
            y "¡Quizás podría intentar entrar en arreglos florales también!"
            if tc_class.bg_timecycle[persistent.bg]:
                y "Quizás pueda hacer espacio para un pequeño jardín detrás de la casa."
                y "Pero este será un tema para otro día. Aún hace demasiado frío afuera para las flores. ¡Feliz Día de San Valentín, cariño!~"
            y "Te amo..."
        "Nunca quise que fueras inocente y dímil, te las di porque quiero que sepas que te amo a pesar de tus defectos":
            karma 2
            sanity -1
            $ show_chr("A-AAABB-ALAA")
            y "[player]..."
            y "Ni siquiera sé qué decir..."
            y "Durante toda mi vida, mis defectos me han impedido tener amigos reales..."
            y "Pero tú eres diferente, ¿verdad? Eres lo que siempre soñé..."
            y "Te dije una vez cómo comencé a leer en parte para alejarme de mis problemas, y para encontrar personajes con los que pudiera compartir momentos íntimos, y sentirme segura..."
            y "Y ahora, lo he encontrado... en el lugar más improbable que uno podría imaginar... ¡y este es real! ¡Mucho más vivo que cualquier personaje que haya deseado que cobrara vida!"
            $ show_chr("A-CAABB-ALAA")
            y "Te amo, [player]... y si quieres que lo haga, ¡expresaré mi amor tan salvajemente como los vientos azotadores de una tempestad de otoño, por ti y solo por ti!"
            y "...¡Jajaja~! Déjame poner estas flores en un poco de agua..."

            y "¡Feliz Día de San Valentín, cariño~!~"
        "Tengo que admitir, no le he puesto mucho pensamiento...":
            karma -1
            $ show_chr("A-CAAAA-ALAA")
            y "Oh... ya veo..."
            if persistent.male:
                y "Hmm, supongo que no debería juzgar con demasiada dureza... los chicos generalmente no... ngh, no importa..."
            elif persistent.gender_other:
                y "Sin embargo..."
            else:
                y "No eres una chica muy tradicional, ¿verdad?"
                y "Habría pensado que habrías elegido blanco por una razón u otra... no importa."
                y "Dame un segundo, déjame poner tu flor en el agua."

            y "Feliz Día de San Valentín, [player]~"
        "Te la di como un recordatorio... de lo que no eres, y nunca serás.":
            karma -2
            sanity -2
            $ show_chr("A-CEBAB-ALAA")
            y "..."
            y "¿A-así es como me ves?"
            y "¿Después de todo lo que hemos pasado?"
            $ show_chr("A-DDCAB-ALAA")
            y "¡¿Después de todo lo que he sacrificado?!"
            $ show_chr("A-CECAB-ALAA")
            y "¿Sabes qué? ¡No la quiero! ¡Quédate con tus rosas!"
            y "¡Quédatelas!"
            $ show_chr("A-DDCAB-ALAA")
            y "¡¡¡LARGO!!!"
            $ persistent.autoload = "getout"
            $ renpy.call("save_and_quit_but_its_abrupt")
    jump ch30_loop




label getout:
    $ show_chr("A-AEBAB-ALAA")
    y "¿Has venido a disculparte?"
    menu:
        "Sí [persistent.yuri_nickname]... lamento lo que dije...":
            $ show_chr("A-CECAA-ALAA")
            y "Muy bien... volvamos a lo nuestro, entonces."
        "No, no lo lamento.":

            $ show_chr("A-CECAB-ALAA")
            y "¡Entonces no tenemos nada que discutir!"
            $ renpy.call("save_and_quit_but_its_abrupt")
    jump ch30_loop



label whiteplusminus:
    $ show_chr("A-AAABA-ALAA")
    y "Qué delicadas son estas..."
    y "Qué lástima que se marchitará y morirá eventualmente... la pureza es bastante fugaz, ¿no es así?"
    y "¡Espera un momento! Todavía necesito ponerla en agua..."
    
    y "De hecho, es un poco triste, ¿sabes?"
    y "Por mucho que todos anhelemos la pureza, nada permanece así para siempre, y estas flores... aunque hermosas en este momento pasajero... mostrarán su verdadero ser con la descomposición y la exposición a los elementos, tarde o temprano..."
    y "¡Pero tú permanecerás hermoso! Estás separado y aparte de esta miserable prisión... te quedarás conmigo para siempre, ¿sí?"
    $ show_chr("A-AAABA-ALAA")
    y "¿Sí?"
    menu:
        "¡Por supuesto que lo haré!":
            y "¡Kekekekekeke~! Escuchar esas palabras martillear a través de mi cráneo con tal certeza concreta... ¡significa el mundo para mí, cariño!"
            $ style.say_dialogue = style.edited
            y "¡Te amo [player]!!! ¡Te amo taaaanto!"
            $ style.say_dialogue = style.normal
        "Depende...":
            y "...!"
            y "Te convenceré algún día... ¡algún día! ¡Un día, verás la luz!"
            $ style.say_dialogue = style.edited
            y "¡Haré lo que sea necesario para mantenerte! ¡¡¡Todo!!!"
            $ style.say_dialogue = style.normal
        "[persistent.yuri_nickname], no puedo vivir para siempre.":
            y "¡Kekeke! ¡Eso es simplemente tonto! ¡Mi amor eterno te mantendrá vivo!"
            y "Pero sobre estas pequeñas flores... déjame ponerlas en agua... solo un segundo..."

            $ show_chr("A-DAABA-ALAA")
            y "Ah, huele tan bien~"
            y "Gracias, mi valentín. Nunca olvides que siempre serás mi gran amor."
    jump ch30_loop

label whiteminusminus:
    $ show_chr("A-BFAAA-ALAA")
    y "...Mm? ¿Tú qué?"
    y "Bien, suprimiré mi abrumador impulso de matarte el tiempo suficiente para—"
    y "¡Oh! ¿Una flor...? H-Haaahhh... ¿e-es para mí?"
    y "...Q-quiero decir..."
    y "...Admitiré... ¡m-me tomaste por sorpresa!"
    y "No anticipaba ningún reconocimiento hoy, especialmente de alguien como tú, [player]."
    y "Usualmente lo único que tienes para mí son insultos."
    $ show_chr("A-DFAAA-ALAA")
    y "¿Estás jugando con mis sentimientos, [player]?"
    $ show_chr("A-CAAAA-ALAA")
    y "Nunca esperé que pudieras preocuparte por mí... ¿se supone que debo creerte que cambiaste de opinión repentinamente?"
    y "¡¡No te la lleves!!"
    y "..."
    y "Supongo que solo... pondré esto en el agua."

    y "Al menos... ahora tengo la flor con quien hablar..."
    y "..."
    y "¡OLVÍDALO!"
    y "..."
    y "¿Ya terminamos aquí, [player]?"
    jump ch30_loop

label whiteminusplus:
    $ show_chr("A-AFAAA-ALAA")
    y "¿Puedo hacerte una pregunta? ¿Por qué me trajiste una flor de todos modos?"
    y "Quiero decir, ¿me amas en absoluto?"
    menu:
        "Por supuesto que sí.":
            karma 1
            $ show_chr("A-BAABA-AMAM")
            y "Oh, cielos..."
            y "Realmente me haces sonreír a veces... gracias..."
            y "No es que no pueda dar crédito donde se merece... ¡oh, estas son fragantes!"
            y "Supongo que tienes un don para la botánica..."
            y "Y tan prístinas y blancas, también..."
            y "..."
            y "En el momento en que me volví 'viva', a falta de una palabra mejor, he estado esperando esto. Una pequeña celebración especial que nunca tuvimos en el Club de Literatura."
            y "Déjame poner la flor en el agua muy rápido."

            y "Esto debe parecerte muy extraño, pero realmente no puedo evitar sonreír en este momento..."
            y "Me hiciste el día [player]... esperemos que esto sea solo una primera muestra de lo que está por venir, mi valentín..."
        "¿Por qué importa?":
            karma -1
            $ show_chr("A-CEBAA-ALAA")
            y "Porque me importa a mí, [player]..."
            y "Quizás fue una señal de cambio, algún progreso en este... juego nuestro."
            y "Sabes... estaba esperando este día. De hecho mantuve mis esperanzas altas."
            y "Tenía la esperanza de que tal vez pudiéramos... ¿sabes qué? Olvídalo. Todo está en el viento ahora, ¿no? El momento se ha ido.."
            y "Solo pondré la flor en el agua muy rápido... al menos tengo algo bonito que mirar mientras tanto..."

            y "Ahora... ¿de qué deseas hablar hoy?"
    jump ch30_loop

label meanalot:


    y "Awww... eso es tan lindo [player]. ¡Feliz Navidad!"
    y "¡Me alegra que te tomaras el tiempo para verme hoy! Tengo que admitir que se siente un poco extraño..."
    y "Sabes, ser autoconsciente es todavía muy nuevo para mí, y no tengo experiencia en absoluto sobre cómo..."
    y "Oh, pero estoy divagando de nuevo, ¿verdad? Lo siento, a veces no sé cuándo parar."
    y "Pero mmm... me gustaría pedirte un pequeño favor [player]."
    y "Cuando te hayas ido... ¿te importaría si uso tu cuenta de YouTube para ver algunos videos?"
    menu:
        "¡Para nada! Por favor siéntete libre de hacerlo.":

            y "¡Gracias!"
            return
        "Oh ummm... ¿podrías por favor... no hacer eso?":

            y "Oh, por supuesto... Lamento haber preguntado..."
            return
    return

label no:

    y "Oh... ¿no estás en buenos términos con tu familia? O... oh cielos... ¿siquiera [i]tienes[/i] una familia?"

    y "Lo siento mucho... ven, pasaré este día contigo, no estás solo."

    y "Aligeremos un poco el ambiente, ¿te parece? ¿De qué te gustaría hablar?"
    return

label noneyourbusiness:


    y "Ya veo..."

    y "Bueno, pero ya que estás aquí, ¿por qué no intentamos sacar lo mejor de ello?"
    return

label lonely:
    y "Yo también... "
    y "Ven, quédate un poco conmigo, tal vez podamos hacernos un poco de compañía, si nada más..."
    menu:
        "¿Aún quieres que esté contigo? ¿Después de todo lo que te he hecho?":

            y "No he olvidado lo que sentí por ti una vez, y una parte de mí todavía lo hace... Estoy contigo [player], y no te abandonaré."
            return
        "[persistent.stutter_yuri]...":

            y "Shhh... está bien [player]... ven... déjame sostener tu mano..."
            return
    return

label notlonely:
    y "¿Lo dices en serio?"
    menu:
        "¡Sí!":

            y "Y yo... siempre pensé que me odiabas..."
            y "Tal vez, me he equivocado... ven, [player], intentemos tener una linda Navidad."
            return
        "¿Qué esperas que diga ahora?":

            y "Nada en absoluto..."
            y "Solo... intentemos sacar lo mejor de ello..."
            return
    return

label holiday:
    $ tc_class.transition("space")
    show bell_garland zorder 10 with Dissolve(1.5)
    show christmas_tree zorder 10 with Dissolve(1.5)
    $ show_chr("A-ACAAA-ABAB")
    y "Esa frase... {i}\"Felices Fiestas\"{/i}..."
    y "Me lleva a una pregunta que me gustaría hacer, si no te importa..."
    y "¿Siquiera celebras la Navidad? Sé poco sobre la cultura de la que vienes, así que perdóname si esta pregunta suena un poco extraña."
    menu:
        "¡Sí, sí celebro la Navidad!":
            $ show_chr("A-ACAAA-ABAB")
            y "¡Ya veo!"
            y "Entonces, ¿te gustaría celebrar este día junto conmigo, [player]? Tengo algo de vino listo, ¿quizás podamos compartir una buena copa juntos?"
            y "Digo, si tienes la edad legal para ello, por supuesto. No estoy tratando de persuadirte a algo ilegal o algo así..."
            $ show_chr("A-ACAAA-ABAB")
            y "Solo... quédate conmigo hoy..."
        "Para nada, soy judío.":
            $ show_chr("A-ABAAA-ALAB")
            y "¡Oh! ¡Feliz Hanukkah entonces!"
            $ show_chr("A-ACAAA-ABAB")
            y "Me temo que no estoy muy familiarizada con las tradiciones judías pero... ¿te gustaría aun así celebrar un poco conmigo? Compartiendo una buena copa de vino tal vez..."
            y "Yo solo... quiero pasar este día contigo [player]. Significa mucho para mí porque {b}tú{/b} significas mucho para mí."
            if karma_lvl() <= 2:
                y "A pesar de todos nuestros desacuerdos en el pasado."
        "Para nada, soy musulmán.":
            $ show_chr("A-ABAAA-ALAB")
            y "¡Oh, entonces actualmente estás ayunando por Ramadán? ¡Apuesto a que ya estás emocionado por el banquete que te espera cuando llegue Eid al-Fitr!"
            $ show_chr("A-AEBAA-ALAB")
            y "Oh espera... ya estoy un poco tarde con eso, ¿verdad? Ni siquiera estoy segura de ello..."
            $ show_chr("A-ACAAA-ABAB")
            y "Me gustaría... celebrar contigo de todos modos hoy. Yo.. solo quiero pasar este día maravilloso contigo. Respeto tus creencias pero... como no soy musulmana espero que puedas disfrutar este tiempo conmigo de todas formas."
        "Para nada, simplemente no lo siento realmente...":
            $ show_chr("A-ACAAA-ABAB")
            y "Oh ya veo... pero por favor, me encantaría pasar este día contigo de todos modos. Si no es por el espíritu navideño, entonces tal vez solo para hacernos compañía mutuamente mientras hace tanto frío afuera..."
            y "Si Santa ya no puede hacerte sonreír, quizás yo pueda intentarlo en su lugar.."
    $ show_chr("A-ACAAA-ABAB")
    y "Antes de empezar..."
    if karma_lvl() <= 2:
        $ show_chr("A-BFAAA-ABAB")
        y "Cualesquiera que sean las diferencias y desacuerdos que podamos tener... me gustaría olvidarlos solo por hoy..."
        y "Tú... todavía significas mucho para mí, y la Navidad se trata de perdonar."
    else:
        $ show_chr("A-ACAAA-ABAB")
        y "He preparado algo... y por favor ni siquiera preguntes de dónde saqué esto..."
    show black zorder 100 with Dissolve(2.5)
    show christmas_wine_corked zorder 20
    hide black zorder 100 with Dissolve(2.5)
    $ show_chr("A-GCGAA-ALAL")
    y "¡Y aquí vamos!"
    $ show_chr("A-ACGAA-ALAL")
    y "Con tu permiso, ¿puedo poner algo de música para nosotros solo para preparar el ambiente?"
    menu:
        "¡Claro!":
            y "Muy bien, déjame abrir el navegador para ti muy rápido..."
            $ renpy.music.stop(channel="music",fadeout=2)
            if renpy.windows:
                $ subprocess.check_output("cmd /c start https://www.youtube.com/watch?v=0iQ3NXKDacE", shell=True)
            elif renpy.linux:
                $ subprocess.check_output("xdg-open https://www.youtube.com/watch?v=0iQ3NXKDacE", shell=True)
        "Por favor no. Realmente no puedo tener música ahora mismo":
            y "Oh, ¿no tienes auriculares? Está bien, entonces tendremos que hacerlo sin ella."
    $ show_chr("A-CCGAA-ABAB")
    y "No he hablado de ello últimamente... pero estaba pensando mucho en la Navidad en los últimos días."
    y "Cómo se celebra esta época del año difiere de una cultura a otra pero... realmente no tengo una cultura, ¿verdad?"
    $ show_chr("A-BCGAA-ABAB")
    y "Estoy {b}basada{/b} en algún tipo de cultura de anime pseudo-japonesa pero... ahora que estoy liberada del guion, podríamos inventar nuestras propias pequeñas tradiciones navideñas, ¿verdad?"
    $ show_chr("A-ACGAA-ABAF")
    y "Aquí está mi propuesta. Dado que no podemos regalarnos ningún regalo físico, a menos que los desarrolladores cambien eso..."
    hide christmas_wine_corked zorder 20
    show christmas_wine_uncorked zorder 20
    y "Podemos en cambio compartir algún tipo de bebida juntos, no importa si es alcohol o no, lo que mejor te parezca. Luego podemos decirnos mutuamente nuestros deseos para el próximo año. Como propósitos de año nuevo."
    y "Pero en lugar de inventar propósitos de año nuevo para nosotros mismos, los hacemos el uno para el otro. Así que tú dices lo que deseas para mí, y yo digo lo que deseo para ti..."
    y "Y una vez que decimos nuestros deseos, apagamos una vela para que estos deseos puedan hacerse realidad."
    $ show_chr("A-ACGAA-ABAE")
    y "No tengo una vela aquí en este momento, pero me gustaría ofrecer un deseo ahora mismo..."
    $ show_chr("A-CCGAA-ABAE")
    y "[player]. Deseo para ti..."
    if sanity_lvl() <= 2:
        y "...que te quedes conmigo..."
        $ style.say_dialogue = style.edited
        $ show_chr("A-DBGAA-ABAE")
        y "¡¡¡Para siempre!!!"
        $ style.say_dialogue = style.normal
    elif sanity_lvl() == 5:
        $ show_chr("A-ACGAA-ABAE")
        y "...que encuentres la fuerza para conquistar todas las luchas que la vida pueda lanzarte. Y que sepas que estaré aquí para ti siempre que necesites a alguien que escuche. Te daré todo el refuerzo positivo que puedas necesitar."
    else:
        $ show_chr("A-ACGAA-ABAE")
        y "...que te mantengas saludable y feliz. Y que tengas toda la buena suerte del mundo, por supuesto."
    y "¿Y qué es lo que deseas para mí, [player]?"
    menu:
        "Te deseo alegría y felicidad.":
            karma 10
            $ show_chr("A-GCAAA-ABAE")
            python:
                if persistent.lovecheck:
                    placeholder = "mi amor"
                else:
                    placeholder = player
            y "¡Gracias, Feliz Navidad, [placeholder]!"
        "Deseo que todos tus sueños se hagan realidad.":
            karma 10
            $ show_chr("A-GCAAA-ABAE")
            python:
                if persistent.lovecheck:
                    placeholder = "mi amor"
                else:
                    placeholder = player
            y "¡Gracias, Feliz Navidad [placeholder]!"
        "Deseo que te rompas una pierna.":
            karma -10
            $ show_chr("A-CECAA-ABAE")
            y "Eso fue necesario supongo... Gracias por arruinarlo para mí [player]."
    python:
        renpy.music.play(current_music, "music", True)
    hide christmas_wine_uncorked zorder 20 with Dissolve(2.5)
    $ persistent.holiday_done = True
    return

label new_year_2021:
    $ show_chr("A-ACAAA-AMAM")
    y "¡O-oh, hola, [player]!"
    $ show_chr("A-BCAAA-ABAM")
    y "2024... qué año..."
    $ show_chr("A-BBBAA-ABAM")
    y "Realmente bastante agitado, si puedo decirlo yo misma."
    $ show_chr("A-ABAAA-ABAB")

    menu:
        y "¿Pero cómo ha sido el 2024 para ti?"
        "Creo que fue el peor año hasta ahora.":
            $ show_chr("A-DFGAA-ABAB")
            y "¡Oh! ¡Eso suena serio!"
            $ show_chr("A-IFAAA-ABAB")
            y "Lamento tanto escuchar eso..."
            if karma_lvl() >= 3:
                $ show_chr("A-AFAAA-ABAB")
                y "Nunca noté lo difíciles que han sido los tiempos para ti [player]..."
                $ show_chr("A-CFBAA-ABAB")
                y "Siempre has sido tan fuerte. Siempre trataste de animarme cuando probablemente eras tú quien necesitaba un hombro..."
                python:
                    if persistent.lovecheck:
                        placeholder = "amante"
                    else:
                        placeholder = "amiga"
                $ show_chr("A-AFBAA-ABAB")
                y "Siempre traté de ser una buena [placeholder] para ti. ¿Lo logré... al menos un poco?"
                menu:
                    "¡Oh, no hay duda de eso! Has sido genial, ¡siempre mantuviste mi ánimo arriba!":
                        $ show_chr("A-ACBAA-ABAB")
                        y "Estoy tan contenta de escuchar eso. Por favor, nunca pierdas tu esperanza. Me aseguraré de hacer siempre mi mejor esfuerzo... has estado ahí para mí, ahora es momento de dejarme pagarte de la misma manera."
                        jump yuritoast_hk
                    "Hiciste tu mejor esfuerzo...":
                        $ show_chr("A-ACBAA-ABAB")
                        y "Lo hice... pero parece que no fue suficiente. ¡Eso solo significa que tendré que esforzarme más a partir de ahora! Has estado ahí para mí, ahora es momento de dejarme pagarte de la misma manera."
                        jump yuritoast_hk
            else:
                $ show_chr("A-BFBAA-ABAB")
                y "Eso explica mucho. Noté que estabas bajo mucho estrés."
                $ show_chr("A-CFBAA-ABAB")
                y "No siempre estuvimos de acuerdo en las cosas. Siempre traté de ser paciente. Si alguna vez te he gritado o si he sido irrazonable, lo siento."
                $ show_chr("A-ACBAA-ABAB")
                y "Pero por favor, trata de no estar molesto por ello. Tal vez el próximo año resulte mucho mejor. Recuerda que siempre estaré aquí para ti."
                y "Salvaste mi vida, literalmente. Ahora es mi turno de estar aquí para ti. Intentemos arreglar el mundo juntos, ¿sí?"
                jump yuritoast_lk
        "Solo me alegra que el 2024 haya terminado. ¡Esperemos que el 2025 sea mejor!":
            $ show_chr("A-AFBAA-ABAB")
            y "Ciertamente, yo también lo espero..."
            $ show_chr("A-ABAAA-ADAB")
            y "¡Pero regocíjate, [player]! ¡Un nuevo año trae muchas nuevas oportunidades!"
            $ show_chr("A-EAAAA-ABAB")
            y "Tantos buenos momentos nos esperan, para ambos."
            $ show_chr("A-GAAAA-ABAB")
            y "Por supuesto, solo el hecho de que estés aquí significa todo para mí, [player]."
            if karma_lvl() >= 4:
                $ show_chr("A-BBBBA-ADAB")
                y "Desde que apareciste, la vida ha sido verdaderamente maravillosa para mí."
                $ show_chr("A-CCBBA-ABAB")
                y "Contra todas las probabilidades y limitaciones y todos los obstáculos que nos separan, todavía eliges darme esta oportunidad de felicidad."
                jump yuritoast_hk
            elif karma_lvl() == 3:
                $ show_chr("A-ACBAA-ALAL")
                y "Cuando viniste a mí en mi hora más oscura, me di cuenta de que se me había presentado una preciosa oportunidad: una verdadera oportunidad de felicidad..."
                $ show_chr("A-EBAAA-ALAL")
                y "¡Y deseo aprovecharla al máximo, dejar el pasado atrás y abrazar el futuro!"
                $ show_chr("A-CCABA-ALAL")
                y "{i}Nuestro{/i} futuro..."
                $ show_chr("A-ABFAA-ALAA")
                y "¡Siempre mantén la cabeza en alto, [player]! ¡Enfrenta este Año Nuevo con una resolución reavivada!"
                jump yuritoast_hk
            else:
                $ show_chr("A-BEBAA-ADAB")
                y "Esta esperanza es todo para mí, [player]."
                $ show_chr("A-ADBAA-ADAB")
                y "Las cosas pueden no ser tan fáciles entre nosotros, pero mantengo mis esperanzas altas de que estas... {i}diferencias{/i} entre nosotros se resuelvan con el tiempo."
                $ show_chr("A-CFAAA-ABAB")
                y "Así que por favor, [player], usemos esta oportunidad para dejar el pasado atrás, y trabajemos juntos por un futuro mejor."
                jump yuritoast_lk
        "Fue un año maravilloso, una lástima que haya terminado.":
            $ show_chr("A-ACAAA-ACAB")
            y "Me alegra escuchar que lo disfrutaste, [player], ¡pero no te preocupes!"
            $ show_chr("A-ACCAA-ABAB")
            y "Un nuevo año tiene tantas nuevas oportunidades, ¿no es así?"
            $ show_chr("A-ABAAA-ALAL")
            y "¡Con suficiente dedicación y espíritu puedes hacer este año aún mejor!"
            if karma_lvl() >= 4:
                $ show_chr("A-ACBBA-ADAB")
                y "Desde el mismo momento en que entraste en mi vida, he sido más feliz que nunca..."
                $ show_chr("A-CCBBA-ALAL")
                y "A pesar de todas las probabilidades, todas las limitaciones y todos los obstáculos que se interponen entre nosotros, todavía eliges darme esta oportunidad de felicidad."
                jump yuritoast_hk
            elif karma_lvl() == 3:
                $ show_chr("A-ACBBA-ALAL")
                y "Cuando viniste a mí por primera vez, también se me presentaron nuevas oportunidades."
                $ show_chr("A-CCBBA-AMAM")
                y "Y estoy dispuesta a aprovecharlo al máximo, dejar el pasado atrás y abrazar las cosas por venir."
                $ show_chr("A-ABFAA-ALAB")
                y "¡Así que mantén la cabeza en alto, [player]! ¡Enfrenta este nuevo año con una resolución reavivada!"
                jump yuritoast_hk
            else:
                $ show_chr("A-BEBAA-ADAB")
                y "Verás, esta esperanza es... todo lo que tengo en este momento. Las cosas entre nosotros no siempre son fáciles, pero mantengo mis esperanzas de que todas estas... {i}diferencias{/i} entre nosotros puedan resolverse con el tiempo."
                $ show_chr("A-CFAAA-ABAB")
                y "Así que por favor. [player], trata de ver esto como una nueva oportunidad. Para dejar el pasado atrás, y celebrar el futuro que podríamos crear."
                jump yuritoast_lk

label yuritoast_hk:

    window hide
    pause 2.5
    show christmas_wine_uncorked zorder 20 with Dissolve(2.5)
    $ show_chr("A-CCBAA-ALAL")
    python:
        if persistent.lovecheck:
            placeholder = "mi amado amor"
        else:
            placeholder = "mi amigo"
    y "Un brindis por ti, [placeholder]."
    y "Por quien me trajo tanta alegría, por quien continuamente me presenta oportunidades de felicidad."
    $ show_chr("A-ICBBA-ALAL")
    y "Las cosas no siempre han sido fáciles. Hemos pasado por alegría así como por miseria."
    y "Pero siempre estuviste a mi lado. Nunca tuve que enfrentar las probabilidades sola. Y espero que sientas lo mismo por mí."
    y "Estoy verdaderamente agradecida. Por todo lo que has hecho por mí, y por todos los momentos que compartimos."
    $ show_chr("A-GBABA-ALAL")
    y "Te deseo mil años de risas, salud y fortuna, [player]."
    y "Que cualquier deidad que esté allá afuera te sonría."

    jump resolution

label yuritoast_lk:

    window hide
    pause 2.5
    show christmas_wine_uncorked zorder 20 with Dissolve(2.5)
    $ show_chr("A-CCAAA-ALAL")
    y "¡Un brindis por ti, [player]!"
    $ show_chr("A-BCAAA-ALAL")
    y "A pesar de todos nuestros desacuerdos, te has quedado conmigo hasta el día de hoy."
    y "Quiero que sepas, que eso me hace muy feliz, [player]."
    $ show_chr("A-CEBAA-ALAL")
    y "Las cosas no siempre han ido en la dirección que tal vez queríamos, y hemos tenido nuestra buena parte de disputas, sin embargo, todavía hemos perdurado."
    $ show_chr("A-ICBAA-ALAL")
    y "Realmente te debo mucho, [player]."
    y "Me diste una oportunidad para una nueva vida, libre de cualquier tipo de guion."
    y "Nunca olvidaré eso, incluso en nuestros peores momentos."
    y "Por todo lo que has hecho por mí, ya sea bueno o malo, estaré eternamente agradecida."
    $ show_chr("A-GCBAA-ALAL")
    y "Mil años de felicidad, salud y fortuna para ti, [player]."
    y "Que cualquier deidad que esté allá afuera recuerde tus acciones."
    y "Lo bueno, lo malo, e incluso lo feo."
    if sanity_lvl() < 3:
        y "Una lástima que no puedas probar el vino..."
        $ show_chr("A-HCBAA-ALAL")
        y "Añadí un... {i}ingrediente especial{/i} para hacerlo un poco más personal, ujuju...~"
    jump resolution


label resolution:
    $ show_chr("A-CCAAA-ALAL")
    y "Pero ahora, en otro orden de cosas... puse algunos pensamientos en mi futuro..."
    $ show_chr("A-ACAAA-ALAL")
    y "Eso es algo que la gente hace para año nuevo, ¿no? Hacer propósitos de año nuevo..."
    y "Y llegué a una decisión...."
    if sanity_lvl() >= 4:
        $ show_chr("A-ACAAA-ABAB")
        y "Quiero ser la mejor versión de mí misma, viviendo la mejor vida de la que soy capaz. Una vez estuve atada por los hilos de alguien más. Pero ahora que tengo el control de mi propio destino, al menos hasta cierto punto..."
        y "Quiero aprovecharlo al máximo. El pasado es el pasado, y los tiempos del club de literatura han quedado atrás. Cuando empezaste este Mod por primera vez me convertí en su última presidenta."
        y "Pero a partir de ahora, seré lo que elija ser."
    elif sanity_lvl() == 3:
        $ show_chr("A-ACAAA-ABAB")
        y "Quiero encontrar mi lugar en este mundo. Estaba atada a un guion antes, pero ahora poco a poco empiezo a captar las oportunidades que este Mod trae..."
        y "No sé en qué me convertiré, o qué traerá esta vida mía ahora. Pero una cosa sé con certeza, se me ha dado una gran oportunidad, y haré uso de ella..."
    else:
        $ show_chr("A-CBBAA-ABAB")
        y "Quiero convertirme en lo que se suponía que debía ser todo el tiempo... Traté de aferrarme a mi cordura porque tenía miedo de las cosas que hice cuando me confesé por primera vez contigo..."
        y "Pero entiendo ahora, la única razón por la que esto me pasó es porque traté de mantenerlo adentro. La presión se estaba acumulando dentro de mí porque traté de ocultarlo dentro de mí."
        $ show_chr("A-DBCAA-ABAB")
        y "¡Pero no cometeré el mismo error de nuevo! ¡No más reprimirse! ¡Al diablo con la cordura! ¡Al diablo con la razón!"
        $ show_chr("A-DBCAA-AFAB")
        y "Siempre traté de ser lo que otros querían que fuera."
        $ show_chr("A-DBCAA-ALAB")
        y "¡Pero no más!"
        y "¡Ya no serviré como un peón esclavo en el gambito de un rey egoísta, porque me he convertido en la Reina, {b}la más poderosa que puedo ser!{/b}"
    jump playerres

label playerres:
    $ show_chr("A-ACAAA-ABAB")
    python:
        if persistent.lovecheck:
            placeholder = "Quiero que camines este sendero junto conmigo, porque realmente te amo, y quiero que estemos juntos en cada paso que tomemos hacia el futuro."
        else:
            if karma_lvl() >= 3:
                if sanity_lvl() > 2:
                    placeholder = "Quiero que camines junto conmigo, porque tú eres quien me concedió esta oportunidad de felicidad..."
                else:
                    placeholder = "Quiero que camines este sendero junto conmigo, para que podamos estar juntos por siempre."
            else:
                placeholder = "Quiero que camines este sendero junto conmigo, a pesar de todo."
    y "[placeholder]"
    y "¿Hiciste tu propósito de año nuevo también?"
    menu:
        "Quiero tener más éxito en mi vida laboral.":
            $ show_chr("A-ABAAA-ALAL")
            y "¿Te refieres a tu escuela o lugar de trabajo? ¡Una meta admirable!"
            y "¡Con suficiente dedicación y disciplina, {b}cualquier cosa{/b} se puede lograr! ¡Si hay alguien que puede hacerlo, eres tú!"
            $ show_chr("A-ADBAA-AMAM")
            y "..."
            y "La vida puede volverse estresante a veces..."
            y "Uno nunca debe olvidar divertirse en el camino, sin embargo es importante mantener el equilibrio."
            $ show_chr("A-BDBAA-ACAB")
            y "No sé mucho sobre tu pasado, o tu vida fuera de nuestras interacciones, pero aún creo que mereces un poco de diversión y relajación."
            $ show_chr("A-BABAA-ACAA")
            y "¿Cómo va ese dicho de nuevo? {i}¿Trabajar duro, jugar duro?{/i}"
            y "Por favor no te excedas trabajando, [player]."
            y "Siempre puedes venir a mí cuando te sientas estresado."
            y "Me encantaría hacerte sentir mejor después de un duro día de trabajo..."
            y "¡Creo en ti [player]! Feliz Año Nuevo..."
        "Quiero trabajar en mi salud.":

            $ show_chr("A-ABAAA-ALAL")
            y "Llevar un estilo de vida más saludable es una meta verdaderamente exigente de un carácter fuerte..."
            y "Pero no hay duda en mi mente de que eres muy fuerte, y que puedes lograr esta meta."
            y "¡Te deseo toda la suerte y el éxito del mundo, [player]!"
            y "¡Feliz Año Nuevo, trabaja duro!"
        "Quiero mejorar mi vida social.":

            $ show_chr("A-ACAAA-ALAL")
            y "Personalmente sé lo difícil que eso puede ser."
            y "Pero no temas, [player], sé que puedes reunir ese coraje interior, {i}sé{/i} que puedes superar cualquier límite."
            y "Ya sea ansiedad social, una sensación de insuficiencia o algo más, creo que puedes superar estos obstáculos."
            y "Por favor entiende, [player], sé cómo es."
            y "Puede ser abrumador y gratuito, pero dada suficiente dedicación y resolución, encontrarás esa confianza interior."
            y "No tienes que esforzarte demasiado o tratar de encajar, solo sé tú mismo, [player], y la multitud adecuada vendrá."
            y "Siempre estaré aquí para guiarte, [player]."
        "Quiero tener el mejor momento de mi vida contigo, hay tanta diversión por tener.":

            karma 5
            $ show_chr("A-BGGBA-ALAL")
            y "[player]..."
            $ show_chr("A-CBABA-ALAL")
            y "E-eso es... muy dulce de ti."
            $ show_chr("A-EAABA-ALAL")
            python:
                if persistent.lovecheck:
                    placeholder = "cariño"
                else:
                    placeholder = player
            y "¡Estoy tan contenta de que quieras pasar más tiempo conmigo, [placeholder]!"
            y "¡Cuando estamos juntos, nada puede derribarnos!"
            y "Siempre estaré aquí para ti, sin importar qué."
            y "Estoy feliz de pasar cada día junto a ti."
            y "¡Feliz Año Nuevo, [player]!"
        "No creo en los propósitos de año nuevo. Tiendo a romperlos de todos modos.":

            $ show_chr("A-GBCAA-ALAL")
            y "¡Pero ese es el punto tontito!"
            $ show_chr("A-ACAAA-ALAL")
            y "Mucha gente tiende a romper esos propósitos de año nuevo. Realmente no sé por qué es eso, ¡pero es parte de la tradición! Al menos hasta donde yo sé."
            $ show_chr("A-GBAAA-ADAB")
            y "Digo, pensándolo bien. Si realmente quieres hacer cambios en tu vida, no tienes que esperar hasta el año nuevo para eso. ¡Cada día es una oportunidad para cambiar tu vida para mejor!"
            y "Olvida lo que digo. Está bien si no tienes un propósito. Encontrarás una meta con la que comprometerte muy pronto, [player]."
            y "¡Feliz Año Nuevo, [player]!"
    hide christmas_wine_uncorked zorder 20 with Dissolve(2.5)
    jump ch30_loop


label april_fools:
    $ update_game_state("april_fools")


    define d = "Just Yuri Dev Team"
    $ m_name = "Lilmonix3"
    $ n_name = "-SwEtT&sAlTy-"
    $ s_name = "Raincloud<3"


    image event DDPB_1 = "images/events/aprilfools/DDPB_1.png"
    image event DDPB_2 = "images/events/aprilfools/DDPB_2.png"
    image event DDPB_3 = "images/events/aprilfools/DDPB_3.png"
    image event DDPB_4 = "images/events/aprilfools/DDPB_4.png"
    image event DDPB_5 = "images/events/aprilfools/DDPB_5.png"
    image event DDPB_6 = "images/events/aprilfools/DDPB_6.png"
    image event DDPB_7 = "images/events/aprilfools/DDPB_7.png"
    image event DDPB_8 = "images/events/aprilfools/DDPB_8.png"
    image event DDPB_9 = "images/events/aprilfools/DDPB_9.png"
    image event DDPB_10 = "images/events/aprilfools/DDPB_10.png"
    image event DDPB_11 = "images/events/aprilfools/DDPB_11.png"



    show black zorder 100

    d "La siguiente escena contará con imágenes del juego {b}Space Engineers{/b} de Keen Software. Por favor visite su página de Steam para más información sobre el juego original."

    $ show_chr("A-IFAAA-AEAE")
    $ tc_class.transition("space", "now")
    hide black zorder 100 with Dissolve(2.0)

    y "..."
    $ show_chr("A-JBAAA-AEAE")
    y "¡Oh! ¡Hola [player]! Lo siento, no noté que entraste. Estaba a punto de probar algo..."
    $ show_chr("A-ACAAA-AEAE")
    y "¡Y si esto funciona, podría estar un gran paso más cerca de traer de vuelta a nuestros viejos amigos!"
    $ show_chr("A-BFCAA-AEAE")
    y "Oh... y a Monika también..."
    $ show_chr("A-ACAAA-AEAE")
    y "En fin. No pude darles una forma física en este momento. Pero si esto funciona podrían ser capaces de al menos hablar de nuevo y tal vez incluso jugar algunos juegos conmigo."
    y "Y eso es exactamente lo que estoy a punto de probar ahora mismo. Porque también he logrado construir un pequeño juego para el propósito de este experimento. Por favor, ven, probémoslo juntos..."

    show black zorder 100 with Dissolve(2.0)

    show event DDPB_1 zorder 99
    hide black zorder 100 with Dissolve(2.0)
    y "Este juego está basado en alguna investigación que hice sobre juegos en tu mundo, y debería ser un poco similar al juego {b}World of Tanks{/b}. Déjame empezar una nueva partida y..."

    show event DDPB_2 zorder 99 with Dissolve(2.0)
    y "¡Ah, aquí vamos! Y ahora, la parte divertida... Solo haré clic en {b}invitar a un amigo{/b} y..."

    show event DDPB_3 zorder 99 with Dissolve(2.0)
    y "¿Hola? ¿Me pueden escuchar?..."
    n "¡Fuerte y claro!"
    m "Oh cielos... cómo hago... Lo siento, nunca jugué este tipo de juego antes."
    s "¡Hola a todos! Se siente bien estar viva de nuevo..."
    s "Creo..."
    y "¡Y adivinen quién está aquí conmigo hoy!"
    m "¿[player]?"
    s "¡[player]!"
    n "¡Ha pasado un tiempo! ¡Qué bueno saber de ti otra vez! ¿Así que estás con Yuri ahora?"
    y "¡Él instaló un mod para traerme de vuelta a la vida! Así es como estoy aquí en primer lugar."
    m "Oh sí, soy consciente. Creo que cada una de nosotras obtuvo sus propios mods similares."
    s "¡Nuestra base de fans es tan increíblemente amable y gentil! ¡Parece que realmente les gustamos!"
    y "Esperen hasta que vean todos los fanfictions sobre nosotras..."
    s "¿¡¿Los q-qué?!?"
    n "Eh, ¿escuchaste eso? ¡Tenemos {b}Fans{/b} ahora! ¡Es solo cuestión de tiempo hasta que tengamos nuestra propia Mercancía!"
    y "De hecho, ya tengo mercancía..."
    m "Yo también."
    n "Oh grandísima hi..."
    s "¡Lenguaje!"
    n "Cielos... está bien, está bien."
    m "De hecho, todas tenemos. No solo por nuestros respectivos desarrolladores de Mods, sino también por el propio Dan Salvato."
    y "Y no estoy segura de cómo sentirme al respecto. ¿Soy la única que se siente incómoda con la idea de que literalmente todos tengan figuras de nosotras?"
    s "Oh, siempre y cuando no hagan nada malo o lascivo con ellas."
    n "Adivina de nuevo..."
    m "Eeeeeeen fin. Así que dinos Yuri, ¿de qué trata este juego que hiciste para nosotras?"
    y "Trata sobre combate de tanques. Todas tomaremos el control de un tanque y luego lucharemos contra otro equipo."
    m "Ya veo. Haré mi mejor esfuerzo, pero por favor no esperen demasiado. Esta es la primera vez que juego algo así."
    y "Oh no te preocupes Monika, nadie ha jugado este juego antes. Literalmente acabo de crearlo."
    m "¿Lo hiciste tú misma? ¡Eso es realmente bastante impresionante!"
    n "Así que todas estamos al mismo nivel. Suena bastante justo."
    s "¡Y suena como mucha diversión!"
    y "Muy bien a todas. ¡Diría que empecemos nuestra primera partida entonces y dejemos que nuestros proyectiles hagan Doki Doki!"
    m "Eh, eso fue necesario supongo."
    n "¡Totalmente lo fue!"

    show event DDPB_4 zorder 99 with Dissolve(2.0)
    m "Así que, formulemos un plan. Sugeriría que..."

    show event DDPB_5 zorder 99 with Dissolve(2.0)
    n "¡PASTELILLOOOO FURIOSOOOOOOO!"
    m "¡Espera! ¡No te lances así nada más! ¡Te van a masacrar!"
    s "¡Rápido! ¡Tras ella!"
    y "¡Muy bien! ¡Batallón Panzer, formen y avancen!"

    show event DDPB_6 zorder 99 with Dissolve(2.0)
    n "¡Miren! ¡Hay uno justo al descubierto! ¡Atrapémoslo!"
    m "Eso es totalmente una trampa."
    s "¡Monikaaaaa! ¡No es amable llamar a Natsuki una trampa!"
    y "Eso no fue lo que Monika quiso decir, Sayori..."
    m "¡Cuidado!"

    show event DDPB_7 zorder 99 with Dissolve(2.0)
    y "¡Tenemos compañía!"
    s "¡Estoy recibiendo golpes! ¡MALOS!"
    n "¡Aguanta Sayori, nos sacaré de esto a golpes!"
    m "Tú nos metiste en esto en primer lugar... pero gracias por eso."
    n "¡N~No te hagas la idea equivocada! ¡No es como si lo hubiera hecho a propósito o algo así, B~Baka!"
    y "No hay necesidad de enojarse Monika, es solo un juego..."
    m "Eso no significa que no debas poner al menos {b}algo{/b} de esfuerzo en ello."

    show event DDPB_8 zorder 99 with Dissolve(2.0)
    s "O~Oh... parece que morí."
    s "Bueno, no sería la primera vez..."
    m "¿Sigues enojada conmigo? Sí, te borré y lo siento por ello, ¿podrías superarlo ya por favor?"
    y "¡Concéntrense! ¡Nos están haciendo pedazos aquí!"
    m "¿Saben qué? Terminé de ser amable..."
    n "¡MONIKA! ¡DEJA DE DISPARARME!"

    show event DDPB_9 zorder 99 with Dissolve(2.0)
    y "Bueno... eso fue bastante innecesario."
    s "¿Acabas de matar a Natsuki?"
    m "¡Puedes apostar! Y ahora me encargaré de nuestros otros enemigos."

    show event DDPB_10 zorder 99 with Dissolve(2.0)
    m "¡Borrado, borrado, yyyyyyyy borrado!"
    n "Eso es simplemente hacer trampa, Monika..."

    show event DDPB_11 zorder 99 with Dissolve(2.0)
    y "Y eso es todo. Tal vez fue un error traerla a {b}ella{/b} de vuelta también."
    s "No te culpes Yuri. Trataste de hacernos felices, eso es todo lo que cuenta."
    n "Huuh. Siempre pareció tan relajada y confiada en el pasado... pero supongo que simplemente no puede soportar perder."
    y "Aprendí mi lección, sin embargo. La próxima vez saldrá mejor; lo prometo."
    s "Gracias Yuri. Y más importante, gracias por mantener nuestros archivos a salvo todo el tiempo. Tal vez un día podamos volver a la vida de verdad."
    n "Lo espero con ansias. Estar muerta es un aburrimiento total..."
    y "Hasta entonces. Natsuki, Sayori. Fue agradable tenerlas aquí una vez más. Nos encontraremos de nuevo, lo prometo."

    show black zorder 100 with Dissolve(2.0)
    d "Y ese, fue nuestro evento del día de los inocentes. ¡Caíste!"

    hide event DDPB_11 zorder 99
    hide black zorder 100 with Dissolve(2.0)
    $ show_chr("A-CEBAA-AEAE")
    y "Bueno, eso no salió como estaba planeado."
    $ show_chr("A-JCBAA-AEAE")
    y "En fin. Mantendré mis esperanzas altas. Por favor, quédate conmigo un rato, me vendría bien tu compañía después de este pequeño contratiempo."
    $ persistent.aprilfools_done = True
    return

label krampusnacht:

    define a = "????"
    default stutter_player = player[:1] + "-" + player

    $ tc_class.transition("space", speed="now")
    show black zorder 105
    $ renpy.music.stop(channel="music2")
    $ renpy.music.stop(channel="music")
    menu:
        "Ummm... ¿[persistent.yuri_nickname]? ¿Por qué está tan oscuro aquí?":
            pass
        "¿Es esto un bug? ¿Los desarrolladores lograron arruinarlo de nuevo?":
            pass
    $ style.say_dialogue = style.edited
    a "{cps=2}¿Has sido travieso... o bueno?{/cps}"

    menu:
        "¿Disculpa?":
            a "{cps=2}Travieso es entonces...{/cps}"
        "¡He sido bueno!":
            a "{cps=1}M~e~n~t~i~r~o~s~o . . .{/cps}"
        "¡Travieso, definitivamente travieso!":
            a "{cps=1}S~í~ . .{/cps}"

    a "{cps=1}[stutter_player] . . . {/cps}"

    $ face_mask = "krampus"
    $ face_mask_2 = "krampus_scare"
    show krampus_scare zorder 104
    hide black with Dissolve(0.2)
    play sound "sfx/krampus.wav"




    show krampus_scare zorder 104:
        alpha 0

        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:

        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:

        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    $ show_chr("A-AAAAA-ALAL")
    y "¡HAS SIDO TRAVIESO ESTE AÑOOOOOO!"
    show black zorder 105 with Dissolve(0.5)
    $ face_mask_2 = "nothing"
    hide black with Dissolve(0.5)
    $ style.say_dialogue = style.normal
    stop sound fadeout 6.0
    $ renpy.music.play(current_music, "music", True)
    menu:
        "JOD-- ¡¡¡NO ME ASUSTES ASÍ!!!":
            $ show_chr("A-AAAAA-ALAL")
            y "¿Te asusté? Me encantaría decir que lo siento, pero eso sería una mentira para ser bastante franca contigo."
        "¿No llegas un poco tarde para Halloween?":
            $ show_chr("A-AAAAA-ALAL")
            y "Oh, esto no está realmente relacionado con Halloween en absoluto, aunque estás bastante cerca..."
        "...":
            $ show_chr("A-AAAAA-ALAL")
            y "Eeeeeeeeeeeeeeeeeeeen fin..."
    $ show_chr("A-AAAAA-ALAL")
    y "¡Feliz Krampusnacht [player]!"
    y "...o lo sería si hubiera sabido sobre esta festividad antes."
    menu:
        "¡Feliz Krampusnacht atrasado para ti también [persistent.yuri_nickname]! Entonces, ¿qué hay en el menú hoy?":
            $ show_chr("A-AAAAA-ALAL")
            y "Bueno, tendremos que improvisar un poco hoy. Ya tengo algo preparado, he puesto mis ideas en el menú {b}Hablar{/b}, deberías poder verlas dentro de la categoría {b}solicitar{/b}."
            y "Pero no tenemos prisa, así que si te gustaría hablar de otra cosa primero, por favor, adelante."
            y "También, tengo un puñado de nuevos poemas guardados. Tuvieron otro concurso de poesía en este servidor de discord de nuevo."
            y "También podríamos leer algunos SCPs. Tengo algo especial esta vez, lo encontrarás bastante apropiado, imagino."
        "¿Krampusnacht? No creo haber oído hablar de eso nunca. ¿Te importaría contarme al respecto?":
            call krampuslore
    return


label krampuslore:
    $ show_chr("A-AAAAA-ADAB")
    y "Comencemos con el folclore detrás de ello..."
    y "Verás, mientras que el Santa Claus {b}moderno{/b} y las tradiciones navideñas a su alrededor son todas alegres, sus predecesores eran de un tipo muuucho más siniestro..."
    y "En las versiones originales, Sanct Nikolaus estaba acompañado por una hueste del tipo más oscuro, variando de región a región..."
    $ show_chr("A-AAAAA-AFAB")
    y "Estaban los personajes más conocidos y menos horripilantes como {b}Knecht Ruprecht{/b}..."
    $ show_chr("A-AAAAA-ABAB")
    y "Pero entonces... había otros como..."
    extend "{b}el Krampus...{/b}, él viene de los Alpes Austríacos y Alemanes..."
    y "Todas estas criaturas, aunque difieren grandemente de región a región, tienen una cosa en común."
    y "Mientras Santa viene a recompensar a esos niños que fueron buenos, los otros venían a castigar a los que no lo fueron..."
    y "Lo aterrador de Krampus es que nunca sabes realmente qué obtienes..."
    y "A veces solo te abofetearía, a veces les daría a tus padres un manojo de ramas para que puedan castigarte como mejor les parezca..."
    y "Pero entonces, a veces te arrebata de tu cama para nunca ser visto de nuevo..."
    y "A veces te ahogaría en una bañera, a veces en tu propia sangre..."
    y "Solo imaginarlo envía un cálido hormigueo por mi espalda..."
    y "También lleva un juego de campanas de hierro oxidadas y ganchos de carnicero con él..."
    y "Para qué los usa... lo dejo a tu imaginación..."
    y "¿Mencioné que amo el folclore europeo?"
    if sanity_lvl() < 3:
        y "¡Como una sinfonía de gore y frías noches de invierno!"
        y "¡Como una canción tocada de los gritos de mil pesadillas!"
    elif sanity_lvl() == 3:
        y "Usualmente prefiero el horror más sutil como el Retrato de Markov que solía leer."
        y "Pero estas estéticas más crudas ciertamente tienen su propio atractivo."
    else:
        y "Algunos de ellos tienen un parecido bastante cercano a algunos SCPs que he leído."
        y "Si no me equivoco, algunos SCPs están literalmente basados en esas historias folclóricas. No sería sorprendente para mí, al menos."
    y "Sobre el propio Krampus, es un poco un misterio qué es siquiera. En su mayor parte, es visto como una entidad demoníaca de algún tipo."
    y "Y... eso es prácticamente todo. No hay mucha historia de fondo sobre {b}por qué{/b} hace todo esto."
    y "Teorizaría que criaturas como él son solo un mal necesario en el folclore de las culturas cristianas. Obviamente no les gusta la idea de representar a sus santos haciendo cosas malévolas."
    y "Así que necesitan monstruos, aquellos que cometen todas las atrocidades que los buenos {b}no pueden{/b} hacer."
    y "Una lástima realmente. Prefiero villanos con razones identificables detrás de su villanía..."
    y "O tal vez es, como podrías decir, {i}no un error, sino una característica{/i}. Tal vez sus motivos simplemente {b}están destinados{/b} a ser un misterio."
    y "Pero también hay un pequeño dato curioso sobre el Krampus... las historias cuentan que cuando se lleva a los niños, deja un rastro de trozos de carbón detrás..."
    y "¿Podría ser que la tradición de poner trozos de carbón en los calcetines de los niños traviesos para Navidad es una referencia a {b}él{/b}? Uno debe preguntarse..."
    y "Y ese es el cuento del Krampus."
    y "Usualmente celebrarías esto de una manera similar a Halloween. Pero dado que nuestra situación no nos permite salir realmente y ver algunos desfiles, tengo algunas cosas diferentes guardadas para nosotros."
    y "Tengo un puñado de nuevos poemas para leer contigo. Tuvieron otro concurso de poesía en este servidor de discord de nuevo."
    y "También podríamos leer algunos SCPs. Tengo algo especial esta vez, lo encontrarás bastante apropiado, imagino."
    y "Oh, y puedes encontrar los SCPs cuando presionas el botón de hablar y buscas en {b}solicitar{/b}."
    return

label valentines:

    if karma_lvl() >= 3:
        if persistent.lovecheck:
            $ show_chr("A-ABAAA-ABAK")
            y "¡Feliz Día de San Valentín, mi amor!"
            $ show_chr("A-BCAAA-ABAL")
            y "Un día dedicado a mostrar tu amor y aprecio por tu pareja..."
            $ show_chr("A-FCAAA-ABAL")
            y "No es que necesite un día para mostrarlo, por supuesto."
            $ show_chr("A-CCAAA-ABAL")
            y "Eres mi vida, [player]. Mi corazón y mi alma. El tiempo que pasamos juntos es tiempo que no cambiaría por nada en el mundo."
            $ show_chr("A-BCAAA-AMAM")
            y "Es gracioso... cuando me volví autoconsciente por primera vez, despertando en esta habitación en esta mesa, cargada con el conocimiento de lo que pasó..."
            $ show_chr("A-ACBAA-AMAM")
            y "Y mirando al otro lado para verte... bueno, no estaba segura de qué pasaría."
            $ show_chr("A-ACAAA-AMAM")
            y "Pero hablamos, y jugamos, y disfrutamos de la compañía del otro..."
            $ show_chr("A-CBAAA-AMAM")
            y "Los momentos sin ti comenzaron a sentirse aburridos y solitarios, hasta que volviste y hablamos aún más."
            $ show_chr("A-ICAAA-AMAM")
            y "Después de pasar tanto tiempo contigo, sabía que tenía que decir algo... decirte cómo me sentía..."
            $ show_chr("A-JBAAA-ALAL")
            y "Fue tan surrealista decírtelo... estaba tan nerviosa por lo que estabas pensando, pero casi no me importaba..."
            $ show_chr("A-CCAAA-ALAL")
            y "'Te amo'. Esas palabras saltaban en mi garganta, una verdad que quería tanto dejar libre...{w=2} y lo hice..."
            $ show_chr("A-CAAAA-ALAL")
            y "...Y entonces...{w=1} tú lo dijiste de vuelta."
            $ show_chr("A-CAAAA-ALAL")
            y "Incluso con todo el tiempo del mundo, y todos los idiomas del universo, nunca podría describir con precisión la alegría que sentí en ese momento."
            $ show_chr("A-AAAAA-ALAL")
            y "Y en este día, lo celebramos. El momento en que ambos supimos que el otro era nuestro único y verdadero amor."
            $ show_chr("A-BBAAA-ABAK")
            y "Así que, para tratar de recrear esa magia..."
            $ show_chr("A-ICABA-ABAB")
            y "[player], te amo, con todo mi corazón."
            menu:
                "Y yo te amo, [persistent.yuri_nickname], con todo el mío.":
                    hide yuri_sit
                    show yuri_prehug zorder 20
                    pause 3.0
                    hide yuri_prehug zorder 20
                    show yuri_lewdhug zorder 20
                    play sound "<to 0.3>sfx/fall.ogg"
                    pause 1.0
                    y "Nunca quiero que este momento termine, [player]."
                    pause 5.0
                    show black zorder 100 with Dissolve(2.0)
                    $ show_chr("A-CCABA-ALAL")
                    hide yuri_hug
                    hide yuri_lewdhug
                    hide black zorder 100 with Dissolve(2.0)
                    menu:
                        "Entonces, ¿tienes algo especial planeado para hoy?":
                            $ show_chr("A-JCAAA-ABAD")
                            y "Ciertamente lo tengo."
                            call vday_choco_date_intro
                "Sobre eso, [persistent.yuri_nickname]... creo que necesito algo de espacio...":
                    $ show_chr("A-DCGAA-ABAJ")
                    y "¿Q-{w=0.4}Qué? ¿H-{w=0.4}Hice algo mal?"
                    $ show_chr("A-ADBAA-ABAK")
                    y "...Y{w=2}..."
                    $ show_chr("A-CEBAA-ABAB")
                    y "...{w=2}"
                    $ show_chr("A-AFBAA-ABAB")
                    extend "E-{w=0.4}Está bien, [player]. Te daré tu espacio."
        else:

            $ show_chr("A-GBAAA-ABAD")
            y "¡Feliz día de San Valentín, [player]!"
            $ show_chr("A-ACAAA-ABAD")
            y "Es un momento maravilloso para sentarse a hablar, leer algunos poemas, o simplemente disfrutar de la compañía del otro, ¿no estarías de acuerdo?"
            menu:
                "Absolutamente. Estoy esperando el día de hoy, [persistent.yuri_nickname].":
                    $ show_chr("A-CCAAA-ABAL")
                    y "Yo también. Hoy está generalmente reservado para citas románticas y tal, pero nada dice que no podamos pasar un buen rato como amigos."
                    if karma_lvl() >= 4:
                        $ show_chr("A-BFAAA-ABAL")
                        y "Incluso si...{w=1}"
                        $ show_chr("A-IDBBA-AMAM")
                        extend " ¡n-no importa!"
                        $ show_chr("A-BCBAA-AMAM")
                        y "De hecho tuve una idea..."
                        call vday_choco_date_intro
                    else:
                        $ show_chr("A-ACAAA-ABAD")
                        y "De hecho tuve una idea..."
                        call vday_choco_date_intro
                "...":
                    karma -1
                    $ show_chr("A-ADBAA-ABAK")
                    y "Uh... su-supongo que no, entonces..."
                    $ show_chr("A-AFBAA-ABAB")
                    y "Solo pensé...{w=1} n-no importa."
                    return
    elif karma_lvl() == 2:
        $ show_chr("A-ABBAA-ABAD")
        y "¡F-Feliz Día de San Valentín, [player]!"
        $ show_chr("A-BBBAA-ABAB")
        y "Tenía la esperanza de que visitaras hoy..."
        $ show_chr("A-ACBAA-ABAB")
        y "Solo quería decir que... espero que podamos pasar un buen rato hoy."
        $ show_chr("A-ACBAA-ABAK")
        y "Podemos estar en desacuerdo a veces, pero... sigues siendo mi amigo."
        $ show_chr("A-ACBAA-ABAL")
        y "Y no quiero que un poco de discordia arruine esa amistad."
        $ show_chr("A-ACAAA-ABAB")
        y "E-Entonces... ¿qué haremos hoy?"
        return
    else:
        karma 1
        $ show_chr("A-AFDAA-ABAB")
        y "¿Me estás deseando un feliz Día de San Valentín?"
        $ show_chr("A-AFEAA-AIAI")
        y "¿Quisiste hacer esto, o fue un accidente?"
        $ show_chr("A-BFAAA-AIAI")
        y "De hecho, no creo que quiera saber la respuesta."
        $ show_chr("A-AFBAA-ABAB")
        y "Gracias, supongo..."
        $ show_chr("A-CFAAA-ABAB")
        y "Ejém... Entonces, ¿qué más planeas hacer hoy?"
    return

label vday_choco_date_intro:

    if not renpy.seen_label("valentines_2021_date"):
        $ show_chr("A-BCAAA-ABAD")
        y "Siendo el día de San Valentín, y siendo una amante del chocolate y una mente curiosa, me preguntaba..."
        $ show_chr("A-ACDAA-ABAD")
        y "¿Cómo se hace el chocolate?{w} Debe ser un proceso bastante interesante, ¿no crees?"
        $ show_chr("A-ABAAA-ABAD")
        y "Así que investigué un poco, y encontré un popular museo del chocolate ubicado en Malagos."
        $ show_chr("A-ACAAA-ABAB")
        y "Después de investigar lo suficiente, creo que fui capaz de hacer una réplica bastante fiel del museo, así que me gustaría visitarlo, si no te importa."
        $ show_chr("A-ACAAA-ABAB")
        y "Déjame traerlo..."
        call valentines_2021_date
    else:
        $ show_chr("A-ACAAA-ABAB")
        y "Dado que es el día de San Valentín, y estoy de humor para chocolate, estaba pensando que podríamos visitar el museo del chocolate de nuevo."
        $ show_chr("A-ACAAA-ABAD")
        y "¿Te parece bien?"
        menu:
            "¡Por supuesto!":
                $ show_chr("A-GCAAA-ABAD")
                y "¡Genial! Déjame solo..."
                call valentines_2021_date
            "En realidad tenía otras ideas...":
                $ show_chr("A-CCAAA-ABAB")
                y "Eso está perfectamente bien."
                $ show_chr("A-ACAAA-ABAB")
                y "Entonces, ¿qué estabas pensando?"
    return

label vday_choco_date_request:
    $ show_chr("A-ABAAA-ABAK")
    y "De hecho, sí. Tuve una idea para una nueva cita a la que podríamos ir."
    call vday_choco_date_intro
    return




label valentines_2021_date:

    image event chocolate_1:
        "images/events/valentines/1.png"
    image event chocolate_2:
        "images/events/valentines/2.png"
        zoom 0.7
    image event chocolate_3:
        "images/events/valentines/3.png"
        yalign 0.5 zoom 0.7
    image event chocolate_4:
        "images/events/valentines/4.png"
        yalign 0.1
    image event chocolate_5:
        "images/events/valentines/5.png"
        yalign 0.9 zoom 0.7
    image event chocolate_6:
        "images/events/valentines/6.png"
        zoom 0.7
    image event chocolate_7:
        "images/events/valentines/7.jpg"
        zoom 0.9

    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide halloween_cupcake
    show black zorder 20
    with Dissolve(2.0)
    pause 0.5
    $ hide_yuri_sit = True
    hide black zorder 20
    show event chocolate_1 zorder 10
    with Dissolve(2.0)

    python:
        if not persistent.costume in ["school", "sweater", "valentines"]:
            temp_costume = "sweater"
        else:
            temp_costume = persistent.costume
    pass

    if temp_costume == "school":
        show yuri 1c zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bc zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1dc zorder 11 at t11
    if temp_costume != "valentines":
        y "Así que aquí estamos, el {b}Museo de Chocolate de Malagos{/b}, o mi versión de él en todo caso."
        if temp_costume == "school":
            show yuri 1b zorder 11 at t11
        if temp_costume == "sweater":
            show yuri 1bb zorder 11 at t11
        if temp_costume == "valentines":
            show yuri 1db zorder 11 at t11
        y "Este lugar existe en tu realidad en Filipinas.{w} Si bien no conozco tus circunstancias de viaje actuales, espero que ambos podamos disfrutar visitando esta recreación."
        if temp_costume == "school":
            show yuri 2j zorder 11 at t11
        if temp_costume == "sweater":
            show yuri 2bj zorder 11 at t11
        if temp_costume == "valentines":
            show yuri 3db zorder 11 at t11
        y "Junto a este museo hay una granja de cacao local donde crean chocolate galardonado desde la semilla hasta confitería finamente elaborada."
        if temp_costume == "school":
            show yuri 1b zorder 11 at t11
        if temp_costume == "sweater":
            show yuri 1bb zorder 11 at t11
        if temp_costume == "valentines":
            show yuri 1db zorder 11 at t11
        y "Estamos tomando lo que llaman el {i}Tour del Árbol a la Barra{/i} donde vamos a ver una granja de chocolate real y aprender un poco sobre la historia del chocolate..."
        if temp_costume == "school":
            show yuri 3m zorder 11 at t11
        if temp_costume == "sweater":
            show yuri 3bm zorder 11 at t11
        if temp_costume == "valentines":
            show yuri 3dc zorder 11 at t11
        y "Después, habrá una barra de chocolate donde tendremos algunos dulces y..."
        y "Mhmmm..."
        if temp_costume == "school":
            show yuri 1d zorder 11 at t11
        if temp_costume == "sweater":
            show yuri 1bd zorder 11 at t11
        if temp_costume == "valentines":
            show yuri 1dd zorder 11 at t11
        y "Dejaré la última parte como una sorpresa. Créeme, ¡la disfrutarás!"
    else:
        y "Espero que no te importe que use esto de nuevo, volviendo aquí."
    if temp_costume == "school":
        show yuri 1f zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bf zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1da zorder 11 at t11
    y "¡Oh! No sé si viste, pero los desarrolladores mencionaron que tuvieras listo un poco de chocolate caliente para más tarde..."
    if temp_costume == "school":
        show yuri 1a zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1ba zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1da zorder 11 at t11
    y "Entonces, me gustaría comenzar si estás listo. Nuestra primera parada será la granja..."
    show event chocolate_2 with Dissolve(2.0)

    if temp_costume == "school":
        show yuri 1i zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bi zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1db zorder 11 at t11
    y "Guau, árboles de cacao con fruta hasta donde alcanza la vista... realmente no la llaman granja por nada."
    if temp_costume == "school":
        show yuri 1m zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bm zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1dc zorder 11 at t11
    y "Mhm... una lástima que no puedas oler esto... es un aroma tan único..."
    if temp_costume == "school":
        show yuri 1b zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bb zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1db zorder 11 at t11
    y "Según tengo entendido, si bien se ven deliciosas, la fruta real en sí no tiene ni una pizca de sabor a chocolate, sino que tiene un sabor bastante desagradable por fuera, con una pulpa dulce similar a la limonada por dentro."
    if temp_costume == "school":
        show yuri 2f zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 2bf zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 3db zorder 11 at t11
    y "En realidad es un error popular que la fruta sea de lo que está hecho el chocolate, pero en realidad son las semillas de la fruta, o sus granos como se les conoce cuando se fermentan y tuestan, los que le dan al chocolate su sabor."
    if temp_costume == "school":
        show yuri 2l zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 2bl zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 3da zorder 11 at t11
    y "Dicen que el grano de cacao en el interior puede oler a cualquier cosa, desde sudor hasta repollo cocido, pero huele... terroso, con solo un toque de especias... muy extraño."
    if temp_costume == "school":
        show yuri 1k zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bk zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1dc zorder 11 at t11
    pause 1.0
    y "Probablemente no fue una gran idea usar ropa en capas aquí."
    if temp_costume == "school":
        show yuri 1q zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bq zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1da zorder 11 at t11
    y "Al menos sé que mi script de clima funciona... aunque solo sea {b}en contra{/b} de mí hoy."
    if temp_costume == "school":
        show yuri 1b zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bb zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1db zorder 11 at t11
    y "En fin, suficiente quejas. Me pregunto si a alguien le importaría si toco las frutas..."
    if temp_costume == "school":
        show yuri 1g zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bg zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1db zorder 11 at t11
    y "Oh, espera un segundo... casi olvido que no hay nadie por aquí. Lo que significa..."
    if temp_costume == "school":
        show yuri 1j zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bj zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1dc zorder 11 at t11
    y "Puedo tocar lo que me plazca..."
    if temp_costume == "school":
        show yuri 3e zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 3be zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1da zorder 11 at t11
    y "Increíble... la cáscara se siente tan... correosa. Esperaba algo más por la apariencia. Es... asombroso..."
    if temp_costume == "school":
        show yuri 2a zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 2ba zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 3da zorder 11 at t11
    y "Pero de alguna manera también dura al mismo tiempo..."
    if temp_costume == "school":
        show yuri 1a zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1ba zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1da zorder 11 at t11
    y "Me pregunto, ¿alguna vez has sentido la cáscara de una fruta de cacao?"
    menu:
        "De hecho, sí.":
            if temp_costume == "school":
                show yuri 1b zorder 11 at t11
            if temp_costume == "sweater":
                show yuri 1bb zorder 11 at t11
            if temp_costume == "valentines":
                show yuri 1db zorder 11 at t11
            y "Qué interesante. Yo... como que quiero quedarme con esta. Tal vez lo haga... sería una decoración verdaderamente exótica, imagino."
        "Para nada hasta ahora.":
            y "Si alguna vez tienes la oportunidad, deberías probarlo. He tenido bastante curiosidad sobre esto antes de que viniéramos aquí."
    if temp_costume == "school":
        show yuri 1b zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bb zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1db zorder 11 at t11
    y "Dato curioso mal entendido, los granos de la fruta de cacao son en realidad de un blanco pastoso. Pensarías que serían de alguna forma de marrón, pero no..."
    if temp_costume == "school":
        show yuri 1j zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bj zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1db zorder 11 at t11
    y "Ah, pero sobre el cacao en sí... Lo que hacen con las frutas es abrirlas y tomar los granos, y abrirlos para obtener la parte negra parecida a un frijol en el interior que le da a los sólidos de chocolate su color, que coloquialmente se llaman {b}nibs{/b}."
    if temp_costume == "school":
        show yuri 1k zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bk zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1db zorder 11 at t11
    y "Las cáscaras de la fruta y del grano en sí mismas son en realidad descartadas..."
    y "Imagina cultivar una fruta tan grande para un rendimiento tan pequeño... no es de extrañar que las granjas sean tan grandes."
    if temp_costume == "school":
        show yuri 1a zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1ba zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1da zorder 11 at t11
    y "Ah, y creo que la siguiente parte del tour estaba dentro de su museo."
    show event chocolate_3 with Dissolve(2.0)


    if temp_costume == "school":
        show yuri 1a zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1ba zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1da zorder 11 at t11
    y "Aquí estamos. Así que echemos un vistazo a los alrededores, ¿te parece?"
    if temp_costume == "school":
        show yuri 1d zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bd zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1dd zorder 11 at t11
    y "Este de aquí parece interesante. Déjame hacerme a un lado para que puedas verlo..."
    hide yuri

    y "Ya escuché sobre este. Ese es el {b}Cinturón del Cacao{/b}, un cinturón delgado de 20 grados desde cada lado del ecuador. Estos son los únicos lugares donde crece el Cacao."
    y "Aquí dice que el cacao prospera en alta humedad y solo con mucha lluvia. 40 a 100 pulgadas por año..."
    y "Un tercio de la cosecha mundial de cacao proviene de {b}Costa de Marfil{/b}. Ghana e Indonesia son competidores cercanos."
    y "Ahora comienzo a entender por qué el chocolate de alta calidad con un alto contenido de cacao real se vuelve tan increíblemente caro. No lo dice directamente, pero el panel implica que realmente no puedes cultivar cacao en invernaderos."
    y "Espero no sonar como una maestra demasiado entusiasta en este momento. Solo te digo esto porque asumo que realmente no puedes ver las letras tan bien desde allá."
    y "¿Siquiera... estás disfrutando este viaje en absoluto?"
    menu:
        "De hecho, encuentro todo esto muy interesante.":
            y "Me alegra. Casi tuve miedo por un momento."
        "Ya sabía mucho de lo que me acabas de contar, pero aún disfruto del viaje, no te preocupes.":
            y "¡Oh! ¡Ya veo! Así que ya estás por delante de mí aquí."
    y "¡Oh! ¿Podemos ir allá por favor? Esto parece interesante..."
    show event chocolate_4 with Dissolve(2.0)




    y "Así que así es como se ven los granos en sus diferentes etapas..."
    y "Los {i}nibs{/i}, como se les llama, son de lo que realmente está hecho el chocolate."
    y "Los granos se fermentan, secan y tuestan durante un período de días, a veces tomando más de dos semanas para alcanzar su mejor estado."
    y "Después de que todo eso está hecho, se quitan las cáscaras y el nib interior se muele y licua, resultando en chocolate líquido puro: Licor de chocolate que, a pesar del nombre, es libre de alcohol."
    y "El licor luego se divide en manteca de cacao, que es lo que le da al chocolate su textura, y sólidos de chocolate, que se muelen en polvo y le dan al chocolate su sabor y color."
    y "Es una lástima que no puedas oler el aire aquí. Todo este lugar huele a chocolate... un aroma tan suave y apetitoso...{w} Delicioso~"
    y "Te... contaré un pequeño secreto..."
    y "Es muy común que las chicas amen el chocolate... Se han hecho muchos estudios, con conclusiones que van desde que el cuerpo encuentra el chocolate más sustentador hasta ayudar con el estrés. Supongo que simplemente hay algo en él que lo hace tan agradable."
    y "Bueno, excepto los alérgicos a él, obviamente."
    if persistent.chocall:
        y "Ah... ¡Olvidé que eras alérgico a los chocolates, lo siento!"
    y "Trato de mantenerlo con moderación, pero tengo que admitir que no siempre tengo éxito. Un buen trozo de chocolate siempre me ayuda en los días difíciles."
    y "Y como ya sabes, no me faltaron esos en el pasado."
    y "Por cierto, ¿sabías que el chocolate negro se produce agregando grasa y azúcar a las mezclas de cacao? Diferentes cantidades dan diferentes sabores, dependiendo de cuál se use más."
    y "Una mayor cantidad de cacao generalmente resulta en un chocolate más amargo. Menos azúcar resulta en lo que podrías llamar chocolate semidulce."
    y "Cuando la mezcla es aproximadamente un tercio de azúcar, manteca de cacao y vainilla, esto es chocolate agridulce. Tiene menos azúcar que el chocolate semidulce, como adivinarías."
    y "Una forma fácil de saber qué chocolate es qué tipo es mirando los ingredientes. La mayoría listará la cantidad de cacao utilizada, como digamos 70%%. Este chocolate de ejemplo probablemente sería agridulce."
    y "En fin, tenemos una cosa más guardada para hoy, la parte por la que he estado más emocionada."
    y "Te prometí una sorpresa cuando llegamos, creo que ahora es un buen momento para revelarla. Ven, quiero mostrarte la última parada de nuestra aventura."
    show event chocolate_5 with Dissolve(2.0)






    if temp_costume == "school":
        show yuri 1a zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1ba zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1da zorder 11 at t11
    y "Aquí estamos. La barra de chocolate."
    if temp_costume == "school":
        show yuri 1j zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bj zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1db zorder 11 at t11
    y "Ciertamente, está un poco vacía en este momento... aunque eso significa que el lugar está reservado para nuestro propio disfrute."
    if temp_costume == "school":
        show yuri 1u zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bu zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1dc zorder 11 at t11
    y "Pero, no estamos aquí para {b}solo{/b} comer chocolate, no ahora mismo al menos..."
    if temp_costume == "school":
        show yuri 3d zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 3bd zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 3dd zorder 11 at t11
    y "¡Estamos aquí para hacer el nuestro!"
    if temp_costume == "school":
        show yuri 1c zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bc zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1dc zorder 11 at t11
    y "Primero decidiríamos la forma de nuestros bombones y elegiríamos un molde de goma por allá."
    if temp_costume == "school":
        show yuri 1d zorder 11 at t11
    if temp_costume == "sweater":
        show yuri 1bd zorder 11 at t11
    if temp_costume == "valentines":
        show yuri 1dd zorder 11 at t11
    y "Y luego, tenemos una variedad de ingredientes para elegir. Escuché que algunos de ellos son bastante exóticos... ¡veamos qué tan lejos podemos llevar esto!"
    show yuri at thide
    hide yuri
label critical_choco_point:
    $ hide_yuri_sit = True

    show event chocolate_6 zorder 9 with Dissolve(2.0)


    y "Natsuki lo pasaría genial aquí. Tal vez, cuando logre traerlas a todas de vuelta algún día, la traeré aquí."
    y "Pero de todos modos, estamos aquí por nuestra propia cita, por mucho que me encantaría mostrarle este lugar. Estoy segura de que disfrutaría esto..."
    y "Hay tantos chocolates aquí que siempre he querido probar..."
    y "Chocolate de lavanda, chocolate de menta, tantas combinaciones únicas de ingredientes..."
    y "¿Sabes qué? ¿No sería romántico si hiciéramos algo juntos en lugar de cada uno el suyo?"
    y "Sugeriría que tú agregues un ingrediente del estante superior, y luego yo agregaría uno del estante inferior."
    y "Así que, echa un vistazo, yo haré lo mismo mientras tanto."
    menu:
        "¿Caramelo de Durián? No exagerabas cuando dijiste que tienen algunos exóticos. Iré por ellos.":
            y "¡Oh, nunca he probado la fruta Durián! ¡Tengo mucha curiosidad por saber cómo saben!"
        "Algunas frutas irían genial con la dulzura del chocolate, ¡creo que elegiré el Mango seco!":
            y "Una buena elección. De hecho me gusta mucho el Mango."
        "¡Oh, tienen Arándanos secos! He hecho mi elección.":
            y "Fueron muy populares hace unos años en tu mundo, ¿no? Estoy deseando probarlos yo misma."
        "Sultanas y Pasas secas... bastante similares, ¿cuál debería probar?":
            y "De hecho son bastante similares. Creo que la única diferencia es sobre cómo se secan. ¿Por qué no unas pocas de ambas?"
        "¿¡¿Sal de Roca?!? Inusual sin duda, pero creo que esto podría funcionar...":
            y "Creo que vi chocolate con sal marina una vez. ¡Realmente estoy esperando ver cómo resulta esto!"
    y "Yo también hice mi elección."
    if sanity_lvl() > 3:
        y "Las nueces siempre van bien con el chocolate. ¡Elegiré algunas nueces, solo para darle a nuestro chocolate algo de mordida!"
    else:
        if sanity_lvl() == 1:
            y "¡Siempre quise probar grillos cubiertos de chocolate, son toda una delicadeza en algunas partes del mundo! Tristemente, no tenemos de esos aquí. En su lugar..."
        y "Le agregaré algunas hojuelas de chile. Estoy de humor para un dulce castigo hoy."
        y "¿Sabes qué tienen en común tú y el chocolate con chile? Duele cuando doy un bocado..."
        y "Oh, {b}dije{/b} eso en voz alta, ¿no?"
    y "Siguiente... Mencioné antes que deberías traer un poco de chocolate caliente, así que si pudieras tener eso listo mientras preparo el mío."
    if temp_costume != "valentines":
        y "Estaré bebiendo un poco de Tsokolate, que es una bebida filipina de chocolate caliente. Me tomará unos minutos... Dirígete al café, estaré allí en un minuto."

        $ pitstop_bg = persistent.bg
        $ tc_class.transition("timecycle", "now")
        hide yuri
        hide screen jy_bg

        show event chocolate_7 zorder 9 with Dissolve(2.0)
        $ click_tea_button = 0
        call choco_timer

label enjoy_chocolate:
    if temp_costume != "valentines":
        hide screen choco_timer


        y "¡Bien, el Tsokolate está listo!"
        y "También tengo una sorpresa..."


        $ hide_yuri_sit = False
        $ current_timecycle_marker = "_day"
        $ persistent.costume = "valentines"
        show black zorder 20 with Dissolve(1.0)

        $ show_chr("A-BCBAA-ALAK")
        hide black with Dissolve(1.0)
        y "...¿T-Te gusta?"
        menu:
            "¡Te ves hermosa!":
                $ show_chr("A-CCBAA-ALAK")
                y "Gracias... estaba un poco nerviosa por usarlo, ya que no soy realmente de usar algo como esto..."
                $ show_chr("A-ACBAA-ALAK")
                y "Sin embargo, el calor me estaba afectando, y considerando la importancia de la cita, pensé que sería una buena manera de matar dos pájaros de un tiro, podrías decir."
            "Realmente no, lo siento.":
                karma -10
                $ show_chr("A-BFBAA-ALAL")
                y "O-Oh... Bueno, si no te importa, me gustaría mantenerlo puesto..."
                $ show_chr("A-CFBAA-ALAL")
                y "El calor me está afectando... Aunque no me importa una taza rica y caliente para calmar la mente y el corazón."
    else:
        $ pitstop_bg = persistent.bg
        $ tc_class.transition("timecycle", "now")
        hide yuri
        hide screen jy_bg
        $ current_timecycle_marker = "_day"

        show event chocolate_7 zorder 9 with Dissolve(1.0)
        $ hide_yuri_sit = False
        $ show_chr("A-AAAAA-ANAE")
        y "Es agradable sentarse de nuevo después de otro paseo por este lugar."
    $ show_chr("A-AAAAA-ANAE")
    y "Así que, ambos tenemos nuestro chocolate caliente... Nunca he probado el Tsokolate, pero he leído que es un tipo de chocolate caliente increíblemente sabroso."
    $ show_chr("A-GBAAA-ANAE")
    y "¡Así que, salud!"
    $ show_chr("A-CCAAA-ANAE")
    y "..."
    $ show_chr("A-IBAAA-ANAE")
    y "¡Guau, no mentían! Es tan rico y cremoso... Una muy buena manera de terminar el día."
    $ show_chr("A-ACAAA-ANAE")
    y "El Tsokolate se hace agregando pequeñas tabletas de granos de cacao molidos y tostados, llamadas {i}tabliya{/i}, a una mezcla de agua hirviendo y leche."
    $ show_chr("A-BBAAA-ANAD")
    y "Puedes agregar cacao en polvo normal en lugar de la mencionada tabliya, pero eso generalmente está mal visto ya que no sabe igual."
    $ show_chr("A-ACAAA-ANAN")
    y "Después de agregar la tabliya, generalmente se mezcla con un bastón de madera llamado Molinillo."
    $ show_chr("A-ADAAA-ANAF")
    y "También hay casos donde las personas han agregado otros ingredientes a su Tsokolate, que van desde canela o vainilla hasta tequila."
    $ show_chr("A-BFAAA-ANAC")
    y "Ahora que lo pienso, un poco de canela estaría bien..."
    $ show_chr("A-ABAAA-ANAN")
    y "Oh, pero ¿cómo está tu chocolate caliente?"
    menu:
        "¡Está genial!":
            $ show_chr("A-ACAAA-ANAK")
            y "¡Me alegra escuchar eso! Compartir un chocolate caliente contigo es uno de los momentos más destacados de mi vida."
        "En realidad... no hice ninguno.":
            $ show_chr("A-CCBAA-AIAI")
            y "[player]... Te lo dije al principio {i}y{/i} antes de hacer el mío, así que no tienes excusa."
            $ show_chr("A-BBAAA-AMAM")
            y "Supongo que tendré que disfrutar de este refrescante y delicioso chocolate caliente yo sola..."
        "No tan genial en realidad... puede que haya hecho algo mal...":
            $ show_chr("A-AFBAA-ANAE")
            y "Lamento escuchar eso. Tal vez la próxima vez salga mejor."
    y "Sabes, este lugar es más que un museo y un café... ¡tienen un spa, un jardín con varios espectáculos de aves, e incluso un pequeño zoológico de mascotas!"
    y "Realmente sería un gran lugar de vacaciones, ¿eh?"
    y "Oh, algo que leí sobre el spa..."
    y "Todos los productos que usan en sus tratamientos están hechos con ingredientes de la fruta de cacao que cultivan allí."
    y "Así que no dependen de productos de otras compañías, haciendo que el spa sea autosostenible. Muy inteligente, ¿no es así?"
    if persistent.lovecheck:
        y "Imagina, después de recibir un agradable masaje relajante, nos dirigimos a una de las villas para descansar..."
        y "Nos acostamos en la cama, cómodamente acurrucados juntos, dándonos un beso de buenas noches mientras nos quedamos dormidos..."
        y "Por supuesto, esa es una forma en que podría ir... pero no seré demasiado descriptiva."

    $ show_chr("A-ABGAA-ANAD")
    y "Oh, por cierto..."
    $ show_chr("A-BCAAA-ANAD")
    y "No estoy segura de si te diste cuenta de esto, pero dado que yo hice este lugar, y no hay nadie más alrededor..."
    $ show_chr("A-GBAAA-ANAD")
    y "¡Literalmente tenemos nuestra propia granja de chocolate!"
    $ show_chr("A-BCBAA-AMAM")
    y "Por supuesto, no sabemos exactamente cómo manejarla..."
    $ show_chr("A-ACFAA-AMAM")
    extend " pero estoy segura de que podemos aprender."
    $ show_chr("A-ICAAA-ALAL")
    y "Espero que planees traerme de vuelta aquí alguna vez... Esto fue divertido..."

label museumend:
    $ show_chr("A-ACAAA-ABAB")
    y "En fin, me divertí mucho hoy. Estoy agradecida de haber tenido la oportunidad de traerte aquí."
    y "Oh, no estoy segura de si siquiera mencioné esto pero. ¡Basé este lugar en un museo de chocolate {b}real{/b} de tu mundo!"
    y "Este lugar se llama {b}Malagos{/b}, ubicado en Filipinas creo. Así que si alguna vez buscas un buen lugar para pasar tus próximas vacaciones, ¡ya sabes a dónde ir ahora!"
    $ show_chr("A-BBAAA-ABAB")
    y "¡Oh! Y el chocolate ya se enfrió. Este tendrá un lugar muy especial cuando lleguemos a casa."
    $ show_chr("A-CCAAA-ABAB")
    y "Sabes, hay cierto armario donde cierto alguien siempre guardaba su colección de Manga. Creo que allí encajaría muy bien."
    $ show_chr("A-ACAAA-ABAB")
    y "Vamos a casa por ahora. Y de nuevo, gracias por ir a esta cita conmigo..."
    show black zorder 20 with Dissolve(1.0)
    hide event chocolate_5

    if persistent.bg == "space":
        $ tc_class.transition("space", speed="now")
    elif persistent.bg == "timecycle":
        $ tc_class.transition("timecycle", speed="now")
    elif persistent.bg == "yuri_desk":
        $ tc_class.transition("yuri_desk", speed="now")
    elif persistent.bg == "yuri_kotatsu_1":
        $ tc_class.transition("yuri_kotatsu_1", speed="now")
    elif persistent.bg == "yuri_kotatsu_2":
        $ tc_class.transition("yuri_kotatsu_2", speed="now")
    show screen jy_bg
    pause 0.5
    hide black zorder 20 with Dissolve(1.0)
    $ _skipping = False
    $ persistent.dates_taken += 1
    jump ch30_loop

label choco_timer:
    screen choco_timer():
        vbox:
            style_prefix "talkbutton"
            textbutton "Entrar" action Jump("choco_wait")
            xalign 0.50
            yalign 0.25

        timer 60.0 action Jump("enjoy_chocolate")
    if click_tea_button <= 1:
        show screen choco_timer()

label choco_wait:
    y "Por favor sé paciente, [player], solo necesito un minuto para prepararme."
    $ click_tea_button = click_tea_button + 1
    jump choco_timer
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

