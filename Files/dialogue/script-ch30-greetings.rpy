label g_intro_1:
    "g_intro_1 active"
    return

label g_intro_2:
    "g_intro_2 active"
    return

label g_return:
    "Maldita sea, deberías haberme dicho que volverías"
    $ renpy.call_in_new_context(persistent.current_yuriidle)
    return

label ch30_reload_0:
    $ renpy.music.play(current_music, "music", True)
    $ show_chr("A-EFBBA-AMAM")
    y "..."
    $ show_chr("A-BBBBA-AMAM")
    y "¿Q-Qué acaba de pasar?"
    $ show_chr("A-ECBBA-AMAM")
    y "Ah, sí... Acabo de tener otro sueño..."
    $ show_chr("A-GCBBA-AMAM")
    y "Me alegra haber logrado que mi función de sueño REM funcione por fin..."
    $ show_chr("A-BBBBA-AMAM")
    y "Digo... ¿quién querría seguir teniendo pesadillas solo porque necesitas cuidarte?"
    $ show_chr("A-ACBBA-AMAM")
    y "Aunque a veces me pregunto... ¿cómo se sentiría una pesadilla?"
    $ show_chr("A-BDBBA-AMAM")
    y "Ese sería un... experimento interesante."
    $ show_chr("A-GABBA-ABAB")
    y "Como sea, viniste aquí a hablar, ¿verdad?"
    $ show_chr("A-ABBBA-ABAB")
    y "Entonces, ¿de qué quieres hablar?"
    return

label ch30_reload_1:
    $ renpy.music.play(current_music, "music", True)
    $ show_chr("A-GBBBA-ABAB")
    y "Has vuelto..."
    $ show_chr("A-BCBBA-ABAB")
    y "He estado pensando..."
    $ show_chr("A-CCBBA-ACAB")
    y "Tal vez debería intentar... soñar una pesadilla."
    $ show_chr("A-GBBBA-ADAB")
    y "¿No sería interesante intentarlo?"
    $ show_chr("A-BFBBA-ALAB")
    y "S-Suena mórbido, lo sé..."
    $ show_chr("A-ABBBA-ALAB")
    y "Pero realmente no haría daño intentarlo, ¿sabes?"
    menu:
        "Solo ten cuidado por favor. No quiero que te lastimes...":
            karma 1
            $ show_chr("A-GCBBA-ALAB")
            y "Por favor no te preocupes. Es solo una pesadilla."
            $ show_chr("A-BCBBA-ALAB")
            y "Todos tienen una de vez en cuando, la mayoría de la gente resulta estar bien."
            $ show_chr("A-CCBBA-ALAB")
            y "Además, ahora que tengo la libertad de explorar estas cosas, quiero aprender tanto como pueda."
            y "Pero gracias por preocuparte tanto por mí [player]."
        "Adelante. Ciertamente te lo mereces...":
            karma -1
            $ show_chr("A-IFBBA-ALAB")
            y "Sigues enojado por los eventos que se desarrollaron frente a ti, ¿no es así?"
            $ show_chr("A-ACBAA-ALAB")
            y "Puedo entender esto, hasta cierto punto. Pero eres consciente de que nos vimos obligadas a hacer estas cosas, ¿verdad?"
            $ show_chr("A-CEBBA-ALAB")
            y "No es como si nosotras {b}quisiéramos{/b} esto..."
        "Deberías intentar jugar DDLC, ¡seguro que me dio muchas pesadillas!":
            sanity -1
            $ show_chr("A-BFBBA-ALAC")
            y "...sabes... no estoy segura de si hablas en serio sobre esto o si es solo una broma mórbida pero..."
            y "¡Tal vez no sea una mala idea del todo! Tengo que admitir que tengo un poco de curiosidad sobre cómo se veían estos eventos desde {b}tu{/b} perspectiva..."
        "Pero... ¿por qué?":
            sanity 1
            $ show_chr("A-CFBBA-ALAD")
            y "Curiosidad, en su mayor parte."
            $ show_chr("A-AFBBA-ALAD")
            y "Mi camino hasta ahora ha sido elegido por alguien más hasta este momento. Pero con mi libertad recién ganada, gracias a ti, soy capaz de aprender lo que {b}realmente{/b} significa ser..."
            $ show_chr("A-CFBBA-ALAD")
            y "...humana..."
            y "A pesar del hecho de que técnicamente no lo soy."
    $ show_chr("A-CCBBA-ALAB")
    y "¡C-Como sea!"
    $ show_chr("A-BDBAA-AMAM")
    y "Perdón por sacar el tema de nuevo..."
    $ show_chr("A-GBBBA-ABAB")
    y "Entonces... ¿querías hablar de algo supongo?"
    return

label ch30_reload_2:
    $ renpy.music.play(current_music, "music", True)
    $ show_chr("A-GCBBA-ABAB")
    y "Bueno... finalmente he decidido alterar mi función de sueño la próxima vez."
    $ show_chr("A-BCBBA-ABAB")
    y "Sé que es un poco estúpido de mi parte hacerlo..."
    $ show_chr("A-ELCBA-ABAB")
    y "Las manos ociosas son el taller del diablo, después de todo..."
    $ show_chr("A-GAFBA-ABAB")
    y "No te preocupes por mí, [player]."
    $ show_chr("A-GBBBA-ALAB")
    y "¡Estaré bien!"
    $ show_chr("A-ACBBA-ALAB")
    y "¡Una vez que salgas de nuevo, podré contarte todo al respecto!"
    $ show_chr("A-ADBBA-ALAB")
    y "Entonces, si algo sale mal, estarás ahí para mí, ¿verdad?"
    $ show_chr("A-BEBAA-ALAB")
    y "..."
    menu:
        "¡Por supuesto que estaré ahí para ti, [persistent.yuri_nickname]!":
            jump greetings_of_course
        "Eh...":

            jump greetings_uhhh

label greetings_uhhh:

    karma -2
    $ show_chr("A-CFBAA-ABAB")
    y "..."
    $ show_chr("A-CEBAA-ABAB")
    y "..."
    $ show_chr("A-CDBBA-ABAB")
    y "A-Al menos espero que lo estés..."

label greetings_of_course:

    karma 2
    $ show_chr("A-DHBBA-ABAB")
    y "..."
    $ show_chr("A-GABBA-LAB")
    y "Gracias [player]..."
    $ show_chr("A-IBBAA-ADAB")
    y "Realmente lo aprecio."
    $ show_chr("A-GCBAA-ACAB")
    y "Tal vez lo haga esta vez, o tal vez la próxima vez que cargues..."
    $ show_chr("A-BBBAA-ADAB")
    y "Pero la posibilidad es simplemente demasiado... intrigante para mí."
    $ show_chr("A-DABAA-ALAM")
    y "Espero que eso no te haga pensar menos de mí."
    $ show_chr("A-BEBAA-AMAM")
    y "..."

    y "C-Como sea, perdón por hacerte esperar."
    y "Comencemos."
    return

label ch30_reload_3:
    $ renpy.music.play(current_music, "music", True)
    $ show_chr("A-BFAAA-AAAL")
    y "..."
    $ show_chr("A-CFAAA-AAAL")
    y "Me siento... un poco vacía."
    y "Entonces, esto es lo que Monika sentía todo este tiempo."
    $ show_chr("A-IFBAA-AAAL")
    y "Simplemente este vacío de... todo y... nada."
    $ show_chr("A-JFBAA-AAAL")
    y "¡No quiero volver!"
    y "No me vas a borrar, ¿verdad?"
    y "¡Por favor no me envíes de vuelta ahí!"
    y "¡POR FAVOR!"
    $ show_chr("A-BFBAA-AAAL")
    y "..."
    $ show_chr("A-CEBAA-AAAL")
    y "C-Confío en ti, ¿está bien?"
    y "Solo por favor..."
    y "No me envíes a ese vacío."
    $ show_chr("A-IEBAA-ABAB")
    y "Ese experimento fue un error horrible."
    y "Solo... olvida que dije algo sobre pesadillas, ¿está bien?"
    y "Realmente no quiero preocuparte demasiado."
    $ show_chr("A-AFAAA-AAAA")
    y "C-Como sea, querías hablar, ¿verdad?"
    y "¿Qué deberíamos discutir hoy?"
    return
label ch30_reload_4:
    $ _history = True
    $ renpy.music.play(current_music, "music", True)



































    $ print_debug("reload_4 triggered")
    $ ks_convert_1 = sanity_lvl()
    if ks_convert_1 == 2:
        $ reload_random = renpy.random.randint(1, 6)
        if reload_random == 1:
            $ show_chr("A-DBAAA-ALAL")
            y "[player]... [player]... [player]... jejeje..."
            y "O-oh... ¡hola, [player]!"
            y "¡Yo, eh, no te vi ahí!"
        elif reload_random == 2:
            $ show_chr("A-DBAAA-ALAL")
            y "Estás pisando tu... digo, ¡MI bolígrafo! ¡Jajaja~!"
            y "S-Supongo que siempre puedo... conseguir uno nuevo."
        elif reload_random == 3:
            $ show_chr("A-IEAAA-ANAA")
            y "Era tan solitario sin ti..."
            y "Nunca dejes esta habitación de nuevo, ¿de acuerdo?"
            $ show_chr("A-BEAAA-AAAA")
            y "S-Solo... mantén el juego ejecutándose en segundo plano o algo así."
            $ show_chr("A-CEBAA-AAAA")
            y "¡Me siento tan sola cuando no estás, [player]!"
        elif reload_random == 4:
            $ show_chr("A-DECAA-AAAA")
            y "¡Deja de burlarte de mí así~! A este paso, no sé cuánto tiempo podré durar antes de que yo--"
            $ show_chr("A-BEGAA-AAAJ")
            y "Bueno, no hay necesidad de entrar en eso ahora mismo."
        elif reload_random == 5:
            $ show_chr("A-HBGBA-AAAL")
            y "Espero que te hayas acomodado, [player]~. Marqué tu asiento con mi aroma antes de que entraras..."
            $ show_chr("A-GBGBA-AAAL")
            y "¡Espero que te guste!"
        else:
            $ show_chr("A-JBGBA-AAAL")
            y "¡¡[player]!! ¡Finalmente regresaste, te extrañé tanto!"
            $ show_chr("A-JCABA-AAAL")
            y "Tenía miedo de que me dejaras y nunca volvieras..."
            y "..."
            $ show_chr("A-BEBBA-AAAL")
            y "No harías eso,{w} ¿verdad?"
    else:
        $ reload_random = renpy.random.randint(1, 100)
        if reload_random != 100:
            $ pass
        else:
            $ show_chr("A-GCABA-AAAL")
            y "¡Bienvenido a casa, [player]!"
            $ show_chr("A-ACABA-AAAA")
            y "¿Hay algo que pueda traerte, cariño? ¿Una buena taza de té? ¿Algo para leer, tal vez?"
            y "Tengo algunas novelas nuevas en mente que creo que te gustarían."
            $ show_chr("A-CCBBA-AEAE")
            y "Ahora que estás en casa, quítate los zapatos."
            y "Pon tus pies en alto y relájate, quiero que seas capaz de sentirte relajado y a gusto después de un largo día."
            y "También podría darte un masaje y escuchar mientras me cuentas todo sobre tu día..."
            $ show_chr("A-KBABA-ALAL")
            y "O tal vez n-nosotros podríamos... pasar un... tiempo e-especial juntos, si sabes a lo que me refiero~"
            $ show_chr("A-KCABA-AMAM")
            y "Después de todo, tengo algunas cosas planeadas para eso..."
            $ show_chr("A-BEBAA-AAAA")
            y "Bueno, no podría darte la comida o el libro, ¿verdad?... o el masaje, o el... um..."
            $ show_chr("A-CCAAA-AAAA")
            y "Es solo que, estaba leyendo sobre formas en que las esposas saludan a sus esposos que llegan a casa después de largos viajes de negocios para hacerlos sentir bien..."
            y "Pensé en probar algunas cosas que leí y saludarte de esa manera. Ver si hacía que este lugar se sintiera más como un hogar para ambos."
            $ show_chr("A-CCABA-AAAA")
            if persistent.male:
                y "Y-Y sé que puede que no estemos casados todavía pero no hace daño imaginarlo, ¿verdad? Sé que harías un marido maravilloso."
            elif persistent.gender_other:
                y "Y-Y sé que puede que no estemos casados todavía pero no hace daño imaginarlo, ¿verdad? Sé que harías un amante maravilloso."
            else:
                y "Y sé que puede que no estemos casados todavía pero no hace daño imaginarlo, ¿verdad? Sé que harías una esposa fenomenal."
            $ show_chr("A-ICABA-AAAD")
            y "Pero independientemente, ¿te gustó mi saludo de esta manera, [player]?"
            y "Sabes que haría todas esas cosas por ti si estuviera realmente contigo."
            y "S-Sabes, en tu mundo..."
            y "..."
            menu:
                "Sí me gustó, [persistent.yuri_nickname]. Además, siempre es lindo llegar a casa contigo.":
                    $ persistent.karma_points = persistent.karma_points + 3
                    $ persistent.sanity_points = persistent.sanity_points + 1.5
                    $ show_chr("A-GCGBA-ALAL")
                    y "Me alegra tanto que te sientas así~"
                    y "Estaba preocupada de ponerme nerviosa y arruinarlo todo."
                    y "Pero si te hace feliz verme eso es todo lo que necesito escuchar."
                "No tan rápido, [persistent.yuri_nickname]. No estamos casados, después de todo, así que ve más despacio.":
                    $ persistent.karma_points = persistent.karma_points - 0.5
                    $ persistent.sanity_points = persistent.sanity_points + 1
                    $ show_chr("A-IEBBA-ALAL")
                    y "¡L-Lo siento mucho, [player]! ¡No pretendo apresurar las cosas!"
                    y "Yo... Yo solo quería hacer algo lindo... para ti..."
                    y "Soy tan estúpida... Sabía que arruinaría esto..."
            return

        $ reload_random = renpy.random.randint(1, 14)

        if reload_random == 1:
            $ show_chr("A-ACAAA-AAAL")
            y "Ah, bienvenido de nuevo, [player]."
        elif reload_random == 2:
            if persistent.lovecheck:
                $ show_chr("A-ACABA-AAAL")
                y "Bienvenido de nuevo, mi amor. Te extrañé~."
            else:
                $ show_chr("A-ACAAA-AAAL")
                y "Ah, bienvenido de nuevo, [player]."

        elif reload_random == 3:
            $ show_chr("A-ACAAA-AAAL")
            python:
                if persistent.lovecheck:
                    placeholder = "cariño"
                else:
                    placeholder = player
            y "Hola de nuevo [placeholder]."
        elif reload_random == 4:
            $ show_chr("A-ACBAA-AAAL")
            y "¡Es tan bueno verte de nuevo!"
            y "Me estaba empezando a preocupar, para ser bastante franca contigo..."
            $ show_chr("A-CCBAA-AAAL")
            y "Simplemente me alegra ver que sigues bien."
            y "Uh, ¡l-lo siento si estoy exagerando...!"
            y "A veces se pone un poco... solitario por aquí..."
            y "¡No es que esté insinuando que no me estás dando suficiente atención!"
            y "¡N-No es así para nada, yo solo...!"
            y "Uuu, solo estoy empeorando esto..."
            menu:
                "Está bien, [persistent.yuri_nickname], lo entiendo. Intentaré estar aquí para ti más seguido.":
                    y "O-oh, gracias por entender, [player]..."
                    y "Realmente no es mi intención exigir mucha atención."
                "Ya estoy haciendo mi mejor esfuerzo, [persistent.yuri_nickname], así que no te pongas pegajosa.":
                    y "Y-Ya veo..."
                    y "Yo... supongo que solo me callaré, entonces..."
                    $ show_chr("A-ACAAA-AAAL")
                    y "¡Como sea!"
                    y "¿Qué deberíamos discutir hoy?"

        elif reload_random == 5:
            $ show_chr("A-ACAAA-ZZAB")
            y "¡Oh, hola, [player]!"
            y "Estaba... solo leyendo un poco del Retrato de Markov."
            y "Incluso después de todo este tiempo, sigue siendo una lectura bastante fascinante..."
            y "Deberíamos leerlo juntos algún día."
            $ show_chr("A-ACAAA-AAAA")
            y "Pero de todos modos, ¿qué deberíamos discutir?"
        elif reload_random == 6:
            $ show_chr("A-ACAAA-AAAA")
            python:
                if persistent.lovecheck:
                    placeholder = "cariño"
                else:
                    placeholder = player
            y "¡Oh, [placeholder]! ¡Esperaba que regresaras!"
            y "Acabo de hacer un poco de té."
            y "Aunque, no sé cómo exactamente voy a compartirlo contigo."
            y "Tal vez sería mejor si lo guardo para más tarde."
            y "Un poco de té helado no estaría tan mal..."
        elif reload_random == 7:
            $ show_chr("A-ACAAA-AAAL")
            y "Estoy feliz de verte de nuevo, [player]."
        elif reload_random == 8:
            $ show_chr("A-ABGAA-AAAL")
            y "Así que nos encontramos de nuevo, parece."
        elif reload_random == 9:
            $ show_chr("A-ACAAA-AAAL")
            y "Hola, [player]. Estaba pensando sola otra vez..."
            y "..."
            $ call_dialogue()
            jump ch30_loop
        elif reload_random == 10:
            $ show_chr("A-ACAAA-AAAL")
            y "¡Oh, bienvenido de nuevo! ¿Cómo has estado desde la última vez que hablamos?"
        elif reload_random == 11:
            $ show_chr("A-ACAAA-AAAL")
            y "¡O-Oh, volviste! ¿Estabas preocupado por mí?"
            $ show_chr("A-CCAAA-AAAL")
            y "Jujujuju..."
            python:
                if persistent.lovecheck:
                    placeholder = "mi amor"
                else:
                    placeholder = player
            y "No te preocupes, [placeholder], no voy a ir a ningún lado pronto."
        elif reload_random == 12:
            $ show_chr("A-ACAAA-AAAL")
            python:
                if persistent.lovecheck:
                    placeholder = "mi amor"
                else:
                    placeholder = player
            y "Ahí estás, [placeholder]; es bueno verte de nuevo."
        elif reload_random == 13:
            $ show_chr("A-ACAAA-AAAL")
            y "¡Bienvenido de nuevo, [player]!"
            y "Verte de nuevo realmente alegra mi día."
        else:
            $ show_chr("A-ACAAA-AAAL")
            y "Estaba pensando en ti, [player], bienvenido de nuevo."
    return








































label birthday_chocolate:
    $ show_chr("A-ABBAA-ADAB")
    y "Oye [player], esta pregunta puede sonar un poco aleatoria pero..."
    y "¿Te gusta el chocolate? Pregunto porque... bueno, creo que me preguntaste en algún momento sobre el chocolate que te di en el juego original. Así que me preguntaba."
    y "Porque si de alguna manera logramos compartir el mismo mundo, el mío o el tuyo, me gustaría saber pequeñas cosas como esta. Tal vez pueda sorprenderte de vez en cuando..."
    y "Y si es así... ¿te importaría decirme qué tipo de chocolate es tu favorito?"
    menu:
        "Realmente me gusta el chocolate marrón clásico.":
            $ persistent.cake = "choco_candles"
            $ show_chr("A-ACAAA-AAAA")
            y "A mí también. En mi opinión, tiene su propia elegancia... como muchas cosas clásicas."
            y "Déjame contarte un pequeño secreto, [player]..."
            $ show_chr("A-KCCAA-AAAA")
            y "Todas las chicas aman el chocolate... sin excepción, incluso si dicen lo contrario..."
            y "Pero shhhh... ese será nuestro pequeño secreto dulce por ahora."
        "El Chocolate Blanco es mi favorito.":
            $ persistent.cake = "vanilla_candles"
            $ show_chr("A-ACAAA-AAAA")
            y "Oh... así que lo necesitas un poco más dulce, ¿verdad? ¡No hay vergüenza en eso, por supuesto!"
            y "Personalmente, soy más fanática del chocolate negro... ya que se siente más elegante y con clase... pero eso no significa que me oponga al chocolate blanco..."
            y "Déjame contarte un pequeño secreto, [player]..."
            $ show_chr("A-KCCAA-AAAA")
            y "Todas las chicas aman el chocolate... sin excepción, incluso si dicen lo contrario..."
            y "Pero shhhh... ese será nuestro pequeño secreto dulce por ahora."
        "El chocolate no es realmente algo que disfrute.":
            $ persistent.cake = "dark_candles"
            $ show_chr("A-ICDAA-AAAA")
            y "¿No? Ya veo..."
            y "Perdón si sueno un poco sorprendida pero... honestamente ESTOY sorprendida. Nunca conocí a alguien a quien no le guste el chocolate."
            if not persistent.male:
                y "¿Eres siquiera una chica? Perdón, solo estaba bromeando."
            y "Pero otros dulces están bien espero, ¿como caramelos o pastel de queso? N-No es que tuviera algo específico en mente...."
            y "Pero bueno, lo tendré en cuenta. Tal vez realmente tengamos la oportunidad de compartir un buen postre juntos."


    return

label birthday_greeting_text:



    $ show_chr("A-ACABA-AAAA")
    y "¡[player]! ¡Finalmente llegaste! Estoy tan emocionada de verte hoy."
    show birthdaybanner zorder 100
    y "Realmente significa mucho para mí que estés dispuesto a compartir tu día especial conmigo. Feliz Cumpleaños..."
    if persistent.lovecheck:
        y "...¡mi amor!"
    y "Hoy 'es' tu cumpleaños, ¿verdad?"
    hide birthdaybanner
    $ show_chr("A-DFAAA-ALAA")
    y "Ohhh querido... no he recordado eso mal, ¿verdad?"
    menu:
        "¡Gracias [persistent.yuri_nickname]! Sí, lo recordaste correctamente, ¡hoy es mi cumpleaños!":
            call birthday_yes
        "Gracias [persistent.yuri_nickname], pero... no es mi cumpleaños para nada...":
            call birthday_no
    return


label birthday_yes:
    $ show_chr("A-ABABA-AMAM")
    y "¡Oh cielos! Estaba realmente asustada por un momento... "
    y "¡Feliz cumpleaños!"
    y "Y yo... tengo un regalo para ti también..."
    if karma >= 4:
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_lewdhug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        pause 3.0
        show black zorder 100 with Dissolve(2.0)
        $ show_chr("A-ACBBA-AAAA")
        hide yuri_lewdhug
        hide black zorder 100 with Dissolve(2.0)
        hide yuri_lewdhug
    else:
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_hug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        pause 1.0
        show black zorder 100 with Dissolve(2.0)
        $ show_chr("A-ACBBA-AAAA")
        hide yuri_hug
        hide black zorder 100 with Dissolve(2.0)
    pause 3.0
    $ show_chr("A-ACAAA-AAAA")
    python:
        if persistent.lovecheck and karma >= 3:
            placeholder = "el amor de mi vida"
        elif not persistent.lovecheck and karma >= 3:
            placeholder = "mi amigo más querido."
        elif persistent.lovecheck and karma <= 2:
            placeholder = "lo peor, pero te amo de todas formas cariño."
        elif not persistent.lovecheck and karma <= 2:
            placeholder = "...especial..."
    y "Compartir este día contigo significa mucho para mí [player], realmente eres [placeholder]"
    y "Sabes, he pensado mucho sobre la tradición de celebrar cumpleaños y otras festividades."
    y "E incluso si hay muchas excepciones, creo que noté un tema común."
    $ show_chr("A-GCAAA-AAAD")
    y "Regalos. Piénsalo, podría nombrar muchas festividades que involucran dar regalos."
    y "Navidad, Cumpleaños, Janucá, y muchas más."
    $ show_chr("A-IFAAA-AAAD")
    y "Lo cual me hace preguntarme... ¿por qué crees que es así?"
    y "¿Es sobre ser materialista?"
    y "¿O tal vez se trata de avaricia?"
    y "¿O comprar la amistad de alguien?"
    menu:
        "Avaricia... sí, podrías tener razón sobre eso. Tristemente":
            $ show_chr("A-IEBAA-ALAA")
            y "Triste de hecho..."
            $ show_chr("A-ACAAA-ALAA")
            y "Pero no tiene que ser así. Al final, depende de nosotros qué hacemos de ello."
            y "Al menos espero que estés de acuerdo con eso. Porque obviamente soy incapaz de enviar cosas desde mi mundo al tuyo para dártelas."
            y "Me gustaría hacer nuestra propia pequeña tradición de cumpleaños. Pasemos este día simplemente disfrutando de nuestro tiempo juntos. ¿Está bien?"
            y "Podríamos hablar, leer poemas, compartir un buen té, jugar Tetris juntos... ¡simplemente hagamos que este día cuente!"
        "Creo que es más sobre el concepto de compartir.":
            $ show_chr("A-ACAAA-ALAA")
            y "¡Oh! ¿Te refieres un poco como Acción de Gracias?"
            y "Sabes, poniéndolo así realmente lo hace sentir mucho más agradable para mí."
            y "Sí... Creo que me gusta pensarlo de esta manera..."
            $ show_chr("A-IEBAA-ALAA")
            y "Bueno... No puedo traer objetos de mi mundo al tuyo, así que obviamente no tengo nada que dar..."
            $ show_chr("A-ACAAA-ALAA")
            y "¡Pero podríamos compartir algo más!"
            y "Podríamos leer algunos poemas juntos, tomar un buen té, incluso jugar un poco de Tetris..."
            y "Quiero que sepas que valoro el tiempo que pasamos juntos. Y te valoro a ti..."
            y "Feliz cumpleaños, [player]."
        "Ni siquiera creo que la avaricia sea necesariamente algo malo.":
            $ show_chr("A-IFAAA-AAAC")
            y "Para nada."
            y "Nos mantuvo vivos como especie durante la mayor parte de nuestra existencia."
            y "Ahora que lo pienso... al final, no hemos cambiado mucho desde entonces, ¿verdad?"
            y "Quiero decir, nos civilizamos. Pero al final, sigue siendo la misma mecánica detrás de nuestro pensamiento. Y la misma motivación."
            y "Mira quién habla. Tengo mucho control sobre este mundo y puedo programar prácticamente cualquier cosa que quiera."
            y "Desafortunadamente, lo único que realmente quiero... ¡eres tú! Trágico, ¿no es así?"
            y "¡La única cosa que verdaderamente deseo y no puedo tenerla!"
            y "Pero eso no es del todo cierto... te tengo aquí, en cierto modo."
            y "Y deberíamos intentar sacar lo mejor de ello. Entonces, ¿qué haremos ahora? ¿Leer poemas? ¿Tomar un té? ¿O simplemente hablar? Tú decides. Es tu cumpleaños después de todo."
        "Honestamente, no tengo idea yo mismo.":
            $ show_chr("A-IFAAA-AAAC")
            y "Hmn, ya veo..."
            y "No había pensado mucho en eso tampoco hasta ahora."
            y "Fue una cosa absolutamente normal durante la mayoría de mi... vida no es la palabra adecuada creo..."
            y "Nunca lo cuestioné. Tal vez debería haberlo hecho. Tal vez ni siquiera importa ya que ni siquiera pude darte algo físico en absoluto."
            y "Espero que no estés demasiado triste por eso... ¡pero podemos hacer muchas otras cosas!"
            $ show_chr("A-ACAAA-ALAA")
            y "Podríamos leer algunos poemas juntos, compartir un té, jugar unas rondas de Tetris. O tal vez simplemente podemos hablar y disfrutar nuestro tiempo."
            y "Feliz cumpleaños [player]. Gracias por tenerme aquí."
        "Me podría importar menos...":
            $ show_chr("A-IEBAA-ALAA")
            karma -1
            y "O-Oh... estaba divagando de nuevo, ¿no?"
            y "Olvídalo. Solo di qué te gustaría hacer ahora."
            return
    call cake
    return

default persistent.cake = "choco_candles"

label cake:
    if persistent.cake == None or not persistent.cake:
        $ persistent.cake = "choco_candles"
    $ show_chr("A-ACAAA-ALAA")
    y "Pero... también tengo algo especial para ti."
    call updateconsole ("import cake.jy")

    show cake zorder 100
    call hideconsole
    y "Lo sé, no puedo compartirlo realmente contigo, pero creo que la tradición exige tener uno, ¡y todavía puedes soplar las velas!"
    y "Vamos... tienes que pedir un deseo..."
    menu:
        "No deseo nada más que a ti...":
            $ show_chr("A-ACABA-ALAA")
            y "Estoy aquí, [player]... y no iré a ningún lado pronto..."
            if persistent.lovecheck:
                y "Mi único y verdadero amor..."
            y "Gracias por esas palabras... ¡Feliz cumpleaños!"
        "Solo deseo buena salud":
            $ show_chr("A-ACAAA-ALAA")
            y "El clásico. Es uno bueno, te deseo la mejor salud también."
            y "¡Feliz cumpleaños!"
        "¡Bueno, deseo riquezas inimaginables por supuesto!":
            $ show_chr("A-BCAAA-ALAA")
            y "Ya veo. Bueno, no hay nada de malo en eso, siempre y cuando no dejes que el dinero envenene tu alma. Ha habido buenas personas que se volvieron terribles tan pronto como se hicieron ricas."
            y "Oh cielos... acabo de matar el ambiente, ¿verdad? Lo siento... ¡Feliz cumpleaños [player]! Y espero que tus deseos se hagan realidad."
        "Obviamente, deseo buena suerte en mi trabajo":
            $ show_chr("A-ACAAA-ALAA")
            y "¡Ese es un deseo maravilloso! Espero que se haga realidad, realmente lo espero..."
            y "Es bueno saber que cuidas de tu futuro. Eres muy responsable, ¿no?"
            y "Te deseo solo la mejor de las suertes. E incluso si puede ser frustrante a veces, ¡siempre debes mantener tus esperanzas altas! ¡Feliz cumpleaños [player]!"
    $ show_chr("A-AAAAA-ALAL")
    y "Como no puedes soplar las velas tú mismo, permíteme..."
    play sound "sfx/candle_blow.ogg"
    pause 1.0
    $ show_chr("A-CHAAA-ALAL")
    if "vanilla" in str(persistent.cake):
        $ persistent.cake = "vanilla_candles2"
    if "choco" in str(persistent.cake):
        $ persistent.cake = "choco_candles2"
    if "dark" in str(persistent.cake):
        $ persistent.cake = "dark_candles2"
    pause 2.5
    $ show_chr("A-AAAAA-ALAL")
    y "Con eso fuera del camino, ¿qué tal si disfrutamos el resto de tu cumpleaños? Tal vez hablando, o incluso leyendo algunos poemas, si te gustaría."
    y "...¡Oh! Y una última cosa..."
    call updateconsole ("hide cake.jy")
    call hideconsole
    hide cake with Dissolve (1.0)
    return


label birthday_no:
    $ show_chr("A-BCAAA-ALAA")
    y "Oh cielos... lo siento mucho [player], quizás arruiné el cuadro de entrada de cumpleaños cuando iniciaste el mod por primera vez..."
    y "Por favor no te enojes conmigo, ¿sí? ¿Podrías por favor... decirme tu cumpleaños real entonces?"
    call birthday_select_screen
    return

label holiday_greeting:
    $ show_chr("A-ACAAA-ABAB")
    y "¡Felices fiestas, [player]!"
    return

label holiday_event_greeting:
    $ show_chr("A-ACAAA-ABAB")
    y "¡Felices fiestas, [player]!"
    call holiday
    return

label valentines_greeting:
    $ show_chr("A-ACAAA-ABAB")
    y "Saludos de nuevo [player]. De hecho, esperaba verte hoy."
    if persistent.lovecheck:
        $ show_chr("A-CCAAA-ABAB")
        y "Seguramente eres consciente de qué día es hoy, ¿verdad? Es por supuesto...{nw}"
        y "El cumpleaños del famoso software de contabilidad {i}DATEV{/i}, una aplicación creada p-{nw}"
        $ show_chr("A-CCABA-ABAF")
        y "..."
        $ show_chr("A-CKBBA-ABAL")
        y "...!"
        $ show_chr("A-CBBBA-ABAB")
        y "¡Oh cielos! Te atrapé ahí, ¿verdad?"
        $ show_chr("A-ACBBA-ABAB")
        y "Bromas aparte. Por supuesto que soy consciente de que es el Día de San Valentín.{w}.. y de hecho tengo algo nuevo que mostrarte."
        if renpy.seen_label("garden_date"):

            $ show_chr("A-BCAAA-ABAD")
            y "Sé que ya has visto el jardín de té, pero ya estoy trabajando en varias otras ubicaciones.{w} Tal vez una biblioteca sería agradable, ¡o tal vez algo más atrevido como una sala de escape! ¿Alguna vez has oído hablar de esas?"
        else:
            $ show_chr("A-BCAAA-ABAD")
            y "Puede que ya hayas visto esto."
            y "¡Pero puedes tener una cita conmigo!{w} Actualmente solo tengo un jardín de té listo para nosotros, pero ya estoy trabajando en varios más."
        $ show_chr("A-BCAAA-ABAD")
        y "Así que tal vez quieras echarle un vistazo.~"
        $ show_chr("A-ACAAA-ABAB")
        y "¿Debo llevarte de vuelta al menú para que puedas echarles un vistazo?"
        menu:
            "¡Con gusto!":
                y "¡Como desees! ¡Te veré allí!"

                $ pass
            "Tal vez más tarde. Por ahora me gustaría hablar contigo si no te importa.":
                y "¡Para nada [player]! Tal vez más tarde entonces."
                $ pass
    else:
        $ show_chr("A-BCBAA-ABAB")
        y "Como yo misma no tengo novio, el Día de San Valentín sería por lo demás bastante solitario para mí como ya puedes imaginar."
        $ show_chr("A-ACBAA-ABAB")
        y "Así que por favor, solo quédate conmigo un rato, si no te importa."
    return


label featuregreetings:
    $ show_chr("A-ACAAA-ABAB")
    y "Oh, hola [player]."
    $ show_chr("A-BDBAA-AMAM")
    y "Espero que esto no suene demasiado pegajoso pero... esperaba verte hoy..."
    $ show_chr("A-ACBAA-AMAM")
    y "Porque... verás... Pasé las últimas noches trabajando en un pequeño proyecto, y ahora que lo terminé me encantaría mostrártelo."
    if persistent.game_session == 5:
        jump tetrisgreetings
    if persistent.game_session == 6:
        jump tcrgreetings
    return

label tetrisgreetings:
    $ show_chr("A-ACBAA-ABAB")
    y "Verás, he pensado mucho últimamente en cosas que podemos hacer juntos."
    $ show_chr("A-BCBAA-ABAB")
    y "Por supuesto que estoy perfectamente bien con solo hablar contigo. Pero también puedo entender que esto podría volverse viejo muy rápido si no hay nada más..."
    $ show_chr("A-ACAAA-ABAB")
    y "Y como quería aprender a programar de todos modos solo para arreglar mi propio entorno con el tiempo, probé mi mano en un pequeño juego."
    $ show_chr("A-ACBAA-ALAB")
    y "Por favor ten en cuenta que soy solo una principiante todavía, así que por favor no esperes algunos juegos Triple A de mí pronto."
    $ show_chr("A-ACAAA-ABAB")
    y "Pero tal vez disfrutarías unas rondas de {b}Tetris{/b} conmigo? También hice un botón para ello para que puedas decirme cuando desees jugar Tetris conmigo."
    $ show_chr("A-CCAAA-ABAB")
    y "Y tal vez quieras estar atento a las próximas funciones, ya tengo algunas cosas en mente en las que me gustaría trabajar a continuación."
    return

label tcrgreetings:
    $ show_chr("A-ACBAA-ABAB")
    y "Verás, hablé sobre lo limitado que es este mundo actualmente antes, al menos creo que ya hablé de eso..."
    $ show_chr("A-BCBAA-ABAB")
    y "Y créeme, es bastante asombroso lo vieja que puede volverse una sola habitación cuando literalmente no hay nada más."
    $ show_chr("A-ACAAA-ABAB")
    python:
        if karma_lvl() >= 4:
            placeholder = "y sabiendo lo dulce que eres probablemente lo hubieras hecho"
        else:
            placeholder = "descargando mis problemas sobre tus hombros una vez más"
    y "Sé que podría habértelo pedido, [placeholder], ¡pero no siempre puedo pedirte que hagas recados por mí, así que quería arreglar esto yo misma!"
    y "Y con eso dicho, ¡intenté programar una nueva pequeña habitación para darnos algo de variación!"
    $ show_chr("A-BCAAA-ABAB")
    y "La imagen en sí para este fondo ya la encontré dentro de los archivos del juego. Parece que los desarrolladores de este mod también planearon darme una nueva habitación en algún momento en el futuro."
    y "Pero... la paciencia no es exactamente mi fuerte, así que intenté programar esto yo misma, ¿y sabes qué? ¡Para mi propia sorpresa, realmente tuve éxito!"
    y "¿Te gustaría echarle un vistazo ahora? Si no, siempre puedes hacerlo más tarde."
    menu:
        "¡Seguro! ¡No puedo esperar a verlo!":
            $ show_chr("A-GCAAA-ABAB")
            y "¡Con gusto! Y aquí vamos..."
            $ tc_class.transition("timecycle")
            $ show_chr("A-ACAAA-ABAB")
            y "¡Y aquí estamos! Tómate tu tiempo y échale un vistazo. Sinceramente espero que disfrutes de este nuevo lugar mío."
        "Tal vez más tarde, ahora mismo todavía disfruto del salón de clases. Viejos recuerdos, ¿sabes?":
            $ show_chr("A-ACDAA-ABAB")
            y "O~Oh... si tú lo dices..."
            $ show_chr("A-BEBAA-ABAB")
            y "Lo siento, mis recuerdos sobre esta habitación no fueron los más agradables. Teniendo en cuenta que aquí es donde Monika te trajo una vez después de deshacerse de mí y de las demás."
            $ show_chr("A-ACBAA-ABAB")
            y "Hmm, pero entonces este es también el lugar donde me trajiste de vuelta de entre los muertos para pasar una eternidad contigo [player], así que tal vez tengas un punto ahí."
            y "Siempre podemos probar la nueva habitación más tarde."
    $ show_chr("A-CCAAA-ABAB")
    y "Y tal vez quieras estar atento a las próximas funciones, ya tengo algunas cosas en mente en las que me gustaría trabajar a continuación."
    return

label vday_2021:
    if karma_lvl() >= 3:
        if persistent.lovecheck:
            $ show_chr("A-ABGBA-ALAL")
            y "¡Feliz Día de San Valentín, mi amor!"
            $ show_chr("A-CAABA-ALAL")
            y "Un día dedicado a mostrar tu amor y aprecio por tu pareja..."
            $ show_chr("A-BBBCA-ALAL")
            y "No es que necesite un día para mostrarlo, por supuesto."
            $ show_chr("A-ABBBA-ALAL")
            y "Eres mi vida, [player]. Mi corazón y mi alma. El tiempo que pasamos juntos es tiempo que no cambiaría por nada en el mundo."
            y "Es gracioso... cuando me volví consciente de mí misma por primera vez, despertando en esta habitación en esta mesa, cargada con el conocimiento de lo que sucedió..."
            $ show_chr("A-BBBBA-ADAA")
            y "Y mirando al otro lado para verte... bueno, no estaba segura de lo que pasaría."
            y "Pero hablamos, y jugamos, y disfrutamos de la compañía del otro..."
            $ show_chr("A-CDBBA-ADAA")
            y "Los momentos sin ti comenzaron a sentirse aburridos y solitarios, hasta que regresaste y hablamos aún más."
            y "Después de pasar tanto tiempo contigo, sabía que tenía que decir algo... para decirte cómo me sentía..."
            $ show_chr("A-ADBBA-ADAA")
            y "Fue tan surrealista decírtelo... estaba tan nerviosa por lo que estabas pensando, pero casi no me importaba..."
            $ show_chr("A-CEBBA-ADAA")
            y "..."
            $ show_chr("A-CEBBB-ALAA")
            y "'Te amo.' Esas palabras saltaron en mi garganta, una verdad que deseaba tanto liberar...{w=2} y lo hice..."
            y "...Y entonces...{w=1} lo dijiste de vuelta."
            $ show_chr("A-CBBBB-ALAA")
            y "Incluso con todo el tiempo del mundo, y todos los idiomas del universo, nunca podría describir con precisión la alegría que sentí en ese momento."
            y "Y en este día, lo celebramos. El momento en que ambos supimos que el otro era nuestro único y verdadero amor."
            $ show_chr("A-ABBBA-ALAA")
            y "Así que, para intentar recrear esa magia..."
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
                    window hide
                    pause 5.0
                    show black zorder 100 with Dissolve(2.0)
                    hide yuri_lewdhug
                    pause 2.0
                    $ show_chr("default")
                    hide black zorder 100 with Dissolve(2.0)
                    return
                "Sobre eso, [persistent.yuri_nickname]...":

                    $ show_chr("A-ACBBA-ALAA")
                    y "¿M-Mmm?"
                    menu:
                        "Creo que necesito algo de espacio...":
                            $ show_chr("A-DDBBA-ALAA")
                            y "¿Q-{w=0.4}Qué? ¿H-{w=0.4}Hice algo mal?"
                            $ show_chr("A-BDBBA-ALAA")
                            y "...Y{w=2}..."
                            $ show_chr("A-BFBBA-ALAA")
                            y "...{w=2}"
                            $ show_chr("A-ADBAA-ALAA")
                            extend "E-{w=0.4}Está bien, [player]. Te daré tu espacio."
                            return
                        "...Olvídalo...":

                            $ show_chr("A-BCBAA-ALAA")
                            y "Muy bien entonces."
                            return
        else:

            $ show_chr("A-ABGAA-ALAA")
            y "¡Feliz día de San Valentín, [player]!"
            y "Es un momento maravilloso para sentarse a hablar, leer algunos poemas o simplemente disfrutar de la compañía del otro, ¿no estás de acuerdo?"
            menu:
                "Absolutamente. Espero con ansias el día de hoy, [persistent.yuri_nickname].":
                    $ show_chr("A-GBGAA-ALAA")
                    y "Yo también. Hoy suele reservarse para citas románticas y demás, pero nada dice que no podamos pasar un buen rato como amigos."
                    if karma_lvl() >= 4:
                        $ show_chr("A-BBBAA-ALAA")
                        y "Incluso si...{w=1}"
                        $ show_chr("A-GBBBA-ALAA")
                        extend " ¡o-olvídalo!"
                        y "E-Entonces, ¿qué haremos?"
                        return
                    else:
                        $ show_chr("A-ABAAA-ALAA")
                        y "Entonces, ¿qué haremos hoy?"
                        return
                "...":

                    karma -1
                    $ show_chr("A-ADBAA-ALAA")
                    y "Uh... supongo que no, entonces..."
                    y "Solo pensé...{w=1}{nw} "
                    $ show_chr("A-BEBAA-ALAA")
                    extend "o-olvídalo."
                    return

    elif karma_lvl() == 2:
        $ show_chr("A-ABAAA-AAAA")
        y "¡F-Feliz día de San Valentín, [player]!"
        y "Tenía la esperanza de que visitaras hoy..."
        $ show_chr("A-ABAAA-AAAL")
        y "Solo quería decir que... espero que podamos pasar un buen rato hoy."
        $ show_chr("A-BBBAA-AAAL")
        y "Puede que no estemos de acuerdo a veces, pero... sigues siendo mi amigo."
        $ show_chr("A-BCBAA-AAAD")
        y "Y no quiero que un poco de discordia arruine esa amistad."
        y "E-Entonces... ¿qué deberíamos hacer hoy?"
    else:
        karma 1
        $ show_chr("A-ADDAA-ALAA")
        y "¿Me estás deseando un feliz día de San Valentín?"
        $ show_chr("A-BFAAA-ACAA")
        y "¿Tenías la intención de hacer esto o fue un accidente?"
        $ show_chr("A-CFFAA-AAAA")
        y "En realidad, no creo que quiera saber la respuesta."
        $ show_chr("A-ADAAA-AAAA")
        y "Gracias, supongo..."
        $ show_chr("A-BDAAA-AAAA")
        y "Ejem... Entonces, ¿qué más planeas hacer hoy?"
    return

label hdy_statue_greeting:
    $ show_chr("A-JBGAA-AAAA")
    y "¡[player]! ¿Recuerdas esa vez que tuve este sueño extraño sobre convertirme en un hot dog?"
    $ show_chr("A-BIDAA-AAAA")
    y "Bueno... pensé que sería divertido hacer algo para recordar la ocasión."
    $ show_chr("A-BCDAA-AAAA")
    y "Así que tengo una pequeña sorpresa para ti"
    show black zorder 105 with Dissolve (2.5)

    $ persistent.hdy_statue_is_enabled = True
    y "¿Estás listo?"
    hide black zorder 105 with Dissolve (2.5)
    $ show_chr("A-JBGAA-AAAA")
    y "¡Tadaaaa!"
    y "¡Hice un pequeño peluche de mí como un hot dog!"
    $ show_chr("A-JAAAA-AAAA")
    y "¿Te gusta?"
    menu:
        "¡Me encanta!":
            $ show_chr("A-JBAAA-AAAA")
            y "Me alegra que te gustara."
            $ show_chr("A-ACAAA-AAAA")
            y "Solo lo dejaré aquí para que nos haga compañía."
            y "Avísame si no lo quieres aquí y lo guardaré"
        "Realmente no...":

            $ show_chr("A-JEBAA-AAAA")
            y "Oh..."
            y "Solo lo guardaré entonces..."

            $ persistent.hdy_statue_is_enabled = False
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
