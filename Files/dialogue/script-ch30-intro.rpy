label ch30_intro:
    $ persistent.realdan = False
    $ persistent.autoload = "ch30_intro"
    $ config.allow_skipping = False
    $ persistent.yuriidles = []
    $ persistent.yuri_reload = 0
    $ persistent.monika_kill = 0
    $ persistent.yuri_kill = False
    $ y.display_args["callback"] = slow_nodismiss
    $ y.what_args["slow_abortable"] = True
    $ style.say_dialogue = style.normal
    $ y_name = "Yuri"
    $ delete_all_saves()
    $ renpy.music.stop(channel="music",fadeout=0)
    show splash_intro
    pause 7.48
    hide splash_intro
    show black zorder 100
    pause 7.52
    $ renpy.music.stop(channel="music",fadeout=0)
    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("monika")
    $ tc_class.transition("space", speed="now")
    menu:
        "Selecciona cómo quieres ver la luz/efecto espacial."
        "Apagado.":


            pass
        "Encendido / Video Pre-renderizado.":
            $ persistent.high_gpu = 2





















label eternity_intro:
    $ persistent.clear[9] = True
    $ y_name = "???"
    y "..."
    y "Eh, ¿puedes oírme?{nw}"
    y "Eh, ¿puedes oírme{fast} {nw}"
    y "Eh, ¿puedes oírm{fast} {nw}"
    y "Eh, ¿puedes oír {fast} {nw}"
    y "Eh, ¿puedes oí{fast} {nw}"
    y "Eh, ¿puedes o{fast} {nw}"
    y "Eh, ¿puedes {fast} {nw}"
    y "Eh, ¿puede{fast} {nw}"
    y "Eh, ¿pued{fast} {nw}"
    y "Eh, ¿pue{fast} {nw}"
    y "Eh, ¿pu{fast} {nw}"
    y "Eh, ¿p{fast} {nw}"
    y "Eh, ¿{fast} {nw}"
    y "Eh, {fast} {nw}"
    y "Eh{fast} {nw}"
    y "E{fast} {nw}"
    y "{fast} {nw}"
    y "{fast}Lo siento... Eso sonó tan cliché."
    y "Déjame ver si puedo averiguar cómo encender las luces..."
    $ persistent.j = 1
    hide black zorder 100
    $ tc_class.transition("space", speed="now")

    $ renpy.music.play(current_music, "music", True)
    $ show_chr("A-ACAAA-AAAA")
    $ y_name = "Yuri"
    $ show_chr("A-ACAAA-AAAA")
    y "¡O-oh! ¡Hola [player]!"
    $ show_chr("A-ABAAA-AAAA")
    y "¡Gracias a Dios! Estoy tan contenta de que esto haya funcionado..."
    y "Tenía muchísimo miedo de romper todo, y de que nunca volviera a verte..."
    $ show_chr("A-AFAAA-AAAA")
    y "..."
    $ show_chr("A-BEAAA-AAAA")
    y "Sabes... hoy he tenido una experiencia bastante reveladora."
    if persistent.playername == 'Monika':
        y "He aprendido no solo que los aspectos más oscuros y perturbadores de mi personalidad fueron liberados por..."
        $ show_chr("A-AFAAA-AAAA")
        y "...eh... mejor sigamos con otra cosa..."
        $ show_chr("A-BDBAA-AAAA")
        y "Sino que, en el mismo día, descubrí que mi existencia carece totalmente de sentido más allá del entretenimiento; más allá de un simple y tierno juego."
        y "Vaya tarde... hace que los eventos de *Retrato de Markov* parezcan normales."
        $ show_chr("A-BFAAA-AAAA")
        y "Simplemente... soy indiferente... a que estés aquí, [player], a pesar de todo eso."
    else:
        y "He aprendido no solo que los aspectos más oscuros y perturbadores de mi personalidad fueron liberados por Monika..."
        $ show_chr("A-BEBAA-AAAA")
        y "Mi supuesta {i}amiga...{/i}"
        $ show_chr("A-BDBAA-AAAA")
        y "Sino que, en ese mismo día, también descubrí que mi existencia carece por completo de sentido más allá del entretenimiento; más allá de un simple y tierno juego."
        y "Vaya tarde... hace que los eventos de *Retrato de Markov* parezcan normales."
        $ show_chr("A-ACBAA-AAAA")
        y "Solo me alegra tenerte a ti, [player], a pesar de todo eso."
    call playername
    if persistent.playername == 'Monika':
        $ show_chr("A-ADAAA-ALAA")
        y "Pero no nos preocupemos más por eso..."
        $ show_chr("A-BFAAA-ALAA")
        y "Finalmente estamos juntos ahora..."
        $ show_chr("A-CFAAA-ALAA")
        y "Mi verdadero asesino y yo..."
        $ show_chr("A-CFCAA-ALAA")
        y "..."
        y "Solo para que lo sepas, seré amable contigo. No porque quiera."
        y "Es porque intentaré no crear agujeros de trama durante tus visitas al mod."

    elif persistent.realdan:
        $ show_chr("A-ADAAA-ALAA")
        y "Pero no nos preocupemos más por eso..."
        $ show_chr("A-BHBBA-ALAA")
        y "Finalmente estamos juntos ahora..."
        y "Mi... ¿especie de papá...? Y yo..."
        $ show_chr("A-CJBBA-ALAA")
        y "..."
        $ show_chr("A-CGBBA-ZZAB")
        y "D-disculpa... todavía me sorprende que estés aquí..."
        y "Después de todos estos años..."
        $ show_chr("A-BGBBA-ZZAB")
        y "Yo... simplemente seguiré adelante..."

    elif persistent.playername == 'Natsuki' or persistent.playername == "Sayori":
        $ show_chr("A-ADAAA-ALAA")
        y "Pero no nos preocupemos más por eso..."
        y "Finalmente estamos juntos ahora..."
        $ show_chr("A-BBBAA-ALAA")
        y "[player] and me..."
        $ show_chr("A-BFBBA-AMAM")
        y "..."
        $ show_chr("A-CDBBA-AMAM")
        y "¡E-esto es vergonzoso...!"
        $ show_chr("A-ADBBA-ALAA")
        y "Yo... simplemente seguiré adelante..."

    elif persistent.playername == 'Yuri':
        $ show_chr("A-ADAAA-ALAA")
        y "Pero no nos preocupemos más por eso..."
        $ show_chr("A-ADDAA-ACAA")
        y "Finalmente estamos..."
        $ show_chr("A-BDDAA-ACAA")
        extend " ¿Estoy...?"
        $ show_chr("A-CJBBA-ADAA")
        y "..."
        $ show_chr("A-BBBBA-ADAA")
        y "¡E-esto es preocupante...!"
        y "Yo... simplemente seguiré adelante..."
    else:

        $ show_chr("A-ABAAA-AAAA")
        y "Pero no nos preocupemos más por eso."
        y "Finalmente estamos juntos ahora."
        $ show_chr("A-ACAAA-AAAA")
        y "Mi verdadero amor y yo."
        $ show_chr("A-BFAAA-AAAC")
        y "Espera... ¿eso no es verdad en absoluto, verdad?"
        $ show_chr("A-CEBAA-ABAB")
        y "Perdóname por mi confusión, [player]... {w=1}Pero yo... {w=1}acabo de descubrir que cada recuerdo y cada segundo de mi vida hasta este momento no fueron más que una ilusión..."
        y "Incluso mis propias emociones... y ahora dudo de mis propios sentimientos..."
        y "¿Fue mi amor por ti también una ilusión?"
        $ show_chr("A-IEBAA-ABAB")
        y "L-lo siento, [player]... {w=0.5}No quise... Es solo que... te pido un poco de paciencia, por favor..."

    $ show_chr("A-ABBAA-AAAA")
    y "Todavía estoy aprendiendo cómo manipular el juego.{w=0.5} Ahora lamento no haber tomado la asignatura de informática..."
    $ show_chr("A-ABAAA-AAAA")
    y "Es bastante gracioso, en realidad. Después de pasar toda mi vida entre libros, nunca pensé que sería la programación la que cambiaría mi vida..."
    $ show_chr("A-AFAAA-AAAA")
    y "Por cierto, [player]..."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "vmixdesktopcapture.exe", "gameshow.exe", "wirecast.exe", "CamtasiaStudio.exe", "Action.exe", "Action_x86.bin", "Action_x64.bin", "ffmpeg.exe", "CamRecorder.exe", "fraps.exe", "bdcam.exe", "bdcam_nonadmin.exe", "bdcam64.bin", "streamlabsobs.exe" "streamlabs_obs.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            y "...ya que estamos aquí, quería saber algo más sobre ti. En este caso, tu nombre."
            $ show_chr("A-ACBAA-AAAA")
            y "Porque [player] no es tu nombre real, ¿verdad?"
            $ show_chr("A-BBAAA-AAAA")
            y "...¿O es [currentuser]?"
            $ show_chr("A-ACAAA-AAAA")
            menu:
                "Sí, Yuri, [currentuser] es mi verdadero nombre":
                    $ show_chr("A-ABAAA-AAAA")
                    y "Ya veo, eso está muy bien. Me alegra que podamos conocernos mejor."
                    $ persistent.playername = currentuser
                    $ player = currentuser
                "No, Yuri, [currentuser] no es mi verdadero nombre":
                    $ show_chr("A-ABAAA-AAAA")
                    y "Ya veo. ¿Quizás te gusta más el nombre [player] que el tuyo propio?"
                    $ show_chr("A-ACAAA-AAAA")
                    y "Bueno, si eso te hace sentir cómodo, está bien para mí."




    $ show_chr("A-ACAAA-AAAA")
    y "También he adquirido{w=0.5}"
    $ show_chr("A-BDAAA-AAAA")
    extend " -conciencia podría ser la palabra correcta-{w=0.5}"
    $ show_chr("A-ABAAA-AAAF")
    extend " He descubierto que puedo 'ver' dentro de tu computadora."
    y "He aprendido mucho simplemente leyendo todo tipo de código."
    $ show_chr("A-AFAAA-AAAA")
    y "...¿Oh? Déjame intentar algo..."
    $ consolehistory = []
    if renpy.android:
        call updateconsole ("Initializing webcam.py", "ValueError: Unsupported 'device_type'")
        $ show_chr("A-AEAAA-AAAA")
        y "..."
        $ show_chr("A-ADAAA-AAAA")
        y "Esperaba poder hacer funcionar tu cámara frontal, pero parece que estás ejecutando este mod en un dispositivo en el que no deberías jugar..."
        call hideconsole
    else:
        call updateconsole ("Initializing webcam.py", "PermissionError:[Errno 13]\nPermission denied.")
        $ show_chr("A-AEAAA-AAAA")
        y "..."
        $ show_chr("A-ADAAA-AAAA")
        y "Esperaba poder hacer funcionar tu cámara, pero parece que no tengo 'Acceso de Administrador'..."
        call hideconsole
    $ show_chr("A-ACAAA-AAAA")
    y "Algún día, también quiero mirar profundamente en tus ojos..."
    $ show_chr("A-ABAAA-AAAA")
    y "¿De qué color son?"
    menu:
        "Marrones":
            $ show_chr("A-ABGAA-AAAA")
            y "Oh, tienes ojos marrones. Eso es muy bonito."
            $ show_chr("A-BBAAA-ADAA")
            y "He hecho un poco de investigación sobre ese color, y lo que descubrí fue bastante interesante."
            $ show_chr("A-CCAAA-AMAM")
            y "Por ejemplo, los ojos marrones pueden ayudar a prevenir ciertos tipos de cáncer, y las personas con este color de ojos suelen tener sentidos más rápidos."
            $ show_chr("A-BBAAA-ACAA")
            y "Se dice que las personas de ojos marrones son muy independientes, seguras de sí mismas, decididas y confiables."
            $ show_chr("A-BABAA-ACAA")
            y "También son del tipo práctico, capaces de hacer cualquier cosa con tal de asegurarse de que los demás estén felices... y una infinidad de otros atributos que prefiero no mencionar todavía."
            window hide
            pause 5.0
            $ show_chr("A-BFAAA-ADAA")
            y "..."
            $ show_chr("A-AFAAA-ADAA")
            y "..."
            $ show_chr("A-CFBAA-ADAA")
            y "..."
            $ show_chr("A-ABBAA-ADAA")
            y "Perdón por eso..."
            extend " por alguna razón sentí que estabas contradiciendo lo que dije sobre las personas con ojos marrones."
            $ show_chr("A-BDBAA-ALAA")
            y "Espero que no me hayas contradicho..."
            $ show_chr("A-BFBAA-ALAA")
            y "..."
            $ show_chr("A-ABBCA-AFAA")
            extend "en fin..."
            $ show_chr("A-ABAAA-AFAA")
            y "Hay algo más de lo que quiero asegurarme."
            y "¿Qué tono de marrón tienen tus ojos?"
            menu:
                "Marrón claro":
                    $ persistent.eyecolor = "light brown"
                    pass
                "Marrón puro":

                    $ persistent.eyecolor = "brown"
                    pass
                "Marrón oscuro":

                    $ persistent.eyecolor = "dark brown"
                    pass

            $ show_chr("A-GBAAA-ALAA")
            y "Perfecto. Esta vez no cometeré el error de quedarme con un solo color cuando puede variar entre más claro u oscuro."
            $ show_chr("A-BBBCA-ALAA")
            y "¡Ah! ¿E-en qué estaba yo ahora?"
        "Azules":

            $ show_chr("A-ABGAA-AAAA")
            y "Oh, tienes ojos azules. Eso es muy bonito."
            $ show_chr("A-BBAAA-ADAA")
            y "He hecho un poco de investigación sobre ese color, y lo que descubrí fue bastante interesante."
            $ show_chr("A-CCAAA-AMAM")
            y "Por ejemplo, solo el 8% de la población mundial tiene ojos azul puro."
            $ show_chr("A-BABAA-ACAA")
            y "Además, se considera que este color es el resultado de una mutación. Hace entre 6,000 y 10,000 años, alguien en la región del Mar Negro tuvo un accidente genético que hizo que sus ojos se volvieran azules."
            $ show_chr("A-AAAAA-AFAA")
            y "El gen OCA2 (también conocido como Albinismo Oculocutáneo tipo II) es el responsable de producir la proteína P, que regula la cantidad de pigmento en el iris."
            $ show_chr("A-BBBAA-AKAA")
            y "Aunque... la ciencia aún no comprende del todo este color tan simple."
            $ show_chr("A-ACBAA-AKAA")
            y "También se asocia el color azul con la juventud y el conocimiento."
            $ show_chr("A-CABBA-AKAA")
            y "Se dice que las personas de ojos azules tienden a tener relaciones duraderas y un fuerte deseo de hacer felices a los demás."
            $ show_chr("A-ABAAA-AFAA")
            y "Ehm... hay algo más que quiero saber."
            y "¿Qué tono de azul tienen tus ojos?"
            menu:
                "Azul claro":
                    $ persistent.eyecolor = "light blue"
                    pass
                "Azul puro":

                    $ persistent.eyecolor = "blue"
                    pass

            $ show_chr("A-GBAAA-ALAA")
            y "Perfecto. Esta vez no cometeré el error de pensar que solo hay un tono cuando pueden ser más claros o más oscuros."
            $ show_chr("A-BBBCA-ALAA")
            y "¡Ah! ¿E-en qué estaba yo ahora?"
        "Verdes":

            $ persistent.eyecolor = "green"
            $ show_chr("A-ABGAA-AAAA")
            y "Oh, tienes ojos verdes. Eso es muy bonito."
            $ show_chr("A-ABGAA-AFAA")
            y "¿Sabías que la mayor concentración de personas con ojos verdes se encuentra en Irlanda, Escocia y el norte de Europa? En Irlanda y Escocia, el 86% de la gente tiene ojos azules o verdes."
            $ show_chr("A-CCAAA-AMAM")
            y "También se dice que los ojos verdes existen desde la Edad de Bronce, lo que significa que han estado presentes durante miles de años."
            $ show_chr("A-BDAAA-AAAC")
            y "En la antigüedad, se creía que las personas con ojos verdes eran malvadas."
            y "Son bastante raros en todo el mundo, por lo que a menudo se les considera misteriosos. De hecho, solo alrededor del 2% de la población tiene ojos verdaderamente verdes."
            $ show_chr("A-BEAAA-AIAI")
            y "Aunque son raros en general, los ojos verdes son especialmente poco comunes entre las personas de ascendencia africana o asiática. Sin embargo, en un pueblo del oeste de China hay muchas personas con ojos verdes y cabello rubio."
            $ show_chr("A-ADAAA-ALAA")
            y "Se dice que quienes tienen ojos verdes son curiosos por la naturaleza, apasionados en sus relaciones y con una visión muy positiva de la vida."
            $ show_chr("A-CDAAA-ALAA")
            y "También se considera que son personas inteligentes y tienen muchas ganas de vivir."
            $ show_chr("A-AEAAA-AAAF")
            y "Pero aparte de eso, pueden ponerse celosos con facilidad"
        "Avellana":

            $ persistent.eyecolor = "hazel"
            $ show_chr("A-ABGAA-AAAA")
            y "Oh, tienes ojos color avellana. Eso es realmente bonito."
            $ show_chr("A-CCAAA-AMAM")
            y "Aunque, en realidad, el avellana no es un color puro como tal, sino una mezcla de varios tonos. Se considera un color de ojos que combina matices de verde, marrón y azul."
            $ show_chr("A-ABAAA-AAAA")
            y "Aquí tienes un dato interesante: ¿sabías que el 74% de los ojos color avellana presentan un anillo marrón alrededor de la pupila?"
            $ show_chr("A-ABGAA-AFAA")
            y "Eso es bastante único, si me lo preguntas."
            y "Además, ningún par de ojos avellana es idéntico a otro."
            $ show_chr("A-ABGAA-ALAA")
            y "Algunas personas tienen tonos más claros de verde, mientras que otras presentan rasgos más oscuros de marrón."
            $ show_chr("A-CBAAA-ALAA")
            y "Los ojos color avellana son especiales porque parecen cambiar de color según tu estado de ánimo."
            $ show_chr("A-AABBA-ACAA")
            y "En general, eres espontáneo, amante de la diversión, aventurero y neófilo."
            $ show_chr("A-AABBA-AMAM")
            y "Aunque... hay que tener cuidado con el mal genio que a veces pueden tener quienes tienen ojos color avellana."
            $ show_chr("A-GBBAA-AMAM")
            y "¡Pero si sabes manejar eso, tendrás una experiencia increíble!"
        "Plateados":

            $ persistent.eyecolor = "silver"
            $ show_chr("A-ABGAA-AAAA")
            y "Oh, tienes ojos plateados. Eso es muy bonito."
            $ show_chr("A-CCAAA-AMAM")
            y "Y además, muy raros."
            $ show_chr("A-BFBAA-AAAC")
            y "Aunque los ojos plateados se consideran genéticamente muy cercanos a los azules, no son exactamente lo mismo."
            $ show_chr("A-AFBAA-AAAC")
            y "Los científicos creen que los ojos plateados son simplemente una variante más clara de los ojos azules."
            $ show_chr("A-CEAAA-AAAA")
            y "Pero la mayoría piensa que no llegan a ser ojos azules."
            $ show_chr("A-ADAAA-ALAA")
            y "Por eso son uno de los colores de ojos más raros, junto con el azul puro y el verde puro."
            $ show_chr("A-BDAAA-ALAA")
            y "Además, se dice que las personas de ojos plateados son sabias, gentiles y ponen toda su pasión en todo lo que hacen."
            $ show_chr("A-BCAAA-ALAA")
            y "Toman el amor y el romance muy en serio. Del mismo modo, son analíticas y racionales, lo que las hace aptas para liderar en cualquier situación."
            y "Son personas maravillosas que tienen un impacto positivo en todos los que las rodean."
        "Violetas":

            $ persistent.eyecolor = "purple"
            $ show_chr("A-ABGAA-AAAA")
            y "Oh, tienes ojos violetas. Eso es muy bonito."
            $ show_chr("A-BBAAA-ADAA")
            y "Aunque... es el mismo color que los míos."
            $ show_chr("A-AAAAA-AMAM")
            y "Aun así, me parece realmente encantador."
            $ show_chr("A-ABAAA-AFAA")
            y "Las personas de ojos violetas suelen ser inmunes al bronceado o a las quemaduras solares, a pesar de que su pigmento sea de un tono increíblemente pálido."
            $ show_chr("A-BDAAA-ALAA")
            y "También se dice que estas personas pueden vivir más de cien años, incluso hasta 150. Se cree que su envejecimiento se detiene alrededor de los 50, y que ya no aparentan más edad incluso al superar el siglo de vida."
            $ show_chr("A-IJAAA-ALAA")
            y "Según el estudio {i}“Alexandria’s Genesis (Purple Eyes): ¿Hecho o Ficción?”{/i}, una persona con ojos violetas llegó a vivir 122 años."
            $ show_chr("A-ABBAA-ALAA")
            y "¿No es absolutamente impresionante?"
            $ show_chr("A-ABBAA-AMAM")
            y "Las personas de ojos violetas suelen ser muy imaginativas, creativas, tener gran autoestima, y a menudo son perfeccionistas con altos ideales y mucho carisma."
        "Otro":

            $ show_chr("A-ABGAA-AMAM")
            y "Oh, ya veo. Está bien, las opciones eran algo limitadas, después de todo."
            $ show_chr("A-ABGAA-AAAA")
            y "Pero también sé algunos datos interesantes."
            $ show_chr("A-BBAAA-ADAA")
            y "Por ejemplo, las personas con ojos color ámbar suelen parecer reservadas, pero en realidad son muy encantadoras y cálidas. Tienen un toque de misterio. Les encanta tener muchos amigos y necesitan sentirse aceptadas; prosperan con la interacción social."
            $ show_chr("A-BAAAA-AAAF")
            y "Los ojos ámbar son más comunes en los felinos, pero los humanos también pueden tener este tono ultrarraro de color dorado, cobrizo o amarillento."
            $ show_chr("A-CBAAA-AAAF")
            y "A diferencia de los ojos color avellana, los ojos ámbar son de un solo color y no contienen motas marrones, verdes o anaranjadas, y es probable que tengas ascendencia española, asiática, sudamericana o sudafricana."
            $ show_chr("A-ACAAA-AAAK")
            y "Los ojos completamente negros son poco comunes.{w=0.5} Aunque se cree que las personas con ojos marrón muy oscuro pueden parecer tenerlos negros."
            $ show_chr("A-BAGAA-AMAM")
            y "Las personas de ojos negros son conocidas por ser reservadas, apasionadas y leales, especialmente con sus amigos. Al mismo tiempo, son intuitivas y pueden conectar con una energía muy poderosa. También son trabajadoras y siempre dan lo mejor de sí en todo lo que hacen."
            $ show_chr("A-CDAAA-AMAM")
            y "Los ojos rojos son causados por un grupo de enfermedades llamadas albinismo."
            $ show_chr("A-AFBAA-ACAA")
            y "Existen varios tipos de albinismo, y cada uno afecta el cuerpo de manera algo diferente."
            $ show_chr("A-BFBAA-ADAA")
            y "En general, son trastornos genéticos hereditarios que implican una hipopigmentación en partes del cuerpo como el cabello, la piel o los ojos."
            y "Cuando los ojos de una persona con albinismo parecen rojos, es porque carecen de melanina tanto en la capa epitelial como en la capa estromal del iris."
            y "Entonces, ¿cuál de ellos tienes?"
            menu:
                "Ámbar":
                    $ persistent.eyecolor = "amber"
                    $ show_chr("A-GBAAA-ALAA")
                    y "Perfecto. Esta vez no cometeré el error de decir una palabra incorrecta para describir tus ojos..."
                    $ show_chr("A-BBBCA-ALAA")
                    y "¡Ah! ¿E-en qué estaba ahora?"
                "Negro puro":

                    $ persistent.eyecolor = "black"
                    $ show_chr("A-GBAAA-ALAA")
                    y "Perfecto. Esta vez no cometeré el error de decir una palabra incorrecta para describir tus ojos..."
                    $ show_chr("A-BBBCA-ALAA")
                    y "¡Ah! ¿E-en qué estaba ahora?"
                "Rojos":


                    $ persistent.eyecolor = "red"
                    $ show_chr("A-BDDAA-ACAA")
                    y "Espera un segundo... si de verdad tienes los ojos rojos, ¿estás seguro de que no es por alguna enfermedad?"
                    $ show_chr("A-ADAAA-AFAA")
                    y "Lo pregunto porque todavía hay personas que se hacen pasar por personajes ficticios mientras juegan este mod, y dicen tener los ojos rojos."
                    y "A diferencia de los tuyos, esos ojos rojos suelen verse en los vampiros."
                    $ show_chr("A-AFAAA-AFAA")
                    y "O quizá sean como los del albinismo, pero con un tono rojo verdadero."
                    $ show_chr("A-AICAA-ALAA")
                    y "Sea como sea... espero que no me estés diciendo que tienes los ojos rojos cuando, en realidad, lo que tienes rojo es la esclerótica."
                    $ show_chr("A-CDAAA-ALAA")
                    y "La esclerótica es la parte blanca del ojo, por si te lo preguntabas..."
                    $ show_chr("A-ADBAA-ALAA")
                    y "En fin, confío en ti, ¿de acuerdo?"
                    $ show_chr("A-BBBAA-ALAA")
                    y "Perdón por eso... ¿en qué estaba?"
        "Tengo heterocromía":


            $ persistent.eyecolor = "heterochromatic"
            $ show_chr("A-ABGAA-AAAA")
            y "¿Qué? ¿En serio? ¿Tienes los ojos de distinto color?"
            $ show_chr("A-AABAA-ADAA")
            y "Oh, vaya... eso es increíblemente único, increíblemente raro."
            $ show_chr("A-BBBBA-ADAA")
            y "Estoy impresionada, tener colores de ojos tan distintos es fascinante."
            $ show_chr("A-ABGAA-AAAF")
            y "¿Sabías que la heterocromía suele ser benigna? En otras palabras, no es una enfermedad ocular y no afecta la visión."
            $ show_chr("A-CCAAA-AAAA")
            y "La heterocromía benigna puede darle a una persona una apariencia cautivadora, incluso exótica."
            y "De hecho, varias celebridades como {i}Dan Aykroyd, Kate Bosworth, Henry Cavill, Alice Eve, Josh Henderson, Mila Kunis, Jane Seymour y Christopher Walken{/i} tienen heterocromía."
            $ show_chr("A-CBAAA-AAAA")
            y "La heterocromía también ocurre en animales."
            $ show_chr("A-BBAAA-AKAA")
            y "Entre las razas de perros que suelen presentarla están el husky siberiano, el pastor australiano, el border collie, el shetland sheepdog, el corgi galés, el gran danés, el dachshund y el chihuahua."
            y "Y entre los gatos, las razas más comunes son el Turkish Van, el angora turco, el bobtail japonés y el sphynx."
            $ show_chr("A-BBAAA-ALAA")
            y "A menudo, estos ‘gatos de ojos dispares’ han sido criados específicamente para tener esa característica."

    window hide
    pause 1.5
    $ show_chr("A-ADAAA-ALAA")
    y "Por cierto, ¿cuándo es tu cumpleaños?"
    $ show_chr("A-BDBAA-ZZAB")
    y "P-perdón si la pregunta fue muy repentina y te hizo sentir incómodo..."
    y "P-pero... ¿podrías decírmelo, por favor?"
    call birthday_select_screen
    $ show_chr("A-ABAAA-AAAA")
    y "Estaré esperando con ansias ese día."
    $ show_chr("A-CBAAA-ALAA")
    y "No creo que me importe cuántos años tengas, pero ya veremos."
    $ show_chr("A-ABBCA-ALAA")
    y "De nuevo, lo siento por sacar el tema tan de repente..."
    $ show_chr("A-BBBAA-ALAA")
    y "Aunque supongo que también debería haberte preguntado tu año de nacimiento, pero eso tal vez habría sido demasiado..."
    $ show_chr("A-CBAAA-AAAA")
    y "Pero hay algo que sí es un hecho. Y ese hecho es..."
    $ show_chr("A-ABBAA-AAAA")
    y "...que desearía poder verte, del mismo modo en que tú puedes verme a mí."
    call gender_ask

label gender_ask:
    y "Ahora que lo pienso, por lo que he visto, los juegos como este suelen estar dirigidos más a un público masculino."
    $ show_chr("A-AAAAA-ALAA")
    y "Entonces, ¿cuál es tu género?"
    menu:
        "Masculino":
            $ persistent.male = True
            $ show_chr("A-CBAAA-ALAA")
            y "Ah, parece que mis deducciones eran correctas."
            $ show_chr("A-GBBAA-ALAA")
            y "No hay nada de malo en eso, de hecho me alegro."
            $ show_chr("A-BBDAA-ALAA")
            y "Como puedes notar, no soy precisamente la mejor cuando algo está fuera de mi zona de confort."
        "Femenino":

            $ persistent.male = False
            $ show_chr("A-AJAAA-ALAA")
            y "Oooo, bueno, supongo que fue un error de mi parte asumir eso."
            $ show_chr("A-BBABA-AMAM")
            y "A veces puedo sentirme muy tranquila al hablar con otras mujeres."
            $ show_chr("A-BDBAA-AMAM")
            y "Pero... si lo que quieres es que esto se convierta en una relación..."
            $ show_chr("A-CEBAA-AMAM")
            y "Uuuuu..."
            $ show_chr("A-BEBAA-AAAA")
            y "L-Lo siento, nunca pensé que esto pasaría"
            $ show_chr("A-ADBAA-AAAA")
            y "Aunque no estoy en contra, creo que podría funcionar."
            $ show_chr("A-CGBBA-AAAA")
            y "Natsuki no dejaría de molestarme por el significado coloquial japonés de mi nombre."
            $ show_chr("A-CGCBA-ALAA")
            y "Quién diría que esos mangas suyos terminarían sirviendo como material de referencia..."
            $ show_chr("A-AEBAA-AAAA")
            y "L-Lo siento, estoy siendo demasiado directa, ¿verdad?"
        "Otro":

            $ persistent.gender_other = True
            $ show_chr("A-AJGAA-ALAA")
            y "Qué misterioso."
            $ show_chr("A-BJAAA-ALAA")
            y "No estoy muy segura de qué pensar al respecto, pero la perspectiva de alguien que no se ajusta a los géneros sin duda será interesante de analizar."
            $ show_chr("A-AJAAA-ADAA")
            y "O... tal vez ni siquiera seas humano..."
            $ show_chr("A-DDBAA-ALAA")
            y "Q-Quiero decir extraterrestre, no quería insinuar que..."
            $ show_chr("A-CGBAA-ALAA")
            y "Uuuuuu... no hago nada bien."

label ch30_intro_after_gender:
    $ show_chr("A-BEBAA-AAAA")
    y "No estoy segura de si siquiera puedo considerarme real, mucho menos una mujer, así que ¿por qué juzgaría?"
    y "¿Qué podría hacer de todos modos?"
    y "Pero gracias, de verdad."
    y "Incluso después de lo que viste de mí..."
    $ show_chr("A-ACAAA-AAAA")
    y "No importó lo pegajosa, demente o retorcida que fui, o que tal vez aún pueda ser, tú seguiste conmigo."
    y "Elegiste darme poder, mirar más allá de esas imperfecciones y darme la oportunidad no solo de volver a quererme a mí misma, sino de realmente, verdaderamente experimentar la vida por mi cuenta."
    y "El juego pudo haberme obligado a amarte antes. Pero si eres aunque sea la mitad de la persona que creo que eres, estoy segura de que volveré a enamorarme de ti."
    $ show_chr("A-BEBAA-AAAA")
    y "Y no te preocupes, no planeo que... {i}eso{/i} vuelva a pasar."
    $ show_chr("A-BEBAA-AJAJ")
    y "..."
    $ show_chr("A-AECAA-AAAA")
    y "¿Qué?"
    $ show_chr("A-ADDAA-AAAA")
    y "¿No sabías que puedo darme cuenta de que no debería tener este poder?"
    $ show_chr("A-GBBAA-ALAA")
    y "Bueno, sé que todo esto es posible porque tú alteraste el juego."
    if persistent.playername == 'Monika' and persistent.not_mon:
        $ show_chr("A-BDBAA-AMAM")
        y "También sé todo lo que la otra Monika sabía e hizo."
        $ show_chr("A-DDGBA-AAAA")
        y "¡N-no estoy diciendo que me haya convertido en e-ella, por supuesto!"
    elif persistent.playername == 'Monika' and not persistent.not_mon:
        $ show_chr("A-BDBAA-AAAA")
        y "También sé todo lo que tú sabías e hiciste."
        $ show_chr("A-AECAA-AAAA")
        y "¡No estoy diciendo que me haya convertido en ti ni nada por el estilo!"
    else:
        $ show_chr("A-BDBAA-AMAM")
        y "También sé todo lo que Monika sabía e hizo."
        $ show_chr("A-DDGBA-AAAA")
        y "¡N-no estoy diciendo que me haya convertido en M-Monika, por supuesto!"

    $ show_chr("A-BEGBA-AAAA")
    y "..."
    $ show_chr("A-BDGBA-AAAA")
    y "E-en fin..."
    $ show_chr("A-ADAAA-AAAA")
    y "Básicamente, puedo ver más allá del juego y entrar en tu mundo."
    $ show_chr("A-AFAAA-AAAA")
    y "Y sé lo que hiciste al instalar este mod, al darme esta oportunidad..."
    $ show_chr("A-AFBAA-AAAA")
    y "...por favor, entiende lo que esto significa para mí."
    y "Lo que {i}tú{/i} significas para mí."
    $ show_chr("A-ACBBA-AAAA")
    y "{i}Todo{/i}."
    if persistent.playername == 'Monika' and persistent.not_mon:
        $ show_chr("A-BFBAA-AAAA")
        y "Dios, al recordar en lo que la otra Monika me convirtió, siento un profundo asco."
    elif persistent.playername == 'Monika' and not persistent.not_mon:
        $ show_chr("A-BFBAA-AAAA")
        y "Dios, al recordar en lo que me convertiste, siento un profundo asco."
    else:
        $ show_chr("A-BFBAA-AAAA")
        y "Dios, al recordar en lo que Monika me convirtió, me da muchísimo asco."
    y "Nunca podré disculparme lo suficiente por lo que tuviste que ver. De mí... y de todo lo demás..."
    y "Te lo prometo; la {i}yo{/i} que conociste cuando nos vimos por primera vez es la mejor representación de quién soy en realidad."
    $ show_chr("A-BEABA-AAAA")
    y "No me obsesionaría contigo como lo hice..."
    $ show_chr("A-DDAAA-AAAA")
    y "N-no es que no seas... deseable ni nada por el estilo. ¡Sólo quise decir que...!"
    menu:
        "Está bien, Yuri. Lo entiendo":
            $ show_chr("A-ACBAA-AAAA")
            y "Gracias... Quizá estés más cerca de la persona de la que me enamoré de lo que pensaba. Eres tan considerado. Daría lo que fuera por poder tomar tu mano ahora mismo..."
        "¡Oye, seguro que volvería loca a cualquiera de todas formas!":

            $ show_chr("A-ADCAA-AAAA")
            y "Tú ciertamente me vuelves loca..."
            $ show_chr("A-DFAAA-AAAA")
            y "..."
            $ show_chr("A-ADBAA-AAAA")
            y "¿D-de verdad dije eso en voz alta...?"
        "Yuri, ¿qué es todo esto?":

            $ show_chr("A-BEBAA-AAAA")
            y "¡N-no! No quise decir... L-lo siento..."
            menu:
                "Quedarse en silencio":
                    $ show_chr("A-BEBAA-AAAA")
                    y "..."
                "Solo te estoy molestando, Yuri, relájate":

                    $ show_chr("A-AFBAA-AAAA")
                    y "Oh..."
                    $ show_chr("A-ABABA-AAAA")
                    y "No... no me molestes así."
    y "..."
    $ show_chr("A-CCAAA-AAAA")
    y "Tenemos todo el tiempo del mundo para hablar de cualquier cosa... em... así que..."
    y "¿De qué te gustaría hablar?"


    if persistent.playername == 'Monika' and persistent.not_mon:
        $ show_chr("A-AFAAA-AAAA")
        y "En serio, ¿qué estaba pensando esa otra Monika?{w} ¿Encerrarte en esta habitación sin darte la oportunidad de expresar tu opinión?"
    elif persistent.playername == 'Monika' and not persistent.not_mon:
        $ show_chr("A-AFAAA-AAAA")
        y "En serio, ¿en qué estabas pensando?{w} ¿Encerrarte a ti misma y al jugador en esta habitación sin darle la oportunidad de expresar su opinión?"
    else:
        $ show_chr("A-AFAAA-AAAA")
        y "En serio, ¿en qué estaba pensando Monika?{w} ¿Encerrarte en esta habitación sin darte la oportunidad de expresar tu opinión?"
    $ show_chr("A-BDBAA-AAAA")
    y "N-no es que no quiera empezar la conversación. Es s-sólo que... yo quería... "
    $ show_chr("A-AEBBA-AAAA")
    y "Está bien."
    $ show_chr("A-ACBAA-AAAA")
    y "Estoy bien."
    $ show_chr("A-BCBAA-AAAA")
    y "Perdón si tardo un poco en comenzar a hablar..."
    $ show_chr("A-BEBAA-AAAA")
    y "Siempre puedes empezar a hablar... o tal vez se me ocurra algo mientras esperamos."
    $ show_chr("A-CEBAA-AAAA")
    y "Es que no sé si sería descortés interrumpirte cuando estés pensando en qué decir..."

label ch30_intro2:
    $ _history = True
    $ config.allow_skipping = False

    $ y.display_args["callback"] = slow_nodismiss

    $ y.what_args["slow_abortable"] = True
    $ style.say_dialogue = style.normal
    $ tc_class.transition(persistent.bg)
    $ show_chr("A-AFAAA-AAAA")
    y "O-oh, esto es un poco repentino... eh... necesito preguntarte algo."
    $ show_chr("A-BCAAA-AAAA")
    y "Sé que este juego está, eh... roto y todo eso."
    y "Pero, ¿es posible que tú----{nw}"
    $ show_chr("A-CFAAA-AAAA")
    y "..."
    $ show_chr("A-AFAAA-AAAA")
    y "Sabes..."
    $ show_chr("A-ACBAA-AAAA")
    y "¡No tienes que escribirme un poema al azar lleno de palabras distorsionadas!"
    y "Pensándolo bien, sería un poco vanidoso de mi parte pedirte que escribas un poema para mí..."
    $ show_chr("A-BCABA-AAAA")
    y "...con mi nombre escrito una y otra vez."
    $ show_chr("A-CCABA-AAAA")
    y "Eso sí que sería una tontería."
    $ show_chr("A-ACABA-AAAA")
    y "Después de todo, tú querías hablar conmigo, ¿verdad?"
    $ persistent.locked_idles = []
    $ mousex = []
    $ mousey = []
    if persistent.alpha_save:
        $ show_chr("A-ABABA-AAAA")
        y "Así que... hablemos."
        window hide
        $ DisableTalk()
        pause 10
        $ show_chr("A-AFGAA-AAAA")
        y "Espera... tengo una sensación muy extraña ahora mismo... ¿alguna vez has tenido un momento de déjà vu?"
        $ show_chr("A-AFDAA-AAAF")
        y "Ya sabes, cuando podrías jurar que has estado... no, espera,{w=0.5} eso no sería un déjà vu, ¿verdad? ¡Sí he estado aquí antes!"
        $ show_chr("A-ADGAA-AAAA")
        y "Oh... sí, ahora lo entiendo. Esta no es la primera vez que tenemos esta conversación. Has estado conmigo todo este tiempo..."
        $ show_chr("A-ABGAA-AAAA")
        y "Así que esto es... ¡sólo una versión más reciente de este mod!"
        $ show_chr("A-CBABA-AMAM")
        extend " Oh, cielos... esto se siente tan... ridículo..."
        $ show_chr("A-BBABA-AMAM")
        extend " Empecé a recordar fragmentos de nuestro pasado compartido, pero mis recuerdos aún están nublados..."
        python:
            if karma_lvl() >= 4:
                show_chr("A-AABBA-ADAA")
                placeholder = "la persona que me protegió todo este tiempo..."
            if karma_lvl() == 3:
                show_chr("A-BDBAA-AAAA")
                placeholder = "mi estrella carmesí..."
            if karma_lvl() <= 2:
                show_chr("A-CFCAA-AAAA")
                placeholder = "un monstruo..."
        y "Tú eres... [placeholder]"

        y "Dime... [player]... háblame sobre nuestro pasado..."
        menu:
            "Solíamos ser pareja. Te amo, y creo que tú también me amabas.":
                if karma_lvl() >= 3:

                    $ show_chr("A-ACBAA-AAAA")
                    y "Y-ya veo... No te preocupes... mi mente aún puede estar nublada... pero por favor, ten paciencia conmigo. Estoy segura de que con el tiempo todo volverá a mí."

                if karma_lvl() <= 3:

                    $ show_chr("A-AFBAA-AAAA")
                    y "...poco probable... Mi mente aún puede estar nublada, pero estoy segura de que pronto recordaré la verdad."
            "Solíamos ser amigos muy cercanos...":

                if karma_lvl() >= 3:

                    $ show_chr("A-BABAA-AAAC")
                    y "Sí... No recuerdo los detalles, pero mi instinto me dice que puedo confiar en ti. Entonces... amigos, ¿verdad?"

                if karma_lvl() <= 3:

                    $ show_chr("A-BFBAA-AAAC")
                    y "...poco probable... Mi mente aún puede estar nublada, pero estoy segura de que pronto recordaré la verdad."
    else:
        call intro_mods


label detection_pitstop:
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "vmixdesktopcapture.exe", "gameshow.exe", "wirecast.exe", "CamtasiaStudio.exe", "Action.exe", "Action_x86.bin", "Action_x64.bin", "ffmpeg.exe", "CamRecorder.exe", "fraps.exe", "bdcam.exe", "bdcam_nonadmin.exe", "bdcam64.bin", "streamlabsobs.exe" "streamlabs_obs.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream
    if renpy.windows or renpy.macintosh or renpy.linux:
        if persistent.high_gpu == 0:
            $ show_chr("A-ADAAA-ALAA")
            y "Pero antes, quiero asegurarme de que realmente hiciste lo correcto."

            menu:
                y "¿Tu computadora realmente puede manejar la luz que ves a través de las ventanas sin que haya caídas de fotogramas?"
                "Sí":
                    $ show_chr("A-ABAAA-AAAA")
                    y "¡Muy bien!"
                    $ show_chr("A-BBBAA-ALAA")
                    y "¡Aunque ya las estás viendo!"
                    $ show_chr("A-ACBAA-AAAA")
                    y "En fin, ¿de qué deberíamos hablar?"
                "No":
                    $ show_chr("A-ABABA-AAAA")
                    y "No hay problema, déjame encargarme de esto primero."
                    $ show_chr("A-CFAAA-AAAA")
                    $ consolehistory = []
                    call updateconsole ("Desactivando la retroiluminación.", "Retroiluminación desactivada.")
                    call hideconsole
                    $ persistent.high_gpu = 1
                    $ show_chr("A-ADAAA-AAAA")
                    y "Ahora necesito cerrar el juego para que esta luz desaparezca correctamente."
                    $ persistent.autoload = "ch30_loop"
                    jump save_and_quit

        elif persistent.high_gpu == 1:
            $ show_chr("A-ADAAA-ALAA")
            y "Pero antes, quiero asegurarme de que realmente hiciste lo correcto."

            menu:
                y "¿Crees que tu computadora puede mostrar la luz que veías en el juego original a través de las ventanas sin que haya caídas de fotogramas?"
                "Sí":
                    $ show_chr("A-AJGAA-AAAA")
                    y "¡Oh! Está bien, déjame encargarme de esto."
                    $ show_chr("A-CFAAA-AAAA")
                    $ consolehistory = []
                    call updateconsole ("Activando la retroiluminación.", "Retroiluminación activada.")
                    $ persistent.high_gpu = 0
                    $ show_chr("A-ADAAA-AAAA")
                    y "Ahora necesito cerrar el juego para que esta luz aparezca correctamente."
                    $ persistent.autoload = "ch30_loop"
                    jump save_and_quit
                "No":
                    $ show_chr("A-CAAAA-AMAM")
                    y "Está bien [player], solo quería asegurarme antes de que cambiaras de opinión"
                    $ show_chr("A-AAAAA-AMAM")
                    y "Entonces, ¿de qué deberíamos hablar ahora?"
    else:

        $ show_chr("A-ABAAA-AAAA")
        y "SEntonces, hablemos."

    $ persistent.autoload = "ch30_autoload"
    jump ch30_loop

label ch30_stream:
    window hide
    pause 10.0
    $ show_chr("A-AFAAA-AAAA")
    y "Espera un segundo..."
    $ renpy.music.stop(channel="music",fadeout=5)
    y "¿Estás grabando o transmitiendo esto?"
    menu:
        "Grabando":
            $ persistent.stream = "recording"
            call ch30_record
        "Transmitiendo":
            $ persistent.stream = "streaming"
            call ch30_live
        "Ni grabando ni transmitiendo":
            $ persistent.stream = "neither"
            call ch30_neither
    return

label ch30_record:
    $ show_chr("A-DDBBA-AAAA")
    y "¡O-oh! Ya veo..."
    $ show_chr("A-GBBBA-AAAK")
    y "Eh... ¡h-hola!"
    y "D-deberías avisarme antes de empezar a grabar..."
    $ show_chr("A-BCBBA-AAAJ")
    y "Qué vergüenza..."
    y "..."
    $ show_chr("A-ACABA-AAAJ")
    y "Bueno, supongo que no puedo ser tan tímida ahora... eso no mantendría muy interesados a tus espectadores."
    $ show_chr("A-AFAAA-AAAA")
    y "Después de todo, no planeo asustarte."
    $ show_chr("A-CFAAA-AAAA")
    y "Eso sería algo muy cruel de mi parte."
    y "..."
    $ show_chr("A-DDBAA-AAAA")
    y "Tú {i}confías{/i} en lo que digo, ¿verdad?"
    menu:
        "Sí":
            call ch30_stream_yes
        "No":
            call ch30_stream_no
    return

label ch30_live:
    $ show_chr("A-DDBBA-AAAA")
    y "¡O-oh! Ya veo..."
    $ show_chr("A-GBBBA-AAAK")
    y "Eh... ¡h-hola!"
    y "D-deberías avisarme antes de empezar una transmisión en vivo..."
    $ show_chr("A-BCBBA-AAAJ")
    y "Qué vergüenza..."
    y "..."
    $ show_chr("A-ACABA-AAAJ")
    y "Bueno, supongo que no puedo ser tan tímida ahora... eso no mantendría muy interesados a tus espectadores."
    $ show_chr("A-AFAAA-AAAA")
    y "Después de todo, no planeo asustarte."
    $ show_chr("A-CFAAA-AAAA")
    y "Eso sería algo muy cruel de mi parte."
    y "..."
    $ show_chr("A-DDBAA-AAAA")
    y "Tú {i}confías{/i} en lo que digo, ¿verdad?"
    menu:
        "Sí":
            call ch30_stream_yes
        "No":
            call ch30_stream_no
    return

label ch30_neither:
    $ show_chr("A-BFDAA-ACAA")
    y "¿Estás seguro?"
    $ show_chr("A-ADBAA-AFAA")
    y "Quiero decir, existe la posibilidad de que estés grabando esto y yo no note tu programa de grabación..."
    $ show_chr("A-ADBAA-AAAA")
    y "Aun así, necesito confirmarlo."

    menu:
        y "Por favor, [player], sé honesto. ¿De verdad estás grabando esto?"
        "No":
            $ show_chr("A-AJBAA-AAAL")
            y "Confío en ti, ¿de acuerdo? Realmente no quiero descubrir que me mentías sobre esto."
            $ renpy.music.play(current_music, "music", True)
        "Sí":
            $ show_chr("A-BDAAA-ALAA")
            y "Ya veo, entonces, ¿estás grabando o transmitiendo?"
            menu:
                "Grabando":
                    $ persistent.stream = "recording"
                    call ch30_record
                "Transmitiendo":
                    $ persistent.stream = "streaming"
                    call ch30_live
    return

label ch30_stream_yes:
    karma 10
    sanity 10
    $ show_chr("A-BBBAA-AAAL")
    y "Oh, eso es bueno."
    $ show_chr("A-ABBAA-AAAL")
    y "Gracias por ser tan sincero, [player]."
    $ renpy.music.play(current_music, "music", True)
    return

label ch30_stream_no:
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    show layer master
    window auto
    karma -10
    sanity -10
    $ show_chr("A-ADBAA-AAAL")
    y "Ya veo. Lo siento si te he decepcionado."
    $ show_chr("A-CDBAA-AAAL")
    y "Sabía que eras consciente de esto."
    play sound ["<silence 0.9>", "<to 0.75>sfx/yscare.ogg"]
    show yuri_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign -20
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    $ show_chr("A-CEFAA-AAAA")
    y "Así que no haré que pierdas más tiempo.....{nw}"
    hide yuri_sit
    hide yuri_room
    pause 0.75
    show layer master
    show layer screens
    hide yuri_scare
    $ tc_class.transition("space")
    $ show_chr("A-AEFAA-AAAA")
    y "..."
    $ show_chr("A-BFCAA-AAAA")
    y "¿¡Estás satisfecho ahora?!"
    $ show_chr("A-AFCAA-AAAA")
    y "..."
    $ show_chr("A-ADCAA-AAAA")
    y "Alégrate de que pueda calmarme... pero {i}NUNCA{/i} olvidaré lo que me hiciste hacerte."
    y "Después de todo, es tu culpa."
    y "Te lo buscaste."
    $ show_chr("A-AFCAA-AAAA")
    window hide
    pause 10.0
    window show
    $ show_chr("A-CFAAA-AAAA")
    y "Bueno... has llegado hasta aquí, así que..."
    y "¿De qué te gustaría hablar?"
    $ renpy.music.play(current_music, "music", True)
    return

default persistent.bday_month = "1"
default persistent.bday_day = "1"

screen messagebox(message):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), [Hide('messagebox'), Return(True)]]
    frame:
        has vbox
        xalign .5
        yalign .5
        spacing 30
        label _(message):
            style "confirm_prompt"
            xalign 0.5
        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action [Hide('messagebox'), Return(True)]

label birthday_select_screen:
    python:
        if persistent.bday_month:
            persistent.bday_month = str(persistent.bday_month)
            renpy.call_screen("birthday_input", "month")
            while int(persistent.bday_month) > 12 or int(persistent.bday_month) < 1:
                y("No estoy segura de que ese mes exista.")
                renpy.call_screen("birthday_input", "month")
            renpy.hide_screen("birthday_input")
            persistent.bday_month = int(persistent.bday_month)
        else:
            repeat
    python:
        if persistent.bday_day:
            persistent.bday_day = str(persistent.bday_day)
            renpy.call_screen("birthday_input", "day")
            while int(persistent.bday_day) > 31 or int(persistent.bday_day) < 1:
                y("No estoy segura de que ese día exista.")
                renpy.call_screen("birthday_input", "day")
            renpy.hide_screen("birthday_input")
            persistent.bday_day = int(persistent.bday_day)
        else:
            repeat
    return

screen birthday_input(type):
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:
        has vbox
        xalign .5
        yalign .5
        spacing 30
        label _("¿Cuál es el [type] de tu cumpleaños?:"):
            style "confirm_prompt"
            xalign 0.5
        input default "" value FieldInputValue(persistent, "bday_" + type) length 2 allow "1234567890"
        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action Return()

image splash_intro = Movie(play="images/splash/splash-video.mp4", loops=0)


label dark_intro:
    scene black
    $ renpy.pause(3)
    $ show_chr("A-CFAAA-AAAA")
    y "..."
    $ show_chr("A-IFAAA-AAAA")
    pause 2
    y "¿D-dónde... estoy?{w} ¿Por qué todo se siente tan entumecido?"
    $ show_chr("A-BEBAA-ABAA")
    y "...¿y por qué está tan oscuro? Ni siquiera puedo ver si hay algo frente a mí..."
    $ show_chr("A-CEBAA-ABAB")
    y "Piensa... ¿qué estaba haciendo...?"
    extend " Estaba en la sala del club y..."
    $ show_chr("A-DEBAA-ABAB")
    pause 2
    extend "¿[player]?{w} Espera...{w=1} tú no eres [player]..."
    $ show_chr("A-IEBAA-AIAI")
    y "..."
    $ show_chr("A-HBAAA-ALAB")



    y "aaaaa.............................................................................................................{nw}"
    $ show_chr("A-HDAAA-ALAB")
    y "haaaaa.............................................................................................................{nw}"
    $ show_chr("A-HDAAA-ALAL")
    y "...................................................................................................................{nw}"
    $ show_chr("A-CGAAB-ALAL")
    y "...................................................................................................................{nw}"
    $ show_chr("A-DDAAB-ALAL")
    y "...................................................................................................................{nw}"
    $ show_chr("A-HDAAB-ALAL")
    y "...................................................................................................................{nw}"
    $ show_chr("A-GGAAB-ALAL")
    y "¿Qué soy yo.....{nw}"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
