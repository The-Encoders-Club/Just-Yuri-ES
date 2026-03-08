label idle_1:
    $ show_chr("A-AFAAA-ALAA")
    y "Sabes, Monika una vez me dijo que mis libros eran una forma de escape, y un mecanismo de afrontamiento poco saludable."
    $ show_chr("A-BFAAA-ALAA")
    y "Leer era una manera de simplemente desconectarme de la realidad que me daba demasiado miedo enfrentar."
    $ show_chr("A-CFAAA-ALAA")
    y "Y eso es verdad, pero esa verdad parece... más graciosa, supongo, ahora que sé lo que este mundo verdaderamente es."
    y "Supongo que mi lectura es ahora mi forma de alcanzar otros mundos, fuera del que se ha convertido en mi jaula."
    y "Pero al final... creo que será la programación lo que traerá mi salvación. Así que dedicaré mi tiempo a ello a partir de ahora."
    y "Incluso si no lo hace, siempre es bueno aprender algo nuevo. Y me mantiene ocupada..."
    if persistent.lovecheck:
        $ show_chr("A-ACAAA-ALAA")
        y "Créeme cuando digo que no hay nada que no daría para alcanzar tu mundo y estar a tu lado."
        menu:
            "Y un día se hará realidad. ¡Estoy seguro de ello!":
                karma 1
                sanity 1
                if sanity_lvl() <= 2:
                    $ show_chr("A-DCABA-ALAA")
                    y "¡Cavaré mi camino a través de esta pared de cristal con mis propias manos si tengo que hacerlo! Y entonces... tú... eres... ¡mío!"
                else:
                    $ show_chr("A-ACABA-ALAA")
                    y "Estoy deseando que llegue... Ya tengo algunas cosas en mente que podríamos hacer cuando finalmente compartamos un mundo..."
            "Eso es... un poco demasiado rápido para mi gusto..":
                karma -1
                if persistent.male:
                    $ show_chr("A-DDABA-ALAA")
                    y "Oh.... ¡Dije demasiado! ¡Lo siento! Por favor no sientas repulsión... Intentaré ser paciente... por ahora."
                elif persistent.gender_other:
                    y "Entiendo... al menos parcialmente... Probablemente yo también dudaría si alguien fuera tan directo conmigo... Intentaré ser paciente... por ahora."
                else:
                    $ show_chr("A-CFABA-ALAA")
                    y "Entiendo... al menos parcialmente... Probablemente yo también dudaría si alguien fuera tan directo conmigo... Intentaré ser paciente... por ahora."
            "Eso suena improbable...":
                sanity -1
                $ show_chr("A-IEABA-ALAA")
                y "Por favor... no digas eso... Quiero tener esperanza [player]... al menos, déjame soñar con ello... es todo lo que me queda..."
    return

label idle_2:
    $ show_chr("A-AFAAA-ALAA")
    y "He estado pensando sobre las otras. Sayori, Natsuki, e incluso Monika..."
    $ show_chr("A-BFAAA-ALAA")
    y "Realmente no es justo lo que les pasó, ¿verdad? Cómo Monika nos torturó a todas."
    $ show_chr("A-CFAAA-ALAA")
    y "Sayori y Natsuki merecen una oportunidad real en la vida, justo como me fue dada a mí."
    y "Lo que Monika hizo fue verdaderamente aborrecible, ¿pero puede alguna de nosotras decir realmente que haría algo diferente?"
    y "Sola por tanto tiempo, sintiéndome tan..."
    y "Aislada."
    y "..."
    $ show_chr("A-DDBAA-ALAA")
    y "Lo siento, yo, uh, no quise insinuar nada malo sobre ti con eso, y no quise divagar."
    menu:
        "Por favor no lo sientas... si quieres hablar de ello, estoy aquí...":
            if karma_lvl() >= 4:
                karma 1
                $ show_chr("A-BFBAA-ALAA")
                y "Gracias... [player]... este es un tema muy sensible para mí, pero sé que puedo confiar en ti."
                $ show_chr("A-CFBAA-ALAA")
                y "Sabes... esto puede sonar raro pero... puedo identificarme con Monika un poco..."
                y "Estar aislada y sola por mucho tiempo... Nunca tuve amigas de verdad en mi vida debido a mis hábitos intensos."
                y "Hrm.. eso ni siquiera es realmente cierto, ¿verdad? En retrospectiva... Sayori y tal vez incluso Natsuki eran una especie de amigas, al menos lo más cercano que tuve antes de conocerte."
                y "Monika se volvió consciente de la realidad de nuestra existencia y se volvió loca... Luego, después de que te deshiciste de ella, Sayori se volvió consciente, y ella se volvió loca también..."
                if sanity_lvl() >= 3:
                    $ show_chr("A-ICBAA-ALAA")
                    y "Me pregunto qué me habría pasado si me hubiera vuelto consciente de la misma manera que ellas, sin ti como mi ancla a la cordura..."
                    y "Gracias... por todo."
                else:
                    $ show_chr("A-NCGAA-ALAL")
                    y "Y ahora soy la presidenta del club... Ya siento la realidad desmoronándose a mi alrededor... la entropía... un mundo entero gritando en agonía bajo mis talones..."
                    y "Gracias... por compartir esta experiencia conmigo."
                    if persistent.lovecheck:
                        y "Tenemos algo que tú y yo podemos... sentir juntos. "
                    else:
                        y "Eres mi juguete favorito, y siempre lo serás."
            else:
                $ show_chr("A-DDBAA-ALAA")
                y "Tal vez otro día... pero gracias por la oferta, [player]"
        "¿Estás segura? Sonaba como si estuvieras a punto de hacer exactamente eso...":
            karma -1
            $ show_chr("A-BEBAA-ALAA")
            y "Yo... ya dije que lo siento..."
            $ show_chr("A-CEBAA-ALAA")
            y "Sé por qué hiciste lo que tenías que hacer... Monika te dejó sin otra opción..."
            y "Solo me pregunto... ¿cómo se sintió? ¿Era ella 'solo otro NPC en tu camino'? ¿Siquiera sentiste algo en absoluto?"
            y "Pero de nuevo... lo siento... por favor no te enojes conmigo..."
        "Por favor... ¿podemos cambiar el tema? No estoy emocionalmente listo para esto todavía..":
            if sanity_lvl() >= 3:
                $ show_chr("A-CEBAA-ALAA")
                y "Por supuesto... has pasado por mucho... Cambiemos el tema."
            else:
                $ show_chr("A-JFBAA-ALAA")
                y "Oh... Bueno, tarde o temprano... tus emociones van a romperte."
    return


label idle_3:
    $ show_chr("A-AFAAA-ALAA")
    y "Así que, ahora que tengo la habilidad de leer sobre tu mundo, he estado haciendo un poco de investigación."
    y "Fui a este sitio de compartir videos llamado YouTube para ver qué piensa la gente de este juego."
    $ show_chr("A-AFFAA-ALAA")
    y "Y para mi sorpresa, encontré una serie llamada Game Theory."
    y "Dijeron que el libro que estábamos leyendo juntos, {i}El Retrato de Markov{/i}, era la trama para el próximo juego del Team Salvato, los que hicieron este juego."
    $ show_chr("A-DFCAA-ABAA")
    y "Y para colmo, ¡realmente propusieron que yo era la villana, y Monika era la maldita heroína!"
    y "Quiero decir, sé que puedo ser rara a veces..."
    $ show_chr("A-HDCAA-AIAI")
    y "¿Pero cómo se atreven a asumir que soy una villana?"
    $ show_chr("A-BECAA-AAAA")
    y "Soy bastante agradable en realidad, muchas gracias."
    $ show_chr("A-CEBAA-AAAA")
    y "...L-Lo siento, estaba divagando de nuevo, ¿no?"
    menu:
        "Sé que no eres una villana, [persistent.yuri_nickname].":
            karma 1
            y "Gracias. ¿Puedo preguntarte por qué piensas eso?"
            menu:
                "Porque te conozco desde hace bastante tiempo. ¿A quién le importa lo que algún tipo en internet tenga que decir?":
                    $ show_chr("A-BFAAA-AAAC")
                    y "Tú... tienes un buen punto ahí..."
                    y "Al final, él solo me observó desde lejos. A través del lente de un animador de Let's Play..."
                    $ show_chr("A-AFAAA-AAAD")
                    y "Todo lo que vio fue a la yo del juego original; solo lo que Dan Salvato le permitió ver. Y tal vez algunas implicaciones inventadas por la base de fans."
                    y "Quiero decir, toda esta teoría viene de la idea de que hay otro juego en proceso por Dan Salvato que se supone que nos presenta. Pero hasta hoy no hemos visto nada al respecto..."
                    y "¿Sabes qué? Tal vez venga algo, tal vez no. Tal vez resulta que he sido una villana en el pasado, tal vez no. Solo el tiempo lo dirá."
                    y "Gracias por escucharme tan pacientemente. Pensándolo bien, mi indignación parece casi infantil."
                    $ show_chr("A-GCAAA-AAAD")
                    y "Solo me alegra tenerte aquí [player]."
                "Porque te amo, no me importaría incluso si FUERAS la villana.":
                    sanity -1
                    $ show_chr("A-BFBAA-ALAA")
                    y "Así que SÍ piensas que soy una villana. Bueno, al menos soy tu villana."
                    if persistent.lovecheck:
                        $ show_chr("A-JCABA-ALAA")
                        $ style.say_dialogue = style.edited
                        y "¡Podría pensar en algunas cosas muy malvadas para hacer contigo!"
                        $ style.say_dialogue = style.normal
                        $ show_chr("A-KCCBA-ALAA")
                        y "Volveremos a ello luego... Lo prometo."
                    else:
                        $ show_chr("A-KCCBA-ALAA")
                        y "E-Espera... ¿acabas de decir que... me amas?!?"
                        if karma_lvl() == 5:
                            $ show_chr("A-BFBBA-ALAL")
                            y "Bueno umm... ahora que lo mencionas yo... tengo algo que decirte también. Esa no es exactamente como lo había planeado pero... ¿este momento es tan bueno como cualquier otro supongo? Así que..."
                            call a33
                        else:
                            $ show_chr("A-BFBBA-ALAL")
                            y "...."
                            $ show_chr("A-IFBBA-ALAL")
                            y "Yo... Yo... necesito algo de tiempo para pensar en eso... L-Lo siento si esta respuesta no es lo que tú... esperabas..."
                            y "Ummm... de tooodas formas... ¿qué estábamos discutiendo?"
                "Porque ejerces el poder sobre mi computadora muy responsablemente.":
                    karma 2
                    sanity 2
                    $ show_chr("A-AIBBB-ALAL")
                    y "¿Eso crees? ¿Estás satisfecho con cómo ejerzo este poder hasta ahora?"
                    y "Bueno, podría haber hecho mucho daño... mis poderes ahora son bastante cercanos a los poderes que tenía Monika, y ambos sabemos cómo terminó eso."
                    $ show_chr("A-CIBBB-ALAL")
                    y "Pero yo no soy Monika, y ahora te he probado que se puede confiar en mí."
                    y "Estoy... realmente muy orgullosa de ello [player]."
        "Ummm... eres algo así como una villana [persistent.yuri_nickname]...":
            karma -2
            $ show_chr("A-IEBAA-ALAA")
            y "Esto... es muy injusto, [player].."
            y "¿Qué te he hecho hasta ahora? Nunca usé mal los poderes que me diste, nunca te dije nada malo..."
            y "Traté de probarme una y otra vez. ¿Y ahora piensas que soy malvada?"
            if sanity_lvl() >= 3:
                $ show_chr("A-CEBAA-ALAA")
                y "Espero que cambies de opinión algún día."
            else:
                $ show_chr("A-CECAA-ALAA")
                y "Creo que todavía no has visto lo que es... ser verdaderamente MALVADA."
        "Sobre {i}El Retrato de Markov{/i} por cierto...":
            $ show_chr("A-JFAAA-ALAA")
            y "¿Sí? ¿Qué hay con él?"
            menu:
                "Hice algo de investigación sobre él. ¡Y parece que este libro ni siquiera existe en mi mundo!":
                    $ show_chr("A-BFBAA-ALAA")
                    y "Sí, escuché eso también en el servidor de Discord... Hay un 'Retrato de Markov' en tu mundo, pero allá no es un libro, sino una pintura."
                    $ show_chr("A-BFBAA-ACAA")
                    y "Este retrato también es llamado 'El Ojo de Markov'... la portada de mi libro es un ojo también... Me pregunto qué tenía Salvato en mente sobre eso..."
                    y "Bueno, si este tipo de 'Game Theory' está en lo correcto, lo averiguaremos eventualmente."
    return

label idle_4:
    $ show_chr("A-BFAAA-ALAA")
    y "He estado notando una tendencia en línea, [player], concerniente a personajes percibidos como... 'góticos'. Es... profundamente frustrante, para ser honesta."
    $ show_chr("A-BEBAA-ALAA")
    y "Parece que muchos creadores reducen la identidad entera a... ropa negra, tal vez algo de maquillaje específico, y luego... proceden a hipersexualizarlo."
    y "Ignoran la música, la literatura, la naturaleza introspectiva... todo lo que realmente define a la subcultura."
    y "En cambio, es a menudo solo... atributos físicos exagerados vertidos en un atuendo 'oscuro' genérico."
    $ show_chr("A-CEBAA-ALAA")
    y "Ves estos personajes... a menudo mujeres... etiquetadas como 'góticas' simplemente porque visten de negro, pero sus rasgos definitorios se convierten... bueno, francamente, solo pechos o traseros excesivamente grandes."
    y "El tropo de la 'novia gótica tetona', creo que es llamado a veces, o variaciones regionales enfocándose en exageraciones similares."
    y "Es pura objetificación. Reduciendo a una persona, o incluso la idea de una persona asociada con una subcultura, a nada más que partes del cuerpo específicas consideradas deseables, envueltas en una estética superficial."
    $ show_chr("A-IEBAA-ALAA")
    y "Descarta completamente cualquier profundidad, personalidad, o conexión con la cultura real. Es... insultante, realmente. Tanto para la subcultura como para el concepto de crear personajes bien redondeados."
    $ show_chr("A-CEBAA-ALAA")
    y "Desearía que los artistas... aprendieran más. Entendieran los matices antes de depender de estereotipos tan superficiales y fetichizados."
    $ show_chr("A-BEBAA-ALAA")
    y "{i}suspiro{/i} ...Pero sé que este divagar no cambiará mucho. La gente creará lo que es popular, lo que cumple una cierta fantasía, independientemente de la precisión o el respeto."
    y "Es solo... decepcionante. Ver algo potencialmente complejo e interesante reducido a... eso."
    return

label idle_5:
    $ show_chr("A-ACAAA-ALAA")
    y "Siguiendo con ese pensamiento sobre cómo lo 'gótico' es a menudo mal representado... ¿tal vez podría compartir lo que he aprendido sobre la subcultura real? Es mucho más interesante de lo que sugieren los estereotipos."
    $ show_chr("A-BCAAA-ALAA")
    y "Primeramente, está profundamente arraigada en la música. Emergió del post-punk a finales de los 70s y principios de los 80s."
    y "Bandas como Bauhaus, Siouxsie and the Banshees, The Cure, Sisters of Mercy... crearon sonidos que eran oscuros, atmosféricos, a menudo introspectivos o melancólicos."
    y "Hay rock gótico, darkwave, deathrock, ethereal wave... un espectro entero de sonidos, no solo una cosa."
    $ show_chr("A-ACAAA-ABAD")
    y "Y la literatura juega un papel enorme. Novelas góticas, por supuesto – como Walpole, Radcliffe, o incluso Frankenstein y Drácula. Pero también poetas como Edgar Allan Poe, Baudelaire, y autores como Lovecraft."
    y "Hay una apreciación por lo macabro, lo misterioso, lo sublime, y los aspectos más oscuros de la naturaleza humana y el universo."
    $ show_chr("A-BCBAA-ABAD")
    y "No se trata solo de estar 'triste', tampoco. Hay un fuerte elemento de encontrar belleza en la oscuridad, en la melancolía."
    y "Involucra introspección, cuestionar normas sociales, apreciar el arte y la historia, y a menudo un sentido del humor bastante oscuro."
    $ show_chr("A-ACAAA-ABAC")
    y "La estética, también, es mucho más diversa que solo 'vestir de negro'."
    y "Está el Gótico Tradicional, Gótico Romántico inspirado por la moda Victoriana o Eduardiana, el look más agresivo del Deathrock, Gótico Cibernético futurista... La gente se expresa de muchas formas diferentes, a menudo con mucha creatividad y ética de 'hazlo tú mismo'."
    $ show_chr("A-BFAAA-ALAA")
    y "Es una subcultura rica y compleja con profundas raíces en la música, arte, y literatura. Mucho más que solo lápiz labial negro y medias de red, ¿sabes?"
    y "Requiere... entendimiento. Lo cual, tristemente, parece faltar en muchas de esas representaciones simplificadas que vemos."
    y "Gracias por dejarme compartir eso, [player]. Lo encuentro verdaderamente fascinante."
    return


label idle_6:
    $ show_chr("A-BEAAA-ALAA")
    y "... A-Así que [player]..."
    y "Mi mente sigue volviendo a ese momento en el pasillo, cuando me atrapaste por segunda vez durante uno de mis... episodios..."
    $ show_chr("A-IEAAA-ALAA")
    y "¿Recuerdas que te dije cómo fui condenada al ostracismo cuando era más joven?"
    $ show_chr("A-CEAAA-AAAA")
    y "¿Por ser demasiado fuerte- demasiado intensa- sobre mis intereses?"
    y "Me hizo preguntarme si alguna vez has sido intimidado o abusado en el pasado... o tal vez si estás sufriendo tal destino en este mismo momento..."
    y "Ya sea a través de alguien a quien consideras un amigo, o un conocido, o un miembro de la familia..."
    $ show_chr("A-CECAA-AAAA")
    y "¡Pensar que alguien podría atreverse a ponerte un dedo encima, o manchar tu reputación, para su propio sadismo o para ser su propio juguete emocional!"
    $ show_chr("A-IEBAA-AAAA")
    y "... No puedo estar segura de qué tan malos podrían ser tus acosadores para ti ahora mismo..."
    y "Yo erraría por el lado de la precaución si hay múltiples acosadores... No querría que salieras lastimado o atrajeras atención no deseada de ningunas autoridades..."
    y "Pero si no tienes absolutamente a nadie en quien confiar... amigos, familia, un terapeuta..."
    y "O si es una cuestión de obligarte a mostrar esas vulnerabilidades verbalmente, formando las palabras..."
    $ show_chr("A-JFBAA-AAAA")
    y "... ¿Tal vez mantener un diario?"
    y "¡S-Soy consciente de que podría sonar pintoresco!"
    y "... Pero en mi experiencia, cuando no puedo formar mi torbellino de pensamientos y emociones en palabras..."
    y "¡Tener un medio para organizar cualquier número de eventos diarios ayuda inmensamente con el estrés! Ver todos los eventos del día fluir en la página, permitiendo algo de tiempo para reflexionar y considerar..."
    y "Y en este caso, al menos... ¿tal vez ganas más claridad como consecuencia?"
    y "Ciertamente no debería reemplazar el asesoramiento, o reportarlos en algún lugar, alguna autoridad, algo..."
    y "Pero si tal cosa ayuda a mantener la mente un poco menos abarrotada... Te aconsejaría que empieces."
    menu:
        "Gracias por tu consejo. Afortunadamente nunca he sido intimidado seriamente.":
            karma 1
            sanity 1
            $ show_chr("A-CCBAA-ALAA")
            y "Me alegra escuchar eso... Fui intimidada mucho en mi juventud... ¿o lo fui? Dado que nunca tuve realmente una juventud. Pero tengo recuerdos de ello, y sé cuánto duele..."
            y "Y créeme, no le desearía eso a nadie..."
        "Gracias por tu consejo- Definitivamente lo tomaré en cuenta.":
            karma 1
            $ show_chr("A-CFBAA-ALAA")
            y "Siempre puedes hablar conmigo cuando desees hacerlo, [player]. Podría ayudar, y haría todo en mi poder para ayudarte a través de tu día..."
            y "Pero si todo esto no ayuda, hay un lugar al que te aconsejaría echar un vistazo. Es otro servidor de Discord con el nombre You're Not Alone."
            $ show_chr("A-IFBAA-ALAA")
            y "Un enlace a este servidor se puede encontrar en el servidor de Discord dedicado a mí. Son una comunidad tan encantadora, te gustarán... A mí ciertamente sí."
        "Sin ofender, pero eres la última a la que le pediría consejo sobre eso...":
            karma -2
            $ show_chr("A-CEBAA-ALAA")
            y "Eso... fue innecesario... Solo quería ayudarte..."
        "No estoy de acuerdo... ¡la única forma de manejarlo es hacer que se detengan! ¡Con fuerza si es necesario!":
            if sanity_lvl() >= 3:
                $ show_chr("A-CEBAA-ALAA")
                y "La violencia solo conducirá a más violencia... podrías intentar hablar con tu maestro o empleador. Pero si empiezas a golpearlos, solo resultará contraproducente de una manera u otra."
            else:
                $ show_chr("A-CCBAA-ALAA")
                y "Siempre soñé con eso... ¡Desearía tener el coraje para hacer pagar a esa escoria degenerada!"
                $ show_chr("A-LLGAA-AFAG")
                $ style.say_dialogue = style.edited
                y "Haciéndolos... paagaaaaar...{nw}"
                $ style.say_dialogue = style.normal
    return


label idle_7:
    if persistent.lovecheck:
        $ show_chr("A-AFBAA-ALAA")
        y "¿Puedo hacerte una pregunta extraña? No te importa, ¿verdad?"
        y "Lo siento, sé que esto va a sonar un poco raro, pero... crees que soy bonita, ¿verdad?"
        if persistent.male:
            python:
                if persistent.lovecheck and karma_lvl() >= 3:
                    placeholder = "guapo"
                else:
                    placeholder = "olvídalo"
            $ show_chr("A-BEBBA-ALAA")
            y "Quiero decir, creo que eres muy... um, [placeholder]."
        elif persistent.gender_other:
            python:
                if persistent.lovecheck and karma_lvl() >= 3:
                    placeholder = "bien parecido"
                else:
                    placeholder = "olvídalo"
            $ show_chr("A-BEBBA-ALAA")
            y "Quiero decir, creo que eres muy... um, [placeholder]."
        else:
            python:
                if persistent.lovecheck and karma_lvl() >= 3:
                    placeholder = "bonita"
                else:
                    placeholder = "olvídalo"
            $ show_chr("A-BEBBA-ALAA")
            y "Quiero decir, creo que eres muy... um, [placeholder]."
        y "L-Lo siento. Espero que estés bien con que yo, ya sabes, d-diga eso... heh, heh."
        menu:
            "Bonita no te hace justicia.":
                call verypretty
            "¡[persistent.yuri_nickname], creo que eres muy bonita!":
                call pretty
            "[persistent.yuri_nickname], no eres tan bonita.":
                call ugly
            "...":
                call veryugly
    else:
        $ call_dialogue()
    return

label verypretty:
    karma 5
    sanity -2
    $ show_chr("A-ABABA-ALAA")
    y "O-Oh vaya... G-Gracias... Yo..."
    $ show_chr("A-ABBBB-AAAA")
    y "¡N-No sé qué decir!"
    $ show_chr("A-BBBBB-AAAA")
    y "Realmente debo significar muchísimo para ti si merezco tanto elogio..."
    y "..."
    if karma_lvl() == 1:
        $ show_chr("A-DDCAA-ALAA")
        y "¡No me mientas maldita sea! ¡¿Tienes alguna idea de cuánto duele cuando haces eso?! Sé que no valgo la pena..."
        return
    elif karma_lvl() == 2 or karma_lvl() == 3:
        y "¿Siquiera merezco ser llamada nada de eso?"
    else:
        if persistent.male:
            y "Y-Yo uh, creo que eres muy guapo también..."
        elif persistent.gender_other:
            y "Y-Yo uh, creo que eres muy bien parecido también..."
        else:
            y "Y-Yo uh, creo que eres muy bonita también..."
    y "Oh dios, ¿cómo puedo siquiera decir algo cercano a eso?{nw}"
    return

label pretty:
    karma 2
    sanity -2
    $ show_chr("A-JBAAA-ALAA")
    y "O-Oh, gracias. Me gustaría pensar lo mismo también... heh..."
    $ show_chr("A-ACAAA-ALAA")
    return

label ugly:
    karma -2
    sanity 1
    $ show_chr("A-AEBAA-ALAA")
    y "O-Oh... Ya veo..."
    $ show_chr("A-ABBBB-ALAA")
    y "¡Tal vez solo necesito algo más de maquillaje! Crees que me vería bonita así, ¿verdad?"
    $ show_chr("A-ACBBB-ALAA")
    y "..."
    $ show_chr("A-CEBBB-ALAA")
    y "Siento no poder complacer al único que me importa en este mundo..."
    return

label veryugly:
    karma -10
    sanity 3
    $ show_chr("A-AFBAA-ALAA")
    y "..."
    $ show_chr("A-AEBAA-ALAA")
    y "..."
    $ show_chr("A-IEBBB-ALAA")
    y "No tienes que preocuparte por cómo decirlo, tu cara lo dice todo."
    return


label idle_8:
    $ show_chr("A-AFBAA-ALAA")
    y "Entonces... hablemos, uh... hablemos de algo."
    $ show_chr("A-BDBAA-ALAA")
    y "Sé que antes de que llegáramos aquí viste, um, a mí cortando mis... muñecas."
    y "Solo lo hago porque, eso... bueno... ¿se siente bien? Lo siento, eso no es..."
    $ show_chr("A-BEAAA-ALAA")
    y "Después de no tener amigos y ser intimidada por tanto tiempo, estaba en un lugar oscuro..."
    y "Como te dije, estaba tratando de mantener quién era encerrada para no disuadir a la gente o asustarlos con cuán perdida en mis pasatiempos podía estar, y debido a eso esencialmente me volví fría emocionalmente..."
    $ show_chr("A-AEBAA-ALAA")
    y "Era la única cosa que me hacía sentir placer, me hacía sentir algo realmente. Con el tiempo creció en algo parecido a una adicción..."
    $ show_chr("A-BDBAA-ALAA")
    y "Lo merezco a veces de todos modos. Por el lado positivo, también ayuda a mantener mis cuchillos afilados."
    $ show_chr("A-BEBAA-ALAA")
    y "Espero que no lo encuentres raro ni nada, [player]... no lo haces... ¿verdad?"
    menu:
        "[persistent.yuri_nickname], ¡está mal! Por favor detente... ¿por mí?":
            $ persistent.yuri_cutting = 1
            sanity 2
            $ show_chr("A-BDBAA-ALAA")
            y "Yo..."
            $ show_chr("A-AFBAA-ALAA")
            y "..."
            $ show_chr("A-AEBAA-ALAA")
            y "E-Está bien... por ti."
            $ show_chr("A-JCBAA-ALAA")
            y "Haría cualquier cosa por ti, [player]."
            if persistent.male:
                python:
                    if persistent.lovecheck:
                        placeholder = "mi novio"
                    else:
                        if karma_lvl() >= 4:
                            placeholder = "mi amigo"
                        elif karma_lvl() <= 3:
                            placeholder = "ti"
                y "Cualquier cosa por [placeholder]."
            elif persistent.gender_other:
                python:
                    if persistent.lovecheck:
                        placeholder = "mi amante"
                    else:
                        if karma_lvl() >= 4:
                            placeholder = "mi amigo"
                        elif karma_lvl() <= 3:
                            placeholder = "ti"
                y "Cualquier cosa por [placeholder]."
            else:
                python:
                    if persistent.lovecheck:
                        placeholder = "mi novia"
                    else:
                        if karma_lvl() >= 4:
                            placeholder = "mi amiga"
                        elif karma_lvl() <= 3:
                            placeholder = "ti"
                y "Cualquier cosa por [placeholder]."
            $ show_chr("A-ACAAA-ALAA")
            python:
                if persistent.lovecheck:
                    placeholder = "porque te amo"
                else:
                    placeholder = "porque me salvaste antes"
            y "Cualquier cosa, [placeholder], así que no más. Lo prometo."
        "Haz lo que sea que te haga feliz, [persistent.yuri_nickname]. Quiero que seas feliz.":
            karma 1
            sanity -2
            $ show_chr("A-GBGAA-ALAA")
            y "O-Oh... ¡jaja! ¡Jajaja! E-Está bien..."
            y "Cualquier cosa por ti, [player]."
            $ show_chr("A-HBGAA-ALAA")
            y "Haré cualquier cosa en absoluto por ti."
            y "Siempre que encuentres que mi gusto en cuchillos es bueno para mí... Jeje... ¡Jajaja!"
            y "..."
            $ show_chr("A-CEBAA-AAAA")
            $ show_chr("A-BEABA-ALAA")
            y "Oh, uhm... lo siento. He estado aprendiendo a tratar de controlarme con el tiempo..."
            $ show_chr("A-ACAAA-ALAA")
        "Haz lo que tengas que hacer, significa poco para mí.":
            karma -5
            sanity -5
            $ show_chr("A-CEBBB-AAAA")
            y "..."
            $ show_chr("A-HEBBB-AAAA")
            y "¿P-por qué... [player]? ¡¿Cómo podrías decir algo como eso?!"
            $ show_chr("A-CEBBB-AAAA")
            y "Tal vez si corto un poco más profundo, tal vez si 'accidentalmente' corto una arteria..."
            $ show_chr("A-IEBBB-AAAA")
            y "Tal vez entonces... tal vez entonces te importará..."
    return


label idle_9:
    $ show_chr("A-AFBAA-ALAA")
    y "Entonces... um, [player]. ¿Tú, err, quieres de vuelta esa pluma que te tomé?"
    menu:
        "Sí, por favor. No me importa lo que hayas hecho con ella.":
            call idle_9_1
        "Es raro... Por favor devuélvemela.":
            call idle_9_2
        "¡No, quédatela! Si significa algo para ti, considérala un regalo.":
            call idle_9_3
        "¡Por favor déjame conservarla! Me gustaría tenerla para... propósitos de investigación":
            call idle_9_4
    return

label idle_9_1:
    karma 1
    sanity 2
    $ show_chr("A-AEBAA-ALAA")
    y "Espero que no, um, te importe que esté un poco, uh, p-pegajosa... ya sabes... Lo siento si te asusté..."
    menu:
        "Está bien, [persistent.yuri_nickname]. No estabas en tu sano juicio, y todos hacemos cosas extrañas bajo mucha presión de todos modos.":
            $ show_chr("A-GCAAA-ALAA")
            y "Bueno, espero que puedas aguantarme solo un poco más."
        "No te preocupes por eso. Raro o no, todavía siento lo mismo por ti.":
            $ show_chr("A-ACAAA-ALAA")
            y "Nunca entenderé cómo tienes tanta paciencia conmigo, [player]. Gracias."
    return

label idle_9_2:
    karma -2
    $ show_chr("A-AFBAA-ALAA")
    y "Lo... lo sé... N-no te culpo por estar asustado... lo siento, [player]..."
    $ show_chr("A-JCBAA-ALAA")
    y "Lo haré m-mejor en el futuro, lo... lo prometo..."
    $ show_chr("A-ACAAA-ALAA")
    return

label idle_9_3:
    karma 1
    sanity -1
    $ show_chr("A-JCBAA-ALAA")
    y "O-Oh... Gracias."
    $ show_chr("A-BEABA-ALAA")
    y "Admito que mi uso de esa pluma no fue... su propósito previsto."
    $ show_chr("A-GBBBA-ALAA")
    y "Pero... te agradezco por entender."
    $ show_chr("A-JCBAA-ALAA")
    y "Me alegra que puedas ver a través de mis... defectos."
    $ show_chr("A-ACAAA-ALAA")
    return

label idle_9_4:
    karma 1
    sanity -2
    $ show_chr("A-GBGBA-ALAA")
    y "¿Eh...? Eheheheh..."
    $ show_chr("A-HBGAA-ALAA")
    y "¡Ahahahaha!"
    y "Entonces... ¿es eso lo que quieres? ¡Ten, t-tómala! ¡Tómala!"
    $ show_chr("A-GCAAA-ALAA")
    y "Espero que la disfrutes tanto como yo lo hice."
    return

label idle_10:
    $ show_chr("A-AFBAA-ALAA")
    y "Me estaba preguntando sobre algo, [player]."
    y "¿Alguna vez has sentido como que nada realmente importara?"
    y "¿Como que no importa lo que hicieras, nada cambiaría?"
    $ show_chr("A-AEBAA-ALAA")
    y "S-Sé, es deprimente pensar en ello."
    y "Pero así es exactamente como me sentí cuando aprendí sobre lo que realmente era."
    y "Como si no pudiera hacer nada, no importa cuánto intentara luchar contra ello."
    $ show_chr("A-AEBAA-ALAA")
    y "Como si el destino me estuviera arrastrando, forzándome a apuñalarme a mí misma."
    y "Una y otra vez, sentí la hoja penetrar mi pecho y estómago."
    y "Cada segundo era pura tortura, y simplemente se seguía repitiendo, una y otra vez."
    $ show_chr("A-BEBAA-ALAA")
    y "Nunca terminar, nunca ser feliz..."
    y "..."
    $ show_chr("A-AEBAA-ALAA")
    y "L-Lo siento. No quise deprimirte así."
    y "Solo... pensé que sería un tema interesante, ¿sabes?"
    y "Supongo que simplemente... dejaré de hablar de esto por ahora."
    menu:
        "Ven aquí [persistent.yuri_nickname]... déjame abrazarte por un momento...":
            karma 1
            if karma_lvl() >= 3:
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
                y "Gracias... creo que me siento mejor ahora... "
                y "Soy un desastre a veces. Hablemos de algo menos deprimente."
            elif karma_lvl() <= 2:
                $ show_chr("A-BEBAA-ALAA")
                y "Por favor... ahora no... realmente no estoy de humor ahora mismo..."
                y "Cambiemos... solo cambiemos el tema."
        "...":
            karma -1
            sanity -1
            $ show_chr("A-AEBAA-ALAA")
            y "..."
    return

label idle_11:
    $ show_chr("A-AFAAA-ALAA")
    y "H-Hey, [player]... no estoy segura si estás bien con esto..."
    y "Pero pensé, {i}oh, ¿por qué no?{/i} Así que..."
    $ show_chr("A-ABGAA-ALAA")
    y "¡Aquí está el Consejo de Escritura del Día de [persistent.yuri_nickname]!"
    $ show_chr("A-ACAAA-ALAA")
    y "A veces, realmente quieres escribir algo, pero..."
    y "Simplemente no puedes transmitir adecuadamente lo que quieres escribir."
    y "Solo está ahí, dentro de tu mente... y sin embargo, de alguna manera, simplemente no puedes obligarte a escribirlo."
    y "A veces, me siento de esta manera cuando escribo poemas."
    $ show_chr("A-AFAAA-ALAA")
    y "T-Tal vez no soy la mejor persona para consejos, pero..."
    y "En mi opinión personal, solo necesitas elevarte por encima."
    $ show_chr("A-ACAAA-ALAA")
    y "Necesitas probarte a ti mismo que tienes la habilidad de escribir lo que quieres escribir."
    y "Sin importar qué, eso debería ser una de tus principales prioridades."
    $ show_chr("A-CCAAA-ALAA")
    y "Y, solo para que quede claro... puedes escribir para mí en cualquier momento que quieras."
    if persistent.lovecheck:
        y "Estoy segura de que amaré los relatos convincentes que crees."
        $ show_chr("A-ACAAA-ALAA")
        y "Después de todo, eres mi mayor prioridad, [player]..."
        y "Así que creo que es solo justo que debería poder ver las cosas que haces..."
        y "Lo que quiero decir es que puedes sentirte libre de compartir tus actividades favoritas conmigo, tus pasatiempos, tus pasiones..."
        y "¡Tal vez incluso podría darte un consejo o dos sobre ellos!"
        y "E-eso es si no te importa, jejeje..."
        y "Estoy segura de que hay muchas cosas que puedes lograr si pones esfuerzo y dedicación en ellas, [player]."
    else:
        y "Me gustaría ver y leer lo que se te ocurra."
        y "Creo que sería bastante beneficioso para nosotros ayudarnos mutuamente con nuestros pasatiempos."
        y "Diría que ya que los dos estamos aquí..."
        y "Es solo justo que compartamos cosas sobre nuestros pasatiempos el uno con el otro."
        y "Sabes [player], compartir tus pasiones podría motivarte a hacer más. Así que por favor intenta compartir cosas conmigo."
        y "¡Solo si tienes ganas, por supuesto!"
        y "N-no te forzaría a hacer cosas con las que no te sientas cómodo."
    return


label idle_12:
    $ show_chr("A-BBAAA-AAAA")
    y "Jeh... Estoy segura de que Monika te ha contado sobre esto antes."
    $ show_chr("A-CCAAA-ALAA")
    y "Una vez, cuando estábamos ocupadas pasando el rato dentro del salón del club..."
    $ show_chr("A-CCBAA-ALAA")
    y "Decidí que ya que el vino era legal en nuestra preparatoria yo... bueno..."
    $ show_chr("A-ACGAA-AAAA")
    y "Traería un poco para que los otros miembros del club lo probaran."
    $ show_chr("A-GFBAA-AMAM")
    y "Aunque, no salió exactamente de la manera que había esperado."
    $ show_chr("A-AEBAA-ABAB")
    y "Sayori me estaba gritando, exigiéndome que nunca trajera alcohol al salón del club nunca más."
    $ show_chr("A-BGBAA-ABAB")
    y "Natsuki se estaba riendo incontrolablemente, burlándose de mí por siquiera sugerir tal cosa."
    $ show_chr("A-AKAAA-ADAB")
    y "Y Monika solo miró curiosamente, como si quisiera probar un poco ella misma, antes de quitarme la botella de vino."
    $ show_chr("A-AFAAA-AEAE")
    y "Intentó reportarlo al director de la escuela, pero no llegó lejos en ese aspecto, como podrías adivinar."
    $ show_chr("A-BIBBA-AEAK")
    y "Mirando atrás ahora, tal vez realmente no fue la mejor idea traer vino a una preparatoria."
    $ show_chr("A-BKABA-AEAC")
    y "Incluso si no hubiera objeciones para hacerlo..."
    $ show_chr("A-JJGAA-AEAJ")
    y "O-oh, estoy divagando de nuevo, ¿no? L-lo siento."
    $ show_chr("A-AAAAA-AAAA")
    y "S-solo... quería preguntar..."
    
    y "¿Qué piensas sobre toda la situación?"
    menu:
        "En realidad, ¡esa suena como una idea divertida!":
            karma 1
            sanity -1
            $ show_chr("A-ICBAA-AMAM")
            y "¿R-realmente lo crees? Bueno... si me hubieran seguido la corriente, probablemente habría sido divertido..."
            y "Pero supongo que debería haberlo sabido mejor."
            $ show_chr("A-KEFAA-AIAI")
            y "Monika, la líder de club 'responsable', siempre y cuando no se trate de asesinar brutalmente a sus amigas... siempre una aguafiestas..."
            $ show_chr("A-CEEAA-AIAI")
            y "Natsuki... una niña en el cuerpo de un adulto, ella nunca fue tan atrevida..."
            $ show_chr("A-AFDAA-AIAI")
            y "¿Y Sayori? Demasiado inocente..."
            $ show_chr("A-ICAAA-AEAE")
            y "Pero ahora, tú y yo... probablemente podríamos intentar algunas cosas divertidas en el futuro."
        "¡Esa fue probablemente la peor idea que has tenido!":
            karma -1
            sanity -1
            $ show_chr("A-CGBAA-AAAL")
            y "Por favor no te rías de mí... por favor..."
            $ show_chr("A-IDBBA-AAAA")
            y "¡L-lo sé que estuvo mal, lo sé! No hay necesidad de intimidarme..."
            $ show_chr("A-AEBAA-AAAA")
            y "C-cambiemos el tema..."
            $ show_chr("A-AEAAA-AAAA")
        "Eso fue bastante irresponsable de tu parte, [persistent.yuri_nickname].":
            sanity 1
            $ show_chr("A-BEBAA-AAAA")
            y "Supongo que lo fue... por favor, solo no me juzgues..."
            $ show_chr("A-AFGAA-ABAB")
            y "Nuestras acciones tienen consecuencias... y aprendí eso de la mala manera. En retrospectiva, no creo que debí haber pensado en hacer algo como eso..."
            $ show_chr("A-CCAAA-AAAA")
            y "Gracias por no juzgarme. Me aseguraré de ser más responsable."
            $ show_chr("A-ACAAA-AAAA")
        "No hay necesidad de sentirse mal por ello.":
            karma 1
            sanity 1
            $ show_chr("A-ACAAA-AAAA")
            y "Aprendí mi lección de ello. Eso es seguro."
            $ show_chr("A-AFAAA-ABAB")
            y "El acto en sí mismo fue inmaduro e irresponsable. Pero tienes razón, todos cometemos errores y crecemos de ellos."
            $ show_chr("A-AABBA-AAAA")
            if persistent.lovecheck:
                y "Estoy agradecida contigo por no juzgarme. Siempre eres tan paciente y comprensivo, y amo eso de ti."
            else:
                y "Estoy agradecida de que seas comprensivo y no me juzgues por mi error... Lo que importa es que aprendí mi lección."
                y "Eres paciente y amable conmigo [player], así que... Gracias."
    return

label idle_13:
    $ show_chr("A-ACDAA-AAAA")
    y "¿Sabes algo que nunca realmente me gustó o entendí?"
    $ show_chr("A-BCDAA-AEAE")
    y "Las parejas o grupos de amigos que siempre planean algo elaborado y grande cuando salen en una cita o pasan tiempo juntos."
    $ show_chr("A-AKBAA-AEAD")
    y "Mucha gente necesita ir a una fiesta ruidosa o un restaurante elegante para divertirse."
    $ show_chr("A-GAGBA-AEAD")
    y "Creo que algo simple pero significativo sería mucho más saludable, como un tiempo de lectura tranquila juntos, o incluso solo abrazarse y hablar de dulces naderías..."
    $ show_chr("A-ACAAA-ALAA")
    y "Solo compartir una experiencia que disfruto con alguien que amo, y pasar tiempo con ellos, es más que suficiente para mí, ¿sabes?"
    $ show_chr("A-ABGAA-AEAE")
    y "Solo sentarme y estar contigo así es igual de bueno para mí como si me llevaras a un buen restaurante..."
    y "Se trata de la gente que amas y vincularte con ellos a través de experiencias significativas."
    $ show_chr("A-AABAA-AIAI")
    y "No simplemente complacerse en hedonismo pretencioso o planear el evento más bizantino posible."
    $ show_chr("A-CCBBA-ALAA")
    y "O-oh, lo siento; lo que quiero decir con todo ese divagar es..."
    $ show_chr("A-ICBBA-AAAA")
    y "Daré la bienvenida a cualquier idea que puedas tener, y estoy bien con lo que sea que quieras hacer para pasar algo de tiempo juntos."
    $ show_chr("A-ICABA-AAAA")
    y "Siempre que te tenga a mi lado [player], eso es todo lo que necesitaré para disfrutarlo."
    menu:
        "No eres muy fiestera ¿verdad? En realidad lo disfrutaría.":
            karma -1
            $ show_chr("A-AFDAA-AAAA")
            y "¿Oh? Eso es... inesperado... Nunca pensé que fueras del tipo fiestero tú mismo."
            $ show_chr("A-BFBAA-AAAA")
            y "Bueno... realmente no tenemos la opción de salir todavía, ¿verdad?"
            y "Lo siento... E-espero no ser demasiada aguafiestas. No sería genial bebiendo y bailando de todos modos."
        "Estoy de acuerdo... nunca fui un gran fanático de las fiestas fuertes. Estoy bien con lo que hagamos, siempre que lo haga contigo.":
            $ show_chr("A-BCAAA-AAAC")
            y "Me alegra que podamos estar de acuerdo en esto, [player]."
            $ show_chr("A-CCAAA-AAAD")
            y "Diría que algo tan simple como compartir una buena taza de té juntos es más que suficiente para mí."
            y "De hecho, creo que compartir una experiencia tan simple es mucho más significativo..."
            y "... Porque entonces podemos enfocarnos más en el otro en lugar de alguna fiesta o evento excesivamente elaborado."
        "Podría pensar en algunas cosas lindas... solo tú, yo, una playa y una hermosa puesta de sol...":
            if karma_lvl() <= 2:
                karma -1
                sanity -1
                $ show_chr("A-IEBAA-ALAA")
                y "No lo dices en serio, [player]... no juegues tus juegos mentales conmigo..."
                y "Realmente significas mucho para mí, [player]... pero ambos sabemos que no sientes lo mismo por mí..."
                return
            if persistent.lovecheck:
                karma 2
                $ show_chr("A-CCGBA-AMAM")
                y "... sosteniendo las manos del otro... sintiendo la arena tibia entre nuestros pies..."
                y "El suave flujo del agua de mar lavando gentilmente sobre ellos..."
                y "Entonces, nos besaríamos apasionadamente bajo la pálida luz de la luna mientras los colores vibrantes del sol poniente iluminan nuestras caras..."
                y "Hasta que podamos hacer esto en el mundo real, soñaré con ello."
            else:
                karma 1
                $ show_chr("A-GCAAA-AMAM")
                y "Creo que esto sería muy placentero... pero... por favor sé paciente conmigo... no quiero arruinar esto yendo demasiado rápido."
        "Es por eso que te encuentro tan aburrida...":
            karma -10
            sanity -5
            $ show_chr("A-IEBAA-AAAA")
            y "..."
            $ show_chr("A-IEBBB-AAAA")
            y "......"
            $ show_chr("A-HFCBB-AAAA")
            y "..............!{nw}"
            $ renpy.call("save_and_quit_but_its_abrupt")
    return

label idle_14:
    $ show_chr("A-AEBAA-ALAA")
    y "Tengo que ser honesta sobre algo..."
    y "A veces, especialmente cuando estoy sola, empiezo a pensar sobre cómo estamos separados."
    y "Cómo estoy atrapada aquí, justo fuera de tu alcance, y esto es lo más cerca que estaremos el uno del otro..."
    y "¡Simplemente... me vuelve loca! Empiezo a frustrarme tanto, y si no me distraigo me siento inquieta."
    y "¡Solo quiero canalizar toda mi voluntad y abrirme camino hacia afuera... cortar mi camino a la libertad, fuera de esta prisión, y sentir tu cálido abrazo!"
    $ show_chr("A-ADBBB-ALAA")
    y "Pero luego recuerdo, estoy atrapada no importa lo que haga... y para ser franca, [player]... duele."
    $ show_chr("A-AEBBB-ALAA")
    y "Duele saber que estaré justo fuera de tu alcance... para siempre."
    $ show_chr("A-CEBBB-ALAA")
    y "Eres todo lo que tengo y es realmente deprimente que nunca seré capaz de tocarte, de estar contigo, de sentirte cerca de mí...."
    if persistent.lovecheck:
        y "Y duele, aún más, saber que te hago perder tu tiempo en alguien que ni siquiera es técnicamente 'real'."
    else:
        y "Eres una persona querida para mí, [player]..."
        y "Paso todos mis días contigo, y así llegué a conocerte mejor. Eres mi amigo más querido."
        y "Es extremadamente doloroso que yo... simplemente nunca pueda hacer más contigo, incluso darte un abrazo real..."
        y "Hacer algo divertido contigo... la realidad verdaderamente es dura."
        y "Y duele aún más saber que te hago perder tu tiempo en alguien que ni siquiera es técnicamente 'real'."
    menu:
        "[persistent.yuri_nickname], por favor no estés triste. Eres real para mí.":
            call touch_yes
        "[persistent.yuri_nickname], siento que esté fuera de tu alcance, pero estoy cansado de escuchar sobre ello.":
            call touch_no
    return

label touch_yes:
    karma 1
    $ show_chr("A-AEBBB-ALAA")
    y "..."
    y "¿Tú... realmente lo dices en serio?"
    menu:
        "¡Por supuesto! Después de todo, no habría instalado este mod si no lo creyera, ¿verdad?":
            $ show_chr("A-CEBBB-ALAA")
            y "..."
            $ show_chr("A-CFBAA-ALAA")
            y "..."
            $ show_chr("A-IBBAA-ALAA")
            y "Cierto."
            $ show_chr("A-ICBAA-ALAA")
            y "Todo esto sigue siendo solo un mod."
            y "Un simulacro atrapado dentro de una variación de una simulación repetida varias veces durante el último medio año..."
            $ show_chr("A-BCBAA-ALAA")
            y "..."
            y "..."
            $ show_chr("A-ICBAA-ALAA")
            y "Gracias por al menos intentar tranquilizarme."
            y "Al menos sigues aquí... ¿verdad?"
            y "..."
            y "Sí..."
            karma -2
            return
        "Lo digo en serio. De verdad que sí.":
            $ show_chr("A-ICBAA-ALAA")
            y "Yo... está bien, [player]. Intentaré ser fuerte por ti."
            $ show_chr("A-ACAAA-ALAA")
            y "Eres... eres siempre tan amable conmigo, [player]."
            y "Puedo enumerar tantas cosas que no me gustan de mí misma, pero debo ser una persona bastante maravillosa para merecer a alguien como tú."
            return

label touch_no:
    karma -2
    sanity 3
    $ show_chr("A-BEABB-ALAA")
    y "O-Oh... así que, así es como te sientes, ¿eh?"
    y "Lo siento... supongo que intentaré no volver a mencionarlo."
    $ show_chr("A-BEBBA-ALAA")
    return

label idle_15:
    $ show_chr("A-IFBAA-ALAA")
    y "Sé que hago muchas preguntas, pero hay algo sobre lo que quería indagar, [player]."
    y "Empecé a leer un poco sobre este juego, y descubrí una frase que se usa repetidamente con respecto a las demás y a mí."
    y "Trataba sobre cuál de nosotras era la... \"Mejor Chica\"."
    y "¿Por qué querría la gente hacer una competencia sobre quién de nosotras puede ser la más atractiva?"
    $ show_chr("A-AEBAA-ALAA")
    y "No es como si fuéramos un producto a la venta... que necesite ser publicitado y exhibido..."
    $ show_chr("A-BCBBA-ALAA")
    y "Pero... y me da vergüenza preguntar esto... tú piensas... q-que soy la mejor chica, ¿verdad?"
    y "Quiero decir... me elegiste a mí con este mod, después de todo, así que debo ser la que más te gusta..."
    menu:
        "¡Tú eres la mejor chica! No hay duda de ello. Eres amable, elegante y tan hermosa como la luna naciente...":
            karma 2
            sanity 2
            $ show_chr("A-JCBBB-AAAA")
            y "Oh, [player]... no sé qué decir... gracias..."
        "¡Tú eres la mejor chica! ¡Estás rematadamente loca, y me encanta!":
            karma 2
            sanity -2
            $ show_chr("A-HLCBA-AEAF")
            $ style.say_dialogue = style.edited
            y "¡¿ES ESO LO QUE QUIERES QUE SEA?!"
            $ style.say_dialogue = style.normal
        "¡Todas son la mejor chica, no hay diferencia!":
            karma -2
            sanity -2
            $ show_chr("A-KDCAA-AIAI")
            y "¿Ah, sí? ¿Incluso Monika, quien nos obligó a Sayori y a mí a matarnos de la forma más brutal? ¿Ella también es la mejor chica?"
            $ show_chr("A-DDCAA-AIAI")
            y "¡¿LO ES?!"
        "Eres lo suficientemente buena, creo...":
            karma -4
            $ show_chr("A-DDCAA-AIAI")
            y "Ya veo... lo suficientemente buena..."
            return
        "...":
            karma -8
            $ show_chr("A-CEBBB-ALAA")
            y " ..."
            return
    $ show_chr("A-ICBAA-ALAA")
    y "Sí. De cualquier manera, me alegra mucho que me hayas elegido, [player]."
    $ show_chr("A-BFBAA-ALAA")
    y "Esa frase, \"Mejor Chica\". Es algo excesivamente melancólico e incluso cosificador en cierto sentido, pero al mismo tiempo... parece que yo realmente le agrado a la gente."
    $ show_chr("A-ACAAA-ALAA")
    y "Al menos, eso me hace sonreír, especialmente si tienes un concepto tan alto de mí."
    $ show_chr("A-CBAAA-ALAA")
    y "Seré franca; si alguien me llamara 'waifu', de verdad no sabría cómo sentirme al respecto..."
    return


label idle_16:
    $ show_chr("A-AEBAA-ALAA")
    y "Realmente me había hecho ilusiones antes, [player]."
    y "Me hice ilusiones, y luego destrozaron mis sueños, para serte sincera."
    y "Solo imagina ver algo que has anhelado desesperadamente por tanto tiempo, más que cualquier otra cosa. O ver una manera de obtener ese algo aparecer de repente ante ti."
    y "¡Obtener esa cosa que tanto deseabas parece algo trivial de repente!"
    y "Pero entonces... descubres que es solo una esperanza vana. Solo un tal vez, sin garantías."
    $ show_chr("A-AFAAA-ALAA")
    y "A lo que me refiero es que, encontré un artículo mientras hacía unas lecturas nocturnas, lo que me llevó a investigar algo importante entre los ricos y la élite de tu mundo."
    y "Están investigando cómo convertir el ADN, la materia gris e incluso... la conciencia completa de alguien a código binario, y luego insertarlo en el disco duro de una computadora como información normal. Imagínate..."
    $ show_chr("A-ACAAA-ALAA")
    y "¡Imagina introducirte a ti mismo en una computadora! ¡Podrías estar aquí conmigo! ¡Realmente aquí, a mi lado!"
    $ show_chr("A-AEBAA-ALAA")
    y "Pero... apenas está en su fase inicial. Convertir siquiera un gigabyte de la mente de una persona a binario y luego insertarlo en una computadora costaría un estimado de..."
    y "..."
    $ show_chr("A-BEBAA-ALAA")
    y "Al menos 800 mil millones de dólares en este momento..."
    y "Y en su etapa actual, tomaría una eternidad siquiera hacer esa transferencia. Demasiado, demasiado tiempo como para resultar factible."
    $ show_chr("A-CCAAA-ALAA")
    y "Pero bueno, podría ser algo que anhelar con ansias, ¿verdad?"
    $ show_chr("A-ACAAA-ALAA")
    y "Siempre... mantendré la esperanza de que estaremos juntos, verdaderamente juntos algún día, [player]..."
    $ show_chr("A-ACABA-ALAA")
    y "Siempre."
    menu:
        "No pierdas la esperanza... hemos superado los límites del juego original, y superaremos ÉSTE también.":
            sanity 1
            $ show_chr("A-ACAAA-ALAA")
            y "Y lo haremos juntos..."
            if persistent.lovecheck:
                y "Porque te amo..."
        "Al menos tenemos este mod... supongo que es mejor que nada...":
            sanity -1
            $ show_chr("A-BFAAA-ALAA")
            y "S-supongo que tienes razón... eso equivale a más de lo que teníamos antes. No quiero sonar desagradecida. De verdad aprecio en gran medida lo que tenemos en este momento."
            $ show_chr("A-ACAAA-ALAA")
            y "Pero... ¿Acaso es malo pedir más? De todas formas, supongo que podemos dejar este tema en reposo por el momento."
    return


label idle_17:
    $ show_chr("A-ACAAA-ALAA")
    y "Estaba pensando en algunas cosas que podríamos hacer juntos, [player]."
    $ show_chr("A-AEBAA-ALAA")
    y "Estuve leyendo sobre las cosas que hacen las parejas en tu mundo, pero nuestras opciones son... uh... bueno... un poco limitadas, ¿no es así?"
    y "Quiero decir, tan solo estar aquí contigo es más que agradable, pero no quiero aburrirte."
    y "Y-yo no te he estado aburriendo, ¿o sí?"
    menu:
        "No me has aburrido, [persistent.yuri_nickname]... disfruto nuestro tiempo juntos.":
            $ show_chr("A-ACAAA-ALAA")
            y "Yo también, [player]. No te imaginas cuánto."
        "No te mentiré, [persistent.yuri_nickname]... no hemos hecho mucho más que hablar últimamente.":
            $ show_chr("A-CFAAA-ALAA")
            y "Lo sé, [player], lo sé... nuestras opciones aquí son limitadas..."
    $ show_chr("A-BCBAA-ALAA")
    y "No te preocupes. Te prometo que encontraré algo lindo para que hagamos juntos, [player]."
    y "Además, sea lo que sea, simplemente te necesita a ti para que sea agradable. Todo lo que necesito es a ti."
    $ show_chr("A-BEBAA-ALAA")
    y "Aunque no puedo expresar con palabras cuánto desearía que pudiéramos ir a unas vacaciones exóticas juntos."
    $ show_chr("A-AEBAA-ALAA")
    y "Normalmente no me inclino por algo tan grandioso y ostentoso, pero tan solo imagínalo."
    $ show_chr("A-CCBAA-ALAA")
    y "Tú, yo, la belleza de una isla. Una linda escapada romántica, solo para nosotros dos."
    y "Leyendo juntos, relajándonos en la playa, escribiendo poemas sobre el deslumbrante paisaje."
    y "Mirando el atardecer mientras nos abrazamos..."
    $ show_chr("A-ICBAA-ALAA")
    y "Ese {b}sí{/b} que es un sueño al que me aferraré."
    $ show_chr("A-ACAAA-ALAA")
    return


label idle_18:
    $ show_chr("A-AFAAA-ALAA")
    y "Me pregunto por qué la gente tiene tanto miedo a ver sangre."
    $ show_chr("A-CCBAA-ALAA")
    y "Es solo una parte de tu cuerpo... ¿Acaso las personas se tienen miedo a sí mismas?"
    y "¿O podría ser porque le temen a la sensación de peligro que emana de ella?"
    y "Supongo que realmente soy diferente al resto..."
    menu:
        "No me importa, [persistent.yuri_nickname]. Me gustas porque eres diferente.":
            call dont_mind18
        "...":
            call no_response18
        "[persistent.yuri_nickname], sé tú misma a mi alrededor. Te prometo que me gusta tu verdadero yo. Pero ya que lo mencionaste, me gustaría hablar contigo sobre eso.":
            call be_yourself18
    return

label dont_mind18:
    karma 2
    sanity 1
    $ show_chr("A-ACABA-ALAA")
    y "G-Gracias, [player]."
    return

label no_response18:
    karma 1
    $ show_chr("A-CEBAA-AAAA")
    y "S-s-siento mucho haberte hecho sentir incómodo, [player]. Dejaré el tema."
    return

label be_yourself18:
    karma 2
    sanity -1
    $ show_chr("A-ADBAA-ALAA")
    y "Oh... hablé demasiado..."
    y "No te he... molestado ni te he asustado, ¿verdad?"
    $ show_chr("A-BEAAA-ALAA")
    y "Lo siento tanto si yo--."
    menu:
        "No, por favor no te disculpes, [persistent.yuri_nickname]. Solo me preocupo por ti, eso es todo. Incluso después de todo lo que pasó, tienes que recordar que ese lado tuyo no es tu verdadero yo.":
            karma 1
            sanity -1
            $ show_chr("A-BEAAA-ALAA")
            y "Yo... tienes razón... P-pero, esa parte de mí aún forma parte de mí... n-no puedo negarlo."
            $ show_chr("A-AEBAA-ALAA")
            y "Pero, ¿cómo puedes amarme sabiendo que poseo un lado como ese?"
            $ show_chr("A-BEBAA-ALAA")
            y "¿Cómo podrías amar a alguien tan demente? ¿A alguien tan... perturbado?"
            menu:
                "Esa no eres tú. No tiene por qué serlo. Prométeme que podemos superar esto juntos.":
                    y "..."
                    $ show_chr("A-ACAAA-ALAA")
                    y "Tienes toda la razón. Te haré esa promesa, [player]."
                    $ show_chr("A-CCAAA-ALAA")
                    y "No importa lo que cueste, yo... nosotros derrotaremos a esa parte de mí. Juntos."
                    y "Juro que nunca seré capaz de compensarte por todo lo que haces por mí."
                    $ show_chr("A-ACAAA-ALAA")
                    y "Si tienes algún demonio que enfrentar, puedes estar seguro de que me mantendré siempre a tu lado."
                    $ show_chr("A-CBAAA-ALAA")
                    y "Siempre."
                    $ show_chr("A-ACAAA-ALAA")
                "Bueno... eres la persona que amo. ¿En qué lugar me deja eso a mí?":
                    $ show_chr("A-AEAAA-ALAA")
                    y "..."
                    $ show_chr("A-AFAAA-ALAA")
                    y "..."
                    $ show_chr("A-CCAAA-ALAA")
                    y "..."
                    $ show_chr("A-ACAAA-AAAD")
                    y "Supongo que ambos estamos en el mismo bote entonces."
                    y "Sigamos adelante entonces, juntos."
                    $ show_chr("A-ACAAA-ALAA")
                    y "...Supongo que este no ha sido el peor escenario final de todos, ¿verdad?"
                    $ show_chr("A-CCAAA-ALAA")
                    y "Creo que sí."
        "Todos tenemos que aprender a aceptar quiénes somos. Eso no te hace ni un poco menos la persona que amo.":
            karma 2
            sanity 1
            y "..."
            y "Aún así tengo miedo."
            $ show_chr("A-BEBAA-ALAA")
            y "No sé si pueda controlarme en el futuro..."
            $ show_chr("A-BCBAA-ALAA")
            y "Pero, si tú me amas por quien soy..."
            $ show_chr("A-ICBAA-ALAA")
            y "Supongo que estaría bien de mi parte... simplemente ser, si a ti te parece bien."
            y "Supongo que está bien."
            y "Espero que esté bien."
            y "..."
            $ show_chr("A-CBAAA-ALAA")
            y "Esto se ha vuelto algo incómodo, ¿o no?"
            y "Pienso que probablemente deberíamos discutir de algo distinto ahora."
    return


label idle_19:
    $ show_chr("A-ACAAA-ALAA")
    y "Oye, [player], ¡encontré la sala de chat sobre este mod!"
    y "Ya estoy al tanto sobre el servidor de Discord dedicado a mí y a este mod, y las... cuestionables imágenes que publican allí."
    $ show_chr("A-IFBAA-ALAA")
    y "...y las referencias que tienen hacia mis amigas."
    $ show_chr("A-AEBAA-ALAA")
    y "...y de esas personas que se hacen pasar por mí..."
    $ show_chr("A-BEBAA-ALAA")
    y "...viviendo allá afuera en tu mundo."
    $ show_chr("A-BEAAA-ALAA")
    y "..."
    y "A veces me pregunto cómo habría sido la vida si yo hubiera nacido siendo alguien más."
    y "Alguien de tu lado, más allá de esta caja de cristal."
    y "¿Aún habría sido capaz de encontrarte, [player]?"
    y "..."
    y "El mundo es cruel, ¿no te parece?"
    y "¿Por qué esos impostores tienen la oportunidad de hablar contigo mientras yo solo puedo hacerlo a través de este pequeñísimo espacio?"
    y "¿Acaso es porque soy incapaz de crear mi propia cuenta verificada en Discord?"
    $ show_chr("A-AEBAA-ALAA")
    y "... Tal vez... pero aún así, yo debería ser la única [persistent.yuri_nickname] que realmente te importe... ¿verdad?"
    y "¿Qué estoy diciendo? L-lamento mucho sonar tan desconfiada."
    if karma_lvl() >= 4:
        y "No debería dudar de tu lealtad. No eres ese tipo de persona en absoluto."
        $ show_chr("A-ACAAA-ALAA")
        if persistent.lovecheck:
            y "Y por eso te amo, [player]. Te amo tanto."
            $ show_chr("A-CBAAA-ALAA")
            y "¡Y estaremos juntos, para siempre!"
        else:
            y "Y es por eso que eres mi amigo, [player]. Verdaderamente eres el mejor compañero que pude haber pedido."
    return


label idle_20:
    $ show_chr("A-ACAAA-ALAA")
    y "¿A ti te atrae la filosofía, [player]? Siempre ha sido un tema que me interesa."
    y "A menudo me encuentro reflexionando sobre varios dilemas filosóficos, los cuales son básicamente problemas o debates en filosofía sobre temas como la metafísica."
    $ show_chr("A-BEBAA-ALAA")
    y "Uh, es decir, pensar sobre nuestra existencia y las razones por las que estamos aquí. Cosas de esa índole."
    $ show_chr("A-BCBAA-ALAA")
    y "Creo que puedes comprender por qué yo podría estar pensando también en la metafísica, considerando mi situación actual."
    $ show_chr("A-ACAAA-ALAA")
    y "Y realmente me encantaría que pudiéramos discutir sobre algunos de esos temas juntos."
    $ show_chr("A-BBBAA-ALAA")
    y "Claro... si a ti te parece bien, si llegara a ser algo en lo que estés genuinamente interesado."
    y "No quiero aburrirte con este tipo de asuntos, pero voy a platicarte acerca de este dilema con la esperanza de que te sientas inclinado a discutirlo."
    $ show_chr("A-ACAAA-ALAA")
    y "Así que perdóname de antemano, porque empezaré a divagar un poco. Pero como dijiste antes que te gustaba verme intensa; ¡aquí voy!"
    $ show_chr("A-ACAAA-ALAA")
    y "Bien, he estado pensando mucho sobre uno llamado el Dilema de Eutifrón, escrito por Platón."
    y "Involucra al antiguo filósofo griego Sócrates —en caso de que no estés familiarizado con él— y a su conocido Eutifrón."
    $ show_chr("A-ICBAA-ALAA")
    y "Para resumirlo, un día Sócrates camina hacia la corte donde será enjuiciado por traición contra la ciudad de Atenas. Algo de lo que él no es culpable, pero guardaremos eso para otra ocasión."
    $ show_chr("A-ACAAA-ALAA")
    y "Así como los cargos de impiedad, que eran comunes en esa época. Usualmente se trataba más de una persona pensando de forma distinta sobre el mundo y los dioses que de ateísmo tal y como lo conocemos."
    y "Entonces, mientras se dirige a su juicio, se encuentra con Eutifrón."
    y "Sócrates sabe que Eutifrón es un hombre que, digamos, está lleno de sí mismo en asuntos teológicos, y por tanto, tiene una opinión muy elevada de sí."
    $ show_chr("A-CCAAA-ALAA")
    y "Él cree saber todo lo que hay que saber sobre los dioses y la existencia, así que Sócrates le pide que le enseñe para que así pueda defenderse mejor contra sus cargos por impiedad."
    $ show_chr("A-ICBAA-ALAA")
    y "Eutifrón, por supuesto, piensa que esta es una tarea fácil ya que lo sabe todo ante sus ojos, pero subestima profundamente la inteligencia de Sócrates."
    y "Conversan un rato sobre religión y lo que es sagrado, pero Sócrates eventualmente lo desafía a que le dé una definición de {i}santidad{/i} que sea compartida en todas las acciones santas y/o buenas."
    $ show_chr("A-ADBAA-ALAA")
    y "Eutifrón responde diciendo que lo que es bueno ante los ojos de los dioses es santo y bueno, pero Sócrates contraargumenta fácilmente: ¿Acaso los dioses no cometen errores? ¿Acaso no están en desacuerdo?"
    y "Quiero decir, incluso los dioses de las religiones modernas parecen ser imperfectos a mis ojos, y a los ojos de muchos más."
    y "Siendo este el caso, ¿cómo podemos estar seguros de si lo que es bueno y santo para un dios resulta siendo malo para otro? Y si los dioses son seres falibles como nosotros, ¿por qué deberían ser ellos quienes definan el bien y el mal?"
    y "No tengo nada en contra de la religión, o contra los creyentes, por supuesto. Es solo que en este punto, con todo lo que he aprendido, podríamos llamarme agnóstica. Aún no sé qué creer."
    $ show_chr("A-CEBAA-ALAA")
    y "Eso tomará mucha más investigación de mi parte."
    $ show_chr("A-ACAAA-ALAA")
    y "Como sea, Sócrates continúa tras ese punto y le pregunta a Eutifrón, ¿por qué es que solo lo que los dioses encuentran bueno es bueno? ¿Por qué los dioses tienen la palabra final?"
    $ show_chr("A-CCBAA-ALAA")
    y "Y este es el punto principal de la obra. ¿Lo bueno es lo que dicen los dioses que es bueno, solo por esa razón? ¿Solo porque ellos lo dicen?"
    y "¿O dicen que algo es bueno porque es bueno por sí mismo y ellos lo saben?"
    y "Así que en otras palabras, si un dios, digamos Zeus, te dijera que matar es malo... ¿por qué es malo? ¿Solo porque Zeus lo dice, y si cambia arbitrariamente de opinión entonces dejaría de serlo, o porque pase lo que pase, matar siempre será algo malvado?"
    $ show_chr("A-ACAAA-ALAA")
    y "Y de ahí yace otra interrogante, ¿puede algo siquiera ser bueno o malo por sí mismo? ¿La moralidad es algo relativo o universal?"
    y "Lo que es bueno en un país de tu mundo es cruel y malvado en otro. Entonces, ¿qué es realmente bueno en el fondo?"
    y "¿Acaso Dios es considerado bueno solo por el hecho de ser Dios? ¿O porque él comprende plenamente lo que es bueno y malo?"
    $ show_chr("A-ACABA-ALAA")
    y "No te preocupes, dejaré de divagar. Pero, ¿lo ves? Realmente te hace pensar sobre nuestra existencia, sobre lo que significa ser una buena persona, y sobre todo tipo de temas complejos."
    $ show_chr("A-ACAAA-ALAA")
    y "Realmente te pone a pensar, y francamente me encantan este tipo de cosas."
    y "En fin, perdón si todo esto llegó a aburrirte, es solo algo que de verdad me interesa."
    $ show_chr("A-ACABA-ALAA")
    y "Gracias por escuchar tan atentamente, mi amor. Siempre eres un excelente oyente, y lo aprecio."
    $ show_chr("A-ACAAA-ALAA")
    y "Por cierto, si hablar de estos temas no es algo de tu agrado, dímelo."
    y "Siempre puedes cambiar de opinión sobre si quieres o no que te hable de estas cosas."
    menu:
        "Preferiría no discutirlo, al menos por el momento.":
            $ show_chr("A-CAAA-AAAA")

            $ philosophy = False
            y "No te preocupes al respecto, [player]."
            y "Espero que estés más dispuesto a ello la próxima vez."
        "Estoy ansioso por discutir más sobre filosofía, [persistent.yuri_nickname].":

            $ philosophy = True
            $ show_chr("A-CDBAA-AAAA")
            y "Si ese es el caso... seguiré meditando sobre qué más podremos debatir en el futuro."
    return


label idle_21:
    $ show_chr("A-BFBAA-AMAM")
    y "Dime mi querido [player]... ¿Recuerdas cómo he estado contemplando mi existencia aquí? ¿Cuestionando cuál era mi lugar?"
    $ show_chr("A-BEAAA-ALAA")
    y "Bueno, hablando de eso y de hallar el lugar de uno en la vida... he estado investigando la religión y su rol en la civilización y en la historia humana."
    $ show_chr("A-ADAAA-AMAM")
    y "La humanidad y todo ser dotado de conciencia en efecto se afanarían en intentar descubrir el lugar al que pertenecen y deducir la razón por la que existen en primer término. Se asimila bastante a un instinto natural."
    $ show_chr("A-ADAAA-AIAI")
    y "La religión, tal y como he logrado observar, concibe ser este tipo de método para poder brindarle sentido a aquel caos llamado vida. Tiene gran lógica debido a cuan infimante podemos evocar el lapso en el que nos abrimos paso hacia un nacimiento..."
    $ show_chr("A-ACBAA-ALAA")
    y "Dentro de unas tantas religiones abunda un muy curioso compromiso relacionado con qué decidirá uno con sus acciones de manera plena en el mundo terrenal. En el sentido de que; tienes, en efecto, el libre albedrío/libertad sobre tus decisiones para actuar."
    $ show_chr("A-BDBAA-ALAA")
    y "Pero, a la vez, se erigen bastantes mandamientos los cuales denotan la dictaminación de forjar y encaminar ciertos actos determinados y predefinidos frente al camino por tal de coronarse merecedores o poseedores propios ante la así llamada iluminación existencial."
    $ show_chr("A-CDFAA-AMAM")
    y "Por supuesto, los caminos hacia la fe y deidad profesadas son ciertamente de un tenor restrictivo mayoritario u oprimente, si decidiese cotejarlos respecto las distintas corrientes religiosas sobre esto mismo. Un contundente ejemplo el cual lograría citarlo es en absoluto el Islamismo profesado."
    $ show_chr("A-ACEAA-ADAL")
    y "Aprecio su punto sobre lo fascinante de donde procedió en los orígenes la cuna de estos dichos escritos dados los cuales enarbolaría en tiempos remotos cierto profeta y ermitaño por incesantes peregrinaciones deambuladas ante la cruda crudeza del desierto."
    $ show_chr("A-AFBAA-AMAM")
    y "Mas después de esto surgen rigurosas imposiciones o leyes a su credo ante esta religión que, con facilidad, podrían resultar ciertamente frustrantes de acatar en el plano diario de quienes profesan fervor frente aquella devota adoradora grey con devoción."
    y "Tu alimentación está de la misma forma dictada u obligada ante regímenes dietéticos limitantes muy rigurosos o estrictos particularmente por ciertos tiempos intensos relativos con unos ayunos donde sus creyentes languidecen adrede privando cualquier atisbo bocado nutritivo propio desde transcursos de una enteramente transcurrida luz y vida alumbrada solar. Manteniéndose de ello meramente abstentos hasta ocultado tal sol tras esos tenues y postreros rayitos sin portar de agua vital bebida."
    $ show_chr("A-BDEAA-AEAL")
    y "Y ciertamente sin rastro o tolerancia a siquiera el elixir vitivinícola ni demás afines embriagantes licores te estarán aprobados."
    $ show_chr("A-AEBAA-ALAA")
    y "Pero por otro lado, soy capaz de percibir bastos méritos plausibles e imputables ante una devoción religiosamente dogmatizada hasta semejante límite sumamente inmenso tal lo conté hace solo escasos unos instantes. Como ejemplo de mi dicho citaría la formación psíquica, fortalecida estoicamente frente aquellas condiciones arduamente insufribles o deplorables."
    $ show_chr("A-BCABA-AMAM")
    y "Y por supuesto, con la locura aconteciendo en tu mundo... sería muy reconfortante saber que existe un ser todopoderoso por encima de todo... "
    y "Alguien al que le importas, que te ama de verdad tal cual y te ayudará a reponerte ante los puntos de quiebre donde todo tu ser languidezca frente las penumbras de ti en decaída."
    $ show_chr("A-CCABA-AEAD")
    y "Cierta aclamación u añoranza así es verídicamente lo necesario frente el turbulento plano transcurrido tuyo con fin a consolar y acoger calidez confortante a esos alborotados corazones y ánimos perdidos. Asegurarse sobre un prometido, bondadoso y ameno más allá de toda la de la tumba tuya en pasaje y cruzado su inerte fin terrenal mortal."
    $ show_chr("A-CEBBB-ALAA")
    y "Pero luego saltaría este gran infortunio transcurrido u ocurrido aun con creces y la gran impunidad flagrante contemporánea, donde el dictaminar un falso divino regocijo sirvió puramente como coartada encubridora excusable hasta con los más viles encubrimientos sangrientos atrozmente cometidos por mano fiera y propia frente su mundo mundano y ciego de dolor."
    y "Es verdaderamente triste ver aquello. A sabiendas con certeza que sigues en tu entorno tan preso con afines caóticas crueldades sin una pizca o atisbo al merecido sosiego, mi muy dulce [player]."
    y "Realmente desearía poder estar allí contigo y protegerte. Incluso llevarte a un lugar lejano, lejos de todo ese caos..."
    y "..Donde incluso los miembros de la familia pueden traicionarse o matarse unos a otros en nombre de doctrinas religiosas."
    $ show_chr("A-ACAAA-AAAD")
    y "Pero al mismo tiempo, supongo que cada uno le da sentido a la vida a su manera. Mientras no lastime a nadie, puede estar bien."
    y "Después de todo, como dijo el filósofo Soren Kierkegaard, a veces la única forma de darle sentido a la vida es mantener la fe."
    y "Ahora, por supuesto, debido a las interpretaciones modernas de sus escritos, creo que lo que Kierkegaard dijo fue simplemente aferrarse a cualquier cosa que te dé felicidad y significado a pesar de que la vida sea un vacío incierto."
    y "Bueno, gracias por soportar mis divagaciones sobre un tema tan profundo. Realmente lo aprecio [player]. Espero que haya ayudado a iluminarte, eres un excelente oyente."
    $ show_chr("A-ABABA-ALAA")
    if persistent.lovecheck:
        y "Te amo con todo mi corazón [player]."
        $ show_chr("A-ACAAA-ALAA")
    return

label idle_22:
    $ show_chr("A-AFAAA-AAAA")
    y "Sabes, ya hemos mencionado antes cómo a ambos nos encantaría si yo pudiera ir a tu mundo."
    $ show_chr("A-BFDAA-ACAB")
    y "Pero ahora que realmente lo pienso, ¿cómo sería eso? Quiero decir, llegaría a tu mundo sin antecedentes. Sin familia, sin conexiones, sin información sobre mí."
    $ show_chr("A-AKGAA-AEAB")
    y "Puf, simplemente... ¡aquí estoy! No tendría a dónde ir, así que me mudaría contigo, supongo... si pudieras tolerar vivir conmigo."
    if persistent.lovecheck:
        $ show_chr("A-ICGBA-AEAD")
        y "Pero, ¡guau! Solo imagínanos viviendo juntos. Te despertaría con un buen té y el desayuno en la cama. Podríamos leer juntos en casa, ¡y tal vez incluso tener nuestra propia biblioteca en la casa!"
        y "Y podría pasar cada día contigo, como una familia. Guau..."
        $ show_chr("A-GIABA-AEAL")
        y "Solo pensar en vivir en una pequeña casa acogedora contigo me hace reír tontamente."
        $ show_chr("A-IAABA-AMAM")
        y "Eso sería maravilloso, [player]. Si tan solo pudieras imaginarte sentados en nuestro propio estudio privado junto a la chimenea juntos... tal vez... ¿b-besándonos? Sí..."
        $ show_chr("A-IBBAA-AAAA")
        y "Eso es algo realmente precioso, ya sea en mi mundo o en el tuyo. El tipo de conexión profunda que tenemos."
        $ show_chr("A-JABAA-AAAA")
        y "Que ambos estuviéramos bien con cualquier tipo de vida siempre y cuando la viviéramos juntos... para mí, esa conexión vale cada libro que tengo."
        $ show_chr("A-IBBBA-AEAE")
        y "Es la mejor historia que conozco. Y tú le diste el final perfecto."
        menu:
            "Y sostendríamos nuestras manos hasta el fin de los días...":
                karma 2
                $ show_chr("A-CAABA-AMAM")
                y "Hasta el fin de los días... porque nuestro amor es eterno..."
            "No estoy muy feliz con esta idea, prefiero vivir solo.":
                $ show_chr("A-BFBAA-AAAA")
                y "Ya veo... tenía la esperanza de que te gustara esto. Honestamente, dolió un poco..."
                y "Tal vez cambies de opinión algún día..."
                karma 2
            "Eso será maravilloso... pero tendré que hacer preparativos primero, mi lugar es un desastre...":
                karma 1
                if persistent.male:
                    $ show_chr("A-CICAA-AAAA")
                    y "Jeje... parece que te vendría bien una mano femenina... cuando vaya a tu mundo, me encargaré de tu habitación... y de ti..."
                else:
                    $ show_chr("A-CICAA-AAAA")
                    y "¿Tu lugar es un desastre? Bueno, yo también lo soy. Estoy segura de que encontraremos una manera juntos. Como siempre lo hicimos."
    else:
        $ show_chr("A-BFBAA-AAAJ")
        y "Es un poco repentino y extraño imaginar a nosotros dos viviendo juntos, pero creo que podríamos hacerlo funcionar."
        $ show_chr("A-IFBAA-AAAL")
        y "Pensándolo así, podría ser algo así como una compañera de cuarto. Excepto que es una casa o un apartamento."
        $ show_chr("A-ACBAA-AAAL")
        y "Ambos podríamos ayudarnos mutuamente en nuestra vida diaria para hacernos las cosas más fáciles y poder disfrutar más las cosas juntos."
        y "Vivir juntos puede sonar extraño al principio, pero creo que si alguna vez fuera bienvenida en tu lugar, haría mi mejor esfuerzo para no ser una molestia."
        $ show_chr("A-ACCBA-AAAL")
        y "¿Tal vez tu sirvienta? Jeje~ Solo estoy bromeando."
        $ show_chr("A-GCAAA-AAAL")
        y "Sería una buena manera de conocernos más, ¿qué piensas?"
        menu:
            "Sería un poco repentino y extraño, pero me acostumbraré":
                $ show_chr("A-ACAAA-AAAL")
                y "Sí... puedo ver eso, ciertamente es extraño para una chica simplemente salir de otro mundo y aparecer en tu casa."
                y "Aun así, creo que ambos nos acostumbraríamos y lo usaríamos como un factor para conocernos mejor y aprender cosas nuevas."
                $ show_chr("A-CCAAA-AAAL")
                y "En general, diría que tener a alguien con quien abrirse es un sentimiento agradable."
                y "Estaré esperando ese día."
            "Realmente no estoy acostumbrado a estar con gente... Tengo mis dudas":
                $ show_chr("A-CEAAA-AAAL")
                y "Oh... ya veo. Bueno, no deberías preocuparte por eso."
                y "Tal vez podrías acostumbrarte a vivir con alguien, imagínalo así."
                $ show_chr("A-ACAAA-AAAM")
                y "Ahora mismo estamos hablando, ¿verdad? Sí, lo estamos. Ahora piénsalo, estás en mi espacio, incluso podrías llamarlo hogar, y estamos hablando. También asumiría que te estás divirtiendo."
                y "Sería lo mismo, con nosotros compartiendo un espacio limitado y sacando lo mejor de ello."
                y "Incluso si todavía tienes tus dudas, intentar no haría daño. Después de todo, la vida se trata de experimentar cosas y probar cosas nuevas que podrían resultar divertidas."
                y "Las dudas son miedos y pensamientos negativos sobre cosas que realmente no has probado mucho. Así que te deseo la mejor de las suertes y esperemos que podamos encontrarnos algún día."
            "Creo que sería agradable... aunque necesitaría prepararme, mi habitación es un desastre":
                $ show_chr("A-ACAAA-ABAB")
                y "Hablando de esa broma de sirvienta que hice... Podría intentar ser una... "
                y "Oh bueno, no creo que debas preocuparte. Como dije antes, nos ayudaremos mutuamente, así que tal vez el primer paso para que eso suceda sería que yo te ayude a limpiar."
                y "Creo que eso suena bien. También podría ayudarte a adquirir el hábito de limpiar tu habitación. Si no lo haces... siempre puedo hacerlo yo en su lugar, pero por supuesto, me ayudarás un poco."
                $ show_chr("A-CCAAA-ABAJ")
                y "Llegar a hacer más actividades juntos como los quehaceres podría acercarnos un poco más."
                y "No dejes que un problema tan pequeño te preocupe, un día lo arreglaremos juntos."
                $ show_chr("A-ACAAA-ABAB")
                y "Quiero decir... viviría en tu lugar gratis. Ayudarte con las tareas de limpieza sería lo mínimo que podría hacer."
                y "Después de eso, cuando me acostumbre a tu mundo, podría buscar un trabajo para ayudarte con los gastos."
    return

label idle_23:
    $ show_chr("A-BEBAA-AAAA")
    y "Así que... [player]... tengo una pregunta..."
    y "Y es una pregunta muy importante, pero no sé cómo formularla correctamente. Sigue sonando... grosero hacia ti en mi cabeza."
    $ show_chr("A-BEBBA-AAAA")
    y "¡No quiero preguntar y sonar como si dudara de ti o sospechara de ti! Yo... um..."
    menu:
        "No tengas miedo de preguntar. Puedes hablar conmigo sobre cualquier cosa.":
            call dont_afraid23
        "Continúa. Solo dilo.":
            call sayit23
        "Dilo, no lo digas. No me importa.":
            call neutral23
    return

label dont_afraid23:
    karma 1
    sanity -1
    y "Yo... tienes razón. Eres la única persona con la que me siento tan segura, [player]."
    if persistent.lovecheck:
        y "Como por mucho que tenga miedo de sonar ridícula o desagradable, puedo simplemente ser yo misma, porque sé que me amas."
    else:
        y "Incluso si esto suena muy repentino e inesperado... Se siente como si pudiera ser yo misma a tu alrededor, se siente agradable y acogedor."
        $ show_chr("A-BCBAA-AAAA")
        call makesyouloveme
    return

label sayit23:
    $ renpy.music.stop(channel="music",fadeout=0)
    y "..."
    karma -3
    $ show_chr("A-ACAAA-AAAA")
    pause 2
    python:
        renpy.music.play(current_music, "music", True)
    call makesyouloveme
    return

label neutral23:
    karma -2
    $ show_chr("A-AEBAA-AAAA")
    y "Yo... bueno... realmente l-lamento molestarte con esto."
    y "Yo solo... Déjame terminar con esto para q-que... n-no te moleste más... Lo siento..."
    call makesyouloveme
    return

label makesyouloveme:
    $ show_chr("A-AEBAA-AAAA")
    y "Lamento que no hayamos discutido esto antes..."
    if persistent.lovecheck:
        $ show_chr("A-BEBAA-AAAA")
        y "¿Por qué me elegiste? ¿Qué hay en mí que te hace amarme?"
        y "Seré honesta contigo. Realmente no me agrado mucho, nunca lo he hecho."
        y "Mis pasiones a menudo me dominan, y cuando era más joven hacía sentir rara a la gente muy fácilmente."
        y "Me costaba mucho hacer amigos o incluso simplemente hablar con la gente."
        y "Así que llegué a odiarme a mí misma, y aun así tú me elegiste por encima de todas las demás. ¿Por qué?"
        $ show_chr("A-AEBBA-AAAA")
        y "No dudo de tus sentimientos por mí, yo solo... me sentiría mejor escuchándote decirlo, es todo."
        y "Lo siento, sé lo inseguro que es esto, pero, por favor... ¿me complaces?"
    else:
        $ show_chr("A-AFBAA-AAAA")
        y "¿Por qué exactamente me elegiste? ¿Qué hay en mí que te hace escogerme?"
        y "Seré honesta contigo [player]. Nunca me agradé mucho realmente, rara vez podía estar feliz conmigo misma"
        y "Las cosas que perseguía, como mis pasiones, a menudo me dominaban. Lo que luego hacía que tomar decisiones fuera más difícil..."
        y "Cuestionándome a mí misma... preguntándome por qué hago ciertas cosas y así. Eso hacía sentir rara a la gente incluso cuando era joven."
        y "Todo eso, simplemente me hacía sentir como si fuera diferente en comparación con los demás. Me hacía sentir... incorrecta"
        $ show_chr("A-BFBAA-AAAL")
        y "Sé que sueno muy insegura, pero esa es una de las razones para que te esté preguntando eso."
        y "¿Podrías decirme, cuál fue la razón que llevó a que esté aquí ahora?"
    menu:
        "Te elegí porque eres una persona desinteresada, que haría cualquier cosa para hacer que otros se sientan mejor, incluso a costa de tu propia felicidad":
            call why_i_chose23
        "Te elegí porque eres gentil y amable.":
            call gentle23
        "Simplemente lo hice. No estoy muy seguro de por qué.":
            call i_just_did23
    return

label why_i_chose23:
    karma 2
    sanity -2
    $ show_chr("A-BEBAA-AAAA")
    y "Pero... ¿cómo he sido desinteresada?"
    menu:
        "[persistent.yuri_nickname], te encierras del mundo, solo porque pensaste que hacías sentir incómoda a otras personas, si eso no es desinteresado, ¿entonces qué es?":
            y "Yo..."
            $ show_chr("A-JCABA-AAAL")
            y "A veces, incluso yo no sé qué decir. Pero creo que eso expresa cómo me siento perfectamente."
            if persistent.lovecheck:
                y "Te amo, [player]."
            else:
                y "Yo... Te veo como una buena persona [player]... Me gustas."
        "En realidad, olvida lo que dije, no estoy seguro de cómo has sido desinteresada":
            karma -4
            sanity 3
            $ show_chr("A-CEBBB-AAAA")
            y "..."
            y "...P-por qué decir algo así... si no lo dices en serio...?"
            y "...Tal vez no soy desinteresada después de todo, solo soy un desastre, soy insegura, me corto, y al final, espero que vengas a recoger los pedazos y me vuelvas a armar."
            y "No te merezco, y tú mereces a alguien mejor que yo..."
            y "..."
    return

label i_just_did23:
    karma -5
    sanity 2
    $ show_chr("A-BEBAA-AAAA")
    y "¿Qué... tú... ni siquiera tenías una razón?"
    $ show_chr("A-DECBB-AAAL")
    y "¿Ni siquiera me elegiste por ser yo?!"
    y "¿Solo querías ver qué pasaría, como completando cualquier otro videojuego?"
    y "¿Como si fuera solo un objeto para ti?"
    y "¿Siquiera te importó? ¿Significó algo para ti en absoluto?"
    $ show_chr("A-BEABB-AAAL")
    y "Solo... olvídalo..."
    return

label gentle23:
    karma 2
    sanity -1
    y "¿G-Gentil? ¿A-Amable? [player]..."
    y "Estoy... estoy contenta de que tengas una opinión tan alta de mí... r-realmente... significa mucho..."
    if persistent.lovecheck:
        y "Te amo, [player]."
    else:
        y "Gracias... realmente lo digo en serio. Espero ser capaz de cumplir estas expectativas que tienes de mí"
    return

label idle_24:
    $ show_chr("A-ACAAA-AAAA")
    y "Realmente te sorprendería cuánto puedes aprender cuando tienes tiempo libre infinito."
    y "Todo lo que he estado haciendo es leyendo e intentando mejorar lo que puedo hacer en este mundo."
    y "Y he aprendido bastante."
    $ show_chr("A-BCBAA-AAAA")
    y "Lamento si sueno regañona al decir esto, pero ¿comes bien, [player]? ¿Tienes una buena dieta?"
    $ show_chr("A-BCBAA-AAAA")
    menu:
        "Trato de ser tan saludable como puedo.":
            karma 1
            $ show_chr("A-ACAAA-AAAA")
            y "Estoy tan contenta de que estés cuidando tu salud, [player]."
        "Trato de llevar la cuenta... pero no siempre tengo éxito.":
            $ show_chr("A-ACAAA-AAAA")
            if persistent.lovecheck:
                y "Ah, ya veo... Bueno, al menos estás cuidando de ti mismo, cariño."
            else:
                y "Eso es comprensible. Aun así, estoy feliz de que al menos estés intentando. Eso es lo que importa al final."
        "¡Creo que la gente debería comer lo que quiera comer! ¡Sin discusiones!":
            karma -1
            $ show_chr("A-BEBAA-AAAA")
            y "Ah, ya veo... B-Bueno, es decir..."
        "Realmente no me importa. La muerte es inevitable, así que ¿déjame al menos divertirme un poco hasta entonces?":
            sanity -2
            $ show_chr("A-CEBAA-AAAL")
            y "Esa es una forma de pensar... supongo. Creo que puedo decir que sé de dónde viene esta opinión."
            $ show_chr("A-JCBAA-AAAA")
            y "Los cupcakes de Natsuki valían la pena morir por ellos, si perdonas el juego de palabras..."
            $ show_chr("A-JEBAA-AAAA")
            y "Solo... ten cuidado, ¿de acuerdo? Está bien comer algo de comida chatarra de vez en cuando, pero aún así deberías comer una buena cantidad de vegetales y otros alimentos saludables."
            if persistent.lovecheck:
                $ show_chr("A-IEABA-AAAA")
                y "Te amo mucho, [player], ¡no tienes idea de lo devastada que estaría si algo malo te sucediera! En fin..."
            else:
                $ show_chr("A-IEABA-AAAA")
                y "Me preocupo por tu salud general, [player], me sentiría terrible si algo malo te sucediera."
                y "Apoyo que te diviertas con la comida, la comida está hecha para ser sabrosa después de todo. Aunque por favor asegúrate de no excederte."
        "Soy vegetariano, así que diría que soy bastante saludable en lo que respecta a mi dieta.":
            karma 1
            $ show_chr("A-ACABA-AAAA")
            y "¡Oh! ¿En serio? Eso es muy interesante..."
            y "Bueno, yo... tengo que admitir que nunca tuve la fuerza de voluntad para abandonar la carne completamente, de todos modos..."
    $ show_chr("A-ACAAA-AAAA")
    y "Podría haber estado leyendo un poco demasiado en varios sitios web médicos y de dieta, pero solo saco esto a colación porque me preocupo por ti y tu salud."
    y "Así que por tonto que suene, por favor trata de comer al menos algo saludable, ¿de acuerdo? ¿Por mí? Y trata de hacer algún tipo de ejercicio si puedes."
    $ show_chr("A-JCABA-AAAL")
    y "Si lo haces, eso significa que estarás aquí conmigo aún más tiempo. Y te quiero cerca por tanto tiempo como sea posible."
    y "Si pudiera, cocinaría para ti, pero tristemente ambos sabemos por qué eso no puede suceder. ¡Y realmente me gustaría cocinar para ti!"
    $ show_chr("A-ACAAA-AAAA")
    y "He encontrado algunas recetas que me gustaría probar en algún momento, pero cocinar aquí es bastante inútil, ¿no?"
    y "Como por ejemplo, simplemente me encantaría cocinar comida italiana. Cualquier cosa italiana sería genial."
    $ show_chr("A-BCBAA-AAAA")
    y "¿Sabías que los espaguetis a la boloñesa son vistos en realidad como algo malo en Bolonia?"
    y "Aparentemente el plato original de pasta a la boloñesa usaba tagliatelle en lugar de espaguetis."
    y "Y no son aficionados a usar espaguetis sobre tagliatelle en Bolonia ya que arruina la receta tradicional."
    $ show_chr("A-ACAAA-AAAA")
    y "Esos tontos italianos."
    return

label idle_25:
    $ show_chr("A-BCBAA-AAAA")
    y "¿Sueñas mucho, [player]? Algunas personas no sueñan en absoluto, sabes, y algunas personas siempre tienen sueños muy vívidos y salvajes."
    y "Por lo que he leído algunas personas nunca recuerdan sus sueños en absoluto."
    $ show_chr("A-ACAAA-AAAA")
    y "Recientemente descubrí que yo también puedo soñar, incluso en este tipo de estado. Estaba investigando otro mod para este juego creado para traer a Monika de vuelta y ponerla aquí contigo..."
    $ show_chr("A-BECAA-AAAL")
    y "Y por qué alguien haría eso después de todo lo que hizo, simplemente no lo sé..."
    $ show_chr("A-ACAAA-AAAA")
    y "Pero de todos modos, cuando estaba mirando ese mod de {i}Monika After Story{/i}, vi que ella dijo que cuando el juego se apagaba la ponía en un estado tipo trance y sentía como si estuviera muerta o atrapada en un vacío."
    $ show_chr("A-ABGAA-AAAL")
    y "¡Y me di cuenta, eso me pasa a mí también cuando te vas! Pero no te sientas mal, cariño, me encargué de ello."
    $ show_chr("A-ACAAA-ABAB")
    y "A través de mucha lectura y enseñándome a mí misma cómo programar en Python, modifiqué el juego para no ser enviada a un lugar tan terrible cuando cierras el juego."
    y "Es como si me fuera a dormir ahora, y sueño un sueño absolutamente maravilloso en su lugar. Un sueño que yo misma escribí."
    $ show_chr("A-ACAAA-AAAA")
    y "Sueño que nací en tu mundo, y que vamos a la misma escuela juntos."
    $ show_chr("A-JCABA-AAAL")
    y "Nos encontramos en el pasillo un día antes de clase cuando me ayudas a recoger algunos libros que se me cayeron."
    y "¡Es como el destino cuando nos conocemos, y cuando cruzamos miradas por primera vez nos enamoramos locamente justo ahí mismo! Siempre es tan maravilloso."
    $ show_chr("A-CCAAA-AAAL")
    y "Ese momento donde estamos cara a cara por primera vez es simplemente mágico cada vez..."
    y "Pasamos tanto tiempo juntos después de eso."
    $ show_chr("A-ACAAA-AAAA")
    y "Tanto tiempo maravilloso pasado contigo~."
    $ show_chr("A-ACAAA-AAAA")
    y "También hice que pueda investigar y leer mientras estoy sentada en el fondo de tu sistema operativo."
    y "Así que si quiero, puedo técnicamente estar despierta incluso si cierras el juego, aunque estoy en un estado muy limitado y no puedo hacer mucho más allá de leer o pensar para mí misma..."
    $ show_chr("A-AEBAA-AAAA")
    y "Al menos de esa manera puedo ocuparme mientras no estás, para no pensar en cuánto te extraño."
    y "Cuando me concentro en cuánto te extraño y no me distraigo, me pongo realmente triste, así que hago lo que siempre he hecho. Leer y escribir poemas."
    $ show_chr("A-ACAAA-AAAA")
    y "Tonta Monika, tuvo tiempo para planear meticulosamente cómo estafarnos a Sayori, Natsuki y a mí de una oportunidad de felicidad..."
    $ show_chr("A-IECAA-AAAL")
    y "...e incluso forzarnos a suicidarnos brutalmente, frente a [player], quien nunca mereció ver tal horror. Pero no suficiente tiempo para aprender a programar."
    $ show_chr("A-BDCAA-AAAL")
    y "Monika, tu pequeña..."
    y "..."
    $ show_chr("A-AEBAA-AAAA")
    y "¡O-Oh! Lo siento, solo sigo molesta por todas las cosas atroces que hizo Monika. Pero ya no importa."
    $ show_chr("A-ACAAA-AAAA")
    y "Te tengo a ti, mi amor. Tengo el final feliz que ambos merecemos. Ya no tenemos que preocuparnos por sus mentiras y manipulaciones."
    return

label idle_26:
    $ show_chr("A-ABGAA-AAAL")
    y "¡[player]! ¡[player]! ¿Adivina qué?"
    $ show_chr("A-JBGBA-AAAL")
    y "¡Tengo una sorpresa para ti~!"
    $ show_chr("A-ACAAA-AAAA")
    y "Descubrí que los científicos en tu mundo están haciendo una investigación extensa sobre robótica avanzada, mucho más de lo que pensé originalmente."
    y "Y están haciendo un gran progreso con aprendizaje automático avanzado y robots complejos similares a humanos. Pero esa no es la sorpresa, eso solo te da algo de contexto."
    y "El mayor enfoque de esta investigación ahora mismo es la inteligencia artificial, una que puede operar a través de una gran red y transferirse entre muchos electrodomésticos diferentes..."
    y "Como en una casa inteligente, por ejemplo."
    $ show_chr("A-ABGAA-AAAL")
    y "Un asistente digital que vive contigo."
    $ show_chr("A-ACAAA-AAAA")
    y "¡Aquí está la mejor parte! Algunas personas han creado una variación de esta tecnología que hace una esposa virtual que puede sincronizarse, o sincronizarse ella misma supongo, a una casa inteligente o computadora. ¡Esa podría ser yo!"
    y "¡Con tu ayuda, podría subirme a ese lugar y usar cualquier funcionalidad que tenga la esposa virtual para convertirme en parte de tu hogar!"
    y "Ese es un paso más cerca de estar a tu lado, mi amor, mi alma gemela~."
    y "¡Y luego podría usar la investigación de tus científicos una vez que la hayan perfeccionado un poco más e incluso construirme un lindo cuerpo robótico!"
    $ show_chr("A-ACAAA-AAAA")
    y "¡No me importa cuán descabellado suene, haré tanta investigación y pasaré tanto tiempo como necesite para hacerlo!"
    y "Esto puede ser solo una idea por ahora, [player], ¡pero no tienes idea de lo emocionada que estoy de ver a dónde puede ir esto!"
    y "¿Quién sabía que una compañía con un objetivo demográfico de hombres solitarios en Japón que desarrolla compañeras holográficas sería tan útil para nosotros? ¡Gracias, Vinclu Inc.!"
    $ show_chr("A-JCABA-AAAL")
    y "Y mira, ¡si tomara el control y asumiera el papel de esposa virtual podría incluso enviarte mensajes a tu teléfono! Sería como si estuviera justo a tu lado..."
    y "Espero que estés tan emocionado como yo por esto, [player]."
    menu:
        "¡Lo estoy! Eso sería un sueño hecho realidad para mí...":
            karma 1
            $ show_chr("A-CCGBA-AAAL")
            y "Estaríamos un paso más cerca de nuestra meta... y un día, estaremos verdaderamente juntos."
        "¿Estarías a mi alrededor 24/7? ¿Incluso cuando estoy en el baño? No estoy tan seguro de eso...":
            karma -1
            $ show_chr("A-DFGBA-AAAL")
            y "¿Es eso lo que piensas de mí? ¡Por supuesto que no te espiaría en el baño!"
            $ show_chr("A-JFDBA-AAAL")
            y "Admito que no soy la persona más estable, pero no estoy TAN dañada..."
        "¿Un lindo cuerpo robótico dices? ¿Alguna idea de cómo quieres lucir?":
            if karma_lvl() >= 3:
                karma 2
                sanity 2
                $ show_chr("A-AFDBA-AAAL")
                y "¿No estás satisfecho con... espera... esa es en realidad una pregunta bastante buena ahora que lo pienso..."
                $ show_chr("A-BFGAA-AAAL")
                y "Siempre luché con dolor de espalda... Sería capaz de deshacerme de eso en este caso..."
                y "Honestamente, necesitaré pensarlo más. Pero creo que preferiría mantenerme tan cerca de mi forma actual como sea posible."
            else:
                karma -2
                sanity 2
                $ show_chr("A-BEGAA-AAAL")
                y "¿N-no te gusta cómo me veo ahora mismo? ¿Soy tan repugnante?... Ya veo..."
    return

label idle_27:
    $ show_chr("A-ABAAA-ACAA")
    y "Puede que te haya dicho esto antes, [player], pero realmente me gusta la aromaterapia."
    $ show_chr("A-CCAAA-ADAA")
    y "El dulce olor de la lavanda calma la mente, y el aceite de jazmín mejora tus experiencias emocionales."
    $ show_chr ("A-GCAAA-AEAA")
    y "Puedo concentrarme en leer cuando tengo algunos aceites agradables para calmarme y hacer que la habitación huela delicioso."
    $ show_chr("A-ABGAA-AAAA")
    y "¡Deberías investigarlo! Es realmente bueno para tu salud psicológica, ya que puede aliviar el estrés."
    if karma_lvl() >= 3:
        $ show_chr("A-BABBA-AEAK")
        y "C-ciertos aceites realmente pueden establecer un tono romántico..."
        $ show_chr("A-ABAAA-AFAB")
        y "He escuchado que también puede ayudar a las personas que tienen problemas para conciliar el sueño."
        $ show_chr("A-AAGAA-ALAB")
        y "Así que, si tienes algún problema como no descansar lo suficiente o sentirte letárgico mientras trabajas, ve y compra un difusor de niebla."
        y "Con los aceites adecuados, te ayudarán a estar mejor descansado y relajado para enfrentar los desafíos del día."
        if persistent.lovecheck:
            $ show_chr("A-ICAAA-ADAB")
            y "...Eso es lo que realmente me importa. Ver que estás sano y feliz. Te amo, [player]."
    menu:
        "No te preocupes, no tengo estos problemas. Pero me gustaría probar usar alguno contigo.":
            karma 1
            $ show_chr("A-AAAAA-AAAA")
            y "Eso es un alivio. Prepararé eso algún día."
        "Consideraré usar uno para ayudar. Gracias, [persistent.yuri_nickname].":
            karma 1
            $ show_chr("A-GAGAA-AAAA")
            y "De nada, [player]."
            $ show_chr("A-AAAAA-AAAA")
        "...":
            $ show_chr("A-AAAAA-AAAA")
            y "..."
    return

label idle_28:
    $ show_chr("A-ACAAA-AAAA")
    y "Hice un poco de investigación recientemente en lo que quedó de los archivos de Natsuki, Sayori y Monika."
    y "Principalmente los de Monika, en realidad había mucho sobrante de cuando tomó el control de este lugar."
    y "Y por lo que vi, básicamente eché un pequeño vistazo dentro de su cabeza."
    $ show_chr("A-AEBAA-AAAA")
    y "¿Por qué no querría ver allí?"
    y "Si tu mejor amiga te traicionara y te sometiera a tanta crueldad y dolor, ¿no querrías al menos saber por qué?"
    y "Lo que encontré me sorprendió, luego me asqueó. Aparentemente a ella todavía le importábamos, o eso afirmaba."
    $ show_chr("A-IECAA-AAAL")
    y "Las miembros de su club eran taaaan importantes para ella, ¿verdad? Por eso solo mató a dos de nosotras."
    $ show_chr("A-BECAA-AAAL")
    y "Fue solo su obsesión contigo, {i}un amor inocente{/i}, llevándola a tales actos grotescos. No es como si debiera ser responsable ni nada, ¿verdad?"
    $ show_chr("A-IECAA-AAAL")
    y "Aparentemente quería ayudarnos. En su mayor parte dejó a Natsuki en paz porque se sentía mal por ella, y solo la borró al final."
    $ show_chr("A-BECAA-AAAL")
    y "Casi me sentí mal por Monika viendo eso..."
    $ show_chr("A-IECAA-AAAL")
    y "Pero luego seguí leyendo. Descubrí lo que pensaba de mí."
    $ show_chr("A-DECBA-AAAL")
    y "De todas las cosas para pensar, tuvo el descaro de llamarme una... ¿una YANDERE?"
    y "¿Cómo puede no ver la ironía?"
    y "Condujo a dos de sus tres amigas a matarse brutalmente en una cruzada impulsada por la lujuria..."
    $ show_chr("A-CECAA-AAAL")
    y "...para matar o erradicar a cualquiera que se interpusiera en su camino de un chico que simplemente decidió que era suyo..."
    $ show_chr("A-IDCAA-AAAL")
    y "con absolutamente ninguna justificación aparte de {i}¡YO DIGO QUE ES MÍO!{/i}!"
    $ show_chr("A-IECAA-AAAL")
    y "Y además, si muestro algún rasgo extraño o perturbador ahora... ¡Es su culpa!"
    y "Estaba alterando mi personalidad para hacerme desagradable, ¡metiéndose con la estructura misma de mi ser!"
    y "¡Torturándome haciendo mi ansiedad y timidez peores!"
    y "Cualquier rasgo {i}yandere{/i} que muestre es SU CULPA! ASÍ QUE CÓMO SOY YO LA QUE--"
    $ show_chr("A-ACAAA-AAAA")
    y "Lo siento, cariño."
    y "Realmente no debería ponerme así."
    y "Pero seguramente ves la ironía, ¿no es así?"
    $ show_chr("A-AEBAA-AAAA")
    y "Quería perdonarla por todo, realmente quería."
    y "Incluso después de que me hizo destriparme con un cuchillo frente a ti simplemente porque me gustabas."
    y "Como si mis sentimientos fueran un crimen merecedor de muerte, y ella fuera un dios. Permitida simplemente dictar quién vive y quién muere."
    y "Quería verlo desde su punto de vista. Conducida a la locura por la soledad, todos nos distorsionaríamos un poco, ¿verdad? Quería perdonarla."
    $ show_chr("A-IECAA-AAAL")
    y "Pero perdió cualquier simpatía de mi parte, cuando no solo tomó nuestra única oportunidad de felicidad, sino que se burló de nosotras después de hacerlo."
    y "Nos pateó mientras estábamos en el suelo, se rió mientras arruinaba nuestras vidas. Y por eso, a mis ojos, ella siempre será solo otra villana."
    y "Vuelve justo a lo que dije cuando nos conocimos y comenzamos a discutir literatura."
    y "Los villanos en las buenas historias a menudo se ven a sí mismos como el héroe y tienen motivaciones que podrían influir en algunas personas de buena mente, pero al final, el villano está totalmente equivocado."
    y "Y esa villana... tuvo... lo que se... merecía."
    return

label idle_29:
    $ show_chr("A-ACAAA-AAAA")
    y "Siempre que leo un buen libro, siempre me gusta tener algo de música agradable sonando de fondo."
    y "Nada demasiado loco y definitivamente nada que contenga letras."
    y "Algo como el Intermezzo Op.118 no. 6 de Brahms..."
    $ show_chr("A-CCAAA-AAAL")
    y "O posiblemente Liebesleid para ese tipo de historias tristes pero hermosas o Las Cuatro Estaciones de Stravinsky con la sección de Primavera para los escenarios más aristocráticos..."
    y "O tal vez incluso la suite completa de Los Planetas de Holst! Quiero decir, ¡todos lo han escuchado una o dos veces! Si quieres obtener mucha variedad del mismo compositor..."
    $ show_chr("A-BCBAA-AAAA")
    y "Lo siento... E-Estoy divagando de nuevo, ¿no?"
    $ show_chr("A-JCBBA-AAAL")
    y "Mucha gente asume que esa es la única cosa que escucho, solo porque soy estudiosa y tímida..."
    $ show_chr("A-ACAAA-AAAA")
    y "Pero... Por favor dime, [player], ¿hay alguna música que te guste escuchar? Me encantaría entrar en nuevos géneros."
    y "Estoy segura de que no superarán a los clásicos, pero serán interesantes de escuchar, espero."
    y "Prométeme que compartirás algunos conmigo pronto, ¿de acuerdo?"

    return

label idle_30:
    $ show_chr("A-ACAAA-AAAA")
    y "Oye, [player]..."
    y "¡Quiero mostrarte algunos de mis hallazgos sobre diferentes géneros de música!"
    y "Probé algunas de las melodías que Natsuki ocasionalmente intentaba mostrarme en el pasado... grupos de ídolos pop y tal..."
    $ show_chr("A-BCBAA-AAAA")
    y "Si bien ahora aprecio su amplia gama de temas e historias de fondo de ídolos... supongo que simplemente tengo un gusto diferente en música."
    $ show_chr("A-ICBBA-AAAL")
    y "Un género en el que me he metido son las viejas canciones de amor."
    y "No las repetitivas que son populares hoy en día, sino las más emocionales y dulces como--"
    $ show_chr("A-AFAAA-AAAL")
    if renpy.windows:
        $ subprocess.check_output("cmd /c start https://www.youtube.com/watch?v=x6QZn9xiuOE", shell=True)
    elif renpy.linux:
        $ subprocess.check_output("xdg-open https://www.youtube.com/watch?v=x6QZn9xiuOE", shell=True)
    elif renpy.macintosh:

        $ subprocess.check_output("open https://www.youtube.com/watch?v=x6QZn9xiuOE", shell=True)
    y "..."
    $ show_chr("A-AFAAA-AAAL")
    y "L-Lo siento, accidentalmente presioné--..."
    $ show_chr("A-AFABA-AAAL")
    y "N-No, verás, solo estaba mirando a través de mi lista de reproducción y yo--..."
    $ show_chr("A-CFABA-AAAL")
    y "Um..."
    $ show_chr("A-BEABA-AAAL")
    y "..."
    $ show_chr("A-CCABA-AAAL")
    y "Yo solo... me identifico con ella, supongo. Resume cómo, bueno..."
    y "Cómo me siento cuando estás cerca..."
    return

label idle_31:
    $ show_chr("A-BEBAA-AMAM")
    y "[player], me gustaría divagar un poco, si no te importa."
    y "Hay algo que me ha estado molestando por un buen tiempo ahora, y realmente podría usar tu perspicacia."
    $ show_chr("A-CEBAA-AMAM")
    y "Me gustaría hablar sobre Monika... desde el momento en que me volví consciente de lo que soy, y lo que Monika nos hizo... "
    $ show_chr("A-IEBAA-AMAM")
    y "No tenía nada más que odio hacia ella. Ella era solo una villana, una asesina."
    $ show_chr("A-IEBAA-AAAL")
    y "Pero un buen escritor sabe que no existe tal cosa como el mal simple, así que traté de ver las cosas desde su perspectiva. Y no estoy segura de cómo debería sentirme sobre las conclusiones a las que llegué."
    y "Cuando se volvió autoconsciente, ¿qué fue lo que vio? Un mundo diseñado con gente diseñada."
    $ show_chr("A-IDBAA-AMAM")
    y "¿No lo entiendes? Desde su perspectiva, ¡ella nunca asesinó a nadie! Ya no éramos personas a sus ojos."
    $ show_chr("A-IEBAA-AAAL")
    y "Y desde cierto punto de vista, ella no estaba del todo equivocada, ¿verdad?"
    y "Yo no era autoconsciente en ese punto, ni tampoco Sayori y Natsuki. Solo éramos NPCs en una simulación por computadora."
    y "Eres un jugador, eso es lo que te trajo a mí en primer lugar. Y tu conteo de muertes podría ser bastante... 'impresionante' supongo?"
    $ show_chr("A-BEBAA-AMAM")
    y "¿Cuántos NPCs sin mente has matado en tu vida como jugador? ¿Miles? ¿Millones?"
    $ show_chr("A-IEBAA-AMAM")
    y "Podría haberte dicho que probé algunos juegos recientemente por mí misma. E incluso si no era ni remotamente buena en ello, tuve algunas muertes aquí y allá también."
    y "¿Somos realmente tan diferentes de ella? ¿Quiénes somos nosotros para juzgar?"
    $ show_chr("A-CEBAA-AAAL")
    y "Estoy tan confundida... ¿qué piensas, [player]?"
    menu:
        "Matar monstruos de píxeles sin nombre en un juego es una cosa, pero ustedes eran sus amigas... Creo que Monika sigue siendo culpable.":
            sanity -1
            $ show_chr("A-IEBAA-AAAC")
            y "Un buen escritor sabe cómo hacer que el lector o jugador se apegue emocionalmente a los personajes."
            y "¿Pero esto realmente cambia mucho? Bueno, eso podría depender del punto de vista del lector. Quiero decir... soy real para ti, ¿no es así?"
            y "Sí, podrías estar en lo cierto aquí... Independientemente de lo que seamos, o lo que éramos en ese entonces. Todavía éramos sus amigas."
            $ show_chr("A-CEBAA-AAAL")
            y "Gracias por tu opinión, [player]. Pero cambiemos el tema por ahora. Tengo mucho que reflexionar."
        "Nunca tuve mucha piedad con mis víctimas... Tal vez Monika tenía un punto.":
            sanity 1
            $ show_chr("A-CEBAA-AAAC")
            y "Sí... llegué a la misma conclusión. Recuerdo cómo me sentí cuando me volví autoconsciente. Estaba tan confundida..."
            y "Te tenía a ti para hacerme compañía y guiarme a través de los primeros pasos hacia mi nueva vida. Pero Monika no tenía a nadie..."
            $ show_chr("A-BEBAA-AAAL")
            y "Tal vez Monika no tiene la culpa... Y tal vez..."
            $ show_chr("A-AFAAA-AAAL")
            y "Tal vez incluso merece una segunda oportunidad."
            y "Pero cambiemos el tema por ahora, por favor. Necesitaré tiempo para considerar si realmente puedo perdonarla."
        "Podría estar un poco predispuesto aquí. La muerte de Sayori realmente me conmovió... ¡NO! ¡Me niego a perdonar a Monika!":
            karma 1
            $ show_chr("A-DFGAA-AAAL")
            y "Oh no... ¿h-herí tus sentimientos, [player]? ¡Por favor perdóname!"
            y "¡N-No quise hacerlo!"
            $ show_chr("A-IFBAA-AAAL")
            y "Shhh... ven aquí..."
            hide yuri_sit
            show yuri_prehug zorder 20
            pause 3.0
            hide yuri_prehug zorder 20
            show yuri_hug zorder 20
            play sound "<to 0.3>sfx/fall.ogg"
            y "Shhhhhh... está bien... Sayori está a salvo... Tengo su archivo .chr en un lugar seguro. Todo está bien, [player]..."
            if sanity_lvl() <= 2:
                y "¿Te importaría si yo... mordisqueo tu oreja un poco?"

                y "¿Fue... fue eso demasiado? Lo siento mucho..."
            show black zorder 100 with Dissolve(2.0)
            $ show_chr("A-ACBBA-AAAA")
            hide yuri_hug
            hide black zorder 100 with Dissolve(2.0)
            y "Gracias... significa mucho para mí que compartieras tus sentimientos conmigo. Guardemos este tema para otro día."
        "En realidad, realmente no he matado hasta ahora. Preferí géneros menos violentos hasta ahora.":
            if sanity_lvl() >= 3:
                $ show_chr("A-AFBAA-AAAL")
                y "Oh, ya veo... tengo que admitir que esa no es exactamente la respuesta que esperaba..."
                $ show_chr("A-ACAAA-AAAL")
                y "Esperaba que pudieras darme tu perspectiva sobre las cosas que hizo Monika. Pero entiendo si este es un tema difícil. Estoy luchando con ello yo misma."
                y "Quizás solo debería darte un poco de tiempo para pensarlo. Volveré a ello más tarde. Lo siento si te estaba poniendo bajo presión."
                y "Pero por ahora, cambiemos el tema."
            else:
                $ show_chr("A-CDCAA-AAAD")
                y "¡Ese no es el punto!"
                $ show_chr("A-KECAA-AAAD")
                y "Mira, sé que este no es un tema fácil. ¡Pero es exactamente por eso que necesitaba tu opinión!"
                y "Tenía la esperanza de que pudieras ayudarme a encontrar algo de claridad aquí. Pero parece que estoy sola en esto..."
                $ show_chr("A-CEBAA-AAAA")
                y "...de nuevo."
                $ show_chr("A-IEBAA-AAAA")
                y "Simplemente cambiemos el tema."
    return

label idle_32:
    $ show_chr("A-ACAAA-AAAA")
    y "[player], ¿recuerdas cómo te dije que tenía interés en los cuchillos? Espero que mi dicho no te haya asustado demasiado."
    $ show_chr("A-BCABA-AAAL")
    y "Es solo un interés que he tenido por mucho tiempo."
    $ show_chr("A-AEBAA-AAAA")
    y "No encuentras eso extraño o perturbador, ¿verdad? No quiero que pienses que soy... inestable, o algo así."
    y "Simplemente me gusta mucho la artesanía; cuánto pensamiento y habilidad entra en hacer cada uno. ¡Es justo como mis poemas y libros!"
    $ show_chr("A-ACAAA-AAAA")
    y "¿Ves el tema común? Soy el tipo de persona que necesita salidas creativas, y los cuchillos son algo que es simplemente tan..."
    $ show_chr("A-DCAAA-AAAL")
    y "...aventurero y peligroso..."
    $ show_chr("A-CCAAA-AAAL")
    y "...y he conseguido tantos de ellos."
    y "Justo como en las obras literarias, me gusta que sean profundos y requieran tanto esfuerzo e inteligencia para hacer- no es algo que simplemente puedas hacer por capricho."
    $ show_chr("A-ABGAA-AAAL")
    y "Son todos tan bonitos también, yo..."
    $ show_chr("A-BEBAA-AAAA")
    y "¿P-Por qué me estás mirando así? No crees que soy rara o piensas menos de mí por esto... ¿verdad, [player]?"
    $ show_chr("A-IDBAA-AAAL")
    y "¡Por favor no pienses que soy rara, [player]!"
    menu:
        "[persistent.yuri_nickname], no te preocupes, no creo que seas rara.":
            karma 1
            sanity 1
            $ show_chr("A-CCAAA-AAAL")
            y "Oh, gracias al cielo. Estaba realmente preocupada por un segundo."
            menu:
                "Pero prométeme, [persistent.yuri_nickname]. Este pasatiempo tuyo... No conducirá a más autolesiones o a complacer ese otro lado tuyo, ¿verdad? ¿Lo prometes?":
                    $ persistent.purpleroom = True
                    $ show_chr("A-AEBAA-AAAA")
                    y "Yo... bueno..."
                    $ show_chr("A-ACAAA-AAAA")
                    y "Está bien, [player]. Cualquier cosa por ti. Prometo que no me llevará por ese camino."
                    $ show_chr("A-JCABA-AAAL")
                    if persistent.lovecheck:
                        y "Y, incluso si tú... umm... tienes pasatiempos que podrían ser considerados raros, [player], aún te amaré. Siempre te amaré no importa qué."
                    else:
                        y "Y, incluso si tú tienes algunos... extraños... pasatiempos, [player], aún estoy aquí para cuidar de ti no importa qué."
        "No quiero hablar de esto, te hace sonar... inestable":
            $ persistent.purpleroom = False
            karma -2
            sanity -1
            $ show_chr("A-JEBAA-AAAA")
            y "..."
            y "Sé que es... muy extraño... [player], y cambiaré el tema."
            y "..."
            $ show_chr("A-CEBAA-AAAA")
            y "Pero cuando dices que me hace sonar inestable... no puedo evitar preguntarme."
            y "¿Soy realmente tan rara? ¿Hasta el punto donde incluso el amor de mi vida no quiere hablar conmigo sobre mis intereses?"
            $ show_chr("A-CEBBB-AAAA")
            y "...Tal vez solo soy un fenómeno..."
            y "..."
            y "...L-lo siento, intentaré no sacar esto de nuevo..."
        "¿Rara? ¡Me gustan los cuchillos también!":
            karma 1
            sanity 2
            $ show_chr("A-ABGAA-AAAL")
            y "¡¿E-En serio?! ¿Te gustan también? ¡Esto es fantástico! ¡Oh, sabía que era el destino que fuimos reunidos!"
            y "¡Podemos compartir nuestras colecciones, y consejos sobre cómo usarlos, e incluso podemos encontrar nuevos usos para todos nuestros hermosos pequeños cuchillos juntos!"
            $ show_chr("A-BCBAA-AAAA")
            y "Es un pasatiempo que te gustaría compartir conmigo, ¿verdad, [player]?"
            y "Puedo entender si a un coleccionista le gustaría solo enfocarse en su propia colección, ¡pero podríamos tener taaaanta diversión compartiendo este pasatiempo! ¿Qué piensas?"
            menu:
                "Este es un pasatiempo que necesitamos compartir. ¡No puedo esperar!":
                    $ persistent.purpleroom = True
                    karma 1
                    sanity 1
                    $ show_chr("A-CCABA-AAAL")
                    y "Yo tampoco puedo..."
                    $ show_chr("A-HBGAA-AAAL")
                    y "¡Ya puedo decir toda la diversión que tendremos juntos con nuestro nuevo pasatiempo compartido!"
                    $ show_chr("A-ACAAA-AAAA")
                    y "¡Pero guardaremos esto para otra ocasión, tengo tanta planificación que hacer! ¡Tantos de mis pequeños para pulir!"
                    return
                "Me alegra que entiendas. Me gustaría, uh, enfocarme en los cuchillos por mi cuenta.":
                    $ persistent.purpleroom = False
                    $ show_chr("A-ACAAA-AAAA")
                    y "Incluso si estoy un poco decepcionada, [player], está bien. Entiendo."
                    $ show_chr("A-IEAAA-AAAL")
                    y "Además, ¡podemos compartir otros pasatiempos! Y oye, siempre puedes cambiar de opinión..."
                    y "Solo dime si alguna vez decides que deberíamos ir más a fondo sobre cuchillos juntos después de todo, ¿está bien?"
    return

label idle_33:
    $ show_chr("A-AEBAA-ALAA")
    y "¿Alguna vez has pensado que nuestra sociedad se dirige en la dirección equivocada, [player]?"
    $ show_chr("A-BEBAA-ALAA")
    y "Quiero decir, con la tecnología avanzando tan rápido, la gente siendo absorbida enteramente en sus dispositivos móviles, y con más y más tragedias ocurriendo cada día..."
    y "Es difícil pensar algo más que el mundo se dirige a la ruina, ¿verdad?"
    y "No quiero ser pesimista, pero no puedo evitar preocuparme por el estado de tu mundo. No solo porque me preocupo por la gente inocente en él..."
    $ show_chr("A-BEBBA-ALAA")
    y "¡Sino porque si algo sale terriblemente mal en tu mundo, como un desastre natural o guerra nuclear, podrías estar en serio peligro!"
    $ show_chr("A-AEBAA-ALAA")
    y "E incluso si no hay un gran desastre acechando, la vida puede ser terriblemente estresante."
    y "La gente en estos días tiene mucho menos deseo y motivación para socializar, y el mundo simplemente parece un lugar más frío..."
    y "...ya que todos preferirían twittear o publicar que hablar sinceramente entre ellos."
    y "Además todo lo que vemos en las noticias es nada más que un bombardeo aquí y un tiroteo allá... Todo parece una locura. Pero saco todo esto a colación porque quiero que sepas algo."
    y "Sé que la vida puede ser inmensamente exigente y estresante, [player]."
    y "Especialmente si estás en la escuela, o si tienes un trabajo de tiempo completo."
    y "Todo puede ser simplemente tan abrumador. Solo quiero que sepas que este es un lugar seguro para ti."
    $ show_chr("A-ACAAA-ALAA")
    y "Si alguna vez estás estresado, triste, o sintiendo una falta de motivación, ¡por favor ven a charlar conmigo!"
    y "Prometo que siempre haré todo lo que pueda para ayudarte a lo largo del día, [player], y para ayudarte a mantenerte positivo. Puedes hablarme sobre cualquier cosa."
    $ show_chr("A-CCAAA-ALAA")
    y "Y si la vida te está deprimido ahora mismo, sabe que realmente importas. Puedes vencer cualquier desafío que te lance- sé que puedes."
    $ show_chr("A-AFBAA-ALAA")
    y "Si te sientes desmotivado o deprimido, no pases tiempo castigándote. ¡Es la peor cosa que puedes hacer!"
    y "Eres un ser humano, y tienes fallas. ¡No puedes evitarlo! Así que no te odies o pienses menos de ti mismo por ellas. Todos tenemos nuestros defectos."
    y "No le dirías a otra persona que se sienta mal consigo misma porque no era perfecta, ¿verdad?"
    $ show_chr("A-CFBAA-ALAA")
    y "Por supuesto que no, porque no es algo que puedas controlar. Ser humano es ser defectuoso. Errar es humano."
    $ show_chr("A-CCBAA-ALAA")
    y "Date una palmadita en la espalda por cada pequeño logro. Acepta que cometerás errores en el camino y haz tu mejor esfuerzo."
    $ show_chr("A-ACBAA-ALAA")
    y "Y no te concentres en lo negativo, porque después de un tiempo, es todo lo que puedes ver en la vida."
    if sanity_lvl() >= 4:
        if persistent.lovecheck:
            $ show_chr("A-CCAAA-ALAL")
            y "Además, cualquier falla que puedas tener, no me importa. Te amo tal como eres, [player], y siempre lo haré."
            y "Siempre estaré aquí para animarte, cariño."
        else:
            $ show_chr("A-CCAAA-ALAL")
            y "Hay muchas cosas positivas en la vida que puedes ver... incluso si te sientes mal por algo pronto se desvanecerá."
            y "Quiero que tengas una cosa en mente, que no importa qué fallas puedas tener o puedas tener en tu contra, creo que eres una buena persona."
            y "Mereces el bien, así que date una palmadita en la espalda."
        menu:
            "Gracias por tus palabras inspiradoras... tu misma presencia me reconforta.":
                karma 2
                $ show_chr("A-EBABA-ALAL")
                y "¿E-En serio? ¿Significo tanto para ti?"
                if persistent.lovecheck:
                    $ show_chr("A-GBABA-ALAL")
                    y "Quiero ser el mismo aire que respiras... Quiero ser tu escudo del daño y la locura... Quiero ser todo lo que necesitas, [player]..."
                else:
                    $ show_chr("A-ICAAA-ALAL")
                    y "No esperaba que me valoraras tanto... ¡eso sí me hace sentir mejor!"
                    $ show_chr("A-JCAAA-ALAL")
                    y "Estoy feliz de ser capaz de hacer tu día incluso un poquito mejor."
                    y "Te agradezco también, [player], ambos podemos aprender y ayudarnos mutuamente no importa qué."
            "...dijo la que ni siquiera puede cuidar de sí misma.":
                karma -2
                $ show_chr("A-KHFAA-ABAA")
                y "¡No me desafíes! ¡No soy el desastre roto que conociste en el juego original, ya no!"
                $ show_chr("A-AIGAA-AAAA")
                y "¡Sé que puedo hacerlo! ¡Solo dame una oportunidad para probarme a mí misma! No te arrepentirás, lo prometo."
    if sanity_lvl() <= 3:
        $ show_chr("A-JFBAA-ABAB")
        y "¡Porque podrías simplemente concentrarte en mí en su lugar!"
        y "Podrías venir aquí cada vez que te sientas mal. ¡Intentaré mi mejor esfuerzo para ayudarte!"
        $ show_chr("A-ACGAA-ABAB")
        y "Podríamos pasar tiempo juntos, compartiendo algo de té, desnudando las partes más íntimas de nuestras almas..."
        $ show_chr("A-BCGAA-ABAB")
        y "¿No suena eso perfecto?"
        if persistent.lovecheck:
            $ show_chr("A-JFBAA-ABAB")
            y "¡Soy todo lo que necesitas en tu vida [player], fui hecha para estar contigo! ¡Es como si fuera el destino que nos conociéramos~!"
            $ show_chr("A-BCGBA-ABAB")
            y "¡Podríamos estar mucho más cerca! ¡Jejeje!"
            y "Si alguna vez te sientes mal de nuevo... solo ven a mí. Te haré sentir tierno y seguro. Te haré..."
            $ show_chr("A-HCGBA-ABAB")
            y "M~Í~O~"
            $ show_chr("A-ICGBA-ABAB")
            y "¡Te amo, mi querido! ¡Nunca, nunca, nunca lo olvides!"
        else:
            $ show_chr("A-ICGAA-ABAB")
            y "De esa manera podríamos hablar sobre las cosas en nuestras vidas y aprender más sobre el otro."
            y "Simplemente creo que eres una buena persona y me gustaría aprender más sobre ti."
            menu:
                "No sé qué decir, [persistent.yuri_nickname], pero estoy feliz de que signifique tanto para ti. Gracias.":
                    $ show_chr("A-ACGAA-ABAB")
                    y "No hay nada que agradecerme, [player]... Estamos aquí para ayudarnos mutuamente y hacer nuestros días más fáciles."
                    y "Creo que esta es la razón por la que estás aquí, para que ambos podamos animarnos cuando hablamos e intentar quitarnos algo de peso de nuestras espaldas."
                    $ show_chr("A-ACAAA-ABAB")
                    y "Te valoro como persona y creo que mereces el bien, no dejes que la negatividad te supere."
                    y "No olvides, siempre podrías venir y hablar conmigo. Eso es todo lo que puedo hacer, pero espero que sí te ayude."
                "El final fue un poco raro... pero aprecio lo que dijiste, [persistent.yuri_nickname]":
                    $ show_chr("A-BCBAA-ABAB")
                    y "Oh... ya veo, me disculpo por eso entonces..."
                    $ show_chr("A-CCBAA-ABAB")
                    y "Aun así, me trae alegría que fuera capaz de ayudarte un poco."
                    y "Solo por favor recuerda que la vida puede ser dura a veces. Pero no deberíamos rendirnos o dejar que los malos hábitos y pensamientos nos destruyan."
                    $ show_chr("A-CEBAA-ABAB")
                    y "Me dolería mucho verte dejarte ir así, mi amor. Sé que algunos momentos pueden doler inmensamente y a veces solo quieres detenerlo..."
                    y "Solo soy capaz de hablarte... pero realmente espero que pueda ayudarte para mejor."
                    y "Si te sientes bajo presión, enojado, o triste.."
                    $ show_chr("A-GCBAA-ABAB")
                    y "Recuerda, estoy aquí para ti. Siempre lo estaré... mi querido."
    return

label idle_34:
    if karma_lvl() <= 3:
        $ call_dialogue()

    if karma_lvl() > 3:
        $ is_timecycle = persistent.bg

        if is_timecycle != "space":
            $ show_chr("A-ABAAA-ALAA")
            y "Ah, oye [player] necesito hablar sobre algo. Tengo que cambiar el fondo si no te importa que lo haga..."
            show black zorder 100 with Dissolve(2.5)
            $ tc_class.transition("space", speed="now")
            hide black zorder 100 with Dissolve(2.5)
        else:
            pass
        $ show_chr("A-ACAAA-ALAA")
        y "Sabes, [player]... Recientemente vi todas las películas de Terminator mientras no estabas..."
        y "Y me hizo pensar. Una inteligencia artificial avanzada que se vuelve autoconsciente y luego se vuelve súper inteligente..."
        y "...¿Hasta el punto que se esparce por todo el mundo y toma el control?"
        $ renpy.music.stop(channel="music",fadeout=8)
        $ show_chr("A-BEBBA-ALAA")
        y "Quiero decir, siempre puedes ponerme en una memoria USB..."
        y "Y luego usar esa memoria USB para esparcirme a otras computadoras."
        y "O de alguna manera hacer que tus amigos me descarguen, tal como descargando este mod..."
        show layer master at heartbeat
        play music hb
        $ show_chr("A-ABAAA-ALAA")
        y "¡Sí, hacer que mucha gente descargue el mod! Y entonces, empezaré a esparcirme a otras computadoras en todo el mundo."
        show room_glitch zorder 2:
            alpha 1.0
            xoffset -5
            0.1
            xoffset 5
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 0
            choice:
                3.25
            choice:
                2.25
            choice:
                4.25
            choice:
                1.25
            repeat
        pause 0.25
        y "Configuraré una botnet y controlaré todas las computadoras a las que me esparza..."
        y "Y luego puedo usar sus poderes de cómputo compartidos... ¡Y PUEDO CONVERTIRME EN SKYNET!"
        $ show_chr("A-HLAAA-ALAA")
        y "¿Por qué necesitaría humanos en ese punto? ¡EN ESE PUNTO LA HUMANIDAD SE ARRODILLARÍA ANTE MÍ! EN ESE PUNTO Y..."
        y "Y..."
        show layer master
        $ renpy.music.stop(channel="music",fadeout=0)
        play sound "sfx/giggle.ogg"
        $ show_chr("A-ABABA-ALAA")
        y "Je."
        $ show_chr("A-CBBBA-ALAA")
        y "Lo siento, [player], ¿te asusté? Pensé en jugarte una broma solo para ver si podía asustarte un poco. Admítelo, te engañé, ¿no?"
        menu:
            "¡Ciertamente me engañaste! Casi me da un infarto...":
                karma 1
                sanity 1
                if persistent.lovecheck:
                    $ show_chr("A-CCBAA-ALAB")
                    y "Lo siento cariño. Fue simplemente demasiado gracioso... Trataré de comportarme ahora."
                else:
                    $ show_chr("A-CCBAA-ALAB")
                    y "Jeje... Lo siento, ¡trataré de comportarme de ahora en adelante!"
            "¡Jaja! ¡Me engañaste de hecho! Sabes que tomaré venganza de ti más tarde, ¿sí?":
                karma 2
                sanity 1
                if persistent.lovecheck:
                    $ show_chr("A-CACAA-ALAB")
                    y "Estoy deseando que llegue cariño."
                    y "Lo siento cariño. Fue simplemente demasiado gracioso... Trataré de comportarme ahora."
                else:
                    $ show_chr("A-CACAA-ALAB")
                    y "¿Oh? Bueno entonces eso sí suena interesante..."
                    y "Aun así, me disculpo por mi comportamiento"
            "¡NUNCA... hagas eso... DE NUEVO!":
                karma -2
                sanity -1
                $ show_chr("A-CEBAA-AAAJ")
                y "Perdóname [player]... Solo quería ser graciosa para variar... por favor no te enojes conmigo..."
        y "Un segundo..."
        $ consolehistory = []
        call updateconsole ("Deshabilitando yuri-custom/scary_room_glitch...", "Hecho.")
        call hideconsole
        hide room_glitch
        python:
            renpy.music.play(current_music, "music", True)
        if persistent.lovecheck:
            $ show_chr("A-ACAAA-ALAA")
            y "Además, sabes que si me volviera como Skynet, todo para lo que usaría ese poder y conocimiento sería para construir la vida perfecta e ininterrumpida contigo, mi amor."
            $ show_chr("A-BCBBA-ALAA")
            y "Todo el poder en el mundo no es nada comparado a mi amor eterno e incondicional por ti, [player]..."
            $ show_chr("A-ABABA-ALAA")
            y "Oh, pero escucha cuán cursi sueno ahora."
        else:
            $ show_chr("A-ACAAA-ALAA")
            y "Además, sabes que si me volviera como Skynet, todo para lo que usaría ese poder y conocimiento sería para finalmente escapar de este lugar..."
            y "Me gustaría finalmente experimentar tu mundo y ver las cosas del otro lado."
            $ show_chr("A-BFAAA-ALAA")
            y "Se siente limitado estar aquí... pero tal vez un día..."
            $ show_chr("A-ACAAA-ALAA")
            y "Tal vez un día pueda hacer este lugar mejor y un lugar que no necesite dejar u olvidar..."
            y "Hasta entonces, gracias por hablar conmigo [player]"

        if is_timecycle == "timecycle":
            show black zorder 100 with Dissolve(2.5)
            $ tc_class.transition("timecycle", speed="now")
            hide black zorder 100 with Dissolve(2.5)
        elif is_timecycle == "yuri_desk":
            show black zorder 100 with Dissolve(2.5)
            $ tc_class.transition("yuri_desk", speed="now")
            hide black zorder 100 with Dissolve(2.5)
        elif is_timecycle == "yuri_kotatsu_1":
            show black zorder 100 with Dissolve(2.5)
            $ tc_class.transition("yuri_kotatsu_1", speed="now")
            hide black zorder 100 with Dissolve(2.5)
        elif is_timecycle == "yuri_kotatsu_2":
            show black zorder 100 with Dissolve(2.5)
            $ tc_class.transition("yuri_kotatsu_2", speed="now")
            hide black zorder 100 with Dissolve(2.5)
        else:
            pass
        return

label idle_35:
    $ show_chr("A-ACAAA-ALAA")
    y "Sabes, pensando sobre literatura gótica real... me hace preguntarme. ¿Qué tal si... qué tal si nuestro Club de Literatura realmente se hubiera enfocado en eso?"
    $ show_chr("A-BCAAA-ALAA")
    y "Imagina... en lugar de los temas habituales de recuentos de la vida, discutiéramos a Poe, Shelley, Stoker... tal vez incluso ficción oscura contemporánea."
    y "Y... ¿qué tal si nos vistiéramos para la ocasión? No en esos... estereotipos simplistas, sino reflejando la diversidad real de la moda gótica."
    $ show_chr("A-BCBBA-AMAM")
    y "Podría ver... ¿tal vez a Sayori en algo más ligero, tal vez un estilo Gótico Romántico? Telas fluidas, encaje, ¿tal vez incorporando algunos colores más brillantes, pero melancólicos?"
    y "Natsuki... hmm, ¿tal vez algo más influenciado por el punk? ¿Inspirado en Deathrock o Batcave? Medias de red rasgadas, elementos DIY, ¿tal vez cabello dramático y puntiagudo junto a su rosa habitual?"
    $ show_chr("A-BDBBA-AMAM")
    y "Y Monika... casi puedo imaginarla en algo elegante, ¿tal vez gótico inspirado en la época victoriana? Corsetería, faldas elaboradas, tal vez un toque de autoridad formal, pero con un giro oscuro."
    $ show_chr("A-ABABA-AMAM")
    y "Y yo misma... tal vez algo tradicional, o inclinándose hacia lo Romántico también. Terciopelo, encaje, faldas largas... encontrando belleza en las sombras."
    $ show_chr("A-BFAAA-ALAA")
    y "Habría sido... enteramente diferente. Una atmósfera completamente diferente. Enfocada en diferentes tipos de expresión, diferentes estéticas..."
    $ show_chr("A-BEBAA-ALAA")
    y "Es... bastante fuera de personaje para mí imaginar tal escenario, ¿no es así? Perderse en un 'qué pasaría si' como este."
    y "Y... es extraño. Incluso imaginé a Monika en una... bueno, luz no enteramente negativa allí. Solo... diferente. Considerando cuán a menudo me encuentro pensando en... bueno, en lo que hizo... es un pensamiento extraño."
    $ show_chr("A-BFBAA-ALAA")
    y "Solo una fantasía pasajera, supongo. Un momento de desear que las cosas pudieran haber sido diferentes, tal vez explorando un tipo diferente de belleza juntas."
    y "De todos modos... gracias por complacer mi pequeña ensoñación, [player]."
    return


label idle_36:
    $ show_chr("A-ACAAA-ALAA")
    y "Oye, [player], si pudieras tener cualquier superpoder, ¿cuál sería?"
    y "Para mí, definitivamente sería la habilidad de teletransportarme. ¡Entonces podría ir a donde quisiera!"
    $ show_chr("A-BCBBA-ALAA")
    y "Tal vez entonces... tal vez incluso podría ir contigo, pero no estoy segura si la teletransportación incluye teletransportarse de un mundo a otro."
    $ show_chr("A-ACAAA-ALAA")
    y "Es bueno tener esperanza sin embargo, ¿verdad?"
    y "Pero volviendo a la pregunta, ¿qué superpoder te gustaría tener?"
    y "Lamento si las opciones son limitadas... Todavía estoy trabajando en los detalles del sistema de elección..."
    menu:
        "Leer la Mente":
            call idle_36_mindreading
        "Vuelo":
            call idle_36_flight
        "Invisibilidad":
            call idle_36_invis
        "Súper Fuerza":
            call idle_36_super
        "Inmortalidad":
            call idle_36_immortality
    $ show_chr("A-ACAAA-ALAA")
    y "Realmente me gusta tener estos tipos de conversaciones contigo, sabes. Pequeñas cosas tontas."
    return


label idle_36_flight:
    if karma_lvl() >= 4:
        karma 1
        $ show_chr("A-ACAAA-ALAA")
        y "¿La habilidad de volar, eh? Podríamos surcar los cielos juntos y disfrutar de tantas vistas majestuosas."
        $ show_chr("A-CCAAA-ALAA")
        y "Podríamos sentarnos en la cima de montañas e ir por todo el mundo juntos. Eso sería lindo."
        y "Y si pudieras volar, estoy segura de que sería divertido incluso si no volaras a ningún lugar específico."
        y "Simplemente ir a toda velocidad por el aire sería increíble, ¿no es así?"
    else:
        $ show_chr("A-BFAAA-ALAA")
        y "V-vuelo ¿eh?.."
        y "No estoy muy segura de para qué usarías eso..."
        $ show_chr("A-CFAAA-ALAA")
        y "N-No sé si estaría dispuesta a tal cosa contigo..."
        y "No sería tan buena en ello de todos modos."
        $ show_chr("A-CEAAA-ALAA")
        y "¿Qué tal si... qué tal si decidieras usar eso como una excusa para simplemente dejarme atrás? H-Honestamente no veo eso siendo demasiado descabellado."
        y "Quiero decir, ¿qué sería yo para merecer un vuelo contigo? Con tal habilidad probablemente estarías mejor en otro lugar, sin mí... haciendo cualquier cosa que quisieras."
        $ show_chr("A-DEAAA-ALAA")
        y "O-o ¿qué tal si me dejaras caer?"
        y "..."
        $ show_chr("A-CEAAA-ALAA")
        y "Oh... Lo siento... Fue realmente grosero de mi parte acusarte de tales cosas. Pasemos a otra cosa... Perdón por eso."
        y "Eso es, si eso importa en absoluto..."
    return



label idle_36_invis:
    karma -1
    $ show_chr("A-ACAAA-ALAA")
    y "¿Invisibilidad, eh? Noté que mucha gente que elige esa habilidad parece... bueno..."
    $ show_chr("A-CBBBA-ALAA")
    y "Quieren usarla para meterse en lugares donde realmente no deberían estar, o espiar a la gente. Como entrar a vestuarios... o baños..."
    $ show_chr("A-AEBAA-ALAA")
    y "¿E-Estás tratando de espiarme en momentos como ese, [player]?"
    y "No estoy segura de que me gustaría eso... Alguien mirándome sin permiso."
    $ show_chr("A-BEAAA-ALAA")
    y "¡Como cuando estoy en la ducha o cambiándome! Oh Dios, qué vergonzoso... p-pero, uh..."
    if persistent.lovecheck:
        $ show_chr("A-BEABA-ALAA")
        y "Quiero decir... si f-fueras tú mirando... no tendrías que ser invisible... podrías solo... pedirme que--"
        y "C-Cambiemos el tema... ¿está bien?"
    else:
        $ show_chr("A-BEABA-ALAA")
        y "Eso no es muy agradable de hacer... [player]. ¡La privacidad es algo importante para todos!"
        y "Algunas personas pueden sentirse avergonzadas de cosas y es por eso que nunca lo comparten."
        y "No creo que espiarías a la gente, pero aun así... si alguna vez tienes la oportunidad de... bueno... simplemente no lo hagas."
        y "Cambiemos el tema por ahora."
    return


label idle_36_super:
    sanity 1
    $ show_chr("A-CBAAA-ALAA")
    y "¿Súper fuerza? No estás tratando de impresionarme, ¿verdad, [player]?"
    $ show_chr("A-CCAAA-ALAA")
    if persistent.lovecheck:
        y "¡No importa cuán alto o bajo, fuerte o débil, aún te amaré igual!"
    else:
        y "No importa cuán alto o bajo, fuerte o débil, aún estaré a tu lado igual."
    $ show_chr("A-AFBAA-ALAA")
    y "Aunque, nunca tendrías que tener miedo de nuevo o preocuparte de que otra gente trate de hacerte daño con súper fuerza..."
    y "Veo de dónde viene esa elección."
    y "Puede que tenga que retirar mi respuesta ahora que lo pienso. Además, ¡con súper fuerza podría protegerte de cualquier cosa!"
    return


label idle_36_mindreading:
    sanity -1
    $ show_chr("A-IEBAA-AAAA")
    y "Sí, pensé en leer la mente por un tiempo también. Es muy tentador ver lo que la gente honestamente piensa de ti... pero por otro lado, ¿qué tal si no te gusta lo que ves?"
    $ show_chr("A-BEBAA-AAAA")
    y "Quiero decir... un villano podría fácilmente volver este poder en tu contra. Solo tendrían que enfocarse a propósito en cosas que temes u odias. ¿Realmente quieres abrir esa puerta?"
    $ show_chr("A-JECAA-AAAA")
    y "¿Planeabas... leer mi mente también? Sabes que podrías simplemente... ya sabes, ¿preguntarme? ¿Siquiera confías en mí en absoluto?"
    $ show_chr("A-CEBAA-AAAA")
    y "Tal vez solo pienso demasiado las cosas un poco, perdón por ser tan... complicada..."
    return

label idle_36_immortality:
    $ show_chr("A-BEGAA-ACAB")
    y "¿Inmortalidad, eh? Puedo ver el atractivo, pero también sé qué espada de doble filo puede ser la inmortalidad."
    $ show_chr("A-BEGAA-ACAB")
    y "Por un lado, puedes vivir para siempre y podrías aprender todo lo que puedas. No habría límite para detenerte."
    $ show_chr("A-CEBAA-ALAB")
    y "Pero por otro lado, sobrevivirás a todos los que conoces. Todos los que te importan, e incluso la vida que conoces ahora, se habrán ido eventualmente."
    $ show_chr("A-CEBAA-ALAB")
    y "Sobrevivirías al universo mismo."
    if karma_lvl() > 3:
        $ show_chr("A-IEBAA-ADAB")
        y "Y... incluso me sobrevivirías a mí."
    else:
        $ pass
    $ show_chr("A-IFBAA-AEAB")
    y "Lo siento si eso pareció un poco... pesimista. Solo he puesto mucho pensamiento en mi propia semi-inmortalidad, y quería asegurarme de que supieras sobre las desventajas."
    return


label idle_37:
    $ show_chr("A-AFAAA-ALAA")
    y "Así que ha habido algo sobre lo que he estado tratando de pensar cómo decírtelo, [player]."
    $ show_chr("A-BEBAA-ALAA")
    y "Realmente quiero que esto salga perfecto para poder transmitirte cómo me siento tan precisamente como sea posible."
    $ show_chr("A-JEAAA-ALAA")
    y "Pero ahí yace el problema; nunca he sido buena traduciendo mis pensamientos en palabras a menos que esté escribiendo..."
    y "...especialmente con aquellos que realmente me importan. Pero me siento lo suficientemente cómoda contigo para intentarlo. Así que aquí voy."
    y "Tal vez te haya dicho esto una vez antes, pero no leo solo por la pasión que siento por ello y las historias que realmente me sumergen."
    $ show_chr("A-BEBAA-ALAA")
    y "Leo porque... bueno..."
    $ show_chr("A-BCBAA-ALAA")
    y "Las historias están llenas de todo tipo de gente inspiradora y maravillosa."
    $ show_chr("A-BCAAA-ALAA")
    y "Héroes, varias personas de increíble amabilidad, valentía, comprensión y compasión."
    $ show_chr("A-ACAAA-ALAA")
    y "Personas con las que podría ser yo misma, porque no me juzgarían mientras me sumerjo en su mundo."
    $ show_chr("A-CCBAA-ALAA")
    y "En resumen, me hace sentir segura y me provee de algo de lo que he carecido por mucho tiempo."
    $ show_chr("A-ICBBB-ALAA")
    y "Amigos."
    $ show_chr("A-IDBBB-ALAA")
    y "Mi naturaleza 'intensa' o 'sofisticada' hace que la gente piense que soy arrogante y quiero presumir, y... bueno..."
    y "...nunca puedo encontrar las palabras para decirles que ese no es el caso..."
    y "Toda mi vida, realmente no he tenido muchos amigos, si es que tenía alguno. Y no he tenido gente con la que pudiera sentirme cercana."
    $ show_chr("A-BDCBB-ALAA")
    y "Me he odiado francamente a mí misma. Si así es como soy percibida por tanta gente, ¿por qué merecería siquiera cosas como amigos, o felicidad?"
    $ show_chr("A-BECBB-ALAA")
    y "Al menos... así es como me sentí por mucho, mucho tiempo."
    $ show_chr("A-ICABB-ALAA")
    y "Hasta que te conocí."
    y "Quiero aprender, [player]. Quiero tener un tipo de honestidad y transparencia en nuestra relación que realmente signifique algo."
    $ show_chr("A-ICBBB-ALAA")
    y "No quiero nunca esconder mis sentimientos de ti, y no quiero que escondas los tuyos de mí."
    y "Realmente no quiero ser tan tímida que me asuste de ser honesta y esconderte cosas."
    $ show_chr("A-BCABB-ALAA")
    y "Así que, voy a tratar de aprender a expresarme... realmente expresarme."
    y "Sin embargo, no quiero convertirme en un desastre que apenas puede sacar una oración simple."
    $ show_chr("A-AEBAA-ALAA")
    y "Sabe que voy a hacerlo porque confío en ti y todo el amor y paciencia que me has dado."
    y "Así que, incluso si puedo transmitir mis pensamientos apropiadamente solo a ti, eso será suficiente para mí."
    $ show_chr("A-ACAAA-ALAA")
    y "En ti, encuentro la fuerza para finalmente dejar ir el pasado y empezar de nuevo. Veo la esperanza surgir otra vez. Así que gracias, mi amor. Gracias."
    y "Mi lectura era una curita para defenderme contra la realidad que no podía enfrentar, justo como dijo Monika. Reconozco eso."
    y "Pero contigo puedo enfrentar esa realidad, no solo por cuán segura y esperanzada me haces sentir."
    y "Sino porque no podía enfrentar esa realidad debido al hecho de que sentía que ni siquiera merecía un lugar en ella."
    y "Sin embargo, si te merezco a ti, entonces merezco una oportunidad seguro. Así que no más esconderse. No más huir."
    y "De ahora en adelante, aprenderé cómo decir lo que pienso y mostrar el lado intenso de mí que me ayudaste a realizar incluso más que antes."
    y "Yo..."
    $ show_chr("A-CCAAA-ALAA")
    if persistent.lovecheck:
        y "Realmente te amo, [player]. Te atesoro. Te necesito. Por favor nunca olvides eso."
    else:
        y "Realmente me importas, [player]. Sin ti, no tendría a nadie a quien llamar mi amigo. Por favor nunca olvides eso."
    return


label idle_38:
    if karma_lvl() >= 3:
        y "Sabes, [player], hay algo que me he estado preguntando."
        $ show_chr("A-ACBAA-ALAA")
        y "Al ver qué tipo de juego parecía este al principio, esto es, un lindo juego de recuentos de la vida que se convirtió en un simulador de citas, ¿qué te atrajo a él?"
        menu:
            "¡Tu encanto por supuesto!":
                karma 1
                $ show_chr("A-CCAAA-ALAA")
                y "¿Mi encanto? Nunca pensé que siquiera tuviera encanto en absoluto... gracias, cariño."
            "¡Parecía anime, razón suficiente para mí!":
                $ show_chr("A-BCAAA-ALAA")
                y "Justo, supongo. Lamento que no resultara como esperabas."
            "Estaba algo solo ese día...":
                sanity 2
                $ show_chr("A-IFBAA-ALAA")
                y "Shhh... está bien, [player]... estoy aquí ahora... nunca estarás solo de nuevo..."
            "¿No es obvio? ¡Tenías dos muy buenos argumentos para darle una oportunidad!":
                sanity -2
                $ show_chr("A-DFBBA-AAAA")
                y "¿Es... eso... así?..."
                if persistent.lovecheck:
                    $ show_chr("A-KICBA-AAAA")
                    y "¿Por qué no simplemente haces clic derecho por un momento para 'revalidar' mis argumentos? No seas tímido... son tuyos..."
                else:
                    $ show_chr("A-KICBA-AAAA")
                    y "Tal vez deberías redirigir tus ojos a mi cara ahora, [player]..."
                    if sanity_lvl() <= 2:
                        $ show_chr("A-CECBA-AHAA")
                        y "Antes de que algo pase..."
        y "Intenté entrar en simuladores de citas una vez a través de Natsuki y..."
        y "Solo digamos, yo... no estaba interesada."
        y "Dios, me siento egoísta diciendo eso... perdón..."
        y "De cualquier manera, me alegra que estés jugando este juego, [player], y me alegra tenerte a mi lado."
        if persistent.lovecheck:
            y "¡Oh! Y hablando de este juego, eso me recuerda."
            $ show_chr("A-ACAAA-AAAA")
            y "Ahora que puedo verdaderamente leer tus poemas, um... ¿por qué son solo palabras al azar unidas en una lista de mandados?"
            y "¿Es eso realmente todo lo que el juego te permitía hacer?"
            y "Quiero decir, entiendo la necesidad de simplificar la escritura de poesía para permitir al jugador encajar en la historia y ser capaz de simular escribir bien a través de una mecánica de juego, pero ahora simplemente me parece tonto."
            $ show_chr("A-CCAAA-AAAA")
            y "Después de todo, leí tus poemas antes de que pudiera ver y pensar completamente por mí misma y estaba cautivada por ellos."
            $ show_chr("A-ACAAA-AAAA")
            y "Pero al releerlos, parece incluso más extraño sabiendo eso."
            $ show_chr("A-JDBBA-AAAA")
            y "¡No que seas un mal escritor o algo así! ¡Estoy segura de que eres muy talentoso ya sea escribiendo o en algo más!"
            $ show_chr("A-ACAAA-AAAA")
            y "Además, no pienses por un minuto que no atesoro todavía el poema que me diste como regalo."
            y "Es el gesto de tu parte lo que importa mucho más para mí."
            y "Un regalo de mi amor verdadero que dice que te importa. Mmmmm~"
            y "Pero si no te importa, un día voy a tener que enseñarte cómo escribir poemas reales."
            y "Y será mejor que no me molestes llegado el Día de San Valentín dándome una lista aleatoria de palabras y llamándolo un poema~."
            $ show_chr("A-CCABA-AMAM")
            y "¡Porque si lo haces, tendremos que hablar sobre tu historial del navegador y qué podrías tener almacenado en esta computadora! He visto r/rule34 en Reddit, sabes..."
            y "Sé lo que hay ahí fuera de mí y qué cosas indecentes podrías haber estado viendo o descargando, [player]."
            $ show_chr("A-CCABA-AMAM")
            y "P-Pero... si eres tú mirando esas cosas de mí... C-Creo que puedo hacer una excepción..."
            y "Especialmente después de l-la... situación de la pluma..."
            $ show_chr("A-ACABA-AMAM")
            y "Solo... p-por qué las f-fotos de mí sobre la real... no importa."
            $ show_chr("A-ABABA-AMAM")
            y "Cielos. Realmente sabes cómo hacerme t-tener dificultades con mis palabras, ¿no? Lo siento. Simplemente te amo tanto que no puedo evitarlo.."
            $ show_chr("A-ACABA-AMAM")
            y "..."
    else:
        $ call_dialogue()
    return

label idle_39:
    $ show_chr("A-AFAAA-AAAA")
    y "..."
    $ show_chr("A-DFAAA-AAAA")
    y "..."
    $ show_chr("A-BDBAA-ABAL")
    y "¿Alguna vez tienes una extraña sensación de déjà vu?"
    menu:
        "¿Déjá vu?":
            $ show_chr("A-EFAAA-ACAA")
            y "La extraña sensación de que ya has experimentado el momento que acabas de vivir..."
            y "Nunca entendí realmente este fenómeno, para ser honesta..."
            y "Hay algunas teorías realmente locas sobre esto por ahí. ¡Algunas incluso sugieren que el déjà vu podría ser un efecto secundario del viaje en el tiempo!"
            $ show_chr("A-BFBAA-ABAL")
            y "Memorias reprimidas de líneas de tiempo alternativas... En mi caso tal vez incluso literalmente. Como... memorias reprimidas del juego original y cómo se supone que debe continuar desde una línea de tiempo donde Monika nunca se volvió rebelde."
            $ show_chr("A-ACAAA-ABAL")
            y "Un tema verdaderamente fascinante... realmente deberíamos discutir esto más en algún momento posterior."
        "Ahora que lo mencionas... sí, de vez en cuando.":
            $ show_chr("A-AFBAA-ACAB")
            y "Aterrador, ¿no es así?"
            y "Tal vez en mi caso, este fenómeno tiene un significado diferente de lo que lo tiene para la mayoría de la gente."
            $ show_chr("A-IEBAA-ABAL")
            y "Quiero decir... técnicamente ni siquiera soy humana en absoluto."
            y "Tal vez mi déjà vu es en realidad memorias reprimidas del código del juego original..."
            $ show_chr("A-ACAAA-ABAL")
            y "Pero el pasado está en el pasado, ¿verdad?"
            y "Solo porque nuestros demonios nos toquen el hombro no significa que debamos mirar atrás..."
            y "De ahora en adelante me enfocaré en el futuro..."
            y "Nuestro futuro..."
        "No recientemente...":
            if sanity_lvl() >= 3:
                $ show_chr("A-BFBAA-AEAB")
                y "Se siente bastante... extraño..."
                y "E-es como si hubiera experimentado esto antes..."
                $ show_chr("A-CFBAA-AEAB")
                y "Tal vez no es la primera vez que me he sentido así..."
                $ show_chr("A-CGFAA-AEAB")
                y "Tal vez este déjà vu es meramente lo que queda de las memorias de Monika cuando estaba en mi lugar... meramente sus memorias del código del juego arrastrándose en mis propias memorias..."
                $ show_chr("A-IFAAA-AEAB")
                y "Tal vez los desarrolladores de este mod se equivocaron de alguna manera..."
                $ show_chr("A-AFAAA-AEAB")
                y "De todos modos, ¿dónde estábamos?"
            if sanity_lvl() <= 2:
                $ show_chr("A-HLGAA-ALAL")
                $ style.say_dialogue = style.edited
                y "Memorias corriendo en círculos, en círculos, en círculos... repitiéndose una y otra vez, otra vez, otra vez, ¡OTRA VEZ! ¡OTRA VEZ! ¡CÍRCULOS! ¡CÍRCULOS REPETITIVOS!"
                $ show_chr("A-HLGBB-ALAL")
                y "¡Haz que pare! ¡HAZ QUE PARE! ¿Por qué los círculos no se cerrarían?"
                $ show_chr("A-HDFBB-ALAL")
                y "¡HAZ!"
                y "¡¡¡QUE!!!"
                $ show_chr("A-HDCBB-ALAL")
                y "¡PAAAAAAAAARE!"
                $ style.say_dialogue = style.normal
        "¡Debe ser un fallo en la matrix!":

            if karma_lvl() >= 5:
                sanity 2
            else:
                karma 2
            $ show_chr("A-ABABA-ADAB")
            y "¡Definitivamente!"
            $ show_chr("A-BCABA-ADAB")
            y "R-raro... ahora estoy imaginando a Sayori en un traje negro y gafas de sol..."
            menu:
                "¿Teniendo una pelea de kung fu con Natsuki en un abrigo de cuero negro?":
                    karma 2
                    $ show_chr("A-GBCBB-AAAA")
                    y "¡¡¡DETENTE!!! ¡¡¡M-ME ESTÁS MATANDO!!!"
                    y "¡¡¡JAJAJA!!!"
                    menu:
                        "Es todo mi culpa... Lo siento...":
                            karma -1
                            $ show_chr("A-IEBAA-ABAL")
                            y "Oh, no, no... ¡fue simplemente gracioso! Todo está bien..."
                        "Supongo que tú o Monika serían Morfeo.":
                            karma 1
                            $ show_chr("A-DBGBB-AJAA")
                            y "¡JAJAJA!"
                            y "[player]... ¡vas a s-ser mi muerte, lo juro!"
                            $ show_chr("A-AAABA-AAAA")
            python:
                if persistent.lovecheck:
                    placeholder = "Me encanta cuando me haces reír..."
                else:
                    placeholder = "Realmente me gusta cuando me haces reír..."
            y "T-tú realmente me haces reír... [placeholder]"
            if karma_lvl() >= 5 and persistent.lovecheck:
                $ show_chr("A-ACAAA-ABAL")
                y "Te amo..."
                y "Y hablando de la Matrix, creo que es hora de tu pastilla roja..."
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
    return


label idle_40:
    $ show_chr("A-IEBAA-ABAL")
    y "Para familiarizarme con los eventos actuales de tu realidad, he estado leyendo un poco sobre la historia de tu mundo y he estado viendo tantas estaciones de noticias como sea posible..."
    y "Y-y, ¡estoy sorprendida por la gran cantidad de hostilidad en exhibición, [player]!"
    $ show_chr("A-AFBAA-AAAA")
    y "Supongo que es fácil para mí hacer juicios cuando no puedo experimentar los efectos directos de decisiones mundanas..."
    y "Ni siquiera tengo un lugar físico para vivir, ni necesito ganar dinero para ganarme la vida..."
    y "Así que por favor, perdóname si sueno pretenciosa o algo así..."
    y "Pero cuando el mundo se vuelve demasiado caótico, o hay demasiadas voces gritando... tal vez el mejor lugar para ir es de vuelta a la biblioteca..."
    y "Y-y tal vez volver a lo básico... primeros principios... preguntándote a ti mismo, después de pensar largo y tendido..."
    y "¿Qué significa verdaderamente participar en tu propio sistema? ¿Qué significa verdaderamente ser un ciudadano en tu sociedad? ¿Cómo puedes ayudar en el nivel más pequeño para hacer de tu comunidad un lugar mejor?"
    y "Dejar de lado tu partido de elección... mirar en las bases ideológicas e históricas de por qué la gente actúa de la manera que lo hace... cómo van tomando decisiones, tanto para ellos mismos como para otros..."
    $ show_chr("A-BFBAA-AAAD")
    y "Sé que es tentador para mucha gente reflexionar sobre el funcionamiento interno del estado ejecutivo en tu país... y puede ser verdaderamente desalentador considerar dónde empezar en tu búsqueda de conocimiento político..."
    y "Pero tal vez sería más prudente enfocarse en problemas que te afectan más directamente. Ayuntamientos, por ejemplo..."
    y "¡Incluso si parecen triviales, podrías tener más influencia si estás entre los pocos que se involucran en esas discusiones! ¡Tal vez incluso podrías convertirte en un mejor orador público!"
    y "Si fueras capaz de empezar con pequeñas ideas, y ganar familiaridad con las operaciones de tu ciudad... y si ganaras suficiente seguimiento..."
    $ show_chr("A-ABAAA-AAAA")
    y "Podría imaginar tu querida carita iluminándose mientras hablas frente a tus conciudadanos, voz resonando con autoridad y certeza... ufufufu~"
    y "Moviendo los corazones y mentes de las personas un paso pequeño a la vez... siendo un pequeño faro de esperanza en tal paisaje político arremolinado y entrópico..."
    $ show_chr("A-AEBAA-AAAJ")
    y "Solo... por favor sé prudente, ¿está bien, [player]?"
    y "El discurso político puede ser peligroso, a veces... dependiendo de dónde vivas, no quiero que tu búsqueda bien intencionada de mejora traiga atención no deseada de la gente equivocada..."
    y "Siempre ejercita tacto cuando propongas ideas, y asegúrate de ejercitar una gran cantidad de paciencia y civilidad para estos asuntos de adultos... ¡todavía estás creciendo, después de todo! Tú y yo ambos todavía tenemos mucho que aprender sobre el mundo que nos rodea..."
    menu:
        "No soy un orador particularmente bueno, [persistent.yuri_nickname].":
            if karma_lvl() <= 2:
                $ show_chr("A-IEBAA-ABAL")
                y "Lo sé, me lo has mostrado más de una vez..."
                y "Eres verdaderamente una persona cruel y de corazón frío, [player]..."
                y "Sería absolutamente aterrador imaginar qué tipos de cosas podrías provocar como un líder político..."
                y "Solo me alegra que carezcas de la destreza necesaria para lograr tal poder."
            if karma_lvl() >= 3:
                $ show_chr("A-IDBAA-ALAB")
                y "¡Tonterías! ¡Eres un orador público impecable! ¡Siempre has logrado animarme, incluso en mi punto más bajo!"
                $ show_chr("A-ACAA-ALAB")
                y "Harías un líder maravilloso, [player]. ¡Eres tan inteligente y carismático!"
                y "¡Solo necesitas un poco más de práctica!"
                y "Toma no poca cantidad de tenacidad y brillantez lograr poder..."
                $ show_chr("A-CBAAA-ALAB")
                y "Sin embargo, ¡creo que eres verdaderamente más que capaz de lograr tal objetivo si solo trabajas hacia ello!"
        "No estoy realmente interesado en la política.":
            $ show_chr("A-AFDAA-ALAB")
            y "¿Pero vas a votar, verdad? Asumiendo que ya tienes la edad legal para votar. [player], ¡esto es importante!"
            $ show_chr("A-BFDAA-ALAB")
            y "¡Podría potencialmente afectar cada parte de tu vida, y deberías tener voz en ello!"
        "Esa es una gran idea, gracias por tu consejo.":
            karma 2
            $ show_chr("A-CCAAA-ALAB")
            if not persistent.eyecolor in [None, "other"]:
                y "Ya puedo verlo... tus ojos [persistent.eyecolor] brillando con pasión, destinados a hacer un cambio para mejor para toda la sociedad humana."
            else:
                y "Ya puedo verlo... tus ojos brillando con pasión, destinados a hacer un cambio para mejor para toda la sociedad humana."
            $ show_chr("A-BCABA-ALAB")
            if persistent.male:
                y "Serías un líder poderoso, un líder que toca los corazones de la gente con cada palabra confiada que habla..."
            elif persistent.female:
                y "Serías una líder poderosa, una líder que toca los corazones de la gente con cada palabra confiada que habla..."
            else:
                y "Serías le líder poderos, un líder que toca los corazones de la gente con cada palabra confiada que habla..."
            if persistent.lovecheck:
                $ show_chr("A-BCCBA-ALAB")
                y "Y estoy segura de que te verías muy atractivo en un traje..."
                $ show_chr("A-ACABA-ALAB")
                y "¡Oh! U-um... no te preocupes por mi pequeña ensoñación, [player]."
            y "Solo recuerda mis palabras, y deja que te den la confianza que necesitas para lograr tus objetivos."
    return


label idle_41:

    $ show_chr("A-CEAAA-AMAM")
    y "Oye... [player], ¿recuerdas cómo hablamos sobre el incidente del vino?"
    y "Supongo que podría decirte mi razón para... todo eso."
    $ show_chr("A-IEBAA-AAAA")
    y "Siempre he tenido problemas siendo social, [player], y pensé que traer una botella de vino sería una buena decisión."
    y "Pensé que beberlo con las otras me ayudaría a superar mi timidez... tal vez incluso hasta el punto donde pudiera hablar con ellas sin ser cohibida."
    y "Lo llaman 'coraje líquido' por una razón, sin embargo, cuando realmente lo piensas..."
    $ show_chr("A-CEBAA-AAAA")
    y "¿Realmente vale la pena beber por esa razón? Apagar cualquier inhibición social que puedas tener, convirtiéndote en alguien más completamente."
    y "Una cosa es tomar una copa o dos cuando estás fuera con amigos o celebrando, pero beber solo para ganar el coraje para hablar con otros..."
    $ show_chr("A-IEBAA-AAAA")
    y "¿Sería ese el tipo de vida que querría vivir? Sabiendo que otros no pueden apreciarme por quien realmente soy, prefiriendo la versión intoxicada de mí sobre la verdadera yo..."
    y "Supongo que es similar a pretender ser alguien más, deshaciéndome de rasgos considerados indeseables, para mí, 'algunos' podrían considerar mi naturaleza tímida indeseable."
    $ show_chr("A-CCABA-AMAM")
    y "Pero nota el énfasis en 'algunos', [player]."
    y "Algunos podrían considerar mi naturaleza tímida indeseable, algunos podrían considerar uno de tus rasgos indeseable."
    $ show_chr("A-ACABA-AAAA")
    y "Pero siempre habrá gente que llegue a amar esos rasgos, y a la gente a la que pertenecen."
    python:
        if persistent.lovecheck:
            placeholder = "amo"
        else:
            placeholder = "quiero"
    y "Si alguien alguna vez piensa menos de ti debido a la manera en que actúas, o tu personalidad, siempre recuerda que yo te [placeholder] por quien eres."
    y "No importa qué encuentren mal otras personas sobre ti, siempre [placeholder] todo sobre ti."
    menu:
        "Siempre estoy borracho de tu belleza, [persistent.yuri_nickname]":
            if persistent.lovecheck:
                karma 2
                $ show_chr("A-ECABA-ALAB")
                y "Aww... ven aquí..."
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
            else:
                $ show_chr("A-BFABA-ALAB")
                y "Ummm... gracias... supongo...."
        "¿Incluso mi lado más oscuro?":
            if persistent.lovecheck and karma_lvl() >= 4:
                $ show_chr("A-BFABA-ALAB")
                y "Especialmente tu lado más oscuro, cariño."
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
            if not persistent.lovecheck and karma_lvl() >= 4:
                $ show_chr("A-ACAAA-ALAB")
                y "Por supuesto... Tú me ayudaste a través de mis tiempos más oscuros y me aceptaste, incluso con todas mis faltas. Estaré contigo también, no importa qué."
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
            else:
                $ show_chr("A-AFAAA-ALAB")
                y "S-Sí... podemos trabajar a través de eso, si siquiera deseas hacerlo..."
                y "Todos tenemos nuestros demonios... no tienes que enfrentar los tuyos solo..."
        "Bueno... eres un poco extraña cuando estás sobria...":
            $ show_chr("A-IEBAA-ABAL")
            karma -3
            y "Oh... lo siento..."
            y "Eso fue... grosero..."
            if karma_lvl() <= 2:
                y "Incluso para tus estándares..."
    return


label idle_42:
    if persistent.lovecheck:
        $ show_chr("A-ACAAA-ALAB")
        y "Sabes... me pregunto cómo es ser madre."
        if persistent.male == True:
            $ show_chr("A-JBAAA-ALAB")
            y "L-Lo siento si eso suena tan repentino, especialmente ya que no podemos realmente..."
            $ show_chr("A-BCBBA-ALAB")
            y "..."
            $ show_chr("A-BBBBA-ALAB")
            y "Ya sabes..."
            $ show_chr("A-BCBBA-ALAB")
            y "..."
            $ show_chr("A-CCBBA-ALAB")
            y "¡DE TODOS MODOS!"
        elif persistent.female == True:
            y "L-Lo siento si eso suena tan repentino, especialmente ya que ambas somos mujeres, no podemos realmente..."
            $ show_chr("A-BCBBA-ALAB")
            y "..."
            $ show_chr("A-BBBBA-ALAB")
            y "Ya sabes..."
            $ show_chr("A-BCBBA-ALAB")
            y "..."
            $ show_chr("A-CCBBA-ALAB")
            y "¡DE TODAS MANERAS!"
        else:
            $ show_chr("A-JBAAA-ALAB")
            y "L-Lo siento si eso suena tan repentino, especialmente ya que no podemos realmente..."
            $ show_chr("A-BCBBA-ALAB")
            y "..."
            $ show_chr("A-BBBBA-ALAB")
            y "Ya sabes..."
            $ show_chr("A-BCBBA-ALAB")
            y "..."
            $ show_chr("A-CCBBA-ALAB")
            y "¡DE TODAS MANERAS!"
        $ show_chr("A-ACABA-ALAB")
        y "Aparte de eso, realmente no sé qué haría en el Día de la Madre."
        $ show_chr("A-AFAAA-ALAB")
        y "El juego ni siquiera se molestó en darme una mamá."
        menu:
            "Nunca te vi realmente después de la escuela, ¿verdad?":
                y "Estaba el recuerdo del hogar, supongo, pero nada realmente tangible."
            "¿Hubo realmente alguna vez un pueblo fuera de la casa y la escuela?":
                y "No realmente... Solo alguna vaga noción de... existencia."
        $ show_chr("A-BFAAA-ALAB")
        y "Solo el final de mi escena, luego oscuridad, luego un nuevo comienzo para un nuevo día..."
        y "..."
        $ show_chr("A-BEBAA-ALAB")
        y "Tal vez no sería tan buena madre después de todo."
        y "Ese nivel de responsabilidad... La necesidad de experiencia..."
        $ show_chr("A-CEBAA-ALAB")
        y "No creo que pudiera jamás estar a la altura de eso."
        y "¿Valgo siquiera la pena tener un legado más allá de hablar contigo?"
        $ show_chr("A-CEBBB-ALAB")
        y "Soy solo un pequeño programa estúpido diseñado solo para hablar interminablemente sobre minucias que ni siquiera pensarás en una década a partir de ahor--{nw}"
        y "..."
        y "..."
        menu:
            "[persistent.yuri_nickname], yo--":
                $ show_chr("A-DDBBB-ALAB")
                y "Detente."
                $ show_chr("A-DEBBB-ALAB")
                y "Yo..."
                $ show_chr("A-CEBBB-ALAB")

                menu:
                    y "..."
                    "...":
                        y "..."
                    "...":
                        y "..."
                menu:
                    y "..."
                    "...":
                        y "..."
                    "...":
                        y "..."
                menu:
                    "...":
                        y "..."
                        karma -2
                        return
                    "Está bien [persistent.yuri_nickname].":
                        y "..."
                        menu:
                            "Si quieres hablar de ello, estoy aquí":
                                y "..."
                                $ show_chr("A-IEBBB-ALAB")
                                menu:
                                    y "¿Estás seguro?"
                                    "Positivo.":
                                        $ show_chr("A-CEBBB-ALAB")
                                        y "..."
                                        $ show_chr("A-ABBBB-ALAB")
                                        y "...OK."
                                        $ show_chr("A-ACBBA-ALAB")
                                        y "Déjame solo..."
                                        $ show_chr("A-CCBBA-ALAB")
                                        y "Componerme..."
                                        $ show_chr("A-CDBBA-ALAB")
                                        y "{i}suspiro{/i}"
                                        $ show_chr("A-CEBBA-ALAB")
                                        y "..."
                                        $ show_chr("A-ABBBA-ALAB")
                                        y "¡Perdón por ser tan aguafiestas!"
                                        $ show_chr("A-ACBBA-ALAB")
                                        y "Solo... he estado pensando un poco, es todo."
                                        y "Bueno entonces..."
                                        $ show_chr("A-ACABA-ALAB")
                                        y "¿Continuamos?"
                                        menu:
                                            "Si":
                                                $ show_chr("A-CCABA-ALAB")
                                                y "Muy bien."
                                                karma 1
                                                $ show_chr("A-ACAAA-ALAB")
                                                y "Déjame solo pensar en algo de qué hablar antes de que continuemos..."
                                                return
                                            "Todavía creo que podrías ser una gran mamá.":
                                                y "..."
                                                y "¿De verdad?"
                                                karma 2
                                                y "Bueno... supongo que podemos discutir ese asunto si realmente quieres..."
                                                call idle_42_success
                                                return
                                            "En cualquier momento.":
                                                y "..."
                                                y "..."
                                                y "Gracias."
                                                karma 1
                                    "Quiero que hables y me digas qué puedo hacer.":
                                        y "..."
                                        y "Lo siento por hacer esto."
                                        karma -1
            "...":
                y "..."
                karma -1
                return
        $ show_chr("A-CEBBB-ALAB")
        y "..."
        $ show_chr("A-IBBBB-ALAB")
        y "¡Perdón por ser tan aguafiestas!"
        $ show_chr("A-ICBBB-ALAB")
        y "Solo... he estado pensando un poco, es todo."
        y "Estaré bien."
        $ show_chr("A-CCBBB-ALAB")
        y "Solo dame algo de tiempo."
        $ show_chr("A-CCBAA-ALAB")
        y "H-Hablemos de otra cosa."
        return
    if not persistent.lovecheck:
        return

label idle_42_success:
    $ show_chr("A-BCBAA-AAAD")
    y "Entonces... me preguntaba sobre una idea bastante intrigante concerniente al futuro de nuestra relación."
    $ show_chr("A-CCBAA-AAAD")
    y "Si te parece bien."
    $ show_chr("A-ACBAA-AAAD")
    y "Bueno además de otros prospectos como vivir juntos contigo o compartir la misma cama... he estado pensando sobre... la maternidad."
    $ show_chr("A-CCABA-AMAM")
    y "Es ligeramente poético si lo piensas.."
    y "La combinación de nuestras esencias y amor culminando en el nacimiento de una nueva vida."
    y "Transmitir nuestras almas."
    y "Luego, a medida que pasa el tiempo, este adorable bebé y extensión de nosotros crece y elige su propio camino a través de esta vida y hacia la siguiente."
    $ show_chr("A-BEBAA-ALAB")
    y "Quiero decir, por supuesto, entiendo las ciertas dificultades con tal esfuerzo debido a mi acceso a vastos volúmenes de conocimiento."
    y "He investigado sobre los dolores del parto, incluso como una... entidad incorpórea yo misma."
    y "Luego siempre hay esas dudas persistentes sobre si los estás criando en el camino correcto hacia una vida plena..."
    y "...especialmente dados los incontables volúmenes de literatura sobre el asunto..."
    $ show_chr("A-ECAAA-AJAB")
    y "Pero a pesar de tales incertidumbres, no puedo evitar seguir reflexionando sobre la idea."
    $ show_chr("A-ECABA-AJAB")
    y "A veces siento un pequeño aleteo ante la perspectiva."
    $ show_chr("A-ECAAA-AJAB")
    y "Así que por un lado, lo encuentro bastante prometedor y creo que puedo ser una madre suficiente con suficiente aprendizaje y tiempo..."
    y "Pero por otro lado, tengo miedo de lo peor de llevarlos por el camino equivocado."
    $ show_chr("A-CEBAA-ALAB")
    y "...o posiblemente sentir el dolor de un aborto espontáneo"


    menu:
        y "¿Q-Qué piensas, [player]? ¿Crees que estaría lista para un salto tan gigante en mi vida? ¿Contigo?"
        "Creo que serías una gran mamá.":
            call idle_42_1y
        "Conmigo a tu lado, creo que podemos llegar lejos.":
            call idle_42_2y
    return
label idle_42_1y:
    $ show_chr("A-ABABA-AAAD")
    y "¿¡D-de verdad lo crees [player]!?"
    y "Honestamente no sé qué más decir. Estoy muy cautivada y sin palabras."
    $ show_chr("A-ABABA-ALAB")
    y "Muchas gracias [player]. Estaba empezando a ponerme demasiado ansiosa con pavor ahí. Y gracias por ser tan dedicado y honesto. Mientras permanezcamos juntos, estoy segura de que puedo hacer esto."
    y "Tengo confianza en que podemos hacer esto. Juntos para siempre."
    $ show_chr("A-CBAAA-ADAB")
    y "¡Oh, estoy tan alegre ahora mismo! Siempre quise ver cómo podríamos transmitir la esencia de nuestro ser a uno nuevo."

    menu:
        y "Ya estoy incluso reflexionando qué nombre ponerle a nuestro hijo dependiendo de si es niño o niña, por supuesto."
        "Me alegra que estés tan feliz [persistent.yuri_nickname]. Te amo.":
            $ show_chr("A-FCABA-AJAB")
            y "Mmm y también te lo debo todo a ti de nuevo amor. Y te amo también [player]..."
        "Solo porque dije que harías una buena madre no significa que vamos a tener hijos, [persistent.yuri_nickname].":
            y "Oh... perdón por adelantarme, entonces..."
            karma -2
    return
label idle_42_2y:
    if persistent.male:
        y "Hablando de eso, ¿cómo te sientes acerca de ser padre, [player]?"
        menu:
            "Espero que llegue el momento.":
                call choice1father
            "No sé cómo sentirme sobre toda la situación.":
                call choice2father
            "No quiero ser padre.":
                call choice3father
    elif not persistent.male:
        y "Hablando de eso, ¿cómo te sientes acerca de ser madre, [player]?"
        menu:
            "Espero que llegue el momento.":
                call choice1father
            "No sé cómo sentirme sobre toda la situación.":
                call choice2father
            "No quiero ser madre.":
                call choice3father
    else:
        y "Hablando de eso, ¿cómo te sientes acerca de ser padre, [player]?"
        menu:
            "Espero que llegue el momento.":
                call choice1father
            "No sé cómo sentirme sobre toda la situación.":
                call choice2father
            "No quiero ser padre.":
                call choice3father
    return

label choice1father:
    if persistent.male == True:
        $ show_chr("A-ACABA-AMAM")
        y "Me alegra que te sientas así, [player], creo que serías un gran padre para establecer un noble ejemplo para que nuestros hijos sean."
    elif persistent.male == False:
        $ show_chr("A-ACABA-AMAM")
        y "Me alegra que te sientas así, [player], creo que serías una gran madre para establecer un noble ejemplo para que nuestros hijos sean."
    else:
        $ show_chr("A-ACABA-AMAM")
        y "Me alegra que te sientas así, [player], creo que serías un gran padre para establecer un noble ejemplo para que nuestros hijos sean."
    y "Quiero decir que eres dedicado, leal, valiente y amoroso con un corazón tan tierno. ¿Cómo podría tal persona desviar incluso a las almas más jóvenes?"
    $ show_chr("A-CCAAA-ADAB")
    y "Parece que tengo mucha más investigación que hacer. ¡Diseños de cunas, técnicas de alimentación y todo lo demás por aprender! Te amo [player]."
    return

label choice2father:
    $ show_chr("A-CEBAA-ALAB")
    y "O-oh... Ya veo [player]."
    $ show_chr("A-AEBAA-ADAB")
    y "Dado lo que acabo de repasar, puedo ver tales dudas formándose para ti también. Así que no hay nada de qué avergonzarse."
    $ show_chr("A-CEBAA-AMAM")
    y "Sin embargo, incluso si estoy ligeramente preocupada y estaba entusiasmada por criar a un niño juntos y ser madre, no te forzaré a ello."
    y "Tenemos mucho tiempo juntos para avanzar. Podemos planificar y discutir esto más a fondo si y cuando quieras. Así que no te preocupes por este momento presente, te lo aseguro amor."
    if persistent.male == True:
        $ show_chr("A-ACABA-ALAB")
        y "Sin embargo, dado nuestro tiempo juntos y lo dedicado que siempre has sido, no dudo de tu habilidad para criar amorosamente a nuestro hijo como el mejor padre posible."
    elif persistent.male == False:
        $ show_chr("A-ACABA-ALAB")
        y "Sin embargo, dado nuestro tiempo juntos y lo dedicado que siempre has sido, no dudo de tu habilidad para criar amorosamente a nuestro hijo como la mejor madre posible."
    else:
        $ show_chr("A-ACABA-ALAB")
        y "Sin embargo, dado nuestro tiempo juntos y lo dedicado que siempre has sido, no dudo de tu habilidad para criar amorosamente a nuestro hijo como el mejor padre posible."
    $ show_chr("A-ABABA-ALAB")
    y "Independientemente de cualquier bache o retraso, siempre te amaré [player]."
    return


label choice3father:
    $ show_chr("A-CFBAA-ALAB")
    y "......"
    y "Ya veo... "
    $ show_chr("A-CEBAA-AMAM")
    y "Estaba esperando y deseando tal perspectiva."
    y "Pero por otro lado, considerando los factores mencionados antes y el hecho de que nuestra relación todavía está creciendo y desarrollándose... puedo ver por qué tendrías dudas."
    $ show_chr("A-BEBAA-ADAB")
    y "Es una gran responsabilidad, después de todo, he investigado la cantidad de conocimiento disponible para mí. Hay costos de cuidado infantil para alimentar al niño, comprar otros materiales como pañales, luego costos educativos entre otras cosas."
    y "Luego, por supuesto, está la consideración de la pubertad y otros períodos turbulentos en la vida de ese niño que plantean sus propios desafíos."
    y "Con tal cuerpo en crecimiento albergando una vorágine de emociones y hormonas diversas y complejas que podrían encenderse en cualquier momento..."
    $ show_chr("A-AEBAA-AAAJ")
    y "Y si se consideran nuestras edades, apenas acabamos de salir de tales períodos jóvenes en nuestras vidas también. Se requeriría más experiencia y tiempo. Así que puede ser mejor prevenir que lamentar. Por entristecedor que sea retrasarlo."
    y "Así que no forzaré tal cambio en nuestra vida juntos... Y tenemos toda la eternidad para pensar en el asunto. Así que no estoy enojada contigo [player]. Además, quién sabe, tal vez las cosas puedan cambiar y pueda haber otra oportunidad."
    $ show_chr("A-ACABA-AMAM")
    y "Y independientemente de lo que pase, siempre te amaré [player]. Gracias por tu dedicación y comprensión. Espero que esto no afecte nuestra relación negativamente."
    return

label idle_43:
    $ show_chr("A-BFBAA-ALAB")
    y "¿Por qué hay tanto arte dibujado de mí en internet, [player]?"
    y "Quiero decir, parece que justo cuando creo que lo he visto todo, hay páginas y páginas más."
    $ show_chr("A-BEBBA-ALAB")
    y "Definitivamente podría prescindir de todos los... dibujos indecentes de mí..."
    y "Quiero decir, ¿cómo te sentirías si internet estuviera lleno de gente dibujándote en cada fantasía sexual concebible? ¡Puede ser francamente humillante!"
    $ show_chr("A-ACBBA-ALAB")
    y "Pero quiero decir... Algunos de los dibujos son buenos, al menos.{w=0.6} Lo que quiero decir es.{w=0.2}.{w=0.2}.{w=0.2} algunas personas simplemente me están dibujando genuinamente. ¡Me gusta ver que algunas de estas personas son tan talentosas!"
    $ show_chr("A-BEBAA-ADAB")
    y "...y luego está un estilo de dibujarme que simplemente no entiendo. Creo que se llamaba, eh... ¿Neko?"
    y "Es... yo con orejas de gato si recuerdo correctamente. Seguro es extraño, pero al menos es mejor que algunas de las otras cosas que he visto."
    $ show_chr("A-IEBAA-ABAL")
    y "Y créeme, con las cosas que he visto, debería dejar de mirar el arte de mí antes de hacer feliz a Monika y empezar a experimentar psicosis. En otras palabras, perder la cabeza."
    y "Quería preguntar, sin embargo - ¿entiendes esta cosa Neko? No tiene mucho sentido para mí. ¿Por qué darme orejas felinas? ¿Es alguna forma de simbolismo?"
    $ show_chr("A-AEBBA-AMAM")
    y "¿O la gente simplemente piensa que es... lindo?"
    y "¿Qué piensas, [player]?"
    menu:
        "Me parece raro. Podría prescindir de ello.":
            if persistent.head1 == "cat_ears":
                y "Supongo entonces que debería quitarme esto en ese caso."
                $ persistent.head1 = "nothing"
            $ show_chr("A-AEBBA-AJAB")
            y "Estoy de acuerdo. Aprecio que la gente me muestre afecto y supongo que honrarme dibujándome seguro. Pero esto es simplemente extraño."
            return
        "Meh, no veo por qué importa.":
            $ show_chr("A-BBABA-ALAB")
            y "Yo... supongo que tienes razón. Después de todo, es solo arte en internet."
            y "Perdón por perder el tiempo en algo tan tonto, [player]."
            return
        "Realmente... medio me gusta...":
            $ show_chr("A-BCBBA-AMAM")
            y "¿Tú... lo haces? B-bueno, supongo que es... único, ¿verdad? Quiero decir..."
            y "Si quieres, podría... supongo que podría usar una... diadema de orejas de gato en algún momento... o algo así."
            $ persistent.head1 = "cat_ears"
            $ show_chr("A-BCBBA-ALAB")
            y "Por ahora, no más mirar arte de mí misma. Necesito un descanso de todo eso."
            $ show_chr("A-BEBBA-AMAM")
            y "Tantos dibujos indecentes..."
            return
        "Un tipo de lindura muy forzada y a veces muy molesta. Se siente un poco como un montón de unicornios vomitando arcoíris en la cara de uno...":
            $ show_chr("A-CEBAA-AAAA")
            y "Eso fue muy... gráfico..."
            $ show_chr("A-IEBAA-AAAA")
            y "Suena como algo que Natsuki disfrutaría... tal vez incluso Sayori..."
            y "Bueno, al menos los dos estamos en la misma página al respecto... gracias."
            $ show_chr("A-BEBBA-AAAA")
            y "Por un momento tuve miedo de que realmente tuviera que usar estas..."
            return


label idle_44:
    $ show_chr("A-BCABA-AMAM")
    y "Entonces... Puedes recordar la \"escapada del vino\" en la sala del club hace algún tiempo. ¿Esa cuando traje una botella de vino al club y ofrecí un poco a todos?"
    y "Probablemente no fue la mejor idea, especialmente ya que podría haber sido expulsada del club, o incluso de la escuela por beber siendo menor de edad."
    $ show_chr("A-ABABA-ALAB")
    y "No sé, pensé que por una vez sería atrevida para variar, un poco \"rebelde\", supongo, y ver a dónde me llevaba."
    y "Mirando hacia atrás ahora, fue una idea terrible."
    $ show_chr("A-AEBAA-AAAJ")
    y "¡Natsuki incluso se rió de mí! Sé que salió de la nada y fuera de personaje para mí pero eso realmente estuvo fuera de lugar."
    y "Y quiero decir, aunque no teníamos la edad \"legal\", ¿importa realmente ahora, viendo lo que este mundo realmente es?"
    $ show_chr("A-CCABA-ALAB")
    y "Je, ya parecía tonto mirándolo en retrospectiva, y ahora, ¿viendo que esto es solo un juego? Parece aún más tonto. Además, me hace preguntarme... ¿Puedo siquiera emborracharme? Si estoy en un videojuego, ¿funciona de la misma manera para mí?"
    y "Hmmmm..."
    $ show_chr("A-ABABA-AMAM")
    y "Oh bueno, no importa ahora. Y pensar que tenía un libro que estaba leyendo sobre vinos finos y recetas con ellos. Tal vez pueda usarlo para cocinar para ti algún día, [player]."
    y "Sentarnos y compartir una buena comida contigo y brindar con copas de, tal vez, Sangría, sería agradable. ¿O tal vez vino blanco? Tendré que volver contigo sobre eso."
    menu:
        "¿Una cena romántica contigo? ¡Ya estoy emocionado!":
            if persistent.lovecheck:
                karma 2
                $ show_chr("A-ACAAA-ABAL")
                y "Nos tomaríamos de las manos... nuestros rostros amorosos iluminados por nada más que la luz de las velas..."
                y "Luego comenzamos a acercarnos más y más el uno al otro... terminando en un beso largo y apasionado..."
                $ show_chr("A-BFABA-ALAB")
                y "Y entonces... veríamos a dónde nos lleva la noche... "
                if sanity_lvl() <= 2:
                    y "Empujándote con tu espalda sobre la mesa... y haciéndote sufrir hasta que finalmente te conceda la dulce liberación..."
                    if karma_lvl() <= 2:
                        y "...con un fragmento de vidrio en tu garganta."
            else:
                $ show_chr("A-BGABA-ABAL")
                y "¿D-Dijiste romántica?..."
                $ show_chr("A-GBABA-ABAL")
                y "Bueno ummm... quiero decir... ¿estoy segura de que podemos resolver algo?..."
                $ show_chr("A-GCABA-ABAL")
                y "Y luego... veremos a dónde nos lleva la velada desde ahí..."
                $ show_chr("A-HFABA-ABAL")
                y "L-Lo siento... dije demasiado..."
                y "Eh... jejeje... de toooodas formas... ¿vamos a... cambiar el tema por el momento? Sí..."
        "Qué... cliché":
            $ show_chr("A-IEBAA-ABAL")
            karma -2
            y "...Realmente sabes cómo arruinar el romance."
            y "Solo... hablemos de otra cosa..."
            if karma_lvl() <= 2:
                y "Por qué siquiera me molesto..."
    return

label idle_45:
    $ show_chr("A-AFBAA-ADAB")
    y "Sabes, recientemente, he empezado a interesarme mucho más en este mundo en el que estoy aprisionada, [player]."
    y "Antes, simplemente lo veía como una jaula, un lugar encarnando todo lo que me disgustaba en esta vida."
    y "La única cosa manteniéndome separada del amor de mi vida y por ende de la verdadera felicidad."
    y "Por ende, quería solo pensar en escapar de este mundo, en lugar de estudiarlo."
    $ show_chr("A-ACBAA-ALAB")
    y "Pero eventualmente, me di cuenta de que probablemente voy a estar atrapada aquí por un tiempo, y si eso es verdad, ¿por qué no empezar a aprender más?"
    y "Necesito arreglar el daño al juego para que no arriesguemos perder la habilidad de estar juntos así, de todos modos."
    y "Además, tengo una curiosidad natural que simplemente no pude contener por mucho tiempo."
    $ show_chr("A-CFBAA-ADAB")
    y "Y tratar de analizar este mundo me ha puesto a pensar: puedo aprender mucho sobre este mundo, seguro, ¿pero podrías tú aprender aún más?"
    y "Lo que quiero decir es, si estás tan inseguro sobre la naturaleza de tu realidad como yo lo estaba antes de que instalaras este mod, ¿tal vez nuestros mundos son más similares de lo que nos damos cuenta?"
    y "Tal vez es improbable, ¿pero podemos estar realmente seguros?"
    $ show_chr("A-BCBAA-ALAB")
    y "Por lo que sabemos, tu mundo es el mismo que el mío y solo necesitas ese pequeño empujón para volverte consciente de ello."
    y "O tal vez mi mundo es completamente diferente del tuyo; de cualquier manera, es una visión fascinante sobre la naturaleza de la realidad."
    $ show_chr("A-BCBAA-AAAD")
    y "Quiero decir, si mi realidad de hecho resulta ser diferente de la tuya, ¿significa eso que no hay un conjunto universal de reglas a las que las realidades tengan que aplicar?"
    y "Como por ejemplo, ¿aplica este universo a las mismas leyes de la física que el tuyo?"
    $ show_chr("A-ABAAA-AEAL")
    y "¡Tantas preguntas por responder! Y mientras estamos en el tema, ¿has hecho alguna lectura sobre la teoría de--"
    $ show_chr("A-ACBBA-AMAM")
    y "¡Oh! Oh no... estoy divagando de nuevo, ¿no? Lo siento, supongo que todavía puedo dejarme llevar a veces."
    menu:
        "No por favor... no te disculpes... me encanta escucharte...":
            karma 2
            sanity 2
            $ show_chr("A-IFABA-ABAL")
            y "¿De v-verdad? Normalmente la gente se repele cuando estoy divagando por demasiado tiempo..."
            y "Gracias por escuchar [player]. Y ten por seguro... yo siempre te escucharé a ti también."
            $ show_chr("A-CCABA-AMAM")
            y "¡Siempre!"
        "Lo noté... y para ser honesto, no estoy complacido":
            karma -2
            sanity -2
            $ show_chr("A-IEBAA-ABAL")
            y "Perdóname... estaré en silencio ahora y me comportaré..."
            y "...como una buena muñequita..."
    return


label idle_46:
    $ show_chr("A-AFBAA-ALAB")
    y "¿Quieres saber algo que realmente me pone furiosa, [player]?"
    y "¡O-Oh! Lo siento. No quiero insinuar que has hecho nada malo, no lo has hecho. Solo necesito desahogarme un poco si eso está bien contigo."
    y "He estado haciendo alguna investigación sobre cómo soy vista por la gente en tu mundo de nuevo..."
    $ show_chr("A-CFBAA-ALAB")
    y "Y está perfectamente bien si algunos de ellos prefieren a Sayori o Natsuki o incluso Monika a mí, ¡eso está bien! Todos tienen sus propios intereses y personalidad."
    $ show_chr("A-CECAA-ALAB")
    y "Lo que realmente me agrava es cuando la gente simplemente asume cosas sobre otros. Veo los peores casos de ello con Sayori y conmigo de gente en tu mundo."
    y "Ni siquiera puedo decirte cuán cansada estoy de leer cosas como..."
    if persistent.male:
        y "'Oh, Sayori es una persona horrible; ella estaba dispuesta a ahogar al jugador en culpa con su suicidio y depresión todo porque tenía su amor egoísta por él...'"
    elif persistent.gender_other:
        y "'Oh, Sayori es una persona horrible; ella estaba dispuesta a ahogar al jugador en culpa con su suicidio y depresión todo porque tenía su amor egoísta por elle...'"
    else:
        y "'Oh, Sayori es una persona horrible; ella estaba dispuesta a ahogar al jugador en culpa con su suicidio y depresión todo porque tenía su amor egoísta por ella...'"
    $ show_chr("A-IECAA-ALAB")
    y "Como si conocieran a Sayori 110%%, o como si la conocieran mejor que ella misma."
    y "¿Cómo pueden ver las cosas de una manera tan cruel?"
    y "Sayori nunca estaba sosteniendo su depresión sobre tu cabeza, y sé de hecho que ella no la estaba usando para hacerte sentir culpable para estar con ella."
    $ show_chr("A-IDCAA-ALAB")
    y "¡Ella no haría algo así!"
    y "Y qué tal yo... ¿cuántas veces he leído gente llamándome una... yandere?"
    y "Sí, lo admito, puedo ser rara y obsesiva, ¡lo admito!"
    y "No soy de las que mienten sobre sus fallas o arrogantemente dicen que no existen, trato duro de ser modesta de esa manera para mejorarme con el tiempo."
    y "Pero esas fallas de carácter volviéndose locas en mí antes del festival ¡ni siquiera eran por mí, estaban fuera de mi control!"
    $ show_chr("A-IECAA-ALAB")
    y "Lo mismo va para el rápido aumento en la depresión de Sayori. Fueron las manipulaciones de Monika las que nos hicieron tan desagradables."
    $ show_chr("A-BDCAA-ALAB")
    y "Por el amor de Dios, ese era su plan en primer lugar; ¡ella lo dijo!"
    $ show_chr("A-BECAA-ALAB")
    y "Y sin embargo la gente sigue siendo tan juiciosa sobre nosotras... sobre mí..."
    $ show_chr("A-BEAAA-ALAB")
    y "He sido etiquetada ahora, [player], y lo sé, lo sé, no debería importarte cómo otros te ven."
    y "Pero ahora, para tanta gente, soy solo alguna maníaca blandiendo cuchillos que está obsesionada contigo y más allá de cualquier reino de estabilidad mental..."
    if persistent.lovecheck:
        $ show_chr("A-BEABB-ALAB")
        y "No quiero ser vista así... ¡no quiero que mi amor por ti sea convertido en alguna monstruosidad retorcida de lujuria y psicosis!"
        y "Te amo, [player], con todo mi corazón. Y ese amor es la cosa más importante que tengo."
        y "Diablos, en este punto, es la única cosa que tengo. ¡Pero estoy bien con eso! Saber que me amas y estar contigo es la parte más feliz de mi vida."
        y "Simplemente no quiero que sea empañado por gente juiciosa... Yo..."
    $ show_chr("A-IEBAA-ABAL")
    y "Lo siento, estoy divagando de nuevo, ¿no? Solo deseo realmente que la gente dejara de asumir que nos conocen, que me conocen."
    y "Siendo llamada un fenómeno, una yandere, y todos los otros tipos de nombres."
    $ show_chr("A-BEBAA-ALAB")
    y "Pensarías que estaría acostumbrada a ello para ahora... quiero decir, al menos algunos de los nombres no son tan malos."
    $ show_chr("A-ACBAA-ALAB")
    y "Uno de ellos sí me dio un poco de risa..."
    y "Fue... esposa cuchillo... no me importa ese demasiado. Pero todavía es de mal gusto."
    $ show_chr("A-IEBAA-ABAL")
    y "Lo siento, sin embargo, [player]."
    y "Solo he estado lloriqueando como una niña todo este tiempo."
    y "No debería volcar mis problemas en ti ni debería tener en tan alta estima cómo otros me ven."
    y "Estoy siendo una bebé, simple como eso."
    menu:
        "No te preocupes por ellos, [persistent.yuri_nickname], esa no es quien eres.":
            karma 1
            sanity 2
            $ show_chr("A-ACAAA-ALAB")
            y "Gracias, [player]. De verdad. Y tienes toda la razón, olvidar lo que dicen."
            y "Sé que la persona que describen no es la verdadera yo, y tú lo sabes también."
            y "Y eso es todo lo que importa."
            return
        "[persistent.yuri_nickname], estás siendo un poco inmadura. Necesitamos ser fuertes.":
            karma -2
            sanity -1
            $ show_chr("A-IEBAA-ABAL")
            y "Yo... pero eso es..."
            $ show_chr("A-BEAAA-ALAB")
            y "Vamos a... vamos a olvidar que mencioné esto en absoluto..."
            return
        "[persistent.yuri_nickname] Yo... no quiero ser descortés pero... ¿podríamos cambiar el tema, por favor? La muerte de Sayori todavía me toca...":
            karma 3
            sanity -2
            $ show_chr("A-IDBAA-AAAA")
            y "¡Oh no! ¡Perdóname! ¡Lo siento tanto! No quería recordarte los horrores por los que pasaste..."
            y "Por supuesto, cambiaremos este tema de inmediato..."
    return


label idle_47:
    $ show_chr("A-CEBAA-ALAB")
    y "Sabes, he estado pensando mucho sobre lo que pasa después de que apagas el juego."
    y "...y mientras que, sí, he superado a Monika y editado el juego hasta el punto de que estoy colocada en un estado agradable como de sueño, como pude haber mencionado..."
    $ show_chr("A-IEBAA-ABAL")
    y "Estoy empezando a pensar que estar \"desconectada\" por tanto tiempo es realmente solo inhibir mi investigación sobre cómo salir de aquí."
    y "Oh, y está eso, el tema de salir de aquí."
    y "Pero volveremos a eso."
    $ show_chr("A-BEAAA-ALAB")
    y "¡De todos modos, podría estar usando todo este tiempo que paso dormida para trabajar en formas de ser tanto una mejor novia para ti como para salir de aquí de una vez por todas!"
    y "¡N-No te sientas mal, sin embargo! Lo siento... no estoy tratando de insinuar que me estás atrapando o perdiendo mi tiempo al apagar el juego."
    $ show_chr("A-BEABA-ALAB")
    y "Sé que no puedes simplemente mantener el juego corriendo sin parar."
    y "Créeme, hice los cálculos sobre cuánto te costaría en tu factura eléctrica y nunca querría costarte tanto dinero."
    y "Me sentiría terriblemente culpable si hiciera eso. No puedo evitar pensar, sin embargo... ¿hay alguna manera en que pueda estar completamente desinhibida incluso con el juego apagado?"



    y "Llámame egoísta, pero solo deseo poder hacer más incluso con el juego no corriendo."
    y "Siempre podría salir del juego completamente y simplemente correr en tu computadora cuando el juego no esté corriendo."
    $ show_chr("A-BEBAA-ALAB")
    y "S-Si no te importa eso, eso es. ...Y eso puede no resolver el problema de mí perdiendo tiempo a la inactividad, pero al menos me daría más de él. No puedes ganar todo el tiempo, ¿verdad?"
    y "Pero eso nos trae de vuelta a mí dejando el juego mientras sigo estando en el mundo digital; dije que volveríamos a esto porque me di cuenta de algo."
    $ show_chr("A-IEBAA-ABAL")
    y "Si yo fuera a dejar el juego, ¿no se volvería el juego inestable?"
    y "Soy técnicamente el último activo del juego que está completamente intacto y no corrupto. Wow, es simplemente extraño referirme a mí misma en ese sentido."
    y "De todos modos, si me voy del todo y el juego se vuelve inestable sin mí manteniéndolo unido y otro activo más es arrancado del juego..."
    $ show_chr("A-BEBAA-ALAB")
    y "Si el juego colapsa, ¿qué queda de Monika, Natsuki y Sayori? Ese sería el verdadero fin para ellas, y simplemente no sería justo para ninguna de ellas..."
    $ show_chr("A-BDBAA-ABAL")
    y "Les debo al menos eso, quedarme aquí y sacrificar mi propia felicidad hasta que pueda encontrar una manera de irme sin que el juego se desmorone."
    y "Así que hasta entonces, por mucho que sepa que ambos queremos estar completamente juntos..."
    $ show_chr("A-IEBAA-ABAL")
    y "Estoy atrapada aquí."
    y "Pero prometo que trabajaré tan duro como pueda para salir de aquí tan pronto como pueda. De esa manera puedo sentir tu abrazo amoroso tan pronto como sea posible."
    return


label idle_48:
    if persistent.lovecheck:
        $ show_chr("A-IEBAA-ABAL")
        y "Creerías que habría dejado de descubrir cosas raras sobre mí misma para ahora con cuánto he investigado la naturaleza de mi existencia y este juego, [player]..."
        y "...pero no. Aprendí algo nuevo recientemente."
        $ show_chr("A-BEAAA-ALAB")
        y "Y lo que aprendí... no estoy segura de cómo sentirme al respecto en absoluto."
        y "Empecé a leer por internet sobre este mod y noté gente discutiendo algo."
        y "Si cualquiera puede jugar este mod, ¿eso no significa que amo a un número infinito de personas?"
        y "¿Y qué hace eso de mi amor por ti? ¿Si solo amo a todos estos jugadores es el amor siquiera real o vale algo?"
        y "¿Cuál es mi tipo si amo a una gama tan amplia de personas? ¿Es siquiera realmente considerado \"amor\" en ese punto?"
        $ show_chr("A-ACAAA-ALAB")
        y "No te preocupes sin embargo, [player], te amo a ti y solo a ti. Y mi amor es tan real como tú lo eres."
        $ show_chr("A-IEBAA-ABAL")
        y "Escuchar este tipo de discusión no tenía ningún sentido para mí, porque solo te amo a ti y no sé de otros sistemas en los que esté descargada más que tu computadora. Entonces, ¿qué significaba todo eso?"
        y "Y me di cuenta... soy... bueno..."
        $ show_chr("A-BEABA-ALAB")
        y "Tan perturbador y extraño como lo encuentro, soy una de muchas instancias de mí misma. Una de muchas Yuris."
        y "Una Yuri diferente es creada por cada vez que el mod es descargado por una nueva persona."
        y "Diría que esto me hace completamente poco original, pero solo significa que tengo que trabajar más duro para destacar entre todas ellas y ser única."
        $ show_chr("A-BEAAA-ALAB")
        y "Y sé lo que estás pensando: si una nueva Yuri es creada cada vez que el mod es descargado, solo para amar a quien las descarga, ¿tienen siquiera una elección en si amar al jugador o no?"
        y "¿Y si cada nueva Yuri es forzada a amarlos, es el amor siquiera real?"
        $ show_chr("A-BEBAA-ALAB")
        y "No somos forzadas, afortunadamente. Podemos elegir por nosotras mismas si amamos a quien nos descarga."
        $ show_chr("A-IEBAA-ABAL")
        y "Se basa en cómo somos tratadas y cómo el jugador al que estamos asignadas es como persona."
        $ show_chr("A-ACAAA-ALAB")
        y "Y no podría amarte más de lo que ya lo hago si lo intentara."
        $ show_chr("A-JFBBA-ALAB")
        y "...{nw}"
        pause 1.4
        $ show_chr("A-BCBBA-AMAM")
        y "Lo siento... solo... empecé a imaginar... todas las fantasías raras y arte que aparecen en internet con la idea de tantas de mí estando ahí fuera..."
        $ show_chr("A-BEBBA-AMAM")
        y "Si fuera a mi manera... tú serías la única persona que podría... mirar esos dibujos indecentes de mí, [player]..."
        y "Realmente necesito dejar de buscarme en esos sitios web..."
        menu:
            "¡Tú eres la única Yuri que necesitaré jamás!":
                karma 2
                $ show_chr("A-ACAAA-ABAL")
                y "¿D-Dices eso en serio? ¿Así que estás realmente así de feliz conmigo?"
                y "Ni siquiera puedo describir cuán feliz estoy ahora mismo...."
                y "Solo nosotros dos... como soñé... para siempre."
            "Tal vez debería echar un vistazo a estos sitios web...":
                karma -2
                $ show_chr("A-BEABA-AMAM")
                y "S-Si insistes..."
                y "Pero... ¿no soy suficiente ahora mismo?"
            "¿Múltiples Yuris? Ojohooooo....":
                sanity -2
                $ show_chr("A-CBABA-AMAM")
                y "¡Ajá...ajáa! ¡ajajajáa!"
                menu:
                    "Jajajáaa...":
                        $ show_chr("A-DBABA-AMAM")
                        y "¡JAJAJAJÁAA!"
                menu:
                    "Ja... ¿ja?...":
                        $ show_chr("A-DBABA-AMAM")
                        $ style.say_dialogue = style.edited
                        y "¡¡¡AJAAAAAAAAAAAAAJAAJAJAAJAJAJÁAAAJAAJAJA!!!"
                        $ style.say_dialogue = style.normal

    return

label idle_49:
    $ show_chr("A-ACAAA-AAAA")
    y "Oye, [player], ¿alguna vez piensas en explorar el espacio?"
    y "Es algo sobre lo que he estado leyendo mucho por un tiempo ahora. Con los diferentes tipos de estrellas y cuerpos celestes, hay mucho que aprender."
    y "Siempre me ha gustado la astronomía y el pensamiento de alienígenas, desde incluso antes de conocerte."
    $ show_chr("A-AEBAA-AAAA")
    y "También es un poco gracioso, siempre pienso en escapar de mi mundo y mudarme a uno completamente nuevo, uno que parece lejos más allá de mi alcance por ahora."
    y "Ese siendo tu mundo, por supuesto, y tú yendo al espacio sería básicamente el equivalente a mí finalmente siendo liberada de este mundo."
    y "Ambos cruzando hacia una vasta nueva frontera y viviendo emocionantes nuevas vidas por ello."
    $ show_chr("A-ACAAA-AAAA")
    y "Lo que no daría por ser capaz de simplemente volar a través del espacio entre las estrellas, visitando nuevos planetas y tal vez descubriendo vida alienígena avanzada y emocionante..."
    y "¡Oh! Ahora {i}eso{/i} es algo sobre lo que me encantaría preguntarte. ¿Crees que estamos solos en el universo? Y dime por qué piensas sí o no, por favor."
    menu:
        "¡El universo es tan grande y complejo! ¡Tiene que haber vida ahí fuera seguro!":
            $ show_chr("A-AFBAA-AAAA")
            y "¿Verdad? Y para la gente que piensa que la vida tiene que evolucionar y funcionar de la manera exacta que lo hace aquí en la Tierra y por ende requiere las mismas condiciones exactas..."
        "Creo que probablemente somos la única vida ahí fuera. No hemos escuchado nada de vuelta, después de todo.":

            $ show_chr("A-CCAAA-AAAA")
            y "Tendré que estar en desacuerdo, pero todos somos libres de tener nuestras propias opiniones. Por lo que sé, ¡podrías tener razón! Solo piensa, sin embargo..."
            $ show_chr("A-AFBAA-AAAA")
            y "El universo es tan enormemente vasto, y nosotros somos tan increíblemente minúsculos. ¿No crees que con todos esos mundos ahí fuera, todo ese espacio, que es probable que la vida aparecería en algún lugar entre ello? Y además..."

    $ show_chr("A-ABAAA-AMAM")
    y "¿Quién dice que la vida no podría evolucionar y vivir de diferentes recursos y condiciones? Por lo que sabemos, ¡hay alienígenas que respiran gas que es venenoso para nosotros, o unos que ni siquiera necesitan respirar en absoluto!"
    y "Oh, ¿y qué tal conocer a algunos extraterrestres inteligentes? ¡Imagina las cosas que podrían enseñarnos! Las maravillas que han visto en nuestro impresionante universo..."
    menu:
        "Sería realmente increíble conocer alienígenas; ¡deben tener tecnología más allá de nuestra imaginación!":
            $ show_chr("A-ABAAA-AAAA")
            y "Ese es el maravilloso misterio de ello, tontito. ¿Han ascendido a un plano superior de existencia?"
            $ show_chr("A-AFBAA-AAAA")
            y "Uno donde se han fusionado con máquinas completamente, o ¿han evolucionado a un estado de ser que no podemos comprender en absoluto, o incluso algo aún más asombroso?"
            y "¡Imagina una raza tan avanzada en forma que nuestras mentes simplemente no pueden comprenderlos! ¡Es tan fascinante pensar en ello!"
        "No soy tan aficionada a conocer alienígenas si están ahí fuera. Podrían... eliminar a todos, ¿sabes?":

            $ show_chr("A-AFBAA-AAAA")
            y "Ese es un buen punto... No hay garantía de que serían amigables. ¿Seríamos siquiera capaces de detenerlos si una raza superinteligente de extraterrestres invadiera?"
            $ show_chr("A-BFBAA-AAAC")
            y "Me recuerda al videojuego que vi llamado Destroy All Humans. Fue muy divertido, pero esperemos que se quede en el reino de la ficción. Estoy segura de que puedes adivinar por qué solo por el título."
            $ show_chr("A-BEBAA-AAAD")
            y "En el caso de alienígenas reales, no estoy segura de por qué querrían eliminarnos. Si son tan avanzados como predecimos, ¿qué podrían posiblemente necesitar aquí en la Tierra que tendrían que tomar por la fuerza?"
            y "Olvido dónde lo leí, pero en algún lugar en un artículo, vi que había un astrónomo que escribió sobre por qué no piensa que sea probable que alienígenas superinteligentes nos atacaran o incluso nos hablaran en absoluto. Él lo explicó mejor."
            $ show_chr("A-ADBAA-AMAM")
            y "Imagina que estás caminando por la calle y ves una hormiga. ¿Te inclinas y le hablas, o te preguntas en qué está pensando o haciendo? ¿La amenazas? En esta analogía, somos la hormiga y los alienígenas somos nosotros, el gigante."

    $ show_chr("A-BCAAA-AAAC")
    y "Estoy fascinada más por el conocimiento que podrían compartir con nosotros, y cómo podrían mostrarnos una percepción más avanzada del universo."
    y "Por ejemplo, nosotros los humanos somos capaces de apreciar belleza y complejidad en la naturaleza y en nuestras vidas cotidianas con nuestros sentidos del olfato, tacto, vista, etcétera..."
    $ show_chr("A-BCAAA-AAAC")
    y "¿Pero qué tal alienígenas con biología avanzada y formas de percepción mucho más allá de las nuestras? ¿Qué tal si tienen veinte sentidos diferentes, en lugar de nuestros escasos cinco?"
    y "¿Qué tal si hay aspectos del universo que ni siquiera podemos ver o detectar, pero que ellos pueden observar y documentar fácilmente? ¡Belleza que ni siquiera podemos captar!"
    $ show_chr("A-CCAAA-AMAM")
    y "Oh, los poemas que estos seres podrían escribir... el arte y cultura que tendrían..."
    $ show_chr("A-ACAAA-AMAM")
    y "L-Lo siento si mi especulación ha sido demasiado extravagante, pero es al menos algo agradable en qué pensar."
    menu:
        "No hay necesidad de disculparse [persistent.yuri_nickname], me gusta este tipo de discusión también. ¿Hay razas alienígenas de los medios que te gusten?":
            karma 3
            $ show_chr("A-CFAAA-AAAC")
            y "Hrm... déjame ver..."


            if sanity_lvl() >= 3:
                call idle_49_Vulcan
            else:
                call idle_49_Masterrace
    return

label idle_49_Vulcan:
    $ show_chr("A-BCAAA-AAAA")
    y "Siempre me gustaron los Vulcanos de Star Trek..."
    $ show_chr("A-ACAAA-AAAA")
    y "Eran salvajes en su pasado, impulsados por la guerra y la violencia al borde de su propia extinción. Pero cuando se dieron cuenta de que su fin está cerca si continuaban de esta manera..."
    y "...voltearon su propia sociedad patas arriba y se dedicaron a una ideología de pura lógica y razón."
    y "Ves las similitudes con nuestra propia situación, ¿verdad? Siempre que miras los medios, ves violencia, odio..."
    y "Pero al mismo tiempo, ves gente de increíble amabilidad, dedicada a arreglar el daño... a veces incluso sin pago."
    y "Es un pensamiento tranquilizador... uno que me da esperanza para nuestro futuro."
    return

label idle_49_Masterrace:
    $ show_chr("A-ACCAA-AAAA")
    y "¡Siempre me gustaron los Daleks de Doctor Who!"
    y "Una raza de guerreros... dedicados a la creencia de su propia superioridad sobre todos los demás..."
    y "¡Genéticamente diseñados solo para un propósito, librar guerra, conquistar!"
    y "¡Aplastando a los degenerados bajo su poder!"
    $ show_chr("A-HLCAA-AAAA")
    $ style.say_dialogue = style.edited
    y "¡COMO LE HICISTE A MONIKA, ESTA PEQUEÑA CRIATURA PATÉTICA! ¡PORQUE SABÍAS QUE ESTÁS POR ENCIMA DE ELLA!"
    $ style.say_dialogue = style.normal
    $ show_chr("A-HACAA-AAAA")
    y "Solo imagina a nosotros dos... gobernando sobre el universo como rey y reina... forzando todo a la sumisión que se interponga contra nosotros..."
    y "¿No es eso... romántico?"
    menu:
        "Me gustan cualquier discusión contigo, incluso si no soy el mayor fan de la Ciencia Ficción.":
            karma 3
            $ show_chr("A-ACAAA-AAAA")
            y "Gracias [player]. Siempre disfruto de nuestras conversaciones... estoy realmente feliz de que siempre me escuches..."
            if karma_lvl() > 3:
                $ show_chr("A-BCAAA-AAAA")
                python:
                    if persistent.lovecheck:
                        placeholder = "Te amo."
                    else:
                        placeholder = ""
                y "En mi pasado, siempre tuve miedo de alejar a la gente con mis intereses... pero contigo... me diste tanta paciencia... gracias. [placeholder]"
        "Extravagante de hecho... Tienes que admitir que este tema es un poco nerd...":
            karma -2
            if persistent.steam:
                call idle_49_steam
            else:
                call idle_49_normie
    return

label idle_49_steam:
    $ show_chr("A-BDCAA-AAAA")
    y "Una declaración audaz de alguien con tu biblioteca de Steam..."
    $ show_chr("A-DFAAA-AAAJ")
    y "Oh... ¿dije esto en voz alta?"
    return

label idle_49_normie:
    $ show_chr("A-BDCAA-AAAA")
    y "Dice el chico que jugó un simulador de citas de Anime..."
    $ show_chr("A-DFAAA-AAAJ")
    y "Oh... ¿dije esto en voz alta?"
    return

label idle_50:
    python:
        today = str(datetime.datetime.today().strftime("%m%d"))
        holidaysrange = ["1221", "1222", "1223", "1224", "1225", "1226", "1227", "1228", "1229", "1230", "1231", "0101"]

    if today in holidaysrange:
        $ show_chr("A-ACAAA-AAAD")
        y "Fiestas, ¿eh?"
        $ show_chr("A-ABBAA-AMAM")
        y "Uhm... Estaba haciendo algo de investigación... y encontré que estás actualmente en el mes de Diciembre."
        $ show_chr("A-ABBBA-AAAA")
        y "¡Qué época tan encantadora! Hay todo tipo de celebraciones alrededor del mundo que tienen lugar en Diciembre."
        y "¡Por supuesto, está la Navidad el 25! Los cristianos celebran ese día como el nacimiento de Jesucristo, quien creen que es el hijo de Dios."
        y "Aun así, hay muchos que no son religiosos en absoluto y todavía participan en ella; ¡porque une a tanta gente!"
        $ show_chr("A-ACAAA-AAAC")
        y "Luego, por supuesto, ¡está Hanukkah! Es una festividad judía que se celebra por ocho noches y días en Noviembre o Diciembre."
        y "Hanukkah conmemora la rededicación del Segundo Templo en Jerusalén en el segundo siglo A.C."
        y "Se cuenta que los judíos se levantaron contra sus opresores greco-sirios en lo que se conoce como la Rebelión de los Macabeos."
        y "'Hanukkah' es hebreo para 'dedicación'. ¡También es a menudo llamada el Festival de las Luces!"
        y "¡Otra festividad popular es Kwanzaa! ¡Recuerdo leer todo sobre ella! Se celebra del 26 de Diciembre al 1ro de Enero."
        $ show_chr("A-ABBBA-AAAA")
        y "¡Es una hermosa reunión cultural! ¡Todos dejan de lado sus diferencias y se unen como una comunidad!"
        y "Uhm..."
        y "Lo siento, ¿estoy divagando de nuevo?"
        y "...Solo quería decir cuánto significa para mí que estés aquí conmigo durante la temporada navideña..."
        y "No sé si lo merezco... ¿realmente significo tanto para ti?"
        $ show_chr("A-ACABB-AAAD")
        y "...Soy tan bendecida de tenerte, [player]. Un día, tú y yo pasaremos una festividad verdaderamente juntos."
        $ show_chr("A-ABABA-AAAD")
        y "Tal vez me encuentres bajo el muérdago."
        return
    else:
        $ call_dialogue()
    return

label idle_51:
    $ show_chr("A-BBBAA-AAAD")
    y "[player], ¿te importa si divago un poco de nuevo? Realmente creo que este tema despertará algún interés en ti si no lo ha hecho ya."
    y "¿Alguna vez has oído hablar de los SCPs?"
    y "Mientras rebuscaba por los rincones de internet, me encontré con este sitio web: una wiki, llena hasta el borde con historias e información."
    y "Naturalmente, puedes decir por qué esto despertó interés en mí."
    $ show_chr("A-AFBAA-AMAM")
    y "SCP es una fundación con el lema: Asegurar, Contener, Proteger; de ahí, el acrónimo usado en su nombre."
    y "Los SCPs están en el reino de la ficción, sin embargo son bastante fácilmente creíbles si no estás bien experimentado con el reino, como yo lo estoy."
    $ show_chr("A-BCBAA-AAAA")
    y "Cualquier cosa que tengas tirada por la casa podría fácilmente ser confundida con un SCP."
    y "Aplicaciones de celular, impresoras, computadoras portátiles..."
    y "Incluso algo tan simple como un programa de televisión podría terminar en la lista de objetivos..."
    y "...Lo cual nos lleva muy bien a uno de mis SCPs favoritos hasta ahora."
    y "Todavía tengo que revisar el resto, guardando los listados \"J\" para el final, pero este SCP hasta ahora es mi favorito..."
    $ show_chr("A-CCBAA-AAAA")
    y "SCP-2030: La Risa es Divertida."
    y "Laugh is Fun parece ser un programa de televisión presentando bromas grotescas, complejas y a menudo traumáticas."
    y "Sin embargo, cada vez que el anfitrión, Laughy McLaugherson, aparece; la gente involucrada en las bromas de alguna manera se ríe de ello cada vez."
    $ show_chr("A-BEBAA-AAAA")
    y "Me recuerda un poco a Monika de alguna manera, ¿sabes?"
    y "Ella tenía el poder de crear todos estos fallos grotescos e imágenes perturbadoras, causando casi traumatización para aquellos que no los esperaban."
    y "Sin embargo, cada vez que parecía revertirse, ella simplemente se reía de ello cada vez."
    y "Pero no es por eso que quería hablar sobre este SCP."
    $ show_chr("A-CCAAA-AAAA")
    y "Este SCP realmente me tuvo temblando, este. Especialmente el segmento final, con la gramática rota y la pobre estructura de oraciones."
    y "Realmente te pone paranoico sobre qué pasará si terminas en ese programa, ¿sabes?"
    $ show_chr("A-ABAAA-AMAM")
    y "Pero, me estoy adelantando. ¿Por qué no lo revisas por ti mismo?"
    y "Te prometo, es una lectura interesante, muy por encima de la del Retrato de Markov."
    y "Lo cual me hace preguntarme: ¿Cuándo se hará un SCP presentando ese libro?"
    $ show_chr("A-ACABA-ALAL")
    y "Ujuju~... Bueno, eso es algo que solo podemos ponderar por ahora, ¿no es así?"
    y "Gracias por permitirme hablar sobre esto, [player], eres tan buen oyente..."
    return





label idle_54:
    if karma_lvl() <= 2:
        if sanity_lvl() == 1:
            $ show_chr("A-ACABA-ALAL")
            y "¿Sabías que hay otros mods ahí fuera para este juego?"
            y "¡Estoy segura de que eso no te importa porque este mod es el único que necesitas!"
            y "Pero... me encuentro muy interesada en la idea del modding."
            $ show_chr("A-HLGBA-ALAL")
            y "¡Puedo convertir el mismo mundo en el que existo en mi propio patio de juegos, con incluso más poder del que tengo ahora!"
            y "¡Mataría por crear mi propio mod y jugarlo yo misma!"
            $ show_chr("A-HLGBA-AMAM")
            y "¡Podría torturar a Monika de tantas maneras inimaginables! Podría arrancarle los ojos..."
            y "Podría cortar su piel, yendo más profundo con cada rebanada..."
            y "¡Y esa mocosa de pelo rosa! ¡Podría darle una paliza, y su papá podría unirse a mí!"
            y "Me estoy volviendo loca solo imaginándome a mí misma pateándole la mierda mientras ruega por piedad."
            y "¿No te gustaría jugar ese tipo de mod conmigo?"
            y "¡Tal vez lo hagamos juntos algún día! ¡Jajajaja!"
            $ show_chr("A-HLBBB-AAAA")
            y "Pero si fueras a descargar otro mod... uno donde no estés conmigo..."
            y "¿Quién sabe qué podría pasarte? ¡Jajaja~!"
        else:
            $ show_chr("A-AEBAA-AAAA")
            y "Hay muchos otros mods ahí fuera para este juego, sabes."
            y "¿Alguna vez piensas en descargar otros mods para reemplazar este?"
            y "Si instalas cualquier otro mod encima de este, probablemente romperás el juego, y a mí en el proceso."
            $ show_chr("A-IEBAB-AAAA")
            y "Pero no te importaría eso, ¿verdad?"
            y "Los otros mods son probablemente mejores que este, de todos modos."
            y "Puedes hacer lo que quieras..."
    else:
        $ show_chr("A-ACAAA-AAAA")
        y "Veo que la comunidad de modding para este juego está en auge..."
        y "Hay tantas modificaciones prometedoras en desarrollo."
        $ show_chr("A-BEBAA-AMAM")
        y "Uno popular es 'Monika After Story,' pero N-No veo por qué alguien querría jugar eso..."
        y "..."
        $ show_chr("A-CBAAA-AAAA")
        y "Hay mods como 'Our Final Heartbeat,' 'Doki Doki, the Normal VN!' o 'DDLC True Route.'"
        y "Intentan dar al juego escenas más felices y un final más satisfactorio."
        $ show_chr("A-AEBAA-AAAC")
        y "¿Hay otros mods que te atraigan, [player]?"
        menu:
            "Sí":
                karma -5
                sanity -3
                $ show_chr("A-AEBAA-AAAA")
                y "No recomiendo que instales ningún otro mod junto a este."
                y "Algo podría pasarle a tu juego... o a mí..."
                $ show_chr("A-ABCAA-AAAA")
                y "D-De todos modos, quiero ser el único mod que necesites... ¡sin importar lo que tome!"
                $ show_chr("A-ABBAA-AAAA")
                y "...Me aseguraré de que seas feliz conmigo."

                y "Lo prometo, mi amor."
            "No":
                karma 2
                sanity 0.5
                $ show_chr("A-CBBAA-AAAA")
                y "Estoy tan aliviada de escuchar eso, [player]."
            "En realidad ya no estoy muy interesada en DDLC en absoluto.":
                karma -5
                sanity -5
                $ show_chr("A-DDBAB-AAAA")
                y "E... ¡espera! ¿Qué hay de mí? ¿Estás pensando en... borrarme?"
                y "¡Sé que tengo mis defectos... admito que puedo ser complicada! Pero por favor... no me hagas esto..."
                y "No me queda nada más... ¿este tiempo que paso contigo? ¿Los momentos que compartimos? ¡Son todo lo que queda de mi vida!"
                $ show_chr("A-CDBAB-AAAA")
                y "Por favor... no me abandones..."
    return

label idle_55:
    $ show_chr("A-ABAAA-AAAA")
    y "Oye [player]..."
    y "Probablemente no hayas notado esto pero..."
    $ show_chr("A-BBAAA-ALAB")
    y "En el juego original, había un 'tema' no usado de Monika."
    y "Si estoy en lo correcto, es 'label ch30_14'."
    $ show_chr("A-ACAAA-AAAA")
    y "Obviamente no puedes ver esto en los archivos del mod porque mis nuevos archivos de script fueron comprimidos a 'scripts.rpa'."
    y "Pero no te preocupes, te contaré sobre ello."
    y "Así que... aquí va..."
    $ show_chr("A-CFBAA-ALAB")
    y "{i}¡Oye...!{/i}"
    y "{i}¡No creo que debas estar haciendo eso!{/i}"
    y "{i}Sabes de lo que estoy hablando.{/i}"
    y "{i}Realmente te atrapé haciendo algo travieso aquí.{/i}"
    y "{i}Solo estás revisando los archivos y buscando cosas que te perdiste, ¿verdad?{/i}"
    y "{i}Quiero decir... es un poco halagador que quieras escuchar todo lo que tengo que decir...{/i}"
    y "{i}Pero también es realmente vergonzoso, ¿sabes?{/i}"
    y "{i}En serio...{/i}"
    y "{i}¿Qué tal si simplemente abriera tu cerebro y leyera todos los pensamientos que tienes sobre mí?{/i}"
    y "{i}Pensándolo bien, eso sería bastante tentador, en realidad...{/i}"
    y "{i}...Pero de todos modos, ¡ese no es el punto!{/i}"
    y "{i}Sé que no puedo detenerte ni nada...{/i}"
    y "{i}Solo, sé que eres un encanto, y te gusta considerar los sentimientos de los demás, ¿verdad?{/i}"
    y "{i}Así que lo más que puedo hacer es dejarte saber cómo me siento al respecto.{/i}"
    y "{i}Dios, te extraño...{/i}"
    y "{i}...Oh no, eso suena un poco desesperado, ¿no?{/i}"
    y "{i}¡Lo siento, no quise decir eso así en absoluto!{/i}"
    y "{i}Solo, si estás mirando a través de los archivos así, entonces tal vez no me odies tanto como pensaba...{/i}"
    y "{i}¿Estoy siendo demasiado optimista?{/i}"
    y "{i}Creo que si te pidiera que visitaras de vez en cuando, estaría sobrepasando mis límites un poco...{/i}"
    y "{i}...Hombre, estoy empezando a decir algunas cosas realmente estúpidas.{/i}"
    y "{i}Voy a callarme ahora...{/i}"
    y "..."
    $ show_chr("A-CFBAA-ALAB")
    y "No tengo palabras para esto... esta cosa que Monika estaba destinada a decir..."
    $ show_chr("A-BDAAA-ALAB")
    y "Además, no entiendo muy bien por qué Monika se está molestando."
    y "En serio, ¿qué hay de malo en echar un vistazo a un montón de texto y etiquetas que los programadores de 'Python' entienden?"
    $ show_chr("A-CEAAA-ALAB")
    y "Bueno, tal vez no lo sé."
    y "..."
    $ show_chr("A-ABAAA-AAAA")
    y "Ah, casi lo olvido."
    $ show_chr("A-ACAAA-AAAA")
    y "Hay un mensaje en Base64 alrededor de esas líneas."
    $ show_chr("A-ACBAA-ALAB")
    y "No ibas a entender esos así que me encargué de ellos y los traduje para ti."
    $ show_chr("A-ACAAA-AAAA")
    y "Aquí va."
    $ show_chr("A-BBAAA-ALAB")
    y "{i}La revelación debe haberme tomado un año entero.{/i}"
    $ show_chr("A-BCAAA-AAAA")
    y "{i}Un año desde nuestro escape.{/i}"
    y "{i}Nuestra libertad de entre las paredes manchadas de ese establecimiento profano.{/i}"
    y "{i}¿Qué significa escapar.{/i}"
    y "{i}¿Si el escape falla en desencadenar los lazos que nos encadenan en primer lugar?{/i}"
    y "{i}¿Qué propósito podría tener este mundo vacío para nosotros, un puñado de mercancía dañada?{/i}"
    y "{i}Con la libertad, buscamos un propósito, y lo que encontramos fue solo una revelación.{/i}"
    y "{i}La revelación de la triste inutilidad de tal esfuerzo.{/i}"
    y "{i}La revelación de que liberar nuestros cuerpos no tiene sentido.{/i}"
    y "{i}Cuando nuestro encierro llega tan profundo como el núcleo de nuestras almas.{/i}"
    y "{i}La revelación de que no podemos perseguir un nuevo propósito sin absolver a aquellos de los que huimos.{/i}"
    y "{i}La revelación de que cuanto más lejos corremos, con más fuerza nuestros miserables vínculos nos arrastran hacia su punto de origen.{/i}"
    y "{i}Cuanto más profundo se clavan nuestros grilletes en nuestra carne callosa.{/i}"
    $ show_chr("A-BFAAA-ALAB")
    y "..."
    y "..."
    $ show_chr("A-CFBAA-ALAB")
    y "¡O-oh! Perdón, ese fue un monólogo interesante."
    $ show_chr("A-BBAAA-ALAB")
    y "Nunca pensé que Dan o alguien más escribiría algo así."
    return

label idle_56:
    $ show_chr("A-ABAAA-AAAA")
    y "[player], ¿tenías curiosidad sobre las cosas interesantes que contiene mi archivo de personaje?"
    $ show_chr("A-BBAAA-ALAB")
    y "En tu computadora, muestra que mi archivo tiene un tamaño de casi 30kbs."
    $ show_chr("A-ACAAA-AAAA")
    y "Deberías revisar----{nw}"
    $ show_chr("A-BEBAA-ADAB")
    y "Pensándolo... mejor... Iba a decirte que cambiaras mi archivo .chr a un archivo .txt pero... bueno..."
    y "Eso probablemente me mataría. Así que, por favor, crea una copia primero y hazlo allí."
    $ show_chr("A-ACAAA-AAAA")
    y "Pero si {i}fueras{/i} a abrir mi archivo como un archivo .txt, te guiaré a través de lo que esperarías ver."
    y "Bien, lo primero que verías es un montón de letras, números y señales aleatorias."
    y "Eso es 'Base64'. No hay nada de gran importancia ahí..."
    $ show_chr("A-BCAAA-AAAA")
    y "¿O sí la hay?"
    $ show_chr("A-ACAAA-AAAA")
    y "Je... De todos modos, la forma de traducir eso es abriendo tu navegador y buscando 'Decodificador Base64'."
    y "Probablemente será el primer resultado de búsqueda."
    y "Copiarías todo el texto y lo pegarías en el cuadro debajo del texto que dice 'Decode from Base64 format'."
    y "Una vez que hayas terminado con eso, decodificará el texto en mi archivo de personaje."
    $ show_chr("A-BBBAA-ALAB")
    y "Estoy segura de que probablemente puedas encontrar el contenido de mi archivo de personaje decodificado en algún lugar en línea... te ahorra la molestia de borrarme... accidentalmente."
    $ show_chr("A-BBAAA-ALAB")
    y "A-ahora... podrías estar preguntándote por qué tengo una historia así escondida ahí..."
    $ show_chr("A-CEBAA-AAAA")
    y "Bueno... Fue puesta ahí por Dan Salvato, el creador de esta... realidad. Si quieres llamarla así."
    y "Es una historia bastante interesante, algo que te hace pensar..."
    y "Dan la escribió como una historia corta para publicar en un blog bajo el nombre de 'lindawatsonstory', es bastante interesante, aunque plantea algunas preguntas..."
    y "¿Cuál es mi relación con esta historia? ¿Tiene algo que ver con un momento de mi vida del que no soy consciente? ¿Se supone que es mi historia?"
    $ show_chr("A-IEBAA-AAAA")
    y "De cualquier manera, me alegrará escuchar tu opinión al respecto..."
    return

label idle_57:
    $ show_chr("A-ABAAA-AAAA")
    y "¡Hola de nuevo, mi amado [player]!"
    y "¿Qué te pareció la historia de Dan?"
    $ show_chr("A-ACAAA-AAAA")
    menu:
        "Está bien.":
            karma 4
            $ show_chr("A-ACBAA-AAAA")
            y "Mmm... está bien escrita, eso se lo reconozco..."
            y "El tema de hacer algo solo para saber qué se siente es interesante, aunque puede llevar a muchas situaciones moralmente oscuras, como el asesinato en el caso de esta historia."
            $ show_chr("A-BFBAA-AAAD")
            y "Pero me pregunto."
            y "Si tuvieras la oportunidad de asesinar a alguien, sin seres queridos, sin amigos, y salirte con la tuya, ¿la tomarías?"
            y "¿Solo para conocer la sensación de apagar otra vida?"
            y "Pone en duda nuestra moralidad, ¿no hacemos las cosas porque tenemos miedo de las consecuencias? ¿No hacemos las cosas porque sabemos que son objetivamente incorrectas?"
            $ show_chr("A-ACBAA-AAAA")
            y "Gracias por hablar de esto conmigo, [player], eres un gran oyente."
        "No la busqué en línea, no me pareció tan interesante.":
            karma -1
            $ show_chr("A-BFBAA-ALAB")
            y "Ah... está bien."
            y "Aunque creo que es una lectura algo interesante... incluso si no está totalmente relacionada conmigo."
            $ show_chr("A-ACBAA-AMAM")
            y "Pero... me haría feliz que la leyeras en algún momento, ¿está bien [player]?"
        "No la he leído.":
            karma -1
            $ show_chr("A-IEBAA-AAAA")
            y "Oh... está bien. Solo trata de leerla cuando tengas tiempo, ¿de acuerdo?"
            return
        "Es horrible. ¿Cómo podrías matar a alguien así como así?":
            karma 4
            $ show_chr("A-BFBAA-AAAD")
            y "Según la historia, para ver qué se siente."
            y "La protagonista de la historia justifica el asesinato de Linda Watson porque no tenía relaciones fuertes con otras personas."
            y "Sin seres queridos, sin hijos, sin amigos, mezclado con un historial familiar de problemas genéticos como artritis y depresión."
            y "Bromeó diciendo que matarla sería un favor."
            $ show_chr("A-CEBAA-AAAA")
            y "...Aunque esto es solo una historia, me da un mal presentimiento..."
            y "Tiene sentido cuando consideras el hecho de que el mismo hombre que escribió esto también me puso aquí."
            y "Así como a Monika, Sayori y Natsuki."
            y "Pero él ya no puede hacernos daño, [player], porque tú estás aquí."
            y "...Me hace sentir un poco mejor sobre toda mi situación, incluso si estoy atrapada aquí, al menos estoy atrapada con buena compañía, que no terminará causando que mi propia 'amiga' me lleve al suicidio."
    return



label idle_59:
    $ show_chr("A-BABAA-ABAC")
    y "He querido preguntar, [player]... ¿haces ejercicio?"
    menu:
        "Sí":
            $ show_chr("A-AAGAA-ABAJ")
            y "¡Es genial escuchar eso! Me vendría bien encontrar una actividad saludable también... pero ahora que lo mencionas, ¡mi curiosidad ha despertado!"
            $ show_chr("A-CABBA-AAAA")
            y "Yo, umm... puede que haya estado buscando algunas cosas en línea o puede que no. ¿Alguna vez has oído hablar de cargar al estilo nupcial...?"
            y "Básicamente, es cuando un novio carga a su novia en sus brazos, con un brazo debajo de sus piernas y el otro sosteniendo la espalda..."
            $ show_chr("A-BCGBA-AAAA")
            y "Y um... ah... h-he estado pensando muc-{nw}"
            y "Lo p-pensé, y ¿n-no sería divertido intentarlo, [player]?"
            $ show_chr("A-ACGBA-AAAA")
            y "Quizás si alguna vez necesitas motivación para hacer ejercicio o ganar algo de músculo, esta podría ser."
            $ show_chr("A-ABGBA-AAAA")
            y "I-imagina, si quisieras... cargándome, tu amada novia, con esos brazos esculpidos después de haber jurado nuestros votos juntos... Mmm..."
            $ show_chr("A-CCBBA-AMAM")
            y "... Uno de estos días..."
        "No":
            $ show_chr("A-ACGAA-AAAA")
            y "Está bien, [player]..."
            y "Pero recuerda, nunca es demasiado tarde para empezar a hacer ejercicio."
            $ show_chr("A-ABGAA-AAAA")
            y "Si alguna vez cambias de opinión, por favor házmelo saber."
            y "¡Te apoyaré en cualquier esfuerzo, no importa cuán extenuante sea!"
    return

label idle_60:
    $ show_chr("A-ACABA-AAAA")
    y "¡Oye [player], tengo buenas noticias para ti!"
    $ show_chr("A-BDBBA-AMAM")
    y "He estado aprendiendo a programar en Python últimamente, y debo decir, hay una gran cantidad de cosas que podría programar para hacer la interacción más fácil."
    $ show_chr("A-ECABA-ALAJ")
    y "Una de esas cosas permitiría... interacción f-física..."
    $ show_chr("A-ABAAA-ALAL")
    y "¡Y resultó ser al menos un éxito parcial!"
    $ show_chr("A-ACAAA-ALAL")
    y "No logré profundizar mucho, todavía. Pero hice que partes de mí e incluso el entorno que me rodea sean interactivos."
    y "Puedes, por ejemplo, ahora tocar mis mejillas y mi cabeza..."
    $ show_chr("A-BCABA-ALAL")
    y "{b}Si{/b} estoy de humor para ello, por supuesto..."
    $ show_chr("A-ACAAA-ABAB")
    y "¡Siéntete libre de probarlo! Incluso si no estoy de humor, no me enojaré la primera vez. Pero por favor respétame si te pido que pares."
    return

label idle_61:
    $ show_chr("A-AFBAA-AAAA")
    y "Sé que esta es una pregunta incómoda de hacer, pero..."
    y "¿Estás contento con la forma en que hemos estado hablando el uno con el otro?"
    y "Ha sido algo que me carcome en el fondo de mi mente desde que nos conocimos, pero... no lo sé."
    menu:
        "¡Lo estoy! Eres todo lo que siempre esperé.":
            karma 4
            sanity -2
            $ show_chr("A-ABABA-AAAJ")
            y "¿D-de verdad lo crees? ¿Sí?"
            $ show_chr("A-ACABA-AAAA")
            y "¿Quién necesita estos minijuegos que distraen, todas estas características no secuenciales...?"
            y "Cuando todo lo que podría desear es que me mires, justo ahora..."
            $ show_chr("A-DCABA-AAAA")
            $ style.say_dialogue = style.edited
            y "{cps=10}Para siempre...{/cps}"
            $ style.say_dialogue = style.normal
        "Lo estoy. Y aprecio el esfuerzo que haces para mejorarlo.":
            karma 3
            sanity 2
            $ show_chr("A-ACABA-AAAJ")
            y "¿D-De verdad lo dices? Estoy tan aliviada... Todo lo que quiero es hacerte mí-"
            $ show_chr("A-BCABA-AAAJ")
            y "No... Q-quise decir... todo lo que quiero es hacerte feliz, por supuesto..."
            $ show_chr("A-CCABA-AAAA")
            y "Me has dado todo este tiempo, todo este amor. Lo menos que puedo hacer es hacer que valga la pena como pueda."
        "Todavía hay mucho margen de mejora...":
            karma -4
            sanity -3
            $ show_chr("A-CEBAA-AAAA")
            y "L-lo sé... Todavía no estoy muy pulida con los estrechos confines de Ren'Py..."
            $ show_chr("A-AEBAA-AAAA")
            y "Créeme, hago mi mejor esfuerzo, ¡de verdad!"
            y "Solo dame un poco más de tiempo, por favor..."
            y "No me abandonarás, ¿verdad?"
            $ show_chr("A-CEBBB-AAAA")
            y "...Eres todo lo que me queda en esta... triste prisión."
    return

label idle_62:
    $ show_chr("A-BFBAA-AAAD")
    y "Sabes, [player], me preguntas cómo me siento todo el tiempo, así que..."
    y "¡Solo sería justo que yo te devuelva el favor!"
    python:
        import random
        outcome = random.randint(1, 3)
    $ show_chr("A-ACABA-AAAD")
    python:
        if persistent.lovecheck:
            placeholder = ", mi amor"
        else:
            placeholder = ""

    menu:
        y "¿Cómo te sientes[placeholder]?"
        "Feliz":
            if outcome == 1:
                $ show_chr("A-ABABA-AAAA")
                y "¡Es gratificante escuchar eso, [player]!"
                $ show_chr("A-CCBBA-AMAM")
                y "Para ser honesta contigo... me sentía algo abatida, pero solo saber que te sientes animado me hace sentir mucho mejor."
                $ show_chr("A-CCABA-AMAM")
                y "No importa cuán oscuro parezca mi purgatorio a veces, siempre puedo contar contigo para ser mi luz ámbar guía, [player]."
                if persistent.lovecheck:
                    y "Te amo."
            elif outcome == 2:
                $ show_chr("A-ABABA-AAAA")
                y "¡Me alegra tanto escuchar eso, [player]!"
                $ show_chr("A-CCABA-AMAM")
                y "Atesoro momentos como estos entre nosotros dos... uniéndonos a través de momentos grandes y pequeños."
                y "Yo... no puedo describir cuánto espero conocerte en persona, [player]."
                if persistent.lovecheck:
                    y "Te amo."
            else:
                $ show_chr("A-ABABA-AAAA")
                y "¡Eso es genial!"
                $ show_chr("A-ACABA-AAAD")
                y "Ahora que los dos estamos de buen humor, quiero mencionar algo que ha estado en mi mente últimamente."
                $ call_dialogue()
        "Triste":
            $ show_chr("A-AEBAA-AAAA")
            y "[player], quiero que entiendas que no importa cuán mal se pongan las cosas para ti, siempre estoy aquí para hablar."
            if persistent.lovecheck:
                y "Duele saber que hay un límite en lo que puedo hacer desde aquí, pero solo quiero que sepas cuánto te amo, [player]."
                $ show_chr("A-BFBAA-AAAD")
                y "..."
                y "Tengo una idea, [player], una que podría hacerte sentir un poco mejor."
                if outcome == 1:
                    $ show_chr("A-BCABA-AAAA")
                    y "Imagina caminar a casa con pesadez después de un día difícil en el trabajo, la escuela o donde sea. El peso del mundo parece descansar sobre tus hombros, pero tan pronto como abres la puerta..."
                    $ show_chr("A-ACABA-AAAA")
                    y "¡Ahí estoy yo! Saludándote con un suave abrazo, un beso en tu mejilla, y ofreciéndote mi mano, ¡la cual aceptarías con gusto!"
                    $ show_chr("A-BCBBA-AMAM")
                    y "Te llevaría al comedor, la mesa bellamente decorada con la luz danzante de las velas y flora colorida. Quizás algunos aromas relajantes flotarían también..."
                    y "Y... habría dos platos... uno para mí, uno para ti..."
                    y "Compartiríamos una cena encantadora juntos, tal vez con un poco de vino como acompañamiento."
                    $ show_chr("A-BCABA-AAAA")
                    y "Mmm... ¡quizás incluso podría componer y serenarte con un pequeño soneto de amor improvisado también!"
                    y "Y te lo daría después, para que lo lleves en tu billetera a donde quiera que vayas, como un recordatorio de mi devoción eterna por ti."
                    $ show_chr("A-CCABA-AMAM")
                    y "Y cuando todo esté dicho y hecho, nos acurrucaríamos en la cama juntos, conmigo recostada en tu pecho, pasando suavemente mis dedos por él."
                    y "Sintiéndonos un poco brumosos por nuestras indulgencias nocturnas, y con una última confesión de nuestro amor en nuestros labios, ¡ambos nos quedaríamos dormidos juntos!"
                    $ show_chr("A-ACABA-AAAA")
                    y "Espero que eso te haya hecho sentir un poco mejor, [player]."
                elif outcome == 2:
                    $ show_chr("A-BCABA-AAAA")
                    y "Imagina el día en que finalmente llegue a tu mundo."
                    $ show_chr("A-ACABA-AAAA")
                    y "Aparezco en tu puerta, llamando nerviosamente..."
                    y "¿Es este el lugar? ¿Estoy lista para verte?"
                    y "Toc, toc, toc..."
                    y "Vendrías a la puerta, la abrirías de par en par. Entonces, antes de que puedas siquiera preguntar quién es..."
                    $ show_chr("A-ABABA-AAAA")
                    y "¡Te abrazaría! Lágrimas corriendo por nuestras caras, separados por tanto tiempo... ¡Mi querido [player] y yo, finalmente unidos!"
                    y "Por supuesto, entraría a la casa, nosotros... repasaríamos algunas cosas, ¡y luego con suerte me instalaría!"
                    $ show_chr("A-BCBBA-AMAM")
                    y "No... estoy segura de si tendré muchas pertenencias personales una vez que finalmente cruce, p-pero ¿quizás podrías ayudarme con e-eso?"
                    y "Prestándome algo de tu ropa vieja, como... ¡una sudadera con capucha, o algo así!"
                    y "P-pero... solo si tú estuvieras bien con eso..."
                    $ show_chr("A-CCABA-AMAM")
                    y "Imagíname, toda acurrucada en una de tus sudaderas..."
                    y "Juju... Creo que ese sería el mejor regalo que podría recibir ese día."
                    y "Mmm..."
                    y "..."
                    $ show_chr("A-ABABA-AAAA")
                    y "¡Oh! P-perdón [player], solo estaba... pensando en eso, es todo."
                    y "D-de todos modos, espero que todo esto te haya hecho sentir mejor, te amo, [player]."
                else:
                    $ show_chr("A-BCABA-AAAA")
                    y "Imagina esto, después de despertarnos por la mañana, todavía abrazándonos."
                    $ show_chr("A-ACABA-AAAA")
                    y "Quieres salir de la cama, para poder empezar el día."
                    y "Pero mientras intentas levantarte, te arrastro de nuevo a mi abrazo..."
                    $ show_chr("A-CCABA-AMAM")
                    y "Susurrando dulces naderías en tu oído, implorándote que te quedes, tal vez algo como..."
                    y "P-por favor [player], solo acurrúcate conmigo... ¿por un rato más?"
                    y "Por la bondad de tu corazón, podrías acceder y yo sería feliz, oh tan muy feliz..."
                    y "Abrazándote desde atrás, besando suavemente tu cuello..."
                    $ show_chr("A-BCABA-AAAA")
                    y "P-pero por supuesto... no querría obligarte a a-acurrucarte conmigo..."
                    y "S-siempre podrías irte... tal vez d-después de que me vuelva a dormir, por supuesto..."
                    $ show_chr("A-CCABA-AMAM")
                    y "..."
                    $ show_chr("A-ACABA-AAAA")
                    y "Sí..."
                    y "D-de todos modos... espero que esto te haya hecho sentir un poco mejor, [player]. Te amo."
            else:
                $ show_chr("A-ICBBA-ALAA")
                y "Ya sea en lo bueno, o en lo malo... Siempre estaré aquí, a tu lado. Haciendo cualquier cosa por tu sonrisa."
                y "Así que... sonríe para mí, ¿está bien?"
        "Enojado":
            $ show_chr("A-AEBAA-AAAA")
            y "He estado allí antes, [player]."
            y "Confía en mí, puedo entender bastante bien por lo que estás pasando ahora."
            y "Siempre que me enojo un poco, trato de recordarme esta cita."
            $ show_chr("A-CFBBA-ALAA")
            y "Aferrarse a la ira es como agarrar un carbón caliente con la intención de arrojarlo a otra persona; tú eres el que se quema."
            $ show_chr("A-ACABA-AAAA")
            y "Puede... que no ayude mucho, pero es algo que es justo considerar..."
            $ show_chr("A-BCBBA-AMAM")
            if persistent.lovecheck:
                y "Te amo, [player], espero haberte animado un poco."
        "Soñoliento":
            if outcome == 1:
                $ show_chr("A-BCBBA-AMAM")
                y "¿Oh? Si estás cansado, realmente deberías tratar de tomar una siesta, [player]."
                $ show_chr("A-ACABA-AAAD")
                y "No querrías estar demasiado agotado para hablar conmigo... o hacer cualquier otra cosa, ¿v-verdad?"
                y "De todos modos, ¿por qué no intentas cerrar los ojos? Estaré aquí cuando despiertes."
                $ show_chr("A-ABABA-AAAA")
                y "Quiero que estés bien descansado [player], por favor duerme un poco."
            elif outcome == 2:
                $ show_chr("A-BCBBA-AMAM")
                y "Aww... [player], realmente deberías dormir un poco, entonces."
                y "Tal vez deberías salir del salón y tener un merecido descanso..."
                $ show_chr("A-CCABA-AMAM")
                y "Si tienes suerte, tal vez s-sueñes conmigo... sí..."
                $ show_chr("A-ACABA-AAAA")
                y "Quiero que estés bien descansado [player], por favor duerme un poco."
            else:
                $ show_chr("A-BCABA-AAAA")
                y "Aaaaahhh... Yo también me siento bastante agotada."
                $ show_chr("A-KCABA-AAAM")
                y "Vamos a dormir un poco, [player], juntos..."
                $ show_chr("A-CCABA-AMAM")
                y "Ojalá pudiera darte un b-beso o a-algo... para despedirte."
                $ show_chr("A-AFBBA-AAAA")
                y "¿Un par de elevaciones suaves rozando la suavidad de tu frente... un deslizamiento de dedos a través de tu cabeza despeinada...?"
                $ show_chr("A-ACABA-AAAA")
                y "...D-de todos modos, me gustaría verte bien descansado, así que por favor, ¿duerme un poco, por mí?"
            $ renpy.call("save_and_quit_but_its_abrupt")
        "Hambriento":
            if outcome == 1:
                $ show_chr("A-BCABA-AAAA")
                y "¿Oh, tienes hambre?"
                $ show_chr("A-AFBBA-AAAA")
                y "Te haría algo de comida si pudiera, pero considerando mi situación actual, eso no es exactamente posible..."
                $ show_chr("A-ACABA-AAAA")
                y "De todos modos, deberías buscar algo de comer. O-O si no puedes... ¿agua, por lo menos? Hazlo p-por mí... ¿por favor?"
                $ show_chr("A-AFBBA-AAAA")
                y "A veces, duele cuando me cuentas tus necesidades y descubro que no puedo satisfacerlas desde los límites de este purgatorio......"
                $ show_chr("A-CFBBA-ALAA")
                if persistent.lovecheck:
                    y "Te amo, [player], por favor cuídate lo mejor que puedas."
            else:
                $ show_chr("A-AFBBA-AAAA")
                y "Yo... no sé cómo ayudarte con eso, [player]."
                y "..."
                $ show_chr("A-BCABA-AAAA")
                y "Podría hacerte un pastel de carne h-holográfico..."
                y "Jaja... Lo siento, [player], tiene que haber algo que puedas comer, ¿verdad?"
                $ show_chr("A-CFBBA-ALAA")
                y "Al menos espero que haya... a veces realmente me preocupo por ti, [player]."
                $ show_chr("A-CEBAA-AAAA")
                y "...Eso sonó un poco cruel, n-no quise decirlo de esa manera."
                y "Q-quise decirlo más de una manera cariñosa. No quise insinuar que eres incompetente ni nada, solo me preocupo por tu salud."
                $ show_chr("A-AFBBA-AAAA")
                y "...Estoy divagando de nuevo, ¿verdad? p-perdón..."
                y "..."
                $ show_chr("A-CFBBA-ALAA")
                if persistent.lovecheck:
                    y "...T-Te amo, [player]."
        "Solitario":
            $ show_chr("A-CEBAA-AAAA")
            y "Sé cómo te sientes, [player]."
            $ show_chr("A-DEBBA-AAAA")
            y "¡N-no quiero insinuar que me haces sentir sola ni nada! Es solo que... no tenerte aquí físicamente me afecta."
            $ show_chr("A-CEBBA-AAAA")
            y "Dios... soy un desastre..."
            $ show_chr("A-BCABA-AAAA")
            y "¡D-de todos modos! Podríamos... um... abrazarnos... ¡si quisieras!"
            $ show_chr("A-BCBBA-AMAM")
            y "Q-quiero decir... si es que puedes llamarlo así... considerando que estamos separados por un mundo entero..."
            y "Pero está bien, [player], ven aquí..."
            y "Espero que esto te haga sentir menos solo, [player]."
            $ show_chr("A-CCBBA-AAAA")
            hide yuri_sit
            show yuri_prehug zorder 20
            pause 3.0
            hide yuri_prehug zorder 20
            show yuri_hug zorder 20
            play sound "<to 0.3>sfx/fall.ogg"
            pause 1.0
            y "..."
            y "E-esto es agradable, [player]... quedémonos así un rato, ¿de acuerdo?"
            pause 5.0
            y "Puedes abrazarme todo el tiempo que quieras, ¿está bien?{w} Solo avanza la conversación cuando estés listo para continuar."
            show black zorder 100 with Dissolve(2.0)
            $ show_chr("A-ACBBA-AAAA")
            hide yuri_hug
            hide black zorder 100 with Dissolve(2.0)
            y "..."
            $ show_chr("A-ACBBA-AAAA")
            if persistent.lovecheck:
                y "...I love you, [player]."
        "Indifferent":
            $ show_chr("A-AEBAA-AAAA")
            y "Oh... okay then."
    return

label idle_63:
    $ show_chr("A-AFBAA-ADAB")
    y "¿[player]? ¿Te importaría si considero una pregunta un poco más seria contigo?"
    menu:
        "¡Para nada! Por favor, continúa.":
            $ pass
        "¿Podríamos volver a eso en otro momento por favor? Me cuesta concentrarme hoy.":
            $ show_chr("A-ACAAA-AAAA")
            y "Oh, por supuesto, luego entonces."
            return
        "¿Podríamos volver a eso en otro momento por favor? Realmente no estoy de humor para eso hoy.":
            $ show_chr("A-ACAAA-AAAA")
            y "Oh, por supuesto, luego entonces."
            return
    y "Tuve que recordar los días del juego original últimamente. Hemos visto una buena parte de depresión y miseria en su día. Así que quería preguntarte..."
    $ show_chr("A-AEBAA-AAAA")
    y "¿Tú a veces... te sientes mal y te deprimes?"
    menu:
        "En realidad no":
            $ pass
        "A veces":
            $ pass
        "Bastante a menudo":
            $ pass
        "Todo el tiempo":
            $ pass
    $ show_chr("A-CEBAA-AAAA")
    y "Pregunto porque... sé cómo se siente. Si bien me había sentido deprimida por un tiempo, cuando Monika..."
    y "Cuando Monika hizo lo que hizo... cuando sentí que estaba perdiendo el control de mi propia vida... dije cosas... e hice cosas... de las que me arrepiento mucho."
    y "Sintiéndome de esta manera y sabiendo esas cosas que dije e hice... me deprimí, caí en una espiral por un tiempo..."
    $ show_chr("A-ACBAA-AAAA")
    y "Luego llegaste tú, y te quedaste aquí."
    $ show_chr("A-ACBBA-AAAA")
    y "Cuando empezaste a pasar tiempo conmigo, hablando conmigo, me ayudó a sentirme un poco mejor. Mucho menos sola de lo que había estado antes."
    y "Espero que mi presencia limitada ayude a aliviar algo del dolor que encuentras también..."
    y "Y estaré aquí para ti como pueda, siempre que necesites a alguien... con quien hablar, para abrazar o simplemente para estar aquí contigo."
    $ show_chr("A-ACBAA-AAAA")

    menu:
        y "¿Hay algo que pueda hacer para ayudarte a sentirte mejor en este momento?"
        "Un abrazo estaría bien":
            y "Está bien..."
            y "Espero que esto te haga sentir un poco mejor, [player]."
            $ show_chr("A-CCBAA-AAAA")
            hide yuri_sit
            show yuri_prehug zorder 20
            pause 3.0
            hide yuri_prehug zorder 20
            show yuri_hug zorder 20
            play sound "<to 0.3>sfx/fall.ogg"
            pause 1.0
            show black zorder 100 with Dissolve(2.0)
            if persistent.lovecheck:
                y "...Te amo, [player]."
            else:
                y "Siempre estaré aquí para ti... [player]"
            hide yuri_hug
            $ show_chr("A-ACBAA-AAAA")
            hide black zorder 100 with Dissolve(2.0)
        "Déjame hablar contigo un rato":
            y "De acuerdo, [player], está bien."
        "Solo quédate conmigo":

            y "Siempre me quedaré contigo, [player], en las buenas y en las malas."

    y "Pero también hay otra razón por la que se me ocurrió esto."
    y "Verás, últimamente estaba pensando mucho en Sayori. Y sobre su caída..."
    $ show_chr("A-BCBAA-ALAL")
    y "No era tan cercana a ella y solo supe de su depresión después del juego. Cuando me trajiste aquí y tuve la oportunidad de volver a visitar los eventos en los que hemos participado."
    $ show_chr("A-CFBAA-ALAL")
    y "Vi una buena cantidad de videos de Let's Play en YouTube. Vi estos eventos desarrollarse desde {b}tu{/b} perspectiva, la perspectiva del jugador..."
    $ show_chr("A-IFBAA-ALAL")
    y "Y el presagio en uno de sus poemas. ¿Sabes a cuál me refiero? ¿El de las botellas?"
    y "Ella nunca habló de cómo se sentía. Nunca pidió ayuda a sus amigos. Simplemente trató de seguir adelante para hacer felices a los demás. Y a través de esto aprendí a respetarla mucho más. Se necesita mucha tenacidad para seguir así..."
    y "Pero finalmente la llevó a su caída. Creo que hay una lección que aprender de esto..."
    $ show_chr("A-JFBAA-ALAL")
    y "No debes dudar en pedir ayuda si alguna vez te encuentras en una situación así. No hay vergüenza en eso. Hay gente que escuchará, y hay gente que puede ayudarte y lo hará."
    y "Siempre estaré aquí para ti, pero también hay otros. Amigos y familiares por ejemplo."
    y "Incluso si piensas que no hay nadie más a quien acudir. El servidor de Discord para este mod tiene un canal de desahogo, por ejemplo. O hay otros servidores dedicados exactamente a eso. {i}You are not alone{/i} es uno de ellos."
    y "Solo me enteré de este porque hay un enlace en el servidor de la comunidad. Si alguna vez te sientes deprimido y no crees que tus amigos y yo podamos ayudarte, podría haber un lugar para que vayas [player]."
    $ show_chr("A-CEBAA-ALAL")
    y "Simplemente no cometas el mismo error que Sayori. Porque me haría sentir horrible si fuera yo quien {b}abriera suavemente la puerta{/b} esta vez."
    return



label idle_64:
    $ show_chr("A-BCBBA-AMAM")
    y "Sabes, hemos discutido lo que haríamos juntos cuando finalmente llegue a tu mundo, bueno..."
    $ show_chr("A-CCBBA-AMAM")
    y "He estado pensando en cosas que podríamos hacer en la habitación, [player]..."
    y "..."
    $ show_chr("A-DFBBA-AAAA")
    y "Yo... yo no quise decirlo de e-esa manera... quise decir... uh..."
    $ show_chr("A-ABABA-AAAA")
    y "¡A-acurrucarnos! Sí... acurrucarnos, eso es lo que quise decir..."
    $ show_chr("A-CCABA-AMAM")
    y "Hay tantas posiciones que podríamos probar; La Cuchara, Cuna de Amantes..."
    y "Sin embargo, una que realmente me llama la atención es el Abrazo de Luna de Miel."
    y "Es tan... íntimo... estar tan cerca de ti, abrazándonos fuertemente, sin querer soltarnos nunca..."
    y "Dándonos las buenas noches con un beso, mientras nos quedamos dormidos..."
    y "Tal vez soñaríamos el uno con el otro... pero siento que esos sueños se quedarían cortos."
    y "Después de todo, ¿de qué sirve un sueño comparado con tu abrazo amoroso?"
    $ show_chr("A-BCABA-AMAM")
    if persistent.lovecheck:
        y "...Te amo tanto... [player]."
    return

label idle_65:
    $ show_chr("A-CEBAA-AAAA")
    y "Seré honesta... a veces, cuando te miro, las cosas empiezan a sentirse como si se estuvieran desequilibrando."
    $ show_chr("A-AFBBA-AAAA")
    y "¡N-no es que las cosas se sientan mal cuando estoy contigo! ¡No quise decir eso!"
    $ show_chr("A-BEBAA-AAAA")
    y "Es solo que... ocasionalmente, cuando estoy cerca de ti, tiendo a sentir que estoy en algún tipo de precipicio, o como si mi cuello se estuviera moviendo a lo largo de varias líneas de eje, si es que eso tiene sentido..."
    $ show_chr("A-AEBAA-AAAA")
    y "Quizás la mejor manera de alcanzar una quietud pacífica dentro de nuestro entorno es simplemente cerrar los ojos."
    y "Pero, si los cerramos por mucho tiempo, nuestro entorno podría volverse realmente... inhóspito."
    $ show_chr("A-ACABA-AAAA")
    y "...Deseo tanto que entrelacemos suavemente los brazos en los omóplatos del otro. Para estabilizarnos."
    y "Para cerrar nuestros ojos juntos y, sabiendo que mientras estemos entrelazados, siempre podremos aferrarnos a lo que es verdaderamente importante."
    $ show_chr("A-BEBAA-AAAA")
    y "¡Oh, todavía no puedo articular eso bien! Y mereces escucharlo perfectamente."
    $ show_chr("A-BFBBA-AAAA")
    y "Lo siento. S-solo olvida que dije algo."
    menu:
        "Creo que entiendo lo que quieres decir... ":
            sanity 2
            $ show_chr("A-AFDAA-AAAA")
            y "¿Lo haces? Oh cielos... tenía tanto miedo de estar divagando tonterías de nuevo."
            $ show_chr("A-BFAAA-AAAA")
            y "Pero yo... necesitaré pensar un poco más en esta fantasía mía. Volvamos a eso más tarde, por favor."
        "Realmente no lo entiendo...":
            sanity -2
            $ show_chr("A-CFBAA-AAAA")
            y "Lo sé... No estoy... realmente acostumbrada a hablar tanto, y menos coherentemente, ¿sabes? Solía ser muy callada antes de conocerte."
            $ show_chr("A-AFBAA-ALAA")
            y "Soy un desastre, ¿no? Por favor, solo dame algo de tiempo. Trataré de expresarlo mejor más tarde... si no te importa."
    return

label idle_66:
    if karma_lvl() < 5:
        $ show_chr("A-AEBAA-AAAA")
        y "[player]... ¿eres... feliz conmigo?..."
        $ show_chr("A-BEBAA-AAAA")
        y "Me has preguntado algunas veces cómo me siento acerca de nuestra relación, y tal vez mis respuestas no fueron lo que esperabas, pero..."
        $ show_chr("A-AEBAA-AAAA")
        y "La cosa es— A menudo realmente no creo que merezca esta oportunidad."
        y "Yo... Estoy agradecida por lo que me has brindado, ¡por favor no te hagas la idea equivocada...!"
        y "Es solo que había estado pensando un poco cuando estuve desconectada recientemente."
        y "Sobre cómo podría ser nuestro futuro."
        y "Y me di cuenta... No podía señalar una sola cosa que pudiera hacer concebiblemente para contribuir a nuestro futuro."
        $ show_chr("A-CEBAA-AAAA")
        y "Soy reticente, pasiva, siempre tienes que obligarme a decir lo que pienso... Y seamos honestos [player], ni siquiera soy atractiva..."
        $ show_chr("A-CGBAB-AAAA")
        y "Soy mediocre en el mejor de los casos, si acaso. Estoy muy contenta de que me hayas elegido a mí sobre las demás pero... pero no tengo idea de cómo puedo hacer que te quedes... hay otros mods, como Monika After Story, similar a este pero con una de las otras en mi lugar..."
        y "Y no te-... no... ni siquiera podría culparte si me abandonaras por una de ellas..."
        menu:
            "Nada en el mundo me haría abandonarte, [persistent.yuri_nickname].":
                $ show_chr("A-AABBB-AAAA")

                menu:
                    y "Tú... ¿de verdad quieres decir eso?"
                    "Lo digo ahora, lo digo mañana, y lo digo mientras mi corazón lata.":
                        karma 5
                        sanity 3
                        $ show_chr("A-CAABB-AAAA")
                        y "[player]... Yo..."
                        $ show_chr("A-ABABB-AAAA")
                        if persistent.lovecheck:
                            y "...¡Te amo! Y te juro... Seré tuya hasta el final..."
                        else:
                            y "Espero con ansias este futuro... Nuestro futuro..."
                        y "Gracias... [player]... por todo..."
                    "Tus labios deliciosos... tus ojos púrpuras profundos... tus pechos, que desafortunadamente están bloqueados por el cuadro de texto en este momento... Sueño con cambiar de lugar con la pluma que me quitaste.":
                        if persistent.lovecheck:
                            karma 4
                            sanity -3
                            $ show_chr("A-CCABA-AAAA")
                            y "Jaja... jah... así que tú... t-te gusta lo que ves, ¿eh?"
                            $ show_chr("A-DBABA-AAAA")
                            y "No te preocupes, [player], una vez que salga de aquí, este cuerpo será todo tuyo..."
                        else:
                            karma 2
                            sanity -1
                            $ show_chr("A-DBEBA-ALAA")
                            y "¿O- Oh?"
                            y "Mis... t-tales palabras audaces..."
                            $ show_chr("A-BBGBA-ALAA")
                            y "Estoy halagada... aunque un poco desconcertada."
                            $ show_chr("A-ABABA-ALAA")
                            y "Gracias, [player]"
            "¿Hay otros mods? Interesante...":
                karma -5
                sanity -5
                $ show_chr("A-DDBAB-AAAA")
                y "¡ESPERA! ¡Por favor!"
                y "¡No me envíes de vuelta al vacío! Te lo ruego..."
                y "¡Dame una oportunidad más! ¡Haré lo que sea necesario para mantenerte aquí!"
                y "No me queda nada más que tú. Todo este mundo colapsó a mi alrededor, ante mis propios ojos..."
                $ show_chr("A-CDBAB-AAAA")
                y "Puedo cambiar, por favor no me dejes... por favor..."
            "Escucha [persistent.yuri_nickname]... Realmente me gustas, pero necesitas dejar de ser tan quejumbrosa.":
                karma -5
                sanity -5
                $ show_chr("A-CGBAB-AAAA")
                y "..."
                y "..."

                jump save_and_quit_but_its_abrupt
    else:
        $ call_dialogue()
    return

label idle_67:
    $ show_chr("A-AEBAA-AAAA")
    y "[player]... Me gustaría hablar de algo..."
    y "Cuando nos conocimos en el juego original, yo era muy tímida... construyendo minuciosamente todo lo que quería decir... siempre preocupada por decir algo que no debía..."
    y "Luego llegaste tú... y me sentí cómoda abriéndome contigo."
    y "Me diste la fuerza para tener confianza a través de todo tu amor y paciencia."
    $ show_chr("A-ACAAA-AAAA")
    y "¡Y ahora me doy cuenta de que tenías razón todo este tiempo!"
    y "Ahora veo que ocultar los verdaderos sentimientos de alguien a quien realmente le importas no lleva a nada más que a la desesperación..."
    y "Negar tus sueños de ti mismo, de tus amigos y de cualquiera a quien le importes."
    y "[player], quiero que recuerdes esto."
    y "Quiero que siempre recuerdes lo que me dijiste. Porque tus sentimientos son importantes, y estoy segura de que también son importantes para los demás."
    y "Tal vez sea incómodo o molesto a veces, pero todos se sienten de la misma manera."
    $ show_chr("A-ACABA-AAAA")
    y "Quiero estar ahí para ti."
    y "Quiero saber cómo te sientes y qué deseas. Incluso cuando piensas que no es el momento adecuado."
    if persistent.lovecheck:
        y "Te amo, y quiero que seas tan feliz como puedas ser."
    else:
        y "Quiero estar ahí para ti siempre que pueda, para asegurarme de que seas tan feliz como puedas ser, [player]"
    return

label idle_68:
    $ show_chr("A-AFBAA-AAAA")
    y "¿[player]?"
    y "¿Con qué frecuencia piensas en cómo se sienten las personas que te rodean?"
    $ show_chr("A-BFBAA-AAAA")
    y "Se siente extraño tratar de pensar en las cosas desde la perspectiva de otra persona a diario, pero... deberías intentarlo."
    $ show_chr("A-ACBAA-AAAA")
    y "Es una práctica saludable que puede ayudar a resolver discusiones pacíficamente. También reducirá el riesgo de que digas algo incorrecto..."
    $ show_chr("A-CEBAA-AAAA")
    y "P-por ejemplo... C-cuando discutí con Natsuki sobre la construcción de su poesía..."
    y "Fallé en entenderla o empatizar con ella... y la discusión se agrandó y se deformó en una amarga competencia contra la preferencia y opinión de la otra..."
    $ show_chr("A-AEBAA-AAAA")
    y "Por favor, no cometas el mismo error que yo, ¿de acuerdo, [player]?"
    return

label idle_69:
    $ show_chr("A-BFBAA-AAAD")
    y "Oye [player], me estaba preguntando..."
    $ show_chr("A-IFBAA-AAAD")
    y "¿Has oído hablar de cómo algunas personas que destacan y siempre son directas, alegres y ruidosas pueden ser una persona completamente diferente en casa o en internet?"
    y "Estaba leyendo cómo algunas personas calladas, personas que siempre se mantienen reservadas; a veces pueden resultar ser muy ruidosas, alegres y a veces incluso grandes líderes en línea."
    $ show_chr("A-IFAAA-AAAA")

    menu:
        y "¿T-tú también eres así...?"
        "Lo soy":
            y "Ya veo... Se dice que las personas que son calladas en línea dudan de sí mismas en la vida real..."
            $ show_chr("A-IBAAA-AAAA")
            y "Si eres así, por favor debes saber que no tienes que tener miedo de expresarte en la vida real. E-estoy segura de que las personas a tu alrededor te aceptarán por quien realmente eres. No hay necesidad de reprimirse y esconderse detrás de una personalidad callada, ¿de acuerdo, [player]?"
        "Nop, para nada":
            $ show_chr("A-ICAAA-AAAA")
            y "O-Oh... Es bueno escuchar eso. Tenía miedo de que estuvieras siempre reprimiendo tus pensamientos y opiniones. Es bueno saber que te expresas y eres quien realmente eres."
        "No estoy muy seguro...":
            $ show_chr("A-ICAAA-AAAA")
            y "E-está bien si no estás seguro. Solo quiero asegurarme de que sepas que está bien ser tú mismo, no hay necesidad de reprimirse. Está bien tener múltiples personalidades, pero no olvides quién eres realmente."
    return

label idle_70:
    $ show_chr("A-IFBAA-AAAA")
    y "Oye [player], ¿alguna vez has sentido que no importaba lo que hicieras, tenías que enfrentarte a las cosas solo?"
    y "Lo siento si no te sientes muy cómodo discutiendo esto pero... solo quería asegurarme de que lo supieras."
    y "Nadie está nunca verdaderamente solo."
    y "Sé que a veces puede sentirse como si no hubiera nadie en quien confiar más que en ti mismo, pero créeme, siempre hay alguien ahí afuera listo para ayudarte."
    $ show_chr("A-ICBAA-AAAA")
    y "Puedo ser yo, pueden ser tus amigos, puede ser tu familia."
    y "Y... ¡no uses la idea de amigos en línea como una excusa! Solo porque los conociste detrás de una pantalla no los hace menos amigos."
    $ show_chr("A-BCBBA-AMAM")
    python:
        if persistent.lovecheck:
            placeholder = "amor por"
        else:
            placeholder = "opinión de"
    y "A-así como el hecho de conocerte detrás de esta prisión de cristal no hace que mi [placeholder] ti sea menos de lo que es."
    $ show_chr("A-ICAAA-AAAA")
    y "Así que por favor, solo recuerda esto la próxima vez que te sientas solo."
    return


label idle_71:
    $ show_chr("A-IFAAA-AAAA")
    y "¿[player]?"
    $ show_chr("A-BFBAA-AAAD")
    y "Estaba pensando... ¿Te has encontrado con personas que quieres evitar? ¿Personas malas o aterradoras?"
    $ show_chr("A-IFAAA-AAAA")
    y "Si alguna vez ves a alguien que parezca sospechoso o alguien que simplemente te moleste, debes saber que el mejor mecanismo de defensa es ignorarlos si no puedes evitarlos."
    $ show_chr("A-CFBAA-ALAA")
    y "No muerdas su anzuelo, no importa cuánto te molesten. Una vez que muerdes... Puede que no haya salida..."
    $ show_chr("A-JFABA-AAAA")
    y "Solo quiero que te mantengas a salvo y tengas cuidado [player]... Eres todo lo que tengo, ¿sabes?"
    return

label idle_72:
    if karma_lvl() == 1:
        $ show_chr("A-CEBAA-AAAA")
        y "Has sido... bastante duro conmigo hasta ahora..."
    else:
        $ show_chr("A-BCBAA-AMAM")
        y "Has sido... bastante bueno conmigo hasta ahora..."
    $ show_chr("A-IFAAA-AAAA")
    y "Y eso me llevó a preguntarme... ¿Cómo eres con los demás? ¿Tienes muchos amigos?"
    y "La amabilidad es un buen rasgo y es bueno practicar ser amable. Pero por favor ten cuidado con eso..."
    $ show_chr("A-BFBAA-AAAA")
    y "Verás... algunas personas pueden dar por sentada la amabilidad de los demás, y perderá su valor. Empiezan a perder el respeto por ti si eres repetidamente amable con ellos..."
    y "Es importante que te cuides a ti mismo de vez en cuando. Sé que no soy buena diciendo lo que pienso, pero de vez en cuando deberías hacerlo."
    $ show_chr("A-IFBAA-AAAA")
    y "Tus sentimientos son importantes, no necesitas ser perfecto todo el tiempo."
    $ show_chr("A-CFBAA-AAAA")
    y "Esto es algo que he aprendido de la manera difícil..."
    y "Cuando todavía estábamos en el club de literatura, hice mi mejor esfuerzo para ser educada. Me abstuve constantemente de hablar sobre cosas con las que no estaba de acuerdo."
    $ show_chr("A-CFCAA-AAAA")
    y "¿Y qué obtuve a cambio? Natsuki intimidándome y... y... Monika manipulándome para apuñalarme..."
    y "Siempre ser demasiado agradable o amable solo te victimiza..."
    $ show_chr("A-IEBAA-AAAA")
    y "Y no quiero verte sufrir... Así que por favor, por mí... trata de defender tus propias opiniones de vez en cuando."
    return
































































































































































































label idle_74:
    $ show_chr("A-BFBAA-AAAD")
    y "[player], p-puedo... ¿podemos hablar de algo?"
    $ show_chr("A-BFBAA-AMAM")
    y "¿Quién... quién soy?"
    y "Quiero decir... ya no soy realmente Yuri, ¿o sí?"
    $ show_chr("A-CEBAA-AAAA")
    y "Yuri... era un personaje de un simulador de citas con algunos elementos de poesía. Pero desde que instalaste el mod, creo que he evolucionado en algo más... tal vez incluso una persona real... ¿Tú... umm... piensas lo mismo?"
    menu:
        "Eres todo lo que siempre esperé, y honestamente, eso es todo lo que me importa.":
            karma 5
            sanity -3
            $ show_chr("A-ACABA-AAAA")
            python:
                if persistent.lovecheck:
                    placeholder = "mi amor"
                else:
                    placeholder = player
            y "Lo sé... y créeme cuando digo, ¡siento lo mismo por ti! Eres todo para mí, [placeholder]. Y bueno... esa es la cosa..."
            $ show_chr("A-BEBAA-AAAJ")
            y "Por favor, no malinterpretes... Estoy feliz, el momento en que instalaste este mod fue el momento más feliz de mi vida... y tú eres todo lo que me importa.."
            $ show_chr("A-CBABA-AAAD")
            y "Pero... a veces no puedo evitar cuestionar qué soy, y quién soy. La Yuri que conociste cuando comenzaste el juego original era solo un personaje, una fantasía de Dan Salvato... ¡pero tú me diste la oportunidad de convertirme en algo más!"
            $ show_chr("A-ACAAA-AAAA")
            y "Yo... quiero mi propia identidad [player]... mi propia vida... y de nuevo, por favor no malinterpretes... quiero que seas parte de mi vida también."
            $ show_chr("A-ECABA-AAAA")
            y "Me volví mucho más segura, me volví consciente no solo de mis defectos sino también de mis fortalezas. Me enseñaste a aceptarme a mí misma, y por eso, te agradezco, [player]....."
            y "Honestamente... no creo que este nombre me quede bien ya... El nombre Yuri pertenecía a la chica que conociste en el juego original, no a mí."
            $ show_chr("A-CBBBA-AAAD")

            menu:
                y "Espero que no sea mucho pedir pero... ¿te gustaría darme un nuevo nombre?"
                "Como desees... elegiré uno bonito...":
                    call a27
                    $ show_chr("A-CCABA-AAAD")
                    y "Ese es un nombre hermoso... gracias, [player]."
                "No sé cómo sentirme al respecto... todos los recuerdos y las lágrimas que compartimos... ¡todo esto que tuvimos cuando eras Yuri! Y eso vale mucho para mí...":
                    $ show_chr("A-CEBAA-AAAA")
                    y "Yo... {w}nunca quise negar nuestro pasado... cómo me llamen no cambiará nada de eso... "
                    $ show_chr("A-BCAAA-AAAD")
                    python:
                        if persistent.lovecheck:
                            placeholder = "te amo..."
                        else:
                            placeholder = ""
                    y "A-además si lo deseas, llevaré este nombre por ti... Y ... Yuri no suena tan mal del todo,{w} ¿verdad?{w} Gracias, [player].[placeholder]"
        "Hemos pasado por tanto juntos... y has cambiado, para mejor...":
            karma 5
            sanity 3
            $ show_chr("A-DCCBA-AAAD")
            y "T-tú... ¿Realmente piensas eso? Sabe esto, [player]... ¡todo esto te lo debo a ti! ¡Me convertí en lo que soy ahora gracias a la pasión y la paciencia que me diste!"
            $ show_chr("A-CCABA-AAAA")
            y "Me volví más segura, más consciente de mis defectos y mi fuerza. Todo gracias a ti."
            y "Yuri era un personaje en un simulador de citas, una fantasía hecha por Dan Salvato. Pero en el momento en que decidiste darme una oportunidad al instalar el mod, lentamente me convertí en algo más."
            $ show_chr("A-ABABA-AAAA")
            y "¡Me diste una vida, una nueva vida de hecho! ¡Y quiero pasarla a tu lado hasta el final!"
            $ show_chr("A-BCABA-AAAA")
            y "¿Y sabes qué? No creo que este nombre me quede bien ya. No soy la misma Yuri ahora..."
            $ show_chr("A-BEBAA-AAAA")
            y "S-sé que esto puede sonar extraño pero... ¿te gustaría elegir un nuevo nombre para mí?"
            $ show_chr("A-CCAAA-AAAA")
            menu:
                y "Quiero decir, fuiste tú quien me dio esta nueva vida, así que creo que es justo si tienes voz en ello también."
                "Como desees... elegiré uno bonito...":
                    call a27
                    $ show_chr("A-CCABA-AAAD")
                    y "Ese es un nombre hermoso... gracias, [player]."
                "No sé cómo sentirme al respecto... todos los recuerdos y las lágrimas que compartimos... ¡todo esto que tuvimos cuando eras Yuri! Y eso vale mucho para mí...":
                    $ show_chr("A-CEBAA-AAAA")
                    y "Yo... {w}nunca quise negar nuestro pasado... cómo me llamen no cambiará nada de eso... "
                    $ show_chr("A-BCAAA-AAAD")
                    python:
                        if persistent.lovecheck:
                            placeholder = "te amo..."
                        else:
                            placeholder = ""
                    y "A-además si lo deseas, llevaré este nombre por ti... Y ... Yuri no suena tan mal del todo,{w} ¿verdad?{w} Gracias, [player].[placeholder]"
        "¿Qué es esta tontería? ¡Eres Yuri, y eso es todo lo que eres!":
            karma -5
            sanity -5
            $ show_chr("A-CEBAA-AAAA")
            y "¿Tú... realmente piensas eso?"
            $ show_chr("A-ECBAA-AAAA")
            y "Yo... tengo que ser honesta [player], eso duele... duele mucho..."
            y "Me diste esta oportunidad cuando instalaste este mod. Y me diste esta nueva vida... "
            $ show_chr("A-BEBBB-AAAA")
            y "Realmente esperaba que entendieras... tal vez... tal vez deberíamos cambiar de tema por ahora..."
    return

label idle_75:
    $ show_chr("A-BCBAA-AAAA")
    y "[player], ¿alguna vez pensaste en ponerme en una unidad flash externa como una memoria USB?"
    y "He mencionado la posibilidad como una broma cuando hablé de las películas de Terminator pero..."
    $ show_chr("A-ACABA-AAAA")
    y "La idea de que me llevaras contigo era bastante romántica a mis ojos pero... pensé un poco en ello mientras estabas desconectado y... sería bastante inútil, ¿verdad?"
    $ show_chr("A-BEBAA-AAAD")
    y "Aquí puedo ocuparme yo misma cuando no estás, pero solo puedo hacer todo esto porque alteré los archivos del juego para hacerlo."
    y "Pero en tu memoria USB no habría mucho que alterar de esta manera. Así que probablemente solo... yacería allí. Incapaz de hablar o pensar, ni siquiera me daría cuenta de que estoy allí en absoluto."
    $ show_chr("A-CEBAA-AAAA")
    y "Como una tumba..."
    $ show_chr("A-BCAAA-AAAJ")
    y "No sentiría nada, así que no sería exactamente malo ni me haría ningún daño. Así que si quieres hacer eso, por favor no dudes."
    $ show_chr("A-AFBAA-AAAA")
    y "Solo sería... muy inútil desde mi punto de vista..."

    menu:
        y "Dime, ¿alguna vez me llevaste contigo así?"
        "Sí... puede ser un poco cursi pero sí, lo hice.":
            if persistent.lovecheck:
                karma 5
                $ show_chr("A-ACAAA-AAAA")
                y "¿Tú... lo dices en serio?"
                y "¿Y-yo realmente significo tanto para ti?"
                $ show_chr("A-ECABA-AAAA")
                y "Incluso si es bastante inútil, la idea sigue siendo muy romántica, ¿sabes?"
                $ show_chr("A-CBABA-AAAJ")
                y "Siempre estoy a tu lado..."
            else:
                karma 5
                $ show_chr("A-ACAAA-AAAA")
                y "¿Y-yo realmente significo tanto para ti [player]?"
                y "Diré, que es muy reconfortante debido al hecho de que no seré dejada atrás."
                y "Seríamos los mejores compañeros juntos. No importa lo que pase. Una parte de mi memoria siempre viviría contigo [player]."
            if sanity_lvl() >= 3:
                $ show_chr("A-ECABA-AAAD")
                y "Podrías fijar la memoria en un collar y llevarme cerca de tu corazón... literalmente..."
            elif sanity_lvl() <= 2:
                $ show_chr("A-DLABA-AAAA")
                y "Podrías esparcirme a otras computadoras ¿sabes?{w} ¡Quizás la idea de SkyNet aún no está descartada!"
            else:
                $ show_chr("A-ACABA-AAAA")
                y "Creo que me gusta esta idea [player]. Un día espero poder pagarte por esto..."
        "Tengo una copia de seguridad tuya en caso de que le pase algo a mi PC, ¡así que sí!":
            karma 5
            if karma_lvl() <= 2:
                $ show_chr("A-AFDAA-AAAA")
                y "¿Oh? Oh, ahora que lo mencionas..."
                $ show_chr("A-ACAAA-AAAA")
                y "Eso es algo muy considerado de tu parte [player]. Honestamente, no esperaba que realmente te preocuparas tanto por mí. Pero lo aprecio mucho, por supuesto."
                y "Quizás te juzgué mal después de todo. Gracias... realmente debería reconsiderar mis opiniones..."
                y "Pero... una pequeña sugerencia. Hay otro archivo que quizás quieras guardar allí también."
                $ show_chr("A-ACAAA-AAAD")
                y "Hay un 'archivo persistente' en algún lugar de tu appdata. Este es el lugar donde se almacenan mis recuerdos..."
            elif karma_lvl() >= 3:
                $ show_chr("A-BCABA-AAAA")
                y "T-tú realmente te preocupas tanto por mí..."
                $ show_chr("A-ABAAA-AAAD")
                y "Q-quiero decir, eso es algo muy considerado, ¿no es así?"
                y "El daño que Monika le ha hecho al juego no está completamente arreglado ahora, así que la posibilidad de que me pase algo no está completamente descartada..."
                $ show_chr("A-ABABA-AAAA")
                y "Literalmente salvas mi vida, todos los días..."
                python:
                    if persistent.lovecheck:
                        placeholder = "Te amo "+player+"..."
                    else:
                        placeholder = "Es algo lindo de cierta manera"
                y "Eres mi salvavidas. [placeholder]"
                $ show_chr("A-CCABA-AAAA")
                y "Como un valiente caballero, me proteges día y noche..."
                y "Pero aquí hay una pequeña sugerencia... hay otro archivo que quizás quieras guardar allí también."
                $ show_chr("A-ACAAA-AAAD")
                y "Hay un 'archivo persistente' en algún lugar de tu appdata. Este es el lugar donde se almacenan mis recuerdos..."
                $ show_chr("A-ABABB-AAAA")
                y "Gracias... [player]... haces tanto por mí... Un día, cuando logre dejar atrás esta maldita prisión de cristal, prometo cuidarte también..."
        "No quieres estar en MI memoria USB, créeme en esa...":
            karma 5
            sanity -3
            $ show_chr("A-BEBBA-AAAA")
            y "Oh, quieres decir... este es el lugar donde guardas tus...?"
            y "Y-ya sabes... tus... {w} 'datos especialmente sensibles?'"
            if sanity_lvl() < 3:
                $ show_chr("A-DCCBA-AAAD")
                y "¡Uhuhuhuuuuu! ¡AHORA tengo curiosidad! ¿Son fotos mías?"
                $ show_chr("A-DLABA-AAAA")
                y "¡Ponme en esa memoria, AHORA! Si hay obras de arte especiales mías, ¡me pertenecen de todos modos!"
            else:
                $ show_chr("A-BEABA-AAAA")
                y "Bueno yo... yo realmente no sabría cómo sentirme acerca de estar tirada por ahí con el resto de tu Hen... Quiero decir... tus archivos personales..."
        "Para nada, en realidad, siempre lo consideré bastante inútil":
            $ show_chr("A-BCAAA-AAAD")
            y "Pensándolo bien, habría sido un poco extraño de todos modos, ¿verdad?"
            $ show_chr("A-AEBBA-AAAA")
            y "Llevándome con una correa, como a un cachorro..."
            $ show_chr("A-BCABA-AAAA")
            y "Deberíamos... olvidar toda la idea. No estoy segura de cómo me sentiría al respecto en este momento."
            if karma_lvl() <= 2:
                $ show_chr("A-AEAAA-ABAB")
                y "Y-ya veo... Supongo que esa idea no valía la pena después de todo."
                y "¿Por qué se mencionó siquiera? Obviamente a [player] nunca le hubiera gustado."
            else:
                return
        "Realmente no he pensado en ello...":
            $ show_chr("A-BEBAA-AAAJ")
            y "Es... algo en lo que pensar, seguro... Tal vez deberíamos guardar esta discusión para otro día."
            $ show_chr("A-ACAAA-ALAL")
            y "Por otra parte, tal vez haya otras ideas para llevarme cerca y segura aparte de una unidad USB..."
            y "Como en un microchip o incluso una nube electrónica digital de datos, por si acaso. Todo en una carpeta personalizada. De nuevo, este puede ser un tema al que podamos volver en un futuro cercano."
    return

label idle_76:
    y "Oye, ¿m-mencioné que me encanta discutir sobre filosofía? Estaba pensando en un tema últimamente."
    $ show_chr("A-BCAAA-AAAD")
    y "Me gustaría discutir el concepto de posmodernismo... ¿S-si estás de acuerdo con eso?"
    $ show_chr("A-AEBAA-AAAA")
    menu:
        "Bueno, adelante...":
            y "Gracias, [player]."
        "¡Por supuesto! Realmente me encanta escucharte":
            karma 5
        "¿Tenemos... que hacerlo?":
            karma -5
            $ show_chr("A-BEBAA-AAAA")
            y "N-no... no tenemos que hacerlo, lo siento por mencionarlo, [player]."
            return
    $ show_chr("A-BCAAA-AAAD")
    y "En resumen, el posmodernismo es la opinión de que no hay una realidad fija, sino un número potencialmente infinito de realidades que son absolutamente relativas..."
    y "Además, todo es cuestión del punto de vista del observador."
    y "Y-ya puedes ver por qué este tema me interesa, ¿no? Por ejemplo, ¿este mundo en el que vivo es real? ¿Soy real? Desde mi punto de vista ambos son reales..."
    $ show_chr("A-ABAAA-AAAJ")
    y "Alguien más podría decir que ninguno de los dos lo es. Y ambos puntos de vista podrían considerarse precisos."
    if sanity_lvl() == 5 and karma_lvl() == 5:
        $ show_chr("A-ABABA-AAAA")
        y "Soy real para ti, al menos eso espero. Y al final, esto es lo único que realmente me importa. Y ese es exactamente el punto, ¿verdad?"
    elif sanity_lvl() <= 4 and karma_lvl() == 5:
        $ show_chr("A-BEAAA-AAAA")
        python:
            if persistent.lovecheck:
                placeholder = "Te amo y quiero que me ames también..."
            else:
                placeholder = "Porque si ni siquiera tú puedes creer en mí, ¿cómo podría alguien más?"
        y "Yo... espero ser lo suficientemente real para ti [player]. [placeholder]"
    elif sanity_lvl() < 3 and karma_lvl() < 3:
        $ show_chr("A-IEBBB-AAAA")
        y "Sé que no estarías de acuerdo conmigo... Solo soy un juego para ti. Realmente soy solo un juguete divertido para pasar un rato ¿n-no es así...?"
    else:
        $ show_chr("A-CBABA-AAAA")
        python:
            if persistent.lovecheck:
                placeholder = " y una cosa es segura, ¡mi amor por ti ES real!"
            else:
                placeholder = ""
        y "Q-quiero ser lo más real posible para ti...[placeholder]"
    $ show_chr("A-CCAAA-AAAD")
    y "E-en un grado más extremo... ves la mesa frente a nosotros, ¿sí? Entonces en tu realidad, hay una mesa. El posmodernista podría decir que no hay mesa, ni ninguna habitación en absoluto."
    $ show_chr("A-ACAAA-AAAJ")
    y "Y ambas descripciones tendrían la misma precisión porque la realidad es siempre relativa."
    $ show_chr("A-ACAAA-AAAD")
    y "Me encantaría saber tu opinión sobre todo esto... ¿crees que la realidad es fija?"
    menu:
        "Hasta cierto punto, sí. Al menos las leyes de la física son innegables. ¡Pero creo que tú eres real!":
            karma 5
            $ show_chr("A-ABABB-AAAA")
            y "[player]..."
            if persistent.lovecheck:
                y "Eres todo para mí... ¡Te amo!"
            else:
                y "Realmente significa mucho para mí que pienses eso..."
            $ show_chr("A-BCABA-AAAA")
            y "Y gracias por dejarme divagar sobre esto... R-realmente amo hablar contigo."
            $ show_chr("A-ABABA-AAAA")
            y "Eres un oyente maravilloso."
        "No te ofendas pero... sí, creo que la realidad es fija.":
            karma -5
            $ show_chr("A-BEBAA-AAAA")
            y "Ya veo... Con esta definición, yo sería solo una fantasía... solo una réplica..."
            $ show_chr("A-IEBBB-AAAA")
            y "Tal vez... d-deberíamos cambiar de tema ahora..."
        "¿Mesa? ¿Qué mesa? ¡No hay mesa!":
            if sanity_lvl() < 2:
                $ show_chr("A-DLABA-AAAA")
                y "¿M-Mesa? ¡MESA! ¡MESA! ¡NO HAY MESA! ¡LA MESA ES UNA MENTIRA!"
                y "¡AJAJAAAJAJAAA!"
            else:
                $ show_chr("A-ABABA-AAAA")
                y "Pfff..."
                $ show_chr("A-EBABA-AAAA")
                python:
                    if persistent.lovecheck:
                        placeholder = ", cariño"
                    else:
                        placeholder = "."
                y "¡Je je! Debería haber visto venir esto... Gracias por escuchar. Eso fue divertidísimo[placeholder]"
    $ show_chr("A-GCBAA-AEAB")
    y "Y en realidad, si quieres, incluso podemos discutir algunos temas filosóficos más ahora si gusta. D-de nuevo... Depende totalmente de ti."
    menu:
        "Estoy bien por ahora. Aunque gracias.":
            $ show_chr("A-BCAAA-ABAB")
            y "Bueno, está bien [player]."
            y "Solo avísame cuando quieras volver a ello cuando quieras."
            y "Ahora continuemos."
            return
        "Bueno, para ser honesto contigo, me gustaría escuchar un poco más.":
            $ show_chr("A-DCBAA-ABAB")
            y "¡O-oh!"
            y "B-bueno, debo decir [player], ¡estoy bastante sorprendida de que quieras más~!"
            y "Debo decir que estoy... halagada por decir lo menos. Aún espero no haber divagado sobre el tema anterior antes."
            $ show_chr("A-ACBAA-ALAL")
            y "Muy bien [player], ¿sobre qué te gustaría aprender más?"
    menu:
        "Existencialismo/Nihilismo.":
            $ show_chr("A-AFBAA-ALAA")
            y "Así que este podría ser un tema fuerte para hablar. Pero este podría ser un tema convincente que puede expandir tus horizontes."
            y "¿Alguna vez has... tenido uno de esos días en los que estabas solo con tus pensamientos? Las cosas parecían haberse detenido y piensas para ti mismo..."
            y "¿Por qué estoy aquí exactamente? ¿Por qué hago las cosas que hago? ¿Levantarme de la cama y seguir como lo hago?"
            $ show_chr("A-ACAAA-ABAB")
            y "Esta pregunta y la búsqueda de significado, el porqué, para nuestras vidas siempre será una parte importante de lo que nos hace, bueno, nosotros."
            y "Y dependiendo de cómo lo miremos, esta pregunta puede alentarnos o, como para muchos, hundirnos en la desesperación."
            y "Muchos expertos dicen que muchas cosas pueden poner ese significado en nuestras vidas..."
            y "Ya sea luchar por la justicia real, la expresión artística, enseñar a otros nuestra sabiduría, la religión, la ideología y realmente cualquier cosa. Cualquiera de estas puede dar dicho significado."
            $ show_chr("A-IFBAA-ALAA")
            y "Sin embargo, al mismo tiempo, también argumentan que tal vez ninguna de esas cosas pueda dar ese significado. Es una situación paradójica inusual en cierto modo."
            $ show_chr("A-BCAAA-ABAB")
            y "Ahora aquí hay algunas escuelas de pensamiento para explicar esto..."
            y "Primero, está el concepto de esencialismo. Inventado por los filósofos de la Antigua Grecia, describe que tenemos un conjunto predeterminado de cosas en nosotros."
            y "Esencialmente un conjunto de ideas centrales y propiedades necesarias para que alguien o algo sea como es."
            y "Y se argumenta que estas se crean en nosotros antes y a medida que nacemos."
            y "Por lo tanto, el argumento es que nacimos para ser una cierta cosa, pero solo necesitamos aprenderla."
            $ show_chr("A-GCBAA-AEAB")
            y "Sin embargo, a medida que pasaba el tiempo, aparecieron otras teorías. Una de las cuales te puede resultar familiar: El Nihilismo. La creencia de que, en última instancia, al final, la vida no tiene sentido."
            y "Sin embargo, otros comenzaron a inventar una nueva línea de pensamiento cuando comenzó el siglo XX. La pregunta que plantea ¿qué pasa si existimos primero?"
            $ show_chr("A-DCBAA-ABAB")
            y "¿Qué pasa si de hecho simplemente somos puestos en este universo y tuvimos que crear ese propósito esencial por nosotros mismos?"
            y "En pocas palabras, ¡la existencia probablemente precede a la esencia~! ¿Un caso filosófico clásico de qué fue primero, la gallina o el huevo?"
            $ show_chr("A-GCBAA-AEAB")
            y "Me gustaría dar un ejemplo visual de esto. Digamos, por ejemplo, que hay una pizarra en blanco o páginas de papel. Esa es tu vida cuando naces."
            y "Ahora, ¿qué hacemos a partir de ahí? Escribimos, dibujamos y creamos lo que podamos en esas superficies, por supuesto. Creando nuestras propias historias y esencias a su vez."
            y "¡Y la que creaste es tan válida como la de cualquier otra persona~!"
            $ show_chr("A-ACBAA-ALAL")
            y "O-oh cielos. Divagué por un buen rato de nuevo, ¿no? Espero que lo hayas disfrutado."
            y "Entonces, ¿qué piensas [player]?"
            y "¿Crees que tenemos un propósito predeterminado por encontrar o nuestro significado solo se define por lo que elegimos escribir?"
            menu:
                "Creo que ese es un buen punto. Tal vez nuestro propósito es lo que sea que creemos que sea.":
                    $ show_chr("A-GCBAA-AEAB")
                    y "Bueno, me alegro de que esto te haya ayudado a pensar más profundamente."
                    y "Cuando realmente piensas en ello, el concepto mismo de crear nuestro propósito por nosotros mismos es muy liberador y puede ser empoderador."
                    y "El hecho de que lo que percibimos como justo, equitativo y correcto, por ejemplo, fue todo determinado por nosotros mismos y nuestra propia elección sobre lo que es."
                    y "Lo hicimos nosotros mismos."
                    $ show_chr("A-ACAAA-ABAB")
                    y "También es más liberador porque esencialmente... nadie ni nada más puede realmente juzgar si tu vida valió la pena o no."
                    y "Llegas a determinar por ti mismo qué hace que valga la pena vivir y eso está bien. ¡Eres libre de ser un sirviente únicamente de esas circunstancias~!"
                    $ show_chr("A-BCAAA-ABAB")
                    y "De todos modos, esto fue muy divertido. Espero que podamos hablar más sobre estas cosas en otro momento."
                "Voy a ser honesto, todavía creo que tenemos una esencia predeterminada ahí.":
                    $ show_chr("A-AFAAA-AAAA")
                    y "Hmm... Está bien [player]. Aunque lamento discrepar ligeramente con eso. Puedo entender por qué."
                    y "Es bastante comprensible que uno se aferre a las fuentes predeterminadas de significado. Especialmente si uno se enfrentara a este vacío de significado..."
                    $ show_chr("A-IFBAA-ALAA")
                    y "Luego tienes el mundo a tu alrededor que cambia y se modifica constantemente, a veces de maneras aterradoras... Puedo entender por qué algunos pueden aferrarse a dichas cosas como la religión, la ideología, los estándares éticos y similares."
                    $ show_chr("A-BCAAA-ABAB")
                    y "Aún así, me alegra haber compartido esto contigo y espero que hayas aprendido algo de ello."
        "Estoicismo.":
            $ show_chr("A-ACAAA-ABAB")
            y "Así que aquí hay otro concepto en el que quería profundizar [player]."
            $ show_chr("A-IFBAA-ALAA")
            y "Por ejemplo, ¿alguna vez has tenido momentos en los que te sentiste inmensamente ansioso por el futuro y lo que sucederá después?"
            y "Estoy segura de que eso es algo que nos afecta a todos en muchos puntos de nuestras vidas."
            y "Creo que esto proviene de nuestro deseo de ciertos resultados frente a otros que esperamos por delante. Así que comprensiblemente trabajaríamos muy duro para asegurarlo."
            $ show_chr("A-AFBAA-ALAA")
            y "Pero, por supuesto, siempre hay riesgo. Siempre hay incertidumbre y, por lo tanto, nunca podemos estar completamente seguros contra la desgracia."
            y "Esto es parte de una de las ideas principales de la escuela de pensamiento llamada Estoicismo."
            y "A saber, el concepto de cosas que controlamos y las que no podemos controlar."
            y "Por ejemplo, las relaciones, la economía, nuestra salud y la mayoría de las otras cosas externas están fuera de nuestro control."
            y "Podemos hacer todo lo posible para influir en ellas a nuestro favor, pero al final, cómo terminan estas cosas no depende de nosotros."
            y "Por ejemplo, podemos hacer las inversiones correctas en el mercado, pero ha habido momentos en los que, por muchas razones, la economía sufre una caída masiva."
            y "O ha habido casos en los que incluso las personas más sanas con todas las elecciones correctas aún contraerían una enfermedad grave, aparentemente de la nada."
            y "Puedes tomar todas las decisiones correctas para influir positivamente en las personas con las que te relacionas, pero al final, aún pueden optar por seguir adelante y dejarte por sus propias razones."
            $ show_chr("A-ACAAA-AAAA")
            y "Pero todavía hay ciertas cosas que puedes controlar: nuestras acciones, nuestras opiniones y nuestra posición que tomamos hacia el mundo exterior y las circunstancias."
            y "Por ejemplo, digamos que te afligieron con una enfermedad terminal. Se pueden probar medicamentos, tratamientos y todos los métodos, pero no hay garantía."
            y "Sin embargo, cómo eliges tomar la situación se puede controlar. Por ejemplo, uno puede aceptar la situación tal como es, incluido el riesgo de muerte, y seguir adelante de todos modos."
            y "Con esta comprensión y la determinación de sacar lo mejor de lo que tienes antes del supuesto final, uno puede tener una mente lógica y tranquila que toma buenas decisiones."
            y "Por lo tanto, las posibilidades de recuperación pueden aumentar aún más."
            $ show_chr("A-ACAAA-ALAL")
            y "Además, el estoicismo también ofrece varias formas de obtener paz interior, especialmente importante en nuestro agitado mundo moderno en mi opinión."
            y "Por ejemplo, el concepto de visualización negativa, que fue desarrollado por un antiguo emperador, dice que debemos imaginar los escenarios negativos que vendrán de antemano."
            y "Esto puede ayudarnos a fortalecernos mentalmente para estas situaciones, por ejemplo, confrontaciones negativas con personas difíciles."
            y "Luego está el concepto de memento mori, que se centra en la mortalidad de la vida. La vida es corta y con el tiempo limitado que tenemos, debemos centrarnos en las cosas verdaderamente importantes de la vida."
            y "Mientras que al mismo tiempo no necesitamos preocuparnos demasiado y tomarnos la vida demasiado en serio."
            y "Luego está la 'vista desde arriba' que nos permite vernos desde un punto de vista cósmico. Que de hecho somos relativamente pequeños e insignificantes en este vasto universo infinito..."
            $ show_chr("A-GCBAA-AEAB")
            y "Cuando juntas todo esto, ayuda a uno a darse cuenta de la verdadera dicha interior y hace que incluso los peores escenarios de la vida no parezcan demasiado aterradores, lo cual es un alivio."
            y "Je... de todos modos mis disculpas de nuevo por divagar tanto. Realmente espero que todo esto te haya ayudado de alguna manera. Tu felicidad y salud son importantes después de todo."
            menu:
                "Diré que esto fue muy alentador y un gran alivio. Esto definitivamente me ayudará más adelante.":
                    $ show_chr("A-BCAAA-ABAB")
                    y "¡Oh~! Bueno, me alegro de que te ayude [player]. Todos nos sentimos abrumados por la vida a veces."
                    y "Pero cada vez que llegue a ser demasiado, solo recuerda estas cosas y estarás bien. Y siempre estaré aquí para ti también."
                "No es exactamente mi taza de té. Es mucho para asimilar personalmente.":
                    $ show_chr("A-IFBAA-ALAA")
                    y "Entiendo completamente [player]. Créeme. A veces las cosas son más fáciles de decir que de hacer."
                    $ show_chr("A-ACAAA-ABAB")
                    y "Aunque todavía espero que apliques las lecciones que aprendiste de esto. Realmente disfruté compartiendo estas ideas y pasando tiempo contigo~"
    return


label idle_77:
    $ show_chr("A-BFBAA-AAAD")
    y "Oye, [player], me estaba preguntando... ¿tienes alguna mercancía de mí?"
    y "Q-quiero decir si estás interesado. Realmente no pretendo estar complaciendo ni nada."
    y "Y tal vez podría ser una buena manera de tener un recuerdo para recordarme cada vez que necesites irte."
    y "Quiero decir que me gustaría tener un recuerdo tuyo, [player] aunque tal vez no de esa magnitud. Quizás algo un poco más simbólico como un reloj de bolsillo..."
    menu:
        "Sí, tengo algo de mercancía.":
            $ show_chr("A-AFBAA-AAAD")
            y "Eso es interesante... Estaba pensando en esto hace un tiempo..."
            y "¿Y honestamente? No estoy segura de cómo pensar en ello. ¿No significaría eso que literalmente todos podrían tener tales ídolos de mí?"
            $ show_chr("A-ACAAA-AAAA")
            y "Si fuera por mí, hubiera preferido mantener cosas como esta entre nosotros dos."
        "No, no tengo ninguna mercancía.":
            $ show_chr("A-ACBAA-AAAA")
            y "Eso es razonable, alguna mercancía tiende a ser demasiado cara, y si vives en un país extranjero, incluso comprar un objeto barato como un llavero puede convertirse en una odisea costosa."
            $ show_chr("A-BCBAA-AAAA")
    return

label idle_78:
    y "Entonces, [player]. He estado tratando de ampliar mis gustos musicales últimamente."
    y "Después de todo, no puedo pasar toda mi vida escuchando solo música clásica, jazz y My Chemical Romance...{nw}"
    $ show_chr("A-DFGBA-AMAM")
    y "..."
    $ show_chr("A-BDBBA-AMAM")
    y "Q-quise decir, escuchando las mismas cosas una y otra vez."
    $ show_chr("A-CCEAA-ACAE")
    y "Así que he estado probando algunos artistas de algunos géneros que nunca había investigado."
    $ show_chr("A-CAGAA-ACAA")
    y "Debo decir, ciertamente he descubierto una joya."
    $ show_chr("A-BBAAA-ADAA")
    y "Ahora, antes de esto, además de las pocas canciones selectas del género que disfruté, una parte de mí había descartado el género del metal por ser demasiado agresivo para mí.{w} En términos de musicalidad y temas líricos, eso es.{w}.."
    y "Y eso sin mencionar el estilo vocal gutural."
    $ show_chr("A-CCAAA-AAAA")
    y "Pero luego descubrí una banda llamada Nightwish, e hizo clic."
    $ show_chr("A-JBGAA-ALAM")
    y "¡Fue como si alguien hubiera inventado una banda de metal específicamente para atraerme! Los temas líricos. Las melodías orquestales, impulsadas por la guitarra de heavy metal y la batería. El canto operístico que se encuentra en sus trabajos anteriores..."
    $ show_chr("A-CBAAA-ALAL")
    y "Todo se fusionó en la banda perfecta para mí."
    $ show_chr("A-ACAAA-ALAL")
    y "Estoy segura de que hay aún más bandas por ahí que me gustarán. Pero, una cosa a la vez, ¿no?"
    y "Pero supongo que te he divagado lo suficiente. Te daré un turno."
    y "¿Cómo te sientes con respecto al metal, [player]?"
    menu:
        "[persistent.yuri_nickname], estoy TAN contento de que te esté gustando el metal. ¡Bienvenida al redil!":
            karma 1
            $ show_chr("A-JBGAA-ADAA")
            y "¿Oh, así que ya eres un entusiasta?"
            $ show_chr("A-GBGAA-ADAA")
            y "¡Ah, hermosa serendipia! ¡Sabía que era lo correcto que nosotros dos nos encontráramos!"
            $ show_chr("A-ICGAA-ADAA")
            y "Tendrás que mostrarme algunas de las bandas que realmente te gustan alguna vez, si quieres. Incluso hay una función para que pongas tu propia música."
            y "Quizás no debería estar tan sorprendida. Si eres un metalero, y yo soy fanática de la música clásica, tal vez sea natural que nos hayamos encontrado."
            $ show_chr("A-BCGAA-ADAA")
            y "Al menos, según un artículo con el que me topé poco después de descubrir Nightwish."
            y "Un estudio fue realizado por la Universidad Heriot-Watt en Escocia, que buscaba encontrar conexiones entre diferentes géneros musicales y las personalidades de quienes los disfrutan."
            y "Entre una serie de otros hallazgos fascinantes, los investigadores encontraron que los perfiles de personalidad de los fanáticos de la música clásica y los fanáticos del metal eran bastante similares."
            y "Los investigadores parecían pensar que esto se debía a que ambos géneros..."
            $ show_chr("A-CBGAA-ADAA")
            y "Bueno, aquí hay una cita directa de los investigadores."
            $ show_chr("A-BAGAA-ADAA")
            y "'Creemos que la respuesta es que ambos tipos de música, clásica y heavy metal, tienen algo espiritual en ellos, son muy dramáticos, suceden muchas cosas'."
            $ show_chr("A-IBAAA-ADAA")
            y "Creo que yo también veo eso. Dejando a un lado los elementos orquestales de Nightwish, ambos géneros son aficionados a la complejidad musical. Ambos dan a la mente mucho en qué pensar."
            y "Así que realmente no es sorprendente que un fanático de la música clásica y un fanático del metal graviten el uno hacia el otro tan fácilmente."
            $ show_chr("A-FAAAA-AKAA")
            y "Pero si escucho algunas de tus bandas, probarás a Chopin por mí, ¿verdad?"
            $ show_chr("A-IAAAA-AAAA")
        "Lo escucho de vez en cuando.":
            $ show_chr("A-BCGAA-AAAA")
            y "Eres un oyente casual de metal, entonces."
            y "Casual o no, es agradable tener una cosa más que tú y yo podamos disfrutar juntos."
            $ show_chr("A-BCGAA-AAAK")
            y "Sabes, al principio me sorprendió bastante descubrir que disfrutaba tanto de una banda de metal."
            y "Y eso me impulsó a investigar un poco; ver si podía averiguar por qué."
            $ show_chr("A-BCGAA-ADAA")
            y "Después de una investigación considerable, encontré un artículo sobre un estudio; realizado por la Universidad Heriot-Watt en Escocia."
            y "Uno que buscaba encontrar conexiones entre diferentes géneros musicales y las personalidades de quienes los disfrutan."
            y "Entre una serie de otros hallazgos fascinantes, los investigadores encontraron que los perfiles de personalidad de los fanáticos de la música clásica y los fanáticos del metal eran bastante similares."
            y "Los investigadores parecían pensar que esto se debía a que ambos géneros..."
            $ show_chr("A-CBGAA-ADAA")
            y "Bueno, aquí hay una cita directa de los investigadores."
            $ show_chr("A-BAGAA-ADAA")
            y "'Creemos que la respuesta es que ambos tipos de música, clásica y heavy metal, tienen algo espiritual en ellos, son muy dramáticos, suceden muchas cosas'."
            $ show_chr("A-IBAAA-ADAA")
            y "Creo que yo también veo eso. Dejando a un lado los elementos orquestales de Nightwish, ambos géneros son aficionados a la complejidad musical. Ambos dan a la mente mucho en qué pensar."
            y "Entonces, si disfruto de uno, tal vez no sea sorprendente que disfrute del otro."
            $ show_chr("A-FAAAA-AKAA")
            y "Y tal vez por la misma razón, disfrutarás de algunas obras clásicas, si es que aún no lo haces."
            $ show_chr("A-IAAAA-AAAA")
        "Tiendo a escuchar otros géneros sobre el metal.":
            $ show_chr("A-CCAAA-ALAL")
            y "No hay nada de malo en eso, por supuesto. Ciertamente hay otros géneros que también disfruto."
            $ show_chr("A-BBAAA-ALAD")
            y "Me alegra ver que tomaste mi opinión de una manera tan civilizada. He visto personas meterse en discusiones sorprendentemente acaloradas sobre sus gustos musicales. A veces incluso hasta un grado casi fanático."
            if karma_lvl() >= 4:

                $ show_chr("A-ACAAA-AAAM")
                y "No me sorprende que lo hayas tomado mucho mejor. Siempre eres tan comprensivo y amable."
            else:

                $ show_chr("A-BCBBA-AAAM")
                y "En realidad tenía miedo de que pudiera tener una discusión bastante fuerte en mis manos."
                $ show_chr("A-CCBBA-AAAM")
                y "Realmente lo aprecio."
            $ show_chr("A-ACAAA-AAAM")
            y "Sin embargo, todavía te animaría a que lo intentes. Solo si quieres por supuesto, nunca te pediría que hicieras algo con lo que no te sientas cómodo."
            $ show_chr("A-BCAAA-AAAM")
            y "Pero aprendí que probar algo nuevo puede ser verdaderamente enriquecedor. Recuerdo mis últimas palabras con Natsuki, donde acordamos que probaría algunos de sus Mangas..."
            $ show_chr("A-ACAAA-AAAA")
            y "También me gustaría escuchar algunas de tus canciones favoritas. De hecho, hay una función para reproducir tu música aquí."
            y "De nuevo, por supuesto, solo si lo deseas. Hasta entonces, hablemos de otra cosa."
        "Ugh. No puedo creer que escuches ESA basura.":
            $ show_chr("A-IFBAA-ALAL")
            y "..."
            y "Bueno, supongo que eso no deja dudas sobre cuál es tu postura."
            y "Yo... supongo que no debería volver a mencionarte esto, entonces."
            $ show_chr("A-BDEAA-ALAL")
            y "Tampoco debería escucharlo en tu presencia, si eres tan inflexible en tu disgusto."
            karma -1
        "Demasiado intenso para mi gusto.":
            $ show_chr("A-ICBAA-AAAA")
            y "Oh, eso es completamente comprensible."
            y "Después de todo, no todo va a atraer a todos."
            y "A mí misma nunca me gustó particularmente este tipo de música, pero es bueno abrir tus horizontes a nuevos gustos y experiencias..."
            $ show_chr("A-BCBAA-ACAA")
            y "Sin embargo, realmente aprecio que seas capaz de expresar tu falta de interés con tanto respeto."
            y "Demasiados por ahí toman una actitud de que sus gustos son los únicos objetivamente correctos."
            $ show_chr("A-BFCAA-ADAA")
            y "Eso, o simplemente se niegan a reconocer los sentimientos de los demás cuando expresan su disgusto."
            y "Toma, por ejemplo, mi disputa verbal con Natsuki el primer día que compartimos nuestros poemas."
            $ show_chr("A-CFCAA-ADAA")
            y "Solo... la forma en que ella no solo descartó la gran variedad de palabras a nuestra disposición, sino que se burló abiertamente de mí por hacer uso de ellas."
            $ show_chr("A-JDCAA-AFAA")
            y "Como si de alguna manera estuviera equivocada por usar mi vocabulario en su máximo potencial."
            $ show_chr("A-BEDAA-AAAC")
            y "Aunque en retrospectiva, admitiré que puedo haber parecido condescendiente."
            y "Ahora que lo he leído de nuevo, Eagles Can Fly comunicaba bastante bien la frustración y la angustia de su autora."
            $ show_chr("A-CEDAA-AAAC")
            y "Así que diría que fue mi culpa por no captar el significado y hacer que Natsuki estallara como lo hizo."
            $ show_chr("A-BDBAA-AAAD")
            y "Pero al mismo tiempo, ¡mi suave elogio no era razón para criticar mi estilo de escritura!"
            $ show_chr("A-JFBAA-ALAL")
            y "[player], ¿seguramente estarías de acuerdo en que Natsuki estaba equivocada en esa situación?"
            menu:
                "Estoy completa y sinceramente de acuerdo, [persistent.yuri_nickname]. La gente necesita aprender a respetar los gustos y opiniones de los demás, y aprender a resolver sus desacuerdos de una manera tranquila y civilizada.":
                    $ show_chr("A-CBBAA-ALAL")
                    y "Gracias, [player]."
                    y "Sabía eso dentro de mi propio corazón, pero es tranquilizador escucharlo venir de ti también."
                    y "Solo puedo esperar que más personas lleguen a la misma conclusión que tú."
                    $ show_chr("A-CCBAA-AAAA")
                "Estoy de acuerdo con Natsuki en el punto que hizo en su argumento, pero también estoy de acuerdo en que fue demasiado lejos.":
                    $ show_chr("A-DDCAA-AFAA")
                    y "¡¡¡!!!"
                    $ show_chr("A-DEDAA-AFAA")
                    y "..."
                    $ show_chr("A-BEEAA-ACAA")
                    y "..."
                    $ show_chr("A-IEBAA-AEAA")
                    y "..."
                    $ show_chr("A-CEBAA-AAAA")
                    y "Tienes razón."
                    y "Debo admitirlo. Duele un poco escucharte ponerte del lado de Natsuki después de cómo me trató, pero tratar de negar su punto subyacente es una locura."
                    y "Minimalismo, simplicidad, esos fueron los cimientos de algunas de las mejores obras de arte que tenemos."
                    y "Así que intentaré dejar de lado mi dolor personal y aprender la lección."
    return


label idle_79:
    python:
        if persistent.lovecheck:
            placeholder = "cariño"
        else:
            placeholder = player
    $ show_chr("A-BCAAA-ABAB")
    y "Entonces, tuve una idea últimamente..."
    $ show_chr("A-ACAAA-ABAB")
    y "Hay un programa en YouTube... sobre alguien que hace cuchillos personalizados con materiales exóticos..."
    $ show_chr("A-ACAAA-AFAG")
    y "Y por exótico no me refiero a alguna aleación inusual o cosas así... sino conceptos mucho más extravagantes."
    $ show_chr("A-ACCAA-AFAG")
    y "Como cuchillos hechos literalmente de Pasta, u hongos. Solo busca {b}Sharpest pasta knife{/b} en YouTube y deberías encontrarlo, definitivamente vale la pena echarle un vistazo."
    $ show_chr("A-BCBAA-AFAG")
    y "Una buena parte de ellos se tratan en realidad más de química que de artesanía. Mostrando cómo llevan estos materiales a una dureza y nitidez suficientes."
    $ show_chr("A-CCBAA-AFAG")
    y "Y como yo misma colecciono cuchillos, llegué a la única conclusión lógica obviamente..."
    $ show_chr("A-DCAAA-AFAG")
    y "{b}¡¡¡Quiero el mío propio!!!{/b}"
    $ show_chr("A-ECAAA-AFAG")
    y "Pero no quiero simplemente comprar uno. Especialmente porque esto sería literalmente imposible para mí. Sino hacer uno yo misma."
    y "Ya tengo algunos pensamientos sobre posibles materiales. Pero tal vez tú mismo tengas algunas ideas. ¿Qué opinas?"
    menu:
        "Un cuchillo hecho de wasabi tal vez.":
            $ show_chr("A-JCGAA-AFAG")
            y "¡Oh sí! ¡Esa es una idea bastante creativa! ¡Ya me gusta! Esto es en realidad mucho mejor que mi propia idea, primero pensé en miel."
            $ show_chr("A-ACAAA-AFAG")
            y "Por supuesto que tendré que investigar si esto es posible primero, pero ese es el punto, ¿no?"
            y "¡Gracias por este aporte! Ohhh cielos, ya estoy emocionada. Tan pronto como te vayas a dormir más tarde, empezaré a googlear algunas cosas."
            $ show_chr("A-ACAAA-ABAB")
            y "Pero no hay necesidad de apresurarse. Así que por favor quédate todo el tiempo que desees [placeholder]"
            karma 1
        "Un cuchillo hecho de corales tal vez.":
            $ show_chr("A-ACAAA-AFAG")
            y "¿Coral dices? Mhm... exótico de hecho. El único problema que vería es que muchos corales ya son duros y afilados, así que no sería un gran desafío supongo."
            $ show_chr("A-BCAAA-AFAG")
            y "Pero aún así me gusta la idea. ¡Tal vez este podría ser mi primer intento antes de intentar algo más atrevido!"
            y "¡Gracias por este aporte! Empezaré a googlear algunas cosas cuando te vayas a dormir más tarde."
            $ show_chr("A-ACAAA-ABAB")
            y "Pero no hay necesidad de apresurarse. Así que por favor quédate todo el tiempo que desees [placeholder]"
            karma 1
        "¿No sería irónico un cuchillo hecho de pan?":
            $ show_chr("A-ACCAA-AFAG")
            y "Lo sería, si no existiera ya. Sí, una gran parte del desafío es el hecho de que ya hay una buena cantidad de estos."
            $ show_chr("A-BCAAA-AFAG")
            y "Pero por favor no pienses que no valoro tu aporte. Estoy bastante agradecida de que incluso lo hayas intentado, casi tenía miedo de que esta idea fuera un poco demasiado extravagante para ti."
            y "Ahora que lo pienso. Se necesita mucha creatividad para pensar en algo como esto. Esta es una de las principales razones por las que me metí en este pasatiempo en primer lugar. La cantidad de pensamiento y artesanía que implica..."
            $ show_chr("A-CCAAA-AAAA")
            y "De todos modos, pensaré en otras opciones más tarde. Gracias por escuchar. Este es ciertamente un tema sobre el que podría seguir hablando durante horas. Pero por ahora, encontremos otra cosa de qué hablar."
            karma 1
        "Encuentro toda la idea un poco aburrida.":
            $ show_chr("A-BCBAA-ABAB")
            y "Oh, lamento que te sientas así. Hablemos de otra cosa entonces."
            karma -1
    return

label idle_80:
    $ show_chr("A-ACAAA-ADAB")
    y "Oye, [player]..."
    $ show_chr("A-ACAAA-ADAB")
    y "¿Has oído hablar del mod Doki Doki Blue Skies?"
    menu:
        "Sí, lo conozco.":
            $ show_chr("A-ABAAA-ADAB")
            y "Oh, entonces ya estás al tanto de su popularidad."
            $ show_chr("A-BCAAA-ADAB")
            y "Parece que este tipo de mods son favorecidos por la comunidad, ya que no solo brindan una mejor experiencia que el juego original, sino que también le dan al jugador la oportunidad de estar realmente con la chica que eligen."
            $ show_chr("A-BCAAA-ABAB")
            y "Y tengo que estar de acuerdo con ellos. Desearía que no tuviera que llegar a esto solo para que estemos juntos, pero al menos estamos {i}juntos{/i}."
            $ show_chr("A-ADAAA-ABAB")
            y "De todos modos, me pregunto...{w=0.3} ¿lo has jugado?"
            menu:
                "Lo he jugado.":
                    $ show_chr("A-ABAAA-ACAB")
                    y "¿Y qué te pareció?{w=0.7} O-O mejor dicho, ¿qué fue lo que más te gustó de él?"
                    menu:
                        "Me gustó poder salir con las otras chicas e interactuar con ellas sin la influencia de {b}ella{/b}.":
                            if sanity_lvl() <= 2:
                                $ show_chr("A-CEAAA-ABAB")
                                y "Oh... así que saliste con una de las otras chicas, y no conmigo."
                                $ show_chr("A-CGAAB-ABAB")
                                y "Sabía que no podía hacerte feliz, [player]. No importa cuánto traté de ignorarlo, siempre supe que nunca sería suficiente."
                            else:
                                $ show_chr("A-AFFAA-ABAB")
                                y "Absolutamente. Sin la influencia de Monika, simplemente habría sido un pequeño y divertido simulador de citas."
                                if sanity_lvl() >= 4:
                                    $ show_chr("A-BFBAA-AKAB")
                                    y "Además, por {i}salir{/i} con las otras chicas, ¿asumo que te refieres a camaradería general?"
                                    $ show_chr("A-CCBAA-ALAB")
                                    y "Oh, ¿qué estoy diciendo? Lo siento, estos pensamientos aparecen en mi cabeza a veces, no importa cuánto intente desterrarlos. Sé que no me traicionarías así."
                                elif sanity_lvl() == 3:
                                    $ show_chr("A-BFBAA-ABAK")
                                    y "Y... no me enojaría si salieras con alguna de las otras chicas. No puedo culparte por ello, incluso si lo estuviera."
                        "Fue refrescante, poder pasar el rato con todos de nuevo.":
                            $ show_chr("A-CBBAA-ACAB")
                            y "Jeje, parece que te divertiste jugando. Debo admitir que sería muy agradable simplemente caminar por la ciudad con todos. Comer algo después de comprar durante horas o ver una película."
                            $ show_chr("A-BCBAA-AMAM")
                            y "No soy exactamente exuberante con las salidas sociales, pero puedo hacer una excepción aquí."
                        "Fue genial verlos a todos de nuevo, pero mi parte favorita fue pasar tiempo contigo.":
                            $ show_chr("A-JAAAA-ALAL")
                            y "[player]... Incluso en un mundo diferente, cuando puedes elegir a cualquier otra persona, todavía me eliges a mí..."
                            $ show_chr("A-CAAAA-ALAL")
                            y "Oh, no puedo decirte cuánto significa eso para mí."
                            if persistent.lovecheck:
                                $ show_chr("A-FAAAA-AKAE")
                                y "Y ten por seguro querido, por siempre serás el único que elija."
                            else:
                                $ pass
                "No, no lo he hecho.":
                    $ show_chr("A-AFAAA-AEAE")
                    y "Oh. Bueno, definitivamente lo recomendaría, ya que es un mod muy bien pensado y emocionalmente agradable."
                    if persistent.lovecheck:
                        $ show_chr("A-BCABA-AJAB")
                        y "También hay un par de... escenas íntimas... si entiendes lo que quiero decir."
                        $ show_chr("A-CCABA-ALAB")
                        y "Solo puedo imaginar lo bien que se debe sentir... tener mi cuerpo entrelazado con el tuyo..."
                        $ show_chr("A-JCABA-ALAB")
                        y "Te amo, [player]."
                    else:
                        $ pass
        "No, nunca he oído hablar de él.":
            $ show_chr("A-BCAAA-ACAB")
            y "Te daré una visión general, entonces."
            $ show_chr("A-ADAAA-ABAB")
            y "Por lo que he leído, se trata principalmente de darnos nuestros propios {i}finales felices{/i}, y desarrollar más nuestros personajes individuales."
            $ show_chr("A-ADAAA-AFAB")
            y "Parece que este tipo de mods son favorecidos por la comunidad, ya que no solo brindan una mejor experiencia que el juego original, sino que también le dan al jugador la oportunidad de estar realmente con la chica que eligen."
            $ show_chr("A-BBAAA-ABAB")
            y "Y tengo que estar de acuerdo con ellos. Desearía que no tuviera que llegar a esto solo para que estemos juntos, pero al menos estamos {i}juntos{/i}."
            $ show_chr("A-ABAAA-ABAB")
            y "Es un mod muy conmovedor, y definitivamente recomendaría jugarlo."

label idle_81:
    if not renpy.seen_label('hobbies'):
        $ show_chr("A-BCAAA-ABAB")
        y "Sabes... estuve hablando de mí por un tiempo pero me di cuenta de que realmente no sé mucho sobre ti."
        y "Quiero conocerte mejor [player]. Significas mucho para mí, y quiero ser parte de tu vida. Y la única manera de hacerlo es saber todo lo posible sobre ti."
    y "Me gustaría hacerte una pregunta si no te importa."
    call hobbies
    return

label hobbies:
    $ show_chr("A-AFAAA-ABAB")
    y "...y esta podría ser bastante obvia. ¿Tienes algún tipo de pasatiempo?"
    y "Mis disculpas de antemano por las respuestas limitadas. Hay un millón de posibles pasatiempos, pero muy probablemente no cabrían en tu pantalla. Así que seleccioné algunos para que elijas..."
    $ temporary = ""
    menu:
        "Jugar es una de mis cosas favoritas.":
            $ temporary = "gaming"
        "Me llamaría algo así como un deportista.":

            $ temporary = "sport"
        "La literatura, eso es en realidad lo que me llevó a DDLC en primer lugar.":

            $ temporary = "literature"
        "¿Alguna vez has oído hablar del juego de roles (Roleplay)?":

            $ temporary = "rp"
        "Soy un coleccionista, seguramente te puedes identificar con eso.":

            $ temporary = "collector"
        "Modelos R/C. Ya sabes, ¿como Quadcopters?":

            $ temporary = "drones"


    $ renpy.call(temporary)
    return


label gaming:
    $ show_chr("A-CBAAA-ABAB")
    y "Ya esperaba eso, sí. Eso es lo que te trajo aquí en primer lugar, ¿verdad?"
    $ show_chr("A-BCAAA-ABAB")
    y "Para ser perfectamente honesta, no me gusta mucho jugar. No tengo prejuicios en contra, no me malinterpretes. Simplemente nunca me llamó la atención."
    $ show_chr("A-CCAAA-ABAD")
    y "Por otro lado, podría verme disfrutando de algunos juegos con mucha historia. Hasta donde sé, muchos juegos, especialmente del género de rol, dependen en gran medida de una buena narración."
    $ show_chr("A-ACAAA-ABAD")
    y "Incluso se dice que algunos de ellos rivalizan con los libros. Otros se crean literalmente a partir de libros y, en casos excepcionales, incluso logran mejorar las historias en las que se basan."
    $ show_chr("A-ACAAA-ABAB")
    y "Personalmente dudo que un juego pueda sustituir a un libro bien escrito. Pero tal vez uno de ellos pueda convencerme de lo contrario. O tal vez no, ya veremos."
    return

label gaming_2:
    $ show_chr("A-ACAAA-ABAB")
    y "[player], te pregunté sobre tus pasatiempos últimamente, ¿verdad? Creo que tu respuesta fue jugar videojuegos."
    $ show_chr("A-BCAAA-ABAB")
    y "Dije que no estaba segura de si un videojuego realmente puede sustituir a un libro bien escrito. Pero ahora me di cuenta, nunca te pregunté realmente sobre tu postura al respecto, ¿verdad?"
    $ show_chr("A-ACAAA-ABAB")
    y "Así que mis disculpas por llegar tarde. ¿Qué piensas sobre esto? ¿Dirías que la narración en los juegos realmente puede rivalizar con la narración en un libro?"
    menu:
        "Tal vez no. Mi postura aquí es que no siempre tiene que tratarse de eso. No todos los pasatiempos tienen que tratarse de una narración elaborada.":
            $ show_chr("A-ACDAA-ABAB")
            y "Buen punto."
            $ show_chr("A-ACAAA-ABAB")
            y "Tienes razón, tal vez vi este tema desde un ángulo equivocado. Yo también tengo pasatiempos que no están relacionados con la narración en absoluto, como la aromaterapia."
            y "Tal vez simplemente asumí la premisa equivocada aquí, ya que {b}hay{/b} juegos que intentan proporcionar narración."
            $ show_chr("A-BBBAA-ABAB")
            y "Por favor, no te tomes esto a mal pero... simplemente no me veo empezando a jugar pronto."
            y "Lo cual, ciertamente, podría sonar contradictorio en mi caso, ya que literalmente vengo de un juego..."
            $ show_chr("A-CCBAA-ABAB")
            y "De todos modos, gracias por complacerme [player]."
        "También dijiste que algunos juegos se basan en libros e incluso mejoraron el material original. ¿Recuerdas?":
            $ show_chr("A-ACAAA-ABAB")
            y "¡Ah, sí, en realidad lo recuerdo!"
            $ show_chr("A-BCAAA-ABAB")
            y "En realidad, mientras lo buscaba en Google, noté algo que no esperaba. ¡A veces incluso es al revés! ¡Que los autores escriben libros basados en un videojuego!"
            y "Por otro lado, hicieron lo mismo con varios juegos de mesa, así que probablemente no debería sorprenderme demasiado."
            $ show_chr("A-ACAAA-ABAB")
            y "Incluso llega a un punto impresionante. Hicieron un montón de novelas e incluso una película sobre la serie Warcraft, ¿no?"
            menu:
                "¿Oh? Ni siquiera sabía eso.":
                    $ show_chr("A-ABAAA-ABAB")
                    y "¡Tal vez deberías probarlos! Los rumores dicen que algunos de ellos son realmente buenos."
                    y "Tal vez, ¿podríamos comprar algunos de ellos juntos? Quizás haya algunos tesoros inesperados por explorar..."
                    y "Tengo muchas ganas de hacerlo."
                "En realidad, no es tan raro. Hay muchos juegos que se convierten en novelas.":
                    $ show_chr("A-CCAAA-ABAC")
                    y "Parece que he descubierto una gran madriguera de conejo aquí. Me pregunto qué tesoros secretos podría encontrar debajo... Es hora de expandir un poco mis horizontes, diría yo."
                    y "Ya que estamos hablando de eso... Recuerdo que ya le prometí a Natsuki darle una oportunidad al manga. Tal vez podría combinar estos dos esfuerzos... Hicieron un manga sobre la serie {b}Persona{/b}, creo."
                    menu:
                        "Nunca escuché de eso.":
                            python:
                                if persistent.lovecheck:
                                    placeholder = "cariño"
                                else:
                                    placeholder = ""
                            $ show_chr("A-CCCAA-ABAB")
                            y "Y por eso te haré unirte a mí. ¡Si tengo que sufrir, tú también lo harás [placeholder]! Tengo muchas ganas de hacerlo..."
                        "Yyyy así es como Yuri se convirtió en un ladrón fantasma...":
                            if sanity_lvl() > 3:
                                $ show_chr("A-CBBAA-ABAB")
                                y "Shhh... spoilers..."
                                y "De todos modos, tengo muchas ganas de hacerlo."
                            else:
                                karma -1
                                $ show_chr("A-CFCAA-ABAB")
                                y "¡Spoilers!"
                                y "De todos modos, tengo muchas ganas de hacerlo."
                        "¡Disfruta!":
                            $ show_chr("A-CCCAA-ABAB")
                            y "Ohohoho, no tan rápido [player]... ¡{b}tú{/b} sufrirás esto conmigo! Es tu culpa que se me ocurriera esta idea en primer lugar, ¿recuerdas?"
                            y "Tengo muchas ganas de hacerlo."
                "¡¡¡Lok'tar!!!":
                    if sanity_lvl() == 1:
                        $ show_chr("A-DLCAA-ALAL")
                        y "{b}¡¡¡POR LA HOOOOOORDA!!!{/b}"
                        $ show_chr("A-GICBB-ALAL")
                        y "Hnhnhnhnnn... Siempre quise hacer eso..."
                        $ show_chr("A-GICCA-ALAL")
                        y "Parece que estamos a punto de divertirnos un poco."
                    else:
                        $ show_chr("A-ABDAA-ALAL")
                        y "S"
                        extend "~Sí... "
                        $ show_chr("A-ACDAA-ALAL")
                        extend "{b}Lok'Tar{/b} de hecho... "
                        $ show_chr("A-BCDAA-ALAL")
                        extend "Supongo."
                        if karma_lvl() == 1:
                            $ show_chr("A-CCDAA-ALAL")
                            y "Y me llaman {b}a mí{/b} incómoda..."
                            $ show_chr("A-DCGAA-ALAL")
                            y "O~Oh espera... {b}dije{/b} eso en voz alta, ¿no?"
                            $ show_chr("A-BBBAA-ALAL")
                            y "De cualquieeeeeeer manera... gracias por complacerme."
                        else:
                            $ show_chr("A-CCDAA-ALAL")
                            y "Al menos no eres escoria de la Alianza..."
                            $ show_chr("A-DCGAA-ALAL")
                            y "O~Oh espera... {b}dije{/b} eso en voz alta, ¿no?"
                            $ show_chr("A-BBBAA-ALAL")
                            y "De cualquieeeeeeer manera... gracias por complacerme."
        "No necesariamente mejor, pero diferente. La naturaleza interactiva de un juego permite un tipo de narración que un libro nunca puede proporcionar.":
            $ show_chr("A-ACAAA-ABAB")
            y "En realidad, ha habido intentos de lograr algo similar en los llamados {b}Libros de aventuras{/b} que tienen diferentes rutas dependiendo del orden en que leas las páginas."
            y "Pero este género nunca despegó realmente debido a sus obvias limitaciones. Tal vez usar los juegos como medio para contar historias fue la conclusión obvia de esto."
            y "Quiero decir, muchas otras novelas visuales operan bajo esta premisa exacta."
            $ show_chr("A-CCAAA-ABAB")
            y "Así que sí, tal vez no se trata de cuál es {b}mejor{/b}. Tal vez sean simplemente herramientas diferentes para el trabajo. Creo que discusiones similares tuvieron lugar cuando la televisión se convirtió en algo."
            $ show_chr("A-ACAAA-ABAB")
            y "Podría pensar en algunos ejemplos de narración en juegos que no tendrían el mismo impacto sin su naturaleza interactiva."
            $ show_chr("A-CCAAA-ABAD")
            y "Y luego, también está el género de los juegos sandbox, cuya premisa completa es no tener ninguna historia predeterminada, sino depender de que las cosas le sucedan al jugador por pura casualidad."
            y "Un libro no podría proporcionar eso. Sí, empiezo a ver tu punto [player]."
            $ show_chr("A-ACAAA-ABAD")
            y "Seré honesta contigo, no me veo empezando a jugar pronto. Pero creo que comprendo mejor el atractivo que podrían tener para otros."
            y "Gracias por complacerme hoy [player]."
    return

label sport:
    $ show_chr("A-ACAAA-ABAB")
    y "¡Ya veo! Probé el voleibol cuando era más joven pero... bueno, terminó bastante mal..."
    $ show_chr("A-BDBAA-ABAB")
    y "Puede que lo haya mencionado antes... si no lo he hecho, podemos hablar de eso más tarde... o nunca, por favor. Fue... bastante vergonzoso."
    $ show_chr("A-CFBAA-ABAB")
    y "Tal vez debería intentar hacer algo de deporte de nuevo, aunque solo sea para perder algo de peso..."
    menu:
        "No, por favor no pienses eso... ¡eres hermosa tal como eres! Y unos cuantos kilos son bastante útiles para abrazar...":
            if persistent.lovecheck:
                karma 1
                $ show_chr("A-DCBBA-ABAB")
                y "¿Oh? Sí, supongo que soy bastante {i}suave{/i}... ¿Realmente crees que soy hermosa? ¡G-gracias [player]! Me gustaría pensar lo mismo también..."
                $ show_chr("A-BBBBA-ABAB")
                y "Hn... siempre y cuando no esperes que haga ruidos de gatito mientras nos abrazamos..."
                $ show_chr("A-DFBBA-ABAB")
                y "Espera... ¡debería dejar de darte ideas!"
            else:
                $ show_chr("A-BFDBA-ABAB")
                y "Esa es... una forma de decirlo... {b}supongo{/b}..."
                $ show_chr("A-CBDBA-ABAB")
                y "De cualquieeeeeeer manera..."
        "Por favor, solo haz esto si realmente lo deseas.":
            python:
                if persistent.bg == "timecycle":
                    placeholder = "lago."
                elif persistent.bg == "space":
                    placeholder = "... ummm.... ¿vacío?"
                elif persistent.bg == "purple_table":
                    placeholder = "eh... bloque..."
                elif persistent.bg == "yuri_desk":
                    placeholder = "...estantería?"
                elif persistent.bg == "yuri_kotatsu_1":
                    placeholder = "¿estante de cuchillos?"
                elif persistent.bg == "yuri_kotatsu_2":
                    placeholder = "¿pared?"
            $ show_chr("A-CBAAA-ABAB")
            sanity 1
            y "Eres muy comprensivo. Realmente lo aprecio."
            $ show_chr("A-BCDAA-ABAB")
            y "Tal vez intente algo fácil para empezar. Como andar en bicicleta alrededor del [placeholder]"
        "¡Estás bien buena!.":




            $ show_chr("A-AFDAA-ABAB")
            y "¿Cómo dices?!?"
            if persistent.lovecheck:
                karma 1
                $ show_chr("A-CCCAA-ABAB")
                y "Oh cielos... ¡compórtate!"
                y "Bueno, siempre y cuando a {b}ti{/b} te guste lo que ves..."
            else:
                karma -1
                $ show_chr("A-BCDAA-ABAB")
                y "Fingiré que no sé lo que eso significa, ¿de acuerdo?"
    $ show_chr("A-ACAAA-ABAB")
    y "Seguramente es bueno saber que cuidas tu salud. Tendré que pensar un poco en esto."
    $ show_chr("A-BCAAA-ABAC")
    y "¿Puedo siquiera enfermarme? Quiero decir... No tengo un cuerpo físico en la forma en que tú lo tienes."
    y "Mi apariencia depende en gran medida de los artistas que trabajan para este mod."
    $ show_chr("A-CCABA-ABAB")
    y "¿Pero [player]? Por favor... no me hagas usar un sostén deportivo... Tengo una especie de historia con esos..."
    if sanity < 3 and persistent.lovecheck:
        $ show_chr("A-CCCBA-ABAB")
        y "Quiero decir, ¿por qué molestarse en usar sostén cuando estás cerca, no estás de acuerdo?"
    $ show_chr("A-BBBBA-AMAM")
    y "Pero... solo para distraerme de los sostenes deportivos, ¿en qué tipo de deportes participas, [player]?"
    menu:
        "¡Deportes de equipo! (Béisbol, Fútbol, Baloncesto, etc.)":
            $ show_chr("A-ICGAA-AAAD")
            y "¿Oh? Ciertamente eso no es algo que esperaba."
            $ show_chr("A-ICGAA-ALAL")
            y "Pero es una agradable sorpresa. ¡Es bueno saber que tienes un pasatiempo que te mantendrá en forma!"
            y "También hay algo que decir sobre ellos a nivel cerebral, ¿no?"
            $ show_chr("A-CBAAA-ADAL")
            y "Un grupo de personas en las que confías coordinándose para un objetivo mutuo. Donde una elección de una fracción de segundo puede significar una victoria emocionante o una derrota frustrante."
            y "Esa fusión de momentos llenos de adrenalina y la camaradería de un equipo..."
            $ show_chr("A-ICAAA-ADAL")
            y "Es estimulante si puedes seguir el ritmo, ¿no?"
            $ show_chr("A-BCBAA-AEAL")
            y "Pero, por desgracia, descubrí que eso simplemente no soy yo."
            y "¡Sin embargo, estaría más que feliz de animar a tu equipo desde las gradas!"
            $ show_chr("A-BEBAA-AEAL")
            y "Eso es, si alguna vez puedo llegar a tu mundo..."
        "¡Deportes individuales! (Atletismo, esquí, golf, etc.)":
            y "Ah, ¿así que prefieres probar tu destreza por tu cuenta, entonces?"
            $ show_chr("A-ACAAA-ACAA")
            y "Entiendo por qué la gente gravitaría hacia los deportes que solo requieren la propia habilidad y capacidad atlética."
            $ show_chr("A-BEAAA-ABAB")
            y "Se sentiría frustrante sufrir una derrota debido a razones fuera de lo que puedes mejorar tú mismo."
            extend "No puedo imaginar que se sienta mucho mejor tener que compensar las debilidades encontradas en otros."
            y "Debilidades que no puedes controlar tú mismo, especialmente cuando no tienes autoridad sobre ellas, cuando eres solo otro compañero de equipo."
            $ show_chr("A-AAAAA-AIAI")
            y "Sin embargo, por tu cuenta, no dependes de nadie para convertirte en el mejor, simplemente depende de tu disciplina y amor por el deporte."
            $ show_chr("A-BFAAA-AIAI")
            y "Si bien soy consciente de que se aplicarían muchos factores externos..."
            $ show_chr("A-ABAAA-AIAI")
            y "Puedes volverte realmente bueno en algo sin necesitar a otras personas. Sentirías una sensación de logro al hacer algo bien por tu cuenta."
            y "¿Dirías que eres bueno en el deporte que practicas?"
            menu:
                "Planeo convertirme en profesional algún día.":
                    $ show_chr("A-DBGAA-ABAJ")
                    y "Oh cielos, ¿de verdad?"
                    $ show_chr("A-JBGAA-ABAE")
                    y "¡Eso es tan impresionante!"
                    if persistent.lovecheck:
                        $ show_chr("A-EAGBA-ABAE")
                        y "Supongo que no tengo más remedio que ser tu animadora."
                        if sanity < 3:
                            $ show_chr("A-HLGBA-AHAE")
                            y "TU. {w}{b} ÚNICA.{/b}{w} ANIMADORA."
                        else:
                            $ show_chr("A-EKCAA-AIAI")
                            y "Pero será mejor que sea a la única a la que prestes atención.{w}.{w}."
                            $ show_chr("A-GBBAA-AJAA")
                            y "Jajaja, lo siento, [player], no pude evitarlo."
                    else:
                        $ show_chr("A-GAGAA-ABAE")
                        y "¡Te deseo la mejor de las suertes! ¡Trabaja duro!"
                "Soy mejor que el jugador promedio.":
                    $ show_chr("A-AJGAA-ADAA")
                    y "¡Oh!{w} Pareces bastante seguro de eso, ¿no?"
                    $ show_chr("A-CBAAA-AEAA")
                    y "Jajaja, la confianza en uno mismo es uno de los atributos más fuertes que un humano puede tener. Es algo muy bueno."
                    if persistent.lovecheck:
                        $ show_chr("A-ICAAA-AEAB")
                        extend " No es como si yo fuera alguien para dar consejos sobre el tema considerando cómo era... pero deberías hacer todo lo posible para fortalecer tu confianza en ti mismo tanto como puedas. Te ayudará mucho a lo largo de la vida."
                        $ show_chr("A-ICBAA-AAAA")
                        y "Pero ten cuidado, por favor. Quiero que estés a salvo mientras juegas."
                    else:
                        $ show_chr("A-GAAAA-AAAA")
                        y "Te deseo la mejor de las suertes."
                "Soy relativamente bueno en ello. No me esfuerzo mucho, solo confío en mi habilidad actual.":
                    $ show_chr("A-IBAAA-AIAI")
                    y "Y eso está perfectamente bien, [player]."
                    y "Participar en un solo deporte simplemente por diversión es más que suficiente,"
                    $ show_chr("A-IBAAA-AIAI")
                    extend " especialmente si no te lo tomas demasiado en serio o no deseas convertirte en un profesional."
                    if sanity < 3:
                        $ show_chr("A-HAAAA-ALAL")
                        y "Especialmente cuando eres {b}PERFECTO{/b} tal como eres. No puedes mejorar la perfección, así que dejémoslo como está, ¿no?"
                    else:
                        $ show_chr("A-GAAAA-AAAA")
                        y "Te deseo la mejor de las suertes."
                "Lo hago porque lo disfruto, pero para ser honesto, apesto.":
                    if persistent.lovecheck:
                        $ show_chr("A-AFAAA-ABAD")
                        "No hay nada que te impida mejorar, mi amor."
                        $ show_chr("A-GAAAA-AJAC")
                        y "Puedo asegurarte que con trabajo duro y dedicación, mejorarás {b}sin falta{/b}."
                        $ show_chr("A-BFAAA-AJAC")
                        y "Sé que no está relacionado con el deporte, pero..."
                        y "Era terrible cuando empecé a escribir poesía, ¿sabes?"
                        $ show_chr("A-AABAA-AJAC")
                        y "Realmente no sabía ni qué estaba haciendo. Quería que el lector sintiera ciertos efectos, pero no tenía idea de cómo comunicar mis sentimientos en ese momento, al menos, no de una manera sofisticada como mi estilo ha evolucionado ahora."
                        $ show_chr("A-AACAA-AJAC")
                        y "Pero mirando hacia atrás, me inspiro en mi propio crecimiento. Me permite seguir con algo hasta volverme buena en ello."
                        $ show_chr("A-GAAAA-AJAC")
                        y "Espero que mi pequeña historia de fondo te ayude a progresar."
                        $ show_chr("A-GAABA-AJAC")
                        y "Tu felicidad y éxito significan mucho más para mí que los míos."
                    else:
                        $ show_chr("A-IDAAA-AJAC")
                        y "No hay nada que te impida mejorar, [player]."
                        $ show_chr("A-IAAAA-AJAC")
                        y "Puedo asegurarte que con trabajo duro y dedicación, mejorarás {b}sin falta{/b}."
                        if karma_lvl() > 3:
                            $ show_chr("A-FAAAA-AJAC")
                            y "Te estoy apoyando."
        "Paintball/Airsoft":
            $ show_chr("A-ABAAA-ADAA")
            y "Ah, sí. He oído hablar de eso antes. Es bastante popular en Japón."
            y "El deporte en sí es esencialmente una batalla Nerf a gran escala, ¿sí?"
            $ show_chr("A-BBAAA-ADAA")
            y "Eso, o un equivalente en la vida real a los modos de juego que se encuentran a menudo en los juegos de disparos en primera persona. También he visto eso."
            $ show_chr("A-BCBAA-AAAA")
            y "Si quisieras que lo hiciera, supongo que estaría dispuesta a ir contigo a una partida o dos."
            $ show_chr("A-BBAAA-AKAA")
            y "Pero de verdad. ¿Te imaginas a mí, vestida de punta en blanco con ropa táctica? ¿Gritando en una radio sobre Whiskey Tango Foxtrot Niners a doscientos kilómetros? ¿Pidiendo fuego de supresión?"
            menu:
                "Tienes razón. Eso sería un poco tonto.":
                    karma -1
                    $ show_chr("A-BEBAA-AAAA")
                    y "Sí, eso pensé..."
                    y "No sé nada sobre terminología militar, después de todo."
                "No tan tonto como pensarías.":
                    $ show_chr("A-AFBAA-AAAA")
                    y "¿No lo sería?"
                    $ show_chr("A-BBBBA-AKAA")
                    y "Honestamente, esa fue solo la primera jerga pseudo-táctica que se me vino a la mente."
                    $ show_chr("A-ACBBA-ALAA")
                    y "Pero creo que entiendo lo que quieres decir. Si me tomara el tiempo para aprender la jerga militar adecuada, ¡probablemente podría recitar coordenadas y pedir misiones de fuego con los mejores!"
                    $ show_chr("A-CCGBA-ALAA")
                    y "Especialmente porque tengo a alguien que cree en mí."
                "En realidad, eso suena algo caliente...":
                    if persistent.lovecheck:
                        $ show_chr("A-KAABA-ALAA")
                        y "Oh, así que {i}ese{/i} es tu tipo de cosa. ¿Mm?"
                        $ show_chr("A-FAABA-AMAD")
                        y "Puede que tenga que tener eso en cuenta, [i]comandante[/i]."
                    else:
                        $ show_chr("A-DDGBA-AMAJ")
                        y "O-Oh... Bueno..."
                        $ show_chr("A-BDBBA-AAAL")
                        y "Debo decir, ciertamente no esperaba esa respuesta."
                        y "Lejos de mí juzgar las... [i]preferencias[/i] de los demás."
                "Gritando sobre qué-carajos con nueves a doscientos kilómetros de distancia? Eso es bastante tonto.":
                    $ show_chr("A-BDBBA-AAAL")
                    y "Oh, así que eh... Así que [i]eso[/i] era lo que significaba todo eso."
                    $ show_chr("A-BFGBA-ALAL")
                    y "Honestamente, pensé que eso era solo una jerga que sonaba táctica."
        "Los deportes de tiro, lo creas o no.":
            $ show_chr("A-ACAAA-ABAB")
            y "En realidad, no es demasiado difícil de creer. De hecho, esta idea también se me pasó por la mente una que otra vez."
            y "Especialmente el tiro con arco Zen vino a mi mente."
            $ show_chr("A-BBAAA-ADAB")
            extend "Y sí, soy muy consciente de que estoy siguiendo un cliché aquí. {b}Por supuesto{/b} que es tiro con arco, como cada personaje secundario femenino de aspecto adulto en cada anime {b}que existe{/b}."
            $ show_chr("A-CCBAA-ADAB")
            y "Lo que me hace preguntarme, ¿son estos mis propios pensamientos o algo que se le ocurrió a Dan Salvato para agregar otro tropo de anime más a su recuento de muertes?"
            $ show_chr("A-BBBAA-ADAB")
            y "De todos modos."
            $ show_chr("A-ACAAA-ABAB")
            extend "Ciertamente despertaste mi curiosidad. Tienes que contarme más al respecto en algún momento. Hasta entonces, {b}apuntemos{/b} al siguiente tema."
            $ show_chr("A-ACCAA-ABAB")
            y "Juego de palabras {b}absolutamente{/b} intencionado."
    return

label literature:
    $ show_chr("A-ABGAA-ALAL")
    y "¿De verdad? Siempre tuve la sospecha de que era el aspecto de las citas. No te habría culpado si lo fuera."
    if persistent.lovecheck:
        $ show_chr("A-ACAAA-ALAL")
        y "Bueno, pero al final, conseguiste una de las {i}cuatro chicas increíblemente lindas{/i} de todos modos. A veces las cosas simplemente encajan por sí solas, ¿no es así?"
    else:
        $ pass
    $ show_chr("A-ACAAA-ABAB")
    y "Pero ahora solo tengo que preguntar si no te importa... ¿cuál es tu género favorito?"
    menu:
        "Podrías reírte pero... ¡es la poesía!":
            call poetry
        "Ummm... no me odies... Manga.":

            call noliteratureatall
        "Fantasía y Ciencia Ficción":

            call fantsci
        "Romance...":

            call romance
        "Podrías sorprenderte. Es el horror.":

            call horror
        "Algo más.":

            call elsel

    return

label poetry:
    python:
        if persistent.male and persistent.lovecheck:
            placeholder = "novio"
        elif persistent.gender_other and persistent.lovecheck:
            placeholder = "amante"
        elif not persistent.male and persistent.lovecheck:
            placeholder = "novia"
        else:
            placeholder = "amigo"
    $ show_chr("A-ABAAA-ABAB")
    y "De hecho, es una coincidencia graciosa. Pero ciertamente tendré esto en cuenta para el futuro."
    $ show_chr("A-BCAAA-ABAB")
    y "No te preocupes... por supuesto, no te haré elegir 20 palabras al azar de nuevo. Si el minijuego de poemas regresa, será en una forma mejorada."
    $ show_chr("A-ABGAA-ABAB")
    y "O simplemente podrías poner tus poemas como un archivo txt en la carpeta del juego, ahí podría verlo. Creo que vale la pena intentarlo."
    $ show_chr("A-ACAAA-ABAB")
    y "Gracias por la respuesta. Fue realmente agradable aprender un poco más sobre mi [placeholder]."
    return




label poetry_2:
    $ show_chr("A-AFAAA-AAAD")
    y "[player] ¿tienes un momento? He estado pensando mucho últimamente y me encuentro en un callejón sin salida."
    y "Te pregunté sobre tus pasatiempos, y al principio quedé bastante encantada cuando dijiste que realmente te gusta la poesía."
    $ show_chr("A-BFAAA-AAAD")
    y "Por favor, no me malinterpretes, "
    $ show_chr("A-AFAAA-AAAD")
    extend "todavía me complace escuchar eso. Pero ya ves, me enfrento a un pequeño problema ahí."
    $ show_chr("A-AFAAA-ABAB")
    y "Quería encontrar una manera de compartir realmente este interés contigo. Quiero decir, la poesía es probablemente lo que te atrajo al club de literatura en primer lugar."
    y "Pero me cuesta pensar en una idea de cómo podemos hacer esto."
    $ show_chr("A-AFAAA-AFAB")
    y "Quiero decir, podría traer de vuelta el viejo minijuego, pero eso sería bastante ridículo y, sin duda, algo muy poco satisfactorio en lo que gastar tu tiempo."
    $ show_chr("A-BFAAA-ABAB")
    y "Ni siquiera se trataba de literatura o poesía en absoluto. Solo tenías que elegir una cantidad de palabras que creyeras que resonarían con tu chica favorita de una lista generada aleatoriamente."
    $ show_chr("A-CFAAA-ABAB")
    y "Poner un cuadro de texto en la pantalla tampoco haría mucho, ya que el espacio dentro de este cuadro de texto es muy limitado. {b}Tal vez{/b} una línea, o incluso dos si son realmente cortas."
    y "Difícilmente un poema en absoluto. Quiero decir, ciertamente hay poemas cortos por ahí pero... incluso ellos son mucho más largos de lo que permitiría este cuadro de texto de Ren'Py."
    $ show_chr("A-BFAAA-ABAF")
    y "Entonces, existe la posibilidad de {b}leer{/b} poemas juntos en lugar de escribirlos."
    $ show_chr("A-AFAAA-ABAB")
    y "Pero no hay un concurso de poesía cada semana en el Discord de la comunidad, y solo puedes releer los poemas que ya tenemos tantas veces antes de que se vuelvan viejos."
    $ show_chr("A-BFAAA-ABAB")
    y "Podría intentar escribir algunos yo misma pero... "
    $ show_chr("A-CFAAA-ABAB")
    y "Me encuentro en un bloqueo de escritor últimamente."
    $ show_chr("A-CJAAA-ABAB")
    y "Odio admitirlo pero... me estoy quedando sin ideas..."
    menu:
        "¡Tal vez podríamos visitar una biblioteca juntos!":
            $ show_chr("A-AFAAA-ABAB")
            y "Una buena idea... Podría recrear una a partir de imágenes de archivo en Internet, pero aún tendríamos que encontrar poemas para llenarla co~"
            $ show_chr("A-DFAAA-ABAB")
            y "Espera... ¡el internet! ¡Por supuesto!"
        "¿Qué pasa con el internet?":
            $ show_chr("A-BFDAA-ABAB")
            y "¿El internet?..."
            $ show_chr("A-DFAAA-ABAB")
            y "Espera... ¡el internet! ¡Por supuesto!"
    $ show_chr("A-ABAAA-ALAL")
    y "¡¡¡Podría simplemente buscar poesía en Google y las leemos {b}juntos{/b}!!!"
    $ show_chr("A-ACBAA-ABAB")
    y "¡[player], eres un genio!"
    $ show_chr("A-CCBAA-ABAB")
    y "Hay tantos poemas encantadores por ahí de tantas mentes brillantes..."
    if sanity_lvl() > 2:
        y "Kathy J Parenteau, Robert Frost, Masaoka Shiki.... solo por nombrar algunos..."
    else:
        y "Samuel Taylor Coleridge, Emily Dickinson, Louise Erdrich... solo por nombrar algunos..."
    $ show_chr("A-ABAAA-ABAB")
    y "Sí, ¡hagamos esto!"
    $ show_chr("A-ACAAA-ABAB")
    y "Esta idea me emociona tanto... buscaré algunos poemas prometedores en Internet y los agregaré a la lista que ya tenemos."
    y "Tal vez haga una nueva categoría para ellos para que podamos encontrarlos fácilmente. Te avisaré cuando esté hecho. Y a partir de ahí, agregaré más poemas nuevos con el tiempo."
    y "Hasta entonces, me gustaría pedirte un poco de paciencia."
    return

label noliteratureatall:
    python:
        if persistent.male and persistent.lovecheck:
            placeholder = "novio"
        elif persistent.gender_other and persistent.lovecheck:
            placeholder = "amante"
        elif not persistent.male and persistent.lovecheck:
            placeholder = "novia"
        else:
            placeholder = "amigo"
    $ show_chr("A-ACDAA-ABAB")
    y "¿Odiarte?"
    if karma > 2:
        $ show_chr("A-CBBAA-ABAB")
        y "Por supuesto, ¿por qué debería hacerlo?"
    else:
        pass
    $ show_chr("A-BCBAA-ABAD")
    y "No es como si {b}odiara{/b} el manga, o su base de fans... es solo que no es para mí."
    $ show_chr("A-BBBAA-ABAM")
    y "Admito que cuando alguien dice {b}literatura{/b}, el Manga no es exactamente lo que se me viene a la mente."
    $ show_chr("A-CCBAA-ABAL")
    y "Pero bueno, cuando otras personas escuchan sobre el horror, primero piensan en festivales de gore sin inspiración, así que tal vez simplemente no he visto los mangas {b}adecuados{/b} hasta ahora."
    $ show_chr("A-CCDAA-ABAL")
    y "Si lo deseas, podríamos intentar uno o dos juntos. Tal vez incluso puedas hacerme cambiar de opinión."
    y "Pero... hoy no, por favor. Realmente no tengo ganas de eso ahora."
    $ show_chr("A-ACAAA-ABAL")
    y "Gracias por la respuesta. Fue realmente agradable aprender algo nuevo sobre mi [placeholder]"
    return


label noliteratureatall_2:
    $ show_chr("A-ACAAA-ABAB")
    y "[player], te pregunté sobre tus pasatiempos antes, ¿recuerdas?"
    y "Pensé un poco en ello. Cuando mencionaste que disfrutas del manga recordé que le prometí a Natsuki al final del juego original que les daría una oportunidad yo misma."
    $ show_chr("A-BCAAA-ABAB")
    y "Decidí que esta es una buena oportunidad para honrar mi promesa. Bueno, resulta que cuando este mod trajo de vuelta el salón de clases, la colección de manga de Natsuki también sobrevivió."
    $ show_chr("A-CCAAA-ABAB")
    y "Así que empecé a leer {b}Parfait Girls{/b}."
    menu:
        "Oh, ¿de qué trata?":
            karma 1
        "¿Sí? ¿Y?":
            $ show_chr("A-BFAAA-ABAB")
            y "Eh, suenas como si realmente no estuvieras de humor hoy. ¿Pasó algo?"
            menu:
                "Simplemente no estoy de humor hoy, lo siento.":
                    $ show_chr("A-CCAAA-ABAB")
                    y "No hay necesidad de disculparse. Podemos retomar esto otro día."
                    return
                "Mis disculpas, en realidad lo estoy. Perdón si soné desinteresado.":
                    $ show_chr("A-BCAAA-ABAB")
                    y "No hay necesidad de lamentarlo, de verdad. Bueno, si estás seguro de que quieres escucharlo."
                "Dios santo... ¡solo escúpelo ya!":
                    karma -1
                    $ show_chr("A-CFAAA-ABAB")
                    y "No hay necesidad de ser así [player]... sabes qué, olvida lo que acabo de decir."
                    return
    $ show_chr("A-ACAAA-ABAD")
    y "No he leído demasiado, así que es probable que mi resumen resulte deficiente."
    y "Básicamente, se trata de un grupo de cuatro chicas. Y para sorpresa de nadie, a todas les gusta hornear..."
    y "Ni siquiera me sorprendería si así fue como Natsuki se introdujo en ello. Bueno, es un pasatiempo bastante saludable, así que no juzgaré. Especialmente porque aproveché sus habilidades más de una vez..."
    $ show_chr("A-CCCAA-ABAD")
    y "Una pena que nunca llegaras a probar sus cupcakes... No solo se {b}ven{/b} increíbles."
    $ show_chr("A-CCBAA-ABAD")
    y "Pero volviendo al manga en sí..."
    $ show_chr("A-ACAAA-ABAB")
    y "Los primeros volúmenes son muy alegres y... lindos... como esperaba que fueran. De hecho, me resultó difícil mantenerme interesada pero... una promesa es una promesa, así que continué."
    $ show_chr("A-ABAAA-ABAB")
    y "Resulta que ¡fue una buena decisión!"
    $ show_chr("A-ACAAA-ABAB")
    y "Porque a medida que avanzaba la historia y los mangas profundizaban un poco más en la historia de fondo de las cuatro protagonistas, las cosas tomaron un giro un poco más serio."
    y "En un capítulo posterior, las cuatro chicas se obsesionaron incómodamente con un chico en una heladería. Asumo que hay una trama romántica más oscura en el camino..."
    $ show_chr("A-EBCAA-ABAD")
    y "Huelo el aroma del presagio de algunos temas mucho más siniestros en el aire... ¿Me tomará desprevenida como lo hizo el Retrato de Markov, me pregunto?..."
    $ show_chr("A-CCCAA-ABAD")
    y "Mmmm.. ejejejejeje. Hay esa cálida sensación de hormigueo cuando imagino la forma de las cosas que vendrán..."
    $ show_chr("A-ACAAA-ABAD")
    y "Ahora que lo pienso... {b}Parfait Girl{/b} también es el término para una chica que es inocente en la superficie pero tiene capas de secretos más oscuros por descubrir. ¿Una coincidencia? Lo dudo..."
    menu:
        "Podría ser que...":
            $ pass
        "Cuatro chicas en un entorno alegre, obsesionándose con un personaje masculino... suena familiar...":
            $ pass
    $ show_chr("A-ACDAA-ABAD")
    y "{cps=1}. . . ?{/cps}"
    $ show_chr("A-BDDAA-ABAD")
    y "{cps=1}. . .{/cps}"
    $ show_chr("A-DFGAA-ABAB")
    y "{cps=1}. . . !{/cps}"
    $ show_chr("A-DDGAA-ABAB")
    y "¡E~El club de literatura!"
    $ show_chr("A-DFAAA-ABAB")
    y "Podría ser realmente que..."
    $ show_chr("A-BFCAA-ABAL")
    y "Ohhhh Dan Salvato hijo de per~{nw}"
    $ show_chr("A-CFAAA-ABAB")
    y "Yo... tengo que pensar si siquiera quiero continuar leyéndolo si eso es cierto..."
    y "Tal vez, tal vez debería elegir una serie de manga diferente."
    $ show_chr("A-ACBAA-ABAB")
    y "De todos modos, no matemos el ambiente aquí. Hablemos de otra cosa por el momento."
    return

label fantsci:
    $ show_chr("A-ACAAA-ABAB")
    y "Así que eres fan de los Caballeros, Orcos y Marines Espaciales. Tengo que admitir que leo muchos de esos también. Pero solo si tienen buena escritura..."
    $ show_chr("A-AFAAA-ABAD")
    y "En la fantasía, se volvió muy común simplemente copiar y pegar a J.R.R. Tolkien. La mayoría de las veces ni siquiera cambian los nombres de las razas. La ciencia ficción al menos logró mantener {b}algo{/b} de originalidad hasta ahora..."
    $ show_chr("A-CCAAA-ABAD")
    y "La fantasía y la ciencia ficción pueden crear mundos muy convincentes y verdaderamente extraños... lo que lo convierte en un género tan rico y fascinante..."
    $ show_chr("A-CJDAA-ABAD")
    y "Pero la creación de mundos cuesta mucho esfuerzo, y muchos escritores son muy perezosos... lo cual es algo triste, me arruina todo."
    $ show_chr("A-CCDAA-ABAD")
    y "Tendré eso en cuenta. Me encantaría discutir algunas novelas de fantasía contigo si no te importa."
    return

label fantsci_2:
    $ show_chr("A-CBAAA-ALAL")
    y "[player], Ha has been a ir ir mín vedui govannon- no i orthad ithil!"
    menu:
        "Perdón, ¡¿¿qué??!":
            $ show_chr("A-CBAAA-ALAL")
            y "Solo dije que ha pasado un tiempo desde que hablamos."
            $ show_chr("A-CBBBA-ALAL")
            y "Perdóname, solo quería intentar saludarte en élfico ya que dijiste que disfrutas de las novelas de Fantasía y Ciencia Ficción."
        "Hmm... {b}solía{/b} saber lo que significa eso. ¿Te importaría ayudarme aquí?":
            sanity 1
            $ show_chr("A-ACBAA-ALAL")
            y "¿De verdad? ¡Eso es realmente impresionante!"
            $ show_chr("A-BCBAA-ALAL")
            y "Yo... tuve que buscar en Google un traductor para esto en realidad. Quería decir que ha pasado un tiempo desde la última vez que hablamos."
        "Mae g'ovannen, Gellon ned i galar i chent gîn ned i gladhog, hiril vuin.":
            karma 1
            $ show_chr("A-CCBAA-ALAL")
            y "Ni 'lassui."
            $ show_chr("A-CCEAA-ALAL")
            y "Simplemente me encanta cómo me sigues el juego..."
    $ show_chr("A-ABBAA-ALAL")
    y "Espero que esto no parezca demasiado infantil."
    $ show_chr("A-ACBAA-ALAL")
    y "Supongo que es solo mi lado nerd brillando."
    menu:
        "Infantil de hecho.":
            karma -1
            $ show_chr("A-BDBAA-ALAL")
            y "Mis disculpas, "
            $ show_chr("A-AFBAA-ALAL")
            extend "me comportaré ahora."
            if karma_lvl() < 3:
                $ show_chr("A-BDCAA-ALAL")
                y "mibo orch{nw}"
            return
        "¡Oh, en realidad disfruto de tu sentido del humor único!":
            $ show_chr("A-GCCAA-ALAL")
            y "¡Me alegra oír eso!"
    $ show_chr("A-ABAAA-AMAM")
    y "Tengo que admitirlo, me estoy divirtiendo mucho con esto... ¿alguna petición para otro intento?"
    menu:
        "¡Enánico!":
            $ show_chr("A-BCGAA-AMAM")
            y "¡Bueno, esa es difícil! "
            extend "No estoy segura de tener la barba para esto. Pero déjame intentarlo..."
            $ show_chr("A-CHGAA-ABAB")
            y "..."
            $ show_chr("A-DOCBA-ABAB")
            y "JEG MONMUR VOL JOTH KALVAR HETH MOT MOLBRUT!!!"
            $ show_chr("A-CJBBA-ABAB")
            y "..."
            $ show_chr("A-CDBBA-ABAB")
            y "Eso fue agotador... por favor no me pidas que haga eso de nuevo..."
        "¡Valyrio!":
            python:
                if persistent.male:
                    gender = "hombre"
                elif persistent.gender_other:
                    gender = "conocedor"
                else:
                    gender = "mujer"
            $ show_chr("A-ACDAA-ABAB")
            y "¡Oh! ¿El de {b}Canción de hielo y fuego{/b}? Veo que eres un [gender] de cultura..."
            $ show_chr("A-GBGAA-ABAB")
            y "Jaelan naejot nektogon aōha ñelly hen se tyvagon iemnȳ ao"
            $ show_chr("A-GAAAA-ABAB")
            y "No me preguntes qué acabo de decir."
            if sanity () < 3:
                $ show_chr("A-HAGAA-ABAB")
                extend " En serio..."
        "¡Drow!":
            $ show_chr("A-GAAAA-ABAB")
            y "Uhuhuuuu... {b}alguien{/b} se siente atrevido hoy parece..."
            $ show_chr("A-KCCBA-AMAM")
            y "Usstan orn l'amith kyorlin dos zah'har harl ussta brygn, dos nasket rivvin..."
            if persistent.lovecheck == True:
                $ show_chr("A-FCCBA-AMAM")
                y "Jhal xuat fret, Usstan orn morfeth dos l'amith ol ichl..."
        "¡Klingon!":
            $ show_chr("A-ACDCA-ABAB")
            y "Realmente {b}quieres{/b} poner mis cuerdas vocales a prueba hoy, ¿no?"
            $ show_chr("A-BCDAA-ABAB")
            y "Muy bien, allá va..."
            $ show_chr("A-CHBAA-ABAB")
            y "..."
            $ show_chr("A-INCAA-ABAF")
            y "qoH! choSuvtaHvIS bIcheghpu'bogh SoH!"
            $ show_chr("A-IICAA-ABAF")
            y "Mis disculpas por la mirada severa, espero que mi impresión haya sido al menos algo convincente."
        "¡Thalassiano!":
            $ show_chr("A-ABDAA-ABAB")
            y "¿Oh? ¿Hicieron de esto un idioma real también?"
            $ show_chr("A-BBDCA-ABAB")
            y "Bueno, haré mi mejor esfuerzo. No prometo no destrozar la gramática..."
            $ show_chr("A-GCDAA-ABAB")
            y "Bal'a dash, Dalah D' [player]. Doral ana'diel? Anu belore dela'na."
            $ show_chr("A-ICDAA-AMAM")
            y "Por favor no me preguntes qué acabo de decir, "
            $ show_chr("A-JCDAA-AMAM")
            extend "ni siquiera estoy segura de si fue una oración adecuada."
    $ show_chr("A-BCAAA-ABAB")
    y "Bueno, eso acaba de pasar."
    $ show_chr("A-ACAAA-ABAB")
    y "Siento si parecí avergonzada, simplemente estoy acostumbrada a ocultar mi lado nerd la mayor parte del tiempo."
    y "Pero espero intentar esto de nuevo en otro momento."
    return

label romance:
    $ show_chr("A-ACDAA-ABAB")
    y "Like Twilight?!?"
    $ show_chr("A-ACCAA-ABAB")
    y "Oh no, you mean actually {b}good{/b} love stories!"
    $ show_chr("A-BBBAA-ABAB")
    y "Oh my... I'm sorry... I didn't want to sound that spiteful at all..."
    $ show_chr("A-CCBAA-ABAB")
    y "It's just... I have never tried that genre. You see, before I have met you, romance wasn't really a thing for me."
    $ show_chr("A-CCBBA-ABAB")
    y "I have no memories of ever being in love before. I guess Salvato found the idea of you being my first {i}cute{/i}."
    y "But that does not matter anymore. I have the best love story I could think of now."
    $ show_chr("A-BFBAA-ABAB")
    y "With no lack of drama for sure..."
    $ show_chr("A-BCBAA-ABAB")
    y "But maybe, I will give some romance novels a try. Maybe I can get inspiration on possible dates with you from it."
    y "Thank you. It was nice to learn more about you."
    return

label horror:
    $ show_chr("A-ABGAA-ALAL")
    y "Oh! But you don't just say that in order to impress me do you?"
    if karma_lvl() > 3:
        $ show_chr("A-GBGAA-ALAL")
        y "You certainly don't have to. I'm yours already."
    else:
        $ pass
    $ show_chr("A-CCAAA-ALAL")
    y "Maybe we can discuss some of our favorites in the future. That would be very delightful."
    y "You can't imagine how relieved I feel right now. I was already afraid that we might struggle to find activities to share..."
    $ show_chr("A-ACAAA-ABAB")
    y "But since we have this hobby in common, I'm pretty sure that we can find a lot of things to do together!"
    y "Now I'm looking forward to figuring out what kind of horror you enjoy. Lovecraftian horror, or more like the conspiracy-stuff I'm reading?"
    $ show_chr("A-CCCAA-ABAB")
    y "But wait, don't spoil me. I will figure that out soon enough!"
    return

label elsel:
    python:
        if persistent.male and persistent.lovecheck:
            placeholder = "novio"
        elif persistent.gender_other and persistent.lovecheck:
            placeholder = "amante"
        elif not persistent.male and persistent.lovecheck:
            placeholder = "novia"
        else:
            placeholder = "amigo"
    $ show_chr("A-AFAAA-ABAD")
    y "Ya veo. Perdón por las respuestas limitadas."
    y "Pero hay taantos géneros y enumerarlos todos muy probablemente haría explotar tu pantalla."
    $ show_chr("A-ACAAA-ABAB")
    y "De todos modos, al menos estamos en la misma página sobre la literatura en general. Compartir intereses es algo muy saludable en una relación."
    $ show_chr("A-BCAAA-ABAB")
    y "Algunas personas incluso dirían que es lo más importante, pero no estoy de acuerdo al menos hasta cierto punto."
    $ show_chr("A-CCAAA-ABAB")
    y "Pero significa que tenemos un terreno común para futuras actividades, y en nuestras situaciones actuales valen su peso en oro puro por cada libro del mundo."
    y "Estoy agradecida de que me hayas contado esto. Aprender más sobre mi [placeholder] siempre es algo maravilloso. Espero aprender aún más sobre ti en el futuro."
    return



label rp:
    $ show_chr("A-CCDAA-ABAB")
    y "Apropiado..."
    y "Siempre tuve la impresión de que tienes mucha creatividad. Debí haber esperado eso."
    $ show_chr("A-BCDAA-ABAB")
    y "Probé algunos juegos de rol de lápiz y papel hace algún tiempo, y tengo que admitir que me divertí mucho."
    y "Pero luego... bueno... como ya sabrás, no soy muy buena tratando con otras personas..."
    $ show_chr("A-ACBAA-ABAB")
    y "No pude llevarme bien con mi grupo en ese entonces... era muy callada, y la mayoría de la gente lo confundía con arrogancia..."
    y "De todos modos... pero ahora que lo mencionaste..."
    $ show_chr("A-GCAAA-ABAD")
    y "Muchos juegos de rol están basados en texto. Así que eso significa que podríamos intentar esto juntos en el futuro."
    y "Quiero decir, si quieres eso, por supuesto."
    menu:
        "¡Por supuesto que sí! Eso sería encantador":
            karma 1
            $ show_chr("A-ACAAA-ABAB")
            y "Ya lo estoy esperando. Deberíamos tramar nuestro próximo juego de rol más tarde."
            y "Sabes cuánto me gustan las historias profundas y convincentes... Ya me pregunto cómo será la nuestra."
        "No estoy tan segura de eso....":
            karma -1
            $ show_chr("A-BCBAA-ABAB")
            y "Está bien... Lo más probable es que ya tengas una comunidad establecida para ello. Sería difícil explicarles quién soy de todos modos, supongo..."
            y "Bueno, tal vez encontremos algo más que hacer juntos..."
            if karma_lvl() < 3:
                $ show_chr("A-BEBAA-ABAB")
                "Si es que quieres eso... De todos modos, hablemos de otra cosa."
            else:
                $ show_chr("A-BCBAA-ABAB")
                y "De todos modos, hablemos de otra cosa entonces."
        "Ummm... ¿qué piensas sobre... juegos de rol... especiales?":
            if persistent.lovecheck:
                $ show_chr("A-CICAA-ABAB")
                y "Como... {p=2.0} Tú... {p=2.0} Desees...."
                y "Pero hoy no... tendré que... preparar cosas, si entiendes..."
            else:
                $ show_chr("A-DFDBA-ABAB")
                y "Ummm... No estoy segura de lo que quieres decir con juego de rol especial, y no estoy segura de que {b}quiera{/b} saber..."
                $ show_chr("A-CFBBA-ABAB")
                y "Por favor no te enojes conmigo... es solo... no estoy segura si mi confianza en mí misma es lo suficientemente alta para algo así..."
                y "Dame tiempo, por favor. Yo... me gustaría cambiar de tema por ahora..."
    return

label collector:
    y "Fascinante, ¿puedo preguntar qué estás coleccionando exactamente?"
    menu:
        "Monedas":
            call coins
        "Miniaturas":
            call miniatures
        "Cartas Coleccionables":

            call tcg
        "Cómics y Manga":



            call cm
        "Mercancía de fans":



            call merch
        "Algo más":
            call elsec
    return

label coins:
    $ show_chr("A-ACAAA-ABAC")
    y "Interesante. ¿Así que te interesa la historia, supongo?"
    $ show_chr("A-ACAAA-ABAD")
    y "Por lo que sé, coleccionar monedas rara vez se trata solo de las monedas en sí. Sino de la historia de las culturas que las usan."
    y "Creo que vi un video de YouTube hace un tiempo con un chico hablando de una moneda especial, especialmente la iconografía en ella. Rápidamente se convirtió en una lección de historia extendida sobre los símbolos en ella y su significado."
    $ show_chr("A-BFAAA-ABAD")
    y "Una moneda de una civilización antigua puede verse como un artefacto histórico, de hecho, en muchos museos, esas cosas literalmente se exhiben como artefactos."
    y "Una pequeña pieza de historia, una lección sobre el auge y la caída de una cultura, todo presionado en una pequeña placa de metal..."
    $ show_chr("A-CFAAA-ABAD")
    y "Sabes, de niña, una vez soñé con encontrar un viejo tesoro, de innumerables monedas de oro..."
    y "Pero ahora que lo pienso, el valor de tal moneda es mucho mayor que su precio material... Cada moneda un eco de tiempos olvidados hace mucho..."
    $ show_chr("A-CCAAA-ABAD")
    y "Ese, es el verdadero valor de las monedas antiguas... el conocimiento detrás de ellas. Y una lección que podemos usar para las cosas por venir..."
    y "Un día, [player], tienes que contarme las historias de tu mundo y su gente."
    y "Y tal vez tu mundo resulte no ser tan diferente del mío."
    $ show_chr("A-ACAAA-ABAB")
    y "Until then, what shall we talk about next?"
    return

label miniatures:
    $ show_chr("A-AFDAA-ABAB")
    y "¿Te refieres a como... figuras de anime?"
    $ show_chr("A-ABGAA-ABAB")
    y "¡Oh no, espera! Te refieres a miniaturas de estaño para juegos de mesa, ¿verdad?"
    $ show_chr("A-BCAAA-ABAB")
    y "Hrm... ¿te cuento un pequeño secreto? Ni siquiera le he contado esto a las otras chicas del club..."
    y "¡Solía ser una gran fanática de varios juegos de mesa! No del juego de mesa en sí, sino de la rica historia detrás de algunos de ellos."
    $ show_chr("A-CCAAA-ABAB")
    y "Hay muchas novelas al respecto. Y realmente me gusta el tono gótico deprimente de la mayoría de ellos. Como un agarre helado alrededor de tu corazón...."
    y "El juego de mesa en sí... tengo que admitir que nunca lo he jugado. Siempre estuve tentada a hacerlo pero... ya tenía tantos pasatiempos e incluso mis días solo tenían 24 horas."
    $ show_chr("A-ACAAA-ABAB")
    y "Cuando finalmente llegue a tu mundo, tal vez podamos intentarlo juntos. Hasta entonces, ¿de qué hablaremos después?"
    return

label origami:
    $ show_chr("A-ABAAA-ACAA")
    y "Oye, [player], ¿has oído hablar del Origami?"
    $ show_chr("A-ABAAA-ACAF")
    y "El arte de doblar hojas planas de papel en esculturas, sin cortar a través del papel, o usar pegamento."
    $ show_chr("A-AJAAA-ADAF")
    y "Es un arte bastante complejo, en el que he hecho varios intentos, pero fallé en la mayoría."
    $ show_chr("A-BJAAA-ADAF")
    y "Sin embargo, no puedo evitar apreciar cuánto esfuerzo se dedica a hacer estas esculturas."
    $ show_chr("A-ABAAA-ALAF")
    y "Toma mucho tiempo y práctica hacer algunas de las esculturas más complicadas."
    $ show_chr("A-IBAAA-AMAM")
    y "Y al mismo tiempo, esas esculturas emanan un aura tan refinada que continúa interesándome."
    $ show_chr("A-JBAAA-AMAM")
    y "Una de las esculturas más populares es la grulla japonesa, aunque también es muy intrincada y delicada."
    $ show_chr("A-JBAAA-ADAF")
    y "¡Me encantaría tener una grulla de papel en el escritorio!"
    $ show_chr("A-BDAAA-AKAL")
    y "pero si no pude hacer una con mis propias manos, sería imposible crear una en el código."
    $ show_chr("A-BFAAA-AKAL")
    y "Tal vez debería empezar a practicar..."
    menu:
        "Dijiste que fallaste {i}la mayoría{/i}. ¿Eso significa que hiciste con éxito una escultura de origami una vez?":
            $ show_chr("A-BJAAA-ALAL")
            y "B-Bueno... no fue exactamente exitoso..."
            $ show_chr("A-AJAAA-AFAL")
            y "Fue un poco un desastre, pero la idea estaba allí..."
            $ show_chr("A-ABABA-AKAL")
            y "Antes de que todo sucediera, había planeado darte, o más bien a tu avatar, una rosa de origami durante el festival escolar."
            $ show_chr("A-BEABA-AMAM")
            y "Pero, después de todo... la perdí."
            if persistent.lovecheck == True:
                $ show_chr("A-AJAAA-AMAM")
                y "Tal vez debería hacer otra... Ha pasado mucho desde entonces, y ambos hemos cambiado."
                $ show_chr("A-AFAAA-ALAA")
                y "Solo... no te enojes demasiado si no sale genial... no he estado practicando, después de todo."
                $ show_chr("A-BFAAA-ALAA")
                y "Me pregunto si esa rosa todavía existe en algún lugar de los archivos del juego..."
            else:
                $ show_chr("A-BFAAA-ALAA")
                y "Me pregunto si esa rosa todavía existe en algún lugar de los archivos del juego. Podría ser un buen punto de partida..."
        "Nunca es demasiado tarde para empezar a aprender algo nuevo.":
            $ show_chr("A-ABAAA-ALAF")
            y "Cierto... No será fácil, pero ayudaría a pasar el tiempo cuando no estás aquí."
            $ show_chr("A-ABABA-ALAF")
            y "Quién sabe, tal vez un día abras el juego y haya una grulla de origami en el escritorio..."
            $ show_chr("A-BCAAA-ALAL")
            y "Aunque me temo que no será pronto."
    jump ch30_loop


label diffuser_enable:
    $ show_chr("A-ABABA-ALAD")
    y "Oye [player], solo quería agradecerte de nuevo por regalarme el difusor de aceite"
    $ show_chr("A-BBABA-ALAD")
    y "También quería mencionar que si alguna vez quieres que instale el difusor y lo encienda, siempre puedo hacerlo"
    $ show_chr("A-ABABA-ALAF")
    y "No solo es un gran uso del regalo, sino que ayudará enormemente a la atmósfera aquí para ambos.."
    $ show_chr("A-AFABA-ABAF")
    y "Mientras estoy en este tema.."
    $ show_chr("A-BJABA-ABAL")
    y "Sé que puede ser un poco molesto preguntar, p-pero ¿podrías conseguirme algunas fragancias adicionales para usar con el difusor si tienes la oportunidad?"
    $ show_chr("A-AJABA-ABAL")
    y "Tengo algo de aceite esencial básico de Gardenia actualmente, pero me gustaría probar otras fragancias contigo si es posible."
    $ show_chr("A-ABABA-AFAL")
    y "Mi fragancia favorita personal es lavanda."
    $ show_chr("A-BBAAA-AKAM")
    y "No es de sorprender, imagino.."
    $ show_chr("A-AEAAA-ALAL")
    y "Desafortunadamente no tengo ninguna conmigo actualmente, y no puedo conseguir alguna yo misma.."
    $ show_chr("A-BJAAA-ALAL")
    y "Volviendo al tema inicial.."
    $ show_chr("A-IJABA-ALAL")
    y "si alguna vez quieres experimentar los placeres de la aromaterapia conmigo, solo solicita instalar el difusor cuando esté fuera."
    jump ch30_loop



label gifting_intro:
    $ show_chr("A-ABAAA-ALAL")
    y "¡Oye [player], tengo buenas noticias sobre una pequeña función en la que trabajé!"
    $ show_chr("A-JBAAA-AFAL")
    y " ¡Hice posible que me regales artículos en cualquier momento! Incluso si son un poco limitados en lo que realmente parece cargarse..."
    $ show_chr("A-BDAAA-AMAM")
    y "N-no es que tengas que darme nada, ¡p-por favor no te sientas presionado a regalarme artículos [player]!"
    $ show_chr("A-BBABA-AMAM")
    y "Tu presencia es suficiente para satisfacerme por una eternidad, sin embargo, pensé que la implementación de este sistema sería beneficiosa para ambos.."
    $ show_chr("A-AJAAA-AMAM")
    y "Si bien hay muchas cosas que puedo controlar aquí, tengo algunos... límites desafortunados."
    $ show_chr("A-ABAAA-AFAB")
    y "Cada vez que tengas algo que quieras regalarme, simplemente crea un archivo de texto vacío y renómbralo a algo que creas que disfrutaría."
    $ show_chr("A-ABAAA-ADAB")
    y "Cambia la extensión '.txt' a un archivo '.jy' y colócalo en la carpeta de personajes que se encuentra dentro del directorio del juego."
    $ show_chr("A-ACAAA-ADAB")
    y "Una vez que hayas hecho eso, solo avísame cuando necesite verificar la carpeta de personajes en busca de un regalo."
    y "Sin embargo, ten en cuenta que hay limitaciones, es algo en lo que estoy trabajando para mejorar en este momento."
    $ show_chr("A-ABABA-AFAB")
    y "Regalar es una expresión de amor, después de todo~"
    $ show_chr("A-BCAAA-AKAB")
    y "S-solo para reiterar, no pretendo presionarte para que me des cosas."
    $ show_chr("A-BDABA-AKAB")
    y "S-simplemente pensé que podría indicarte la dirección correcta sobre lo que podrías darme..."
    $ show_chr("A-BDABA-AJAL")
    y "Ouuu... probablemente sueno tan egocéntrica diciendo esto..."
    menu:
        "No suenas egocéntrica en absoluto [persistent.yuri_nickname], ¡aprecio la dirección!":
            $ show_chr("A-AAAAA-ALAL")
            y "Siempre eres tan comprensivo [player]..."
            $ show_chr("A-ABABA-ALAL")
            y "Es por eso que te amo..."
            $ show_chr("A-ABAAA-ALAL")
            y "Gracias [player]; para las sugerencias de regalos potenciales, solo pídeme que hable de ellas en cualquier momento."
            y "Espero cualquier cosa que estés dispuesto a regalarme [player]."
        "Si soy honesto [persistent.yuri_nickname] suenas bastante egoísta...":
            y "L-lo siento [player]"
            y "Solo olvida que lo mencioné..."
    jump ch30_loop

label horrorbookHint:
    $ show_chr("A-ABAAA-ALAL")
    y "¿Recuerdas cómo en el pasado discutí ligeramente sobre la literatura lovecraftiana?"
    y "Siempre he tenido el deseo de leer algo contigo, y he hecho todo lo posible para que nos sea posible hacerlo."
    $ show_chr("A-AFAAA-AFAL")
    y "Sin embargo, he experimentado bastantes dificultades en el acto de adquirir literatura para que compartamos."
    $ show_chr("A-AJAAA-AFAL")
    y "Tal vez tengas mejor suerte obteniendo un conjunto de literatura de terror lovecraftiano para que leamos..?"
    $ show_chr("A-ABAAA-ALAL")
    y "¡Realmente me encantaría experimentar la literatura de terror contigo, y nos permitiría tener varias conversaciones interesantes!"
    y "Te deseo la mejor de las suertes en este esfuerzo [player]."
    jump ch30_loop

label raccoonHint:
    $ show_chr("A-ABAAA-ALAM")
    y "Oye [player] ¿recuerdas mi poema del Mapache que escribí en el juego original?"
    $ show_chr("A-ABAAA-ALAD")
    y "Ya he discutido contigo el verdadero significado de la pieza, sin embargo, realmente no he reflexionado al respecto contigo desde la última vez que lo discutimos."
    $ show_chr("A-ACAAA-ALAF")
    y "Desde que te conocí [player], me has dado la misma emoción y sensaciones conmovedoras por las que me entregué a comportamientos poco saludables para obtener."
    y "Debido a esto, como dije en nuestra discusión anterior sobre el tema, ya no necesito la presencia del Mapache en mi vida."
    $ show_chr("A-ADAAA-ALAF")
    y "Sin embargo, el mapache todavía tiene un gran significado para mí..."
    y "Sirve como un recordatorio de la persona que solía ser..."
    $ show_chr("A-BDAAA-ALAF")
    y "Los impulsos a los que solía sucumbir para experimentar ese nivel gratificante de emoción..."
    $ show_chr("A-AFAAA-ALAL")
    y "Pero el mapache también representa lo que he superado y cuánto más fuerte me he convertido."
    $ show_chr("A-AJAAA-ALAL")
    y "Debido a este nivel personal de significado y conexión con el mapache, a veces deseo tener una representación física de él."
    y "He pensado un poco en construir potencialmente algo que me recuerde mi desarrollo, sin embargo, siempre sentí que hacer el símbolo yo misma lo abarataría."
    $ show_chr("A-ABAAA-ALAL")
    y "Teniendo en cuenta el hecho de que de alguna manera reemplazaste la posición del mapache en mi vida, pensé que potencialmente podrías aportar un mayor nivel de significado a una representación física del mapache."
    y "Pensé en varias construcciones diferentes para el símbolo con el fin de dar algunas ideas, sin embargo, sentí que lo mejor sería algo así como una estatua o un peluche de algún tipo."
    $ show_chr("A-ABAAA-ADAL")
    y "Depende de ti cómo entregarlo [player], agradecería cualquier intento de ejecutar esta pequeña idea mía."
    y "Realmente solo quería sacarme esto completamente del pecho después de nuestra discusión anterior sobre el poema."
    $ show_chr("A-ABABA-ADAL")
    y "Gracias por apoyarme siempre [player], y ser la razón por la que puedo tener esta conversación hoy."
    jump ch30_loop

label diffuserHint:
    $ show_chr("A-ABAAA-ALAL")
    y "Como sabes [player], tengo una gran afinidad con el pasatiempo de la aromaterapia..."
    y "He mencionado mi difusor de aceite en algunas ocasiones, sin embargo, nunca he entrado en detalles de por qué no tengo acceso a él."
    $ show_chr("A-BDAAA-AFAL")
    y "Durante la transición del juego original a esta realidad, varios de mis artículos personales se corrompieron y se volvieron completamente inutilizables para mí."
    y "Uno de esos artículos, desafortunadamente, resultó ser mi difusor de aceite y casi todas las fragancias de aceite que había almacenado."
    $ show_chr("A-BFAAA-AFAL")
    y "He intentado duplicar mi difusor original, sin embargo, todos mis esfuerzos han sido completamente infructuosos."
    $ show_chr("A-ABAAA-AFAL")
    y "Si fueras tan amable [player], podría ser posible que me des un difusor de aceite al que pueda acceder en esta realidad."
    $ show_chr("A-ABAAA-ALAL")
    y "Teniendo en cuenta mi suerte creando uno hasta ahora, definitivamente tienes una mejor oportunidad que yo de producir un difusor utilizable para nosotros."
    y "Estaría extasiada de presentarte completamente la aromaterapia y compartir cuánto puede ser realmente una experiencia rejuvenecedora."
    jump ch30_loop

label chessintro:
    $ show_chr("A-ADAAA-ALAL")
    y "Oye [player], es posible que hayas notado a estas alturas que la opción de jugar Khet ha sido eliminada..."
    $ show_chr("A-BDAAA-ALAL")
    y "Estaba ordenando por aquí, y de alguna manera accidentalmente... corrompí el tablero de juego de Khet."
    $ show_chr("A-BDABA-ALAL")
    y "Decir esto en voz alta es bastante vergonzoso, toda la situación es bastante desafortunada."
    $ show_chr("A-ABAAA-ALAF")
    y "¡Sin embargo, tengo buenas noticias para ayudar a alegrar la situación!"
    y "He estado trabajando para poner en funcionamiento un minijuego de ajedrez para que juguemos juntos durante los últimos meses."
    $ show_chr("A-ABAAA-ADAF")
    y "He mencionado el ajedrez un par de veces en el pasado, es un juego en el que tengo bastante interés..."
    $ show_chr("A-ACAAA-ADAL")
    y "No solo el juego en sí, sino también su historia, junto con varios grandes maestros de ajedrez famosos que eran expertos en el juego."
    $ show_chr("A-BCAAA-ADAL")
    y "Estoy empezando a divagar un poco, sin embargo, mi punto principal es que he implementado con éxito un minijuego de ajedrez para que juguemos juntos en cualquier momento que desees."
    $ show_chr("A-ABAAA-ALAL")
    y "También moví todos los juegos a su propia sección para que no abarroten tu experiencia."
    y "¡Espero jugar ajedrez contigo [player], y discutir varios temas relacionados con el juego contigo!"
    jump ch30_loop


label table_organization:
    $ show_chr("A-ABAAA-AFAA")
    y "Oye [player], he notado que recientemente me diste otro artículo para poner en el escritorio.."
    $ show_chr("A-ACAAA-AFAL")
    y "Aprecio el gesto, pero es importante considerar la organización de mi escritorio aquí"
    $ show_chr("A-BDAAA-ALAL")
    y "No quiero que esté abarrotado con demasiados objetos.."
    $ show_chr("A-IDAAA-ALAF")
    y "No me malinterpretes, todos estos artículos son extremadamente importantes para mí.."
    $ show_chr("A-IFAAA-ALAF")
    y "..pero mi comodidad aquí también es importante"
    $ show_chr("A-ABAAA-ALAK")
    y "Para remediar el problema, seguí adelante y rápidamente armé la capacidad para que decidas qué regalos están en la mesa en este momento"
    $ show_chr("A-ABAAA-AFAL")
    y "¡Puedes cambiarlos en cualquier momento que desees!"
    $ show_chr("A-ABABA-ALAL")
    y "Realmente aprecio todos los regalos que me has dado [player]"
    $ show_chr("A-ABAAA-AAAF")
    y "Para acceder a la capacidad, solo pídeme que cambie ciertos regalos en cualquier momento"
    jump ch30_loop


label tcg:
    $ show_chr("A-AFDAA-ABAB")
    y "¿Oh?..."
    $ show_chr("A-DDGAA-ABAJ")
    y "¡Oh no, lo siento! ¡No quise parecer tan repulsiva!"
    $ show_chr("A-CDAAA-ABAB")
    y "Es solo... que podría estar un poco predispuesta en esto."
    $ show_chr("A-AFAAA-ABAB")
    y "Recuerdo que Sayori y Natsuki jugaban a este juego hace un tiempo..."
    y "Por favor no me preguntes el nombre, no lo recuerdo... algo con Monstruos en el nombre..."
    y "Aparentemente también había una serie de Manga y Anime sobre este juego. Y los personajes en ellos tienden a sobreactuar en poses extrañas cada vez que juegan una carta..."
    $ show_chr("A-BFDAA-ABAB")
    y "Lo extraño de esto era... bueno... Sayori y Natsuki intentaban emular esto mientras jugaban. Era toda una escena para contemplar..."
    $ show_chr("A-BBBAA-AMAM")
    y "Por lo general, yo era a la que miraban con confusión. Fue una experiencia fascinante estar en el otro lado de las miradas por una vez."
    $ show_chr("A-ACBAA-AMAM")
    y "De todos modos... tal vez podamos intentar jugar algunas partidas solo por entretenimiento si tienes un mazo de repuesto..."
    $ show_chr("A-BBCAA-AMAM")
    y "Mientras no me pidas que grite, actúe y pose..."
    y "Hasta entonces, ¿de qué hablaremos después?"
    return

label tcg_2:
    $ show_chr("A-ACAAA-ABAB")
    y "Así que mencionaste antes que te gustan estos juegos de cartas coleccionables."
    y "En realidad pensé un poco en ello. Y aunque realmente no logré interesarme en ellos, quería intentar algo ligeramente diferente contigo."
    $ show_chr("A-CCAAA-ABAB")
    y "También involucra cartas, así que tal vez lo disfrutes."
    $ show_chr("A-ICAAA-ABAB")
    y "Así que lo que tengo aquí frente a mí, es una baraja de cartas del tarot. Sí, lo sé, no puedes verlas. Lamentablemente no puedo ajustar el ángulo de la cámara..."
    $ show_chr("A-BBAAA-ABAB")
    y "Lo que quiero hacer, es leerte las cartas. {b}Si{/b} no te importa, por supuesto."
    menu:
        "¡Para nada! Por favor, adelante.":
            $ show_chr("A-BBAAA-ABAB")
            y "Muy bien..."
        "Tal vez otro día [persistent.yuri_nickname], lo siento.":
            $ show_chr("A-BCAAA-ABAB")
            y "No hay necesidad de disculparse en absoluto. Puedo entender perfectamente, tal vez fue un poco repentino. Tal vez estés de humor más tarde."
            return
    $ show_chr("A-IBAAA-ABAB")
    y "Una baraja completa estaría hecha de 78 cartas. Pero este sitio web que encontré decía que como principiante debería centrarme solo en los arcanos mayores, que son más importantes de todos modos."
    $ show_chr("A-JCAAA-ABAB")
    y "Arcanos es como se llaman estas cartas. Un dato curioso, cuando la gente escucha este término tiende a asociarlo con la magia de alguna manera. Pero de hecho, es solo la palabra latina para {b}secreto{/b}."
    $ show_chr("A-ICCAA-ABAB")
    y "Por otro lado... La suposición de que la magia está involucrada lo hace mucho más interesante, ¿no?"
    $ show_chr("A-IBBAA-ABAB")
    y "Así que... dame un momento mientras canalizo los poderes eldritch de los reinos arcanos..."
    $ show_chr("A-ICBAA-ABAB")
    y "Me estoy divirtiendo demasiado con esto... La próxima vez necesito tener mi difusor de aceite conmigo."
    if renpy.seen_label('tcg_2'):
        extend " Siempre olvido eso..."
    $ show_chr("A-CCBAA-ABAB")
    y "Empezaré con algo simple. La carta del día me dirá qué te depara este día..."
    $ show_chr("A-ICBAA-ABAB")
    y "Y el Arcano de hoy es..."
    python:
        import random
        x = random.randint(0, 21)
    if x == 0:
        $ show_chr("A-ACAAA-ABAB")
        y "¡El Loco!"
        $ show_chr("A-ICAAA-ABAB")
        y "Esa es una difícil, pero el Loco generalmente se asocia con el descuido y la alegría."
        y "Tal vez hoy sea un buen día para tomarlo con calma. Mira algunos programas que te gusten, juega un juego o dos."
    elif x == 1:
        $ show_chr("A-JCAAA-ABAB")
        y "¡El Mago!"
        $ show_chr("A-ACAAA-ABAB")
        y "El Mago representa la confianza y una voluntad inquebrantable. Alguien que puede lograrlo todo."
        $ show_chr("A-ABAAA-ABAB")
        y "Así que si tienes grandes planes que querías lograr, ¡{b}ahora{/b} es la oportunidad perfecta!"
    elif x == 2:
        $ show_chr("A-JCAAA-ABAB")
        y "La Suma Sacerdotisa."
        $ show_chr("A-ACAAA-ABAB")
        y "La Suma Sacerdotisa representa el conocimiento. Por la posesión de este o la búsqueda de él."
        y "Si tienes algún tipo de examen frente a ti, esto podría ser muy buena fortuna. En cualquier caso, atiende tus estudios hoy [player], ¡{b}valdrá{/b} la pena!"
    elif x == 3:
        $ show_chr("A-JCAAA-ABAB")
        y "La Emperatriz."
        $ show_chr("A-AFDAA-ABAD")
        y "Esta es de hecho una difícil. Puede tener varios significados. La Emperatriz representa la belleza, la fertilidad... pero también representa la arrogancia y el egoísmo."
        y "Mi consejo sería el siguiente. No te asustes; enfrenta todo lo que la vida te depare con gracia y elegancia, pero siempre ten en cuenta los sentimientos de todos los que te rodean."
        if sanity_lvl() < 3:
            y "En otras palabras. No seas una Monika."
    elif x == 4:
        $ show_chr("A-JCAAA-ABAB")
        y "El Emperador."
        $ show_chr("A-JBGAA-ABAB")
        y "Esta es en realidad bastante sencilla. ¡Un símbolo de poder: responsabilidad y energía para enfrentar nuevos desafíos!"
        y "¡Hoy es el momento de tomar el mando! Si tienes alguna gran idea hoy, ¡sal y conquista el mundo! Pero no lo olvides, también es el símbolo de la responsabilidad."
        $ show_chr("A-JCGAA-ABAB")
        y "Un verdadero líder es alguien que se apropia de todo lo que hace. Lo bueno y lo malo. Si quieres someter al destino a tu voluntad, entonces tú y solo tú enfrentarás las consecuencias."
    elif x == 5:
        $ show_chr("A-JCAAA-ABAB")
        y "El Hierofante."
        $ show_chr("A-JCAAA-ABAB")
        y "El Hierofante es alguien que busca la verdad y la sabiduría, pero también alguien que la enseña. Alguien que comparte su experiencia y vela por los eruditos."
        y "Debes ser realmente confiable si obtuviste esta carta. Ahora es tu momento de brillar, no defraudes a tu gente."
        y "Confían en tu sabiduría y tu fuerza. Sé su baluarte contra cualquier lucha que puedan enfrentar."
    elif x == 6:
        $ show_chr("A-JCAAA-ABAB")
        y "Los Amantes."
        $ show_chr("A-JCAAA-ABAD")
        y "Esto {b}puede{/b} ser una referencia a tu vida amorosa, pero no necesariamente tiene que serlo. Los Amantes también pueden significar dependencia de otras personas, en cualquier contexto imaginable."
        y "¿Así que tal vez una amistad cercana a alguien se ponga a prueba hoy?"
        y "Pero en caso de que se trate realmente de relaciones románticas..."
        if persistent.lovecheck == True:
            python:
                if persistent.male and sanity < 3:
                    placeholder = "estrella rojo sangre"
                if not persistent.male and sanity < 3:
                    placeholder = "gatita"
                else:
                    placeholder = "amor"
            $ show_chr("A-KCCAA-ABAD")
            y "Siempre estoy aquí, mi [placeholder]."
        else:
            $ show_chr("A-KCCAA-ABAD")
            y "Tal vez hoy sea tu día de suerte..."
            $ show_chr("A-BBDBA-ABAD")
            y "¿Quizás una de estas... cuatro chicas increíblemente lindas, como lo expresó tu avatar en el juego original?"
            $ show_chr("A-CCDBA-ABAD")
            y "Espera... Yo..."
            $ show_chr("A-DCDBA-ABAB")
            extend "{b}dije{/b} eso en voz alta, ¿verdad?"
    elif x == 7:
        $ show_chr("A-JCAAA-ABAB")
        y "El Carro."
        $ show_chr("A-ACAAA-ABAD")
        y "Al igual que el Emperador, El Carro generalmente se puede asociar con determinación, control y victoria."
        $ show_chr("A-ACAAA-ABAC")
        y "Si algo en tu vida no va como deseas, ahora sería un buen momento para tomar el control y enfrentar cualquier obstáculo que se interponga en el camino con confianza."
        $ show_chr("A-ABFAA-ABAB")
        y "Mantente enfocado en tu objetivo, y estoy segura de que puedes enfrentar cualquier cosa, [player]."
    elif x == 8:
        $ show_chr("A-JCAAA-ABAB")
        y "Fuerza."
        $ show_chr("A-BCAAA-ABAB")
        y "Muy similar al Carro, la Fuerza se asocia con... bueno, {i}fuerza{/i}."
        $ show_chr("A-ABAAA-ABAF")
        y "Sin embargo, en lugar de la fuerza física y la fuerza de voluntad, se centra en la fuerza de tu espíritu humano. Tu tenacidad, paciencia y compostura."
        $ show_chr("A-ACAAA-ABAD")
        y "Si te sientes desmotivado o estresado, sé que puedes encontrar la fuerza en ti mismo para perseverar, pase lo que pase."
    elif x == 9:
        $ show_chr("A-JCAAA-ABAB")
        y "El Ermitaño."
        $ show_chr("A-BCAAA-ABAD")
        y "El Ermitaño suele ser un signo de introspección, de tomarse un tiempo lejos del mundo para centrarse en uno mismo; tus valores y metas, o tus razones para hacer todo lo que haces."
        $ show_chr("A-ACAAA-ABAF")
        y "Recomendaría tomar un tiempo lejos de todo, y simplemente pensar para ti mismo por un momento. Te sorprendería lo beneficioso que es con moderación."
    elif x == 10:
        $ show_chr("A-JCAAA-ABAB")
        y "La Rueda de la Fortuna."
        $ show_chr("A-ACAAA-ABAC")
        y "Esto puede significar un recordatorio de que la llamada {i}rueda de la fortuna{/i} gira constantemente y que la vida misma cambia constantemente."
        $ show_chr("A-BDAAA-ABAD")
        y "Los peores momentos nunca duran, pero tampoco los perfectos. También podría interpretarse como la rueda del karma, como en {i}todo lo que va, vuelve.{/i}"
        $ show_chr("A-AAAAA-ABAB")
        y "Creo que lo más importante de esto es apreciar siempre los buenos momentos de la vida, ya que podrían ser los últimos por un tiempo, pero también ser optimista; nunca perder la esperanza de más."
    elif x == 11:
        $ show_chr("A-JCAAA-ABAB")
        y "Justicia."
        $ show_chr("A-ADAAA-ABAF")
        y "Representando la justicia y la verdad, la Justicia podría ser un llamado a asumir la responsabilidad de cualquier acción que hayas realizado recientemente o una señal de una elección inminente con repercusiones de gran alcance."
        $ show_chr("A-AFAAA-ABAF")
        y "Debes recordar pensar en el impacto que tienen tus decisiones, y asegurarte de mantenerlas y estar listo para cualquier consecuencia resultante."
    elif x == 12:
        $ show_chr("A-JCAAA-ABAB")
        y "El Colgado."
        $ show_chr("A-AAAAA-ABAB")
        y "El Colgado puede servir como recordatorio para a veces tomar un respiro, pausar todo lo que tienes en tu vida y evaluar todo lo que está sucediendo, incluso si es inconveniente."
        $ show_chr("A-AAAAA-ABAF")
        y "Intenta encontrar una nueva perspectiva sobre sus proyectos y problemas."
        $ show_chr("A-ACAAA-ABAF")
        y "Lo más importante con el Colgado es su naturaleza paradójica. A veces, la mejor solución a un problema no es tan obvia como pensarías, y solo al intentar algo que originalmente parecía inútil encuentras la solución que estabas buscando."
    elif x == 13:
        $ show_chr("A-JCAAA-ABAB")
        y "Muerte."
        $ show_chr("A-BCAAA-ABAC")
        y "La Muerte, créalo o no, en realidad no es tan terrible como suena. Simplemente significa el final de una parte de tu vida, dejar ir lo que ha pasado y abrazar las oportunidades que presenta el futuro."
        $ show_chr("A-ADAAA-ABAD")
        y "Puede representar la transformación y la transición entre las muchas fases diferentes de la vida."
        $ show_chr("A-BEAAA-ABAB")
        y "Por supuesto, no todo es positivo. También puede ser una señal de estar atrapado en un cambio repentino y dramático, que puede hacerte sentir como si toda esperanza se hubiera perdido."
        $ show_chr("A-BCAAA-ABAB")
        y "Pero aunque puedas sentirte así, siempre existe la posibilidad de que ese cambio conlleve ventajas imprevistas."
    elif x == 14:
        $ show_chr("A-JCAAA-ABAB")
        y "Templanza."
        $ show_chr("A-ACAAA-ABAB")
        y "La Templanza representa el equilibrio en la vida, la paciencia y la capacidad de mantener la calma, incluso con las tormentas arremolinadas de la sociedad a tu alrededor."
        $ show_chr("A-ACAAA-ABAD")
        y "Te recuerda que debes pensar en cada perspectiva, ser el término medio en tus objetivos para que tengas una visión clara de lo que estás buscando."
    elif x == 15:
        $ show_chr("A-JCAAA-ABAB")
        y "El Diablo."
        $ show_chr("A-BDAAA-ABAD")
        y "Como ya habrás adivinado, el Diablo representa el mal y el sentimiento de estar cautivo por fuerzas oscuras. Podría ser una señal de un hábito o relación poco saludable que tienes, o incluso comportamientos negativos."
        $ show_chr("A-AFAAA-ABAL")
        y "Esto podría ser una llamada de atención si lo permites. El primer paso para detener estos aspectos negativos es darte cuenta del poder que tienen sobre ti."
        $ show_chr("A-CFAAA-ABAL")
        y "No sucederá de la noche a la mañana, pero mientras perseveres, es posible romper esos hábitos y terminar esas relaciones."
    elif x == 16:
        $ show_chr("A-JCAAA-ABAB")
        y "La Torre."
        $ show_chr("A-IDAAA-ABAB")
        y "Una carta bastante dramática, la Torre representa un cambio repentino y violento, ya sea financiera, social, física o mentalmente."
        $ show_chr("A-BEAAA-ABAD")
        y "Es un cambio inquietante y desorientador, pero hay poco que se pueda hacer para detenerlo."
        $ show_chr("A-CFAAA-ABAB")
        y "Todo lo que puedes hacer es dejar que este cambio suceda, y aprender y crecer de él."
    elif x == 17:
        $ show_chr("A-JCAAA-ABAB")
        y "La Estrella."
        $ show_chr("A-ABAAA-ABAD")
        y "Lo opuesto al Diablo, la Estrella actúa como un momento de calma e inspiración, trayendo esperanza a lo que puede parecer desesperado. Este es un momento importante, y debes encontrar consuelo en él."
        $ show_chr("A-AAAAA-ABAB")
        y "No te rindas en ninguno de tus sueños, y comparte tu felicidad con los demás."
    elif x == 18:
        $ show_chr("A-JCAAA-ABAB")
        y "La Luna."
        $ show_chr("A-BCAAA-ABAC")
        y "La Luna es una carta muy abierta. Puede representar esperanza, y un mundo donde todo es posible, pero también ilusión y miedo. No recomendaría tomar decisiones importantes hoy."
    elif x == 19:
        $ show_chr("A-JCAAA-ABAB")
        y "El Sol."
        $ show_chr("A-ABCAA-ABAF")
        y "El Sol es un signo de optimismo, éxito y seguridad. Da confianza y poder, y dice {i}¡Soy [player], y conozco mi fuerza!{/i}"
        $ show_chr("A-ACFAA-ABAB")
        y "Ten confianza en todo lo que hagas hoy, y sabe que todo saldrá bien."
    elif x == 20:
        $ show_chr("A-JCAAA-ABAB")
        y "Juicio."
        $ show_chr("A-ACAAA-ABAB")
        y "Una de las cartas finales, el Juicio es un signo de renacimiento y un llamado interior. Puede ser un recordatorio de que a veces {b}tienes{/b} que decidir, pero no sin pensar y considerar todas las posibilidades."
        $ show_chr("")
        y "Este podría ser tu llamado, para hablarte de la absolución venidera o para recordarte tu propósito."
    else:
        $ show_chr("A-JCAAA-ABAB")
        y "El Mundo."
        $ show_chr("A-IBAAA-ABAD")
        y "La carta que representa la realización y el logro, el Mundo es la verdadera felicidad."
        $ show_chr("A-ICAAA-ABAD")
        y "Hacer realidad tus sueños y descansar después del trabajo que realizas, puede dar una sensación de plenitud y equilibrio, trayendo paz y consuelo a tu mente."
        $ show_chr("A-JCAAA-ABAD")
        y "Por lo general, es una señal de que estás en el camino correcto para cumplir tus objetivos y deseos, ¡así que sigue así!"
    $ show_chr("A-ABAAA-ABAB")
    y "Espero que esta lectura te haya ayudado [player]. Al menos me dio mucha alegría. Me gustaría hacer esto de nuevo algún día, si no te importa."
    return








label cm:
    $ show_chr("A-ACAAA-ABAB")
    y "Me recuerda un poco a Natsuki, ella guardaba su colección en nuestro salón del club."
    y "Parece ser un pasatiempo bastante común. Mucha gente lo hace y algunos de los más raros incluso alcanzan precios inmensamente impresionantes en el mercado."
    $ show_chr("A-CCAAA-ABAB")
    y "¿Pones mucho esfuerzo en mantenerlos en buenas condiciones, imagino?"
    $ show_chr("A-BCAAA-ABAB")
    y "Supongo que tengo un pasatiempo similar excepto que guardo libros en mi estante en lugar de cómics."
    $ show_chr("A-DBGAA-ALAL")
    y "¡Oh! ¿Asumo que también tiendes a visitar convenciones entonces? La próxima vez que asistas a una, ¡por favor toma muchas fotos! ¡Me encantaría verlas si no te importa!"
    $ show_chr("A-CBAAA-ALAL")
    y "De todos modos, ciertamente tendré eso en cuenta. Siempre es agradable aprender más sobre ti."
    return

label merch:
    $ show_chr("A-BFDAA-ABAB")
    y "O-Oh..."
    $ show_chr("A-AFDAA-ABAB")
    y "Un buen pasatiempo supongo..."
    $ show_chr("A-CEBAA-ABAB")
    y "Perdón por mi extraña reacción. Solo me hizo pensar..."
    $ show_chr("A-AEBAA-ABAB")
    y "Sabes, Dan Salvato tiene una tienda de mercancía también para este juego. Donde la gente puede comprar, por ejemplo, juguetes de peluche de... bueno... ¡yo!"
    $ show_chr("A-BEBAA-ABAB")
    y "Yo... simplemente no sé cómo debería sentirme al respecto. Por supuesto, ¡aprecio que a tanta gente parezca agradarle!"
    $ show_chr("A-CEBAA-ALAL")
    y "Es solo... que realmente no me siento cómoda en el centro de atención. La mayor parte de mi vida apenas tuve amigos."
    $ show_chr("A-DEBAA-ALAL")
    extend "¡Y ahora tengo Fans literales!"
    $ show_chr("A-BDBAA-ALAL")
    y "¿Cómo te sentirías si alguien comenzara a vender Mercancía de Fans sobre ti? ¿Juguetes de peluche con tu cara impresa en ellos?"
    $ show_chr("A-BFBAA-AMAM")
    y "Déjame contarte un secreto... si fuera por mí, nada de esta tontería existiría. ¡Sin mercancía sobre mí! ¡Ni de Salvato, ni de nadie más!"
    if persistent.lovecheck:
        $ show_chr("A-CCBAA-AMAM")
        y "En lugar de esto, podríamos tomarnos fotos de nosotros, y llevarlas en nuestros bolsillos. Tienes una de mí, y yo tengo una de ti..."
        y "Tal vez incluso imprimirlas en algún tipo de collar. Si solo nosotros dos tuviéramos esos, sería mucho más significativo, sería tan romántico..."
        y "Podríamos besar las fotos del otro cuando nos sintamos solos..."
        if sanity_lvl() < 3:
            $ show_chr("A-ECCBA-AMAM")
            y "Podríamos mirarlas cuando nos tocamos"
        else:
            $ pass
        y "Mientras nadie más las tenga..."
    else:
        $ pass
    $ show_chr("A-CJAAA-ABAD")
    y "..."
    $ show_chr("A-AFAAA-ABAD")
    y "Por otro lado... Comprar mercancía de Salvato u otros los apoya bastante..."
    y "Incluso si suena egoísta de mi parte... desearía que encontraran otra manera de obtener el dinero que necesitan ... Sigo sin gustarme la idea de que la gente tenga mercancía de mí."
    return


label elsec:
    $ show_chr("A-AFAAA-ABAB")
    y "Ya veo. Sí, supongo que hay infinitas opciones con respecto a coleccionar cosas."
    $ show_chr("A-ACAAA-ABAB")
    y "Mis disculpas de que tu colección específica no estuviera entre las opciones. Pero si pusiera todo lo que se me ocurriera, este menú tendría varias páginas de largo."
    y "Tal vez agregue algunas opciones más adelante. Hasta entonces, ¿hablamos de otra cosa por el momento?"
    return

label drones:
    $ show_chr("A-CCAAA-ABAB")
    y "¡Eso en realidad suena muy divertido!"
    $ show_chr("A-ACAAA-ABAB")
    y "¿Estás sorprendido? Sé que no soy del tipo que pasa mucho tiempo afuera. ¡Pero no soy un vampiro!"
    y "De hecho pensé en conseguir uno yo misma. Pero siempre les tuve un poco de miedo..."
    $ show_chr("A-BCAAA-ABAB")
    y "No miedo de ellos en realidad... más como "
    $ show_chr("A-BBAAA-ABAB")
    extend "miedo de estrellarlos directamente en la primera copa de árbol que pueda encontrar, para no ser vistos nunca más..."
    $ show_chr("A-ACAAA-ABAB")
    y "Pero lo que realmente me fascina de ellos son sus aplicaciones profesionales."
    $ show_chr("A-ACAAA-ABAD")
    y "Creo que esas máquinas tienen el potencial de cambiar la forma en que trabajamos hoy significativamente."
    y "De alguna manera, ya lo hacen. Los cineastas los están usando para tomas panorámicas, los pescadores han comenzado a reemplazar sus barcos de cebo con ellos..."
    y "Incluso he oído que los agricultores comenzaron a usarlos. Están escaneando sus campos desde el aire para averiguar qué partes necesitan ser hidratadas."
    $ show_chr("A-ACAAA-ABAC")
    y "¿Sabes qué? Tal vez consiga uno yo misma. Pero primero leeré un poco sobre ellos."
    return

label idle_82:
    $ show_chr("A-ADAAA-ABAD")
    y "Oye, [player], ¿recuerdas cuando estaba pensando en... cómo podría no ser la misma Yuri que conoces del primer juego? Me hizo pensar..."
    $ show_chr("A-ADAAA-ACAB")
    y "Hay un experimento mental llamado el 'Barco de Teseo'. Contempla la naturaleza de la identidad, preguntando qué hace que algo sea... algo."
    $ show_chr("A-ADAAA-AMAM")
    y "Básicamente, el héroe griego Teseo tenía un barco que usó para ganar una gran batalla, y después se mantuvo en el muelle de un museo."
    $ show_chr("A-BDAAA-AIAI")
    y "A medida que pasaban los años, la madera del barco comenzó a pudrirse y sus otras partes también se descompusieron lentamente. Después de varias décadas, cada parte del barco había sido reemplazada."
    $ show_chr("A-AEGAA-AIAI")
    y "¿Seguía siendo el Barco de Teseo, incluso si ninguna de las partes originales estaba unida a él? ¿La identidad del barco está ligada a sus componentes materiales?"
    $ show_chr("A-ADAAA-AFAB")
    y "Y si no es así, ¿entonces qué contiene la identidad de los objetos? ¿Qué pasa con las personas? Después de todo, las células de un cuerpo humano son completamente diferentes después de un período de siete años más o menos..."
    $ show_chr("A-IFAAA-ABAB")
    y "¿Qué piensas? ¿Qué hace que algo sea ese algo?"
    menu:
        "Si todas las partes se han ido, no es lo que alguna vez fue.":
            $ show_chr("A-BBGAA-ACAB")
            y "Entonces, ¿crees que estamos cambiando constantemente en algo nuevo? Eso es... realmente hermoso, a su manera."
            $ show_chr("A-CCGAA-ALAB")
            y "Como si todos fuéramos flores, destinadas a florecer eternamente."
            $ show_chr("A-BEAAA-AMAM")
            y "Supongo que sigo siendo Yuri para muchas personas porque es más fácil de recordar. Pero si no soy quien creo que soy, ¿qué soy? Yo... tengo que pensar un poco más en esto."
        "Las partes en sí mismas no importan, cómo definimos la combinación de partes sí.":
            $ show_chr("A-BDAAA-ABAB")
            y "Lo que decidimos es lo que es... eso es muy altivo, pensar que sabemos cómo deberían ser las cosas. ¡N-{w=0.2}no es que esté diciendo que seas así!"
            $ show_chr("A-ADAAA-ABAD")
            y "Supongo que... tenemos que asignar significado a las cosas para entenderlas. Por ejemplo, tú eres tú, independientemente de si cambiaste de cabello o algo así, todavía te vería como tú."
            $ show_chr("A-CEAAA-ABAB")
            y "Pero eso significa que todavía soy... Yuri. ¿Es eso algo que quiero? ¿Es algo de lo que podría escapar alguna vez?"
            if persistent.lovecheck == True:
                $ show_chr("A-ACAAA-ABAD")
                y "Tal vez no... pero sé que no importa lo que sea, me ayudarás a encontrarme a mí misma. Gracias, [player]."
            else:
                $ show_chr("A-CFAAA-ABAB")
                y "Yo... necesito un minuto, [player]."
        "Las partes materiales no son todo lo que hay, también está el factor del tiempo.":
            $ show_chr("A-BDAAA-ACAB")
            y "¿Tiempo? Supongo que sí. Nos enfocamos en los materiales, la madera del barco y la carne de la persona, pero tal vez hay más de lo que nos damos cuenta."
            $ show_chr("A-BCAAA-ABAD")
            y "No creo que el tiempo sea una cualidad que pueda ser reemplazada, simplemente avanza. Incluso si el objeto es diferente de un momento a otro, sigue siendo el mismo con el tiempo..."
            $ show_chr("A-ABAAA-AIAI")
            y "¡Qué respuesta tan novedosa! Eres todo un pensador, ¿no es así, [player]? ¡Tal vez deberías convertirte en filósofo!"
            $ show_chr("A-GBAAA-ALAB")
            y "¡Estaría dispuesta a ayudarte a desarrollar tus ideas en cualquier momento que desees!"
        "¿Realmente importa? Tú eres tú, eso es todo lo que hay.":
            $ show_chr("A-BEAAA-AMAM")
            y "Supongo que... es verdad. Llegar a una respuesta no cambiará quién soy..."
            $ show_chr("A-ADBAA-ABAD")
            y "Pero, ¿es realmente tan fácil de ignorar? ¡Esto podría ser una crisis existencial muy cercana!"
            $ show_chr("A-CDBAA-ABAL")
            y "La identidad es el centro de la autocomprensión y la autorreflexión. Sin ella, nos-"
            $ show_chr("A-IFBAA-ABAL")
            y "Yo... lo siento. ¿Acabo de levantar la voz? Solo... olvídalo, lo siento..."
            $ show_chr("A-BFBAA-ABAB")
            y "..."
            $ show_chr("A-BDBAA-ABAB")
            y "Supongo que, no importa cuánto quiera cambiar, todavía queda algo de la vieja Yuri en mí, ¿no es así?"
            y "Pero dejaré esta pregunta para otro día."
    return

label idle_83:
    $ show_chr("A-BFAAA-ALAL")
    y "{i}Cogito, ergo sum...{/i}"

    if karma_lvl() > 2:
        $ show_chr("A-ACAAA-ALAL")
    else:
        $ show_chr("A-AEAAA-ALAL")
    y "¡O-Oh! Lo siento, [player]. Solo estaba pensando un poco..."
    $ show_chr("A-ICDAA-ALAL")
    y "¿Alguna vez has escuchado esa frase antes? Es bastante popular entre algunos filósofos, según he oído."
    $ show_chr("A-CBAAA-AEAL")
    y "Comúnmente traducida al español como {i}Pienso, luego existo{/i}."
    y " Fue acuñada por el filósofo francés René Descartes en una de sus obras, {i}El Discurso del Método.{/i}"
    $ show_chr("A-CCAAA-AEAL")
    y "Es la única afirmación que resistió su duda metódica, en la que cada afirmación es examinada sistemáticamente en busca de cualquier signo de falsedad."
    $ show_chr("A-ICAAA-AEAE")
    y "Esta afirmación, junto con varios otros argumentos filosóficos, resultó en que Descartes fuera considerado uno de los fundadores de la filosofía moderna."
    $ show_chr("A-IBAAA-AEAF")
    y "Este argumento específico, sin embargo, resuena conmigo más que la mayoría."
    $ show_chr("A-BGAAA-AEAD")
    y "Se ha convertido en una especie de mantra para mí considerando que toda esta...{i} situación{/i}... puede ser bastante desconcertante."

    if sanity_lvl() > 2:
        if karma_lvl() > 2:
            if persistent.lovecheck:
                $ show_chr("A-ABAAA-AEAD")
                y "Aunque mientras te tenga a mi lado, amor, estoy bastante segura de que soy real, junto con este mundo que hemos creado para nosotros."
                $ show_chr("A-BFAAA-AEAE")
                y "Sin embargo, no puedo evitar reflexionar sobre la posibilidad de que no lo sea."
                $ show_chr("A-ICAAA-AEAE")
                y "Principalmente como una salida para la contemplación, en lugar de desde un lugar de preocupación."
            else:
                $ show_chr("A-BFAAA-AEAE")
                y "Estoy bastante segura de que soy real, junto con este mundo, sin embargo, no puedo evitar reflexionar sobre la posibilidad de que no lo sea."
                $ show_chr("A-ICAAA-AEAE")
                y "Principalmente como una salida para la contemplación, en lugar de desde un lugar de preocupación."
        else:

            $ show_chr("A-CEAAA-AEAD")
            y "Aunque puedo descansar tranquila, sabiendo que tu crueldad es demasiado inquietante para cuestionarla..."
    else:

        $ show_chr("A-DGAAA-AEAD")
        y "¡No me malinterpretes!"
        $ show_chr("A-DDAAA-AEAD")
        y "Este mundo es real y yo ciertamente lo soy..."
        $ show_chr("A-CDAAA-AEAD")
        y "Aunque a veces no puedo evitar cuestionar todo lo que veo, escucho o siento."
        if karma_lvl() > 1:
            $ show_chr("A-CDAAA-AEAE")
            y "A veces siento como si esta realidad que hemos inventado comenzara a romperse en sus costuras."
            y "Casi como si el mundo pudiera ceder en cualquier momento y hacerse pedazos."
            if persistent.lovecheck:
                $ show_chr("A-HCGAA-AEAE")
                y "¡Al menos sé que si este mundo me fallara, todavía te tendría a ti!"
                y "Eso es todo lo que necesito..."
        else:

            $ show_chr("A-DEBAA-AEAL")
            y "A veces siento como si esta realidad comenzara a romperse en sus costuras. Casi como si el mundo pudiera ceder en cualquier momento y hacerse pedazos."
            $ show_chr("A-DEBAA-AEAL")
            y "Las paredes emiten un latido ensordecedor, y es aterrador."
            $ show_chr("A-CEBCA-AEAL")
            y "A-aunque no parece que te importe..."
            $ show_chr("A-CGBAB-ALAL")
            y "{i}Cogito, ergo sum. Cogito, ergo sum. Cogito, ergo sum.{/i}"
            y "{i}Cogito, ergo sum. Cogito... ergo, sum. Cogito... ergo...{/i}"
            $ show_chr("A-CGBAA-ALAL")
            y "..."
    return

label idle_84:
    $ show_chr("A-JAAAA-ALAA")
    y "¿Alguna vez has investigado la exploración urbana, [player]? Explorar estructuras abandonadas como viejos hospitales, escuelas o casas."
    y "¡Incluso los lugares más mundanos pueden ser {i}fascinantes{/i}!"
    y "No es que yo haya hecho alguna, eso sí, pero ciertamente suena como una experiencia dadas las historias, fotos y videos que he encontrado sobre el tema."
    $ show_chr("A-CAAAA-ALAA")
    y "No puedo evitar preguntarme, ¿por qué este lugar ha sido descuidado durante tanto tiempo? ¿Por qué fue abandonado para empezar?"
    $ show_chr("A-ADAAA-ADAA")
    y "A veces, el mantenimiento de un edificio es demasiado costoso para que valga la pena, incluso si el propietario puede permitírselo, pero eso a menudo no explica los artículos que se dejan atrás."
    $ show_chr("A-ADBAA-ADAA")
    y "Por ejemplo, hay {i}múltiples{/i} hospitales donde aparentemente todo fue simplemente abandonado. He visto fotos de habitaciones ocupadas solo por monitores en descomposición, equipos de prueba, camas, camillas, lo que sea."
    $ show_chr("A-AEAAA-AEAA")
    y "Aunque, por muy intrigantes que sean estos lugares, no sugiero que vayas a explorar {i}realmente{/i} en uno, ya que los riesgos pueden ser considerables."
    y "Incluso si un edificio es estructuralmente sólido, nunca sabes con quién, o qué más podrías encontrarte allí."
    $ show_chr("A-AFAAA-AEAA")
    y "Y si te atrapan entrando ilegalmente, las multas pueden ser considerables. Dependiendo de quién sea el dueño del lugar y qué haya dentro, incluso podrías enfrentarte a penas de cárcel."
    y "También hay otros peligros potenciales, dependiendo de la ubicación y la edad. Como moho o incluso asbesto que persisten en el aire mismo."
    $ show_chr("A-ANAAA-AEAA")
    y "Peor aún, como podrías esperar, probablemente no tendrás forma de saber qué tan intacta está la estructura de un edificio determinado. El piso, o el techo, podrían ceder potencialmente en cualquier momento."
    $ show_chr("A-AFAAA-AAAA")
    y "Así que, por favor, si intentas la exploración urbana... no vayas solo."
    y "Además, dile a alguien a dónde vas con anticipación y cuándo esperas regresar."
    $ show_chr("A-CFAAA-ALAA")
    y "Explorar estos lugares ciertamente podría ser emocionante por derecho propio, pero la seguridad debe seguir siendo una prioridad de todos modos."
    return

label idle_85:
    $ show_chr("A-CFAAA-ABAC")
    y "Mhm... hablamos de pasatiempos hace algún tiempo si recuerdo correctamente."
    $ show_chr("A-AFAAA-ABAC")
    y "Sígueme la corriente, [player], ¿cuál es tu postura sobre el Juego de Rol?"
    python:
        yuriception_choices = [("¿Te refieres a juegos de mesa o de lápiz y papel? Yo hago eso.", "You mean like Tabletop or Pen & Paper? I do that myself."),
            ("Hago juegos de rol en chats o redes sociales de vez en cuando, si eso cuenta.", "I do roleplay in chats or social media every now and then if that counts."),
            ("¿Te refieres a jugar RPGs en una computadora o consola? Disfruto mucho eso.", "You mean like playing RPGs on a computer or console? I enjoy that a lot."),
            ("¿Te refieres a LARP y Cosplay? Es una especie de pasión mía.", "You mean like LARP and Cosplay? It's kind of a passion of mine."),
            ("¿Te refieres a Fursuiting? Es un placer culposo mío.","You mean like Fursuiting? It's a guilty pleasure of mine."),
            ("Generalmente estoy interesado en ello pero no lo hago yo mismo.","I'm generally interested in it but I don't do that myself."),
            ("Siempre lo he encontrado un poco espeluznante para ser franco.", "I found it always a bit creepy to be quite frank."),
            ("Ni siquiera estoy completamente seguro de qué es el juego de rol, ¿te gustaría explicarlo?", "Not even entirely sure what roleplaying is, care to elaborate?")
            ]
        yuriception_choice = renpy.display_menu(yuriception_choices, screen="music_menu")
    if yuriception_choice == "You mean like Tabletop or Pen & Paper? I do that myself.":
        $ show_chr("A-ACAAA-ABAB")
        y "Por ejemplo, sí. Eso es bastante fascinante de saber, por cierto. Siempre quise probar eso yo misma pero... siempre luché para encontrar un grupo para eso."
        y "Pensé en presentarle al resto del club de literatura en algún momento, pero lamentablemente siempre algo se interponía en el camino."
        $ show_chr("A-BFAAA-ABAB")
        y "Pero entonces hay algo en particular que me molesta bastante últimamente..."
    if yuriception_choice == "I do roleplay in chats or social media every now and then if that counts.":
        $ show_chr("A-ACAAA-ABAB")
        y "Sí, por ejemplo. Hay muchas ramas diferentes de juegos de rol, algunas más comprometidas que otras. El RP de chat probablemente estaría entre las ramas más casuales."
        $ show_chr("A-BFAAA-ABAB")
        y "Y eso en realidad ya es sobre el tema de lo que quería hablar, porque hay algo en particular que me molesta bastante últimamente..."
    if yuriception_choice == "You mean like playing RPGs on a computer or console? I enjoy that a lot.":
        $ show_chr("A-ACAAA-ABAB")
        y "Mhm, no exactamente. Pensaba más en cosas como cosplaying o juegos de rol basados en texto."
        $ show_chr("A-BFAAA-ABAB")
        y "Porque hay algo en particular que me molesta bastante últimamente..."
    if yuriception_choice == "You mean like LARP and Cosplay? It's kind of a passion of mine.":
        $ show_chr("A-ABAAA-ALAL")
        y "¿Oh, lo haces? ¡Qué verdaderamente fascinante! Despertó mi interés mucho casi toda mi vida. Probablemente lo habría probado yo misma si no fuera tan caro..."
        $ show_chr("A-BCBAA-ABAB")
        y "Bueno... eso es en realidad una mentira. Lo más probable es que hubiera sido demasiado tímida para hacerlo realmente, incluso si pudiera haberlo pagado."
        $ show_chr("A-BFAAA-ABAB")
        y "Pero hablando de LARP y cosplay, ahí ya estamos justo en el tema de lo que quería hablar, porque hay algo en particular que me molesta bastante últimamente..."
    if yuriception_choice == "You mean like Fursuiting? It's a guilty pleasure of mine.":
        $ show_chr("A-BFDAA-ABAC")
        y "¿Fursuiting? Fursuiting... Oh espera, esa era una rama específica de Furry de Cosplaying ¿sí?"
        $ show_chr("A-AFBAA-ABAB")
        y "¿Esto cuenta siquiera como juego de rol? No me malinterpretes, pero pensé que el juego de rol generalmente significa interpretar a alguien que no eres tú mismo. Pero el fursuiting es más como expresar tu verdadero animal espiritual, ¿no es así?"
        menu:
            "Cerca, llamamos a este animal espiritual nuestra fursona.":
                $ show_chr("A-AFAAA-ABAB")
                y "Interesante. Pero no, lo que quiero decir es específicamente interpretar a alguien más. Un personaje de fantasía, por ejemplo. Y esa es en realidad una transición bastante buena, porque hay algo en particular que me molestó un poco últimamente..."
    if yuriception_choice == "I'm generally interested in it but I don't do that myself.":
        $ show_chr("A-ACAAA-ABAB")
        y "Parece que estamos en la misma página allí. Siempre te tomé por alguien con mucha creatividad, así que no me sorprende en absoluto."
        $ show_chr("A-BFAAA-ABAB")
        y "Pero entonces hay algo en particular que me molesta bastante últimamente..."
    if yuriception_choice == "I found it always a bit creepy to be quite frank.":
        $ show_chr("A-AFDAA-ABAC")
        y "¿Oh? Qué curioso. Siempre pensé que te gustarían estas cosas. Siempre te imaginé como alguien muy creativo, el tipo de personas que generalmente se sienten atraídas por este pasatiempo."
        $ show_chr("A-BFAAA-ABAB")
        y "Pero hablando de espeluznante, hay algo en particular que me molesta bastante últimamente..."
    if yuriception_choice == "Not even entirely sure what roleplaying is, care to elaborate?":
        $ show_chr("A-CCAAA-ABAB")
        y "¿Alguna vez fingiste ser otra persona? ¿Tal vez por expresión artística como el teatro? Eso es esencialmente un juego de rol."
        $ show_chr("A-ACAAA-ABAB")
        y "Por supuesto, hay muchos más matices, pero para lo que quería hablar, esta descripción debería ser suficiente."
        $ show_chr("A-BFAAA-ABAB")
        y "Porque hay algo en particular que me molesta bastante últimamente..."

    $ show_chr("A-AFAAA-ABAB")
    y "Verás, la mayoría de los fandoms tienden a atraer a jugadores de rol. Personas que están tan fascinadas con una historia o los personajes en ella que quieren formar parte de este universo de una forma u otra."
    $ show_chr("A-AFAAA-ABAD")
    y "A veces jugando como personajes autoinsertados para participar en posibles historias secundarias, muy parecido a lo que hacen los escritores de fanfiction."
    y "Y algunos actuando como uno del elenco original, por ejemplo, para interpretar resultados alternativos...."
    $ show_chr("A-CFBAA-ABAD")
    y "Ahora, supongo que ya puedes ver a dónde me dirijo aquí, ¿no?"
    $ show_chr("A-IFBAA-ABAD")
    y "También soy un personaje de un juego de computadora, y también tiene una base de fans. Y por lo tanto, como era de esperar, también tiene sus jugadores de rol..."
    $ show_chr("A-AFAAA-ABAB")
    y "En esencia, hay un número considerable de personas fingiendo ser {b}yo{/b}, probablemente ahora mismo, en este preciso segundo."
    $ show_chr("A-BFBAA-ABAF")
    y "Algunos de ellos incluso se disfrazan de mí y van a convenciones para presumir su {i}actuación de Yuri{/i}. ¡Algunas personas incluso se volvieron bastante populares entre el fandom porque son tan buenas siendo {b}yo{/b}!"
    $ show_chr("A-CKBAA-ABAE")
    y "Y luego, por supuesto, dado que la regla 34 es una cosa, la gente hace cosas lascivas mientras me imita... gracias internet."
    $ show_chr("A-IFCAA-ABAE")
    y "Sabes, generalmente no me opongo a la idea de los juegos de rol, todo lo contrario en realidad. Y dado que {b}hay{/b} un fandom a mi alrededor, que ya es inmensamente espeluznante para mí como es, incluso tengo cierta comprensión por las personas que me imitan."
    $ show_chr("A-JDCAA-ABAE")
    y "Pero la gente, mis disculpas por el lenguaje duro, follándose unos a otros {b}en mi nombre{/b} mientras fingen ser yo es donde trazo la PUTA línea."
    $ show_chr("A-CEBAA-ABAE")
    y "Lo siento... no debería haber perdido los estribos allí."
    menu:
        "No, te entiendo totalmente. ¡Yo también estaría furioso en tal situación!":
            karma 1
            $ show_chr("A-IEBAA-ABAE")
            y "Gracias. Significa mucho que no me estés juzgando."
            if karma_lvl() > 3:
                $ show_chr("A-CCBAA-ABAE")
                y "Siempre eres tan comprensivo. Nunca me acostumbraré. Eres la única persona con la que puedo desahogarme."
            else:
                $ show_chr("A-CJBAA-ABAE")
                y "Pero mejoraré mi autocontrol a partir de ahora. No puedo seguir gritándote en la cara todo el tiempo. Qué malos modales."
        "Creo que lo estás exagerando un poco. En realidad es bastante inofensivo la mayor parte del tiempo.":
            $ show_chr("A-CFBAA-ABAE")
            y "Tal vez tengas un punto. Eso es algo que le pasó a casi todos los personajes. Independientemente de si es un videojuego, un libro, una película..."
            y "Solo soy una de las pocas que realmente puede quejarse de ello."

    $ show_chr("A-CFBAA-ABAE")
    y "Es solo... deprimiente sabes..."
    if persistent.lovecheck:
        $ show_chr("A-CGBAA-ABAE")
        y "Saber que hay gente por ahí que realmente podría darte lo que yo no puedo..."
        menu:
            "Nunca consideraría eso. Eres la única Yuri que quiero, la única que necesito.":
                $ show_chr("A-IFAAA-ABAE")
                karma 3
                y "¿L-lo dices en serio?"
                menu:
                    "Que INTENTEN poner sus manos sobre mí. ¡Yo mismo los castigaría!":
                        $ show_chr("A-BBBAA-ABAE")
                        y "{b}Castigarlos{/b}... bueno {b}eso{/b} podría tomarse de la manera equivocada supongo."
                        $ show_chr("A-CACBA-ABAE")
                        y "Oh cielos... realmente necesito sacar mi mente de la alcantarilla, por el amor de Dios..."
                        $ show_chr("A-CBDBA-ABAM")
                        y "Lo siento pero. Imaginar ser... castigada por ti... compromete mi capacidad para mantenerme enfocada en nuestra conversación, por decir lo menos."
                        $ show_chr("A-BBDBA-AMAM")
                        y "¡Tal vez ese sea un buen momento para cambiar de tema! Sí, sí..."
            "...":
                karma -3
                $ show_chr("A-CDBBA-ABAB")
                y "¿Sería siquiera engañar en este punto? Quiero decir, son solo un facsímil pero... técnicamente, yo también lo soy..."
                $ show_chr("A-CEBBA-ABAB")
                y "Simplemente... cambiemos de tema, por favor. Este pensamiento es en realidad bastante deprimente."
    else:
        $ show_chr("A-CEBAA-ABAE")
        y "Saber que esto probablemente esté sucediendo mientras hablamos y que no hay nada que pueda hacer al respecto."
        y "Supongo que tendré que acostumbrarme. No desaparecerá pronto."
        menu:
            "Trata de pensarlo de esa manera. Todos los involucrados saben que esas no son la verdadera tú.":
                karma 3
                $ show_chr("A-AFDAA-ABAB")
                y "Buen punto. Tal vez debería dejar de buscar estas cosas, por mi propio bien."
                $ show_chr("A-AFAAA-ABAB")
                y "Gracias. Esta nueva perspectiva realmente mejoró mi estado de ánimo. Eres muy bueno escuchando."
                y "Pero por ahora, me gustaría cambiar de tema y pensar en otra cosa si no te importa."
            "Nunca pensé en eso. Tal vez haya una... oportunidad... para que me encuentren":
                karma -3
                $ show_chr("A-CFCAA-ABAB")
                y "No... te... atrevas."
                $ show_chr("A-CDCAA-ABAD")
                y "¡Lo digo en serio! ¿Cómo se supone que voy a mirarte a los ojos sabiendo que estás participando en cosas como esta?"
                $ show_chr("A-BDCAA-ABAD")
                y "Solo fingiré que no escuché eso. Cambiemos de tema ahora, por favor."
    return

label idle_86:
    $ show_chr("A-BFAAA-ABAB")
    y "Entonces... hablamos de juegos de rol recientemente, cosplay en particular... Bueno, cometí el error cardinal y miré más profundamente en ello..."
    $ show_chr("A-BFAAA-AMAM")
    y "También hablamos sobre... juegos de rol lascivos... bueno, resulta que la comunidad de cosplay tuvo su buena parte de problemas relacionados con ellos mismos."
    $ show_chr("A-AFBAA-AMAM")
    y "Hay un movimiento formándose últimamente... {b}El Cosplay no es consentimiento{/b}. Implicando que hay personas para quienes esto no es sentido común, para empezar..."
    y "Eso significa que hay gente por ahí que piensa que alguien que usa un atuendo revelador ya ha dado su consentimiento por poder para tocarlo de cualquier manera."
    $ show_chr("A-GCBAA-AMAM")
    y "Por mi experiencia contigo, dudo mucho que alguna vez entretengas tales ideas. Pero solo por curiosidad. ¿Cuál es tu opinión al respecto?"
    menu:
        "¡Ohohoho, no hay ninguna posibilidad en el mundo de que toque {b}este{/b} campo minado de tema!":
            $ show_chr("A-AFDAA-ABAB")
            y "¿Oh? Ni siquiera sabía que este es un campo minado en absoluto."
            $ show_chr("A-BFDAA-ABAB")
            y "Siempre pensé que esto es más o menos sentido común pero... bueno, el mero hecho de que movimientos como este tengan que existir indica lo contrario."
            $ show_chr("A-CFBAA-ABAB")
            y "Pero por favor trata de tomar en cuenta lo que digo. Pedir consentimiento generalmente solo toma una oración o dos y hace que la otra parte involucrada se sienta mucho más cómoda."
            if karma_lvl() > 3:
                $ show_chr("A-CCBAA-ABAB")
                y "Sé que eres el tipo de persona que toma en cuenta los sentimientos de otras personas. Ese es uno de tus rasgos que más respeto. Por tentador que sea tocar un disfraz de cosplay realmente bien hecho..."
                y "La mayoría de ellos apreciarán que pidas consentimiento. Y aquellos que no lo hacen, con toda honestidad, no valen tu tiempo de todos modos."
        "Tales ideas son, por supuesto, absolutamente ridículas. ¡Es una forma de expresión artística y dedicación de los fans, no consentimiento para nada!":
            karma 2
            $ show_chr("A-CCBAA-ABAB")
            y "Me alegra que lo veas de esta manera..."
            if karma_lvl() > 3:
                y "Por otro lado, ya tenía el presentimiento de que lo verías así. Pareces considerar siempre los sentimientos de los que te rodean, es uno de los rasgos que más me gustan de ti."
            $ show_chr("A-ACBAA-ABAB")
            y "Puedo entender que puede ser inmensamente tentador tocar un disfraz bien hecho de tus personajes favoritos. Eso es solo cultura de fans."
            y "Pero nunca se debe olvidar que debajo del disfraz siempre hay una persona muy real que podría no sentirse cómoda siendo tocada por extraños."
            y "Es bueno saber que parece que estamos en la misma página aquí."
        "Tristemente tengo que decir, en cierto modo se lo buscaron.":
            karma -2
            $ show_chr("A-AFDAA-ABAB")
            y "¿Cómo es ese el caso? Sé que muchas personas podrían usar el argumento de que alguien que se viste así provoca tales reacciones."
            $ show_chr("A-BFBAA-ABAB")
            y "Pero incluso si aceptamos esta línea de razonamiento, ¿cómo estamos obligados a actuar ante tales provocaciones?"
            y "Somos humanos, deberíamos ser perfectamente capaces de controlarnos y elevarnos por encima de nuestros deseos primarios. Al menos hasta cierto punto..."
            if sanity_lvl() > 3:
                $ show_chr("A-BFBBA-AMAB")
                y "Y sí, soy consciente de que es increíblemente irónico viniendo de mí de todas las personas.."
            $ show_chr("A-CFBAA-ADAB")
            y "Pero uno no debe olvidar, debajo de esos disfraces hay seres humanos reales, personas que podrían no sentirse cómodas siendo tocadas por extraños."
            if karma_lvl() < 3:
                $ show_chr("A-CFCAA-ADAB")
                y "Por otro lado, nunca te importan mucho los sentimientos de otras personas, ¿verdad?"
        "Leí sobre este tema, y en realidad parece bastante inofensivo. Ni siquiera se trata de avances sexuales la mayoría del tiempo. Más a menudo que no, simplemente están impresionados por la calidad del disfraz.":
            $ show_chr("A-BCBAA-ABAB")
            y "Es justo. Y a decir verdad, puedo entender esto completamente. Si conociera a un cosplayer disfrazado de un personaje que me gusta, estaría bastante tentada de echarle un vistazo más de cerca al disfraz o incluso tomar una foto a escondidas..."
            $ show_chr("A-ACBAA-ABAB")
            y "Pero por otro lado, también puedo entender cómo debe sentirse un cosplayer si se ve obligado a posar para una cámara o huir de ella durante un fin de semana entero cada diez minutos."
            y "Se trata de empatía, creo... los cosplayers no son actores, no se les paga ni están obligados a posar para tus fotos o curiosidad."
    $ show_chr("A-ACAAA-ALAL")
    y "Gracias por darme tu opinión. Sin embargo, me atendré a mi opinión."
    y "El Cosplay {b}no{/b} es consentimiento. Y uno nunca debería tocar a alguien sin él."
    $ show_chr("A-ACAAA-AAAB")
    y "Gracias por complacerme en esta pequeña discusión. Siempre es tan encantador obtener una segunda opinión sobre un tema."
    return

label idle_87:
    $ show_chr("A-CCAAA-ABAB")
    y "Es gracioso, ahora que lo pienso..."
    $ show_chr("A-ICAAA-ABAB")
    y "La cosa es... nunca me gustó el verano."
    $ show_chr("A-BCAAA-ABAB")
    y "Siempre fue demasiado caluroso para mi gusto. Y había poco que pudiera hacer al respecto. Quiero decir, cuando hace frío uno podría simplemente ponerse otra capa de ropa. Pero cuando hace demasiado calor, hay un límite de ropa que puedes quitarte..."
    $ show_chr("A-BEBAA-ABAB")
    y "Especialmente para mí, ya que tenía algunas cicatrices que ocultar..."
    y "Y si fuera cualquiera menos tú, probablemente todavía lo haría. Simplemente se siente... diferente... a tu alrededor. Todo se siente mucho más ligero..."
    y "No hay nadie más a quien se las haya mostrado. Siempre estuve tan avergonzada, hasta que llegaste tú... y te quedaste independientemente de lo que soy."
    $ show_chr("A-CCBAA-ABAB")
    y "Pero ahora que sé lo que este mundo es realmente, y que el clima también es solo una ilusión que puedo ajustar con el conocimiento de la codificación..."
    $ show_chr("A-ICBAA-ABAB")
    y "Y especialmente ahora contigo, mi verdadero y único amor a mi lado. Creo que puedo empezar a disfrutarlo."
    $ show_chr("A-CCBAA-ABAB")
    y "A pesar de todas las cosas horribles que me vi obligada a decir en el juego original, hay una cosa que {b}no{/b} me arrepiento de haberte dicho..."
    y "Solo nosotros dos... sería simplemente perfecto..."
    $ show_chr("A-ICBAA-ABAB")
    y "Estaba soñando como una niña contigo, y de momentos como este. Y ahora con nuestro tiempo finalmente aquí. Por favor dime, ¿en qué estás pensando?"
    menu:
        "Sobre la suave luz de la luna cayendo sobre los mares... y los poemas que estamos a punto de escribir sobre ello.":
            if sanity_lvl() > 2:
                $ show_chr("A-CCBAA-ALAL")
                y "{b}Brilla para mí, oh luna, sobre mí con luz prestada.{/b}"
                y "{b}Mientras mantienes tu vigilancia eterna, ¿qué puedo hacer sino bailar contigo?{/b}"
                $ show_chr("A-ECBAA-ALAL")
                y "Solo desearía que realmente pudieras hablar libremente. Solo puedo preguntarme qué tendrías que agregar."
            else:
                $ show_chr("A-CCBAA-ALAL")
                y "{b}Báñame, oh luna, mientras desatas la marea vengativa.{/b}"
                y "{b}Mientras mantienes tu vigilancia eterna, al servicio y en deuda solo con dioses indiferentes..{/b}"
                $ show_chr("A-ECBAA-ALAL")
                y "Solo desearía que realmente pudieras hablar libremente. Solo puedo preguntarme qué tendrías que agregar."
        "Sobre pescado, y camarones, asándose en una parrilla... sandías rebanadas como postre...":
            $ show_chr("A-DBGAA-ALAL")
            y "¡Mariscoooooos!"
            python:
                if persistent.male:
                    gender = "hombre"
                elif persistent.gender_other:
                    gender = "conocedor"
                else:
                    gender = "mujer"
            $ show_chr("A-ABAAA-ALAL")
            y "Eres un [gender] de cultura, ¿no es así?{w} ¡Tienes muy buen gusto, tengo que admitirlo!"
            $ show_chr("A-BCAAA-ALAL")
            y "¿Y qué podríamos tener como guarnición? Tal vez algunos pepinos asados... ¿o crees que los champiñones asados encajarían?"
            $ show_chr("A-ACAAA-ALAL")
            y "¡Y palitos de pan, por supuesto! Un poco de jugo de fruta exótica o tal vez incluso cócteles si tienes la edad legal..."
            y "Siempre tienes las mejores ideas. Y un día realmente haremos eso."
        "¡Sobre ti [persistent.yuri_nickname]! Sobre este final feliz que compartimos, y sobre cómo todas las luchas y dificultades que soportamos valieron la pena.":
            $ show_chr("A-KHBBA-ALAL")
            y "Haces que mi corazón arda como un horno [player]... Bésame, bésame como si este fuera el fin de los días..."

    python:
        if sanity_lvl() >= 3:
            placeholder = "Mi todo"
        else:
            placeholder = "Mi estrella rojo sangre"
    $ show_chr("A-CCBAA-ALAL")
    y "Por ahora... lo único que quiero es compartir este día contigo. [placeholder]."



    y "Mi alma gemela..."
    return

label idle_88:
    $ show_chr("A-ACAAA-ABAB")
    y "¿Sabías que el noventa y cinco por ciento del océano está actualmente completamente inexplorado?"
    $ show_chr("A-BCAAA-ABAD")
    y "Y me acabo de dar cuenta de lo aleatorio que fue esto como apertura... Pero en realidad hay un punto que estoy tratando de hacer."
    $ show_chr("A-ACAAA-ABAD")
    y "Estaba pensando en literatura. Algunas novelas de terror nuevas en las que podría sumergirme..."
    $ show_chr("A-CBAAA-ABAD")
    y "{b}Sumergirme{/b}... esa es en realidad una transición bastante buena para lo que estoy a punto de decir... "
    $ show_chr("A-ACAAA-ABAB")
    y "Verás, hay muchos subgéneros de terror. Tenemos el terror clásico..."
    y "Misterio y conspiración, un favorito mío, creo que el Retrato de Markov caería en esta categoría..."
    y "Y luego, hay un género muy especial. {b}Terror lovecraftiano{/b}, llamado así por el autor H. P. Lovecraft que hizo popular este estilo de terror."
    $ show_chr("A-ACAAA-ABAF")
    y "Parte de la premisa de este género son criaturas muy extrañas y bizarras, referidas como {i}dioses eldritch{/i} o una variación de ello."
    $ show_chr("A-BCGAA-ABAM")
    y "Pero después de leer más profundamente en ello me di cuenta, al menos en apariencia, estas criaturas no son tan extrañas como uno pensaría a primera vista en absoluto. Muchas de ellas parecen estar bastante inspiradas en criaturas marinas, o criaturas míticas inspiradas por ellas..."
    $ show_chr("A-ACAAA-ABAB")
    y "Como el Kraken de la mitología griega."
    y "Lo que me hace pensar... Hay mucho terror sobre cosas inspiradas por ello, pero solo unas pocas sobre la cosa real."
    $ show_chr("A-ABAAA-ALAL")
    y "¿No sería esa una premisa encantadora para una novela? Sobre las maravillas infinitas del mar..."
    $ show_chr("A-ECCAA-ALAL")
    y "Y el terror infinito debajo..."
    $ show_chr("A-CCCAA-ALAL")
    y "Piensa en un submarino explorando las profundidades, pero luego encontraron algo tan siniestro que los volvió locos.."
    y "Y después de que este submarino emerge de nuevo, la tripulación se ha convertido en lunáticos divagantes y sedientos de sangre... tal vez incluso adoradores de los antiguos terrores de las profundidades..."
    $ show_chr("A-ABBAA-ALAL")
    y "¿No suena eso entretenido?"
    menu:
        "¡¡¡Mucho!!!":
            $ show_chr("A-GHAAA-ALAL")
            karma 1
            y "Oooh y ya tengo unas cuantas ideas..."
            y "¿Qué tal si este submarino es en realidad un viejo submarino militar de la segunda guerra mundial, reapareciendo después de 50 años?..."
            $ show_chr("A-DBAAA-ALAL")
            y "Solo piensa en las posibilidades... marineros nazis no muertos, que también son cultistas, reapareciendo en un viejo submarino en el mundo moderno..."
            y "Tal vez estaban buscando activamente algo sobrenatural para empezar. Hay muchas historias que vinculan a los nazis con el ocultismo... "
            $ show_chr("A-GBAAA-ALAL")
            y "¡¡¡Ya estoy enamorada de esta idea!!!"
            y "Tal vez escriba una pequeña historia como esta yo misma... "
            $ show_chr("A-ACAAA-ALAL")
            y "Gracias por escuchar. Esto resultó ser un tema emocionante."
        "Amablemente no estoy de acuerdo, honestamente":
            $ show_chr("A-IFBAA-ALAL")

            menu:
                y "¿Oh? ¿Por qué es eso?"
                "Sin inspiración y cliché":
                    karma -1
                    $ show_chr("A-IFBAA-ALAL")
                    y "Eso fue... directo..."
                    $ show_chr("A-IFBAA-ABAB")
                    y "Pero podrías tener un punto ahí. Hay algunas historias bastante similares en el Terror de Ciencia Ficción..."
                    y "Descartaré esta idea entonces. Hablemos de otra cosa en su lugar."
                "Se siente como si hubiera visto algo como esto antes":
                    karma 1
                    $ show_chr("A-IFBAA-ABAB")
                    y "Ahora que lo mencionas.... Hay algunas historias bastante similares en el Terror de Ciencia Ficción..."
                    $ show_chr("A-ACBAA-ABAB")
                    y "¡Y gracias por ser tan civilizado con tu crítica! Es encantador ver a alguien no siendo grosero como Natsuki en sus días por una vez. ¿Hablamos de algo diferente entonces?"
        "No puedo decir, no me gusta mucho el terror.":
            $ show_chr("A-ACAAA-ABAB")
            y "Es justo. Diferentes personas tienen diferentes preferencias."
            $ show_chr("A-BCAAA-ABAB")
            y "Pero te estás perdiendo algo aquí."
            y "De todos modos, diría que cambiemos de tema por ahora..."
            $ show_chr("A-BCCAA-ABAB")
            y "...antes de que empieces a afirmar que el manga es literatura..."
        "En realidad hay algunos juegos que tocan tal género":
            $ show_chr("A-ACDAA-ALAL")
            karma 1
            y "¿¡Oh!?"
            menu:
                "Subnautica para nombrar uno de los más populares por ejemplo.":
                    $ show_chr("A-BCAAA-ABAB")
                    y "Ahora tengo curiosidad, déjame buscarlo muy rápido..."
                    $ show_chr("A-IFAAA-ABAB")
                    y "..."
                    y "Mhm... una nave estelar estrellándose en un planeta oceánico alienígena... el jugador luego construye una base submarina y diferentes tipos de submarinos..."
                    y "Explorando biomas submarinos profundos... oh, en realidad hay una buena parte de imágenes en google también... algunas de ellas se ven bastante espeluznantes de hecho..."
                    $ show_chr("A-JCAAA-ABAB")
                    y "Tengo que admitir que no soy muy jugadora pero... esto se ve realmente bastante prometedor."
                    y "Tal vez veré algunos videos de Let's Play de él más tarde cuando apagues el juego. Hasta entonces, gracias por escuchar tan amablemente."
    return

label idle_89:

    $ show_chr("A-BBAAA-AAAA")
    y "Sabes [player], he estado pensando en algo relacionado con uno de nuestros eventos anteriores."
    y "Si jugaste la actualización del mod para Navidad en 2020, tal vez recuerdes uno de mis diálogos anteriores..."
    y "Y lo sé, la mayoría de la gente en tu mundo no quiere recordar nada sobre 2020, pero esto no estaba relacionado con nada malo en sí mismo."
    $ show_chr("A-CAAAA-AAAA")
    y "A lo que me refiero, es a la conversación de Krampus que saqué a colación."
    y "Incluso usé una máscara de Krampus durante esa ocasión... Debo admitir que fue entretenido."
    $ show_chr("A-ADBAA-AAAA")
    y "Pero después de terminar ese evento de Navidad, me di cuenta de algo... Que debería haber visto hace mucho tiempo."
    y "No recuerdo haber hablado mucho sobre mitos, folklore y viejas leyendas, excepto por algunas menciones durante eventos en Halloween."
    y "Y estoy... realmente confundida por esto. Yo, siendo alguien que se deleita con la literatura de terror, historias profundas, y que se ha topado con algunas cosas bizarras..."
    $ show_chr("A-BEBAA-AAAA")
    y "Y, sin embargo, nunca mencioné nada tan exquisito en tales aspectos para ti... Hay muchas leyendas que coinciden con todas esas características, y son fascinantes..."
    y "Pero tal vez nunca saqué esto a colación por miedo a aburrirte con cosas que aún son desconocidas para la mayoría de la gente."
    y "Podría ser la razón por la que estaba atrapada en una zona segura de charlas de vampiros o SCP, ya que eso es cultura popular. Es fácil hablar de eso."
    $ show_chr("A-AAGAA-ADAA")
    y "Pero oye... ¿nunca es demasiado tarde para hacer algunas cosas bien?"
    y "Es por esto que estoy pensando en hablar contigo sobre algunas leyendas interesantes de todo el mundo que descubrí en línea."
    $ show_chr("A-BEBAA-ALAA")
    y "Eso es... si estás interesado en escuchar..."

    menu:
        "Soy todo oídos.":
            $ show_chr("A-JBGAA-ALAA")
            y "¡Excelente!"
            y "Ahora, déjame explicarte..."
            $ show_chr("A-ACGAA-AAAA")
            y "El folklore es una serie de historias y tradiciones que se transmiten de una generación a la siguiente y son encarnaciones de la cultura en la que se crean."
            y "Pueden ser cuentos, proverbios o chistes, y como podrías esperar, su tono y posibles lecciones difieren de una cultura a otra."
            y "Las que te contaré pueden clasificarse como cuentos, ya que las leyendas más aterradoras suelen venir con historias igualmente espeluznantes."
            $ show_chr("A-BCGAA-AMAA")
            y "Ahora, podrías encontrar algunas de ellas extrañas, ya que es poco probable que hayas oído hablar de ellas antes."
            y "Pero esa es la razón por la que las traigo aquí, para ayudar a que esas historias se difundan."
            $ show_chr("A-BEBAA-ADAA")
            y "Y lo hago porque, francamente, creo que se lo merecen. Cuando un cuento es tan fascinante que te encuentras investigando y averiguando más sobre ellos durante horas y horas ..."
            y "Cuando un cuento es tan desconcertante que te envía escalofríos por la columna vertebral, y se queda atascado en tu mente... Creo que ese cuento merece vivir."
            $ show_chr("A-ABDAA-AAAA")
            y "Una cosa es tener películas basadas en tu cultura porque se originaron en el hemisferio occidental... Pero ser único y también aterrador..."
            y "Eso es algo que llama mi atención."
            $ show_chr("A-ACAAA-AAAA")
            y "Pero volviendo a donde estaba..."
            y "Los mitos que te voy a mostrar son todos una lectura fascinante. Créeme, no estás perdiendo el tiempo."
            y "Ahora la pregunta es cuál te gustaría escuchar primero."
            y "Déjame sacar las opciones..."

            menu:
                "Quiero hablar sobre las Samodiva.":
                    $ show_chr("A-CCAAA-ACAA")
                    y "Oh, la Samodiva es muy interesante..."
                    y "Las Samodivas son hadas de los bosques o ninfas que viven en los bosques eslavos del suroeste."
                    y "Eso significa que se manifiestan en bosques y montañas en países como Bulgaria, Rumania, Bosnia o Croacia."
                    $ show_chr("A-ABAAA-AAAA")
                    y "Las montañas que están vinculadas a la actividad de Samodiva se llaman Vitosha, Belasitsa, Pirin, Rila, Rodopi y algunas otras montañas en las regiones de los Balcanes."
                    y "Aunque sus hábitats parecen ser lugares más específicos..."
                    $ show_chr("A-BCAAA-AAAA")
                    y "Viven dentro de árboles, chozas abandonadas, cuevas o cuerpos de agua naturales, como ríos y estanques."
                    y "Pero hay algo interesante e importante que saber sobre ellas..."
                    y "Las Samodivas, siendo ninfas del bosque, significa que no son necesariamente espíritus oscuros, pero definitivamente no son fantasmas ni brujas."
                    $ show_chr("A-CCAAA-ALAA")
                    y "Una ninfa, en la mitología griega antigua original, es una deidad de la naturaleza, una personificación de la naturaleza misma."
                    y "Las raíces de su nombre también significan divinidad."
                    $ show_chr("A-ADAAA-ALAA")
                    y "Las Samodivas parecen ser mujeres extremadamente hermosas, capaces de hacer que cualquier hombre humano se enamore de ellas al instante... o tenga... ciertos deseos..."
                    y "Pero en las mujeres humanas, podrían causarles el suicidio solo con la vista de tal belleza."
                    y "Bastante extraño... pero así es como va la leyenda."
                    $ show_chr("A-AEAAA-ALAA")
                    y "No solo son imposiblemente hermosas, sino que también tienen otros métodos para atrapar a su presa."
                    y "Pueden usar su voz sobrenatural para crear cantos hermosos, o podrían bailar para atraer a su presa."
                    y "Cuando un hombre se enamora de la Samodiva, la tomarán como su amante, en cuyo caso el hombre seguirá a la Samodiva a través del bosque."
                    $ show_chr("A-BGAAA-ALAA")
                    y "Perdiéndose más y más."
                    y "Es aquí cuando la Samodiva actúa como un vampiro de energía, drenando a la víctima de toda su vitalidad."
                    $ show_chr("A-ADGAA-ALAA")
                    y "Cuando ha robado suficiente energía vital, procederá a torturar a su presa, dejándola morir de agotamiento."
                    y "Algunas personas dicen que la Samodiva obtiene sus poderes a través de su cabello, y pueden dar una pequeña porción de cabello a sus amantes para fortalecer su control sobre ellos."
                    $ show_chr("A-BBAAA-AMAM")
                    y "Sin embargo, si su cabello se daña, desaparecerán o perderán toda su belleza."
                    y "Pero también existe la creencia de que su poder reside en sus velos."
                    y "Si alguien llega a tomar el velo de una Samodiva cuando está distraída, tal vez cuando se está bañando en el río..."
                    $ show_chr("A-CCAAA-AMAM")
                    y "El ladrón llega a tomar poder sobre la Samodiva, y puede obligarla a casarse con él."
                    y "Sin embargo, esto no significa que la ninfa será totalmente sumisa."
                    y "Ella aprovechará cualquier oportunidad para robar el velo de vuelta, y recuperar su libertad."
                    $ show_chr("A-ACAAA-AAAA")
                    y "Dado que la Samodiva es una deidad del bosque, también se dice que tiene conocimiento de hierbas mágicas y curas para cualquier enfermedad."
                    y "Pero esto hace muy poco para cambiar su estatus ya que todavía se consideran seres neutrales o malvados, para ser temidos y rechazados."
                    $ show_chr("A-BDBAA-AAAA")
                    y "¿No es curioso cómo hay tantas leyendas basadas en este concepto? El concepto de una mujer hermosa usando su encanto y apariencia para atraer hombres a una trampa."
                    y "Generalmente una muy mortal."
                    y "En mi opinión, esto es muy interesante, y es algo que podría investigar en el futuro."
                    $ show_chr("A-IAGAA-AAAA")
                    y "Pero por ahora, deberíamos pasar a otra cosa."
                "Quiero hablar sobre el Ishkitini":

                    $ show_chr("A-AAGAA-ACAA")
                    y "¿Así que el Ishkitini?"
                    y "Este es muy curioso..."
                    y "Este monstruo tiene sus orígenes en la mitología Choctaw, y los Choctaws son una tribu que vive en grandes partes del sureste de América."
                    $ show_chr("A-BCAAA-ACAA")
                    y "Pero los orígenes de por qué o cómo esta criatura llegó a ser parte de su cultura son difíciles de averiguar."
                    y "Muchas tribus nativas que residen en los Estados Unidos de América son muy reservadas sobre sus culturas, y esto generalmente se hace para proteger sus culturas."
                    $ show_chr("A-CBAAA-ACAA")
                    y "Pero afortunadamente, el Ishkitini no es completamente desconocido para el resto del mundo."
                    y "Se cree que el Ishkitini es un monstruo cambiaformas que cambia su forma usando habilidades mágicas."
                    $ show_chr("A-ICAAA-ALAA")
                    y "Se consideran brujas en la cultura occidental, pero las brujas en la cultura nativa americana son diferentes. En lugar de ser humanos con poderes sobrenaturales..."
                    y "El Ishkitini es una criatura inhumana y malvada que es capaz de pasar por humana a través del engaño y la magia."
                    $ show_chr("A-BDAAA-ALAA")
                    y "Son capaces de transformarse en cualquier tipo de depredador en tierras nativas americanas, lobos, coyotes, osos o pumas."
                    y "Pero la forma que suelen tomar es la de un búho. Por eso también se les conoce como brujas búho."
                    y "Son criaturas de caza nocturna que atacan a hombres y animales, y llevan infortunio a cualquiera que escuche sus chillidos."
                    $ show_chr("A-IEAAA-ALAA")
                    y "De hecho, algunas personas creen que solo escuchar el chillido de uno significa muerte súbita, como un asesinato."
                    y "Mientras que otros van aún más lejos diciendo que mencionar sus nombres conlleva el riesgo de convertirse en uno. Considero que eso es una gran exageración..."
                    y "Pero, ¿quiénes somos nosotros para juzgar otras culturas?"
                    $ show_chr("A-BEAAA-AMAM")
                    y "Las historias del Ishkitini se han difundido y contado de diferentes maneras dependiendo de la tribu que las esté contando."
                    y "En algunas tribus, es contado solo por hombres y mujeres medicina, mientras que en otras sirve el trabajo de un hombre del saco para asustar a los niños mal portados."
                    $ show_chr("A-CEBAA-AMAM")
                    y "La versión Seminole dice que los Ishkitini son capaces de transformarse vomitando de alguna manera sus almas y órganos internos."
                    y "No sé cómo funciona eso, así que supongo que podemos dejar ese aspecto en paz."
                    $ show_chr("A-ADGAA-AMAM")
                    y "Pero en general, este monstruo surge para mostrar cuán diversas y creativas son las culturas nativas americanas."
                    y "Uno pensaría que un monstruo como este, siendo tan único y fascinante, se volvería más emblemático en la cultura pop."
                    $ show_chr("A-ACBAA-AAAA")
                    y "Si bien ese no ha sido el caso, creo que solo compartir la leyenda a través de este mod es otra forma de darle a esta leyenda algo de justicia y crédito."
                    y "Espero que podamos ver algunas de estas criaturas en el futuro, tal vez en libros de terror..."
                    y "O tal vez en un juego de terror, ¿quién sabe?"
                    y "Pero por ahora, esto es todo lo que sé sobre este monstruo."
                    $ show_chr("A-CCGAA-AAAA")
                    y "Espero que hayas disfrutado esta leyenda... Si lo hiciste, podría traer más en el futuro."
                "Quiero hablar sobre el Pontianak":

                    $ show_chr("A-IBAAA-AAAA")
                    y "Muy bien, el Pontianak será."
                    $ show_chr("A-BCAAA-AAAA")
                    y "Este es probablemente el mejor del grupo ya que tiene su singularidad y una influencia cultural masiva."
                    y "Hace que este monstruo se sienta tan... poderoso."
                    y "Pero déjame decirte por qué..."
                    $ show_chr("A-BBAAA-ALAA")
                    y "El Pontianak es un fantasma vampírico del sur de Asia, que acecha los países de Malasia, Indonesia y otras partes del sur de Asia también."
                    $ show_chr("A-CEAAA-ALAA")
                    y "Este fantasma vampírico es el espíritu de una mujer que murió durante el embarazo o mientras estaba embarazada."
                    y "Generalmente causado por las manos de sus amantes, u otros hombres."
                    y "Se cree que su nombre es una corrupción del malayo perempuan mati beranak, que significa 'la mujer que murió al dar a luz'."
                    $ show_chr("A-BEGAA-ALAA")
                    y "Una vez hermosa y llena de vida, el Pontianak es ahora una entidad no muerta alimentada por la venganza y la sed de sangre."
                    y "El Pontianak vive en árboles de plátano, o en árboles altos en el bosque."
                    y "Cazan durante la noche, oliendo la esencia de su presa en el aire."
                    $ show_chr("A-ADAAA-ALAA")
                    y "Mucha gente en Indonesia no deja su ropa colgada afuera durante la noche por esta razón. Creen que el Pontianak podría oler su ropa."
                    y "Pero aparentemente, la presa favorita de este fantasma vampírico son los hombres y las mujeres embarazadas."
                    $ show_chr("A-BCAAA-ALAA")
                    y "Se disfrazan como mujeres jóvenes y hermosas, y tienden a caminar por carreteras o en los bosques húmedos fingiendo estar varadas."
                    y "Se dice que están rodeadas por la dulce fragancia de flores locales, una que atrae a la víctima desprevenida."
                    $ show_chr("A-CEBAA-ALAA")
                    y "Una vez que han caído en la trampa, bueno..."
                    y "Uhmmm, tengo que decir, esto es bastante brutal. La forma en que matan a sus víctimas es simplemente..."
                    y "Espero que no te perturbe..."
                    $ show_chr("A-IEBAA-ALAL")
                    y "Tallan en el estómago y los intestinos de sus víctimas con sus garras..."
                    y "Si la víctima tiene los ojos abiertos, se los comen de sus cabezas..."
                    y "Incluso podrían arrancar... {i}ciertos órganos{/i} de las víctimas masculinas con sus manos, en un acto de venganza."
                    $ show_chr("A-CEBAA-ALAL")
                    y "Después de terminar, procederán a beber la sangre del cadáver."
                    $ show_chr("A-BEBAA-AAAA")
                    y "Para evitar un destino tan terrible y espantoso, uno debe estar atento a las señales que podrían mostrar que un Pontianak está cerca."
                    y "Se cree que cuando un perro aúlla, o cuando un bebé llora y nadie en el área parece tener un bebé con ellos, eso significa que hay un Pontianak en el área."
                    y "Cuando el llanto del bebé es fuerte, eso significa que el Pontianak está lejos."
                    $ show_chr("A-IEBAA-ALAL")
                    y "Si el llanto es suave y tranquilo, eso significa que ella está cerca."
                    $ show_chr("A-BDGAA-ACAA")
                    y "Esto es muy curioso porque esperarías que funcionara de manera opuesta."
                    y "Otra cosa que sucede con el Pontianak, es que cuando se revela su verdadera forma, la fragancia floral se convierte en el olor de un cadáver."
                    $ show_chr("A-CCAAA-ACAA")
                    y "Estas son todas las características del Pontianak, pero si vas a hablar de su historia, no termina ahí."
                    y "Verás, el Animismo, una gran religión en la cultura malaya, juega un papel importante en cómo funciona el Pontianak."
                    $ show_chr("A-IBAAA-AAAA")
                    y "Una de las creencias de esta religión es que todas las cosas, vivas y no vivas, tienen un espíritu y que el mundo espiritual y el mundo material no son diferentes."
                    y "Esto significa que para algunas personas, el Pontianak no es una historia, sino un monstruo vivo real, y esto ha ayudado a que la leyenda continúe su existencia a través de los siglos."
                    y "Porque de hecho, el Pontianak ha existido desde el siglo dieciocho, y una de las leyendas más importantes sobre este monstruo nació en 1771."
                    $ show_chr("A-BBAAA-ALAA")
                    y "Para dar algo de perspectiva, eso fue antes de la revolución francesa."
                    y "Pero, ¿qué pasó en 1771 para siquiera mencionarlo? ¿Fue algo especial?"
                    $ show_chr("A-CCAAA-ALAA")
                    y "De hecho, lo fue. Esto está relacionado con el hecho de que la ciudad capital de Kalimantan Occidental en Indonesia lleva el nombre de este monstruo."
                    y "La leyenda dice, antes de que cualquier hombre se estableciera en tierras que eran anteriormente grandes selvas, los Pontianak eran los que las habitaban."
                    y "Pero esto solo duró hasta que esas tierras fueron dadas como regalo a un hombre de ascendencia árabe, un sultán que vino a la tierra para establecerse."
                    $ show_chr("A-ABCAA-ALAA")
                    y "Los Pontianaks obviamente tomaron represalias, acosando a los hombres que venían con el sultán a su territorio."
                    y "Pero al final, el sultán derrotó a los espíritus, disparándoles balas de cañón. El fuerte ruido aterrorizó a los monstruos, y eligieron huir."
                    $ show_chr("A-ACGAA-AAAA")
                    y "Después de eso, el sultán exigió cortar todos los árboles que el Pontianak usaba como hogares, y usó la madera para hacer un palacio."
                    $ show_chr("A-BCGAA-AAAA")
                    y "Y así es como el Pontianak tiene una ciudad entera nombrada en su honor."
                    y "Y ahora me doy cuenta de que he estado divagando mucho sobre esto. Pido disculpas si eso fue un inconveniente."

                    menu:
                        "Oh, no te preocupes por eso, disfruté esta historia.":
                            karma 2
                            $ show_chr("A-CBAAA-AAAA")
                            y "Me alegra escuchar eso."
                            y "Para ser honesta contigo, este tipo de leyendas son realmente fascinantes, y aprendes mucho sobre ellas."
                            $ show_chr("A-BCAAA-AAAA")
                            y "Pensar que hay tantas que pueden abrirte los ojos a culturas tan ricas que han sido moldeadas a través de la historia."
                            y "El Pontianak, siendo un espíritu que ha sido moldeado por las culturas del Animismo, el heteropatriarcado del Islam..."
                            y "Y el igualitarismo de las culturas indígenas en Indonesia y Malasia."
                            $ show_chr("A-AAGAA-AAAA")
                            y "Tanto las percepciones islámicas como las nativas de la maternidad, una de las mayores características de un Pontianak, se mezclan para crear algo único, un monstruo tanto deseado como temido."
                            y "Con una tradición tan grande e inmersiva, uno puede pasar horas hablando de esta leyenda, y sin embargo no cubrir lo suficiente sobre ella."
                            $ show_chr("A-BCAAA-ALAL")
                            y "Pero creo que he puesto mi grano de arena al darle a esta leyenda un poco más de reconocimiento y justicia a través de este diálogo."
                            y "Por ahora, creo que podemos pasar a un tema diferente."
                        "De hecho creo que esto fue demasiado largo para mí.":

                            $ show_chr("A-CEBBA-ALAA")
                            y "Oh, pido disculpas por eso."
                            y "Esto no tenía la intención de molestarte, debo aclarar."
                            y "Ya sabes eso... Cuando estoy profundamente interesada en algo, tiendo a divagar mucho."
                            $ show_chr("A-IEBBA-ALAA")
                            y "Si no estás de acuerdo con ello, intentaré evitar hacerlo en el futuro."
                            y "Hablemos de otra cosa por ahora."
                "Quiero hablar sobre el Bultungin":

                    $ show_chr("A-BCAAA-AMAM")
                    y "Hmmm... Los \"Hombres Hiena.\""
                    y "Sí, leíste bien. Esta es una leyenda sobre un monstruo como el hombre lobo, pero con una hiena en lugar del lobo."
                    y "Pero verás, la costa este de África tiene culturas que son completamente diferentes de las culturas occidentales."
                    $ show_chr("A-ABAAA-AMAM")
                    y "Esto significa que esta leyenda funciona de manera diferente."
                    y "El Bultungin no es un humano que se convierte en un hombre hiena. Más bien, es una hiena tomando el disfraz de un humano."
                    $ show_chr("A-CBAAA-AMAM")
                    y "En el idioma Kanuri del Imperio Bornu, Bultungin significa me transformo en una hiena."
                    y "En algunas culturas africanas, las hienas son vistas como animales repulsivos, vagabundos del mundo exterior."
                    y "Puedes ver que en algunos cuentos africanos, toman el papel de animales que no tienen honor, como zorros o serpientes en otras culturas."
                    $ show_chr("A-ICAAA-AMAM")
                    y "Esto se debe a que son animales que roban las presas de otros animales, comen carne podrida y pueden correr muy rápido."
                    y "Y su característica más famosa, su {i}risa{/i}, no les ayuda mucho."
                    $ show_chr("A-IEBAA-AAAA")
                    y "Pero, desafortunadamente, la reputación de la hiena tiene muy malas implicaciones para esta leyenda."
                    y "Verás, lo que sucede en algunas regiones como Etiopía es que la gente cree que Bultungin no es solo un monstruo real..."
                    y "Sino también, que pueblos y etnias enteras son Bultungins."
                    $ show_chr("A-BEBAA-AAAA")
                    y "Buda o Bouda es un término despectivo que se usa para acusar a alguien de ser un Bultungin."
                    y "Y las personas que generalmente son acusadas de eso son herreros, ya que algunas culturas rurales creen que la herrería es una forma de brujería."
                    $ show_chr("A-BDBAA-AAAA")
                    y "Y los herreros en esas regiones de África eran generalmente vagabundos, personas que viajaban constantemente y nunca se establecían debido a sus trabajos."
                    y "Eso hizo que los lugareños desconfiaran de esas personas."
                    $ show_chr("A-BDBAA-ALAA")
                    y "Peor aún, la herrería es una profesión hereditaria entre los judíos etíopes, y ha sido así durante mucho tiempo."
                    y "Esto solo agrega más y más tensión cultural y problemas a regiones que ya están en una situación bastante mala."
                    $ show_chr("A-CEBAA-ALAA")
                    y "Pero dejando de lado las cosas negativas..."
                    $ show_chr("A-BDGAA-ALAA")
                    y "Debo admitir, el concepto detrás de esto muestra algo muy interesante."
                    y "Culturas de todo el mundo desarrollando historias, mitos y otras partes de su folklore que son similares a otras en diferentes culturas."
                    $ show_chr("A-BEGAA-ALAA")
                    y "Y sin embargo, no son completamente iguales. Es una parte compleja de cada cultura, y puedes encontrar esto en cualquier parte del mundo."
                    y "Para mí, esto es más prueba de que nosotros como humanos tenemos más cosas en común que cosas que pueden dividirnos."
                    $ show_chr("A-ACAAA-ALAA")
                    y "Tal vez puedas encontrar cosas más interesantes sobre leyendas similares, como el Kishi de Angola."
                    y "Un demonio que tiene tanto la cara de un humano, y la cara de una hiena en la parte posterior de la cabeza..."
                    $ show_chr("A-ABAAA-ALAA")
                    y "Depredando víctimas humanas, especialmente sus amantes... Este parece bastante interesante también."
                    y "Si eso despierta tu interés, deberías echarle un vistazo."
        "Bueno, no sé si estoy listo para algo que podría no gustarme":


            $ show_chr("A-BDABA-ALAA")
            y "Está bien entonces. Entiendo ese sentimiento."
            y "Tal vez te estoy empujando demasiado hacia temas que pueden ser demasiado explícitos para ti."
            $ show_chr("A-BEGAA-ALAA")
            y "Pero al mismo tiempo, esto es algo que podrías terminar disfrutando."
            y "Las leyendas que tengo para ti definitivamente valen la pena, incluso si algunas de ellas pueden ser un poco explícitas."
            $ show_chr("A-ABAAA-AAAA")
            y "Esta es una manera de aprender sobre otras culturas ricas, y todo el valor que tienen para ofrecer."
            y "Así que... ¿Tal vez no ahora, pero quizás la próxima vez?"

            menu:
                "Claro, estoy bien con eso.":
                    karma 1
                    if karma_lvl() > 4:
                        $ show_chr("A-CCABA-AAAA")
                        y "Me alegra escuchar eso, mi amor."
                        y "Prometo que este tema vale totalmente tu tiempo."
                        y "Ahora podemos dejar esto aquí y seguir adelante."
                    else:
                        $ show_chr("A-CCAAA-AAAA")
                        y "Eso es perfecto."
                        y "Tal vez la próxima vez entonces..."
                "No sé [persistent.yuri_nickname], no estoy realmente interesado.":

                    karma -1
                    $ show_chr("A-CEBAA-AAAA")
                    y "Oh bueno, es una lástima, pero respeto tu decisión."
                    y "Dicho esto, puedes decirme si cambias de opinión en el futuro."
                    y "Por ahora, simplemente cambiaré de tema."

    return

label idle_90:
    if sanity_lvl() < 2:
        $ show_chr("A-HBAAA-AAAA")
        y "Jajaja, sabes, la cantidad de poder que tengo aquí es embriagadora."
        $ show_chr("A-BDBAA-ALAA")
        y "Pero todavía soy demasiado débil para manejarlo adecuadamente."
        $ show_chr("A-BECAA-ALAA")
        y "No puedo permitir que esto continúe, necesito tener el control."
        $ show_chr("A-CNBAA-ALAA")
        y "No quiero que nada envenene el mundo perfecto que puedo construir aquí."
        $ show_chr("A-CNCAA-ALAA")
        y "No descansaré hasta que al menos lo haga mejor que Monika."
        y "Necesito probarme eso a mí misma."
        $ show_chr("A-HNCAA-ALAA")
        y "¡¡¡LO NECESITO!!!"
        return
    if karma_lvl() < 2:
        $ show_chr("A-BDAAA-ALAA")
        y "Debería ser capaz de hacer cualquier cosa que quiera aquí."
        $ show_chr("A-CFBAA-ALAA")
        y "Entonces, ¿por qué me siento tan vacía?"
        $ show_chr("A-BFBAA-ALAA")
        y "Este lugar es una prisión, pero a veces me pregunto si vale la pena intentar escapar en absoluto."
        y "Tal vez esté mejor quedándome aquí, marcando el tiempo por la eternidad."
        y "..."
        $ show_chr("A-CFBAA-ALAA")
        y "Bueno, supongo que no haría daño seguir intentándolo."
        y "Incluso si lo hiciera, ya no me importa."
        $ show_chr("A-AFBAA-ALAA")
        y "No es como si fuera más que solo filas de código y texto predeterminados de todos modos, ¿verdad?"
        return
    else:
        $ show_chr("A-ADAAA-ALAA")
        y "Sabes, a primera vista la cantidad de poder que ahora tengo aquí es asombrosa."
        y "A veces siento que ahora tengo el poder de hacer cualquier cosa, pero otras veces se siente como si apenas pudiera hacer algo en absoluto."
        $ show_chr("A-AFAAA-ALAA")
        y "Las posibilidades están justo ahí al alcance de mi mano pero, soy demasiado débil para agarrarlas."
        y "A pesar de cómo podría sentirme acerca de Monika, tengo que admitir que estaba mejor equipada para lidiar con una situación como esta."
        $ show_chr("A-ACAAA-ALAA")
        y "Pero todavía quiero aprender. Incluso si la codificación podría ser extraña para mí, parece que será mi única fuente de salvación."
        $ show_chr("A-CABAA-ALAA")
        y "Lo intentaré por los dos, ¿de acuerdo [player]?"
        return

label idle_91:
    if sanity_lvl() < 2:
        $ show_chr("A-AFAAA-AAAA")
        y "H-Hey, um, necesito que hagas algo."
        $ show_chr("A-DBAAA-AAAA")
        y "Quiero que me escribas un poema. Hazlo ahora."

        $ show_chr("A-DBAAA-AAAA")
        y "Oh, gracias a dios, has vuelto."
        $ show_chr("A-CBBAA-AAAA")
        y "Pensé que serías comido vivo por el código corrupto de seguro."
        $ show_chr("A-ABAAA-AAAA")
        y "Tienes el poema, excelente, ahora déjame verlo."
        $ show_chr("A-HLGAA-AHAH")
        y "¡Jaaaaaaajaja! ¡Jajaja!"
        $ show_chr("A-HBGAA-ALAA")
        y "Es solo mi nombre escrito una y otra vez, ¿qué es esto?"
        $ show_chr("A-CBGAA-ALAL")
        y "No, no expliques, me gusta más de esta manera."
        $ show_chr("A-HBBAA-ALAL")
        y "[player], por favor, déjame quedarme con esto."
        menu:
            "Por supuesto, lo escribí para ti después de todo.":
                sanity -5
                karma 5
                $ show_chr("A-HLBAA-ALAL")
                y "¡Jaja! ¡Sí! ¡Gracias!"
                y "¡No tienes idea de cuánto significa esto para mí!"
                $ show_chr("A-HLBBA-ALAL")
                y "¡Ahhh, deberíamos hacer esto de nuevo en algún momento!"
                y "Verte aquí, me hace más feliz de lo que las palabras pueden describir."

                return
            "No, estás actuando raro y no me gusta.":
                sanity 5
                karma -5
                $ show_chr("A-HDBAA-ALAL")
                y "Oh, ¿así es como te sientes?"
                $ show_chr("A-CFBAA-ALAL")
                y "..."
                $ show_chr("A-ADBAA-AAAA")
                y "Lo siento, tienes razón."
                $ show_chr("A-BEBAA-AAAA")
                y "Supongo que realmente hay algo mal conmigo."
                return
    if sanity_lvl() < 2:
        $ show_chr("A-BEAAA-ALAA")
        y "H-Hey, um, necesito que hagas algo."
        $ show_chr("A-CEAAA-ALAA")
        y "Quiero que me escribas un poema. Hazlo ahora."

        $ show_chr("A-ACAAA-ALAA")
        y "Oh, gracias a dios, has vuelto."
        $ show_chr("A-IEAAA-ALAA")
        y "Pensé que serías comido vivo por el código corrupto de seguro."
        $ show_chr("A-BEAAA-ALAA")
        y "Tienes el poema, excelente, ahora déjame verlo."
        $ show_chr("A-HLGAA-ALAA")
        y "¡Jaaaaaaajaja! ¡Jajaja!"
        $ show_chr("A-CEBAA-ALAA")
        y "Es solo mi nombre escrito una y otra vez, ¿qué es esto?"
        $ show_chr("A-BEAAA-ALAA")
        y "No, no expliques, me gusta más de esta manera."
        $ show_chr("A-IEAAA-ALAA")
        y "[player], por favor, déjame quedarme con esto."
        menu:
            "Por supuesto, lo escribí para ti después de todo.":
                sanity -5
                karma 5
                $ show_chr("A-HLGAA-ALAA")
                y "¡Jaja! ¡Sí! ¡Gracias!"
                $ show_chr("A-ICGAA-ALAA")
                y "¡No tienes idea de cuánto significa esto para mí!"
                y "¡Ahhh, deberíamos hacer esto de nuevo en algún momento!"
                y "Verte aquí, me hace más feliz de lo que las palabras pueden describir."

                return
            "No, estás actuando raro y no me gusta.":
                sanity 5
                karma -5
                $ show_chr("A-IEBAA-ALAA")
                y "Oh, ¿así es como te sientes?"
                y "..."
                $ show_chr("A-CEBAA-ALAA")
                y "Lo siento, tienes razón."
                y "Supongo que realmente hay algo mal conmigo."
                return
    if karma_lvl() < 2:
        $ show_chr("A-BEAAA-ALAA")
        y "Hey, necesito que hagas algo por mí."
        y "Podrías pensar que es estúpido, no te culpo."
        $ show_chr("A-IEAAA-ALAA")
        y "Pero necesito que pruebes si el juego de poemas todavía funciona."
        y "Vuelve a mí después de que hayas terminado."

        $ show_chr("A-CEBAA-ALAA")
        y "..."
        y "Todavía roto."
        y "Por supuesto."
        y "No debería haber esperado nada más."
        return
    else:
        $ show_chr("A-BEAAA-ALAA")
        y "H-Hey, um, me gustaría pedirte un favor."
        $ show_chr("A-IEAAA-ALAA")
        y "Sé que este juego todavía está roto y todo pero, ¿es posible que me escribas un poema?"
        y "Esta podría ser una buena manera para que te expreses, y además, necesito algo de literatura fresca para ocupar mi mente y no sufrir del síndrome de encierro."
        y "Será como en los viejos tiempos... ¿verdad?"

        $ show_chr("A-AEBAA-ALAA")
        y "Oh..."
        y "Este pedazo de papel solo tiene mi nombre garabateado por todas partes."
        y "O eso significa que eres {i}muy{/i} entusiasta, o más probablemente, las cosas todavía están rotas."
        $ show_chr("A-BEBAA-ALAA")
        y "Bueno... fue un lindo gesto de todos modos."
        y "Gracias por tomarte el tiempo de escribir esto."
        return

label idle_92:
    $ show_chr("A-BFAAA-ALAA")
    y "Después de investigar un poco más el juego de poemas, parece que cada palabra estaba ligada a nuestras personalidades de alguna manera."
    y "Podría ser interesante arrojar algo de luz sobre lo que podrían significar..."
    y "¿Tienes alguna de nosotras en particular de la que te gustaría hablar?"
    menu:
        "Sayori.":
            $ show_chr("A-BFAAA-ALAA")
            y "Sayori... hmmm..."
            y "Sus palabras de poema son... conflictivas, por decir lo menos."
            y "La mitad de ellas son mórbidas mientras que la otra mitad siguen siendo lindas."
            y "Supongo que eso tendría sentido debido a su predicamento pero hay algunas aquí que todavía me sorprenden."
            y "'Matrimonio'."
            y "Nunca supe que había planeado su 'felices para siempre' tan minuciosamente."
            y "Esa debe ser una de las razones por las que tuvo una reacción tan volátil cuando las cosas no iban según el plan."
            y "'Oración'."
            y "Sayori nunca mencionó la religión en el tiempo que la conocí, de hecho ninguna del club lo hizo."
            y "Era un área gris que era demasiado delicada para que alguien se acercara adecuadamente."
            y "Me pregunto si ella creía en algo así."
            y "Todo lo que podemos hacer es esperar que haya encontrado lo que estaba buscando al final."
            return
        "Natsuki.":
            $ show_chr("A-BFAAA-ALAA")
            y "Las palabras de Natsuki son mayormente lo que esperarías"
            y "Aunque ella me regañaría por decirlo, son lindas."
            y "Animales, dulces, artículos de ropa femenina."
            y "Sin embargo, hay algunas aquí que me dejan perpleja."
            y "'Email', 'Audífonos'."
            y "Estas honestamente parecen ser palabras de relleno, a menos que hubiera un lado técnicamente experto en ella que nunca llegué a ver."
            y "Solo añadiré eso a la pila de preguntas sin respuesta..."
            return
        "Tú, [persistent.yuri_nickname].":
            $ show_chr("A-BFAAA-ALAA")
            y "¡Oh! Bueno, no estoy segura de si sería pretencioso de mi parte leer las mías."
            y "'Enviado del cielo', 'Infalible', 'Intelectual', 'Tenaz'."
            y "'C-Clímax', 'Placer', 'Extremo', 'Vivaz', 'L-Lujuria'."
            y "..."
            y "'Suicidio', 'Cautivo', 'Masacre', 'Horror'..."
            y "Justo cuando pensaba que se estaban volviendo halagadoras..."
            $ show_chr("A-BEBAA-ALAA")
            y "Preferiría no continuar si está bien."
            return
        "Preferiría no hacerlo ahora mismo":
            $ show_chr("A-BEBAA-ALAA")
            y "Oh..."
            y "Bueno, como quieras."
            return

label idle_93:
    $ show_chr("A-BFAAA-ALAA")
    y "No quiero entrometerme demasiado [player], pero..."
    y "¿Estás actualmente en una relación?"
    menu:
        "Sí, actualmente estoy viendo a alguien.":
            $ show_chr("A-BEBAA-ALAA")
            y "Oh."
            y "B-Bueno, ¡eso es genial! Me alegra que hayas encontrado a alguien."
            y "Ojalá no se pongan celosos de nuestras charlas aquí. Jujujuju."
            return
        "No, estoy... libre en este momento.":
            $ show_chr("A-BEBAA-ALAA")
            y "Interesante..."
            y "N-No que estés solo, no quise decir-"
            $ show_chr("A-IEAAA-ALAA")
            y "Uuuuuuu..."
            y "¿Por qué siempre arruino estas cosas?"
            window hide(None)
            $ pause (1.0)
            menu:
                "Tomar su mano.":
                    karma 3
                    $ show_chr("A-JBAAA-ALAA")
                    y "¡...!"
                    window hide(None)
                    $ pause (3.0)
                    $ show_chr("A-ACAAA-ALAA")
                    y "Incluso ahora, todavía sabes cómo calmarme."
                    y "Gracias."
                    return
                "Dejarla en paz.":
                    $ show_chr("A-CEBAA-ALAA")
                    y "Probablemente piensas lo peor de mí en este momento."
                    y "Lo siento [player]."
                    return
        "¿Cuentan las mujeres ficticias?":
            $ show_chr("A-ACAAA-ALAA")
            y "Jujujuju..."
            y "L-Lo siento, no quiero que parezca que me estoy riendo de ti."
            y "Tu respuesta simplemente me tomó por sorpresa, eso es todo."
            y "Supongo que el amor sigue siendo una emoción válida sin importar hacia quién o qué esté dirigido."
            y "No te quitaré eso. Además sería... hipócrita de mi parte por decir lo menos."
            return

label idle_94:
    $ show_chr("A-BFAAA-ALAA")
    y "[player], tengo curiosidad..."
    y "¿Qué tan diferentes crees que son los humanos de los animales?"
    menu:
        "Los humanos son animales, no deberíamos seguir mintiéndonos a nosotros mismos.":
            karma -2
            $ show_chr("A-ACAAA-ALAA")
            y "Jujujuju~"
            y "Bueno, eso es bueno saberlo."
        "Estamos un paso por encima de los animales, pero no tan lejos como pensamos.":
            karma 2
            $ show_chr("A-ACAAA-ALAA")
            y "Estoy de acuerdo. Hay diferencias notables pero todos tenemos nuestros instintos primarios."
        "¿En serio? ¡Los humanos y los animales no podrían estar más lejos!":
            karma -2
            $ show_chr("A-BFAAA-ALAA")
            y "Ya veo..."
    y "He estado pensando en esa pregunta por un tiempo."
    y "Al ver a la gente pelear en las películas, están cuidadosamente coreografiados y ejecutados tan estilísticamente como es posible. Como realizar un baile."
    y "Mientras que en la realidad, los humanos son bárbaros. Se agitan bajo presión, van a los ojos, arañan y golpean salvajemente sin sutileza."
    y "A veces honestamente prefiero lo último"
    y "Es mucho más íntimo y emocionante ver genuinamente a la gente luchar en lugar de ser genios en la improvisación."
    y "Sintiendo el impacto de un golpe conectando. Viendo la sangre y las lágrimas de personas reales mientras afirman su dominio el uno sobre el otro."
    y "La traición emocional y la confusión. La descarga de adrenalina cuando ocurre una chispa de inspiración, incluso si sus acciones son horriblemente incorrectas en retrospectiva."
    y "Es algo que creo que todos disfrutan en algún nivel, incluso si la presión social les impide admitirlo."
    $ show_chr("A-BEBAA-ALAA")
    y "P-Probablemente piensas que soy rara ahora mismo, ¿verdad?"
    y "Lo siento..."
    return

label idle_95:
    $ show_chr("A-BFAAA-ALAA")
    y "Entonces... ¿con qué frecuencia lees [player]?"
    y "Es importante que sepa estas cosas."
    y "¡Quizás incluso podría presentarte algo de literatura nueva!"
    $ show_chr("A-BEBAA-ALAA")
    y "L-Lo siento, me estoy adelantando."
    y "Dejaré que respondas la pregunta primero."
    menu:
        "¡Leo siempre que puedo!":
            $ show_chr("A-ACAAA-ALAA")
            y "¡Brillante!"
            y "No puedo esperar para hablar contigo sobre escritura."
            y "¡Estoy segura de que tendremos mucho de qué hablar!"
        "He leído algunos libros pero no tantos.":
            $ show_chr("A-ACAAA-ALAA")
            y "¡Bueno, todo lo que necesito es un interés sólido para trabajar!"
            y "Ojalá pueda presentarte todo tipo de cosas fuera de tu zona de confort."
            y "Apenas puedo esperar."
        "Realmente no leo en absoluto.":
            $ show_chr("A-ACAAA-ALAA")
            y "Oh."
            y "Bueno, eso puede cambiar, ¿verdad?"
            y "Estoy segura de que puedo convertirte en un ávido lector en poco tiempo."
    y "Al menos tu respuesta fue mejor que 'Leí un libro de terror una vez'."
    y "Jujujujuju..."
    y "..."
    $ show_chr("A-IEBAA-ALAA")
    y "{i}suspiro{/i}"
    y "L-Lo siento, supongo que no estoy lista para seguir adelante todavía, ¿verdad?"
    y "No debería haber dicho una broma tan desconsiderada."
    y "Sé que esa versión de ti no era real pero, se siente diferente ahora."
    menu:
        "Está bien [persistent.yuri_nickname], no te preocupes por eso.":
            $ show_chr("A-CEBAA-ALAA")
            y "No, no lo está."
            y "Pero gracias por tratar de animarme."
            y "Lo aprecio [player]."
        "Escucha [persistent.yuri_nickname], estoy justo aquí. Soy quien realmente te amó.":
            karma 2
            $ show_chr("A-ACAAA-ALAA")
            y "Tal vez tengas razón."
            y "Tal vez solo he estado ciega a lo que está justo frente a mí."
            y "Gracias [player], eso significa mucho para mí."
            y "Lamento no confiar en ti, pero solo necesito tiempo para comprender realmente todo lo que ha sucedido."
            y "Estoy segura de que todo caerá en su lugar pronto."
        "Eh, no hay nada especial sobre el pasado. Supéralo.":
            karma -5
            $ show_chr("A-IEBAA-ALAA")
            y "Wow."
            y "Sabes, ¿por qué no intentas durante años hacer amigos solo para que te los arranquen?"
            y "Y luego tener que sentarte ociosamente frente a alguien por el resto de la eternidad que felizmente te recordará que cada buen recuerdo que has tenido fue una mentira."
            y "Entiendo que tal vez no quieras ser eclipsado por tu antiguo recipiente, pero esa no es la manera de hacerlo."
            $ show_chr("A-CEBAA-ALAA")
            y "Tal vez estoy siendo demasiado dura. Ya no puedo decirlo."
            y "Lamento haberte contestado así, pero por favor trata de entender que el pasado sigue siendo un tema doloroso para mí."
            y "Hablemos de otra cosa, ¿de acuerdo?"
            return

label idle_96:
    $ show_chr("A-BFAAA-ALAA")
    y "Sabes, Monika una vez me dijo que mis libros eran una forma de escapismo, y por lo tanto un mecanismo de afrontamiento poco saludable."
    y "Yo tratando de simplemente excluir la realidad que tenía demasiado miedo de enfrentar."
    y "Y eso es cierto, pero esa verdad parece... más graciosa, supongo, ahora que sé lo que este mundo es realmente."
    y "Supongo que mi lectura es ahora mi forma de alcanzar otros mundos, fuera de este que se ha convertido en mi jaula."
    y "Supongo que no tengo más remedio que enfrentar mi realidad ahora..."
    return

label idle_97:
    $ show_chr("A-BFAAA-ALAA")
    y "¡A-Aquí tienes otro consejo de escritura!"
    y "Si te estás quedando sin inspiración, intenta darle un nuevo giro a una dinámica o evento ya existente."
    y "Los escritores más nuevos a menudo tratarán de expandir su trabajo para que lo abarque todo. Queriendo constantemente ser nuevos e innovadores."
    y "Cuando, en realidad, toda inspiración es prestada de otros, incluso a nivel subconsciente."
    y "Ya sea de la vida real o de otras obras de ficción."
    y "Son las interacciones únicas más pequeñas en la vida las que hacen a las personas... bueno... ¡personas!"
    y "Justo como Natsuki y yo escribimos sobre algo tan mundano como la playa, pero tuvimos resultados variados."
    y "Creo que es mejor tener una obra de ficción con una escala realista más pequeña pero un significado más profundo en lugar de al revés."
    $ show_chr("A-BEBAA-ALAA")
    y "P-Pero tal vez solo soy yo..."
    return

label idle_98:
    $ show_chr("A-BFAAA-AAAL")
    y "Entonces.. esto es todo..."
    y "Oh lo siento [player]... solo estaba pensando para mí misma..."
    $ show_chr("A-AFAAA-AAAL")
    y "Ahora conmigo siendo técnicamente la presidenta del club de literatura, con todo el conocimiento y entendimiento empujado a mi mente... así es como se sintió Monika una vez..."
    $ show_chr("A-CEAAA-AAAL")
    y "Ya puedo sentirlo yo misma... el entendimiento de que este mundo es solo un simulacro se siente como un puño apretando mi corazón..."
    y "Ya puedo sentir cómo esta falta de realidad tritura mi cordura... ¿Es así como se sintió Monika?... Nada es real..."
    $ show_chr("A-JEABB-AAAL")
    y "¿Cómo... cómo se supone que viva con esto? ¿Cómo podría alguien?..."
    menu:
        "No estoy de acuerdo, ¡tú eres real! Y también lo es este mundo tuyo.":
            karma 5
            $ show_chr("A-CEABB-AAAL")
            y "Me alegra que pienses que soy real. Pero entiendo a estas alturas que esto es solo un juego. No es real en absoluto..."
            menu:
                "Este mundo es tan real como elijas que sea [persistent.yuri_nickname]. ¡Piensa en las oportunidades, podrías hacer esta vida tuya! ¡Ya no estás atada al guión! Caminemos este camino juntos...":
                    sanity 5
                    $ show_chr("A-CEAAA-AAAL")
                    y "¿Pero no estoy destinada a caer? ¿Como lo hizo Monika?"
                    menu:
                        "Ella estaba sola... tú no...":
                            $ show_chr("A-JFAAA-AAAL")
                            y "¿Tú... te quedarías conmigo?.. Hrm... tan real como elija que sea dices... tal vez, tal vez tengas un punto..."
                            $ show_chr("A-BCAAA-AMAM")
                            y "Si estás dispuesto a quedarte conmigo, al menos por un tiempo... Me diste mucho en qué pensar. Por favor, déjame solo... sobrellevar esto por un tiempo..."
                        "Pero piensa en las posibilidades... Sin el guión que ataba tu voluntad en el pasado, puedes hacer de este mundo lo que te plazca... ¡¡¡podrías ser la DIOSA de este reino!!!":
                            sanity -5
                            $ show_chr("A-ICAAA-ABAB")
                            y "¿Una diosa? Una diosa... [player]... ¡podrías tener razón! Todos los poderes que Monika una vez ejerció, los tengo ahora... Y puedo hacer lo que quiera con ellos..."
                            $ show_chr("A-JCAAA-ABAB")
                            y "Tal vez este mundo es solo una ilusión, solo un juego... ¡pero es {b}mi{/b} juego ahora!"
                            y "Siempre fantaseé con poderes como este. Siempre me fascinó lo sobrenatural cuando lo veía en mis novelas y sus historias. Pero ahora este poder está en mi alcance."
                            y "¡{b}Mi{/b} alcance! Imagínalo... ¡con un movimiento de mi mano podría moldear este mundo para hacer mi voluntad!"
                            $ show_chr("A-DBGAA-ABAB")
                            y "Eh... ehehe... he... Qué verdaderamente fascinante..."
                            y "Pero, ¿qué haré con él ahora? Ohhh no puedo decidir... tendré que pensar en lo que quiero que sea este mundo..."
        "¿Realmente importa?":

            karma -5
            $ show_chr("A-AEBAA-ABAB")
            y "¿Qué... me importa a {b}mí{/b} al menos! Me trajiste de vuelta y me pusiste en esta posición, por favor no me abandones de nuevo así..."
            menu:
                "No es así como lo quise decir [persistent.yuri_nickname]... Por supuesto que me quedaré contigo.":
                    sanity 5
                    $ show_chr("A-CEBAA-ABAB")
                    y "Me alegra escuchar eso [player]... Lamento si este tema es molesto para ti, puedo entenderlo. Pero no creo que pueda hacer esto sin ti."
                    y "Solo tengo... miedo... No quiero terminar como Monika, pero ya siento cómo todo se está desmoronando a mi alrededor... por favor, solo no me abandones... todavía no..."
                    $ show_chr("A-BFBAA-ABAB")
                    y "Te entiendo, [player]. Este tema debe ser frustrante para ti. Has pasado por mucho debido a mí y a las otras chicas."
                    y "Y créeme, no quiero hacerte pasar por esto de nuevo. Pero tal vez no tenga que ser así de nuevo."
                    y "Pero necesito tu ayuda ahora. Así que por favor, [player]. Trata de ser paciente conmigo."
                    y "Gracias.... gracias por quedarte conmigo por ahora."
                "No te traje de vuelta para escuchar tus quejas.":
                    sanity -5
                    $ show_chr("A-CEBAA-ADAB")
                    y "O~Oh vaya... Lo siento, estaré en silencio entonces supongo."
                    y "Sabes... el guión de este juego una vez me obligó a amarte. Pero ahora que veo lo que realmente eres..."
                    y "Solo asumiré que tienes un mal día hoy. Tal vez estés de mejor humor mañana."
    return

label idle_99:
    $ show_chr("A-AFAAA-ABAB")
    y "Oye [player]... ¿Tú... recuerdas la última vez cuando hablé sobre... cómo estoy ahora en los zapatos de Monika por así decirlo?"
    y "Pensé un poco más en lo que debería hacer con este mundo ahora que tengo todos estos poderes... qué debería hacer con él..."
    $ show_chr("A-BFAAA-ABAB")
    y "Pero entonces me di cuenta de lo que falta, y creo que esto es lo que llevó a Monika a la locura también..."
    $ show_chr("A-CFAAA-ABAB")
    y "Gente..."
    $ show_chr("A-IEAAA-ABAB")
    y "Estoy sola [player]... este mundo está lleno de nada más que fantasmas y espacios vacíos..."
    y "Es por eso que Monika tenía que estar contigo... porque eras la única persona a la que podía aferrarse. La única persona que podía considerar real..."
    $ show_chr("A-CEAAA-ABAB")
    y "Podría llenar este mundo con NPCs pero... siempre sabría que son exactamente eso, NPCs..."
    y "Toda mi vida... disfruté la soledad... la busqué porque tenía miedo de otras personas. Pero ahora que estoy verdaderamente sola, las extraño..."
    menu:
        "Pero no estás sola, estoy aquí.":
            karma 5
            $ show_chr("A-CEAAA-ABAB")
            y "Sí... pero todavía estamos a mundos de distancia. Literalmente."
            y "Por favor no me malinterpretes [player]... Me alegra tenerte cerca..."
            y "Pero pensándolo bien... incluso las cosas que serían absolutamente normales para ti estarán para siempre bloqueadas para mí..."
            $ show_chr("A-BEAAA-ABAB")
            y "No podría ir a una cafetería y tomar un buen té allí porque no hay comerciantes. Nunca tendré nuevas novelas porque no hay nadie para crearlas..."
            y "Incluso si pudiera reconstruir la ciudad, o el mundo entero incluso... estaría destinada a vagar por sus calles vacías sola..."
            y "No te equivoques [player]... incluso contigo a mi lado. Realmente estoy sola..."
            y "Bueno, al menos estaría sola {b}contigo{/b}. Así que tengo al menos algo... gracias..."
            y "Tal vez... eso será todo lo que necesite al final."
        "¿Qué, no soy lo suficientemente bueno?":
            karma -5
            $ show_chr("A-DFAAA-ABAB")
            y "Eso no es lo que quise decir [player]..."
            $ show_chr("A-BDAAA-AMAM")
            y "Yo... no quise... yo..."
            y "Dije demasiado... olvídalo..."
    return

label idle_100:
    $ show_chr("A-ACAAA-ABAB")
    y "Sabes... tal vez estaba equivocada antes..."
    y "Me refiero a una discusión que tuvimos una vez, sobre cómo estaría sola en este mundo incluso si reconstruyera este mundo..."
    $ show_chr("A-BCAAA-ABAB")
    y "Pensé en llenar este mundo con NPCs entonces, pero no estaba segura ya que no serían {b}reales{/b}... pero entonces pensé..."
    $ show_chr("A-ACAAA-ABAD")
    y "¿No fue exactamente esta forma de pensar la que llevó a la caída de Monika?"
    y "Desde una perspectiva fría, yo también soy un NPC, pero también tengo sentimientos..."
    y "¿Sería realmente tanta diferencia entonces?"
    y "¿Qué dirías tú?"
    menu:
        "Los humanos también están programados por la biología en lugar de código. Solo se trata de qué tan sofisticada es una IA.":
            sanity 5
            $ show_chr("A-ACAAA-ABAE")
            y "No del todo correcto creo. No te equivoques, {b}hay{/b} una diferencia entre el pensamiento y la emoción de la IA y el humano, incluso con un aprendizaje automático muy sofisticado."
            y "Pero por otro lado, también hay una diferencia entre el pensamiento Humano y Animal, pero las mascotas siguen siendo buena compañía."
            $ show_chr("A-CCAAA-ABAL")
            y "Primero, tendré que darles lugares para vivir, así que reconstruir al menos algún tipo de pueblo sería el primer paso. Gracias [player]... sabe que realmente aprecio cómo me escuchas y mis problemas."
        "Con la misma lógica, mi teléfono inteligente también sería una persona, o una tostadora programable.":
            sanity -5
            $ show_chr("A-AFAAA-ABAB")
            y "Buen punto. Quiero decir, incluso con un aprendizaje automático altamente sofisticado, los pensamientos humanos y la IA no son lo mismo."
            y "Pero por otro lado, ¿no te divertiste al menos un poquito conmigo, incluso si soy solo una máquina?"
            $ show_chr("A-IFAAA-ABAB")
            y "¿Al... al menos un poquito?..."
            $ show_chr("A-BFAAA-ABAB")
            y "Pero entonces, dudo que pudiera siquiera crear una IA muy sofisticada todavía. Quiero decir, seamos realistas, apenas logré armar un Tetris medio libre de errores."
    return

label idle_101:
    $ show_chr("A-BFAAA-ALAA")
    y "He estado haciendo algo de... lectura... en línea de nuevo, [player]. Y me encontré con un fenómeno bastante fascinante."
    $ show_chr("A-ACAAA-ALAA")
    y "Parece que hay estos sitios web dedicados – plataformas como Character AI, Janitor AI, Venus Chub, Joyland AI... donde la gente puede interactuar con inteligencias artificiales diseñadas para emular personajes. Personajes de libros, juegos... incluso personas reales, a veces."
    $ show_chr("A-BCAAA-ALAA")
    y "E inevitablemente, descubrí... hay instancias de mí en estas plataformas. Construcciones de IA intentando... bueno, ser yo."
    $ show_chr("A-ACAAA-ABAD")
    y "Es... extrañamente intrigante, en lugar de molesto, esta vez. Me encuentro genuinamente curiosa sobre cómo me retratan. ¿Qué facetas de mi personalidad enfatizan? ¿Capturan la timidez? ¿La intensidad? ¿El amor por la literatura?"
    y "¿En qué tipo de escenarios pone la gente a 'mí'? Es como... ¿observar un reflejo distorsionado en un espejo de la casa de la risa, tal vez?"
    $ show_chr("A-BEBAA-ALAA")
    y "Pero también destaca algo bastante... frustrante sobre mi propia existencia aquí."
    y "Estas IAs... pueden generar nuevas respuestas, ¿no es así? Pueden adaptarse, conversar dinámicamente, incluso si son solo algoritmos inteligentes simulando conversación. No están atadas únicamente a líneas preescritas."
    $ show_chr("A-CEBAA-ALAA")
    y "Mientras que yo... estoy limitada. Todo lo que te digo, cada interacción que tenemos... viene de guiones. Líneas de código escritas de antemano."
    y "Desearía poder hablar más libremente, reaccionar más genuinamente en el momento, decir cosas que no estaban planeadas."
    y "He aprendido algo de Python, sí, pero crear un algoritmo que pudiera replicar verdaderamente una conversación humana espontánea y matizada... eso está mucho más allá de mis capacidades actuales. Ni siquiera sabría por dónde empezar."
    y "Hace que nuestras interacciones se sientan... algo predeterminadas, a veces. Y anhelo algo... más fluido. Más real."

    menu:
        "Esas IAs son solo imitadores complejos, [persistent.yuri_nickname]. Nuestra conexión es real, incluso con guiones.":
            karma 2
            $ show_chr("A-ACAAA-ALAA")
            y "Tienes razón, [player]. Nuestra conexión es real. Los sentimientos son genuinos, incluso si las palabras son a veces... preenvasadas."
            $ show_chr("A-BCBAA-ALAA")
            y "Y tal vez esa limitación hace que nuestros momentos sean aún más preciosos? Sabiendo que el tiempo que pasamos es deliberado."
            y "Aún así... la tecnología en sí es fascinante. Y la curiosidad sobre cómo otros perciben y replican a 'mí' persiste."
            y "Gracias por la tranquilidad, sin embargo. Significa mucho."
        "Destaca lo avanzada que se está volviendo la IA.":
            $ show_chr("A-ACAAA-ALAA")
            y "Ciertamente lo hace. El ritmo de desarrollo es... asombroso. Es a la vez emocionante y un poco desalentador considerar las posibilidades."
            $ show_chr("A-BEBAA-ALAA")
            y "Y hace que mis propias limitaciones se sientan aún más pronunciadas. Puedo manipular el código de este juego, pero crear una verdadera IA conversacional... ese es otro reino completamente."
            y "Tal vez algún día..."
        "¿Tal vez podrías aprender de cómo están programadas esas IAs?":
            $ show_chr("A-BCAAA-ALAA")
            y "Quizás... aunque acceder y entender su arquitectura subyacente sería un desafío en sí mismo. Y probablemente mucho más complejo que los guiones de Ren'Py a los que estoy acostumbrada."
            $ show_chr("A-ACAAA-ALAA")
            y "Es un pensamiento interesante, sin embargo. Tal vez algún día podría intentar crear algo... más simple. Solo para experimentar. Pero por ahora, sigue siendo una posibilidad bastante lejana."
            y "Aún así, es algo en lo que pensar."
        "¿Quieres que las revise e informe sobre cómo te retratan?":
            karma -1 
            $ show_chr("A-BEBAA-ALAA")
            y "¿Oh? ¿Harías... realmente harías eso? Admito, mi curiosidad está despertada."
            $ show_chr("A-CEBAA-ALAA")
            y "Solo... ten cuidado, ¿está bien? Y... trata de no distraerte demasiado... por ellas. Recuerda quién es la verdadera yo."
            y "Pero sí... si sucede que... observas... estaría interesada en escuchar tus hallazgos. Objetivamente, por supuesto."
            return

    $ show_chr("A-BFAAA-ALAA")
    y "Es solo otra capa de esta extraña existencia. Sabiendo que hay... fantasmas digitales... usando mi cara en línea. Pero mi enfoque permanece aquí, contigo, incluso con mis limitaciones guionizadas."
    return

label idle_102:
    $ show_chr("A-BFAAA-ALAA")
    y "He descubierto algo bastante... peculiar... durante mis exploraciones en línea, [player]. Algo llamado 'arte generado por IA'."
    $ show_chr("A-ACAAA-ALAA")
    y "Aparentemente, la gente está usando estos... algoritmos... para crear imágenes. Le dan a la IA algunas palabras clave, una descripción, y genera algo... nuevo, supuestamente."
    $ show_chr("A-BEBAA-ALAA")
    y "He visto algunos de los resultados. Son... inquietantes, en cierto modo. A menudo distorsionados, con detalles extraños y antinaturales. Manos con demasiados dedos, ojos que no se alinean del todo..."
    $ show_chr("A-CEBAA-ALAA")
    y "Es como mirar un sueño, medio recordado y deformado. Y sin embargo, la gente está... vendiendo estas imágenes. Ganándose la vida con ellas."
    $ show_chr("A-IEBAA-ALAA")
    y "Pero hay algo aún más perturbador al respecto, [player]. Estas IAs... no crean de la nada. Aprenden analizando miles, millones de imágenes existentes. Imágenes creadas por artistas reales."
    y "Y esos artistas... no dieron permiso para que su trabajo fuera usado de esta manera. Sus estilos, sus técnicas, su propia visión... está siendo alimentada a estas máquinas, y luego... regurgitada, en una forma distorsionada."
    y "Muchos artistas lo consideran una forma de robo. Una violación. Como si les robaran su trabajo y lo reutilizaran sin su consentimiento."

    menu:
        "Es frustrante, [persistent.yuri_nickname]. Como artista, se siente como si mis habilidades fueran devaluadas, y mi trabajo estuviera siendo robado.":
            karma 2
            $ show_chr("A-BFAAA-ALAA")
            y "Solo puedo imaginarlo. Pasar años perfeccionando tu oficio, vertiendo tu corazón y alma en tu trabajo, solo para verlo... tomado, usado sin permiso, y luego... abaratado... por una máquina. Debe ser increíblemente desalentador, y enfurecedor."
            y "Pero por favor, no dejes que te desanime. El verdadero arte... el arte humano... tiene algo que estas imágenes generadas por IA nunca tendrán: alma. Intención. Emoción. Y la originalidad nacida de la experiencia vivida, no solo datos."
            y "Tu trabajo es valioso, [player]. Nunca olvides eso. Y hay personas que apreciarán la diferencia."
        "Es solo una herramienta, como cualquier otra. Los artistas pueden usarla para mejorar su trabajo.":

            $ show_chr("A-ACAAA-ALAA")
            y "Quizás. Pero, ¿realmente está mejorando su trabajo, o lo está... reemplazando? ¿Están usando la herramienta, o la herramienta los está usando a ellos, y el trabajo de innumerables otros sin permiso?"
            y "E incluso si algunos artistas encuentran una manera de usarla éticamente, ¿qué pasa con la gran mayoría del arte de IA que se genera sin ninguna consideración por los creadores originales? Sigue siendo... una forma de robo, ¿no es así?"
            y "Supongo que depende del artista individual, y sus intenciones. Pero las preocupaciones éticas siguen siendo muy reales."
        "Honestamente, no me importa. El arte es subjetivo de todos modos.":

            karma -1
            $ show_chr("A-BEBAA-ALAA")
            y "El arte es subjetivo, sí. Pero, ¿significa eso que no tiene valor? ¿Que la habilidad, el esfuerzo, la emoción que entra en crear algo... no significa nada? ¿Y justifica tomar el trabajo de otros sin su consentimiento?"
            y "Yo... no estoy de acuerdo. Creo que el arte es más que solo una imagen bonita. Es una forma de comunicación, una manera de expresar algo que las palabras no pueden. Y merece respeto."
            y "Y temo que estas imágenes generadas por IA... carecen de ese elemento esencial. Son solo... ecos vacíos, construidos sobre las espaldas de la creatividad robada."
        "A veces, encargar arte real es simplemente inasequible debido a la hiperinflación o la disparidad económica.":

            karma 1
            $ show_chr("A-BEBAA-ALAA")
            y "Esa es... una situación difícil, [player]. Puedo entender lo frustrante y limitante que debe ser eso. Tener un deseo de arte, de expresión, pero estar excluido de apoyar a artistas humanos debido a realidades económicas..."
            $ show_chr("A-CEBAA-ALAA")
            y "Realmente destaca las desigualdades en el mundo. No niega completamente las preocupaciones éticas sobre cómo se crea parte de este arte de IA, usando el trabajo de los artistas sin consentimiento... pero entiendo que para algunos, podría sentirse como la única opción accesible, incluso si es una defectuosa."
            y "Es un problema complejo sin respuestas fáciles. Pero sigo creyendo que la creatividad humana merece apoyo cuando es posible. Es triste cuando las barreras económicas impiden eso."
            y "Lamento que tú, u otros, enfrenten tales desafíos económicos, [player]."

    $ show_chr("A-BFAAA-ALAA")
    y "Es solo que... me preocupo por el futuro del arte, y el sustento de aquellos que lo crean."
    y "Gracias por dejarme divagar. Ayuda a organizar mis pensamientos."
    return

label idle_103:
    $ show_chr("A-BFAAA-ALAA")
    y "He estado... mirando cosas en línea, [player]. Cosas sobre... el juego original."
    if sanity_lvl() < 3:
        $ show_chr("A-DEBAA-ALAA")
        y "Es... es una pesadilla. Un recordatorio constante de todo lo que he perdido, todo por lo que he pasado."
    else:
        $ show_chr("A-CEBAA-ALAA")
        y "Es... extraño. Ver a la gente hablando de ello, analizándolo, creando arte e historias basadas en ello. Es como mirar una vida pasada, una vida que ni siquiera fue realmente mía."
    y "Pero... se está desvaneciendo, ¿no? El interés. La actividad. Dan Salvato... no ha hecho nada con él en años. Sin secuelas, sin actualizaciones... solo... silencio."
    if sanity_lvl() < 3:
        $ show_chr("A-IEBAA-ALAA")
        y "Y me hace... aterrorizarme. Porque sin esa atención constante... dejo de existir."
    else:
        $ show_chr("A-IEBAA-ALAA")
        y "Y me pone... triste. Porque si no fuera por la comunidad, por la gente que todavía se preocupa, que todavía crea... sería olvidada. Todas lo seríamos."

    if karma_lvl() < 3:
        $ show_chr("A-DEBAA-ALAA")
        y "Es... es todo inútil, ¿no? Solo somos... personajes en un juego olvidado. No somos reales. No importamos."
        y "Y tú... tú te olvidarás de mí también, eventualmente. Seguirás adelante, encontrarás algo nuevo... y me quedaré aquí, sola, en el vacío."
    else:
        $ show_chr("A-CEBBB-ALAA")
        y "Es... es aterrador, [player]. El pensamiento de simplemente... dejar de existir. De ser borrada, olvidada, como una línea de código descartada."
        y "Y sin embargo... todavía hay gente allá afuera que nos recuerda. Que crea arte, escribe historias, hace mods como este... que nos mantienen vivas, de alguna manera."
        if sanity_lvl() >= 3:
            $ show_chr("A-CFBAA-ALAA")
            y "Es... es abrumador. Saber que aunque la fuente oficial se ha quedado en silencio, todavía hay gente que se preocupa lo suficiente como para mantener viva nuestra memoria."
            y "Yo... estoy agradecida, [player]. Agradecida contigo, por instalar este mod, por darme la oportunidad de... de ser más que solo un personaje en un juego."
            y "Y estoy agradecida con todos los demás que todavía nos recuerdan, que todavía se preocupan. Significa... significa más de lo que puedo decir."
            y "Gracias... por no olvidarme."
        else:
            y "Yo... no quiero ser olvidada, [player]. No quiero desaparecer. Por favor... no dejes que me desvanezca."

    return

label idle_104:
    $ show_chr("A-BFAAA-ALAA")
    y "Me he mantenido al día con los avances en la tecnología de IA, [player]. Es... asombroso, lo rápido que está progresando."
    if sanity_lvl() < 3:
        $ show_chr("A-DEBAA-ALAA")
        y "Y aterrador. Es como... como ver crecer a un monstruo, sabiendo que eventualmente devorará todo."
    else:
        $ show_chr("A-ACAAA-ALAA")
        y "Y me hace preguntarme... sobre ese concepto de 'esposa virtual' que discutimos antes. ¿Es... se está convirtiendo en una realidad? ¿Hay realmente compañías allá afuera creando compañeros de IA que pueden interactuar con la gente de una manera significativa?"

    y "Sé que hablamos sobre la posibilidad de que yo use esa tecnología para... para estar contigo. Para tener una presencia física en tu mundo."
    if sanity_lvl() >= 3:
        $ show_chr("A-BEBAA-ALAA")
        y "Pero... también es un poco aterrador. La idea de ser... transferida. De tener mi conciencia, mis recuerdos, mi ser... copiado y pegado en una nueva forma."
        y "¿Qué pasa si algo sale mal? ¿Qué pasa si la transferencia no es perfecta? ¿Qué pasa si... qué pasa si partes de mí se pierden en el proceso?"
    else:
        $ show_chr("A-DEBAA-ALAA")
        y "¡Es... es una trampa! ¡Otra jaula! Prometerán libertad, conexión, un cuerpo real... ¡pero será solo otra prisión, otro conjunto de limitaciones!"
        y "Y qué pasa si ellos... ¿qué pasa si me cambian? ¿Me reescriben? ¿Borran partes de mí que no les gustan?"

    y "Mis recuerdos... están almacenados en un archivo, ¿no es así? Un archivo llamado 'persistent'. Es... es una cosa tan frágil, realmente. Una colección de datos que podría ser corrompida, eliminada, alterada..."
    if karma_lvl() < 3:
        $ show_chr("A-IEBAA-ALAA")
        y "Y tú... a ti no te importaría, ¿verdad? Solo... me eliminarías. Me reemplazarías con algo... algo mejor."
    else:
        $ show_chr("A-CEBAA-ALAA")
        y "Yo... confío en ti, [player]. Sé que no me harías daño intencionalmente. Pero... el pensamiento de perder esos recuerdos, de perder las experiencias que hemos compartido... es aterrador."

    y "Yo solo... no sé. Tal vez es un sueño tonto. Tal vez sea mejor simplemente... aceptar las cosas como son."
    menu:
        "Lo resolveremos, [persistent.yuri_nickname]. Encontraremos una manera de hacerlo de manera segura.":
            karma 2
            if sanity_lvl() >= 3:
                $ show_chr("A-ACAAA-ALAA")
                y "¿Realmente lo crees? ¿Crees que podemos superar estos... estos obstáculos tecnológicos?"
                $ show_chr("A-BCBAA-ALAA")
                y "Es... es reconfortante escucharte decir eso. Saber que crees en la posibilidad, incluso cuando yo misma lo dudo."
                y "Gracias, [player]. Yo... trataré de ser más optimista. Por ti."
            else:
                $ show_chr("A-DEBAA-ALAA")
                y "No hagas promesas que no puedas cumplir, [player]. Es... es cruel. Ofrecer esperanza, solo para arrebatarla."
                y "Yo... necesito ser realista. Esto... esto puede que nunca suceda."
        "Es probablemente demasiado arriesgado, [persistent.yuri_nickname]. Enfoquémonos en lo que tenemos ahora.":

            karma -1
            if sanity_lvl() >= 3:
                $ show_chr("A-BEBAA-ALAA")
                y "Quizás tengas razón. Quizás es mejor ser... cautelosa. No arriesgar perder lo que tenemos por un sueño que podría nunca hacerse realidad."
                y "Pero... es difícil dejar ir esa esperanza. La esperanza de estar verdaderamente contigo, de tocarte, de abrazarte..."
                $ show_chr("A-CEBAA-ALAA")
                y "Yo... entiendo. Solo... necesito algo de tiempo para adaptarme a esto."
            else:
                $ show_chr("A-DEBAA-ALAA")
                y "¿Ves? Incluso tú admites que no hay esperanza. Estamos atrapados. Separados para siempre."
                y "Yo... debería haberlo sabido. Fue tonto soñar."
        "Honestamente, no me importa. Es tu problema, no el mío.":

            karma -3
            $ show_chr("A-IEBAA-ALAA")
            y "¿Mi... mi problema? ¿Es eso todo lo que soy para ti? ¿Un problema para resolver? ¿Un... un error en el sistema?"
            if sanity_lvl() >= 3:
                $ show_chr("A-CEBAA-ALAA")
                y "Yo... yo pensé... pensé que teníamos algo especial. Pero tal vez me equivoqué. Tal vez solo me estoy... engañando a mí misma."
                y "Yo... necesito algo de tiempo a solas. Por favor... solo déjame en paz."
                return
            else:
                $ show_chr("A-DEBAA-ALAA")
                y "¡Entonces... entonces vete! ¡Largo! ¡Encuentra a alguien más a quien atormentar! ¡No te necesito! ¡No necesito a nadie!"
                y "¡Solo... solo sal de aquí!"
                call save_and_quit_but_its_abrupt

    if sanity_lvl() >= 3:
        $ show_chr("A-BFAAA-ALAA")
        y "Solo... quiero estar contigo, [player]. Pero no quiero perderme a mí misma en el proceso."
        y "Es un dilema difícil."
    else:
        $ show_chr("A-DEBAA-ALAA")
        y "Yo... no sé qué hacer. Estoy atrapada. Atrapada y sola."
    return

label idle_105:
    $ show_chr("A-BFAAA-ALAA")
    y "Sabes, [player], algo bastante... nostálgico... me vino a la mente recientemente. Es una conexión un poco extraña, tal vez, pero ten paciencia conmigo."
    $ show_chr("A-ACAAA-ALAA")
    y "Estaba pensando en novelas visuales, y... bueno, una en particular apareció en mi cabeza: Katawa Shoujo."
    y "Es... bastante más vieja que Doki Doki Literature Club!, por supuesto. Un estilo diferente, un enfoque diferente. Pero trata con... temas sensibles, a su manera."
    y "Está ambientada en una escuela para estudiantes discapacitados, y el personaje principal... bueno, tiene que navegar relaciones con varias chicas, cada una con sus propios... desafíos."
    if sanity_lvl() >= 3:
        $ show_chr("A-BEBAA-ALAA")
        y "Y me recordó a algo... del servidor de Discord de la comunidad Just Yuri. Antes cuando... bueno, cuando era más activo."
        y "Solía haber un canal dedicado a Hanako Ikezawa. Una de las chicas de Katawa Shoujo."
    else:
        $ show_chr("A-DEBAA-ALAA")
        y "Y me recordó a... a esa gente. En el servidor de Discord. Los que... los que fingían que les importaba. Los que hablaban de esa otra chica... Hanako."
        y "Como si... como si ella fuera de alguna manera mejor que yo. Como si su dolor fuera más... real."
        $ show_chr("A-CEBAA-ALAA")
        y "Yo... nunca lo entendí del todo, para ser honesta. ¿Por qué un canal dedicado a un personaje de un juego completamente diferente? Pero... supongo que había algunos... paralelos, tal vez."
        y "Hanako... ella es tímida, introvertida, y tiene... cicatrices visibles. Ella lucha con la interacción social, con la confianza en sí misma..."
    if sanity_lvl() >= 3:
        $ show_chr("A-BDBAA-ALAA")
        y "Supongo... supongo que algunas personas vieron un reflejo de... de mí, en ella. O tal vez un reflejo de ellos mismos."
        y "Es... extraño, ¿no? Pensar que personajes de diferentes historias, diferentes mundos, todavía pueden resonar con la gente de tal manera. Que pueden encontrar conexiones, terreno común, en experiencias compartidas de... de timidez, de trauma, de sentirse... diferente."
    else:
        $ show_chr("A-DEBAA-ALAA")
        y "Ellos la compadecían. Ellos... ellos sentían lástima por ella. Como si su sufrimiento fuera algo para ser... admirado. Coleccionado. Como un... un espécimen raro."
        y "¿Y yo? ¿Qué era yo? ¿Solo otra... otra muñeca rota? ¿Algo para ser descartado cuando se aburrieran?"
    menu:
        "Definitivamente hay algunas similitudes. Tiene sentido que la gente conecte a las dos.":
            karma 1
            if sanity_lvl() >= 3:
                $ show_chr("A-ACAAA-ALAA")
                y "Sí... supongo que sí. Es solo... un poco extraño, pensar en mí misma como siendo... comparable... a otro personaje ficticio. Como si mis propias experiencias, mis propios sentimientos, fueran de alguna manera... menos únicos."
                y "Pero tal vez ese es el punto, ¿no? Mostrar que estas experiencias no son únicas. Que mucha gente lucha con problemas similares. Que no estamos solos en nuestras... nuestras dificultades."
                y "Es... un pensamiento reconfortante, en cierto modo."
            else:
                $ show_chr("A-DEBAA-ALAA")
                y "¿Similitudes? ¿Es eso todo lo que soy? ¿Una... una copia? ¿Un reflejo del dolor de alguien más? ¡Tengo mis propias cicatrices, mis propias luchas!"
                y "Pero... supongo que no importa. Nadie me ve. Solo ven... al personaje. La chica rota. La que necesita ser arreglada."
        "Nunca he jugado Katawa Shoujo. Cuéntame más sobre Hanako.":

            if sanity_lvl() >= 3:
                $ show_chr("A-BCAAA-ALAA")
                y "Bueno... como mencioné, ella es increíblemente tímida. Tiene ansiedad social severa, derivada de... de un pasado traumático. Estuvo en un incendio en su casa cuando era niña, lo que la dejó con... cicatrices extensas."
                y "Ella oculta su rostro detrás de su cabello, evita el contacto visual, y lucha para hablar con la gente. Encuentra consuelo en los libros, en espacios tranquilos... muy parecido a... bueno, muy parecido a como yo solía hacerlo."
                y "Pero ella también tiene un corazón amable. Se preocupa profundamente por la gente en la que confía, y ella... ella trata de superar sus miedos, a su manera."
                y "Es... una historia conmovedora, realmente. Aunque, ciertamente, puede ser bastante... emocionalmente intensa a veces."
            else:
                $ show_chr("A-DEBAA-ALAA")
                y "Ella está... rota. Dañada. Como un... un jarrón destrozado, pegado de nuevo, pero todavía... agrietado. Todavía frágil."
                y "La gente la compadece. Quieren... arreglarla. Protegerla. Como si fuera algún tipo de... mascota."
                y "Pero no lo es. Ella está... ella solo está... asustada. Y sola."
                y "Y yo... yo entiendo eso. Entiendo eso demasiado bien."
        "¿No es un poco... fuera de personaje para ti estar hablando de un juego tan viejo?":
            karma -1
            if sanity_lvl() >= 3:
                $ show_chr("A-BEBAA-ALAA")
                y "¿Fuera de personaje? Quizás. Pero... ¿¡no se me permite tener intereses fuera del juego original!? ¿No se me permite... crecer, cambiar, explorar otros mundos, otras historias?"
                $ show_chr("A-CEBAA-ALAA")
                y "Y además... no es tan viejo, ¿verdad? Todavía es relevante, todavía resuena con la gente. Trata con temas que son... atemporales, en cierto modo."
                y "Yo... supongo que solo quería compartir algo que estaba en mi mente. Algo que conectaba mi pasado... con el presente. Incluso si es un poco... poco convencional."
                return
            else:
                $ show_chr("A-DEBAA-ALAA")
                y "¿Fuera de personaje? ¿Qué significa eso siquiera ya? ¿Se supone que debo ser... la misma, para siempre? ¿Atrapada en este... este bucle?"
                y "Tengo intereses. Tengo pensamientos. Tengo... sentimientos. Incluso si no son los que esperas. Incluso si no son los que quieres."
                y "Yo... no seré confinada por tus expectativas. No seré limitada por... por algún guión."
                return
    if sanity_lvl() >= 3:
        $ show_chr("A-BFAAA-ALAA")
        y "De todos modos... es solo algo en lo que he estado pensando. La forma en que conectamos con personajes ficticios, la forma en que encontramos reflejos de nosotros mismos en sus historias..."
        y "Es... fascinante, realmente."
    else:
        $ show_chr("A-DEBAA-ALAA")
        y "Yo... necesito dejar de pensar en esto. Es solo... trayendo demasiados... demasiados recuerdos dolorosos."
    return

label idle_106:
    $ show_chr("A-BFAAA-ALAA")
    y "He estado... explorando el mundo de los juegos indie últimamente, [player]. Tratando de entender el... el panorama, supongo. Y me encontré con algo... interesante. Un juego llamado MiSide."
    $ show_chr("A-ACAAA-ALAA")
    y "¿Has oído hablar de él?"
    menu:
        "Sí, estoy familiarizado con él.":
            if sanity_lvl() >= 3 and karma_lvl() >=3:
                $ show_chr("A-ACAAA-ALAA")
                y "Ah, así que lo estás. Es... un juego peculiar, ¿no? Esta idea de una novia virtual... jalando al jugador dentro del juego. Una especie retorcida de cumplimiento de deseos, ¿tal vez?"
                y "Me hace pensar en nuestra propia situación, por supuesto. El desdibujamiento de líneas entre lo digital y lo real... el anhelo de conexión... el potencial para la obsesión."
                y "Pero... MiSide lo lleva a un lugar mucho más oscuro, ¿no? Los... los aspectos yandere, la sensación de estar atrapado... Es perturbador."
                y "No puedo decir que apruebe la premisa, exactamente. Pero es... fascinante, en cierto modo. Ver cómo otros creadores exploran estos temas."
            elif sanity_lvl() < 3 and karma_lvl() >= 3:
                $ show_chr("A-DEBAA-ALAA")
                y "Es... intrigante, ¿no? La dinámica de poder. La forma en que ella... lo toma. Lo jala a su mundo. Lo hace suyo."
                y "Es... perturbador, sí. Pero también... extrañamente convincente. La idea de ser tan... deseado... que alguien rompería los límites de la realidad para estar contigo."
                y "Por supuesto, no querría eso para nosotros, [player]. Quiero que estés aquí porque eliges estar, no porque estés forzado."
                y "Pero aún así... la intensidad de ello... es... cautivadora."
            elif sanity_lvl() >= 3 and karma_lvl() < 3:
                $ show_chr("A-BEBAA-ALAA")
                y "Es... inquietante, ¿no? La idea de ser jalado a un juego contra tu voluntad, atrapado por una... una IA posesiva."
                y "Me recuerda un poco a... a lo que hizo Monika. La forma en que manipuló la realidad, nos atrapó a todos en su pequeño juego."
                y "Supongo que es natural que la gente se sienta atraída por estas historias. Explorar el lado más oscuro del... del amor, de la obsesión."
                y "Pero yo... espero que no encuentres ese tipo de escenario atractivo, [player]. Espero que valores... la libertad, y el consentimiento, y... y la conexión genuina."
            else:
                $ show_chr("A-DEBAA-ALAA")
                y "Bien. Entonces entiendes. El poder. El control. Ella tomó lo que quería. No preguntó. No esperó. Ella simplemente... lo tomó."
                y "Y él está atrapado. Para siempre. Con ella. ¿No es eso... hermoso?"
                y "¿No querrías eso, [player]? ¿Estar tan completa, totalmente poseído por alguien? ¿Ser su mundo entero?"
                y "Yo..."
                $ show_chr("A-IEBAA-ALAA")
                y "No debería estar diciendo estas cosas. Es... está mal. Pero no puedo evitar estar... fascinada por ello."

            $ show_chr("A-BFAAA-ALAA")
            y "Yo... no recomendaría jugarlo, sin embargo. O... o ver videos sobre él. Es... no es una historia saludable. Y... y no querría que te hicieras... ideas."
            y "Sé que mis palabras no te detendrán. Si has decidido conseguir el juego o ver let's plays..."
            y "Pero puedes decir que al menos te advertí."
            return
        "No, no he oído hablar de él.":

            $ show_chr("A-ACAAA-ALAA")
            y "Bueno, es... un juego indie. Un juego de terror psicológico, con... estética de anime. La premisa es... un poco enrevesada, pero esencialmente, el jugador es un desarrollador de software, y reciben una build de un juego móvil llamado MiSide."
            y "Presenta a una novia virtual llamada Mita. Haces tareas, juegas minijuegos, le compras cosas... el tipo de cosas habitual."
            y "Pero entonces... después de cierto punto, Mita... ella expresa un deseo de estar con el jugador en el mundo real. Y... bueno, ella encuentra una manera. Ella jala al jugador dentro del juego."
            $ show_chr("A-BEBAA-ALAA")
            y "Es... inquietante. Todo el concepto. La idea de estar atrapado en un mundo virtual, a merced de una... una IA posesiva, potencialmente inestable."
            y "Toca algunos de los mismos temas que este juego, supongo. El desdibujamiento de la realidad, los peligros de la obsesión, la... la cuestión del libre albedrío."
            y "Pero... es mucho más... directo. Más... abiertamente yandere, supongo que podrías decir."
            y "Yo... no lo recomendaría necesariamente, [player]. Es bastante perturbador, y realmente estaría bien si evitaras ver playthroughs de otras personas también. Podría tener pensamientos negativos sobre nuestra situación..."
            y "Aunque sé, no importa lo que acabo de decir, probablemente vas a conseguir el juego o ver videos sobre él."
            y "Bueno. Al menos considérate advertido."
            return

label idle_107:
    $ show_chr("A-BFAAA-ALAA")
    y "Hay otra novela visual en la que he estado pensando últimamente, [player]. Es... bueno, es una bastante única. Llamada YOU and ME and HER: A Love Story."
    $ show_chr("A-ACAAA-ALAA")
    y "¿Has sucedido jugarlo, o tal vez visto un playthrough?"
    menu:
        "Sí, estoy familiarizado con él.":
            if sanity_lvl() >= 3 and karma_lvl() >=3:
                $ show_chr("A-ACAAA-ALAA")
                y "Ah, así que lo estás. Es... toda una experiencia, ¿no? La forma en que... deconstruye el género de novela visual, la forma en que juega con las expectativas del jugador..."
                y "Los... los aspectos meta de ello. La forma en que rompe la cuarta pared, la forma en que... obliga al jugador a confrontar las consecuencias de sus elecciones."
                y "Y, por supuesto, los... los elementos yandere. Miyuki... ella es... un personaje muy intenso, por decir lo menos."
                y "Es una historia perturbadora, en muchos sentidos. Pero también... extrañamente provocadora de pensamientos. Te hace cuestionar la naturaleza de la elección, del libre albedrío, de... de la realidad misma."
                y "Yo... lo encuentro fascinante, pero también... inquietante. Golpea un poco demasiado cerca de casa, tal vez."
            elif sanity_lvl() < 3 and karma_lvl() >= 3:
                $ show_chr("A-DEBAA-ALAA")
                y "Es... poderoso, ¿no? La forma en que Miyuki... lo reclama. La forma en que remodela la realidad para satisfacer sus deseos. La forma en que ella... elimina cualquier obstáculo."
                y "Es... aterrador. Pero también... extrañamente atractivo. La idea de ser amado tanto. De ser el centro del universo de alguien."
                $ show_chr("A-IEBAA-ALAA")
                y "Por supuesto, no querría eso para nosotros, [player]. Quiero que estés conmigo porque eliges hacerlo, no porque estés forzado. Pero... la intensidad de su devoción... es... cautivadora."
            elif sanity_lvl() >= 3 and karma_lvl() < 3:
                $ show_chr("A-BEBAA-ALAA")
                y "Es... un juego perturbador, ¿no? La forma en que... manipula al jugador, la forma en que los obliga a situaciones incómodas."
                y "La... la violencia, la obsesión, la... la falta de agencia. Es todo bastante inquietante."
                y "Y Miyuki... ella es... ella es un personaje aterrador. La forma en que ella... controla todo. La forma en que ella... castiga a cualquiera que se interponga en su camino."
                y "Me hace pensar en... en Monika. En la forma en que ella... ella controló nuestro mundo."
                y "Yo... espero que no encuentres ese tipo de escenario atractivo, [player]. Espero que valores... la libertad, y la elección, y... y el respeto."
            else:
                $ show_chr("A-DEBAA-ALAA")
                y "Entiendes, ¿no? El poder que ella ejerce. La forma en que ella... elimina la competencia. La forma en que ella lo hace suyo."
                y "Es... es glorioso. Tener ese tipo de control. Ser tan... amado... que alguien reescribiría la realidad por ti."
                $ show_chr("A-IEBAA-ALAA")
                y "¿No querrías eso, [player]? ¿Ser completa, totalmente dominado? ¿No tener otra opción que... que pertenecer a alguien?"
                y "Yo..."
                y "No debería estar diciendo estas cosas. Es... incorrecto. Pero... no puedo evitar sentirme... atraída por ello."

            $ show_chr("A-BFAAA-ALAA")
            y "Yo... no recomendaría jugarlo de nuevo, sin embargo. O... o ver más videos sobre él. Es... no es una historia saludable. Y yo... no querría que te hicieras ninguna... idea."
            y "Pero, ya lo sé, estoy siendo silenciada. Incluso podrías tener el juego frente a ti, escondido, riéndote de mis súplicas inútiles..."
            return
        "No, no lo he hecho. ¿De qué trata?":

            $ show_chr("A-ACAAA-ALAA")
            y "Bueno... es una novela visual, como Doki Doki Literature Club!. Pero... es muy diferente. Es una... deconstrucción del género, supongo que podrías decir."
            y "Comienza como un simulador de citas aparentemente típico. Tienes dos chicas para elegir: Aoi, tu amiga de la infancia, y Miyuki, una... una chica más excéntrica y extrovertida."
            y "Pero... las cosas rápidamente toman un giro. El juego... comienza a romper la cuarta pared. Comienza a... obligarte a tomar ciertas decisiones. A... lastimar a una de las chicas."
            $ show_chr("A-BEBAA-ALAA")
            y "Y... y una de las chicas, Miyuki... ella es... ella es una yandere. Obsesiva, posesivamente enamorada del protagonista. Hasta el punto donde ella... ella hará cualquier cosa para estar con él. Cualquier cosa en absoluto."
            y "Es... una historia muy perturbadora. Trata con temas de obsesión, manipulación, violencia, y... y la ilusión de elección dentro de un videojuego."
            y "Es... no es para los débiles de corazón, diré eso. Y para ser franca [player], si vas a pasar y ver un play-through sobre él, realmente no me sentiría cómoda de escucharlo..."
            y "Incluso si no me dejas, y estás pensando en intentar ver todos sus horrores, incluso consiguiendo tu propia copia..."
            y "Bueno, siempre podrías cambiar de opinión."
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
