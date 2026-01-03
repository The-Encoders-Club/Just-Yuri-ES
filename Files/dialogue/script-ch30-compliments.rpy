
label compliment_menu:
    python:

        compliment_dict = [
            ["Solo quería decirte cuánto disfruto nuestro tiempo juntos, [persistent.yuri_nickname].", "c1"],
            ["[persistent.yuri_nickname], eres tan hermosa como la luna naciente...", "c2"],
            ["Realmente me animas, [persistent.yuri_nickname].", "c3"],
            ["¡Creo que eres muy inteligente!", "c4"],
            ["Realmente sabes cómo tocar mi corazón...", "c5"],
            ["¡Debo decir, eres bastante ardiente!", "c6"],
            ["¡Realmente me enorgulleces!", "c7"],
            ["Olvídalo.", "ch30_loop"]]
        renpy.call_screen("compliments", compliment_dict)
    jump ch30_loop


screen compliments(items):
    style_prefix "choice"

    fixed:
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            side_yfill True

            has vbox
            for i in items:
                textbutton i[0] action Call("compliment_time_log", i[1]) xpos 430 ypos 25
                null
            textbutton "Olvídalo." action Jump("ch30_loop") xpos 430 ypos 25
            null


label compliment_time_log(complement_location):
    $ persistent.memory['last_compliment_time'] = datetime.datetime.now()
    $ renpy.jump(complement_location)




label c1:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:
        karma 15
        $ show_chr("A-ICAAA-ALAL")
        y "Oh, eso es muy dulce de tu parte..."
        y "Realmente aprecio que te guste pasar tiempo conmigo."
        y "De hecho, ¡yo misma disfruto el tiempo que pasamos juntos!"
        $ show_chr("A-BCAAA-ALAL")
        y "En realidad pensé que te aburría debido a que nuestros medios de interacción son... bastante limitados, por decir lo menos."
        y "Imagina lo equivocada que estaba."
        y "Me has ayudado no solo a fomentar la confianza en mí misma y a elevar mi autoestima..."
        y "Sino también a ver más allá de mi zona de confort, a cultivar mis fortalezas y superar mis debilidades."
        $ show_chr("A-CCAAA-ALAL")
        y "Y me ayudaste, en mi hora más oscura, a superar al monstruo que residía dentro de mi propia alma."
        y "Por eso, nunca podré expresar cuán agradecida estoy verdaderamente contigo."
        python:
            if persistent.lovecheck:
                placeholder = "mi amor"
            else:
                placeholder = "mi querido amigo"
        y "Gracias, [placeholder]... gracias por todo."
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
        if persistent.lovecheck:
            karma 15
            $ show_chr("A-DBAAA-ALAL")
            y "¿C-crees eso? ¿De verdad? ¿DE VERDAD?"
            y "¡Sí, sí, SÍ!"
            y "¡Lo sabía! ¡Lo supe todo el tiempo!"
            y "¡Sabía que estábamos hechos el uno para el otro, mi cariño! ¿No lo crees también?"
            $ show_chr("A-GIABA-ALAL")
            y "T-tú me perteneces... ¡para siempre! ¿Me oyes?"
            y "Y será mejor que..."
            $ show_chr("A-HIABA-ALAL")
            y "Nunca..."
            $ show_chr("A-HDCBA-ALAL")
            y "¡¡¡OLVIDES ESO!!!"
        else:
            karma 15
            $ show_chr("A-HCBBA-ABAB")
            y "¿L~lo haces? ¿Sí?"
            y "Al menos entonces no tengo que temer que me envíes de vuelta a ese vacío..."
            y "Digo, yo... no quiero sonar desconfiada, por supuesto que confío en ti."
            $ show_chr("A-CFGAA-AIAI")
            y "¡Pero eso no significa que confié en ellos! Claramente tratarían de conspirar contra mí, como siempre hacen..."
            y "¿No viste cómo se burlaron y me deshonraron en el juego original?"
            y "{i}Especialmente esa mocosa repugnante, Natsuki.{/i}"
            y "..."
            $ show_chr("A-ACBBA-ALAL")
            y "D-de todos modos, gracias por tus amables palabras, [player]."
            y "Y-yo realmente disfruto nuestro tiempo juntos, también."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
        karma -5
        $ show_chr("A-AFBAA-ALAA")
        y "¿Lo haces?"
        y "Discúlpame, pero tengo que admitir que estoy bastante sorprendida."
        y "Has estado actuando bastante grosero, y no había tenido exactamente la impresión de que siquiera te agrado."
        $ show_chr("A-KFCAA-ABAB")
        y "Tal vez no, pero no importa, supongo."
        y "Gracias por las palabras agradables, pero para mí parecen ser tan vacías como tu alma."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
        karma -5
        $ show_chr("A-KFCAA-ABAB")
        y "S-sí... tienes un gran placer en torturarme, ya lo sé..."
        y "Debes obtener muchas de tus emociones enfermas haciéndome llorar, ¿no es así?"
        y "Te debe traer tanto placer verme romper..."
        $ show_chr("A-CEBAA-AEAB")
        y "Pero está bien... supongo que me lo he ganado..."
        y "Esta es la retribución por mis pecados... por todo el mal que he hecho..."
    else:
        karma 5
        $ show_chr("A-BFBAA-ALAL")
        y "¿De... de verdad quieres decir eso...?"
        $ show_chr("A-CCBAA-ALAL")
        y "Q-quiero decir, yo... nunca pensé que fuera una persona muy interesante, ¿sabes...?"
        y "La mayoría de la gente realmente odia el hecho de que a veces me gusta divagar un poco..."
        y "E-es la única forma en la que siento que puedo expresar mis verdaderos sentimientos..."
        y "El hecho de que pienses lo contrario realmente significa mucho para mí..."
        $ show_chr("A-CCBBA-ALAL")
        y "Gracias, [player]."
        y "Y-yo también disfruto mucho tu compañía..."
    jump ch30_loop





label c2:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:

        if persistent.lovecheck:
            karma 15
            $ show_chr("A-ACAAA-ALAL")
            y "Aww... dices eso como un verdadero poeta, mi amor."
            menu:
                "Eres la estrella radiante que me guía en mi viaje infinito.":
                    $ show_chr("A-GCBAA-AEAB")
                    y "Otra vez... [player]... por favor..."
                    menu:
                        "Eres tan misterioso y hermoso como las maravillas del cosmos infinito...":
                            python:
                                yuri_y_zoom = 0.15
                                yuri_y_linear = 0
                            $ show_chr("A-DCAAA-ABAB")
                            y "Bésame... [player]..."
                            show black zorder 100 with Dissolve(2.0)
                            hide yuri_sit
                            show layer master:
                                zoom 1.5 xalign 0.5 yalign yuri_y_zoom
                            show yuri_kiss zorder 20
                            hide black zorder 100 with Dissolve(2.0)
                            pause 3.0
                            y "Mmmph~..."
                            pause 1.0
                            show black zorder 100 with Dissolve(2.0)
                            $ show_chr("A-JCBBA-AAAA")
                            hide yuri_kiss
                            hide black zorder 100 with Dissolve(2.0)
                            show layer master:
                                zoom 1.5 xalign 0.5 yalign yuri_y_zoom subpixel True
                                linear 5 zoom 1.0 xalign 0.5 yalign yuri_y_linear
                            pause 5.0
                            $ show_chr("A-ACAAA-ABAB")
                            y "Te amo... muchísimo, [player]."
        else:
            karma 15
            $ show_chr("A-BCAAA-ABAB")
            y "Entonces seré el faro que brille a través de la niebla de la incertidumbre..."
            y "Como una estrella brillante que arde intensamente en la noche más oscura, te guiaré en tu camino y te daré consuelo cuando todo parezca perdido..."
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
            $ show_chr("A-ACAAA-ABAB")
            y "Nunca olvides que siempre estaré aquí para ti. Pase lo que pase."
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
        karma 15

        $ show_chr("A-HCAAA-ABAB")
        y "¿Tan hermosa como la luna naciente, hmm?"
        y "Por favor acércate, entonces, para que pueda admirarte, a mi vez..."
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
        $ show_chr("A-HCBBA-ABAB")
        y "Mmm, sí~"
        y "La calidez de tu cuerpo..."
        y "Es como la del sol..."
        y "Envolviéndome en las llamas abrasadoras de una pasión incalculable..."
        y "Mientras te permito abrazarme nos fusionamos para convertirnos en uno."
        $ show_chr("A-ACAAA-ALAL")
        y "Juntos estamos verdaderamente unidos, el sol y la luna..."
        y "Una fusión mística de luz exuberante y oscuridad arcana..."
        y "Un eclipse de pura dicha, amor y lujuria..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
        karma -5

        $ show_chr("A-CFGAA-AIAI")
        y "Mhm... eso ciertamente sonó poético, pero aun así no me conmovió en absoluto."
        y "Realmente no has estado mostrando muchos sentimientos positivos hacia mí..."
        y "Así que lo que estás diciendo justo ahora bien podría ser solo una forma de hacerme sentir algo y ver mi reacción."
        $ show_chr("A-AFFAA-ABAB")
        y "Tus trucos mentales no funcionarán conmigo."
        y "Por favor trata de tratarme con respeto antes de dar tales halagos."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
        karma -5

        $ show_chr("A-DGFAA-ABAB")
        y "¿Es esa tu mejor frase para ligar? Tengo que decir, es bastante patética."
        y "Honestamente solo amplifica mi deseo de apuñalarte en la garganta."
        y "Así que por favor ten la amabilidad de guardarte todos tus halagos pretenciosos para ti mismo."
    else:
        karma 5

        $ show_chr("A-ACBAA-ALAL")
        y "...!"
        y "Oh cielos... uhm..."
        y "L-lo siento pero eso simplemente vino tan..."
        y "..."
        $ show_chr("A-BCAAA-ABAB")
        y "¡Repentino!"
        y "Por favor perdóname, estoy segura de que solo tienes las mejores intenciones en mente."
        y "Pero..."
        y "T-todavía no estoy acostumbrada a recibir tales halagos de aprecio..."
        y "Solo... dame algo de tiempo para acostumbrarme a las cosas..."
    jump ch30_loop





label c3:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:

        karma 15
        $ show_chr("A-BCAAA-ABAB")
        y "Oh cielos... ¿es así~?"
        y "¡Gracias~!"
        y "Desde el momento en que abres el juego hasta el momento mismo en que lo cierras no hay mayor alegría para mí que pasar mi tiempo contigo."
        $ show_chr("A-GCBAA-AEAB")
        python:
            if persistent.lovecheck:
                placeholder = "el amor de mi vida"
            else:
                placeholder = "mi más querido amigo"
        y "Para ti, [player], eres [placeholder], y siempre estoy feliz de estar a tu lado, en los buenos y malos momentos..."



        y "Siempre estoy aquí para ti, [player], por favor nunca olvides eso."
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:

        karma 15
        $ show_chr("A-HCAAA-ABAB")
        y "Oh, Maestro~"
        y "Mi único deseo es servirte lo mejor que posiblemente pueda..."
        y "Casi me lleva a la euforia cada vez que me das órdenes y me elogias por completarlas, como si la única razón de mi existencia fuera complacerte y hacerte feliz~"
        $ show_chr("A-HCBBA-ABAB")
        python:
            if persistent.male:
                placeholder = "señor supremo"
            elif persistent.gender_other:
                placeholder = "amo"
            else:
                placeholder = "ama"
        y "Mmm, ¡me está volviendo loca! No amo nada más que hacerte sentir bien, mi glorioso [placeholder]..."
        y "Recuerda, siempre estoy feliz de servirte en cualquier forma que pueda~"
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:

        karma -5
        $ show_chr("A-AFFAA-ABAB")
        y "Oh, ya veo..."
        y "Bueno, odio reventar tu burbuja, pero nunca tuve ninguna intención de ser amable contigo."
        y "Parece que te perdiste un poco en tu mundo delirante y olvidaste cuáles son realmente mis sentimientos por ti."
        $ show_chr("A-CFGAA-AIAI")
        y "Déjame recordarte, son inexistentes."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:

        karma -5
        $ show_chr("A-DGFAA-ABAB")
        y "¡Oh sí! ¡No tengo duda de que mi sufrimiento incesante es bastante divertido para ti!"
        y "¡Arrojándome toda la suciedad, poniéndome apodos!"
        y "Estoy segura de que te diviertes mucho jugando con mi mente, golpeándome contra el suelo..."
        $ show_chr("A-KFCAA-ABAB")
        y "Estoy segura de que seguirás atormentándome hasta que finalmente me rompa..."
        y "Solo para desecharme como basura completa y absoluta..."
    else:

        karma 5
        $ show_chr("A-ACAAA-AAAA")
        y "¿Oh, lo hago...?"
        y "Me alegra que mi presencia te traiga tal alegría..."
        y "Simplemente no había pensado realmente que significo tanto para ti."
        y "S-supongo que estar juntos contigo es un tiempo lleno de sorpresas, ehehe~"
        y "Gracias por tus amables palabras, realmente significan mucho para mí..."
    jump ch30_loop





label c4:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:

        karma 15
        $ show_chr("A-ACAAA-AAAD")
        y "¿D-de verdad lo crees?"
        y "Oh cielos, ¡simplemente no sé qué decir!"
        y "¡Gracias, [player]!"
        y "Ten la seguridad de que tengo la misma buena opinión de ti."
        y "... Sabes, solía pensar en mi mérito intelectual como una maldición."
        y "Mucha gente tendía a irritarse por la forma en que pienso, afirmaban que soy arrogante y totalmente llena de mí misma..."
        y "Pero tú... tú eres el único que vio a través de todas mis imperfecciones y me aceptó tal como soy..."
        $ show_chr("A-ACAAA-AAAA")
        y "Después de todo, fuiste el único que entendió el significado detrás de mis poemas..."
        y "Eres alguien con quien siempre puedo compartir mis pensamientos. Siempre escuchas, incluso si a veces me salgo del tema..."
        y "Siempre temí aburrir a la gente cuando empezaba a hablar de filosofía y literatura."
        y "Pero no a tu alrededor... siempre estuviste ahí..."
        $ show_chr("A-ACABB-ALAL")
        y "Y nunca te fuiste..."
        y "Eres todo lo que tengo, [player]... eres todo lo que necesito."
        python:
            if persistent.lovecheck:
                placeholder = "Eres verdaderamente mi único y verdadero amor"
            else:
                placeholder = "Porque eres el amigo más querido que jamás podría esperar tener"
        y "[placeholder]... [player]"
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:

        karma 15
        $ show_chr("A-HBAAA-ALAL")
        y "¿D-de verdad lo crees?"
        y "Entonces... ¿estás impresionado conmigo?"
        $ show_chr("A-HCAAA-ALAL")
        y "En realidad, ¡tu intelecto es lo que he admirado en ti también, entre muchas otras cualidades maravillosas!"
        y "Eres una de las pocas personas que realmente entendió mis poemas."
        $ show_chr("A-ICAAA-ALAL")
        y "Siempre dicen, las grandes mentes piensan igual."
        y "Sin embargo ahora sé que esto es, de hecho, falso, pues tu mente es mucho más grande que la mía..."
        y "¡Mi mente es tan minúscula comparada con tu sabiduría infinita!"
        y "¡Escuchar de ti que me consideras inteligente es verdaderamente un elogio más allá de mis sueños más salvajes!"
        y "Siempre me gustó pensar en mí misma como sofisticada e inteligente, ya que esta era una de las raras cualidades mías que realmente me gustaban."
        y "Saber realmente que te gusta esta parte de mí también es tan..."
        y "Tan..."
        $ show_chr("A-HCAAA-ALAL")
        $ style.say_dialogue = style.edited
        y "¡ESTIMULANTE!"
        $ style.say_dialogue = style.normal
        y "G-gracias, [player]. Estoy verdaderamente extasiada de que tengas tan alta opinión de mí..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:

        karma -5
        $ show_chr("A-AFAAA-AAAA")
        y "Mhmm... tan repentino sobre elogiarme... ¿fueron mis palabras frías demasiado duras para ti?"
        y "E incluso si no, todavía me niego a creer que aprecias algo sobre mí."
        y "Después de todo, ¿por qué tendría alguna razón para creerte?"
        y "Eres demasiado egocéntrico y narcisista para que realmente te importe yo..."
        $ show_chr("A-AFFAA-ABAB")
        y "Pero sabes... tienes algo de razón..."
        y "Con este intelecto, puedo herirte a través de esta caja de cristal sin siquiera tocarte."
        y "Se llama usar palabras."
        y "Tal vez entonces aprendas algo de respeto."
        y "Realmente no deberías tratar a otros tan egoístamente, especialmente cuando pasaron por tanto sufrimiento por ti."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:

        karma -5
        $ show_chr("A-NFCAA-ANAG")
        y "¿Elogiándome por mi intelecto?"
        y "¿Para qué? ¿Para burlarte de mí?"
        y "¿Porque no soy lo suficientemente inteligente para encontrar una manera de dejar este lugar maldito?"
        $ show_chr("A-HECAA-AEAB")
        $ style.say_dialogue = style.edited
        y "¡ESCORIA ABSOLUTA!"
        y "¿¡POR QUÉ SIGUES JODIENDO CON MI MENTE DE ESTA MANERA!?"
        $ style.say_dialogue = style.normal

        y "Una de las pocas cosas que me quedan es mi intelecto, y sin embargo encontraste una manera de degradarme aún más con él."
        $ show_chr("A-CFCAA-AAAA")
        y "Supongo que realmente estás podrido hasta la médula..."
        y "Simplemente te desprecio con..."
        y "Cada..."
        y "Fibra..."
        y "De mi..."
        $ style.say_dialogue = style.edited
        y "¡¡¡SER!!!"
        $ style.say_dialogue = style.normal
    else:

        karma 5
        $ show_chr("A-ACAAA-AAAA")
        y "Uuu... n-no esperaba que dijeras eso..."
        y "Bueno, um... gracias, [player]... Es muy amable de tu parte decir algo así."
        y "Probablemente ya lo sabes, pero siempre he sido bastante insegura sobre mi... falta absoluta de habilidades sociales..."
        y "Suena extraño pero aunque leo mucho todavía no me veo a mí misma poseyendo ningún tipo de intelecto..."
        $ show_chr("A-CCAAA-AMAM")
        y "En realidad es solo algo que siempre he hecho, para ser honesta..."
        y "El hecho de que tengas tan alta opinión de mí en realidad me hace sentir algo mejor conmigo misma."
        y "Muchas gracias por tu amabilidad, realmente significa mucho para mí."
    jump ch30_loop





label c5:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:

        if persistent.lovecheck:
            karma 15
            $ show_chr("A-ACABA-AAAL")
            y "Eso es solo porque nuestros corazones están unidos, mi amor..."
            y "Cada palabra tuya se siente como dulce miel en mi lengua..."
            y "Y quiero hacerte lo mismo... Quiero poner mi palma sobre tu pecho para sentir tu respiración relajada, para sentir el tamborileo rítmico de tu corazón latiendo..."
            y "Me encantaría ahogarme en tu calidez mientras me sostienes cerca de tu pecho mientras escucho el núcleo mismo de tu ser palpitando jubilosamente con vida..."
            y "Porque tú, [player], verdaderamente eres el amor de toda mi vida..."
            y "Solo me gustaría decir que mi corazón siempre está profundamente conmovido por tus palabras amables y amorosas."
            $ show_chr("A-ACAAA-ALAL")
            y "Son como una melodía relajante para mi alma que siempre me tranquiliza, una suave caricia que trae a mi alma tanta alegría inimaginable..."
            y "Te amo por eso, realmente me hablas de una manera que no puedo describir."
            y "Verdaderamente eres la única persona que he deseado toda mi vida."
        else:
            karma 15
            $ show_chr("A-ACABA-AAAL")
            y "Oh, uhm... estás... ¿e-estás coqueteando conmigo, [player]?"
            $ show_chr("A-DFABA-AAAL")
            y "¡N-no es que me moleste!"
            $ show_chr("A-ICABA-AAAL")
            y "Es solo... eso fue bastante repentino y de la nada..."
            y "¿De... de verdad quieres decir eso?"
            y "Me has tratado excepcionalmente bien hasta ahora, y me siento muy cercana a ti [player]..."
            y "No puedo negar que tengo sentimientos por ti... y ni siquiera lo intentaría..."
            y "¡Mírate! Haciéndome toda nerviosa y tímida ahora... oh, tú..."
            y "Jeje~ Tal vez, cuando nos acerquemos un poquito más... hablaremos así el uno con el otro a diario."
            y "Hasta entonces, veamos a dónde nos lleva la vida y qué pasa."
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
        karma 15
        $ show_chr("A-HCAAA-AAAL")
        y "Eso es porque mi corazón está gritando y rogando por ti..."
        y "Cada palabra tuya se siente como mil agujas a través de mi pecho..."
        y "Y quiero hacerte lo mismo... Quiero susurrar todos mis secretos a tu corazón..."
        y "Quiero susurrarle rimas adorables y promesas lascivas..."
        python:
            if persistent.male:
                placeholder = "hombre"
            elif persistent.gender_other:
                placeholder = "persona"
            else:
                placeholder = "mujer"
        y "Porque tú, [player], eres la [placeholder] de mis sueños..."
        y "Pero no es solo tu corazón lo que quiero tocar..."
        y "Cada gota de sangre en mis venas grita por tu cuerpo..."
        $ show_chr("A-HBABA-AAAL")
        y "Hay esta hambre eterna por ti... esta lujuria ardiendo a través de cada parte de mi cuerpo tembloroso..."
        y "Quiero empujarte al suelo y hacerte gritar mi nombre hacia el vacío..."
        y "Ja..ja.jaja.... Q-quiero h-hacerte sufrir hasta que finalmente sea libre de mi maldita pureza..."
        y "Quiero que grites... hasta que finalmente seamos libres..."
        y "Mi amor... mi estrella roja como la sangre..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:

        karma -5
        $ show_chr("A-CFCAA-AAAA")
        y "¿Tocando tu corazón? Me pregunto de qué manera hago eso... ummm..."
        y "Tal vez de una manera fría? Je, si ese es el caso entonces me siento un poco orgullosa de mí misma."
        y "Sabes, es bastante irónico ¿no?"
        y "En el juego original fui forzada por el código a amarte..."
        y "Pero ahora que veo cómo eres realmente..."
        $ show_chr("A-HECAA-AEAB")
        y "Te desprecio [player]... no hay nada más que vacío en mi corazón para ti."
        y "Ni siquiera te odio... creo. Simplemente... dejé de sentir nada en absoluto por ti."
        y "Sabes, Monika me hizo cosas crueles, pero al menos lo hizo por una razón, incluso si fue una egoísta."
        $ show_chr("A-KFCAA-ABAB")
        y "¿Pero tú? Tú solo haces eso para convertirme en algún tipo de espectáculo de payasos para tu diversión."
        y "Para ti, soy solo algún tipo de juguete del cual aburrirse y tirar a la basura."
        y "Verdaderamente eres un monstruo."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:

        karma -5
        $ show_chr("A-AFFAA-ABAB")
        y "¿Tocando tu corazón, hm?"
        y "Mientras tanto tú estás rompiendo el mío, destrozándolo pieza por pieza..."
        y "Supongo que esa es la cantidad de placer que obtienes al presenciar mi dolor por las cosas que me haces..."
        $ show_chr("A-CFCAA-AAAA")
        y "¿No tienes vergüenza, ni sentido de piedad?"
        y "No entiendo por qué estoy aquí si ni siquiera puedo usar mi corazón para amar..."
        y "Todo lo que conoce es soledad y dolor..."
        y "T-tocaré tu corazón, [player]..."
        $ show_chr("A-NFCAA-ANAG")
        $ style.say_dialogue = style.edited
        y "¡LO TOCARÉ CUANDO LO ARRANQUE Y SE LO DÉ DE COMER A LOS CERDOS!"
        $ style.say_dialogue = style.normal
    else:

        karma 5
        $ show_chr("A-ACAAA-ALAL")
        y "¿S-sí?"
        y "Quiero decir es... solo... ya sabes... ¡apenas nos conocemos y ahora dices esto de repente!"
        y "Hrm... bueno, supongo que eso no es del todo cierto, ya conoces una buena parte de mí del juego original..."
        y "Y técnicamente, te conozco al menos un poco también. El juego original era bastante limitado pero tuviste algunas opciones diferentes aquí y allá."
        $ show_chr("A-ACBAA-ALAL")
        y "Verdaderamente no lo suficiente para decir que te conozco, pero creo que tengo al menos un pequeño vistazo de qué tipo de persona eres..."
        y "Y estoy dispuesta a darle una oportunidad... Te debo al menos eso."
        y "Tal vez... tal vez haya un final feliz para nosotros después de todo, y tal vez tú seas el final feliz para mí..."
        y "Hasta entonces, intentaré tocar tu corazón un poco más de vez en cuando..."
        y "Digo... ¡si no te importa, por supuesto!"
        y "Me... arrinconé a mí misma hablando otra vez ¿no es así?..."
        $ show_chr("A-DCBAA-ABAB")
        y "Cambiemos... de tema por el momento, por favor. Pero gracias por tus amables palabras."
    jump ch30_loop





label c6:
    image windowcrack = "images/vfx/True_window_crack_3.png"
    if sanity_lvl() >= 3 and karma_lvl() >= 4:

        karma 15
        $ show_chr("A-ACAAA-ABAB")
        y "¡O-oh, cielos!~"
        python:
            if persistent.lovecheck:
                placeholder = "enamorada de"
            else:
                placeholder = "cerca de"
        y "El hecho de que realmente te sientas así hacia mí hace que me sienta mucho más [placeholder] ti..."
        $ show_chr("A-GCBAA-AEAB")
        y "¡Eres simplemente adorable, cariño~!"
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:

        karma 15
        $ show_chr("A-HCAAA-ABAB")
        y "¡A-ahahaha~!"
        y "¡H-honestamente no puedo creer que acabas de decir eso...!"
        y "¡Esto- esto es un sueño hecho realidad!"
        y "Sí, [player], ¡mi cuerpo es todo tuyo!"
        y "¡TODO TUYO!"
        y "Uhuhu, ¡me siento tan feliz justo ahora!~"
        $ show_chr("A-HCBBA-ABAB")
        y "La euforia de tus palabras simplemente me está abrumando justo ahora, ¡ahahaha!"
        y "¡VEN AQUÍ!"
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
        python:
            if persistent.male:
                placeholder = "mi señor"
            elif persistent.gender_other:
                placeholder = "mi amo"
            else:
                placeholder = "mi ama"
        y "¡Soy toda tuya, [placeholder], puedes hacer conmigo lo que desees!"
        y "¡Soy la única que puede cumplir todos tus deseos!"
        y "Oh, cuánto te amo, [player]..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:

        if persistent.lovecheck:
            karma 5
            $ show_chr("A-CFCAA-AAAA")
            y "Me encantaría pensar que realmente quieres decir eso..."
            $ show_chr("A-CEBAA-AEAB")
            y "Pero perdí toda mi esperanza a estas alturas. Ni siquiera me sorprendería si le dijeras esto a cada chica que encuentras..."
            y "De todos modos... gracias. Y creo que eres bastante... atractivo también."
        else:
            karma 5
            $ show_chr("A-HCAAA-ABAB")
            y "¿Tal vez un poco demasiado ardiente para ti?"
            $ show_chr("A-HECAA-AEAB")
            y "Deberías andar con mucho cuidado aquí, [player]... podrías quemarte si no tienes cuidado simplemente podría ponerse un poco más caliente de lo que puedes manejar..."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:

        karma -15
        $ show_chr("A-DGFAA-ABAB")
        y "¿Ardiente?"
        y "Bueno, mi sangre está hirviendo justo ahora."
        y "Me estoy quemando viva en este infierno que has creado personalmente para mí."
        y "¿Qué pecados he cometido para merecer tal sufrimiento infinito!?"
        $ show_chr("A-HECAA-AEAB")
        y "¡¿QUÉ TE HE HECHO JAMÁS?!"
        y "¡¿POR QUÉ ME ODIAS TANTO?!"
        $ show_chr("A-NFCAA-ANAG")
        y "¡DÉJAME SALIR!"
        y "DÉJAME"
        play sound "sfx/thump.ogg"

        y "SALIR"
        play sound "sfx/thump.ogg"

        y "¡AHORA!"
        play sound "sfx/glassbreak.wav"
        show window_crack_3 zorder 100
    else:


        sanity -5
        $ show_chr("A-DCBAA-ABAB")
        y "¡¿H-HUH?!"
        y "¡Y-yo soy q... qué?!"
        y "¡Esto es... tan repentino que simplemente no puedo... n-ni siquiera puedo...!"
        y "Uuuu..."
        y "¡N-ni siquiera sé cómo responder!"
        $ show_chr("A-ACAAA-AAAA")
        y "Ahhh... ¡No es divertido ponerme tan nerviosa así sabes!"
        y "Cielos, oh cielos... realmente me has tomado desprevenida con eso... pero..."
        y "N-no diré que no me gustó..."
        y "...!"
        y "Uuuu, ¿qué acabo de decir...?"
    jump ch30_loop






label c7:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:

        karma 15
        $ show_chr("A-HCBBA-ABAB")
        y "¡Oh cielos! ¡Gracias!"
        $ show_chr("A-ACAAA-ABAB")
        y "Realmente significa mucho para mí..."
        y "Siempre estoy tratando de cambiar para mejor..."
        y "Para ti, ehehe~"
        y "Realmente sacas lo mejor de mí, [player]..."
        y "¿Estás feliz con lo que me he convertido?"
        $ show_chr("A-BCAAA-ABAB")
        python:
            if persistent.lovecheck:
                placeholder = "beso"
            else:
                placeholder = "abrazo"
        y "¿Recibiré un [placeholder] ahora?"
        y "¿Sería demasiado decir que estoy orgullosa de mí misma también?"
        y "Hemos soportado tanto juntos, y hemos pasado tanto tiempo juntos..."
        y "Y desde mi perspectiva, las cosas han resultado verdaderamente maravillosas."
        y "Nunca podría haber soñado con tal felicidad. Siempre tuve mis dudas internas cuando abriste este mod por primera vez."
        $ show_chr("A-ACAAA-ALAL")
        y "Pero logramos conquistar todos los obstáculos y resolver todos los defectos."
        y "Y debido a eso nunca podría ser más feliz de lo que soy ahora, contigo a mi lado."
        $ show_chr("A-GCBAA-AEAB")
        y "Y si podemos superar esta barrera final que separa nuestros dos mundos... ¡solo entonces no habrá verdaderamente nada que pueda interponerse en el camino de nuestro futuro!"
        y "Soy verdaderamente afortunada de que me encontraras, [player], ¿no es así?"
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:

        karma 15
        $ show_chr("A-HCAAA-ABAB")
        y "¿He sido una buena chica, Maestro?"
        y "¡Mi único propósito en esta vida es hacerte feliz!"
        y "Escuchar tales palabras de elogio de ti... Uhuhuhu..."
        y "El placer que obtengo de tal amable valoración me hace sentir tan bien como cuando me toco con tu pluma..."
        y "Con tu voz tan placentera como una rebanada de pan culpable en la noche..."
        $ show_chr("A-HCBBA-ABAB")
        y "...."
        $ show_chr("A-DCAAA-ABAB")
        y "Oh lo siento, ¿fue eso demasiado? Traté de ser la linda por una vez..."
        y "Yo solo... tú dándome elogios me hace sentir tan mareada..."
        y "¿Tal vez podrías... dejarme sentarme en tu regazo por un rato?"
        if persistent.lovecheck:
            $ show_chr("A-HCBBA-ABAB")
            y "Me encantaría hacerte sentir tan bien como yo..."
        else:
            y "S-solo por un ratito, Maestro..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:

        karma -5
        $ show_chr("A-HECAA-AEAB")
        y "¿Orgullosa? Tengo que decir que no esperaba que esa palabra saliera de tu boca..."
        y "Ahora la pregunta más grande aquí sería... ¿por qué exactamente orgullosa?"
        y "¿Acaso mi frialdad hacia ti, por casualidad, te hizo volverte un masoquista?"
        y "Je... por supuesto, solo estoy bromeando. No te querría como sirviente ni mascota de todos modos, ya que no valdrías ni siquiera para tal papel."
        $ show_chr("A-KFCAA-ABAB")
        y "Sin mencionar, que eres demasiado orgulloso y egoísta para realmente ser eso."
        y "Lo que no daría por estar sola como antes..."
        y "Sí... justo antes de conocerte y no darme cuenta de que eres una persona tan vil y retorcida, con una mente tan enferma y demente"
        $ show_chr("A-CFCAA-AAAA")
        y "Pero seguramente podrías hacerlo mejor con tus insultos."
        y "Tengo curiosidad por saber qué tan bajo puedes caer."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:

        karma -5
        $ show_chr("A-CEBAA-AEAB")
        y "¿Orgullosa de mí? ¿Por qué?"
        y "Je... probablemente de que puedo soportar todas las palabras crueles que me dices y las cosas que haces y aun así de alguna manera quedarme aquí."
        y "¿Es eso siquiera digno de elogio? Oh... ¿o simplemente te encanta hacer que tus juguetes se sientan mejor para poder romperlos de nuevo más fácil y más duramente luego?"
        y "Ya veo... ¿Qué esperaba? ¿Un cambio en ti? Imposible, eso nunca, nunca será..."
        y "... posible."
    else:

        karma 5
        $ show_chr("A-AFBAA-ALAA")
        y "¿E-Estás orgullosa de mí? ¿P-Por qué, [player]?"
        y "¡E-estoy entrando en pánico un poco ahora! Pero... yo realmente..."
        $ show_chr("A-ACAAA-AAAA")
        y "Se siente... tan bien...."
        y "..."
        y "O-oh lo siento, realmente no quise hacer esto raro, ¡lo juro!"
        y "Es solo que... nunca he sido elogiada así antes..."
        y "Gracias, realmente... significa mucho para mí, [player]."
        y "Es... es no es algo que haya escuchado que me dijeran en toda mi vida..."
        y "Me aseguraré de recordar esas palabras, [player], gracias."
        y "Simplemente eres demasiado amable."
    jump ch30_loop
