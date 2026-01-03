default persistent.skin = 0
define TetrisWinner = 0
define LineLimit = 0
define TetrisScore = 0
define PlayerForYuri = 0

label tetris:
    python:
        DisableTalk()
        boopable = False
        show_chr("A-BFBAA-AAAC")
        LineLimit = 0
        TetrisScore = 0
    if sanity_lvl() > 2 and karma_lvl() > 2:

        menu:
            y "Oh, así que te gustaría jugar un poco de Tetris, ¿hmm?"
            "Sí.":
                y "Oh, bien."
                y "¿Qué tema te gustaría esta vez?"
                $ pass
            "No.":
                y "Ya veo..."
                y "Tal vez en otro momento, entonces."
                jump ch30_loop
    elif sanity_lvl() > 2 and karma_lvl() < 3:
        menu:
            y "Tú... ¿quieres jugar Tetris...?"
            "Sí.":
                y "Oh..."
                y "Bueno, seguro, supongo que no me importaría realmente."
                y "Me pregunto si te burlarás de mí por perder."
                y "A juzgar por cuánto placer obtienes de mi miseria, asumo que lo harás."
                y "Como sea, solo elige un tema y sigamos con ello."
                $ pass
            "No.":
                y "Oh..."
                y "Tal vez... en otro momento, entonces."
                jump ch30_loop
    elif sanity_lvl() < 3 and karma_lvl() > 2:
        menu:
            y "Q-quieres jugar Tetris, ¿sí?"
            "Sí.":
                y "¡Uhuhuhu~!"
                y "¿Qué tema te gustaría esta vez?"
                y "¡No importa cuál elijas, estoy segura de que te dominaré sin importar lo que elijas!~"
                $ pass
            "No.":
                y "O-oh..."
                y "Bueno..."
                y "Está bien..."
                y "Tal vez en otro momento, entonces..."
                jump ch30_loop
    elif sanity_lvl() < 3 and karma_lvl() < 3:
        menu:
            y "¿Quieres jugar Tetris, hmm?"
            "Sí.":
                y "Estoy segura de que de alguna manera encontrarás una forma de convertir incluso un asunto tan trivial en una pesadilla para mí..."
                y "De alguna manera todavía encontrarás una forma de humillarme..."
                y "Cierto..."
                y "Como sea, ¿qué tema quieres?"
                $ pass
            "No.":
                y "Oh..."
                y "Bueno... ya veo..."
                y "Tal vez en otro momento cuando aprendas a decidirte."
                jump ch30_loop
    if current_timecycle_marker == "_night":
        menu:
            "Tema por Defecto.":

                y "¿No quieres darle a Tetris ningún tipo de piel? Está bien."
                $ persistent.skin = 1
            "Tema Tetris 99.":

                y "¿Oh? ¿Vas a experimentar uno de los últimos temas de Tetris?"
                y "Pero por favor no esperes demasiado de él."
                $ persistent.skin = 2
            "Tema GameBoy Tetris.":

                y "¡Oh! ¿Es este el clásico Tetris para portátiles? Ten en cuenta que esta es la versión a color."
                $ persistent.skin = 3
            "Tema Mega Drive Tetris.":

                y "Bien. Es desafortunado que no puedas experimentar el Procesamiento de Ráfaga en Ren'Py."
                $ persistent.skin = 4
            "Tema M1ND BEND3R.":

                $ persistent.skin = 5
            "Tema Personalizado.":

                call custom_tetris_checkpoint_start
    else:

        menu:
            "Tema por Defecto.":

                y "¿No quieres darle a Tetris ningún tipo de piel? Está bien."
                $ persistent.skin = 1
            "Tema Tetris 99.":

                y "¿Oh? ¿Vas a experimentar uno de los últimos temas de Tetris?"
                y "Pero por favor no esperes demasiado de él."
                $ persistent.skin = 2
            "Tema GameBoy Tetris.":

                y "¡Oh! ¿Es este el clásico Tetris para portátiles? Ten en cuenta que esta es la versión a color."
                $ persistent.skin = 3
            "Tema Mega Drive Tetris.":

                y "Bien. Es desafortunado que no puedas experimentar el Procesamiento de Ráfaga en Ren'Py."
                $ persistent.skin = 4
            "Tema Personalizado.":

                call custom_tetris_checkpoint_start

    y "Muy bien [player], ahora puedo dejarte seleccionar los modos que quieres jugar."
    menu:
        "Conteo de líneas":
            if persistent.lovecheck and karma_lvl() > 3:

                $ show_chr("A-BBBAA-ADAA")
                y "Es una buena forma de pasar el tiempo, de verdad."
                y "Solo una pareja haciendo cosas juntos..."
                y "Ejem... Como sea, empecemos."
                $ show_chr("A-FCAAA-ACAB")
                menu:
                    "30":
                        $ LineLimit = 30
                    "50":
                        $ LineLimit = 50
                    "100":
                        $ LineLimit = 100
                    "150":
                        $ LineLimit = 150
                    "300":
                        $ LineLimit = 300
                jump tetris_difficulty
            elif karma_lvl() >= 3:

                $ show_chr("A-ACEAA-AMAM")
                y "Oh, elección encantadora, [player]~"
                y "B-bueno, espero resultar un desafío digno..."
                y "Uhuhuhu..."
                y "Bueno, quien llegue a la cantidad específica de líneas gana..."
                menu:
                    "30":
                        $ LineLimit = 30
                    "50":
                        $ LineLimit = 50
                    "100":
                        $ LineLimit = 100
                    "150":
                        $ LineLimit = 150
                    "300":
                        $ LineLimit = 300
                jump tetris_difficulty
            elif karma_lvl() < 3:

                $ show_chr("A-BEBAA-AMAM")
                y "N-no estoy segura de si querrías perder tu tiempo conmigo..."
                y "Digo, este modo parece un poco demasiado simple y aburrido para ti."
                y "Especialmente con alguien como yo."
                $ show_chr("A-CEAAA-ALAL")
                y "¿Tal vez solo quieres un aumento de ego al verme perder?"

                menu:
                    "30":
                        $ LineLimit = 30
                    "50":
                        $ LineLimit = 50
                    "100":
                        $ LineLimit = 100
                    "150":
                        $ LineLimit = 150
                    "300":
                        $ LineLimit = 300
                jump tetris_difficulty
        "Puntuación":

            if persistent.lovecheck and karma_lvl() > 3 and sanity_lvl() < 2:

                $ show_chr("A-KLAAA-AKAK")
                y "Y tal vez me ganes como un premio para ser atesorado... Por siempre~"
                y "O tal vez yo te gane. Hehe. De cualquier manera, ¡todos ganan!"
                menu:
                    "20000":
                        $ TetrisScore = 20000
                    "50000":
                        $ TetrisScore = 50000
                    "100000":
                        $ TetrisScore = 100000
                    "200000":
                        $ TetrisScore = 200000
                    "300000":
                        $ TetrisScore = 300000
                    "500000":
                        $ TetrisScore = 500000
                jump tetris_difficulty
            elif karma_lvl() >= 3:

                $ show_chr("A-FCEAA-ABAB")
                y "Oh, algo de competencia, ¿hmm?"
                y "Bueno, supongo que ser un poco competitiva no sería tan malo, ¿o sí?"
                $ show_chr("A-ABAAA-AMAM")
                python:
                    if sanity_lvl() >= 3:
                        placeholder = "concurso"
                    elif sanity_lvl() <= 3:
                        placeholder = "emoción"
                y "No hay nada malo con un buen [placeholder] de vez en cuando..."


                $ show_chr("A-AAEAA-ALAL")
                y "¡Muy bien, veamos quién superará al otro!"
                menu:
                    "20000":
                        $ TetrisScore = 20000
                    "50000":
                        $ TetrisScore = 50000
                    "100000":
                        $ TetrisScore = 100000
                    "200000":
                        $ TetrisScore = 200000
                    "300000":
                        $ TetrisScore = 300000
                    "500000":
                        $ TetrisScore = 500000
                jump tetris_difficulty
            elif karma_lvl() < 3:

                $ show_chr("A-AEBAA-ALAL")
                y "B-bueno... [player], no sé si esto es simplemente una broma o solo estás tratando de impresionarme..."
                y "Todo solo para probarme algo. Solo para restregármelo en la cara..."
                y "Por otra parte, al menos es una forma de pasar el tiempo."
                $ show_chr("A-BECAA-AMAM")
                y "Bueno, lo que sea."
                y "Sigamos con ello."
                menu:
                    "20000":
                        $ TetrisScore = 20000
                    "50000":
                        $ TetrisScore = 50000
                    "100000":
                        $ TetrisScore = 100000
                    "200000":
                        $ TetrisScore = 200000
                    "300000":
                        $ TetrisScore = 300000
                    "500000":
                        $ TetrisScore = 500000
                jump tetris_difficulty
        "CO-OP":

            if karma_lvl() == 5:

                $ show_chr("A-ABABA-AMAM")
                y "¡Oh qué divertido~!"
                y "B-bueno, si insistes [player]. Es mejor cuando nos esforzamos hacia la misma meta juntos."
                y "Como dice el viejo dicho, Dios los cría y ellos se juntan. ¡Dos cabezas siempre son mejor que una ~!"
                $ show_chr("A-FCCBA-AAAL")
                y "¡Tal vez incluso se convierta en una noche entera! Ehehe..."
                $ show_chr("A-ECABA-AAAJ")
                y "¡Okay, empieza el juego querido [player]!"
                $ AI_difficulty = "CO_OP"
                jump tetris_rules
            elif karma_lvl() == 1:

                $ show_chr("A-CEBAB-AAAL")
                y "¿E-estás seguro...?"
                y "Digo, ¿por qué querrías trabajar junto a mí, mucho menos jugar un juego juntos?"
                y "¿Es esto otra vez una gran broma para ti? Yo... Ya no lo sé."

                y "Intentemos esto... supongo."




                $ AI_difficulty = "CO_OP"
                jump tetris_rules
            else:

                $ show_chr("A-ACAAA-AAAA")
                y "¿O~Oh? ¿Quieres probar el modo Cooperativo?"
                y "Bueno, supongo que podríamos intentarlo juntos... "
                y "Si realmente estás seguro de que quieres..."
                $ show_chr("A-BFAAA-AAAA")
                y "Solo espero no arruinarlo de alguna manera..."
                y "Oh, ¿qué estoy diciendo? Es solo Tetris, estará bien..."
                $ show_chr("A-AFAAA-ABAB")
                y "Así que umm... solo... probémoslo, supongo."
                $ AI_difficulty = "CO_OP"
                jump tetris_rules

label custom_tetris_checkpoint_start:
    $ show_chr("A-ACAAA-ABAB")
    y "Oh, ¿te gustaría probar suerte en una construcción personalizada de Tetris?"
    y "Bueno, déjame darte un rápido recorrido de cómo se hace o ¿ya lo tienes todo resuelto?"
    menu:
        "Pruébame":
            y "Bien"
            jump custom_tetris_checkpoint
        "No":
            y "Por cierto, probablemente deberías escribir esto en algún lugar..."


label custom_tetris_repeat:
    y "Todos esos archivos que crearás tendrán que ir a la carpeta \"game\\custom_tetris\""
    y "Lo primero que necesitas saber es que todas las imágenes tienen que estar en formato .png y todos los sonidos tienen que ser archivos .ogg. Ren'Py rechazará cualquier otra cosa."
    y "Empecemos con el fondo. {b}Conteo de Líneas{/b} y {b}Puntuación{/b} tienen dos tipos de fondo dependiendo de las dificultades."
    y "Para las dificultades Fácil, Media y Difícil tiene que ser una imagen de 220 x 420 píxeles. Usa el archivo {b}background.png{/b} de la carpeta \"game\\images\\tetris\\tetris\" como ejemplo..."
    $ show_chr("A-ACAAA-ABAD")
    y "Para los mismos modos pero en las dificultades Desventaja, Veterano y Experto, es exactamente el mismo procedimiento, pero esta vez tienes que borrar las cuadrículas y llamarlo {b}backgrund_no_grind{/b}... oh sí, ¡y todavía tiene que ser un archivo .png!"
    y "El modo Cooperativo comparte el mismo procedimiento, pero esta vez es de 421 x 420 píxeles y lo llamas {b}grids (coop).png{/b}. Está en la misma carpeta de nuevo."
    y "Ahora llegamos a los bloques."
    y "Dato curioso, ¿sabías que un solo bloque se llama Tetrómino?"
    y "Hay 7 piezas en Tetris que usualmente tienen diferentes colores. Podrías hacerlas del mismo color"
    y "Pero eso sería un poco aburrido. ¿No crees?"
    $ show_chr("A-ACAAA-AFAD")
    y "Cada pieza se construye a partir de bloques individuales que están numerados del 1 al 7."
    y "También en versiones más nuevas de Tetris. Puedes ver dónde aterrizará la pieza. Nos referimos a ella como {b}piezas sombra{/b} "
    y "También necesitan tener sus propios colores que usualmente son transparencia de bloques normales"
    y "Cada uno de los cubos necesita ser una imagen .png con tamaño 20x20. Puedes usar el archivo {b}cube_1.png{/b} de la carpeta \"game\\images\\tetris\\tetris\" como ejemplo..."
    y "Para la Pieza T configuras cube_1.png y shadow_1.png"
    y "Para la Pieza S configuras cube_2.png y shadow_2.png"
    y "Para la Pieza Z configuras cube_3.png y shadow_3.png"
    y "Para la Pieza L configuras cube_4.png y shadow_4.png"
    y "Para la Pieza J configuras cube_5.png y shadow_5.png"
    y "Para la Pieza I configuras cube_6.png y shadow_6.png"
    y "Para la Pieza O configuras cube_7.png y shadow_7.png"
    y "El último es la pared del juego. Para la pared configuras cube_8.png. La mayoría de las veces es negra para distinguir fácilmente"
    y "Por ahora en tu carpeta custome_Tetris, deberías tener 18 archivos. 2 Fondos, 8 cubos y 8 sombras png"
    y "¿Está todo bien? Si no déjame saber y repetiré el paso de nuevo"
    menu:
        "Sí":
            y "Bien. Vamos a la siguiente parte"
        "No":
            y " Oh querido. Déjame repetir los pasos de nuevo."
            jump custom_tetris_repeat


label custom_tetris_repeat_audio:
    $ show_chr("A-ACAAA-ABAD")
    y "Ahora para la parte de audio..."
    y "Todos los archivos de audio deben tener nombres específicos, de lo contrario el juego los rechazará, así que aquí están los nombres para los sonidos."
    y "Tengan en cuenta que los sfx deben ser sonidos muy cortos. Si son largos se superpondrán. Se convertirá en un desastre"
    y "Aquí están los nombres de los sonidos sfx"
    y "t-fl.ogg para una línea limpia simple."
    y "t-2f1.ogg para una línea limpia doble."
    y "t-3fl.ogg para una línea limpia triple."
    y "t-4fl.ogg para una línea limpia de tetris completo."
    y "t-drop.ogg para el sonido de caída fuerte."
    y "t-move.ogg para cada vez que mueves la pieza."
    y "t-rotate.ogg para cada vez que rotas la pieza."
    y "Esos eran sonidos sfx. Para la música principal que se repetirá durante la duración del juego."
    y "Usa \"tetris.ogg\""
    y "Así que al final tu carpeta custome_Tetris debería tener 26 archivos. 2 Fondos, 8 cubos, 8 sombras png y 8 archivos .ogg"
    $ show_chr("A-BCBAA-AEAD")
    y "E-espero no haberte confundido con esa explicación..."
    y "No soy buena explicando tales tecnicismos..."
    y "Si me equivoco y todavía necesitas ajustar algo déjame saber y repetiré los pasos"
    menu:
        "Todo está bien":
            y "Yay"
        "Por favor empieza desde el inicio":
            y "Bien"
            jump custom_tetris_repeat
        "Por favor empieza desde los archivos de audio":
            y "Bien"
            jump custom_tetris_repeat_audio
    if karma_lvl() >= 2:
        $ show_chr("A-GCAAA-AEAD")
        y "De todos modos, ¡espero con ansias lo que puedas idear!"
        y "Todo lo que haces es divertido para mí de todos modos..."
    else:
        $ show_chr("A-BFBAA-AEAD")
        y "Oh, me pregunto qué podrías idear..."
        y "Lo más probable es que algo ridículo o sin sentido..."
    call custom_tetris_checkpoint
    return

label custom_tetris_failure:
    $ show_chr("A-ACDAA-ABAB")
    y "¿[player]? Parece que necesitas arreglar algún problema que mencioné"
    y "Tal vez debería explicar todos los pasos de nuevo"
    call custom_tetris_repeat

label custom_tetris_checkpoint:

    menu:
        y "¿Tienes todo hecho?"
        "Sí.":
            python:
                from os import walk
                f = []
                for (dirpath, dirnames, filenames) in walk(config.basedir + "/game/custom_tetris"):
                    f.extend(filenames)
                    break
                custom_tetris = []

                for i in f:
                    if i.find(".ogg") == -1 and i.find(".mp3") == -1 and i.find(".wav") == -1 and i.find(".flac") == -1 and i.find(".png") == -1:
                        pass
                    else:
                        custom_tetris.append((i, i))
                custom_tetris.append(("", ""))

                if custom_tetris == [("", "")]:
                    show_chr("A-BFAAA-AAAN")
                    y("Parece que no tienes nada en la carpeta ahora mismo...")
                    show_chr("A-BBBAA-AAAN")
                    y("Está bien. Los estaré esperando de todas formas.")
                    renpy.jump("ch30_loop")
                custom_tetris_png_req = ["background", "background_no_grind"]
                custom_tetris_music_req = ["t-fl", "t-2fl", "t-3fl", "t-4fl", "t-drop", "t-move", "t-rotate", "tetris"]
                custom_tetris_all_ready = True
                for i in custom_tetris_png_req:
                    element = (i + ".png", i + ".png")
                    if not element in custom_tetris:
                        y("Parece que hay un problema con la imagen de fondo:" + i)
                        renpy.call("custom_tetris_failure")
                for i in custom_tetris_music_req:
                    element = (i + ".ogg", i + ".ogg")
                    if not element in custom_tetris:
                        y("Parece que hay un problema con los archivos de audio: " + i)
                        renpy.call("custom_tetris_failure")
                for i in range(1, 9):
                    element = ("cube_" + str(i) + ".png", "cube_" + str(i) + ".png")
                    if not element in custom_tetris:
                        y("Parece que hay un problema con la imagen del cubo de la pieza:" + i)
                        renpy.call("custom_tetris_failure")
                for i in range(1, 8):
                    element = ("shadow_" + str(i) + ".png", "shadow_" + str(i) + ".png")
                    if not element in custom_tetris:
                        y("Parece que hay un problema con la imagen de las sombras de la pieza:" + i)
                        renpy.call("custom_tetris_failure")
                persistent.skin = 6
        "No.":
            $ show_chr("A-GCBAA-AAAA")
            y "Ya veo."
            $ show_chr("A-ABBAA-AAAA")
            y "No hay necesidad de apresurarse. Tómate tu tiempo."
            jump ch30_loop
    return

label tetris_difficulty:
    $ show_chr("A-AAAAA-AAAA")
    y "Si no estás acostumbrado a Tetris, podemos ajustar la dificultad un poco. Solo dime cómo deseas que sea, no juzgaré."


    menu:
        "Fácil":
            $ AI_difficulty = 1

            if karma_lvl() >= 3:
                y "Oh, ya veo."
                y "¿Te gustaría que fuera amable contigo esta vez, hm?"
                y "¡Estoy feliz de complacerte, [player]!"

            elif karma_lvl() < 3:

                $ show_chr("A-BEAAA-AMAM")
                y "..."
                y "¿E-es esto algún tipo de broma? ¿Dirigida a mí?"
                y "¿Complacerse en esta actividad pero a un nivel tan infantil... Aparentemente para burlarse de mis habilidades?"
                $ show_chr("A-CEBAA-AAAD")
                y "Como sea... Procedamos."
        "Medio":





            $ AI_difficulty = 2

            if karma_lvl() >= 3:

                $ show_chr("A-ABABA-AAAJ")
                y "Oh ya veo~ Tratando de calentar con un ligero desafío ¿eh?"
                y "¡Bueno entonces. Me gustaría ver cómo lo haces!"
                y "Es bueno salir de tu zona de confort un poco más."

            elif karma_lvl() < 3:

                $ show_chr("A-ADCAA-AAAL")
                y "Hm... Sabes, estoy ligeramente sorprendida de que quisieras participar en este juego conmigo. Pensaba que elegirías una dificultad más difícil solo para probar un punto."
                y "Digo, ¿por qué molestarse con una dificultad tan simple con alguien como yo?"
                y "Si esto se supone que es una broma, francamente no la entiendo."
                $ show_chr("A-CECAA-ALAL")
                y "Como sea... De todos modos que empiecen los juegos."
        "Difícil":


            $ AI_difficulty = 3

            if karma_lvl() >= 3:

                $ show_chr("A-ACCAA-AMAM")
                y "Oh huhuhehehe... Realmente subiendo el nivel ahora, ¿no es así, [player]?"
                y "Bueno, me gusta cuando te pones un poco más atrevido~ Es bastante inspirador."

                y "Bueno, como dice la gente hoy en día, supongo, ¡que estos juegos comiencen!"
                y "O-oh pero no seas muy duro contigo mismo [player]... Eheheh."

            elif karma_lvl() < 3:

                $ show_chr("A-CECAA-ALAL")
                y "S-supongo que realmente quieres restregármelo en la cara solo para probar un punto..."
                y "Muy bien entonces... Que los juegos comiencen, supongo."
                y "Hmph."
        "Desventaja":


            $ AI_difficulty = 4

            if karma_lvl() >= 3:
                $ show_chr("A-DCCBA-AAAD")
                y "Mmm..."
                y "Oh querido [player]. Eso parece una tarea tan Hercúlea para realizar. ¿Estás seguro?"
                $ show_chr("A-ABAAA-ALAL")
                y "Ehehehehe... Bueno está bien si insistes~"
                y "¡Prepara tu mente y cuerpo para el penúltimo desafío de jugador querido [player]!"

            elif karma_lvl() > 3 and sanity_lvl() < 3:

                $ show_chr("A-DLCBA-AMAM")
                y "Oh oh... ¡Oh cielos, sí!"
                y "¿Un glotón por el castigo no eres [player]?"
                y "¡Cualquier cicatriz de esta tarea que lleves la cargaré contigo!"
                y "S-solo ten un poco de cuidado [player]... Si te excedes demasiado y te lastimas, podría tener que destrozar algunas cosas aquí~ Aahahaha..."
                $ show_chr("A-DCAAA-AFAG")
                y "¡¡¡Muéstrame, muéstrales a todos de qué estás hecho dulce [player]!!!"

            elif karma_lvl() < 3:

                $ show_chr("A-DEDAA-ABAB")
                y "Y-ya veo..."
                y "Supongo que solo quieres bromear conmigo entonces..."
                $ show_chr("A-BEABB-AMAM")
                y "¿Tal vez probar tu punto más allá sobre cuán más grande eres que yo? Restregármelo en la cara solo un poco más. ¿Para mostrar cuánto no me necesitas?"
                $ show_chr("A-CEAAA-AMAM")
                y "O-olvídalo... No importa lo que dijera aquí. Que los juegos comiencen supongo."
        "Experto":


            $ AI_difficulty = 5

            $ show_chr("A-ACBAA-AIAI")
            y "Oh te espera un viaje agitado [player]..."

            if persistent.lovecheck:

                $ show_chr("A-ACCBA-AIAI")
                y "...pero supongo que te gusta de esa manera, ¿no?"
            else:

                if karma_lvl() >= 3:

                    $ show_chr("A-ACBAA-ABAL")
                    y "Muy bien, intentaré lo mejor para ofrecerte un desafío adecuado."
                    y "Solo ten en cuenta, es solo un juego. Realmente no importa quién gane mientras estemos pasando un buen rato."

                elif karma_lvl() < 3:

                    $ show_chr("A-AFBAA-ABAL")
                    y "Tal vez pueda enseñarte una lección aquí..."
        "Veterano":


            $ AI_difficulty = 6
            $ show_chr("A-ACAAA-ABAL")
            y "El más alto, ya veo..."
            y "Ni siquiera estoy segura de si soy lo suficientemente buena para lograr esto pero... intentémoslo."
        "Tu elección, [persistent.yuri_nickname]":






            $ import random
            $ randomMood = random.randint(-1, 1)


            if (abs(karma_lvl() + sanity_lvl() - 10) < 2):
                if (randomMood < 1):

                    $ AI_difficulty = 1

                    $ show_chr("A-IAABA-AAAC")
                    if persistent.lovecheck == True:
                        y "Oh, qué educado de tu parte dejarme elegir. ¿Por qué no lo mantenemos casual por ahora con fácil entonces cariño~?"
                    else:
                        y "Oh, qué educado de tu parte dejarme elegir [player]. ¿Por qué no lo mantenemos casual con fácil entonces?"
                else:


                    $ AI_difficulty = 2

                    $ show_chr("A-IAABA-AAAC")
                    if persistent.lovecheck == True:
                        y "Oh, qué educado de tu parte dejarme elegir. ¿Por qué no lo mantenemos casual por ahora con medio entonces cariño~?"
                    else:
                        y "Oh, qué educado de tu parte dejarme elegir [player]. ¿Por qué no lo mantenemos casual con medio por ahora entonces?"


            elif (abs(karma_lvl() + sanity_lvl() - 8) < 2):
                if (randomMood == -1):

                    $ AI_difficulty = 1

                    $ show_chr("A-CCAAA-AAAC")
                    y "Hmm..."
                    $ show_chr("A-ICAAA-AAAC")
                    y "Estoy sintiendo algo solo un poco menos desafiante si te parece bien."
                    y "Fácil debería funcionar bien para nosotros entonces."

                elif (randomMood == 0):

                    $ AI_difficulty = 2

                    $ show_chr("A-CCAAA-AAAC")
                    y "Hmm..."
                    $ show_chr("A-ICAAA-AAAC")
                    y "Estoy sintiendo algo solo un poco desafiante si te parece bien."
                    y "Medio debería funcionar bien para nosotros entonces."
                else:


                    $ AI_difficulty = 3

                    $ show_chr("A-CCAAA-AAAC")
                    y "Hmm..."
                    $ show_chr("A-ICAAA-AAAC")
                    y "Estoy sintiendo algo con un poco decente de desafío si te parece bien."
                    y "Difícil debería funcionar bien para nosotros entonces."




            elif (abs(karma_lvl() + sanity_lvl() - 6) < 2):
                if (randomMood == -1):

                    $ AI_difficulty = 2

                    if (abs(karma_lvl() - sanity_lvl()) < 2):

                        $ show_chr("A-BCAAA-AMAM")
                        y "S-si estás cómodo con eso, [player]."
                        y "No esperes que te dé un pase libre sin embargo."
                        $ show_chr("A-IAAAA-AMAM")
                        y "Medio debería ser suficiente."

                    elif (karma_lvl() < sanity_lvl()):

                        $ show_chr("A-CECAA-AAAA")
                        y "..."
                        $ show_chr("A-CDCAA-AAAA")
                        y "¿Podrías al menos haber puesto el esfuerzo para elegir tu propia configuración de dificultad?"
                        y "Terminemos con esto. Medio será."
                    else:


                        $ show_chr("A-DBAAA-AAAA")
                        y "{b}Sería bastante divertido si siempre fueras tan pasivo hacia mí [player].{/b}"
                        $ show_chr("A-CAABA-ADAA")
                        y "..."
                        $ show_chr("A-CBABA-ADAA")
                        y "Todavía necesito seguir adelante y elegir una dificultad, ¿no? Medio debería estar bien entonces, ¿correcto?"

                elif (randomMood == 0):

                    $ AI_difficulty = 3

                    if (abs(karma_lvl() - sanity_lvl()) < 2):

                        $ show_chr("A-BCAAA-AMAM")
                        y "S-si estás cómodo con eso, [player]."
                        y "No esperes que te dé un pase libre sin embargo."
                        $ show_chr("A-IAAAA-AMAM")
                        y "Difícil debería ser suficiente."

                    elif (karma_lvl() < sanity_lvl()):

                        $ show_chr("A-CECAA-AAAA")
                        y "..."
                        $ show_chr("A-CDCAA-AAAA")
                        y "¿Podrías al menos haber puesto el esfuerzo para elegir tu propia configuración de dificultad?"
                        y "Terminemos con esto. Difícil será."
                    else:


                        $ show_chr("A-DBAAA-AAAA")
                        y "{b}Sería bastante divertido si siempre fueras tan pasivo hacia mí [player].{/b}"
                        $ show_chr("A-CAABA-ADAA")
                        y "..."
                        $ show_chr("A-CBABA-ADAA")
                        y "Todavía necesito seguir adelante y elegir una dificultad, ¿no? Difícil debería estar bien entonces, ¿correcto?"
                else:


                    $ AI_difficulty = 4

                    if (abs(karma_lvl() - sanity_lvl()) < 2):

                        $ show_chr("A-BCAAA-AMAM")
                        y "S-si estás cómodo con eso, [player]."
                        y "No esperes que te dé un pase libre sin embargo."
                        $ show_chr("A-IAAAA-AMAM")
                        y "Desventaja debería ser suficiente."

                    elif (karma_lvl() < sanity_lvl()):

                        $ show_chr("A-CECAA-AAAA")
                        y "..."
                        $ show_chr("A-CDCAA-AAAA")
                        y "¿Podrías al menos haber puesto el esfuerzo para elegir tu propia configuración de dificultad?"
                        y "Terminemos con esto. Desventaja será."
                    else:


                        $ show_chr("A-DBAAA-AAAA")
                        y "{b}Sería bastante divertido si siempre fueras tan pasivo hacia mí [player].{/b}"
                        $ show_chr("A-CAABA-ADAA")
                        y "..."
                        $ show_chr("A-CBABA-ADAA")
                        y "Todavía necesito seguir adelante y elegir una dificultad, ¿no? Desventaja debería estar bien entonces, ¿correcto?"




            elif (abs(karma_lvl() + sanity_lvl() - 4) < 2):
                if (randomMood == -1):

                    $ AI_difficulty = 3

                    if (abs(karma_lvl() - sanity_lvl()) < 2):

                        $ show_chr("A-CEAAA-AAAC")
                        y "N-no sé realmente..."
                        y "¿Realmente importa en qué dificultad jugamos?"
                        y "Supongo que iré por difícil, probablemente solo te jactarás de ello después de todos modos."

                    elif (karma_lvl() < sanity_lvl()):

                        $ show_chr("A-CEAAA-AAAC")
                        y "N-no sé realmente..."
                        y "¿Realmente importa en qué dificultad jugamos?"
                        y "Supongo que iré por difícil, probablemente solo te jactarás de ello después de todos modos..."
                        $ show_chr("A-CEAAB-AAAJ")
                        y "¿Qué hice para merecer este tipo de tratamiento de todos modos?"
                        y "..."
                        $ show_chr("A-CEAAA-AAAK")
                        y "Solo sigamos con ello ya."
                    else:


                        y "¿Qué tal si vamos por difícil si estás dispuesto?"
                        $ show_chr("A-DAAAA-AAAD")
                        y "Sería bastante divertido presionarte solo un poco."
                        y "Sin mencionar que es lindo verte retorcerte tratando de seguirme el ritmo."

                elif (randomMood == 0):

                    $ AI_difficulty = 4

                    if (abs(karma_lvl() - sanity_lvl()) < 2):

                        $ show_chr("A-CEAAA-AAAC")
                        y "N-no sé realmente..."
                        y "¿Realmente importa en qué dificultad jugamos?"
                        y "Supongo que iré por desventaja, probablemente solo te jactarás de ello después de todos modos."

                    elif (karma_lvl() < sanity_lvl()):

                        $ show_chr("A-CEAAA-AAAC")
                        y "N-no sé realmente..."
                        y "¿Realmente importa en qué dificultad jugamos?"
                        y "Supongo que iré por desventaja, probablemente solo te jactarás de ello después de todos modos..."
                        $ show_chr("A-CEAAB-AAAJ")
                        y "¿Qué hice para merecer este tipo de tratamiento de todos modos?"
                        y "..."
                        $ show_chr("A-CEAAA-AAAK")
                        y "Solo sigamos con ello ya."
                    else:


                        y "¿Qué tal si vamos por desventaja si estás dispuesto?"
                        $ show_chr("A-DAAAA-AAAD")
                        y "Sería bastante divertido presionarte solo un poco."
                        y "Sin mencionar que es lindo verte retorcerte tratando de seguirme el ritmo."
                else:


                    $ AI_difficulty = 5

                    if (abs(karma_lvl() - sanity_lvl()) < 2):

                        $ show_chr("A-CEAAA-AAAC")
                        y "N-no sé realmente..."
                        y "¿Realmente importa en qué dificultad jugamos?"
                        y "Supongo que iré por experto, probablemente solo te jactarás de ello después de todos modos."

                    elif (karma_lvl() < sanity_lvl()):

                        $ show_chr("A-CEAAA-AAAC")
                        y "N-no sé realmente..."
                        y "¿Realmente importa en qué dificultad jugamos?"
                        y "Supongo que iré por experto, probablemente solo te jactarás de ello después de todos modos..."
                        $ show_chr("A-CEAAB-AAAJ")
                        y "¿Qué hice para merecer este tipo de tratamiento de todos modos?"
                        y "..."
                        $ show_chr("A-CEAAA-AAAK")
                        y "Solo sigamos con ello ya."
                    else:


                        y "¿Qué tal si vamos por experto si estás dispuesto?"
                        $ show_chr("A-DAAAA-AAAD")
                        y "Sería bastante divertido presionarte solo un poco."
                        y "Sin mencionar que es lindo verte retorcerte tratando de seguirme el ritmo."




            elif (abs(karma_lvl() + sanity_lvl() - 2) < 2):
                if (randomMood == -1):

                        y "N-No espera, ¿sabes qué?"
                        y "Esta sería una buena oportunidad para ponerte en tu lugar, y no la desperdiciaré."
                        $ show_chr ("A-AECAA-AAAG")
                        y "Pongámoslo en desventaja y veamos qué tan bien lo haces."

                elif (randomMood == 0):

                    $ AI_difficulty = 5

                    if (karma_lvl() < sanity_lvl()):
                        $ show_chr ("A-AECAA-AAAF")
                        y "Honestamente no podría importarme menos en qué dificultad juguemos a este punto."
                        y "N-No espera, ¿sabes qué?"
                        y "Esta sería una buena oportunidad para ponerte en tu lugar, y no la desperdiciaré."
                        y "Pongámoslo en experto y veamos qué tan bien lo haces."
                    else:

                        $ show_chr("A-AECAA-AAAF")
                        y "Honestamente no podría importarme menos en qué dificultad juguemos a este punto."
                        y "N-No espera, ¿sabes qué?"
                        y "Esta sería una buena oportunidad para ponerte en tu lugar, y no la desperdiciaré."
                        $ show_chr ("A-AECAA-AAAG")
                        y "Pongámoslo en experto y veamos qué tan bien lo haces."
                else:


                    $ AI_difficulty = 6

                    if (karma_lvl() < sanity_lvl()):
                        $ show_chr ("A-AECAA-AAAF")
                        y "Honestamente no podría importarme menos en qué dificultad juguemos a este punto."
                        y "N-No espera, ¿sabes qué?"
                        y "Esta sería una buena oportunidad para ponerte en tu lugar, y no la desperdiciaré."
                        y "Pongámoslo en veterano y veamos qué tan bien lo haces."
                    else:

                        $ show_chr("A-AECAA-AAAF")
                        y "Honestamente no podría importarme menos en qué dificultad juguemos a este punto."
                        y "N-No espera, ¿sabes qué?"
                        y "Esta sería una buena oportunidad para ponerte en tu lugar, y no la desperdiciaré."
                        $ show_chr ("A-AECAA-AAAG")
                        y "Pongámoslo en veterano y veamos qué tan bien lo haces."


            elif (abs(karma_lvl() + sanity_lvl()) < 2):
                if (randomMood == -1):

                    $ AI_difficulty = 5

                    $ show_chr("A-DBCAA-AAAF")
                    y "{b}JA JA...{/b}"
                    y "¿Quieres que yo elija la dificultad?"
                    y "Bien [player], tus deseos son órdenes."
                    $ show_chr("A-DBCAA-AAAC")
                    y "¿Qué tal experto hmm? Parece una competencia justa, ¿no crees?"
                    $ show_chr("A-CBCAA-AAAC")
                    y "Solo espero que seas capaz de mantener el ritmo. Sería una lástima si diezmara el marcador."
                else:


                    $ AI_difficulty = 6

                    $ show_chr("A-DBCAA-AAAF")
                    y "{b}JA JA...{/b}"
                    y "¿Quieres que yo elija la dificultad?"
                    y "Bien [player], tus deseos son órdenes."
                    $ show_chr("A-DBCAA-AAAC")
                    y "¿Qué tal veterano hmm? Parece una competencia justa, ¿no crees?"
                    $ show_chr("A-CBCAA-AAAC")
                    y "Solo espero que seas capaz de mantener el ritmo. Sería una lástima si diezmara el marcador."


label tetris_rules:
    $ show_chr("A-GAGAA-AAAA")
    if persistent.tetris_first:
        y "Permíteme explicar los controles..."
        y "Puedes usar las flechas para mover tus piezas. Presionar ARRIBA rotará tu pieza, presionar ABAJO acelerará tu caída."
        y "Presionar ESPACIO dejará caer la pieza instantáneamente."
        y "La tecla Q pondrá la pieza en reserva, pero no puedes reservar dos veces la misma pieza..."
        y "...Mientras que la tecla E usará la pieza que estás reservando."
        $ persistent.tetris_first = False


    menu:
        y "¿Te gustaría algo de música de Tetris mientras jugamos?"
        "Sí":
            if AI_difficulty != "CO_OP":
                y "Que gane el mejor jugador de Tetris."
                $ show_chr("A-AACAA-AAAA")
                y "¡A jugar, [player]!"
                $ renpy.free_memory()
            else:
                y "¡Disfrutemos nuestro tiempo juntos tratando de obtener la puntuación más alta!"
                $ show_chr("A-CBBAA-AAAJ")
                y "Realmente espero ser de al menos algo de ayuda para ti, [player]."
                $ show_chr("A-AACAA-AAAA")
                $ renpy.free_memory()
            if persistent.skin == 1:
                $ change_music("<loop 21.06>/music/tetris (a).ogg")

            elif persistent.skin == 2:
                $ change_music("<loop 0.80>/music/tetris_99.ogg")
            elif persistent.skin == 3:
                $ change_music("<loop 19.30>/music/tetris_gb.ogg")
            elif persistent.skin == 4:
                $ change_music("<loop 0>/music/tetris_gmd.ogg")
            elif persistent.skin == 5:
                $ change_music("<loop 0>/music/tetris_m1nd_bend3r.ogg")
            elif persistent.skin == 6:
                $ change_music("<loop 0>/custom_tetris/tetris.ogg")
        "No":
            if AI_difficulty != "CO_OP":
                y "Que gane el mejor jugador de Tetris."
                $ show_chr("A-AACAA-AAAA")
                y "¡A jugar, [player]!"
                $ renpy.free_memory()
            else:
                y "¡Disfrutemos nuestro tiempo juntos tratando de obtener la puntuación más alta!"
                $ show_chr("A-CBBAA-AAAJ")
                y "Realmente espero ser de al menos algo de ayuda para ti, [player]."
                $ show_chr("A-AACAA-AAAA")
                $ renpy.free_memory()

    call screen startTetris(AI_difficulty)

label tetris_over:
    $ change_music(current_music)
    $ renpy.free_memory()
    if TetrisWinner == 0:
        if karma_lvl() > 3 and sanity_lvl() > 3:

            $ show_chr("A-ABABA-AAAL")
            y "¡¡O-oh cielos!! Oh eso fue bastante emocionante~"
            y "Disfruté solo estando en ese momento contigo [player]. Aunque pude haberme esforzado por una puntuación más alta."
            $ show_chr("A-CCAAA-AAAD")
            y "¡De verdad sin embargo, es de hecho el momento compartido juntos y el corazón lo que cuenta!"
            y "Jejeje... Aunque admitiré que parte de mí sí quiere intentar de nuevo y ver si obtengo una puntuación más alta."
            $ show_chr("A-ABAAA-AMAM")
            y "¡De cualquier manera creo que ambos pusimos nuestro mejor esfuerzo!"

            menu:
                y "Entonces [player], ¿quieres intentar de nuevo? ¿Nosotros juntos una vez más?"
                "Sí":
                    menu:
                        y "¿Te gustaría la misma música que en nuestro último juego?"
                        "Sí":
                            if persistent.skin == 1:
                                $ change_music("<loop 21.06>/music/tetris (a).ogg")
                            elif persistent.skin == 2:
                                $ change_music("<loop 0.80>/music/tetris_99.ogg")
                            elif persistent.skin == 3:
                                $ change_music("<loop 19.30>/music/tetris_gb.ogg")
                            elif persistent.skin == 4:
                                $ change_music("<loop 0>/music/tetris_gmd.ogg")
                            elif persistent.skin == 5:
                                $ change_music("<loop 0>/music/tetris_m1nd_bend3r.ogg")
                            elif persistent.skin == 6:
                                $ change_music("<loop 0>/custom_tetris/tetris.ogg")
                            call screen startTetris(AI_difficulty)
                        "No":

                            call screen startTetris(AI_difficulty)
                "No":
                    $ show_chr("A-GBAAA-AMAM")
                    y "Realmente disfruto jugar contigo. Hagamos esto de nuevo pronto."
                    jump ch30_loop

        elif karma_lvl() > 3 and sanity_lvl() == 3:

            $ show_chr("A-BCAAA-AMAM")
            y "O-oh cielos... Oh espero no haber cometido muchos errores."
            y "Jejeje..."
            $ show_chr("A-BCABA-AMAM")
            y "Digo obviamente creo que tus habilidades son encantadoras... S-solo no quiero a-aburrirte demasiado con las mías... ¡Digo! Fue un tiempo encantador y lo aprecié mucho."
            $ show_chr("A-ACAAA-AAAC")

            menu:
                y "De todos modos... ¿T-te gustaría jugar esto de nuevo conmigo [player]...?"
                "Sí":
                    call screen startTetris(AI_difficulty)
                    $ renpy.music.play()
                "No":
                    $ show_chr("A-GBAAA-AMAM")
                    y "Realmente disfruto jugar contigo. Hagamos esto de nuevo pronto."
                    jump ch30_loop
        elif karma_lvl() <= 2:

            $ show_chr("A-ACAAA-AAAC")
            y "¿O-oh ganaste eh...?"
            y "Supongo que ahora sería un buen momento para restregarme que me ganaste."
            $ show_chr("A-ACAAA-AAAC")
            y "A-adelante. Jáctate todo lo que quieras."
            y "Apuesto a que solo fingiste divertirte jugando contra mí..."
            y "Anda [player]."
        elif sanity_lvl() > 2 and karma_lvl() < 3:
            $ show_chr("A-ACAAA-AAAA")
            y "Felicidades, bien hecho."
            y "Tengo que admitir, eso fue más divertido de lo que anticipé. De hecho estaba un poco preocupada de que Tetris pudiera volverse aburrido bastante rápido."
            $ show_chr("A-ACAAA-ALAL")

            menu:
                y "¿Espero que te hayas divertido un poco también? Si deseas podríamos intentar otra ronda. ¿Estás listo para la revancha?"
                "Sí":
                    call screen startTetris(AI_difficulty)
                    $ renpy.music.play()
                "No":
                    $ show_chr("A-GBAAA-AMAM")
                    y "Realmente disfruto jugar contigo. Hagamos esto de nuevo pronto."
                    jump ch30_loop
        elif sanity_lvl() <= 3 and karma_lvl() >= 3:
            $ show_chr("A-ACAAA-ABAB")
            y "¡Oh cielos, parece que me has ganado!"
            y "Podría tener que poner más entrenamiento en esto, para poder ser un desafío real la próxima vez."
            y "De hecho, ¿te gustaría darle otro intento? Jugar contigo resultó ser muy divertido, incluso si es solo Tetris."
            $ show_chr("A-BCAAA-ABAC")
            y "Podríamos probablemente intentar algo más en el futuro. ¿Ajedrez, o tal vez un juego de cartas?"
            y "También pensé en dardos, pero honestamente no tengo idea de cómo codificar eso..."
            $ show_chr("A-ACAAA-ABAE")

            menu:
                y "Oh pero casi lo olvido, ¿te gustaría jugar otra ronda conmigo?"
                "Sí":
                    call screen startTetris(AI_difficulty)
                    $ renpy.music.play()
                "No":
                    $ show_chr("A-GBAAA-AMAM")
                    y "Realmente disfruto jugar contigo. Hagamos esto de nuevo pronto."
                    jump ch30_loop
        elif sanity_lvl() <= 3 and karma_lvl() < 3:
            $ show_chr("A-BFAAA-ABAE")
            y "¿Felicidades, supongo?"
            $ show_chr("A-IFAAA-ABAE")
            y "Oh lo siento, no quise sonar tan poco entusiasta."
            y "Es solo... encuentro un poco difícil concentrarme ahora mismo. No puedo evitar preguntarme cómo terminamos aquí así."
            $ show_chr("A-CFAAA-ABAE")
            y "Perdóname, ¿soy muy dramática? Lo que quise decir es... desearía que pudiéramos hacer más juntos que jugar Tetris. Por favor no le des muchas vueltas."

            menu:
                extend "¿Te gustaría jugar otra ronda?"
                "Sí":
                    call screen startTetris(AI_difficulty)
                    $ renpy.music.play()
                "No":
                    jump ch30_loop
    elif TetrisWinner == 1:
        if sanity_lvl() > 2 and karma_lvl() > 2:
            $ show_chr("A-ACAAA-ALAL")
            y "Oh cielos..."
            y "Buen espectáculo, buen esfuerzo~"
            $ show_chr("A-ACABA-AAAD")
            y "¡Sé que querías una puntuación más alta pero siempre habrá una próxima vez!"
            y "¡Espero que te hayas divertido, [player], sé que yo lo hice!"

        elif karma_lvl() > 4 and sanity_lvl() == 3:

            $ show_chr("A-ACDAA-AMAM")
            y "O-oh... ¿Perdiste? Uhm... jeje."
            y "E-espero no haberme puesto demasiado intensa para ti. No te sientas mal por ello [player]. Tuve mucha diversión."
            y "Espero que tú también... O-oh... digo pero... Podemos hacer algo más si quisieras. Realmente espero que lo hayas disfrutado sin embargo. E-Significa tanto para mí... Solo tiempo juntos así."
            y "¿Te hice sentir mal [player]? Espero que no... Te daría un abrazo al menos por tus esfuerzos..."
            $ show_chr("A-ACAAA-ABAB")
            y "Es el corazón y la intención lo que c-cuenta después de todo."
            y "A-así que... ¿quieres jugar de nuevo? O si quieres hacer algo más, eso está bien también [player]~"

        elif karma_lvl() != 3 and sanity_lvl() != 3:

            $ show_chr("A-BCABA-AMAM")
            y "B-bueno... Esto fue bastante intrigante por decir lo menos."
            y "No estoy exactamente segura si este tiempo juntos cuenta o si importa pero... estoy intrigada por este juego de combinar bloques y fichas."
            $ show_chr("A-JEDBA-AMAM")
            y "Si estás aquí y escuchando esto [player] diría que esta sesión estuvo bien y me siento ligeramente mal de que perdieras."
            y "¿T-tal vez esta actividad podría ayudarme a relajarme y orientarme para acostumbrarme a estar aquí y tal vez conocerte más?"
            $ show_chr("A-ACAAA-AAAC")
            y "N-no estoy segura..."
            y "¿Q-quieres jugar un poco más [player]?"

        elif sanity_lvl() > 2 and karma_lvl() < 3:
            $ show_chr("A-AEAAA-AAAC")
            y "Oh... perdiste, ¿eh?"
            y "Bueno entonces eso no es sorpresa, supongo."
            y "Digo, no es que te importara mi opinión tal vez pero..."
            $ show_chr("A-CEAAA-AAAL")
            y "Hm..."
            y "Bueno, todavía espero que hayas disfrutado jugar... Supongo."

        elif sanity_lvl() < 3 and karma_lvl() > 3:

            $ show_chr("A-ABAAA-AAAD")
            y "Aww... lo siento [player]~"
            y "Parece que gané de nuevo uhuhuhu~"
            y "No te sientas tan mal sin embargo, amor..."
            y "Tuve un tiempo inmensamente placentero solo jugando contigo. Imaginando verte tan concentrado y determinado con el sudor corriendo por tu cara mientras intentabas anotar."
            $ show_chr("A-HCCAA-AMAM")
            y "Tu dulce sudor y esencia... Tus ojos enfocándose en los míos mientras los colores del juego brillaban en tu cara. Solo para mí, y solo para mí."
            $ show_chr("A-HLAAA-AFAG")
            y "Espero con ansias otra sesión contigo como siempre [player]. Por siempre y solo nosotros..."
            y "¡Nadie MÁS!... Solo nosotros uhuhuhehehe...~"

        elif karma_lvl() == 3 and sanity_lvl() <= 2:

            $ show_chr("A-HLAAA-ALAL")
            y "Aww, ¿perdiste?"
            y "B-bueno oye no te sientas mal y te vayas tan pronto..."
            y "Podemos quedarnos aquí en esta habitación juntos por siempre. Respirando los aromas del otro mientras sudamos y jugamos este maravilloso clásico juntos."
            $ show_chr("A-HCAAA-ALAL")
            y "Aquí en esta habitación y nadie más... Sé que quieres... Y yo quiero también~"
            y "¿Qué dices [player]? ¿No suena eso tan celestial?"

        elif sanity_lvl() < 3 and karma_lvl() < 3:
            $ show_chr("A-DECAA-ABAB")
            y "Oh, así que perdiste, ¿hm?"
            y "Bueno, eso no es sorprendente."
            $ show_chr("A-CDCAA-AAAL")
            y "Eso fue honestamente incluso bastante... patético..."
            y "Para ser honesta, esperaba un desafío mayor."

    elif TetrisWinner == 2:
        $ show_chr("A-IBCAA-AAAL")
        y "¡[player], Superamos nuestra Puntuación más alta!"
        $ show_chr("A-GBAAA-AAAL")
        y "Ese fue un gran juego, también..."
    else:
        $ show_chr("A-BEBAA-AMAM")
        y "Lo siento [player]... nos quedamos cortos de nuestra puntuación más alta."
        $ show_chr("A-CBAAA-AMAM")
        y "¡Pero no te preocupes! Siempre hay una próxima vez..."

    jump ch30_loop

screen startTetris(AI_difficulty):
    if AI_difficulty != "CO_OP":
        fixed:
            area (150, 120, 600, 1100)
            if AI_difficulty < 7:
                default tetris_player = tetris(0)
            else:
                default tetris_player = tetris(-1)
            add tetris_player

        fixed:
            area (900, 120, 600, 1100)
            default tetris_Yuri = tetris(AI_difficulty)
            add tetris_Yuri
    else:
        fixed:
            area (50, 120, 600, 1100)
            default tetris_Co_OP = Co_OP_tetris()
            add tetris_Co_OP

init python:

    import pygame
    class tetris(renpy.Displayable):
        def __init__(self, AI):
            renpy.Displayable.__init__(self)
            if AI == -1:
                self.put_shadow = 0
                self.AI = AI + 1
            else:
                self.put_shadow = 1
                self.AI = AI
            self.movesAI = []
            self.PIXEL_SIZE = 20
            self.piece_list = [0,1,2,3,4,5,6]
            random.shuffle(self.piece_list)
            self.tetris_shapes = [
                [[1, 1, 1],
                [0, 1, 0]],

                [[0, 2, 2],
                [2, 2, 0]],

                [[3, 3, 0],
                [0, 3, 3]],

                [[4, 0, 0],
                [4, 4, 4]],

                [[0, 0, 5],
                [5, 5, 5]],

                [[6, 6, 6, 6]],

                [[7, 7],
                [7, 7]]
            ]
            
            self.stage = [[9,9,9,9,9,9,9,9,9,9,9,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,9,9,9,9,9,9,9,9,9,9,9]]
            
            if persistent.skin == 1:
                
                self.color_1 = Image("images/tetris/tetris/cube_1.png")
                self.color_2 = Image("images/tetris/tetris/cube_2.png")
                self.color_3 = Image("images/tetris/tetris/cube_3.png")
                self.color_4 = Image("images/tetris/tetris/cube_4.png")
                self.color_5 = Image("images/tetris/tetris/cube_5.png")
                self.color_6 = Image("images/tetris/tetris/cube_6.png")
                self.color_7 = Image("images/tetris/tetris/cube_7.png")
                self.color_9 = Image("images/tetris/tetris/cube_8.png")
                
                self.shadow_color_1 = Image("images/tetris/tetris/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris/cube_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound2line = "sfx/t-2fl.ogg"
                self.sound3line = "sfx/t-3fl.ogg"
                self.sound4line = "sfx/t-4fl.ogg"
            
            elif persistent.skin == 2:
                
                self.color_1 = Image("images/tetris/tetris_99/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_99/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_99/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_99/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_99/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_99/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_99/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_99/cube_8.png")
                
                self.shadow_color_1 = Image("images/tetris/tetris_99/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_99/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_99/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_99/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_99/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_99/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_99/cube_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(99).ogg"
                self.soundline = "sfx/t-fl(99).ogg"
                self.soundldrop = "sfx/t-fl-drop(99).ogg"
                self.soundmove = "sfx/t-move(99).ogg"
                self.soundrotate = "sfx/t-rotate(99).ogg"
                self.sound2line = "sfx/t-2fl(99).ogg"
                self.sound3line = "sfx/t-3fl(99).ogg"
                self.sound4line = "sfx/t-4fl(99).ogg"
            
            elif persistent.skin == 3:
                
                self.color_1 = Image("images/tetris/tetris_gb/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_gb/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_gb/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_gb/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_gb/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_gb/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_gb/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_gb/cube_8.png")
                
                self.shadow_color_1 = Image("images/tetris/tetris_gb/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_gb/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_gb/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_gb/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_gb/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_gb/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_gb/cube_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound2line = "sfx/t-2fl.ogg"
                self.sound3line = "sfx/t-3fl.ogg"
                self.sound4line = "sfx/t-4fl.ogg"
            
            elif persistent.skin == 4:
                
                
                self.color_1 = Image("images/tetris/tetris_gmd/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_gmd/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_gmd/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_gmd/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_gmd/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_gmd/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_gmd/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_gmd/cube_8.png")
                
                self.shadow_color_1 = Image("images/tetris/tetris_gmd/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_gmd/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_gmd/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_gmd/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_gmd/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_gmd/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_gmd/cube_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(g).ogg"
                self.soundline = "sfx/t-fl(g).ogg"
                self.soundldrop = "sfx/t-fl-drop(g).ogg"
                self.soundmove = "sfx/t-move(g).ogg"
                self.soundrotate = "sfx/t-rotate(g).ogg"
                self.sound2line = "sfx/t-2fl(g).ogg"
                self.sound3line = "sfx/t-3fl(g).ogg"
                self.sound4line = "sfx/t-4fl(g).ogg"
            
            elif persistent.skin == 5:
                
                
                self.color_1 = Image("images/tetris/tetris_mb/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_mb/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_mb/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_mb/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_mb/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_mb/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_mb/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_mb/cube_8.png")
                
                self.shadow_color_1 = Image("images/tetris/tetris_mb/shadow_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_mb/shadow_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_mb/shadow_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_mb/shadow_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_mb/shadow_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_mb/shadow_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_mb/shadow_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(mb).ogg"
                self.soundline = "sfx/t-fl(mb).ogg"
                self.soundldrop = "sfx/t-fl-drop(mb).ogg"
                self.soundmove = "sfx/t-move(mb).ogg"
                self.soundrotate = "sfx/t-rotate(mb).ogg"
                self.sound2line = "sfx/t-2fl(mb).ogg"
                self.sound3line = "sfx/t-3fl(mb).ogg"
                self.sound4line = "sfx/t-4fl(mb).ogg"
            
            elif persistent.skin == 6:
                
                
                self.color_1 = Image("/custom_tetris/cube_1.png")
                self.color_2 = Image("/custom_tetris/cube_2.png")
                self.color_3 = Image("/custom_tetris/cube_3.png")
                self.color_4 = Image("/custom_tetris/cube_4.png")
                self.color_5 = Image("/custom_tetris/cube_5.png")
                self.color_6 = Image("/custom_tetris/cube_6.png")
                self.color_7 = Image("/custom_tetris/cube_7.png")
                self.color_9 = Image("/custom_tetris/cube_8.png")
                
                self.shadow_color_1 = Image("/custom_tetris/shadow_1.png")
                self.shadow_color_2 = Image("/custom_tetris/shadow_2.png")
                self.shadow_color_3 = Image("/custom_tetris/shadow_3.png")
                self.shadow_color_4 = Image("/custom_tetris/shadow_4.png")
                self.shadow_color_5 = Image("/custom_tetris/shadow_5.png")
                self.shadow_color_6 = Image("/custom_tetris/shadow_6.png")
                self.shadow_color_7 = Image("/custom_tetris/shadow_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "/custom_tetris/t-drop.ogg"
                self.soundline = "/custom_tetris/t-fl.ogg"
                self.soundldrop = "/custom_tetris/t-fl-drop.ogg"
                self.soundmove = "/custom_tetris/t-move.ogg"
                self.soundrotate = "/custom_tetris/t-rotate.ogg"
                self.sound2line = "/custom_tetris/t-2fl.ogg"
                self.sound3line = "/custom_tetris/t-3fl.ogg"
                self.sound4line = "/custom_tetris/t-4fl.ogg"
            
            
            class current_shape:
                shape = ""
                shape_number = ""
                shape_hold = ""
                new_shape_number = self.piece_list[0]
                next_shape = self.tetris_shapes[new_shape_number]
                x = 5
                y = 1
                move_time = 0.300
                speed = 0.60 - 2
            self.was_it_hold = False
            self.temp_position = 3
            self.current_shape = current_shape()
            self.level = 1
            self.allLines = 0
            self.oldst = None
            self.new_shape = True
            self.game_over = False
            self.winner = None
            self.Yuri_Face = 0
        
        
        
        def addShapeToStage(self, current_x, current_y):
            for idr, row in enumerate(self.current_shape.shape):
                for idc, column in enumerate(row):
                    if column != 0:
                        self.stage[current_y+idr][current_x+idc]=column
        
        def render(self, width, height, st, at):
            global PlayerForYuri
            
            def winner(win):
                global TetrisWinner
                if win == 0:
                    if self.AI == 0:
                        TetrisWinner = 0   
                    else:
                        TetrisWinner = 1   
                else:
                    if self.AI == 0:
                        TetrisWinner = 1   
                    else:
                        TetrisWinner = 0   
            
            for idc in range(4, 8):
                if self.stage[1][idc] != 0:
                    self.game_over = True
                    winner(1)
            
            if TetrisScore !=0:
                if self.score >= TetrisScore:
                    self.game_over = True
                    winner(0)
            
            elif LineLimit !=0:
                if self.allLines >= LineLimit:
                    self.game_over = True
                    winner(0)
            
            if self.game_over:
                import pygame
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            renpy.jump("tetris_over")
            
            
            
            def lines():
                numberOfFullLines = 0
                
                prevLine = False
                for idr in range(1, 21):
                    fullLine = True
                    for idc in range(1, 11):
                        if self.stage[idr][idc] == 0:
                            fullLine = False
                            break
                    if fullLine:
                        numberOfFullLines += 1
                        renpy.sound.play(self.soundline)
                        for idc in range(1, 11):
                            self.stage[idr][idc] = 0
                        if prevLine != fullLine:
                            for i in range(0, idr-1):
                                for idc in range(1, 11):
                                    self.stage[idr-i][idc] = self.stage[idr-i-1][idc]
                                    self.stage[idr-i-1][idc] = 0
                                    fullLine = False
                    prevLine = fullLine
                
                
                self.allLines += numberOfFullLines
                if numberOfFullLines == 1:
                    self.score += 100 * self.level
                elif numberOfFullLines == 2:
                    self.score += 300 * self.level
                    renpy.sound.play(self.sound2line)
                elif numberOfFullLines == 3:
                    self.score += 500 * self.level
                    renpy.sound.play(self.sound3line)
                elif numberOfFullLines == 4:
                    self.score += 800 * self.level
                    renpy.sound.play(self.sound4line)
                self.level =  int(self.allLines/10)+1
            
            r = renpy.Render(width, height)
            if persistent.skin == 1:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("images/tetris/tetris/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("images/tetris/tetris/background.png"), width, height, st, at)
            
            elif persistent.skin == 2:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("images/tetris/tetris_99/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("images/tetris/tetris_99/background.png"), width, height, st, at)
            
            elif persistent.skin == 3:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("images/tetris/tetris_gb/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("images/tetris/tetris_gb/background.png"), width, height, st, at)
            
            elif persistent.skin == 4:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("images/tetris/tetris_gmd/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("images/tetris/tetris_gmd/background.png"), width, height, st, at)
            
            elif persistent.skin == 5:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("images/tetris/tetris_mb/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("images/tetris/tetris_mb/background.png"), width, height, st, at)
            
            elif persistent.skin == 6:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("/custom_tetris/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("/custom_tetris/background.png"), width, height, st, at)
            r.blit(background, (0, 0))
            lines()
            if self.new_shape:
                self.was_it_hold = False
                self.current_shape.x = 5
                self.current_shape.y = 1
                self.current_shape.shape = self.current_shape.next_shape
                self.current_shape.shape_number = self.current_shape.new_shape_number
                self.piece_list.pop(0)
                if not self.piece_list:
                    self.piece_list = [0,1,2,3,4,5,6]
                    random.shuffle(self.piece_list)
                self.current_shape.new_shape_number = self.piece_list[0]
                self.current_shape.next_shape = self.tetris_shapes[self.current_shape.new_shape_number]
                self.new_shape = False
                self.temp_position = 1
                if self.AI != 0:
                    temp_AI = True
                    for idc in range(1, 11):
                        if self.stage[2][idc] != 0:
                            temp_AI = False
                    if temp_AI:
                        self.movesAI = self.Yuri_AI()
            
            if self.oldst is None:
                self.oldst = st
            if self.level > 19:
                speed_Y = 18
            else:
                speed_Y = self.level
            if self.AI == 1:
                if self.current_shape.y >= 10:
                    self.current_shape.speed = 0.30
            elif self.AI == 2:
                if self.current_shape.y >= 5:
                    self.current_shape.speed = 0.15
            elif self.AI == 3:
                if self.current_shape.y >= 2.5:
                    self.current_shape.speed = 0.075
            elif self.AI == 4:
                if self.current_shape.y >= 0.625:
                    self.current_shape.speed = 0.0375 - 13
            elif self.AI == 5:
                if self.current_shape.y >= 0.3125:
                    self.current_shape.speed = 0.01875 - 26
            elif self.AI == 6:
                if self.current_shape.y >= 0.15625:
                    self.current_shape.speed = 0.009375 - 39
            
            if self.temp_position == self.current_shape.y:
                if len(self.movesAI) != 0:
                    if self.movesAI[0] == "r":
                        self.rotateClockWiseAI()
                    else:
                        self.current_shape.x += int(self.movesAI[0])
                    del self.movesAI[0]
                    self.temp_position += 1
            
            dtime = st - self.oldst
            self.oldst = st
            temp_can_go_down = True
            if self.current_shape.move_time <= 0:
                
                for idr, row in enumerate(self.current_shape.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape.y + 1 + idr][self.current_shape.x + idc] != 0:
                                temp_can_go_down = False
                                renpy.sound.play(self.soundbdrop)
                                break
                if temp_can_go_down != False:
                    self.current_shape.move_time = self.current_shape.speed
                    self.current_shape.y += 1
                else:
                    self.new_shape = True
                    self.addShapeToStage(self.current_shape.x, self.current_shape.y)
            else:
                self.current_shape.move_time -= dtime
            
            def draw_shape(sx, sy, current_shape,shadow):
                for idr, row in enumerate(current_shape):
                    for idc, column in enumerate(row):
                        if column == 1:
                            shape = renpy.render(self.color_1, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_1, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 2:
                            shape = renpy.render(self.color_2, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_2, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 3:
                            shape = renpy.render(self.color_3, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_3, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 4:
                            shape = renpy.render(self.color_4, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_4, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 5:
                            shape = renpy.render(self.color_5, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_5, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 6:
                            shape = renpy.render(self.color_6, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_6, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 7:
                            shape = renpy.render(self.color_7, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_7, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 9:
                            shape = renpy.render(self.color_9, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
            
            
            b = "Líneas - %(s)d " % {"s":self.allLines }
            c = "Nivel - %(s)d " % {"s":self.level}
            d = "Siguiente:"
            
            f = Text(b)
            g = Text(c)
            h = Text(d)
            
            text_allLines_render = renpy.render(f, width, height, st, at)
            text_level_render = renpy.render(g, width, height, st, at)
            text_next_render = renpy.render(h, width, height, st, at)
            
            
            if self.AI == 0:
                r.blit(text_allLines_render, (-120, -100))
                r.blit(text_level_render, (-120, -50))
                r.blit(text_next_render, (-120, -10))
                draw_shape(-100, 40, self.current_shape.next_shape,0)
                i = "Reserva:"
                j = Text(i)
                text_hold_render = renpy.render(j, width, height, st, at)
                r.blit(text_hold_render, (-120, 100))
                draw_shape(-100, 160, self.current_shape.shape_hold,0)
                if LineLimit != 0:
                    i = "Línea para Victoria - %(s)d " % {"s":LineLimit}
                    j = Text(i)
                    text_line = renpy.render(j, width, height, st, at)
                    r.blit(text_line, (420, -100))
                    PlayerForYuri = self.allLines
                elif TetrisScore != 0:
                    a = "Puntuación - %(s)d " % {"s":self.score }
                    e = Text(a)
                    text_score_render = renpy.render(e, width, height, st, at)
                    r.blit(text_score_render, (30, -100))
                    PlayerForYuri = self.score
            else:
                if LineLimit != 0 and (self.allLines > LineLimit/6 or PlayerForYuri > LineLimit/6):
                    if self.Yuri_Face <> 1 and self.allLines > PlayerForYuri:
                        if persistent.skin == 1:
                            music_swap = True
                            if music_swap:
                                change_music("<loop 1.81>/music/tetris (b).ogg")
                                music_swap = False
                            elif not music_swap:
                                pass
                        show_chr("A-ABDAA-AAAJ")
                        self.Yuri_Face = 1
                        renpy.restart_interaction()
                    elif self.Yuri_Face <> 2 and self.allLines < PlayerForYuri:
                        if persistent.skin == 1:
                            music_swap = True
                            if music_swap:
                                change_music("<loop 1.81>/music/tetris (b).ogg")
                                music_swap = False
                            elif not music_swap:
                                pass
                        show_chr("A-DEBAA-AMAM")
                        self.Yuri_Face = 2
                        renpy.restart_interaction()
                elif TetrisScore != 0 and (self.score > TetrisScore/6 or PlayerForYuri > TetrisScore/6):
                    if self.Yuri_Face <> 1 and self.score > PlayerForYuri:
                        if persistent.skin == 1:
                            music_swap = True
                            if music_swap:
                                change_music("<loop 1.81>/music/tetris (b).ogg")
                                music_swap = False
                            elif not music_swap:
                                pass
                        show_chr("A-ABDAA-AAAJ")
                        self.Yuri_Face = 1
                        renpy.restart_interaction()
                    elif self.Yuri_Face <> 2 and self.score < PlayerForYuri:
                        if persistent.skin == 1:
                            music_swap = True
                            if music_swap:
                                change_music("<loop 1.81>/music/tetris (b).ogg")
                                music_swap = False
                            elif not music_swap:
                                pass
                        show_chr("A-DEBAA-AMAM")
                        self.Yuri_Face = 2
                        renpy.restart_interaction()
                
                r.blit(text_allLines_render, (250, -100))
                r.blit(text_level_render, (250, -50))
                r.blit(text_next_render, (250, -10))
                if TetrisScore != 0:
                    a = "Score - %(s)d " % {"s":self.score }
                    e = Text(a)
                    text_score_render = renpy.render(e, width, height, st, at)
                    r.blit(text_score_render, (30, -100))
                draw_shape(280, 40, self.current_shape.next_shape,0)
            
            draw_shape(0, 0, self.stage,0)
            draw_shape(self.current_shape.x*self.PIXEL_SIZE, self.current_shape.y*self.PIXEL_SIZE, self.current_shape.shape,1)
            
            renpy.redraw(self, 0)
            return r
        
        
        def rotateClockWise(self, mat):
            tempShape = mat
            tempRow = tempShape
            tempX = self.current_shape.x
            tempY = self.current_shape.y
            ifRotation = True
            renpy.sound.play(self.soundrotate)
            lenRow = len(mat)
            lenCol = len(mat[0])
            
            
            if lenRow == 4:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape.y+=1
                if self.stage[self.current_shape.y][self.current_shape.x-1] == 0:
                    self.current_shape.x-=1
                for idc, row in enumerate(tempRow[0]):
                    if self.stage[self.current_shape.y][self.current_shape.x+idc] != 0:
                        ifRotation = False
                        break
            
            elif lenRow == 1:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape.y-=1
                self.current_shape.x+=1
                for idr, row in enumerate(tempRow):
                    if self.stage[self.current_shape.y+idr][self.current_shape.x] != 0:
                        ifRotation = False
                        break
            
            
            
            
            elif lenRow == 2 and lenCol != 2:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape.y+idr][self.current_shape.x+idc] != 0:
                                ifRotation = False
                                break
            
            
            
            elif lenRow == 3:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                if self.stage[self.current_shape.y][self.current_shape.x+len(tempRow[0])-1] != 0:
                    self.current_shape.x-=1
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape.y+idr][self.current_shape.x+idc] != 0:
                                ifRotation = False
                                break
            elif lenRow == 2 and lenCol == 2:
                ifRotation = True
            
            if ifRotation == False:
                tempRow = tempShape
                self.current_shape.x = tempX
                self.current_shape.y = tempY
            return tempRow
        
        
        def find_bottom(self):
            temp_y = 0
            for idr in range(self.current_shape.y+len(self.current_shape.shape)-1, 22):
                for idc, column in enumerate(self.current_shape.shape[0]):
                    if self.stage[idr][self.current_shape.x + idc ] != 0:
                        temp_y = idr-len(self.current_shape.shape)
                        break
                if temp_y != 0:
                    break
            for position in range(0, 4):
                temp_fit = True
                for idr, row in enumerate(self.current_shape.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[temp_y+idr][self.current_shape.x + idc] != 0:
                                temp_fit = False
                                break
                if temp_fit:
                    temp_y += 1
                else:
                    temp_y -= 1
                    break
            return temp_y
        
        def player_t_spin(shape, stage):
            if shape[0][1] != 0 and shape[1][0] != 0 and shape[1][2] != 0 and shape[2][1] != 0:
                return True
            elif shape[0][1] == 0 and shape[1][0] == 0 and shape[1][2] != 0 and shape[2][1] != 0:
                return True
            elif shape[0][1] != 0 and shape[1][0] != 0 and shape[1][2] == 0 and shape[2][1] != 0:
                return True
            elif shape[0][1] != 0 and shape[1][0] != 0 and shape[1][2] != 0 and shape[2][1] == 0:
                return True
            else:
                return False
        
        def event(self, ev, x, y, st):
            import pygame
            temp_can_left = True
            temp_can_right = True
            if self.level > 19:
                self.current_shape.speed = 0.20
            else:
                self.current_shape.speed = 0.20
            if ev.type == pygame.KEYDOWN and self.AI == 0:
                if ev.key == pygame.K_UP:
                    self.current_shape.shape = self.rotateClockWise(self.current_shape.shape)
                elif ev.key == pygame.K_LEFT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape.y + idr][self.current_shape.x - 1 + idc] != 0:
                                    temp_can_left = False
                                    break
                    if temp_can_left:
                        self.current_shape.x -= 1
                elif ev.key == pygame.K_RIGHT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape.y + idr][self.current_shape.x + 1 + idc ] != 0:
                                    temp_can_right = False
                                    break
                    if temp_can_right:
                        self.current_shape.x += 1
                elif ev.key == pygame.K_DOWN:
                    self.current_shape.speed = 0.002
                elif ev.key == pygame.K_SPACE:
                    
                    
                    
                    
                    
                    renpy.sound.play(self.soundbdrop)
                    self.addShapeToStage(self.current_shape.x, self.find_bottom())
                    self.new_shape = True
                elif ev.key == pygame.K_q and self.current_shape.shape_hold == "" and self.was_it_hold ==False:
                    self.current_shape.shape_hold = self.current_shape.shape
                    self.new_shape = True
                elif ev.key == pygame.K_e and self.current_shape.shape_hold != "":
                    self.current_shape.next_shape = self.current_shape.shape
                    self.current_shape.shape = self.current_shape.shape_hold
                    self.current_shape.shape_hold = ""
                    self.current_shape.x = 5
                    self.current_shape.y = 1
                    self.was_it_hold = True
        
        def rotateClockWiseAI(self):
            lenRow = len(self.current_shape.shape)
            lenCol = len(self.current_shape.shape[0])
            tempRow = [[] for _ in range(lenCol)]
            for idr, row in enumerate(self.current_shape.shape):
                for idc, column in enumerate(row):
                    tempRow[idc].insert(0,column)
            del self.current_shape.shape
            self.current_shape.shape = tempRow
        
        def find_t_spin(shape, stage):
            if shape[0][1] == 0 or shape[1][0] == 0 or shape[1][2] == 0 or shape[2][1] == 0:
                
                for x in range(1, 11):
                    
                    if stage[1][x] == 0 and stage[0][x-1] != 0 and stage[1][x-1] != 0 and stage[2][x-1] != 0:
                        return -1
                    
                    if stage[1][x] == 0 and stage[0][x+2] != 0 and stage[1][x+2] != 0 and stage[2][x+2] != 0:
                        return 1
            return 0
        
        def Yuri_AI(self):
            
            t_spin_move = find_t_spin(self.current_shape.shape, self.stage)
            
            if t_spin_move != 0:
                self.current_shape.x += t_spin_move
            
            else:
                moves = bestMove()
                
                for i in range(0, moves[1]-1):
                    self.rotateClockWiseAI()
                
                signbit = 1 if moves[0] < 0 else 0
                if signbit == 0:
                    for i in range(0, moves[0]):
                        self.current_shape.x += 1
                else:
                    for i in range(moves[0], 0):
                        self.current_shape.x -= 1
        
        
        
        def Yuri_AI(self):
            def calculateScoreForMove():
                height = 0
                lines = 0
                holes = 0
                temp_col_height = [None] * 10
                bumpiness = 0
                
                for idr in range(20, 0, -1):
                    temp_clear_line = True
                    for idc in range(1, 11):
                        if self.stage[idr][idc] == 0:
                            temp_clear_line = False
                            break
                    if temp_clear_line:
                        lines += 1
                
                for idc in range(1, 11):
                    temp_col_height[idc-1] = 0
                    temp_holes = 0
                    for idr in range(20, 0, -1):
                        if self.stage[idr][idc] != 0:
                            holes += temp_holes
                            temp_holes = 0
                        else:
                            temp_holes += 1
                        if self.stage[idr][idc] != 0:
                            temp_col_height[idc-1] = 21-idr
                for i in range(0, 9):
                    height += temp_col_height[i]
                    bumpiness += abs(temp_col_height[i] - temp_col_height[i+1])
                height += temp_col_height[9]
                score = (-0.510066 * height) + (0.760666 * lines) - (0.35663 * holes) - (0.184483 * bumpiness)
                return score
            
            def shapeRotation(shape):
                if shape == 6:
                    return 2
                elif shape == 0 or shape == 3 or shape == 4:
                    return 5
                elif shape == 1 or shape == 2 or shape == 5:
                    return 3
            
            
            def bestMove():
                import copy
                moves = []
                best_score = -100
                temp_shape = copy.deepcopy(self.current_shape.shape)
                temp_rotation = shapeRotation(self.current_shape.shape_number)
                
                
                temp_stage = copy.deepcopy(self.stage)
                for rot in range(1, temp_rotation):
                    temp_len = len(self.current_shape.shape[0])-1
                    for idc in range(1, 11-temp_len):
                        del self.stage
                        self.stage = copy.deepcopy(temp_stage)
                        temp_break = False
                        for idr in range(1, 22):
                            for idcShape in range(0, len(self.current_shape.shape[0])):
                                if self.current_shape.shape[len(self.current_shape.shape)-1][idcShape] != 0:
                                    if self.stage[idr][idc+idcShape] != 0:
                                        temp_idr = idr
                                        temp_break = True
                                        break
                            if temp_break:
                                break
                        for idr in range(0, 21):
                            temp_free = True
                            temp_idr -= 1
                            for idrShape, row in enumerate(self.current_shape.shape):
                                for idcShape, column in enumerate(row):
                                    if column != 0:
                                        if self.stage[temp_idr+(idrShape-(len(self.current_shape.shape)-1))][idc+idcShape] != 0:
                                            temp_free = False
                            if temp_free:
                                self.addShapeToStage(idc, temp_idr-(len(self.current_shape.shape)-1))
                                temp_score = calculateScoreForMove()
                                if temp_score > best_score:
                                    best_score = temp_score
                                    moves = [idc-5, rot]
                                break
                    self.rotateClockWiseAI()
                self.stage = copy.deepcopy(temp_stage)
                del temp_stage
                self.current_shape.shape = copy.deepcopy(temp_shape)
                del temp_shape
                
                temp_moves = []
                for i in range(0, moves[1]-1):
                    temp_moves.append("r")
                signbit = 1 if moves[0] < 0 else 0
                if signbit == 0:
                    for i in range(0, moves[0]):
                        temp_moves.append("1")
                else:
                    for i in range(moves[0], 0):
                        temp_moves.append("-1")
                return temp_moves
            return bestMove()



    class Co_OP_tetris(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.movesAI = []
            self.PIXEL_SIZE = 20
            self.piece_list_player = [0,1,2,3,4,5,6]
            self.piece_list_Yuri = [0,1,2,3,4,5,6]
            random.shuffle(self.piece_list_player)
            random.shuffle(self.piece_list_Yuri)
            self.tetris_shapes = [
                [[1, 1, 1],
                [0, 1, 0]],

                [[0, 2, 2],
                [2, 2, 0]],

                [[3, 3, 0],
                [0, 3, 3]],

                [[4, 0, 0],
                [4, 4, 4]],

                [[0, 0, 5],
                [5, 5, 5]],

                [[6, 6, 6, 6]],

                [[7, 7],
                [7, 7]]
            ]
            
            self.stage = [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]]
            
            if persistent.skin == 1:
                
                self.color_1 = Image("images/tetris/tetris/cube_1.png")
                self.color_2 = Image("images/tetris/tetris/cube_2.png")
                self.color_3 = Image("images/tetris/tetris/cube_3.png")
                self.color_4 = Image("images/tetris/tetris/cube_4.png")
                self.color_5 = Image("images/tetris/tetris/cube_5.png")
                self.color_6 = Image("images/tetris/tetris/cube_6.png")
                self.color_7 = Image("images/tetris/tetris/cube_7.png")
                self.color_9 = Image("images/tetris/tetris/cube_8.png")
                
                self.shadow_color_1 = Image("images/tetris/tetris/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris/cube_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound4line = "sfx/t-4fl.ogg"
            
            
            elif persistent.skin == 2:
                
                self.color_1 = Image("images/tetris/tetris_99/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_99/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_99/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_99/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_99/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_99/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_99/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_99/cube_8.png")
                
                self.shadow_color_1 = Image("images/tetris/tetris_99/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_99/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_99/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_99/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_99/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_99/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_99/cube_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(99).ogg"
                self.soundline = "sfx/t-fl(99).ogg"
                self.soundldrop = "sfx/t-fl-drop(99).ogg"
                self.soundmove = "sfx/t-move(99).ogg"
                self.soundrotate = "sfx/t-rotate(99).ogg"
                self.sound2line = "sfx/t-2fl(99).ogg"
                self.sound3line = "sfx/t-3fl(99).ogg"
                self.sound4line = "sfx/t-4fl(99).ogg"
            
            
            elif persistent.skin == 3:
                
                self.color_1 = Image("images/tetris/tetris_gb/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_gb/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_gb/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_gb/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_gb/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_gb/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_gb/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_gb/cube_8.png")
                
                self.shadow_color_1 = Image("images/tetris/tetris_gb/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_gb/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_gb/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_gb/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_gb/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_gb/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_gb/cube_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound4line = "sfx/t-4fl.ogg"
            
            
            elif persistent.skin == 4:
                
                
                self.color_1 = Image("images/tetris/tetris_gmd/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_gmd/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_gmd/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_gmd/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_gmd/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_gmd/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_gmd/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_gmd/cube_8.png")
                
                self.shadow_color_1 = Image("images/tetris/tetris_gmd/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_gmd/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_gmd/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_gmd/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_gmd/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_gmd/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_gmd/cube_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(g).ogg"
                self.soundline = "sfx/t-fl(g).ogg"
                self.soundldrop = "sfx/t-fl-drop(g).ogg"
                self.soundmove = "sfx/t-move(g).ogg"
                self.soundrotate = "sfx/t-rotate(g).ogg"
                self.sound4line = "sfx/t-4fl(g).ogg"
            
            elif persistent.skin == 5:
                
                
                self.color_1 = Image("images/tetris/tetris_mb/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_mb/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_mb/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_mb/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_mb/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_mb/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_mb/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_mb/cube_8.png")
                
                self.shadow_color_1 = Image("images/tetris/tetris_mb/shadow_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_mb/shadow_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_mb/shadow_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_mb/shadow_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_mb/shadow_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_mb/shadow_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_mb/shadow_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(mb).ogg"
                self.soundline = "sfx/t-fl(mb).ogg"
                self.soundldrop = "sfx/t-fl-drop(mb).ogg"
                self.soundmove = "sfx/t-move(mb).ogg"
                self.soundrotate = "sfx/t-rotate(mb).ogg"
                self.sound2line = "sfx/t-2fl(mb).ogg"
                self.sound3line = "sfx/t-3fl(mb).ogg"
                self.sound4line = "sfx/t-4fl(mb).ogg"
            
            elif persistent.skin == 6:
                
                
                self.color_1 = Image("/custom_tetris/cube_1.png")
                self.color_2 = Image("/custom_tetris/cube_2.png")
                self.color_3 = Image("/custom_tetris/cube_3.png")
                self.color_4 = Image("/custom_tetris/cube_4.png")
                self.color_5 = Image("/custom_tetris/cube_5.png")
                self.color_6 = Image("/custom_tetris/cube_6.png")
                self.color_7 = Image("/custom_tetris/cube_7.png")
                self.color_9 = Image("/custom_tetris/cube_8.png")
                
                self.shadow_color_1 = Image("/custom_tetris/shadow_1.png")
                self.shadow_color_2 = Image("/custom_tetris/shadow_2.png")
                self.shadow_color_3 = Image("/custom_tetris/shadow_3.png")
                self.shadow_color_4 = Image("/custom_tetris/shadow_4.png")
                self.shadow_color_5 = Image("/custom_tetris/shadow_5.png")
                self.shadow_color_6 = Image("/custom_tetris/shadow_6.png")
                self.shadow_color_7 = Image("/custom_tetris/shadow_7.png")
                
                self.score = 0
                
                self.playsounds = True
                self.soundbdrop = "/custom_tetris/t-drop.ogg"
                self.soundline = "/custom_tetris/t-fl.ogg"
                self.soundldrop = "/custom_tetris/t-fl-drop.ogg"
                self.soundmove = "/custom_tetris/t-move.ogg"
                self.soundrotate = "/custom_tetris/t-rotate.ogg"
                self.sound2line = "/custom_tetris/t-2fl.ogg"
                self.sound3line = "/custom_tetris/t-3fl.ogg"
                self.sound4line = "/custom_tetris/t-4fl.ogg"
            
            
            class current_shape_player:
                shape = ""
                shape_number = ""
                new_shape_number = self.piece_list_player[0]
                next_shape = self.tetris_shapes[new_shape_number]
                x = 5
                y = 1
                move_time = 0.300
                speed = 0.20
            
            class current_shape_Yuri:
                shape = ""
                shape_number = ""
                new_shape_number = self.piece_list_Yuri[0]
                next_shape = self.tetris_shapes[new_shape_number]
                x = 5
                y = 1
                move_time = 0.300
                speed = 0.20
            
            self.temp_position = 3
            self.current_shape_player = current_shape_player()
            self.current_shape_Yuri = current_shape_Yuri ()
            self.level = 1
            self.allLines = 0
            self.oldst = None
            self.new_shape_player = True
            self.new_shape_Yuri = True
            self.game_over = False
            self.winner = None
        
        
        
        def addShapeToStage(self, current_shape, current_x, current_y):
            for idr, row in enumerate(current_shape.shape):
                for idc, column in enumerate(row):
                    if column != 0:
                        self.stage[current_y+idr][current_x+idc]=column
        
        def render(self, width, height, st, at):
            
            global TetrisWinner
            
            for idc in range(4, 16):
                if self.stage[1][idc] != 0:
                    self.game_over = True
            
            if self.game_over:
                if self.score > persistent.best_co_op_tetris_score:
                    persistent.best_co_op_tetris_score = self.score
                    TetrisWinner = 2
                else:
                    TetrisWinner = 3
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            renpy.jump("tetris_over")
            
            
            
            def lines():
                numberOfFullLines = 0
                
                prevLine = False
                for idr in range(1, 21):
                    fullLine = True
                    for idc in range(1, 21):
                        if self.stage[idr][idc] == 0:
                            fullLine = False
                            break
                    if fullLine:
                        numberOfFullLines += 1
                        renpy.sound.play(self.soundline)
                        for idc in range(1, 21):
                            self.stage[idr][idc] = 0
                        if prevLine != fullLine:
                            for i in range(0, idr-1):
                                for idc in range(1, 21):
                                    self.stage[idr-i][idc] = self.stage[idr-i-1][idc]
                                    self.stage[idr-i-1][idc] = 0
                                    fullLine = False
                    prevLine = fullLine
                
                
                self.allLines += numberOfFullLines
                if numberOfFullLines == 1:
                    self.score += 100 * self.level
                elif numberOfFullLines == 2:
                    self.score += 300 * self.level
                elif numberOfFullLines == 3:
                    self.score += 500 * self.level
                elif numberOfFullLines == 4:
                    self.score += 800 * self.level
                    renpy.sound.play(self.sound4line)
                self.level =  int(self.allLines/10)+1
            
            r = renpy.Render(width, height)
            
            if persistent.skin == 1:
                background = renpy.render(Image("images/tetris/tetris/background_co_op.png"), width, height, st, at)
            
            elif persistent.skin == 2:
                background = renpy.render(Image("images/tetris/tetris_99/background_co_op.png"), width, height, st, at)
            
            elif persistent.skin == 3:
                background = renpy.render(Image("images/tetris/tetris_gb/background_co_op.png"), width, height, st, at)
            
            elif persistent.skin == 4:
                background = renpy.render(Image("images/tetris/tetris_gmd/background_co_op.png"), width, height, st, at)
            
            elif persistent.skin == 5:
                background = renpy.render(Image("images/tetris/tetris_mb/background_co_op.png"), width, height, st, at)
            
            elif persistent.skin == 6:
                background = renpy.render(Image("/custom_tetris/background_co_op.png"), width, height, st, at)
            
            r.blit(background, (0, 0))
            lines()
            
            
            if self.new_shape_player:
                self.current_shape_player.x = 5
                self.current_shape_player.y = 1
                self.current_shape_player.shape = self.current_shape_player.next_shape
                self.current_shape_player.shape_number = self.current_shape_player.new_shape_number
                self.piece_list_player.pop(0)
                if not self.piece_list_player:
                    self.piece_list_player = [0,1,2,3,4,5,6]
                    random.shuffle(self.piece_list_player)
                self.current_shape_player.new_shape_number = self.piece_list_player[0]
                self.current_shape_player.next_shape = self.tetris_shapes[self.current_shape_player.new_shape_number]
                self.new_shape_player = False
            
            
            if self.new_shape_Yuri:
                self.current_shape_Yuri.x = 15
                self.current_shape_Yuri.y = 1
                self.current_shape_Yuri.shape = self.current_shape_Yuri.next_shape
                self.current_shape_Yuri.shape_number = self.current_shape_Yuri.new_shape_number
                self.piece_list_Yuri.pop(0)
                if not self.piece_list_Yuri:
                    self.piece_list_Yuri = [0,1,2,3,4,5,6]
                    random.shuffle(self.piece_list_Yuri)
                self.current_shape_Yuri.new_shape_number = self.piece_list_Yuri[0]
                self.current_shape_Yuri.next_shape = self.tetris_shapes[self.current_shape_Yuri.new_shape_number]
                self.new_shape_Yuri = False
                self.temp_position = 1
                temp_AI = True
                for idc in range(1, 21):
                    if self.stage[2][idc] != 0:
                        temp_AI = False
                if temp_AI:
                    self.movesAI = self.Yuri_AI()
            
            if self.oldst is None:
                self.oldst = st
            
            if self.current_shape_Yuri.y >= 4:
                self.current_shape_Yuri.speed = 0.4 - 0.03 * (self.level - 1)
            
            if self.temp_position == self.current_shape_Yuri.y:
                for i in range(0, 3):
                    if len(self.movesAI) != 0:
                        if self.movesAI[0] == "r":
                            self.rotateClockWiseAI()
                        else:
                            self.current_shape_Yuri.x += int(self.movesAI[0])
                        del self.movesAI[0]
                self.temp_position += 1
            
            dtime = st - self.oldst
            self.oldst = st
            temp_can_go_down = True
            
            
            if self.current_shape_player.move_time <= 0:
                
                for idr, row in enumerate(self.current_shape_player.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_player.y + 1 + idr][self.current_shape_player.x + idc] != 0:
                                temp_can_go_down = False
                                renpy.sound.play(self.soundbdrop)
                                break
                if temp_can_go_down != False:
                    self.current_shape_player.move_time = self.current_shape_player.speed
                    self.current_shape_player.y += 1
                else:
                    self.new_shape_player = True
                    self.addShapeToStage(self.current_shape_player, self.current_shape_player.x, self.current_shape_player.y)
            else:
                self.current_shape_player.move_time -= dtime
            
            
            if self.current_shape_Yuri.move_time <= 0:
                
                for idr, row in enumerate(self.current_shape_Yuri.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_Yuri.y + 1 + idr][self.current_shape_Yuri.x + idc] != 0:
                                temp_can_go_down = False
                                renpy.sound.play(self.soundbdrop)
                                break
                if temp_can_go_down != False:
                    self.current_shape_Yuri.move_time = self.current_shape_Yuri.speed
                    self.current_shape_Yuri.y += 1
                else:
                    self.new_shape_Yuri = True
                    self.addShapeToStage(self.current_shape_Yuri, self.current_shape_Yuri.x, self.current_shape_Yuri.y)
            else:
                self.current_shape_Yuri.move_time -= dtime
            
            def draw_shape(sx, sy, current_shape,shadow):
                for idr, row in enumerate(current_shape):
                    for idc, column in enumerate(row):
                        if column == 1:
                            shape = renpy.render(self.color_1, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_1, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 2:
                            shape = renpy.render(self.color_2, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_2, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 3:
                            shape = renpy.render(self.color_3, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_3, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 4:
                            shape = renpy.render(self.color_4, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_4, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 5:
                            shape = renpy.render(self.color_5, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_5, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 6:
                            shape = renpy.render(self.color_6, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_6, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 7:
                            shape = renpy.render(self.color_7, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_7, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 7:
                            shape = renpy.render(self.color_7, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_7, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 9:
                            shape = renpy.render(self.color_9, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
            
            a = "Puntuación - %(s)d " % {"s":self.score }
            b = "Líneas - %(s)d " % {"s":self.allLines }
            c = "Nivel - %(s)d " % {"s":self.level}
            d = "Siguiente jugador:"
            i = "Mejor Puntuación - %(s)d " % {"s":persistent.best_co_op_tetris_score }
            k = "Siguiente Yuri:"
            
            e = Text(a)
            f = Text(b)
            g = Text(c)
            h = Text(d)
            j = Text(i)
            l = Text(k)
            
            text_allLines_render = renpy.render(f, width, height, st, at)
            text_level_render = renpy.render(g, width, height, st, at)
            text_next_player_render = renpy.render(h, width, height, st, at)
            text_next_Yuri_render = renpy.render(l, width, height, st, at)
            
            text_score_render = renpy.render(e, width, height, st, at)
            r.blit(text_score_render, (5, -50))
            
            text_score_render = renpy.render(j, width, height, st, at)
            r.blit(text_score_render, (5, -100))
            r.blit(text_allLines_render, (250, -100))
            r.blit(text_level_render, (250, -50))
            
            r.blit(text_next_player_render, (5, 450))
            draw_shape(25, 500, self.current_shape_player.next_shape,0)
            
            r.blit(text_next_Yuri_render, (250, 450))
            draw_shape(275, 500, self.current_shape_Yuri.next_shape,0)
            
            draw_shape(0, 0, self.stage,0)
            draw_shape(self.current_shape_player.x*self.PIXEL_SIZE, self.current_shape_player.y*self.PIXEL_SIZE, self.current_shape_player.shape,1)
            draw_shape(self.current_shape_Yuri.x*self.PIXEL_SIZE, self.current_shape_Yuri.y*self.PIXEL_SIZE, self.current_shape_Yuri.shape,0)
            
            renpy.redraw(self, 0)
            return r
        
        
        def rotateClockWise(self, mat):
            tempShape = mat
            tempRow = tempShape
            tempX = self.current_shape_player.x
            tempY = self.current_shape_player.y
            ifRotation = True
            renpy.sound.play(self.soundrotate)
            lenRow = len(mat)
            lenCol = len(mat[0])
            
            
            if lenRow == 4:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape_player.y+=1
                if self.stage[self.current_shape_player.y][self.current_shape_player.x-1] == 0:
                    self.current_shape_player.x-=1
                for idc, row in enumerate(tempRow[0]):
                    if self.stage[self.current_shape_player.y][self.current_shape_player.x+idc] != 0:
                        ifRotation = False
                        break
            
            elif lenRow == 1:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape_player.y-=1
                self.current_shape_player.x+=1
                for idr, row in enumerate(tempRow):
                    if self.stage[self.current_shape_player.y+idr][self.current_shape_player.x] != 0:
                        ifRotation = False
                        break
            
            
            
            
            elif lenRow == 2 and lenCol != 2:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_player.y+idr][self.current_shape_player.x+idc] != 0:
                                ifRotation = False
                                break
            
            
            
            elif lenRow == 3:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                if self.stage[self.current_shape_player.y][self.current_shape_player.x+len(tempRow[0])-1] != 0:
                    self.current_shape_player.x-=1
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_player.y+idr][self.current_shape_player.x+idc] != 0:
                                ifRotation = False
                                break
            elif lenRow == 2 and lenCol == 2:
                ifRotation = True
            
            if ifRotation == False:
                tempRow = tempShape
                self.current_shape_player.x = tempX
                self.current_shape_player.y = tempY
            return tempRow
        
        def find_bottom(self):
            temp_y = 0
            for idr in range(self.current_shape_player.y, 22):
                for idc, column in enumerate(self.current_shape_player.shape[0]):
                    if self.stage[idr][self.current_shape_player.x + idc ] != 0:
                        temp_y = idr-len(self.current_shape_player.shape)
                        break
                if temp_y != 0:
                    break
            for position in range(0, 4):
                temp_fit = True
                for idr, row in enumerate(self.current_shape_player.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[temp_y+idr][self.current_shape_player.x + idc] != 0:
                                temp_fit = False
                                break
                if temp_fit:
                    temp_y += 1
                else:
                    temp_y -= 1
                    break
            return temp_y
        
        def event(self, ev, x, y, st):
            import pygame
            temp_can_left = True
            temp_can_right = True
            if self.level > 19:
                self.current_shape.speed = 0.20
            else:
                self.current_shape_player.speed = 0.20
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    self.current_shape_player.shape = self.rotateClockWise(self.current_shape_player.shape)
                elif ev.key == pygame.K_LEFT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape_player.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape_player.y + idr][self.current_shape_player.x - 1 + idc] != 0:
                                    temp_can_left = False
                                    break
                    if temp_can_left:
                        self.current_shape_player.x -= 1
                elif ev.key == pygame.K_RIGHT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape_player.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape_player.y + idr][self.current_shape_player.x + 1 + idc ] != 0:
                                    temp_can_right = False
                                    break
                    if temp_can_right:
                        self.current_shape_player.x += 1
                elif ev.key == pygame.K_DOWN:
                    self.current_shape_player.speed = 0.002
                elif ev.key == pygame.K_SPACE:
                    renpy.sound.play(self.soundbdrop)
                    self.addShapeToStage(self.current_shape_player, self.current_shape_player.x, self.find_bottom())
                    self.new_shape_player = True
        
        def rotateClockWiseAI(self):
            lenRow = len(self.current_shape_Yuri.shape)
            lenCol = len(self.current_shape_Yuri.shape[0])
            tempRow = [[] for _ in range(lenCol)]
            for idr, row in enumerate(self.current_shape_Yuri.shape):
                for idc, column in enumerate(row):
                    tempRow[idc].insert(0,column)
            del self.current_shape_Yuri.shape
            self.current_shape_Yuri.shape = tempRow
        
        
        
        def Yuri_AI(self):
            def calculateScoreForMove():
                height = 0
                lines = 0
                holes = 0
                temp_col_height = [None] * 20
                bumpiness = 0
                
                for idr in range(20, 0, -1):
                    temp_clear_line = True
                    for idc in range(1, 21):
                        if self.stage[idr][idc] == 0:
                            temp_clear_line = False
                            break
                    if temp_clear_line:
                        lines += 1
                
                for idc in range(1, 21):
                    temp_col_height[idc-1] = 0
                    temp_holes = 0
                    for idr in range(20, 0, -1):
                        if self.stage[idr][idc] != 0:
                            holes += temp_holes
                            temp_holes = 0
                        else:
                            temp_holes += 1
                        if self.stage[idr][idc] != 0:
                            temp_col_height[idc-1] = 21-idr
                for i in range(0, 19):
                    height += temp_col_height[i]
                    bumpiness += abs(temp_col_height[i] - temp_col_height[i+1])
                height += temp_col_height[19]
                score = (-0.510066 * height) + (0.760666 * lines) - (0.35663 * holes) - (0.184483 * bumpiness)
                return score
            
            def shapeRotation(shape):
                if shape == 6:
                    return 2
                elif shape == 0 or shape == 3 or shape == 4:
                    return 5
                elif shape == 1 or shape == 2 or shape == 5:
                    return 3
            
            
            def bestMove():
                import copy
                moves = [0,1]
                best_score = -100
                temp_shape = copy.deepcopy(self.current_shape_Yuri.shape)
                temp_rotation = shapeRotation(self.current_shape_Yuri.shape_number)
                
                
                temp_stage = copy.deepcopy(self.stage)
                for rot in range(1, temp_rotation):
                    temp_len = len(self.current_shape_Yuri.shape[0])-1
                    for idc in range(1, 21-temp_len):
                        del self.stage
                        self.stage = copy.deepcopy(temp_stage)
                        temp_break = False
                        for idr in range(1, 22):
                            for idcShape in range(0, len(self.current_shape_Yuri.shape[0])):
                                if self.current_shape_Yuri.shape[len(self.current_shape_Yuri.shape)-1][idcShape] != 0:
                                    if self.stage[idr][idc+idcShape] != 0:
                                        temp_idr = idr
                                        temp_break = True
                                        break
                            if temp_break:
                                break
                        for idr in range(0, 21):
                            temp_free = True
                            temp_idr -= 1
                            for idrShape, row in enumerate(self.current_shape_Yuri.shape):
                                for idcShape, column in enumerate(row):
                                    if column != 0:
                                        if self.stage[temp_idr+(idrShape-(len(self.current_shape_Yuri.shape)-1))][idc+idcShape] != 0:
                                            temp_free = False
                            if temp_free:
                                self.addShapeToStage(self.current_shape_Yuri, idc, temp_idr-(len(self.current_shape_Yuri.shape)-1))
                                temp_score = calculateScoreForMove()
                                if temp_score > best_score:
                                    best_score = temp_score
                                    moves = [idc-15, rot]
                                break
                    self.rotateClockWiseAI()
                self.stage = copy.deepcopy(temp_stage)
                del temp_stage
                self.current_shape_Yuri.shape = copy.deepcopy(temp_shape)
                del temp_shape
                
                temp_moves = []
                for i in range(0, moves[1]-1):
                    temp_moves.append("r")
                signbit = 1 if moves[0] < 0 else 0
                if signbit == 0:
                    for i in range(0, moves[0]):
                        temp_moves.append("1")
                else:
                    for i in range(moves[0], 0):
                        temp_moves.append("-1")
                return temp_moves
            
            
            temp_can_go_down = True
            for idr, row in enumerate(self.current_shape_Yuri.shape):
                for idc, column in enumerate(row):
                    if column != 0:
                        if self.stage[self.current_shape_Yuri.y + 1 + idr][self.current_shape_Yuri.x + idc] != 0:
                            temp_can_go_down = False
                            break
            
            
            if temp_can_go_down == False:
                self.addShapeToStage(self.current_shape_Yuri, self.current_shape_Yuri.x, self.current_shape_Yuri.y)
                self.new_shape_Yuri = True
            else:
                
                return bestMove()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
