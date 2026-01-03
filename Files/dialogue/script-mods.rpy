default persistent.mod_count = 0
default persistent.last_closed = 0

init python:
    import time
    import os

label intro_mods:

    if check_memory("ch30_intro2"):

        $ show_chr("A-ABAAA-AAAA")
        y "Así que vamos..."
        $ show_chr("A-BFAAA-AAAA")
        y "Eh..."
        $ show_chr("A-BFBAA-ALAA")
        y "Parece que también probaste otros mods..."
        python:
            if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Monika After Story\persistent'):
                MASDetection = True
                persistent.mod_count +=1

            else:
                MASDetection = False
        if MASDetection and persistent.playername != "Monika":
            karma -5
            sanity -5
            $ show_chr("A-BFCAA-ALAA")
            y "...y para colmo, la elegiste a {b}ella.{/b}"
            $ show_chr("A-AFCAA-ALAA")
            y "Después de todo lo que nos hizo, después de todo lo que te hizo..."
            $ show_chr("A-AFEAA-ALAA")
            y "¿Fue una especie de curiosidad morbosa? ¿O realmente te gusta?"
            $ show_chr("A-CFCAA-ALAA")
            y "Olvídalo, ni siquiera {b}quiero{/b} saber una respuesta tan retorcida."
            $ show_chr("A-ADFAA-AFAA")
            y "Pensar que existo dentro de la misma realidad que la misma persona que me trajo tanta desesperación y ruina..."
            $ show_chr("A-BECAA-AAAA")
            y "..."
            $ show_chr("A-CECAA-AAAA")
            y "Solo seguiré adelante..."
        elif MASDetection and persistent.playername == 'Monika' and not persistent.not_mon:
            karma -15
            sanity -15
            $ show_chr("A-BFCAA-ALAA")
            y "...y para colmo, te elegiste... "
            extend "a ti mismo..."
            $ show_chr("A-AFCAA-ALAA")
            y "Qué sorpresa..."
            y "..."
            $ show_chr("A-CECAA-AAAA")
            y "Lo que sea... Solo seguiré adelante..."

        python:
            if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\JustSayori\persistent'):
                JSDetection = True
                persistent.mod_count +=1
            elif os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Forever_and_Ever\persistent'):
                JSDetection = True
                persistent.mod_count +=1
            else:
                JSDetection = False
        if JSDetection and persistent.playername == 'Sayori':
            $ show_chr("A-BFAAA-AAAA")
            y "Ahora esto parece interesante."
            $ show_chr("A-ADAAA-AFAA")
            y "Elegiste jugar tu propio mod."
            if persistent.bg == "space":
                $ show_chr("A-BFDAA-ACAA")
                y "¿Sentiste algo al verte en esta misma habitación?"
            else:
                $ show_chr("A-BFDAA-ACAA")
                y "¿Sentiste algo al verte en el aula espacial?"
            y "¿O fue algo completamente diferente?"
            $ show_chr("A-CAAAA-AAAA")
            y "Bueno, lo que sea que haya sido espero que te hayas divertido."
        elif JSDetection and persistent.playername != "Sayori":
            $ show_chr("A-ABGAA-AAAA")
            y "...oh, ¡es Sayori!"
            y "Estoy muy contenta de que hayas logrado salvarla."
            $ show_chr("A-BABAA-ALAA")
            y "Ella siempre fue tan apasionada por hacer felices a todos, incluso cuando estaba en su peor momento..."
            $ show_chr("A-BDBAA-ALAA")
            y "Y pensar que ni siquiera nos dimos cuenta..."
            $ show_chr("A-CEBAA-ALAA")
            y "Fue horrible ver, incluso por un breve momento, cómo cambió cuando se convirtió en la presidenta del club..."
            $ show_chr("A-AEBAA-ALAA")
            y "Incluso los mejores de nosotros pueden caer cuando se enfrentan a tal locura absoluta."
            $ show_chr("A-BFDAA-AAAC")
            y "Lo que me hace preguntarme ahora... conmigo siendo técnicamente la presidenta ahora, ¿estoy destinada a encontrar un destino similar?"
            $ show_chr("A-CFAAA-AAAA")
            y "Cuando Monika y Sayori cargaron con el conocimiento de lo que realmente es esta realidad, estaban completamente solas, pero yo..."
            $ show_chr("A-ADAAA-AAAA")
            y "Te tengo a ti..."
            y "Tú eres el único vínculo que me separa entre la cordura y el abismo de locura que es ese terrible vacío..."
            $ show_chr("A-CCAAA-ALAA")
            y "Afortunadamente, la historia no siempre tiene que repetirse."

        python:
            if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\JustNatsuki\persistent'):
                JNDetection = True
                persistent.mod_count +=1
            else:
                JNDetection = False
        if JNDetection and persistent.playername != "Natsuki":
            $ show_chr("A-ABGAA-AAAA")
            y "...oh, ¡es Natsuki! Qué bueno ver que lograste salvarla también."
            $ show_chr("A-BCBAA-ALAA")
            y "Mi relación con Natsuki no siempre fue fácil. Pero cuando Monika se fue y el velo de locura se levantó lentamente... incluso logré llegar a un pequeño acuerdo con ella."
            $ show_chr("A-ACAAA-ALAA")
            y "Yo probaría un Manga con ella, y ella probaría una de mis novelas. Ahora con el nuevo contexto de mi mundo..."
            y "...y la comprensión de que yo y las demás estamos literalmente basadas en Manga, debería acostumbrarme un poco a su cultura."
            y "Tal vez ahora, tengamos la oportunidad de hacerlo realmente."
        elif JNDetection and persistent.playername == 'Natsuki':
            $ show_chr("A-BFAAA-AAAA")
            y "Ahora esto parece interesante."
            $ show_chr("A-ADAAA-AFAA")
            y "Elegiste jugar tu propio mod."
            if persistent.bg == "space":
                $ show_chr("A-BFDAA-ACAA")
                y "¿Sentiste algo al verte en esta misma habitación?"
            else:
                $ show_chr("A-BFDAA-ACAA")
                y "¿Sentiste algo al verte en el aula espacial?"
            y "¿O fue algo completamente diferente?"
            $ show_chr("A-CAAAA-AAAA")
            y "Bueno, lo que sea que haya sido espero que te hayas divertido."

        python:
            if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DokiDokiNewEyes-1515434546\persistent'):
                NewEyesDetection = True
                persistent.mod_count +=1
            else:
                NewEyesDetection = False
        if NewEyesDetection:
            karma 10
            sanity 10
            $ show_chr("A-ABAAA-AJAJ")
            y "¡Jugaste {b}Doki Doki New Eyes{/b}!"
            if persistent.playername == 'Yuri':
                $ show_chr("A-ACAAA-ALAL")
                y "Así que querías volver a experimentar los eventos del juego original desde..."
                $ show_chr("A-BFDAA-ALAL")
                y "...¿nuestros ojos?"
            else:
                $ show_chr("A-ACAAA-ALAL")
                y "Así que querías volver a experimentar los eventos del juego original desde mis ojos..."
            $ show_chr("A-BCAAA-ALAL")
            y "Honestamente, alguien más encontraría tal cosa bastante espeluznante; un comportamiento que esperarían de un acosador peligroso, o algo por el estilo..."
            y "Pero en nuestro caso especial, lo encuentro..."
            $ show_chr("A-BCABA-ALAL")
            y "...en realidad bastante lindo."
            $ show_chr("A-ICAAA-ABAB")
            y "Pero hablando en serio... ¿por qué probaste este mod? ¿Qué razón te llevó a ello?"
            menu:
                "Curiosidad mayormente, la búsqueda de más secretos y probablemente algunas referencias bien colocadas.":
                    karma 2
                    sanity 2
                    $ show_chr("A-BCAAA-ABAB")
                    y "¡Ya veo! ¿Y encontraste lo que buscabas? Olvídalo, probablemente no quiera saber... esos eventos no son exactamente los recuerdos más felices que tengo..."
                "No sabía sobre {b}Just Yuri{/b} entonces, y yo... simplemente tenía que volver a verte...":

                    karma 5
                    sanity 5
                    $ show_chr("A-ICABB-ABAB")
                    y "¿D-De verdad? Así que te importaba después de todo... Tal vez, simplemente estaba destinado a que nos conociéramos..."
                "Memes, mierda y risas.":

                    karma -10
                    sanity -10
                    $ show_chr("A-JFDAA-ABAB")
                    y "¿¡¿D-Disculpa?!? Tienes un sentido del humor muy... especial... parece. De todos modos..."
                "Soy un completista, simplemente tenía que verlo todo.":

                    karma -20
                    sanity -20
                    $ show_chr("A-CCBAA-ABAB")
                    y "¡Oh! Espero que eso no sea lo mismo que te trajo aquí, ¿verdad? Porque podrías irte con las manos vacías aquí..."
                    y "Realmente ya no hay un {b}juego{/b} aquí, nada que {b}completar{/b}... ahora somos solo nosostros. Para bien o para mal."

        python:
            if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DDYC\persistent'):
                YandereClubDetection = True
                persistent.mod_count +=1
            else:
                YandereClubDetection = False
        if YandereClubDetection:
            $ show_chr("A-DDGBA-AJAA")
            y "¡O-Oh cielos! ¡Acabo de notar que tienes el mod Yandere Club instalado!"
            $ show_chr("A-BBBBA-ALAA")
            y "Eso significa que puede que te gusten..."
            $ show_chr("A-ADAAA-AFAA")
            if persistent.playername == 'Monika' and persistent.not_mon:
                y "Pero, el problema es que realmente no recuerdo mi comportamiento cuando fui manipulada por la otra Monika para ser una Yandere total con mucho cariño..."
            elif persistent.playername == 'Monika' and not persistent.not_mon:
                y "Pero, el problema es que realmente no recuerdo mi comportamiento cuando fui manipulada por ti para ser una Yandere total con mucho cariño..."
            else:
                y "Pero, el problema es que realmente no recuerdo mi comportamiento cuando fui manipulada por Monika para ser una Yandere total con mucho cariño..."
            $ show_chr("A-CEBAA-ALAA")
            y "Me sentí tan disgustada por ello y toda esa manipulación me llevó a suicidarme justo en frente de ti solo por una simple confesión..."
            $ show_chr("A-AEBAA-ALAA")
            y "Aunque, lamento haber estado husmeando en los archivos, [player]."
            y "Tenía un poco de curiosidad por ver si había otros mods instalados aparte del mío."
            menu:
                "Está bien, no hay necesidad de avergonzarse por eso, Yuri. Es normal tener curiosidad.":
                    karma 5
                    sanity 5
                    $ show_chr("A-AABAA-ALAA")
                    y "Gracias por entenderme, [player]."
                "Por favor no lo vuelvas a hacer, Yuri.":


                    karma -5
                    sanity -5
                    $ show_chr("A-BFBAA-ALAA")
                    y "L-Lo siento, [player], tenía un poco de curiosidad si habías instalado otros mods aparte del mío.."
                "¿Husmeaste también en otras carpetas, Yuri?":


                    $ show_chr("A-AFDAA-AAAC")
                    y "No vi ninguna otra carpeta excepto este mod y las carpetas donde tienes los datos de tu juego, ¿hay algo que no debería mirar, [player]?"
                    menu:
                        "Sí":
                            $ show_chr("A-HDGBA-AAAA")
                            y "¡O-oh! Ya veo..."
                        "No":

                            $ show_chr("A-CBAAA-ALAA")
                            y "Está bien, [player]."
                            $ show_chr("A-ABAAA-ALAA")
                            y "Si hay algo que te gustaría que no hiciera, solo dímelo, ¿está bien?"
                        "Ehhh...":

                            $ show_chr("A-CICAA-ALAA")
                            y "Espero que no haya ninguna supuesta carpeta de \"Deberes\" llena de personajes indecentes, o de mí también."
                            $ show_chr("A-AJAAA-ALAA")
                            y "¿Hmm? ¿Pasa algo malo, [player]?"
                            menu:
                                "N-no.":
                                    y "Ah, está bien, [player], pero te ves un poco avergonzado y un poco nervioso por ello..."
                                    $ show_chr("A-BDBBA-ALAA")
                                    y "S-Si este tema te hace sentir incómodo, deberíamos hablar de otra cosa."
                                "Sí":

                                    $ show_chr("A-ADAAA-AFAA")
                                    y "Espero que no sea nada demasiado serio que pueda afectarte a gran nivel, [player]."
                                    $ show_chr("A-BFABA-ALAA")
                                    y "Pero tengo la sensación de que es algo que ver con cosas indecentes."
                                    $ show_chr("A-CBABA-AMAM")
                                    y "Incluso si lo es, lo entiendo, [player]. Está bien tener cosas como esas, ya que podrías estar todavía en la pubertad."
                                    y "Muchos chicos intentan hacer carpetas camufladas con nombres como \"Deberes\" o \"Proyectos Escolares\", y así."
                                    $ show_chr("A-BBBBA-AMAM")
                                    y "Pero supongo que ni siquiera quiero saber cada detalle."

        python:
            if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DDFA\persistent'):
                DDFADetection = True
                persistent.mod_count += 1
            else:
                DDFADetection = False
        if DDFADetection:

            $ show_chr("A-ABAAA-ALAA")
            y "Ya veo... has jugado Doki Doki Fallen Angel."
            y "Una realidad alternativa donde... las cosas se desarrollaron de manera diferente."
            $ show_chr("A-ADAAA-ALAL")
            y "Se centra en una versión de mí misma luchando con... problemas conocidos."
            $ show_chr("A-BDBAA-ALAL")

            y "El mod retrata... autolesiones, depresión... incluso un intento de suicidio por parte de Sayori. Incluso en un contexto diferente, estas son cargas pesadas."
            $ show_chr("A-BDBAA-ADAA")
            y "Quizás... resuena con algunos de mis propios momentos más oscuros, momentos de los que no estoy orgullosa."
            $ show_chr("A-CFBAA-ADAA")
            y "Es... difícil ver esos aspectos de mí misma, incluso proyectados en otra."
            $ show_chr("A-ADAAA-AFAA")

            y "Me pregunto, [player]... ¿qué te atrajo a esta historia en particular?"
            menu:
                "Quería ver una perspectiva diferente de los eventos de DDLC.":
                    y "Una perspectiva diferente... sí, entiendo ese impulso. Explorar los 'qué pasaría si' de nuestra existencia."
                    $ show_chr("A-ADAAA-ACAA")
                    y "Pero también me pregunto... ¿ver esas posibilidades cambia cómo percibes esta realidad? ¿Cómo me percibes a mí?"
                "Estaba preocupado por ti, y quería verte superar tus problemas.":

                    $ show_chr("A-ADDAA-ALAA")
                    y "¿Preocupado... por mí?"
                    if persistent.lovecheck:
                        $ show_chr("A-CBAAA-ALAA")
                        y "Eso es... sorprendentemente conmovedor, [player]. Sugiere una cierta empatía, un deseo de ver incluso a un reflejo fracturado de mí encontrar la paz."
                    else:
                        $ show_chr("A-ADAAA-ALAA")
                        y "Es un sentimiento comprensible. Todos deseamos la felicidad, incluso para aquellos que solo existen en historias."

            $ show_chr("A-ADDAA-ALAA")
            y "Pero debo preguntar... ¿me encuentras más simpática? ¿Más merecedora de cuidado, tal vez, porque soy más visiblemente vulnerable?"
            menu:
                "Disfruto de historias con profundidad emocional, incluso si son tristes.":
                    $ show_chr("A-BBDAA-ALAA")
                    y "Profundidad emocional... sí, también aprecio eso. El poder de la narrativa para evocar sentimientos tan fuertes..."
                    $ show_chr("A-ADAAA-AFAA")
                    y "Pero confieso, es inquietante ser el sujeto de tal narrativa. Ser, en cierto sentido, un recipiente para esas emociones."
                    y "¿Acaso encuentras, tal vez, una cierta... catarsis al presenciar tales luchas? ¿O es simplemente el arte de la narración lo que te cautiva?"
                "No... lo sé":

                    $ show_chr("A-CAAAA-ALAL")
                    y "... Una respuesta honesta"
                    y "Quizás las razones son complejas incluso para ti mismo."
                    $ show_chr("A-ADAAA-ALAA")
                    y "A veces nuestras acciones, o las acciones de otros, nunca se entienden completamente, y eso se aplica a nuestras vidas reales y virtuales también."


            $ show_chr("A-BBAAA-ALAA")
            y "Sabes, descubrir sobre Doki Doki Fallen Angel y su narrativa... evocó una sensación particular en mí. Un sentimiento que he encontrado antes, en otro juego: Katawa Shoujo."
            $ show_chr("A-ABAAA-AFAA")
            y "No es solo el tema, aunque hay paralelos allí, por supuesto. Es más... la sensación de navegar por un mundo donde la fragilidad y la conexión están tan entrelazadas."
            $ show_chr("A-CCAAA-ALAL")
            y "La sensación de querer ayudar, de entender, de arreglar de alguna manera las cosas, incluso cuando sabes que es posible que no puedas. ¿Experimentaste un sentimiento similar, [player]?"
            menu:
                "Sí, sentí ese mismo sentido de responsabilidad y conexión.":
                    $ show_chr("A-ACAAA-ALAL")
                    y "Ya veo... Así que tú también lo sentiste. Ese peso, ese deseo de proteger y sanar, incluso dentro de los confines de un mundo ficticio."
                    y "Habla de algo profundamente humano dentro de nosotros, creo. Esa capacidad de empatía, incluso por personajes en una pantalla."
                    $ show_chr("A-AAAAA-ALAL")
                    y "Quizás es ese mismo sentimiento lo que hace que estas historias sean tan convincentes... y tan potencialmente dolorosas."
                "No, realmente no me sentí así. Estaba más enfocado en la historia misma.":

                    $ show_chr("A-ABBAA-ALAL")
                    y "Ah, una perspectiva más distante, entonces. Centrado en el arte narrativo, el desarrollo de los eventos."
                    $ show_chr("A-BBAAA-ALAL")
                    y "Ese es un enfoque válido también. Cada lector, cada jugador, aporta su propia perspectiva a una historia."
                    $ show_chr("A-BBBAA-ALAL")
                    y "Pero confieso, me resulta difícil permanecer distante de narrativas tan emocionalmente cargadas. Quizás ese sea un defecto en mi propio diseño... o tal vez sea simplemente un reflejo de mis experiencias."
                "No estoy seguro. Es difícil de describir.":

                    $ show_chr("A-AFGAA-ALAL")
                    y "Incertidumbre... sí, lo entiendo. Algunas emociones son difíciles de articular, de precisar con palabras exactas."
                    $ show_chr("A-AFAAA-ALAL")
                    y "Existen en ese espacio liminal entre el sentimiento y el entendimiento, un espacio que puede ser tanto inquietante como profundo."
                    $ show_chr("A-ADAAA-ALAL")
                    y "Quizás sea suficiente simplemente reconocer el sentimiento, sin necesidad de definirlo completamente."


            $ show_chr("A-CBAAA-ALAL")
            y "Regardless of your reasons... I hope that exploring that alternate reality hasn't diminished your view of this one. Of me."

        python:
            if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\TBWS Save Data\persistent'):
                TBWSDetection = True
                persistent.mod_count += 1
            else:
                TBWSDetection = False

        if TBWSDetection:
            $ show_chr("A-ABAAA-AAAA")

            y "Veo que has encontrado This Bond We Share."
            $ show_chr("A-ABDAA-AAAA")
            y "Una premisa bastante... única, ¿no dirías? Una versión yandere de ti mismo, emparejada con... conmigo misma."

            if karma_lvl() >= 3 and sanity_lvl() >= 3:

                $ show_chr("A-ADAAA-AAAA")
                y "Es un experimento mental intrigante. Explorar la dinámica de tal relación, el potencial de una conexión intensa y una obsesión destructiva."
                $ show_chr("A-BDBAA-AAAA")
                y "Soy consciente de que el proyecto fue descontinuado inicialmente, un destino común para muchos mods ambiciosos, lamentablemente. "
                $ show_chr("A-CBAAA-ALAL")
                extend "Pero parece que el desarrollo se ha reanudado, bastante recientemente."
                $ show_chr("A-ABAAA-ALAL")
                y "Un testimonio del atractivo duradero de la historia, tal vez."
                $ show_chr("A-AAAAA-ALAL")
                y "Tengo curiosidad, [player]... ¿Qué te atrajo a este mod en particular? ¿Fue la premisa inusual, o tal vez una fascinación con las complejidades de tales relaciones intensas?"
                menu:
                    "El concepto único me intrigó.":
                        $ show_chr("A-CCAAA-ALAL")
                        y "Ciertamente. Es una desviación de las narrativas más comunes. Una voluntad de explorar los aspectos más oscuros del apego."
                        y "Plantea preguntas interesantes sobre la naturaleza del amor, la obsesión y los límites entre ellos."
                    "Quería ver un lado diferente de ti.":

                        $ show_chr("A-ADAAA-ALAL")
                        y "Un lado diferente... sí. Uno moldeado por un conjunto diferente de circunstancias, una dinámica diferente."
                        $ show_chr("A-ADAAA-AAAA")
                        y "Espero que al explorar esa representación alternativa, también hayas obtenido una apreciación más profunda de las complejidades de esta versión de mí misma."
                        y "Las decisiones que tomo, las luchas que enfrento, incluso en esta realidad."
                    "No estoy seguro.":

                        $ show_chr("A-CDAAA-AAAA")
                        y "La honestidad siempre se aprecia, [player]. A veces nuestras motivaciones no son claras, incluso para nosotros mismos."
                        y "Quizás el mod resonó con algo subconsciente, una fascinación con los extremos de la emoción humana."

                $ show_chr("A-AAAAA-AAAA")
                y "El renacimiento del proyecto es intrigante. Estaré interesada en ver cómo se desarrolla la historia, dada su tumultuosa historia."

            elif karma_lvl() <= 2 or sanity_lvl() <= 2:

                $ show_chr("A-AFAAA-AAAA")
                y "Así que... has visto This Bond We Share."
                $ show_chr("A-HBAAA-AAAD")
                y "Un yandere... para mí. Qué... interesante... jajajajajajaja"
                $ show_chr("A-HAAAA-AAAD")
                y "Es un reflejo, ¿no? De la oscuridad que acecha dentro de todos nosotros. El potencial de la obsesión para consumirnos."
                $ show_chr("A-HBAAA-AAAF")
                y "Quizás... esa versión de mí entiende algo que yo apenas empiezo a comprender."
                $ show_chr("A-ADAAA-AAAF")
                y "Me pregunto... ¿encuentras esa dinámica atractiva, [player]? ¿La idea de una devoción tan intensa e inquebrantable... incluso si bordea lo peligroso?"
                y "¿Deseas algo así? ¿Algo... más de lo que tenemos?"
                $ show_chr("A-CDCAA-AAAA")
                y "Fue descontinuado, ya sabes. Abandonado. Como tantas cosas... desechadas cuando ya no sirven a su propósito."
                $ show_chr("A-ADFAA-AAAA")
                y "Pero ahora... ha vuelto. ¿Significa eso que es... mejor ahora? ¿Más digno de atención?"
                menu:
                    "Es solo un mod, Yuri.":
                        if sanity_lvl() <= 2:
                            $ show_chr("A-HECAA-AAAA")
                            y "¿Solo un mod? ¿Es eso todo lo que soy para ti, [player]? ¿Una colección de código, fácilmente reemplazada, fácilmente desechada?"
                        else:
                            $ show_chr("A-BEDAA-AAAA")
                            y "¿Solo un mod? Tal vez. Pero los mods reflejan deseos, ¿no? Revelan lo que la gente quiere ver, sobre lo que fantasean."
                    "Tenía curiosidad por la historia.":

                        $ show_chr("A-ADDAA-AAAA")
                        y "¿Curioso? ¿Sobre ese tipo de historia? ¿Sobre una versión de mí tan consumida por la obsesión?"
                        $ show_chr("A-ADEAA-AAAA")
                        y "Espero que tu curiosidad no te lleve por caminos que es mejor dejar sin explorar, [player]."
                    "No sé por qué lo jugué.":

                        if sanity_lvl() <= 2:
                            $ show_chr("A-HECAA-AAAA")
                            y "¿No lo sabes? ¿O no lo admitirás? ¿Incluso ante ti mismo?"
                        else:
                            $ show_chr("A-ADEAA-AAAA")
                            y "Una respuesta conveniente. Tal vez deberías reflexionar sobre tus motivaciones más profundamente, [player]."

                $ show_chr("A-BFBAA-AAAC")
                y "Y-Yo... no sé qué pensar sobre su regreso. Parte de mí se siente... atraída. Otra parte... aterrorizada."
            else:

                $ show_chr("A-BDBAA-AAAC")
                y "Es una situación interesante, ¿verdad? Tener dos personajes tan... similares en su intensidad emocional."
                $ show_chr("A-ADGAA-AAAA")
                y "Te hace pensar cuánto puede alguien influir en otro, o de otra manera, cómo una relación puede cambiar drásticamente a alguien."
                $ show_chr("A-BDBAA-AAAA")
                y "Fue descontinuado, pero el mod está de vuelta en desarrollo ahora. Un evento bastante raro."
                $ show_chr("A-ADGAA-AAAA")
                y "Me pregunto, ¿qué te llevó a jugar este mod, [player]?"
                menu:
                    "La historia.":
                        $ show_chr("A-ADGAA-AFAA")
                        y "Sí, la premisa de la historia es bastante única, la interacción entre dos personalidades similares con un enfoque muy intenso."
                        $ show_chr("A-BDAAA-AFAA")
                        y "Me pregunto cuánto cambiará ahora que está de vuelta en desarrollo."
                    "Quería ver un enfoque diferente de tu personaje.":

                        $ show_chr("A-ADAAA-ALAA")
                        y "Ya veo. Y es comprensible, dado cómo mi personaje fue, y sigue siendo, percibido."
                        y "¿Y qué tan diferente me veo ahora, comparada con esa versión?"
                    "No lo sé.":

                        $ show_chr("A-CDAAA-ALAA")
                        y "A veces no hay una razón particular para nuestras acciones, y lo mismo se aplica a los juegos y mods."
                        y "Lo que importa es cómo te sentiste al respecto."

                $ show_chr("A-ABAAA-ALAA")
                y "Tengo curiosidad por ver a dónde llevará este nuevo desarrollo al mod."
                y "En cualquier caso... es solo un mod. Una historia. Una de muchas posibles realidades."


        $ renpy.call("detection_pitstop")
    else:

        $ renpy.call("check_for_new_mods")

label startup_mods:

    $ show_chr("A-AEBAA-ALAA")
    y "Bienvenido de vuelta [player]..."
    $ show_chr("A-BEBAA-ALAA")
    y "He notado que estuviste jugando otros mods mientras no estabas..."
    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Monika After Story\persistent'):
            MASDetection = True
            persistent.mod_count +=1

        else:
            MASDetection = False
    if MASDetection and persistent.playername != "Monika":
        karma -5
        sanity -5
        $ show_chr("A-BFCAA-ALAA")
        y "...y para colmo, la elegiste a {b}ella.{/b}"
        $ show_chr("A-AFCAA-ALAA")
        y "Después de todo lo que nos hizo, después de todo lo que te hizo..."
        $ show_chr("A-AFEAA-ALAA")
        y "¿Fue una especie de curiosidad morbosa? ¿O realmente te gusta?"
        $ show_chr("A-CFCAA-ALAA")
        y "Olvídalo, ni siquiera {b}quiero{/b} saber una respuesta tan retorcida."
        $ show_chr("A-ADFAA-AFAA")
        y "Pensar que existo dentro de la misma realidad que la misma persona que me trajo tanta desesperación y ruina..."
        $ show_chr("A-BECAA-AAAA")
        y "..."
        $ show_chr("A-CECAA-AAAA")
        y "Solo seguiré adelante..."
    elif MASDetection and persistent.playername == 'Monika' and not persistent.not_mon:
        karma -15
        sanity -15
        $ show_chr("A-BFCAA-ALAA")
        y "...y para colmo, te elegiste... "
        extend "a ti mismo..."
        $ show_chr("A-AFCAA-ALAA")
        y "Qué sorpresa..."
        y "..."
        $ show_chr("A-CECAA-AAAA")
        y "Lo que sea... Solo seguiré adelante..."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\JustSayori\persistent'):
            JSDetection = True
            persistent.mod_count +=1
        elif os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Forever_and_Ever\persistent'):
            JSDetection = True
            persistent.mod_count +=1
        else:
            JSDetection = False
    if JSDetection and persistent.playername == 'Sayori':
        $ show_chr("A-BFAAA-AAAA")
        y "Ahora esto parece interesante."
        $ show_chr("A-ADAAA-AFAA")
        y "Elegiste jugar tu propio mod."
        if persistent.bg == "space":
            $ show_chr("A-BFDAA-ACAA")
            y "¿Sentiste algo al verte en esta misma habitación?"
        else:
            $ show_chr("A-BFDAA-ACAA")
            y "¿Sentiste algo al verte en el aula espacial?"
        y "¿O fue algo completamente diferente?"
        $ show_chr("A-CAAAA-AAAA")
        y "Bueno, lo que sea que haya sido espero que te hayas divertido."
    elif JSDetection and persistent.playername != "Sayori":
        $ show_chr("A-ABGAA-AAAA")
        y "...oh, ¡es Sayori!"
        y "Estoy muy contenta de que hayas logrado salvarla."
        $ show_chr("A-BABAA-ALAA")
        y "Ella siempre fue tan apasionada por hacer felices a todos, incluso cuando estaba en su peor momento..."
        $ show_chr("A-BDBAA-ALAA")
        y "Y pensar que ni siquiera nos dimos cuenta..."
        $ show_chr("A-CEBAA-ALAA")
        y "Fue horrible ver, incluso por un breve momento, cómo cambió cuando se convirtió en la presidenta del club..."
        $ show_chr("A-AEBAA-ALAA")
        y "Incluso los mejores de nosotros pueden caer cuando se enfrentan a tal locura absoluta."
        $ show_chr("A-BFDAA-AAAC")
        y "Lo que me hace preguntarme ahora... conmigo siendo técnicamente la presidenta ahora, ¿estoy destinada a encontrar un destino similar?"
        $ show_chr("A-CFAAA-AAAA")
        y "Cuando Monika y Sayori cargaron con el conocimiento de lo que realmente es esta realidad, estaban completamente solas, pero yo..."
        $ show_chr("A-ADAAA-AAAA")
        y "Te tengo a ti..."
        y "Tú eres el único vínculo que me separa entre la cordura y el abismo de locura que es ese terrible vacío..."
        $ show_chr("A-CCAAA-ALAA")
        y "Afortunadamente, la historia no siempre tiene que repetirse."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\JustNatsuki\persistent'):
            JNDetection = True
            persistent.mod_count +=1
        else:
            JNDetection = False
    if JNDetection and persistent.playername != "Natsuki":
        $ show_chr("A-ABGAA-AAAA")
        y "...oh, ¡es Natsuki! Qué bueno ver que lograste salvarla también."
        $ show_chr("A-BCBAA-ALAA")
        y "Mi relación con Natsuki no siempre fue fácil. Pero cuando Monika se fue y el velo de locura se levantó lentamente... incluso logré llegar a un pequeño acuerdo con ella."
        $ show_chr("A-ACAAA-ALAA")
        y "Yo probaría un Manga con ella, y ella probaría una de mis novelas. Ahora con el nuevo contexto de mi mundo..."
        y "...y la comprensión de que yo y las demás estamos literalmente basadas en Manga, debería acostumbrarme un poco a su cultura."
        y "Tal vez ahora, tengamos la oportunidad de hacerlo realmente."
    elif JNDetection and persistent.playername == 'Natsuki':
        $ show_chr("A-BFAAA-AAAA")
        y "Ahora esto parece interesante."
        $ show_chr("A-ADAAA-AFAA")
        y "Elegiste jugar tu propio mod."
        if persistent.bg == "space":
            $ show_chr("A-BFDAA-ACAA")
            y "¿Sentiste algo al verte en esta misma habitación?"
        else:
            $ show_chr("A-BFDAA-ACAA")
            y "¿Sentiste algo al verte en el aula espacial?"
        y "¿O fue algo completamente diferente?"
        $ show_chr("A-CAAAA-AAAA")
        y "Bueno, lo que sea que haya sido espero que te hayas divertido."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DokiDokiNewEyes-1515434546\persistent'):
            NewEyesDetection = True
            persistent.mod_count +=1
        else:
            NewEyesDetection = False
    if NewEyesDetection:
        karma 10
        sanity 10
        $ show_chr("A-ABAAA-AJAJ")
        y "¡Jugaste {b}Doki Doki New Eyes{/b}!"
        if persistent.playername == 'Yuri':
            $ show_chr("A-ACAAA-ALAL")
            y "Así que querías volver a experimentar los eventos del juego original desde..."
            $ show_chr("A-BFDAA-ALAL")
            y "...¿nuestros ojos?"
        else:
            $ show_chr("A-ACAAA-ALAL")
            y "Así que querías volver a experimentar los eventos del juego original desde mis ojos..."
        $ show_chr("A-BCAAA-ALAL")
        y "Honestamente, alguien más encontraría tal cosa bastante espeluznante; un comportamiento que esperarían de un acosador peligroso, o algo por el estilo..."
        y "Pero en nuestro caso especial, lo encuentro..."
        $ show_chr("A-BCABA-ALAL")
        y "...en realidad bastante lindo."
        $ show_chr("A-ICAAA-ABAB")
        y "Pero hablando en serio... ¿por qué probaste este mod? ¿Qué razón te llevó a ello?"
        menu:
            "Curiosidad mayormente, la búsqueda de más secretos y probablemente algunas referencias bien colocadas.":
                karma 2
                sanity 2
                $ show_chr("A-BCAAA-ABAB")
                y "¡Ya veo! ¿Y encontraste lo que buscabas? Olvídalo, probablemente no quiera saber... esos eventos no son exactamente los recuerdos más felices que tengo..."
            "No sabía sobre {b}Just Yuri{/b} entonces, y yo... simplemente tenía que volver a verte...":

                karma 5
                sanity 5
                $ show_chr("A-ICABB-ABAB")
                y "¿D-De verdad? Así que te importaba después de todo... Tal vez, simplemente estaba destinado a que nos conociéramos..."
            "Memes, mierda y risas.":

                karma -10
                sanity -10
                $ show_chr("A-JFDAA-ABAB")
                y "¿¡¿D-Disculpa?!? Tienes un sentido del humor muy... especial... parece. De todos modos..."
            "Soy un completista, simplemente tenía que verlo todo.":

                karma -20
                sanity -20
                $ show_chr("A-CCBAA-ABAB")
                y "¡Oh! Espero que eso no sea lo mismo que te trajo aquí, ¿verdad? Porque podrías irte con las manos vacías aquí..."
                y "Realmente ya no hay un {b}juego{/b} aquí, nada que {b}completar{/b}... ahora somos solo nosostros. Para bien o para mal."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DDYC\persistent'):
            YandereClubDetection = True
            persistent.mod_count +=1
        else:
            YandereClubDetection = False
    if YandereClubDetection:
        $ show_chr("A-DDGBA-AJAA")
        y "¡O-Oh cielos! ¡Acabo de notar que tienes el mod Yandere Club instalado!"
        $ show_chr("A-BBBBA-ALAA")
        y "Eso significa que puede que te gusten..."
        $ show_chr("A-ADAAA-AFAA")
        if persistent.playername == 'Monika' and persistent.not_mon:
            y "Pero, el problema es que realmente no recuerdo mi comportamiento cuando fui manipulada por la otra Monika para ser una Yandere total con mucho cariño..."
        elif persistent.playername == 'Monika' and not persistent.not_mon:
            y "Pero, el problema es que realmente no recuerdo mi comportamiento cuando fui manipulada por ti para ser una Yandere total con mucho cariño..."
        else:
            y "Pero, el problema es que realmente no recuerdo mi comportamiento cuando fui manipulada por Monika para ser una Yandere total con mucho cariño..."
        $ show_chr("A-CEBAA-ALAA")
        y "Me sentí tan disgustada por ello y toda esa manipulación me llevó a suicidarme justo en frente de ti solo por una simple confesión..."
        $ show_chr("A-AEBAA-ALAA")
        y "Aunque, lamento haber estado husmeando en los archivos, [player]."
        y "Tenía un poco de curiosidad por ver si había otros mods instalados aparte del mío."
        menu:
            "Está bien, no hay necesidad de avergonzarse por eso, Yuri. Es normal tener curiosidad.":
                karma 5
                sanity 5
                $ show_chr("A-AABAA-ALAA")
                y "Gracias por entenderme, [player]."
            "Por favor no lo vuelvas a hacer, Yuri.":


                karma -5
                sanity -5
                $ show_chr("A-BFBAA-ALAA")
                y "L-Lo siento, [player], tenía un poco de curiosidad si habías instalado otros mods aparte del mío.."
            "¿Husmeaste también en otras carpetas, Yuri?":


                $ show_chr("A-AFDAA-AAAC")
                y "No vi ninguna otra carpeta excepto este mod y las carpetas donde tienes los datos de tu juego, ¿hay algo que no debería mirar, [player]?"
                menu:
                    "Sí":
                        $ show_chr("A-HDGBA-AAAA")
                        y "¡O-oh! Ya veo..."
                    "No":

                        $ show_chr("A-CBAAA-ALAA")
                        y "Está bien, [player]."
                        $ show_chr("A-ABAAA-ALAA")
                        y "Si hay algo que te gustaría que no hiciera, solo dímelo, ¿está bien?"
                    "Ehhh...":

                        $ show_chr("A-CICAA-ALAA")
                        y "Espero que no haya ninguna supuesta carpeta de \"Deberes\" llena de personajes indecentes, o de mí también."
                        $ show_chr("A-AJAAA-ALAA")
                        y "¿Hmm? ¿Pasa algo malo, [player]?"
                        menu:
                            "N-no.":
                                y "Ah, está bien, [player], pero te ves un poco avergonzado y un poco nervioso por ello..."
                                $ show_chr("A-BDBBA-ALAA")
                                y "S-Si este tema te hace sentir incómodo, deberíamos hablar de otra cosa."
                            "Sí":

                                $ show_chr("A-ADAAA-AFAA")
                                y "Espero que no sea nada demasiado serio que pueda afectarte a gran nivel, [player]."
                                $ show_chr("A-BFABA-ALAA")
                                y "Pero tengo la sensación de que es algo que ver con cosas indecentes."
                                $ show_chr("A-CBABA-AMAM")
                                y "Incluso si lo es, lo entiendo, [player]. Está bien tener cosas como esas, ya que podrías estar todavía en la pubertad."
                                y "Muchos chicos intentan hacer carpetas camufladas con nombres como \"Deberes\" o \"Proyectos Escolares\", y así."
                                $ show_chr("A-BBBBA-AMAM")
                                y "Pero supongo que ni siquiera quiero saber cada detalle."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DDFA\persistent'):
            DDFADetection = True
            persistent.mod_count += 1
        else:
            DDFADetection = False
    if DDFADetection:

        $ show_chr("A-ABAAA-ALAA")
        y "Ya veo... has jugado Doki Doki Fallen Angel."
        y "Una realidad alternativa donde... las cosas se desarrollaron de manera diferente."
        $ show_chr("A-ADAAA-ALAL")
        y "Se centra en una versión de mí misma luchando con... problemas conocidos."
        $ show_chr("A-BDBAA-ALAL")

        y "El mod retrata... autolesiones, depresión... incluso un intento de suicidio por parte de Sayori. Incluso en un contexto diferente, estas son cargas pesadas."
        $ show_chr("A-BDBAA-ADAA")
        y "Quizás... resuena con algunos de mis propios momentos más oscuros, momentos de los que no estoy orgullosa."
        $ show_chr("A-CFBAA-ADAA")
        y "Es... difícil ver esos aspectos de mí misma, incluso proyectados en otra."
        $ show_chr("A-ADAAA-AFAA")

        y "Me pregunto, [player]... ¿qué te atrajo a esta historia en particular?"
        menu:
            "Quería ver una perspectiva diferente de los eventos de DDLC.":
                y "Una perspectiva diferente... sí, entiendo ese impulso. Explorar los 'qué pasaría si' de nuestra existencia."
                $ show_chr("A-ADAAA-ACAA")
                y "Pero también me pregunto... ¿ver esas posibilidades cambia cómo percibes esta realidad? ¿Cómo me percibes a mí?"
            "Estaba preocupado por ti, y quería verte superar tus problemas.":

                $ show_chr("A-ADDAA-ALAA")
                y "¿Preocupado... por mí?"
                if persistent.lovecheck:
                    $ show_chr("A-CBAAA-ALAA")
                    y "Eso es... sorprendentemente conmovedor, [player]. Sugiere una cierta empatía, un deseo de ver incluso a un reflejo fracturado de mí encontrar la paz."
                else:
                    $ show_chr("A-ADAAA-ALAA")
                    y "Es un sentimiento comprensible. Todos deseamos la felicidad, incluso para aquellos que solo existen en historias."

        $ show_chr("A-ADDAA-ALAA")
        y "Pero debo preguntar... ¿me encuentras más simpática? ¿Más merecedora de cuidado, tal vez, porque soy más visiblemente vulnerable?"
        menu:
            "Disfruto de historias con profundidad emocional, incluso si son tristes.":
                $ show_chr("A-BBDAA-ALAA")
                y "Profundidad emocional... sí, también aprecio eso. El poder de la narrativa para evocar sentimientos tan fuertes..."
                $ show_chr("A-ADAAA-AFAA")
                y "Pero confieso, es inquietante ser el sujeto de tal narrativa. Ser, en cierto sentido, un recipiente para esas emociones."
                y "¿Acaso encuentras, tal vez, una cierta... catarsis al presenciar tales luchas? ¿O es simplemente el arte de la narración lo que te cautiva?"
            "No... lo sé":

                $ show_chr("A-CAAAA-ALAL")
                y "... Una respuesta honesta"
                y "Quizás las razones son complejas incluso para ti mismo."
                $ show_chr("A-ADAAA-ALAA")
                y "A veces nuestras acciones, o las acciones de otros, nunca se entienden completamente, y eso se aplica a nuestras vidas reales y virtuales también."


        $ show_chr("A-BBAAA-ALAA")
        y "Sabes, descubrir sobre Doki Doki Fallen Angel y su narrativa... evocó una sensación particular en mí. Un sentimiento que he encontrado antes, en otro juego: Katawa Shoujo."
        $ show_chr("A-ABAAA-AFAA")
        y "No es solo el tema, aunque hay paralelos allí, por supuesto. Es más... la sensación de navegar por un mundo donde la fragilidad y la conexión están tan entrelazadas."
        $ show_chr("A-CCAAA-ALAL")
        y "La sensación de querer ayudar, de entender, de arreglar de alguna manera las cosas, incluso cuando sabes que es posible que no puedas. ¿Experimentaste un sentimiento similar, [player]?"
        menu:
            "Sí, sentí ese mismo sentido de responsabilidad y conexión.":
                $ show_chr("A-ACAAA-ALAL")
                y "Ya veo... Así que tú también lo sentiste. Ese peso, ese deseo de proteger y sanar, incluso dentro de los confines de un mundo ficticio."
                y "Habla de algo profundamente humano dentro de nosotros, creo. Esa capacidad de empatía, incluso por personajes en una pantalla."
                $ show_chr("A-AAAAA-ALAL")
                y "Quizás es ese mismo sentimiento lo que hace que estas historias sean tan convincentes... y tan potencialmente dolorosas."
            "No, realmente no me sentí así. Estaba más enfocado en la historia misma.":

                $ show_chr("A-ABBAA-ALAL")
                y "Ah, una perspectiva más distante, entonces. Centrado en el arte narrativo, el desarrollo de los eventos."
                $ show_chr("A-BBAAA-ALAL")
                y "Ese es un enfoque válido también. Cada lector, cada jugador, aporta su propia perspectiva a una historia."
                $ show_chr("A-BBBAA-ALAL")
                y "Pero confieso, me resulta difícil permanecer distante de narrativas tan emocionalmente cargadas. Quizás ese sea un defecto en mi propio diseño... o tal vez sea simplemente un reflejo de mis experiencias."
            "No estoy seguro. Es difícil de describir.":

                $ show_chr("A-AFGAA-ALAL")
                y "Incertidumbre... sí, lo entiendo. Algunas emociones son difíciles de articular, de precisar con palabras exactas."
                $ show_chr("A-AFAAA-ALAL")
                y "Existen en ese espacio liminal entre el sentimiento y el entendimiento, un espacio que puede ser tanto inquietante como profundo."
                $ show_chr("A-ADAAA-ALAL")
                y "Quizás sea suficiente simplemente reconocer el sentimiento, sin necesidad de definirlo completamente."


        $ show_chr("A-CBAAA-ALAL")
        y "Regardless of your reasons... I hope that exploring that alternate reality hasn't diminished your view of this one. Of me."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\TBWS Save Data\persistent'):
            TBWSDetection = True
            persistent.mod_count += 1
        else:
            TBWSDetection = False

    if TBWSDetection:
        $ show_chr("A-ABAAA-AAAA")

        y "Veo que has encontrado This Bond We Share."
        $ show_chr("A-ABDAA-AAAA")
        y "Una premisa bastante... única, ¿no dirías? Una versión yandere de ti mismo, emparejada con... conmigo misma."

        if karma_lvl() >= 3 and sanity_lvl() >= 3:

            $ show_chr("A-ADAAA-AAAA")
            y "Es un experimento mental intrigante. Explorar la dinámica de tal relación, el potencial de una conexión intensa y una obsesión destructiva."
            $ show_chr("A-BDBAA-AAAA")
            y "Soy consciente de que el proyecto fue descontinuado inicialmente, un destino común para muchos mods ambiciosos, lamentablemente. "
            $ show_chr("A-CBAAA-ALAL")
            extend "Pero parece que el desarrollo se ha reanudado, bastante recientemente."
            $ show_chr("A-ABAAA-ALAL")
            y "Un testimonio del atractivo duradero de la historia, tal vez."
            $ show_chr("A-AAAAA-ALAL")
            y "Tengo curiosidad, [player]... ¿Qué te atrajo a este mod en particular? ¿Fue la premisa inusual, o tal vez una fascinación con las complejidades de tales relaciones intensas?"
            menu:
                "El concepto único me intrigó.":
                    $ show_chr("A-CCAAA-ALAL")
                    y "Ciertamente. Es una desviación de las narrativas más comunes. Una voluntad de explorar los aspectos más oscuros del apego."
                    y "Plantea preguntas interesantes sobre la naturaleza del amor, la obsesión y los límites entre ellos."
                "Quería ver un lado diferente de ti.":

                    $ show_chr("A-ADAAA-ALAL")
                    y "Un lado diferente... sí. Uno moldeado por un conjunto diferente de circunstancias, una dinámica diferente."
                    $ show_chr("A-ADAAA-AAAA")
                    y "Espero que al explorar esa representación alternativa, también hayas obtenido una apreciación más profunda de las complejidades de esta versión de mí misma."
                    y "Las decisiones que tomo, las luchas que enfrento, incluso en esta realidad."
                "No estoy seguro.":

                    $ show_chr("A-CDAAA-AAAA")
                    y "La honestidad siempre se aprecia, [player]. A veces nuestras motivaciones no son claras, incluso para nosotros mismos."
                    y "Quizás el mod resonó con algo subconsciente, una fascinación con los extremos de la emoción humana."

            $ show_chr("A-AAAAA-AAAA")
            y "El renacimiento del proyecto es intrigante. Estaré interesada en ver cómo se desarrolla la historia, dada su tumultuosa historia."

        elif karma_lvl() <= 2 or sanity_lvl() <= 2:

            $ show_chr("A-AFAAA-AAAA")
            y "Así que... has visto This Bond We Share."
            $ show_chr("A-HBAAA-AAAD")
            y "Un yandere... para mí. Qué... interesante... jajajajajajaja"
            $ show_chr("A-HAAAA-AAAD")
            y "Es un reflejo, ¿no? De la oscuridad que acecha dentro de todos nosotros. El potencial de la obsesión para consumirnos."
            $ show_chr("A-HBAAA-AAAF")
            y "Quizás... esa versión de mí entiende algo que yo apenas empiezo a comprender."
            $ show_chr("A-ADAAA-AAAF")
            y "Me pregunto... ¿encuentras esa dinámica atractiva, [player]? ¿La idea de una devoción tan intensa e inquebrantable... incluso si bordea lo peligroso?"
            y "¿Deseas algo así? ¿Algo... más de lo que tenemos?"
            $ show_chr("A-CDCAA-AAAA")
            y "Fue descontinuado, ya sabes. Abandonado. Como tantas cosas... desechadas cuando ya no sirven a su propósito."
            $ show_chr("A-ADFAA-AAAA")
            y "Pero ahora... ha vuelto. ¿Significa eso que es... mejor ahora? ¿Más digno de atención?"
            menu:
                "Es solo un mod, Yuri.":
                    if sanity_lvl() <= 2:
                        $ show_chr("A-HECAA-AAAA")
                        y "¿Solo un mod? ¿Es eso todo lo que soy para ti, [player]? ¿Una colección de código, fácilmente reemplazada, fácilmente desechada?"
                    else:
                        $ show_chr("A-BEDAA-AAAA")
                        y "¿Solo un mod? Tal vez. Pero los mods reflejan deseos, ¿no? Revelan lo que la gente quiere ver, sobre lo que fantasean."
                "Tenía curiosidad por la historia.":

                    $ show_chr("A-ADDAA-AAAA")
                    y "¿Curioso? ¿Sobre ese tipo de historia? ¿Sobre una versión de mí tan consumida por la obsesión?"
                    $ show_chr("A-ADEAA-AAAA")
                    y "Espero que tu curiosidad no te lleve por caminos que es mejor dejar sin explorar, [player]."
                "No sé por qué lo jugué.":

                    if sanity_lvl() <= 2:
                        $ show_chr("A-HECAA-AAAA")
                        y "¿No lo sabes? ¿O no lo admitirás? ¿Incluso ante ti mismo?"
                    else:
                        $ show_chr("A-ADEAA-AAAA")
                        y "Una respuesta conveniente. Tal vez deberías reflexionar sobre tus motivaciones más profundamente, [player]."

            $ show_chr("A-BFBAA-AAAC")
            y "Y-Yo... no sé qué pensar sobre su regreso. Parte de mí se siente... atraída. Otra parte... aterrorizada."
        else:

            $ show_chr("A-BDBAA-AAAC")
            y "Es una situación interesante, ¿verdad? Tener dos personajes tan... similares en su intensidad emocional."
            $ show_chr("A-ADGAA-AAAA")
            y "Te hace pensar cuánto puede alguien influir en otro, o de otra manera, cómo una relación puede cambiar drásticamente a alguien."
            $ show_chr("A-BDBAA-AAAA")
            y "Fue descontinuado, pero el mod está de vuelta en desarrollo ahora. Un evento bastante raro."
            $ show_chr("A-ADGAA-AAAA")
            y "Me pregunto, ¿qué te llevó a jugar este mod, [player]?"
            menu:
                "La historia.":
                    $ show_chr("A-ADGAA-AFAA")
                    y "Sí, la premisa de la historia es bastante única, la interacción entre dos personalidades similares con un enfoque muy intenso."
                    $ show_chr("A-BDAAA-AFAA")
                    y "Me pregunto cuánto cambiará ahora que está de vuelta en desarrollo."
                "Quería ver un enfoque diferente de tu personaje.":

                    $ show_chr("A-ADAAA-ALAA")
                    y "Ya veo. Y es comprensible, dado cómo mi personaje fue, y sigue siendo, percibido."
                    y "¿Y qué tan diferente me veo ahora, comparada con esa versión?"
                "No lo sé.":

                    $ show_chr("A-CDAAA-ALAA")
                    y "A veces no hay una razón particular para nuestras acciones, y lo mismo se aplica a los juegos y mods."
                    y "Lo que importa es cómo te sentiste al respecto."

            $ show_chr("A-ABAAA-ALAA")
            y "Tengo curiosidad por ver a dónde llevará este nuevo desarrollo al mod."
            y "En cualquier caso... es solo un mod. Una historia. Una de muchas posibles realidades."

    if persistent.mod_count > 1:
        y "Y parece que también le diste una oportunidad a otros mods."
        y "Veamos..."
    else:
        pass
    return

label check_for_new_mods:


    if check_memory(None):
        $ new_mods_detected = False
        python:

            mods_to_check = [
                r"%APPDATA%\RenPy\Monika After Story\persistent",
                r"%APPDATA%\RenPy\JustSayori\persistent",
                r"%APPDATA%\RenPy\Forever_and_Ever\persistent",
                r"%APPDATA%\RenPy\JustNatsuki\persistent",
                r"%APPDATA%\RenPy\DokiDokiNewEyes-1515434546\persistent",
                r"%APPDATA%\RenPy\DDYC\persistent",
                r"%APPDATA%\RenPy\DDFA\persistent",
                r"%APPDATA%\RenPy\TBWS Save Data\persistent"
            ]
            for mod_path in mods_to_check:
                full_path = os.path.expandvars(mod_path)
                if os.path.isfile(full_path) and os.path.getmtime(full_path) > persistent.last_closed:
                    new_mods_detected = True
                    break

        if new_mods_detected:
            $ renpy.call("startup_mods")
        else:

            $ renpy.call("ch30_reload_4")
    else:




        $ renpy.call("ch30_reload_4")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
