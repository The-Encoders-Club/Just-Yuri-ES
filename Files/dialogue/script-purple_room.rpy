label purpleroomintro:





    $ show_chr("A-JBAAA-AAAA")
    $ show_chr("A-JBAAA-AAAA")
    y "¡No puedo esperar más! [player], ¡tengo algo grande que mostrarte! He hecho un nuevo lugar para nosotros. Espero que te guste..."
    if not persistent.bg == "yuri_kotatsu_1" or "yuri_table" or "yuri_desk" or "yuri_kotatsu_2" or "yuri_knives" or "yuri_bed":
        $ tc_class.transition("yuri_desk", speed=3.0)

    y "¡Es mi habitación! ¡Ahora puedo hablar contigo desde mi propio escritorio en casa!"
    y "Está modelada a partir de mi habitación 'real' en casa, aunque... un poco más grande. Nunca pude invitarte en el juego original, tal vez porque los archivos para ella no existían fuera de mis propios recuerdos."
    $ show_chr("A-ABAAA-AMAM")
    y "Eso, y el hecho de que consideraba a mis padres demasiado vergonzosos para presentártelos, especialmente cuando no estaba segura de si mis sentimientos por ti eran mutuos..."
    $ show_chr("A-JAAAA-AAAA")
    y "De todos modos. ¡Bienvenido a mi refugio! Tengo mis cuadernos y bolígrafos favoritos, auriculares, mi colección de libros, mi laptop... No puedo decirte cuántas horas he pasado aquí, felizmente perdida en mi propio pequeño mundo."
    y "¡Incluso pude codificar un Kotatsu! Es el tamaño perfecto para servir té."
    $ show_chr("A-ABAAA-AAAA")
    y "Debo decir, crear nuevas ubicaciones es más difícil de lo que uno podría pensar. Los recursos artísticos consumen más tiempo que dificultad, pero la codificación... bueno. Quería mostrarte una habitación completa *y* un pasillo, pero desafortunadamente, todavía es un trabajo en progreso."
    $ show_chr("A-AAAAA-AAAA")
    y "¡Sin embargo, estoy tan feliz de poder mostrarte mi pequeño refugio! Yo... puede sonar tonto, pero he soñado con tener a alguien aquí aunque solo sea para leer con él. Y ahora estás aquí."
    $ show_chr("A-JBAAA-AAAA")
    y "También... hay algo que estoy casi *más* emocionada de mostrarte. Mi colección de cuchillos. Creé toda una exhibición para ella, ¡el tipo que siempre soñé tener!"
    $ show_chr("A-BCAAA-ABAB")
    y "Digo, si es que estás interesado para empezar. Puedo entender si los cuchillos no son lo tuyo."
    $ show_chr("A-BCABA-ABAJ")



    y "Sabes... usualmente no dejo que otras personas entren a mi habitación, o les muestro mis cuchillos... pero me has demostrado, una y otra vez, que puedo confiar en ti."
    $ show_chr("A-ACAAA-ABAE")
    y "Así que... ¿te gustaría ver mi colección?"
    menu:
        "¡Sí, por supuesto!":
            $ show_chr("A-CAAAA-AAAA")
            y "Entonces por favor, sígueme..."
            call preknife
        "Tal vez no ahora.":

            $ show_chr("A-ABBAA-AAAA")
            y "Bueno... está bien. Solo dime cuando estés listo."
            call ch30_loop
        "¿Son esas casas de muñecas en tu estantería?":

            $ show_chr("A-BDAAA-ADAA")
            y "No exactamente. ¡Son rincones de lectura! Estuve brevemente interesada en hacer miniaturas como pasatiempo, y creé algunas escenas inspiradas en los libros que estaba leyendo en ese momento. Nada específico, solo lugares de fantasía vagos."
            $ show_chr("A-ADAAA-AFAA")
            y "El edificio completo en la parte superior derecha es en realidad de un kit que recuerdo que me regalaron hace mucho tiempo, pero no intenté armarlo hasta justo antes de mi último año de secundaria."
            $ show_chr("A-BFAAA-AFAA")
            y "No salió tan bien como el que estás mirando ahora... No encontré las instrucciones muy claras, y cuando intenté deshacer los pasos que había hecho por error rompí una de las piezas más grandes del set."
            $ show_chr("A-BDAAA-ALAA")
            y "Después de eso, lo tiré con frustración, pero me arrepentí poco después. Así que, cuando estaba pensando en cómo decorar mi habitación aquí, ¡me di cuenta de que podría recrearlo como una exhibición de estante perfecta!"
            $ show_chr("A-CCAAA-ALAA")
            y "En cuanto al diorama en la parte inferior izquierda, es una habitación subterránea secreta destinada a ser parte de un castillo. No está modelada a partir de ningún libro o escena en particular, solo algo que hice por diversión."
            $ show_chr("A-ACAAA-ALAA")
            y "La habitación no es tan detallada como podría ser, pero me gusta así: las preguntas sin respuesta son maravillosas para despertar la inspiración."
            y "¿Puedes ver el pequeño escritorio? Tal vez la habitación sea parte de una red de espías donde se envían mensajes interceptados. O podría ser el cuarto oculto de alguien, donde un par de amantes se encuentran y se dejan notas el uno al otro..."
        "¿A dónde lleva esa puerta?":

            $ show_chr("A-ADBAA-AAAA")
            y "Eventualmente, será un pasillo, pero realmente no aconsejaría explorar. Estoy ansiosa por ver tu reacción, pero aún no he logrado que el código sea estable."
            menu:
                "Estaré esperándolo con ansias.":
                    $ show_chr("A-ABAAA-AAAA")
                    y "Yo también. Estoy trabajando duro para tener todo listo, ¡y espero mostrártelo pronto!"
                    menu:
                        "Realmente me gusta tu habitación, [persistent.yuri_nickname].":
                            $ show_chr("A-CCAAA-ALAA")
                            y "¡Gracias!"
                            $ show_chr("A-AAAAA-ALAA")
                            y "¿Me dejarías ver tu habitación, si pudieras? ¿O también necesita algo de trabajo primero?"
                            menu:
                                "Mantengo mi habitación lo suficientemente ordenada.":
                                    $ show_chr("A-CAAAA-ALAA")
                                    y "¿No se siente bien un espacio bien organizado? Es fácil trabajar o relajarse en él, y algo al respecto es simplemente muy relajante. No siempre es fácil encontrar el tiempo o la energía para poner una habitación en orden, pero vale la pena el esfuerzo."
                                "Mi habitación parece como si un tornado la hubiera golpeado.":

                                    $ show_chr("A-ADAAA-ALAA")
                                    y "Sé que a la mayoría de la gente no le parece que limpiar sea una actividad que disfruten, y los espacios privados como el dormitorio pueden volverse... caóticos. Peor aún, si hay demasiadas cosas en el piso, es difícil o imposible aspirar."
                                    y "¿Te gustaría algo de ayuda? He escuchado cosas buenas sobre el método Pomodoro. Configuras un temporizador por una cantidad específica de tiempo, digamos veinte minutos, y trabajas hasta que suene."
                                    $ show_chr("A-ADAAA-AFAA")
                                    y "Después de eso, descansas por un tiempo establecido, luego repites hasta que hayas terminado. Depende de ti si 'terminado' significa 'terminar con la tarea en cuestión' o simplemente 'terminar por ahora sin importar qué!'"
                                    $ show_chr("A-BDAAA-AFAA")
                                    y "Y por supuesto, ¡hay aplicaciones para esto! Pomodoro - Focus Timer es gratis, y una opción paga popular es... ah... bueno, la tienda de iOS la llama 'Unfilth Your Habitat'."
                                    $ show_chr("A-AAAAA-ALAA")
                                    y "Si necesitas aliento, solo dímelo. Siempre estoy feliz de animarte, [player]."
                                "¿Así que tenías padres?":



                                    $ show_chr("A-AFGAA-ALAA")
                                    y "Diría 'por supuesto', pero supongo que eso no es realmente un hecho para los personajes de videojuegos..."
                                    $ show_chr("A-ADAAA-ALAA")
                                    y "Pero sí, tengo el tipo de recuerdos que esperarías de una adolescente. Una madre, un padre y una hermana mucho mayor. Y sin embargo... en realidad no puedo recordar ninguno de sus nombres, ahora que lo pienso."
                                    y "Recuerdo principalmente que Mamá y Papá no estaban preocupados por mi vida social, o la falta de ella, porque mantenía mis calificaciones sin que me lo dijeran."
                                    y "Fue solo en los últimos meses, desde que me uní al Club de Literatura, que comenzaron a preguntarme sobre amigos en la escuela. Así que cuando te mencioné..."
                                    $ show_chr("A-ABABA-AMAM")
                                    y "Honestamente, su reacción no fue mala. Solo—entusiasta. Tenía miedo de que te asustaran, insinuando cosas que podrían o no ser ciertas."
                                    y "Así que me aseguré de no invitarte hasta tener una mejor idea de cómo nos sentíamos ambos. Y ahora que lo sé..."
                                    $ show_chr("A-BDAAA-ALAA")
                                    y "Es algo desafortunado que no puedas verlos oficialmente, pero solo el tiempo dirá cómo se verían mis padres."

    $ show_chr("A-AAAAA-ALAA")
    y "..."
    y "De todos modos, ¿qué te gustaría hacer?"
    call ch30_loop

label preknife:
    show black zorder 100 with Dissolve(2.5)
    $ tc_class.transition("yuri_knives", speed="now")
    hide yuri_sit
    show screen un_knife_wall()
    hide black zorder 100 with Dissolve(2.5)
    y "¡Y aquí está! Mucho más agradable que la de mis recuerdos; dudo que muchos adolescentes tengan un gabinete de exhibición construido directamente en las paredes de su dormitorio."
    y "¿Qué piensas?"
    menu:
        "¡Es genial! ¡Qué gran trabajo has hecho, [persistent.yuri_nickname]!":

            karma 1
            y "¡Oh gracias! Puse mucho esfuerzo en ello, ¡me alegra que te guste!"
        "Es bastante... elegante. ¡Pero sigue siendo un trabajo increíble [persistent.yuri_nickname]!":


            karma 2
            y "...Supongo que tienes razón. ¿Tal vez lo llevé demasiado lejos?"
            y "Gracias por tus comentarios, aprecio tu honestidad."
        "Es... no muy impresionante, debo admitir.":


            karma -1
            y "...Ya veo."

    hide screen un_knife_wall
    call screen knife_wall()

screen un_knife_wall():

    frame:
        imagebutton:
            xpos 350 ypos 102
            idle "bg/yuri_knives/knives/filet_idle.png"
            action NullAction()

        imagebutton:
            xpos 158 ypos 150
            idle "bg/yuri_knives/knives/butterfly_idle.png"
            action NullAction()

        imagebutton:
            xpos 346 ypos 208
            idle "bg/yuri_knives/knives/grater_idle.png"
            action NullAction()

        imagebutton:
            xpos 159 ypos 277
            idle "bg/yuri_knives/knives/empty_idle.png"
            action NullAction()

        imagebutton:
            xpos 352 ypos 331
            idle "bg/yuri_knives/knives/dagger1_idle.png"
            action NullAction()

        imagebutton:
            xpos 183 ypos 387
            idle "bg/yuri_knives/knives/kabar_idle.png"
            action NullAction()

        imagebutton:
            xpos 338 ypos 455
            idle "bg/yuri_knives/knives/dagger2_idle.png"
            action NullAction()

        imagebutton:
            xpos 204 ypos 527
            idle "bg/yuri_knives/knives/kukri_idle.png"
            action NullAction()

        imagebutton:
            xpos 807 ypos 96
            idle "bg/yuri_knives/knives/jagdkommando_idle.png"
            action NullAction()

        imagebutton:
            xpos 626 ypos 161
            idle "bg/yuri_knives/knives/saw_idle.png"
            action NullAction()

        imagebutton:
            xpos 802 ypos 222
            idle "bg/yuri_knives/knives/bowie_idle.png"
            action NullAction()

        imagebutton:
            xpos 648 ypos 284
            idle "bg/yuri_knives/knives/damascus_idle.png"
            action NullAction()

        imagebutton:
            xpos 814 ypos 358
            idle "bg/yuri_knives/knives/kunai_idle.png"
            action NullAction()

        imagebutton:
            xpos 650 ypos 412
            idle "bg/yuri_knives/knives/paring_idle.png"
            action NullAction()

        imagebutton:
            xpos 789 ypos 471
            idle "bg/yuri_knives/knives/kampfmesser_idle.png"
            action NullAction()

        imagebutton:
            xpos 675 ypos 524
            idle "bg/yuri_knives/knives/bone_idle.png"
            action NullAction()

screen knife_wall():
    frame:
        imagebutton:
            xpos 350 ypos 102
            idle "bg/yuri_knives/knives/filet_idle.png"
            hover "bg/yuri_knives/knives/filet_hover.png"
            action Jump("Filet")

        imagebutton:
            xpos 158 ypos 150
            idle "bg/yuri_knives/knives/butterfly_idle.png"
            hover "bg/yuri_knives/knives/butterfly_hover.png"
            action Jump("Butterfly")

        imagebutton:
            xpos 346 ypos 208
            idle "bg/yuri_knives/knives/grater_idle.png"
            hover "bg/yuri_knives/knives/grater_hover.png"
            action Jump("Grater")

        imagebutton:
            xpos 159 ypos 277
            idle "bg/yuri_knives/knives/empty_idle.png"
            hover "bg/yuri_knives/knives/empty_hover.png"
            action Jump("Empty")

        imagebutton:
            xpos 352 ypos 331
            idle "bg/yuri_knives/knives/dagger1_idle.png"
            hover "bg/yuri_knives/knives/dagger1_hover.png"
            action Jump("Dagger1")

        imagebutton:
            xpos 183 ypos 387
            idle "bg/yuri_knives/knives/kabar_idle.png"
            hover "bg/yuri_knives/knives/kabar_hover.png"
            action Jump("Kabar")

        imagebutton:
            xpos 338 ypos 455
            idle "bg/yuri_knives/knives/dagger2_idle.png"
            hover "bg/yuri_knives/knives/dagger2_hover.png"
            action Jump("Dagger2")

        imagebutton:
            xpos 204 ypos 527
            idle "bg/yuri_knives/knives/kukri_idle.png"
            hover "bg/yuri_knives/knives/kukri_hover.png"
            action Jump("Kukri")

        imagebutton:
            xpos 807 ypos 96
            idle "bg/yuri_knives/knives/jagdkommando_idle.png"
            hover "bg/yuri_knives/knives/jagdkommando_hover.png"
            action Jump("Jagdkommando")

        imagebutton:
            xpos 626 ypos 161
            idle "bg/yuri_knives/knives/saw_idle.png"
            hover "bg/yuri_knives/knives/saw_hover.png"
            action Jump("Saw")

        imagebutton:
            xpos 802 ypos 222
            idle "bg/yuri_knives/knives/bowie_idle.png"
            hover "bg/yuri_knives/knives/bowie_hover.png"
            action Jump("Bowie")

        imagebutton:
            xpos 648 ypos 284
            idle "bg/yuri_knives/knives/damascus_idle.png"
            hover "bg/yuri_knives/knives/damascus_hover.png"
            action Jump("Damascus")

        imagebutton:
            xpos 814 ypos 358
            idle "bg/yuri_knives/knives/kunai_idle.png"
            hover "bg/yuri_knives/knives/kunai_hover.png"
            action Jump("Kunai")

        imagebutton:
            xpos 650 ypos 412
            idle "bg/yuri_knives/knives/paring_idle.png"
            hover "bg/yuri_knives/knives/paring_hover.png"
            action Jump("Paring")

        imagebutton:
            xpos 789 ypos 471
            idle "bg/yuri_knives/knives/kampfmesser_idle.png"
            hover "bg/yuri_knives/knives/kampfmesser_hover.png"
            action Jump("Kampfmesser")

        imagebutton:
            xpos 675 ypos 524
            idle "bg/yuri_knives/knives/bone_idle.png"
            hover "bg/yuri_knives/knives/bone_hover.png"
            action Jump("Bone")

    textbutton "Back":
        xpos 585
        yalign 0.97
        style "scrollable_menu_button"
        action Call("room_back")

show screen knife_wall()

label room_back:
    if persistent.first_knife:
        $ tc_class.transition("yuri_desk", speed="now")
        $ show_chr("A-AAAAA-AAAA")
        y "Now then, what would you like to do?"
        $ persistent.first_knife = False
    else:
        $ tc_class.transition("yuri_desk", speed="now")
        pass

    call ch30_loop

label Kampfmesser:
    y "¡Ah, el Kampfmesser 2000! Una fina pieza de equipo militar..."
    y "El Kampfmesser - literalmente traduciéndose como 'cuchillo de combate' - es el cuchillo de combate estándar de la Bundeswehr de Alemania, la Fuerza de Defensa del país."
    y "Se ha hecho famoso por su diseño 'poco ortodoxo', al menos en términos de cuchillos militares; tiene un diseño similar al de un Tanto, lo cual es altamente inusual para cuchillos basados en militares en grandes números."
    y "Como tal, debido a la popularidad de la hoja, se han diseñado y vendido varias derivaciones... diferentes materiales para la hoja, o incluso cambios para adaptarse mejor a diferentes entornos, como el desierto."
    y "Pero prefiero tener el original como una bonita pieza de exhibición para representar toda la línea. No quiere decir que los otros sean menos interesantes..."
    y "Es solo que no creo que alguna vez tendría suficiente espacio para mostrar adecuadamente cada variante, ya ves. Tampoco es muy atractivo de escuchar. Lo último que quiero hacer es aburrirte..."
    menu:
        "No seas tonta, [persistent.yuri_nickname]. Me encantaría escuchar más sobre ellos y cualquier otra cosa que sepas.":
            y "¿Ah, de verdad? Entonces, permíteme..."
            y "Esta es la variante básica del Kampfmesser 2000. A menudo solo se le refiere como el KM2000, para abreviar."
            y "Como dije, se han producido varias variantes para una variedad de situaciones y entornos diferentes."
            y "El KM1000 es esencialmente solo un KM2000 sin el recubrimiento, dejando la hoja en un color plateado agradable y no reflectante. Bueno si no quieres preocuparte de que el recubrimiento se dañe con el tiempo, supongo... pero el recubrimiento es bueno para la resistencia a la corrosión. Estos son cuchillos para casos de uso especial, creo."
            y "Siguiendo desde ahí, está el KM3000, que abandona la punta estilo tanto a favor de una punta casi como de lanza. Una elección extraña, supongo. La punta estilo tanto era bastante icónica entre la marca Kampfmesser."
            y "Estoy segura de que tiene sus usos, pero... bueno. Creo que mi preferencia es conocida, ¿sí? El diseño tanto permite que la punta del cuchillo funcione como una palanca debido a la fuerza del diseño... pero, pasando de eso..."
            y "Ambos tienen más variantes con vainas y empuñaduras de color arena. Como probablemente podrías adivinar, son para su uso en entornos desérticos; vieron cierta popularidad en Afganistán."
            y "Mencioné esto antes, pero parece que los cuchillos en sí no cambiaron mucho para el ambiente caluroso..."
            y "También hay un KM4000. Eickhorn recibió solicitudes de las Fuerzas Armadas Alemanas para una multifuncionalidad más expandida en sus cuchillos, y esta fue su respuesta. Vuelve a la punta estilo tanto, ¡pero también incluye una sierra completa en el lomo junto con un cortador de alambre real!"
            y "Todas estas derivaciones y variantes nacidas de un solo cuchillo. Son en última instancia lo mismo en el fondo, solo con algunas alteraciones."
            y "Las hojas en sí están compuestas de Böhler N695. Es un tipo particular de aleación diseñada para mantener un filo mejor que el acero 1.4110 anterior. Aunque también podrías encontrar cuchillos siendo producidos con 1.4125..."
            y "Yendo más allá, los cuchillos vienen en variantes parcialmente serradas o de borde recto para una variedad de casos de uso, dependiendo de lo que te veas necesitando más. Muchas personas optan por las versiones parcialmente serradas. Tener una sierra a mano es... bueno, útil."
            y "Y antes de que se me olvide, un rasgo interesante que todos parecen compartir se encuentra en el mango del cuchillo mismo. En la parte inferior hay una punta rompecristales; ¡un bloque sólido de metal diseñado para exactamente lo que suena!"
            y "¡Es en realidad el final de la hoja del cuchillo! Los cuchillos son de espiga completa; es decir, una pieza sólida y completa de acero. ¡En esta situación, se siente como si ninguna parte del metal se desperdiciara!"
            y "La familia Kampfmesser es increíblemente diversa en sus varios enfoques de lo que es esencialmente la misma hoja. Aprecio su trabajo en asegurarse de que haya un poco de algo para todos..."
        "Está bien, [persistent.yuri_nickname]. No tienes que dar una lección de historia sobre cada variación.":

            y "Cierto. Si lo hiciera, estaríamos aquí por un tiempo, creo..."
            y "Ah, pero estoy divagando de nuevo. Mis disculpas, [player]."
            y "¿Hay alguna otra hoja de la que quisieras que hable?"
    call screen knife_wall()

label Kabar:
    y "Oh, sí, el famoso Cuchillo de Utilidad USN Mark 2. Muchos entusiastas militares conocen bien esta hoja; casi con certeza te has encontrado con ella a través de alguna forma de medio."
    y "Tal vez lo conozcas mejor por su nombre contemporáneo; ¡El Ka-Bar!"
    y "Un cuchillo de combate adoptado primero por el Cuerpo de Marines de los Estados Unidos, y más tarde por la Armada. Vio servicio por primera vez en noviembre de 1942, después de que los Marines se quejaran de su hoja de elección anterior, el cuchillo de trinchera Mark I..."
    y "Fue diseñado tanto para ser utilizado en combate, como también como una herramienta. Los entornos en los que se encontraron muchos soldados demostraron ser mucho más amigables con esto a su lado."
    y "Hay una historia divertida sobre el nombre comercial KA-BAR que recuerdo haber leído una vez."
    y "Aparentemente, la compañía propietaria de la marca registrada recibió una carta en algún momento de la década de 1920 de un cazador de pieles."
    y "El cazador afirmó que había usado una de sus hojas para acabar con un oso herido que lo había asaltado después de que su rifle se atascara."
    y "La carta era bastante ilegible, sin embargo; solo fragmentos de la frase 'matar un oso' (kill a bear) se podían leer, lo que salió como 'ka bar'. La compañía encontró que esto era un gran elogio, así como un gran punto publicitario."
    y "Como tal, se estableció la marca 'KA-BAR'; un cuchillo lo suficientemente bueno como para matar incluso a un oso."
    y "Ahora, por supuesto, este informe deja mucho que discutir. Por supuesto, la gran pregunta es; ¿realmente mató a un oso?"
    y "¿Quién sabe? Ciertamente no estoy por averiguarlo... ¡y espero que tú tampoco, [player]!"
    y "Jeje... eso fue divertido. ¿Hay algún otro cuchillo del que te gustaría que hablara?"
    call screen knife_wall()

label Bowie:
    y "Oh, cielos, el Cuchillo Bowie... bastante difícil de perder, ¿no es así, [player]?"
    y "Es una hoja casi cómicamente grande, llegando hasta los 30 cm... es decir, 12 pulgadas de largo."
    y "La historia detrás de él es bastante divertida, también. Originalmente fue hecho para un hombre llamado Jim Bowie para su uso en un duelo."
    y "Creo que el duelo se conoce como la Pelea de Sandbar. Un asunto bastante sórdido terminó siendo..."
    y "Fue menos un 'duelo' y más una pelea entre un gran número de participantes. Se sacaron armas, se dispararon tiros, y bueno..."
    y "El cuchillo tiene una historia fascinante, es el punto de todo esto. Bowie incluso logró ganar con el cuchillo a pesar de haber recibido disparos, puñaladas y casi ser golpeado hasta la muerte."
    y "La hoja misma lleva consigo ese mismo espíritu de resistencia. Sería difícil encontrar una situación en la que este bonito número no ayudaría... ya sea a través de la intimidación o la fuerza. ¿Cómo iba esa línea? 'Ese no es un cuchillo... {i}ESTE{/i} es un cuchillo'?"
    y "¡No es que esté diciendo que deberías ir y buscar peleas! ¡O ponerte en una situación en la que se podría buscar una pelea para empezar!"
    y "No, no... por favor, ¡ten cuidado! ¡Cuchillo o no cuchillo!"
    y "Cielos... siento eso. Me preocupo por ti, de vez en cuando, es todo."
    y "¿Había alguna otra pieza de mi colección que te gustaría discutir?"
    call screen knife_wall()

label Jagdkommando:
    y "Ah, la tri-daga Jagdkommando... Entre los cuchillos más peligrosos del mundo."
    y "Una hoja retorcida de 7 pulgadas hecha de Titanio 6AL-4V, con un mango similar a una granada, que también está hecho del mismo material."
    y "En cuanto a comodidad y manejo, no es el mejor, pero el mango le da al usuario un agarre sólido."
    y "La hoja está vaciada, lo que mejora aún más su aspecto amenazante y reduce el peso total de la daga."
    y "El nombre proviene del grupo de Operaciones de Fuerzas Especiales de Austria, ¡y está a la altura de su tocayo de élite!"
    y "La daga viene con una vaina tubular de 6061-T6 con recubrimiento duro personalizada para proteger la hoja y al usuario, ¡y tiene almacenamiento para una brújula también!"
    y "El estilo único de este cuchillo me intriga mucho, y he leído muchas cosas sobre sus capacidades."
    y "Aunque, como puedes ver, [player], este es solo un cuchillo seguro y desafilado, ya que el real es ilegal en muchos países."
    y "Si hubiera alguien lo suficientemente desafortunado como para ser apuñalado por él, ningún médico podría ni siquiera coser el área penetrada debido a que las hojas retorcidas hacen una herida en forma de pirámide que, incluso si se cosiera desde la superficie, no detendría el sangrado, haciéndola así una herida interna."
    y "Su robustez también es de primera categoría, por lo tanto la durabilidad y confiabilidad se disparan a un punto muy alto, y cuando se combina con el agarre que ofrece, incluso podrías apuñalar a través de ladrillos, si eres lo suficientemente fuerte."
    y "Pero, a pesar de que este solo es un cuchillo desafilado, todavía me gusta por su estética y apariencia general, ¡no es que no me gusten mis otros cuchillos, también...!"
    y "{cps=500}¡Oh no estoy siendo vergonzosa de nuevo!- {/cps}{nw}"
    y "Me alegra que ames los cuchillos tanto como yo, [player]."
    if persistent.lovecheck:
        y "Te amo."
    else:
        pass
    call screen knife_wall()

label Bone:
    y "¿Alguna vez has leído sobre cuchillos hechos de hueso? Han sido utilizados para crear hojas en muchas culturas, y no solo en el pasado lejano."
    y "Leí un estudio recientemente sobre personas en la región Sepik de Nueva Guinea, que los hacían para su uso en batalla tan recientemente como en la década de 1970."
    y "No parece haber un nombre especial para estas armas, por lo que los antropólogos solo las llaman 'dagas de hueso'."
    y "Muchas de esas piezas tienen patrones elaborados grabados en ellas, pero otras son estrictamente utilitarias."
    y "Lo que es especialmente fascinante es que los huesos de los que están hechos se adquieren de dos fuentes completamente diferentes."
    y "Una son los casuarios, un tipo muy grande de ave no voladora común en el área, y la segunda es... sus propios antepasados."
    y "Según los estudiosos, las dagas de origen humano se obtuvieron de los fémures de hombres que se habían probado a sí mismos en batalla, a menudo los propios padres de los guerreros, u otros hombres altamente respetados en la comunidad."
    y "Por lo tanto, llevar una parte de ellos contigo a la batalla se veía como una forma de agregar su fuerza a la tuya."
    y "En cuanto a las dagas de casuario, las aves son vistas con razón como criaturas poderosas: ¡realmente puedes ver su ascendencia de dinosaurios cuando las miras!"
    y "Empuñar una parte de uno también se cree que te imbuye con su fuerza, pero las hechas de hueso humano se tienen en mucha mayor estima."
    y "Un estudio mostró que si bien los fémures humanos y de casuario son básicamente iguales en fuerza, el proceso de tallarlos en hojas es diferente dependiendo de la fuente."
    y "Los huesos de casuario se afeitan más, haciéndolos más delgados pero consecuentemente más débiles. En contraste, los huesos humanos se cortan para mantener su curvatura natural, resultando en una hoja más gruesa pero más fuerte, y presentan grabados decorativos también."
    y "¡De hecho tuve la suerte de adquirir una daga de hueso propia! Oh, no te preocupes, es de un casuario, no de un humano. Al menos... eso es lo que su apariencia simple y perfil general delgado apuntan a que sea."
    y "Aunque la compré en línea, así que es imposible decirlo con certeza..."
    call screen knife_wall()

label Filet:
    y "Uno de los primeros cuchillos que compré por mí misma. En realidad es un cuchillo fileteador, destinado a filetear y preparar pescado."
    y "Típicamente presenta una hoja larga y flexible con una punta afilada, lo que le permite maniobrar alrededor de los huesos y quitar la piel del pescado de manera efectiva."
    y "No es de la más alta calidad, pero sigue siendo genuinamente útil, a diferencia de algunos otros que compré."
    y "Muchos platos tradicionales japoneses involucran pescado, así que saber cómo deshuesarlos es una habilidad útil."
    y "La forma del mango de este cuchillo es en realidad muy práctica, ya que no quieres arriesgar que tus dedos entren en contacto accidental con la hoja afilada si el trabajo resulta volverse resbaladizo."
    y "Pude hacer que Natsuki hablara sobre cocinar/hornear una vez. Fue bastante agradable, hasta que le pregunté si alguna vez hacía comida saludable. Eso... no era a donde había intentado que fuera la conversación."
    y "Previsiblemente, tampoco terminó bien."
    call screen knife_wall()

label Butterfly:
    y "Como probablemente sepas, este es un cuchillo plegable, también conocido como cuchillo mariposa."
    y "Además de su uso obvio como arma, hace una herramienta multiusos encantadora; muchas profesiones casi requieren mantener uno doblado en tu bolsillo."
    y "En consecuencia, encuentro que los cuchillos mariposa a menudo están diseñados para ser tanto hermosos como funcionales. De hecho, poseo más de uno, pero este es, con mucho, el más atractivo."
    y "Se originó en Filipinas y ganó popularidad en todo el mundo debido a sus técnicas únicas de volteo y giro."
    y "Los cuchillos mariposa se utilizan a menudo para trucos, volteos y propósitos de exhibición en lugar de como herramientas de corte prácticas."
    y "Si bien son ilegales en algunas jurisdicciones debido a preocupaciones de seguridad y asociación con actividades delictivas, los cuchillos mariposa son legales y ampliamente coleccionados en muchos lugares."
    call screen knife_wall()

label Grater:
    y "Eso... es un pelador de verduras estilizado. Lo compré en una feria de artesanía, así que tiene alguna esperanza de ser seguro para los alimentos, ¡pero sobre todo me atrajo su diseño elegantemente simple!"
    y "¡No me di cuenta de lo que era hasta que leí las instrucciones de cuidado más tarde!"
    y "Si bien no es raro en la ficción ver espadas de tamaño completo con recortes como este, con el argumento de que hace que la hoja sea más ligera, en realidad es lo opuesto a práctico en la vida real."
    y "Tal diseño solo hace que la hoja sea significativamente más débil."
    y "Las espadas reales son en realidad mucho más ligeras de lo que podrías esperar; contrario a lo que algunas películas te harían creer, no están hechas vertiendo metal fundido en moldes."
    y "En cambio, las hojas se forman plegando."
    y "Este proceso implica calentar el metal y luego golpearlo para darle forma, muchas veces, lo que elimina las impurezas en el material y fortalece enormemente la hoja."
    y "Es verdaderamente una forma de arte."
    y "Además, los cuchillos ralladores son herramientas esenciales en tareas culinarias como adornar, hornear y agregar sabor a los platos."
    y "Vienen en varios tamaños y estilos, incluyendo ralladores de mano, ralladores de caja y ralladores rotativos."
    call screen knife_wall()

label Dagger1:
    y "...Debo confesar que no soy inmune a la 'regla de lo genial'. Lo vi, me gustó, y por eso lo compré. Es funcional como abrecartas, pero nada más."
    call screen knife_wall()

label Dagger2:
    y "Solo una compra impulsiva, me temo. Lo vi y me recordó a una hoja en uno de los libros que estaba leyendo, y no pude resistirme. De hecho compré dos ese día... y luego uno de ellos se rompió cuando intenté usarlo realmente, y golpeó la tabla de cortar."
    y "¡Desearía estar bromeando! En ese momento, me di cuenta de que las hojas decorativas probablemente no deberían usarse en la comida de todos modos."
    call screen knife_wall()

label Empty:
    y "Este lugar aquí es para el cuchillo de cocina que tengo conmigo si tenías curiosidad."
    y "Prácticamente sabes para qué sirve un cuchillo de cocina así que no entraré en muchos detalles."
    call screen knife_wall()

label Kunai:
    y "Supongo que estás familiarizado con este: ¡es un kunai!"
    y "Las representaciones en los medios te harían creer que se usa exclusivamente como arma, pero históricamente era más una herramienta de uso múltiple, más comúnmente para la agricultura o la albañilería."
    y "Probablemente no sea una coincidencia que el kunai se parezca un poco a una paleta de albañilería."
    y "En la ficción, los ves usados en gran medida como armas arrojadizas, pero por lo que he leído, eran más prácticos para apuñalar o cortar."
    y "Otro uso común en los medios son las ayudas para escalar, clavándolos en un acantilado o incluso en un muro de piedra para escalarlo."
    y "Por simple que sea el diseño, el kunai se adapta a muchas funciones diferentes. En términos de armamento, el lazo en el extremo permite atarlos a postes como lanzas improvisadas; el mango también se puede envolver para proporcionar un mejor agarre."
    y "Originalmente utilizados como implemento agrícola para cavar, plantar y hacer palanca, los cuchillos kunai se asociaron más tarde con guerreros ninja y la cultura popular."
    y "Los cuchillos kunai son conocidos por su diseño simple y utilitario, con una hoja resistente y un mango con lazo para mejorar el agarre y el control."
    y "En los tiempos modernos, los cuchillos kunai se utilizan a menudo en el entrenamiento de artes marciales, cosplay y como artículos decorativos o coleccionables."
    call screen knife_wall()

label Paring:
    y "Solo un cuchillo mondador, para preparar frutas y verduras. En realidad es una de las hojas de mayor calidad que poseo; lo heredé en lugar de comprarlo. Si tienes curiosidad, originalmente pertenecía a..."
    y "..."
    y "...No puedo recordar a quién. Realmente, realmente me disgusta ser confrontada con recordatorios de que virtualmente cada recuerdo que tengo, antes de esa semana en el club, es falso."
    y "...de todos modos."
    y "Está diseñado para tareas que requieren precisión y control, como pelar, recortar y dar forma a frutas y verduras."
    y "Los cuchillos mondadores vienen en varios estilos, incluyendo hojas de borde recto, serradas y pico de pájaro (curvas), cada una adecuada para diferentes técnicas de corte."
    y "Son herramientas esenciales tanto para chefs como para cocineros caseros, facilitando preparaciones culinarias delicadas e intrincadas con facilidad."
    call screen knife_wall()

label Damascus:
    y "Este es muy especial: ¡es acero de Damasco!"
    y "El acero de Damasco, del cual se derivan los cuchillos de Damasco, tiene una rica historia que se remonta a siglos."
    y "Los orígenes de la producción de acero de Damasco se pueden rastrear hasta el Medio Oriente, particularmente las regiones de Siria e Irán, tan temprano como el siglo III d.C."
    y "El acero de Damasco histórico era famoso por su resistencia excepcional, nitidez y resistencia, lo que lo hacía muy buscado para espadas, cuchillos y otras armas."
    y "El patrón único en el acero de Damasco se crea a través de un proceso de estratificación y forjado de diferentes tipos de aleaciones de acero, resultando en una apariencia ondulada o rizada distintiva."
    y "Los cuchillos de Damasco modernos se elaboran utilizando técnicas de soldadura por patrón que replican la estética del acero de Damasco tradicional."
    y "Estos cuchillos están construidos a partir de capas de aleaciones de acero de alto carbono y bajo carbono, que se sueldan por forja y se manipulan para crear patrones intrincados."
    y "El proceso de estratificación no solo mejora el atractivo visual del cuchillo, sino que también contribuye a su resistencia, durabilidad y retención de filo."
    y "Los cuchillos de Damasco son posesiones preciadas entre coleccionistas, chefs y entusiastas de cuchillos por su artesanía, rendimiento y significado histórico."
    y "La nitidez y durabilidad del acero de Damasco permiten un corte preciso y sin esfuerzo, lo que lo convierte en una opción preferida entre chefs profesionales y cocineros caseros."
    y "Los cuchillos de Damasco se utilizan a menudo para preparar carnes, verduras, frutas y otros ingredientes con precisión y delicadeza."
    y "Si bien son apreciados por su belleza y artesanía, los cuchillos de Damasco también son herramientas funcionales que sobresalen tanto en rendimiento como en estética."
    call screen knife_wall()

label Kukri:
    y "El cuchillo kukri es una hoja tradicional nepalí caracterizada por su distintivo borde curvado hacia adentro."
    y "Sirve como herramienta de utilidad y arma, ampliamente utilizada por los soldados Gurkha de Nepal y varios grupos étnicos en Nepal."
    y "El kukri presenta una hoja pesada, ponderada hacia adelante, diseñada para cortar, rebanar y hackear materiales resistentes."
    y "Su forma y distribución de peso únicas lo hacen eficiente para cortar madera, limpiar matorrales e incluso situaciones de combate."
    y "El kukri a menudo tiene un significado cultural y religioso en Nepal y se usa comúnmente en ceremonias y rituales."
    call screen knife_wall()

label Saw:
    y "El cuchillo de sierra es una herramienta de corte versátil que combina la funcionalidad de un cuchillo con un borde serrado similar al de una sierra."
    y "Se utiliza comúnmente en actividades al aire libre como acampar, hacer senderismo y situaciones de supervivencia para cortar madera, hueso y otros materiales resistentes."
    y "Los cuchillos de sierra pueden presentar un diseño de hoja fija o plegable, con la porción serrada típicamente ubicada cerca del mango para mayor control y precisión."
    y "El borde serrado permite una acción de corte más agresiva en comparación con los bordes de cuchillo tradicionales, lo que hace que los cuchillos de sierra sean ideales para tareas que requieren cortar materiales fibrosos o duros."
    y "Los cuchillos de sierra plegables son populares entre los entusiastas del aire libre por su portabilidad y características de seguridad, ya que la hoja se puede plegar en el mango cuando no está en uso."
    y "En situaciones de supervivencia, los cuchillos de sierra pueden ser cruciales para recolectar recursos, construir refugios e improvisar herramientas para la caza y la pesca."
    call screen knife_wall()

label purple_a1:
    $ show_chr("A-AAAAA-AAAA")
    y "Hmm, okay [player]."
    $ show_chr("A-ABAAA-ALAA")
    y "¿Uno o más de mis cuchillos despertó tu interés?"
    y "¿O olvidaste el nombre?"
    $ show_chr("A-CBAAA-ALAA")
    y "Bueno, no creo que eso importe."
    $ tc_class.transition("yuri_knives", speed="now")
    hide yuri_sit
    call screen knife_wall()

label purple_a2:
    $ show_chr("A-AAAAA-AAAA")
    y "No veo por qué no."
    y "Seguramente quieres echar un vistazo al resto de la habitación de todos modos."
    if persistent.bg == "yuri_kotatsu_1":
        menu:
            "Al lado delantero del Kotatsu.":
                y "Muy bien."
                $ tc_class.transition("yuri_kotatsu_2", speed=3.0)
            "Al escritorio.":

                y "Muy bien."
                $ tc_class.transition("yuri_desk", speed=3.0)
    elif persistent.bg == "yuri_kotatsu_2":
        menu:
            "Al lado trasero del Kotatsu.":
                y "Muy bien."
                $ tc_class.transition("yuri_kotatsu_1", speed=3.0)
            "Al escritorio.":

                y "Muy bien."
                $ tc_class.transition("yuri_desk", speed=3.0)

    elif persistent.bg == "yuri_desk":
        menu:
            "Al lado trasero del Kotatsu.":
                y "Muy bien."
                $ tc_class.transition("yuri_kotatsu_1", speed=3.0)
            "Al lado delantero del Kotatsu.":

                y "Muy bien."
                $ tc_class.transition("yuri_kotatsu_2", speed=3.0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
