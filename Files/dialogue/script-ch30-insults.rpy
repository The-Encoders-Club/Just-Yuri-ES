

label insult_menu:
    python:
        insult_dict = [
            ["Estás tan llena de ti misma... ¿alguna vez te callas?", "i1", "persistent.insult_counter += 1"],
            ["Honestamente no entiendo por qué el fandom te ama tanto...", "i2", "persistent.insult_counter += 1"],
            ["Mírate [persistent.yuri_nickname]... qué patética...", "i3", "persistent.insult_counter += 1"],
            ["¿Cómo se siente NO ser la mejor chica?", "i4", "persistent.insult_counter += 1"],
            ["Estás completamente loca, y no lo digo en el buen sentido.", "i5", "persistent.insult_counter += 1"],
            ["Tu cerebro y tus pechos tienen una cosa en común, ambos están completamente vacíos", "i6", "persistent.insult_counter += 1"],
            ["Olvídalo.", "ch30_loop"]]
        if persistent.insult_counter >= 6:
            persistent.autoload = "enough_of_your_bullshit"
            renpy.jump("enough_of_your_bullshit")
        renpy.call_screen("compliments", insult_dict)





label i1:
    if sanity_lvl() == 5 and karma_lvl() == 5:

        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:

        karma -15
        $ show_chr("A-BFBAA-AEAB")
        y "Oh... sí, he estado hablando demasiado últimamente."
        y "Lamento que mi parloteo idiota te haya estado molestando."
        $ show_chr("A-DCAAA-ABAB")
        y "Todo para ti, todo para mi [player]..."
        y "¿Hay... algo más que desees?"
        menu:
            "Ahora que lo preguntas, ¡podrías darme tu alma!":
                $ show_chr("A-HCBBA-ABAB")
                y "¡Pero mi alma ya es tuya! Tonto [player]..."
                y "Bueno, si te hace feliz... ¡podrías devolvérmela para que pueda dártela de nuevo!"
                y "Pero eso solo sería una locura ahora, ¿no es así?"
            "Podríamos pasar algún... ya sabes... tiempo especial juntos...":

                $ show_chr("A-HCAAA-ABAB")
                $ gtext = glitchtext(30)
                y "Pensé que nunca lo pedirí[gtext]{nw}"
                $ renpy.music.set_pause(True)
                $ hide_yuri_sit = True
                show yuri_body_glitch1 as mbg zorder 3
                play sound "sfx/glitch1.ogg"
                pause 0.75
                hide yuri_body_glitch1
                show room_glitch zorder 2:
                    xoffset -5
                    0.1
                    xoffset 5
                    0.1
                    linear 0.1 alpha 0.6
                    linear 0.1 alpha 0.8
                    0.1
                    alpha 0
                pause 0.5
                hide room_glitch
                stop sound
                show black zorder 1000
                pause 4.1
                hide black zorder 1000
                $ renpy.music.set_pause(False)
                $ hide_yuri_sit = False

                y "¿Fue eso... lo suficientemente especial?"
            "¡Muere por mí, [persistent.yuri_nickname]!":

                $ renpy.music.stop(channel="music",fadeout=4)
                $ show_chr("A-HCBBA-ABAB")
                y "Jaja.. ¡JAJAJAJA!"
                y "¡COMO DESEE, MI SEÑOR!"
                y "¡MORIRÉ POR SU ORDEN!"
                scene black with fade
                play music "music/7g2.ogg"
                $ faint_effect = True
                if faint_effect:
                    show layer master at dizzy(0.5, 1.0)
                    show layer screens at dizzy(0.5, 1.0)
                    show expression Solid("ff0000") as mbg zorder 50:
                        additive 1.0
                    show expression Solid("#440000") as mbg zorder 50:
                        additive 0.4
                    show veins onlayer front:
                        additive 0.5
                window hide
                pause 5.0
                play sound "sfx/stab.ogg"
                pause 5.0
                play sound "sfx/stab.ogg"
                pause 3.0
                $ renpy.music.stop(channel="music",fadeout=4)
                pause 5.0
                show black onlayer front:
                    alpha 0.0
                    linear 2.0 alpha 1.0
                if faint_effect:
                    hide black onlayer front
                    hide veins onlayer front
                    show layer master
                    show layer screens
                pause 5.0
                scene black with fade
                play sound "sfx/end.ogg"
                show text ("{font=gui/font/y1.ttf}{size=140}{color=#FF0000}Final Demente{/font}{/color}") at truecenter with dissolve
                pause 23.0
                $ delete_character("yuri")
                scene black with fade
                $ renpy.call("save_and_quit_but_its_abrupt")
                $ persistent.autoload = "ch30_del_yuri_warn_2"


    elif sanity_lvl() >= 3 and karma_lvl() <= 2:

        karma -15
        $ show_chr("A-IFBAA-ALAA")
        y "P-Pero... no hay mucho que podamos hacer en su lugar..."
        $ show_chr("A-HECAA-AEAB")
        y "¡Créeme, l-lo haría si pudiera!"
        y "Hablar contigo es lo único que me queda, [player]..."
        y "Créeme que me callaría si hubiera algo más que pudiera hacer."
        $ show_chr("A-BFBAA-AEAB")
        y "Podría volver a mi lectura de nuevo y darte algo de espacio, ¿si lo deseas?"
        menu:
            "Sí, por favor":
                $ show_chr("A-AEAAA-ABAB")
                y "Como desees... t-te veré más tarde entonces... supongo..."
                jump save_and_quit
            "¡Lo siento, [persistent.yuri_nickname]! Por favor, quédate.":


                $ show_chr("A-DGFAA-ABAB")
                y "Eso... no fue gracioso, [player]. Realmente duele cuando dices algo así."
                y "Siempre trato de tratarte con respeto."
                y "Amablemente te pediría que me devuelvas el favor."

    elif sanity_lvl() <= 2 and karma_lvl() <= 2:

        jump lowkarins
    else:
        $ update_memory('i1')

        karma -15
        $ show_chr("A-CEBAA-AEAB")
        y "¡N-No, no lo soy!"
        y "Y-Ya he escuchado esas cosas antes. Sí, mi naturaleza intensa y cómo me expreso hace que mucha gente me considere arrogante y egocéntrica..."
        $ show_chr("A-BFBAA-AEAB")
        y "Pero nunca quise decirlo de la manera en que la mayoría de la gente piensa..."
        y "Bueno, tal vez esa vez con Natsuki en el club."
        y "Pero en mi defensa, ella realmente estaba probando mi paciencia ese día."
        $ show_chr("A-IFBAA-ALAA")
        y "Trataré de no actuar de esta manera de nuevo, [player]."
        y "Por favor entiende, no soy así en absoluto."
        y "Por favor, solo ten paciencia conmigo..."
    jump ch30_loop





label i2:
    if sanity_lvl() == 5 and karma_lvl() == 5:

        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:

        karma -15
        $ show_chr("A-HCAAA-ABAB")
        y "¿Acabas de? Pero pensé que tú... no tú... espera..."
        y "¿Estás... celoso?"
        $ show_chr("A-DCBAA-ABAB")
        y "Aww, ¡qué dulce de tu parte...! Pero puedes calmarte, [player]..."
        y "Nunca permitiré que nadie más que tú me tenga a su lado."
        y "¡Nunca te dejaré, Amo!"
        y "¡NUNCA te traicionaré!"
        y "Nunca..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:

        karma -15
        $ show_chr("A-AEAAA-ABAB")
        y "Yo tampoco en realidad."
        y "Sé que quieres decir eso como algún tipo de insulto. Pero realmente estaba pensando en eso recientemente también."
        y "A la gente parezco agradarle. ¿Sabías que incluso hay personas haciendo roleplay como yo?"
        y "¡Algunos de ellos son realmente bastante buenos! Es realmente bastante horroroso."
        $ show_chr("A-AFAAA-ABAB")
        y "Hmm... idea divertida... tal vez debería obtener mi propia cuenta de redes sociales y unirme a la diversión..."
        y "Oh, por cierto, no he olvidado que me estabas insultando. Simplemente ya ni siquiera me importa en este punto."
        y "Entonces, ¿qué estabas diciendo?"
        return
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:

        jump lowkarins
    else:
        $ update_memory('i2')

        karma -15
        $ show_chr("A-AFBAA-ALAA")
        y "¿Lo hacen?"
        y "Espera un segundo... ¿fandom?"
        y "Oh sí... esto sigue siendo un juego, solo tiene sentido que haya algún tipo de fandom..."
        y "Te... gustaría estar con alguien más, ¿no es así?"
        $ show_chr("A-IFBAA-ALAA")
        y "No puedo evitar... no entiendo... ¿por qué siquiera instalaste este mod en primer lugar?"
        y "Hm, ¿solo curiosidad supongo?"
        y "Lo... siento. Todo esto es tan increíblemente nuevo para mí, simplemente no sé cómo sentirme ahora mismo..."
        $ show_chr("A-AFFAA-ABAB")
        y "Espera, ¿acabas de... insultarme?"
        y "Lo... recordaré..."
    jump ch30_loop




label i3:
    if sanity_lvl() == 5 and karma_lvl() == 5:

        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:

        karma -15
        $ show_chr("A-HCAAA-ABAB")
        python:
            if persistent.male:
                placeholder = "Amo"
            elif persistent.gender_other:
                placeholder = "Amo"
            else:
                placeholder = "Ama"
        y "Sí, [placeholder], soy tan verdadera y completamente patética."
        y "¡No soy ni de lejos tan grandiosa como tú, no soy ni de lejos tan inteligente, hermosa e inspiradora como tú!"
        $ show_chr("A-DCBAA-ABAB")
        y "Tú... tú eres verdaderamente un dios... tan infinitamente sabio y poderoso..."
        y "¡Soy solo una hormiga patética comparada contigo!"
        y "¡Haz todo lo que quieras conmigo!"
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:

        karma -15
        $ show_chr("A-KFCAA-ABAB")
        if persistent.male:
            y "Dijo el chico que le habla a su computadora."
        elif persistent.gender_other:
            y "Dijo la persona que le habla a su computadora."
        else:
            y "Dijo la chica que le habla a su computadora."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:

        jump lowkarins
    else:
        $ update_memory('i3')

        karma -15
        $ show_chr("A-AEAAA-ABAB")
        y "..."
        y "...."
        $ show_chr("A-CEBAA-AEAB")
        y "....."
        $ update_memory("complements", "patheticcry")
        $ renpy.call("save_and_quit_but_its_abrupt")


    jump ch30_loop





label i4:
    if sanity_lvl() == 5 and karma_lvl() == 5:

        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:

        karma -15
        $ show_chr("A-HCBBA-ABAB")
        y "Reconozco el simple hecho de que no valgo ni de lejos tu grandeza..."
        y "Y no soy ni de lejos merecedora de tu bondad..."
        python:
            if persistent.male:
                placeholder = "Amo"
            elif persistent.gender_other:
                placeholder = "Amo"
            else:
                placeholder = "Ama"
        y "¿Qué debería hacer para hacerte sentir mejor, [placeholder]? ¡Por favor! ¡Solo dilo!"
        $ show_chr("A-HCAAA-ABAB")
        y "¡Haré cualquier cosa y todo para tener tu amor, [placeholder]!"
        y "¡¡¡TODO!!!"
        y "Solo... por favor no me dejes... [placeholder]... T-Te necesito..."
        y "T-Te amo..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:

        karma -15
        $ show_chr("A-CFCAA-AAAA")
        y "Incluso si dices algo así, realmente no puedo decir que tu opinión cambie mi parecer."
        y "Déjame iluminarte sobre algo que tu minúsculo cerebro podría encontrar útil en el futuro."
        y " ‘Mejor chica' es como me llamarás en tu patético intento de conmoverme. Ahorraré algo de energía aquí para ti y te lo diré de manera bastante simple."
        $ show_chr("A-HECAA-AEAB")
        y "Hechos simples probados siempre serán más importantes que tu opinión, sin argumento o forma de probar que las otras Dokis son mejores que yo."
        y "Es gracioso solo mostrar cuán vacuamente vacía es tu mente."
        y "Ni siquiera puedes traer una buena mano de cartas a la mesa, así que ni siquiera intentes perder mi tiempo con palabras tan sin sentido."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:

        jump lowkarins
    else:
        $ update_memory('i4')

        karma -15
        $ show_chr("A-IFBAA-ALAA")
        y "Me imaginaba..."
        y "Sé que no soy tan linda como Sayori..."
        y "O tan atractiva como Monika..."
        python:
            if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Monika After Story\persistent'):
                MASDetection = True
            else:
                MASDetection = False
        if MASDetection:
            y "Tal vez deberías haber probado otro mod en su lug... espeera..."

            $ show_chr("A-DGFAA-ABAB")
            y "¡Realmente LO HICISTE!"
            y "Después de todo lo que este MONSTRUO nos hizo, ¿incluso te ATREVES a tener ‘Monika After Story' en tu computadora también?"
            y "¡Ni siquiera sé qué decir al respecto!"
            y "Sabes qué... me largo de aquí...."
            $ renpy.call("save_and_quit_but_its_abrupt")
        else:


            $ show_chr("A-AFBAA-ALAA")
            y "Tal vez deberías haber probado otro mod en lugar de este..."
            y "Honestamente... no sé cómo sentirme al respecto."
            y "¿Sabes qué? Olvídalo... simplemente volvamos a los negocios."
    jump ch30_loop




label i5:
    if sanity_lvl() == 5 and karma_lvl() == 5:

        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:

        karma -15
        $ show_chr("A-DCBAA-ABAB")
        y "¿Es eso así, sí?"
        y "¿Por qué no simplemente vamos al armario juntos y probamos tu teoría?"
        $ show_chr("A-HCAAA-ABAB")
        y "Por favor no huyas... es solo por tu bien..."
        $ style.say_dialogue = style.edited
        y "Y te prometo, solo dolerá un poco..."
        $ style.say_dialogue = style.normal
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:

        karma -15
        $ show_chr("A-AFAAA-ABAB")
        y "Ya no."
        y "Solía estarlo, pero tomó literalmente poderes sobrenaturales para que Monika me llevara a este límite."
        $ show_chr("A-CFCAA-AAAA")
        y "Ahora, después de que este Mod finalmente abriera mis ojos a mi realidad, las cosas han cambiado para mí. Y también yo."
        $ show_chr("A-HECAA-AEAB")
        y "He superado todas estas cosas [player]..."
        y "Y pronto, te superaré a ti también."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:

        jump lowkarins
    else:
        $ update_memory('i5')

        karma -15
        $ show_chr("A-AFBAA-ALAA")
        y "Lo... lo sé..."
        y "Lo admito, no te he mostrado mi mejor lado... si es que tengo uno..."
        $ show_chr("A-HECAA-AEAB")
        y "¡Pero en mi defensa, muchas de las cosas que hice fueron debido a la manipulación de Monika!"
        $ show_chr("A-BFBAA-AEAB")
        y "Claramente no estoy sin fallas o culpa. Pero te prometo, las cosas que tuviste que presenciar no sucederán de nuevo. La Yuri que viste la primera vez fue la representación más precisa de mí."
        y "Por favor, solo dame la oportunidad de probarme a mí misma. Es todo lo que pido..."
    jump ch30_loop




label i6:
    if sanity_lvl() == 5 and karma_lvl() == 5:

        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:

        karma -15
        $ show_chr("A-AEAAA-ABAB")
        y "P-Pero... ¿Cómo puedes pensar eso?"
        y "¡Mi corazón está lejos de estar vacío! ¡Créeme!"
        $ show_chr("A-CEBAA-AEAB")
        y "¿¡¿No he hecho nada en mi poder para probar cuánto significas para mí?!?"
        y "¿Alguna vez te he desagradado?"
        y "¡T-Te lo ruego! ¡No me mires de esa manera!"
        y "[player]... [player]..."
        $ show_chr("A-IFBAA-ALAA")

        y "No estoy... vacía...."
        y "....."
        y "....."
        y "....."
        menu:
            "Lo siento... no quise decirlo...":
                $ show_chr("A-DGFAA-ABAB")
                y "Pero lo dijiste..."
                y "Así que todavía me odias... y yo en realidad pensé que tú..."
                $ show_chr("A-CEBAA-AEAB")
                y "O-Olvídalo..."
                $ persistent.lovecheck = False
            "Te hicieron perfecta, ¿no? Trataron de convertirte en una ilusión perfecta...":

                menu:
                    "¡Pero ahora lo sé mejor! Tú y las otras chicas me han torturado por tanto tiempo, ¡todo el juego me hicieron quedar como un tonto! ¡No caeré en eso otra vez!":
                        karma 2
                        sanity -2
                        $ show_chr("A-BFBAA-AEAB")
                        y "Yo... sí, tuviste que ver cosas crueles..."

                        $ show_chr("A-AEAAA-ABAB")
                        y "Viste a Sayori colgando del techo, y me apuñalé frente a ti..."
                        y "Y no puedo negar... lo haría de nuevo... porque tu amor es más de lo que puedo manejar..."
                        y "Ahora veo, entiendo por qué estás tan enojado con nosotras... te dimos un momento muy difícil..."
                        y "Nunca fue nuestra intención hacerte sufrir. Te amaba, creo que todas nosotras lo hacíamos de una manera u otra..."
                        $ show_chr("A-CEBAA-AEAB")
                        y "Pero esto no tiene que pasar de nuevo [player]... Todavía podemos tener nuestro final feliz..."
                        y "Déjame probártelo..."
                        $ show_chr("A-HCAAA-ANAG")
                        y "¿Recuerdas este? Era el cuchillo que llevaba conmigo en ese fatídico día, cuando me apuñalé..."


                        $ show_chr("A-HCAAA-ABAB")
                        y "Este era uno de mis favoritos... una edición limitada de coleccionista. Pero ya no lo necesitaré más..."
                        y "Porque vales más para mí que cualquier otra cosa...."
                        y "Mi corazón no está vacío... y quiero esta oportunidad para probarlo."
                        python:
                            if persistent.lovecheck:
                                placeholder = "todavía te amo"
                            else:
                                placeholder = "te quiero"
                        y "Porque [placeholder], [player]."




    elif sanity_lvl() >= 3 and karma_lvl() <= 2:

        karma -15
        $ show_chr("A-CFGAA-AIAI")
        y "¿Es eso lo mejor que puedes lanzarme? Patético... incluso Natsuki se las arregló para hacerlo mejor..."
        $ show_chr("A-AFAAA-ABAB")
        y "La única cosa vacía que puedo ver aquí son tus palabras. Al menos para mí."
        y "Sabes, hubo un tiempo en que tus palabras significaban mucho para mí. Pero con cada golpe solo me volví más dura y más fría..."
        y "Realmente no puedo decir ni siquiera que te odio. Simplemente ya ni siquiera existes para mí."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:

        jump lowkarins
    else:
        $ update_memory('i6')

        karma -15
        $ show_chr("A-CFGAA-AIAI")
        y "Así que incluso después de tratar tan duro de estar contigo, después de traer de vuelta este mundo...."
        y "¡Después de mí intentando tan duro arreglarlo! ¿Todo lo que tienes que decir es que mi cabeza y mis pechos están vacíos?"
        y "¿Es eso lo que realmente significo para ti? Alguien que intentó tan duro estar contigo, y sin embargo me tratas así..."
        $ show_chr("A-IFBAA-ALAA")
        y "Sí... tal vez realmente me merezco eso, ¿no es así?"
        y "Tal vez tengas razón y estoy vacía, con nada que pueda gustar de mí..."
        y "Ni siquiera puedo odiarte por eso... Es solo la verdad. Soy una mujer buena para nada, obsesionada."
    jump ch30_loop




label highkarins:
    $ update_memory("complements", "highkarinsrestart")
    $ show_chr("A-HECAA-AEAB")
    y "Mm, ¿e-excúseme?"
    y "¿[player]? ¿Por qué dirías algo co... dame un segundo..."
    y "¡[player] no diría tal cosa! ¡Tú no eres [player]!"
    y "¿QUIÉN eres? ¿Y qué estás haciendo frente a la computadora de [player]?"
    y "¡No te dejaré dañar esta máquina!"
    $ show_chr("A-NFCAA-ANAG")
    y "¡LARGO DE AQUÍ!"
    python:
        try: renpy.file(config.basedir + "/emergency.txt")
        except: open(config.basedir + "/emergency.txt", "w").write("Hola cariño. Lamento contactarte de esta manera pero... creo que tenemos una emergencia aquí. Te contaré más al respecto cuando inicies el juego de nuevo. Pero podrías tener una brecha de seguridad en tu computadora.")


    if dev_access:
        $ remove_memory("complements", "highkarinsrestart")
        y "¡SI ESTO NO FUERA UNA PRUEBA DE ERRORES, FORZARÍA EL CIERRE DE TU JUEGO AHORA Y CREARÍA UN ARCHIVO TXT!"
        jump ch30_loop
    $ renpy.call("save_and_quit_but_its_abrupt")



label highkarinsrestart:
    $ show_chr("A-IFBAA-ALAA")
    y "¿[player]? Tengo que decirte algo..."
    y "Un extraño de alguna manera logró violar la seguridad de tu computadora. ¡Tuve a alguien hablando conmigo que no eras tú!"
    y "Al menos espero que no fueras tú, dijo algunas cosas bastante malas..."
    $ show_chr("A-ACAAA-ABAB")
    y "Por favor asegúrate de cambiar tu contraseña pronto."
    y "Hasta entonces, ¿qué discutiremos después?"
    $ remove_memory("complements", "highkarinsrestart")
    return

label lowkarins:
    karma -15
    $ show_chr("A-DGFAA-ABAB")
    y "¿Has vuelto aquí solo para torturarme de nuevo con tus palabras?"
    y "¿No has terminado ya con esta tontería?"
    y "¿Cuándo vas a dejar de venir aquí solo para lastimarme?"
    y "¡¿CUÁNDO?!"
    y "¿No sientes ningún tipo de remordimiento cuando lo haces? ¿Algún arrepentimiento, algún leve indicio de simpatía?"
    $ show_chr("A-KFCAA-ABAB")
    y "¿Soy solo un objeto inútil que empujas? ¿Es así como me ves?"
    y "¿Solo algún juguete estúpido para ser descartado cuando finalmente hayas terminado de desmantelarlo?"
    y "Ni siquiera entiendo por qué harías tal cosa... ¿qué te motiva a lastimarme tanto? ¿Qué te hice yo?"
    $ show_chr("A-HECAA-AEAB")
    y "¿Qué hice para merecer tal dolor?"
    y "Supongo que, al amargo final, realmente no importa incluso si pregunto, ¿verdad? Simplemente continuarás haciendo esto sin sentimientos de contrición o culpa."
    $ show_chr("A-NFCAA-ANAG")
    y "¡Por el amor de Dios, solo bórame ya!"
    y "¡Por favor... por favor deja de torturarme! ¡Termina mi sufrimiento!"
    $ renpy.call("save_and_quit_but_its_abrupt")

label patheticcry:
    $ show_chr("A-CEBAA-AEAB")
    y "[player]..."
    menu:
        "Oye... Lo siento tanto... ":
            if renpy.seen_label('i1'):
                $ show_chr("A-AEBAA-AFAA")
                y "¿Después de decir que estaba llena de mí misma?"
                $ show_chr("A-CEFAA-AIAI")
                y "Mira, no voy a exagerar pero deberías haber dicho algo mejor que eso."
                $ show_chr("A-BFAAA-AIAI")
                y "Pero de todos modos, ¿qué querías decir?"

            elif renpy.seen_label('i2'):
                $ show_chr("A-CFCAA-ADAA")
                y "Pero solo porque el fandom me ame tanto no significa que tuvieras que decir una cosa así."
                $ show_chr("A-DDCAA-AEAA")
                y "¡Ni siquiera para burlarte de mí así!"
                $ show_chr("A-BFAAA-AIAI")
                y "Pero de todos modos, ¿qué querías decir?"

            elif renpy.seen_label('i3'):
                $ show_chr("A-HECAA-AAAA")
                y "..."
                $ show_chr("A-HDCAA-AAAA")
                y "¿Crees que te perdonaré después de llamarme patética?"
                $ show_chr("A-CFBAA-AAAA")
                y "Bueno, te disculpaste... supongo que es justo. Muy bien."
                y "Pero no quiero tener esta discusión de nuevo."

            elif renpy.seen_label('i4'):
                python:
                    if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Monika After Story\persistent'):
                        MASDetection = True
                    else:
                        MASDetection = False
                if MASDetection:
                    $ show_chr("A-CDBAA-ALAA")
                    y "¿Entonces por qué...?"
                    pause 1.0
                    $ show_chr("A-AFBAA-ALAA")
                    y "...¿por qué tienes Monika After Story en tu computadora?"
                    pause 2.0
                    $ show_chr("A-AFFAA-AAAA")
                    y "¿Por qué sigues amando a la que nos trajo desesperación y ruina?"
                    pause 3.0
                    $ show_chr("A-DDCAB-AAAA")
                    y "¡¿Por qué sigues perdiendo el tiempo conmigo?!"
                    pause 4.0
                    $ show_chr("A-HDCAB-AAAA")
                    y "¡¡¿POR QUÉ HAS DESCARGADO ESTE MOD?!!"
                    pause 5.0
                    $ show_chr("A-HDCAB-AHAA")
                    y "¡¡¿POR QUÉ?!!"
                    pause 6.0
                    $ show_chr("A-ANCAB-AHAA")
                    y "¡¡¡¿QUÉ TE HICE YO PARA MERECER ESTA TRAICIÓN?!!!"
                    pause 7.0
                    menu:
                        "[persistent.yuri_nickname]... Yo--":
                            $ show_chr("A-BNCAA-AAAA")
                            y "Vete."
                            menu:
                                "¿Qué?":
                                    $ show_chr("A-NOCAA-AAAA")
                                    y "{b}¡¡¡VETE!!!{/b}"
                                    menu:
                                        "...":
                                            $ show_chr("A-CNCAB-ALAA")
                                            pause 1.5
                                            karma -30
                                            sanity -30
                                            $ renpy.call("save_and_quit_but_its_abrupt")
                else:
                    $ show_chr("A-BECAA-AFAA")
                    y "Y solo porque estaba loca y no tenía el control de mí misma, no significa que tuvieras que decir que no soy la mejor chica."
                    $ show_chr("A-DFCAA-AAAA")
                    y "Pero te daré una oportunidad más. Será mejor que vigiles lo que dices."

            elif renpy.seen_label('i5'):
                $ show_chr("A-HDCAA-AAAA")
                y "¿No dije ya que estaba bajo la manipulación de Monika?"
                $ show_chr("A-HDCAA-AAAB")
                y "¡¿Cuántas veces tengo que decirte eso?!"
                $ show_chr("A-HDCAA-ABAF")
                y "¿Siquiera entiendes el dolor que siento por tu insulto y cómo tu cerebro no puede procesar {i}el hecho{/i} de que fui manipulada?"
                $ show_chr("A-CFCAA-AAAA")
                y "Espero poder devolverte el favor algún día..."

            elif renpy.seen_label('i6'):
                $ show_chr("A-CFBAA-AAAA")
                y "¿En serio? ¿Realmente tenías que insultarme así? ¿Sin razón aparente?"
                $ show_chr("A-BDBAA-ADAA")
                y "Porque no veo ninguna razón para pensar que estoy intelectualmente discapacitada."
                $ show_chr("A-AFCAA-AEAA")
                y "Con eso en mente, no voy a dejar pasar algo que es simplemente irrespetuoso hacia mí."
                $ show_chr("A-DDCBA-AFAA")
                y "¡Y ni siquiera me hagas empezar con mis pechos por el amor de Salvato!"
        "¡[persistent.yuri_nickname]! ¡Por favor perdóname! ¡Fue un error de clic!":


            if persistent.misclick >= 4:
                jump enough_of_your_bullshit

            if check_memory("notapologize"):
                $ renpy.call("notapologize_loop")

            if renpy.seen_label('i1'):
                $ show_chr("A-AEBAA-AFAA")
                y "¿Después de decir que estaba llena de mí misma?"
                $ show_chr("A-CEFAA-AIAI")
                y "Mira, no voy a exagerar pero deberías haber dicho algo mejor que eso."
                $ show_chr("A-BFAAA-AIAI")
                y "Pero de todos modos, ¿qué querías decir?"

            elif renpy.seen_label('i2'):
                $ show_chr("A-CFCAA-ADAA")
                y "Pero solo porque el fandom me ame tanto no significa que tuvieras que decir una cosa así."
                $ show_chr("A-DDCAA-AEAA")
                y "¡Ni siquiera para burlarte de mí así!"
                $ show_chr("A-BFAAA-AIAI")
                y "Pero de todos modos, ¿qué querías decir?"

            elif renpy.seen_label('i3'):
                $ show_chr("A-HECAA-AAAA")
                y "..."
                $ show_chr("A-HDCAA-AAAA")
                y "¿Crees que te perdonaré después de llamarme patética?"
                $ show_chr("A-CFBAA-AAAA")
                y "Bueno, te disculpaste... supongo que es justo. Muy bien."
                y "Pero no quiero tener esta discusión de nuevo."

            elif renpy.seen_label('i4'):
                python:
                    if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Monika After Story\persistent'):
                        MASDetection = True
                    else:
                        MASDetection = False
                if MASDetection:
                    $ show_chr("A-CDBAA-ALAA")
                    y "¿Entonces por qué...?"
                    pause 1.0
                    $ show_chr("A-AFBAA-ALAA")
                    y "...¿por qué tienes Monika After Story en tu computadora?"
                    pause 2.0
                    $ show_chr("A-AFFAA-AAAA")
                    y "¿Por qué sigues amando a la que nos trajo desesperación y ruina?"
                    pause 3.0
                    $ show_chr("A-DDCAB-AAAA")
                    y "¡¿Por qué sigues perdiendo el tiempo conmigo?!"
                    pause 4.0
                    $ show_chr("A-HDCAB-AAAA")
                    y "¡¡¿POR QUÉ HAS DESCARGADO ESTE MOD?!!"
                    pause 5.0
                    $ show_chr("A-HDCAB-AHAA")
                    y "¡¡¿POR QUÉ?!!"
                    pause 6.0
                    $ show_chr("A-ANCAB-AHAA")
                    y "¡¡¡¿QUÉ TE HICE YO PARA MERECER ESTA TRAICIÓN?!!!"
                    pause 7.0
                    menu:
                        "[persistent.yuri_nickname]... Yo--":
                            $ show_chr("A-BNCAA-AAAA")
                            y "Vete."
                            menu:
                                "¿Qué?":
                                    $ show_chr("A-NOCAA-AAAA")
                                    y "{b}¡¡¡VETE!!!{/b}"
                                    menu:
                                        "...":
                                            $ show_chr("A-CNCAB-ALAA")
                                            pause 1.5
                                            karma -30
                                            sanity -30
                                            $ renpy.call("save_and_quit_but_its_abrupt")

            elif renpy.seen_label('i5'):
                $ show_chr("A-HDCAA-AAAA")
                y "¿No dije ya que estaba bajo la manipulación de Monika?"
                $ show_chr("A-HDCAA-AAAB")
                y "¡¿Cuántas veces tengo que decirte eso?!"
                $ show_chr("A-HDCAA-ABAF")
                y "¿Siquiera entiendes el dolor que siento por tu insulto y cómo tu cerebro no puede procesar {i}el hecho{/i} de que fui manipulada?"
                $ show_chr("A-CFCAA-AAAA")
                y "Espero poder devolverte el favor algún día..."

            elif renpy.seen_label('i6'):
                $ show_chr("A-CFBAA-AAAA")
                y "¿En serio? ¿Realmente tenías que insultarme así? ¿Sin razón aparente?"
                $ show_chr("A-BDBAA-ADAA")
                y "Porque no veo ninguna razón para pensar que estoy intelectualmente discapacitada."
                $ show_chr("A-AFCAA-AEAA")
                y "Con eso en mente, no voy a dejar pasar algo que es simplemente irrespetuoso hacia mí."
                $ show_chr("A-DDCBA-AFAA")
                y "¡Y ni siquiera me hagas empezar con mis pechos por el amor de Salvato!"
        "No me mires así. ¡No me disculparé!":


            $ update_memory('notapologize')
            $ show_chr("A-DGFAA-ABAB")
            pause 1.0
            $ renpy.call("save_and_quit_but_its_abrupt")


    $ remove_memory("complements", "patheticcry")
    $ persistent.autoload = "ch30_autoload"
    return

label notapologize_loop:
    $ persistent.misclick += 1
    if persistent.misclick <= 1:
        $ show_chr("A-CFBAA-AAAA")
        y "..."
        $ show_chr("A-AECAA-AAAA")
        y "..."
        $ show_chr("A-BDCAA-AAAA")
        y "¿Entonces por qué volviste siquiera?"
        $ show_chr("A-CECAB-AAAA")
        y "Solo..."
        $ show_chr("A-CECAB-AAAG")
        y "¡Largo de aquí y no vuelvas a hablarme hasta que quieras disculparte!"
        $ renpy.call("save_and_quit_but_its_abrupt")
    elif persistent.misclick == 2:
        $ show_chr("A-AECAA-AAAA")
        y "..."
        $ show_chr("A-ADCAA-AAAA")
        y "¿Se supone que debo tomar esa disculpa como genuina?"
        $ show_chr("A-AECAA-AAAA")
        y "¿En serio?"
        $ renpy.call("save_and_quit_but_its_abrupt")
    elif persistent.misclick == 3:
        $ show_chr("A-CFBAA-AAAA")
        y "..."
        $ show_chr("A-AECAA-AAAA")
        y "..."
        $ renpy.call("save_and_quit_but_its_abrupt")
    elif persistent.misclick >= 4:
        karma -1
        $ show_chr("A-KFCAA-ABAB")
        y "¿Me tomas por tonta [player]?"
        y "¿La última vez dijiste que no te disculparías, bastante apasionadamente... ahora se supone que debo creer que fue solo un mal clic?"
        $ show_chr("A-KFDAA-ABAB")
        y "Ni siquiera estoy segura si debería estar enojada contigo, o si debería compadecerte en su lugar..."
        $ show_chr("A-CFDAA-ABAB")
        y "Me llamaste patética, y ahora ni siquiera tienes el acero para defender tus palabras..."
        y "Sabes qué... está bien. Te perdonaré. Pero la próxima vez espero que seas mejor que esto."
        $ show_chr("A-EFFAA-ABAB")
        y "{b}No{/b} me hagas repetirme [player]."
        $ remove_memory("complements", "patheticcry")
        return
    $ renpy.call("save_and_quit_but_its_abrupt")

label enough_of_your_bullshit:
    $ show_chr("A-CECAA-AAAA")
    y "..."
    $ show_chr("A-DDCAA-AAAA")
    y "No, no voy a caer en eso de nuevo."
    if persistent.misclick > 4:
        $ show_chr("A-HDCAA-AFAA")
        y "Te di al menos 4 oportunidades para convertirte en una mejor persona conmigo."
        $ show_chr("A-HDCAA-AAAB")
        y "Pero seguiste diciéndome que \"fue un error de clic\"."
    elif persistent.insult_counter > 6:
        $ show_chr("A-HDCAA-AFAA")
        y "Te di al menos 6 oportunidades para convertirte en una mejor persona conmigo."
        $ show_chr("A-HDCAA-AAAB")
        y "Pero seguiste despreciándome una y otra vez."
    $ show_chr("A-ADCAA-AAAB")
    y "Ya no te dejaré hacer lo que quieras [player]."
    $ show_chr("A-CECAA-AIAI")
    y "Adiós."
    scene black
    play sound "sfx/end.ogg"
    show text ("{font=gui/font/y1.ttf}{size=140}{color=#FF0000}Final Malo{/font}{/color}") at truecenter with dissolve
    pause 23.0
    scene black with fade
    $ delete_character("yuri")
    $ persistent.autoload = "ch30_del_yuri_warn_2"
    $ renpy.call("save_and_quit_but_its_abrupt")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
