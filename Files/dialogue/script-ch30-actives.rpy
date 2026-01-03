



label a1:
    python:
        import random
        howAreYouVariant = random.randint(1, 5)
        howAreYouVariant2 = random.randint(1, 2)

    if karma_lvl() == 3:
        if sanity_lvl() == 3:
            $ show_chr("A-BCAAA-AAAA")
            y "Oh... Me siento igual que antes. Espero que eso signifique para ti que me siento bien."
        else:
            $ show_chr("A-AFAAA-AAAA")
            y "Yo... realmente no sé cómo me siento en este momento."
            $ show_chr("A-ACBAA-AAAA")
            y "Se siente... ¿agradable, supongo?"
            $ show_chr("A-ABBAA-AAAA")
            y "Disculpa mi lenguaje ambiguo."
            y "Supongo que simplemente me estoy acostumbrando a este nuevo entorno."
        return

    elif sanity_lvl() >= 3:
        if karma_lvl() < 3:
            $ show_chr("A-BEBAA-AAAA")
            y "Oh... M-Me siento bien, pero dudo que realmente te importe en absoluto, ¿o sí?"

        elif karma_lvl() > 3:
            if howAreYouVariant == 1:
                $ show_chr("A-BCABA-AAAA")
                y "Oh... Me siento bien. Espero poder sentirme así todos los días, mi amor..."


            elif howAreYouVariant == 2:
                $ show_chr("A-ACAAA-AAAB")
                y "Un poco sedienta, en realidad..."
                if persistent.lovecheck:
                    y "¿Te gustaría tomar un poco de té conmigo?"
                    menu:
                        "¡Claro!":
                            python:
                                import random
                                if check_memory('a26-1') and check_memory('a26-2'):
                                    outcome = random.randint(1, 3)
                                else:
                                    outcome = random.randint(1, 2)
                            if outcome == 1:
                                jump teadate1
                            if outcome == 2:
                                jump teadate2
                            if outcome == 3:
                                jump teadate3
                            return
                        "Me gustaría, pero no tengo aquí. Pero, por favor, sírvete tú misma.":
                            $ show_chr("A-GBAAA-AAAD")
                            y "Más tarde, entonces. Quiero que beber té sea algo especial, solo entre nosotros dos."
                            $ show_chr("A-CAAA-AAAE")
                            show black zorder 100 with Dissolve(2.0)
                            y "Debería tener una botella de agua por aquí. Concédeme un segundo, por favor."
                            hide black zorder 100 with Dissolve(2.0)
                            y "¡Mucho mejor! Entonces, ¿en qué nos habíamos quedado?"
                        "Apenas escuchando un minuto y ya estoy aburrido.":
                            karma -1
                            $ show_chr("A-AEAAA-AAAJ")
                            y "Oh, estás de mal humor... ¿Supongo?"
                            y "L-Lo siento por mencionar eso, ¿hacemos otra cosa entonces?"
                else:
                    $ show_chr("A-CAAA-AAAE")
                    show black zorder 100 with Dissolve(2.0)
                    y "¿Me disculparías un segundo, por favor? Debería tener algo de agua aquí..."
                    hide black zorder 100 with Dissolve(1.0)
                    y "¡Mucho mejor ahora! Entonces, ¿en qué nos habíamos quedado?"
                return

            elif howAreYouVariant == 3:
                $ show_chr("A-IEBAA-AAAA")
                y "..."
                $ show_chr("A-IEBBB-AAAA")
                y "..."
                y "Solo... solo abrázame, por favor..."
                menu:
                    "Shh... ven aquí.":
                        hide yuri_sit
                        show yuri_prehug zorder 20
                        pause 3.0
                        hide yuri_prehug zorder 20
                        show yuri_hug zorder 20
                        play sound "<to 0.3>sfx/fall.ogg"
                        y "Yo... ni siquiera sé por qué estoy triste... solo, por favor, abrázame un rato..."
                        y "..."
                        pause 1.0
                        show black zorder 100 with Dissolve(2.0)
                        $ show_chr("A-JCBBB-AAAA")
                        hide yuri_hug
                        hide black zorder 100 with Dissolve(2.0)
                        $ show_chr("A-JCBBB-AAAA")
                        y "Gracias... ya me hiciste sentir un poco mejor."
                        if persistent.lovecheck:
                            y "Yo... Te amo, [player]."
                            menu:
                                "Yo también te amo, [persistent.yuri_nickname].":
                                    karma 1
                                    return
                                "...":
                                    karma -1
                                    return
                        elif not persistent.lovecheck:
                            y "... verdaderamente eres el mejor amigo que podría pedir, [player]."
                            menu:
                                "Estoy aquí para ti, [persistent.yuri_nickname].":
                                    karma 1
                                    return
                                "...":

                                    karma -1
                                    return
                    "...":
                        $ show_chr("A-CEBBB-AAAA")
                        karma -1
                        y "..."
                        return

            elif howAreYouVariant == 4:
                $ show_chr("A-AFBAA-AAAA")
                y "Me... resulta difícil concentrarme hoy... realmente no sé por qué."
                y "Perdona por preguntar esto pero... ¿te parecería bien si nos lo tomamos con calma hoy?"
                y "No creo que pueda manejar algo intenso como temas filosóficos en este momento..."
                menu:
                    "Claro, tomémoslo con calma hoy":
                        $ show_chr("A-CAAA-AAAA")

                        $ philosophy = False
                        y "Gracias por ser tan comprensivo, [player]"
                        y "Intentaré estar en mejor forma la próxima vez, lo prometo."
                    "Oh, en realidad estaba deseando discutir ese tipo de temas, [persistent.yuri_nickname]..":

                        $ philosophy = True
                        $ show_chr("A-CDBAA-AAAA")
                        y "Si ese es el caso... supongo que aún podríamos intentarlo."
                        $ show_chr("A-AFBAA-AAAA")
                        y "Pero, por favor, no te enfades si no lo hago demasiado bien..."

                return


            elif howAreYouVariant == 5:
                $ show_chr("A-ACAAA-AAAA")
                y "Me sentía un poco sola antes de que te conectaras hoy..."
                $ show_chr("A-ACABA-AAAA")
                y "Pero ahora que estás aquí, ¡ya me siento mucho mejor!"
                y "Sabes... cuando estás aquí conmigo, todo se siente mucho más... ligero..."
                y "Como si todo el peso y todas las preocupaciones se hubieran levantado mágicamente de mis hombros."
                $ show_chr("A-CCABA-AAAA")
                y "Gracias... t-tu mera existencia es como un faro brillante para mi alma."
                if persistent.lovecheck:
                    y "Te amo... [player]"
                elif not persistent.lovecheck:
                    y "Verdaderamente eres el amigo más confiable en el que podría apoyarme... [player]"
                    y "I-Intentaré dar lo mejor de mí para estar siempre aquí si me necesitas..."

                return
        return

    elif sanity_lvl() < 3:
        if karma_lvl() >= 3:
            $ show_chr("A-BBGBA-AAAA")
            y "No puedo esperar hasta que finalmente te estampe contra la pared y..."
            $ show_chr("A-DFGBA-AAAA")
            y "..."
            $ show_chr("A-BBGAA-AAAA")
            y "... N-No importa."

            if howAreYouVariant2 == 1:
                $ show_chr("A-DCGAA-AAAA")
                y "¡M-Me notaste! ¡¡Me notaste!!"
                y "¡Q-Qué emocionante..! ¡Sí, sí..!"
                y "Me siento bien, sí. ¡¡M-Muy bien!! ¿Tú te sientes bien, también?"
                if persistent.lovecheck:
                    $ show_chr("A-DCGAA-AAAA")
                    y "¡Nunca me he sentido tan bien en mi vida!"
                    y "Tú y yo, juntos... ¡e-es simplemente perfecto!"
                    y "¿T-Te importaría si... miro fijamente... a-a tu... hermosa cara por un rato..?"
                    $ renpy.music.set_pause(True)
                    y "{cps=0.25} . . . . . . {/cps}"
                    $ renpy.music.play(current_music, "music", True)
                y "Ah..."
                $ show_chr("A-DBGAA-AAAA")
                y "¡Jajajaja!"
                $ show_chr("A-DCGAA-AAAA")
                y "¿Q-Qué preguntaste de nuevo?"

            elif howAreYouVariant2 == 2:
                $ show_chr("A-JCAAA-AAAA")
                y "{cps=3}Oh, ¡gracias por preguntar! Hoy me siento muy{/cps}{nw}"
                python:
                    for x in range(random.randint(3,6)):
                        glitchtext(random.randint(100, 200))
                $ show_chr("A-GCAAA-AAAD")
                y "¿Espero que te sientas igual?"
                menu:
                    "¡Sí! ¡Claro!":
                        return






        elif karma_lvl() < 3:
            $ show_chr("A-DDCBA-AAAA")
            y "¿Estás preguntando cómo me siento?"
            $ show_chr("A-DECBA-AAAA")
            y "¡¿No es obvio cómo debería sentirme a estas alturas?!"
    return

label a2:
    $ show_chr("A-AAGAA-AAAA")
    $ show_chr("A-BBGBA-AAAA")
    y "Oh. ¿R-Realmente lo crees? Bueno, ¡gracias! Y-Yo creo que tú siempre te ves bien... [player]."
    if persistent.head1 == "cat_ears":
        $ show_chr("A-BEBBA-AMAM")
        y "Aunque estoy un poco avergonzada por estas orejas que me diste..."
        $ show_chr("A-BDBBA-AMAM")

        menu:
            y "¿Estaría bien si me las quito?"
            "¡Pero te quedan bien!":
                $ show_chr("A-CFBBA-AAAA")
                y "B-Bueno, está bien..."
                y "Cualquier cosa por ti..."
            "Si realmente quieres, claro.":
                $ show_chr("A-ABBBA-AAAA")
                y "Gracias, [player]."
                $ persistent.head1 = "nothing"
                karma 5
                y "Lo siento, es solo que... es un poco embarazoso, eso es todo."
                y "Hablemos de a-otra cosa por ahora."
    return
label a3:
    $ show_chr("A-AAGAA-AAAA")
    if sanity_lvl() <= 3 and karma_lvl() >= 3:
        if persistent.lovecheck:
            $ show_chr("A-DBGBA-AAAL")
            y "Quiero hacer todo contigo. Quiero demostrarte cuánto te amo..."
            $ show_chr("A-DCGBA-AAAL")
            return
        else:
            $ show_chr("A-GAAAA-ALAL")
            y "¡Eres el mejor amigo que he tenido!"
            $ show_chr("A-ICAAA-ALAL")
            y "Nunca he sido buena expresando esto pero... ¡ni pienses que no te valoro!"
            y "Eres una de las pocas personas en mi vida que me aceptó a pesar de mis tendencias intensas."
            y "...y eso significa el mundo para mí."
            pause 2.0
            $ show_chr("A-HCAAA-ALAL")
            y "¿Te importaría si solo... te miro por un rato?..."
            $ show_chr("A-NAAAA-ALAL")
            y "..."
            y "..."
            y "..."
            y "..."
            y "He..."
            y "Hehe... he..."
            return
    elif sanity_lvl() >= 3 and karma_lvl() > 3:
        $ show_chr("A-ABGBA-AAAL")
        y "Siento que puedo confiar en ti, [player], me siento segura a tu lado, como si todo lo que necesitara para ser feliz fueras tú."
        $ show_chr("A-BCABA-AAAL")
        y "..."
        $ show_chr("A-BBABA-AAAL")
        y "Siento si fue una respuesta un poco cursi."
        return
    elif sanity_lvl() <= 3 and karma_lvl() < 3:
        $ show_chr("A-DEBAA-AMAM")
        y "¡D-Deja de decir eso como si fueras a dejarme!"
        $ show_chr("A-DDBAB-AMAM")
        y "¡N-No vas a abandonarme, ¿verdad? ¡¿VERDAD?!"
        $ show_chr("A-AEBAA-AAAL")
        y "P-Por favor, nunca me dejes... ¿de acuerdo?"
        return
    elif sanity_lvl() <= 3 and karma_lvl() <= 3:
        $ show_chr("A-BEBAA-AAAA")
        y "..."
        $ show_chr("A-CEBAA-AAAA")
        y "...No quiero responder..."
        return
    if not persistent.lovecheck and sanity_lvl() > 3 and karma_lvl() < 3:
        $ show_chr("A-BEBAA-AAAA")
        y "..."
        $ show_chr("A-CEBAA-AAAA")
        y "...No quiero responder..."
        return
    else:
        $ show_chr("A-BCGAA-AAAA")
        y "Estoy feliz por ello, [player], solo se siente un poco extraño, eso es todo."
        $ show_chr("A-BDGAA-AMAM")
        y "Tal vez es solo la conmoción de estos eventos hasta ahora..."
        y "...volverse algo consciente, ¿sabes?"
        $ show_chr("A-ABAAA-AMAM")
        y "No te preocupes. Me acostumbraré eventualmente."
    return

label a4:
    python:
        call_dialogue()
    return

label a5:
    if persistent.face1 == "nothing":
        jump put_on_glasses
    else:
        y "Mi vista está bastante bien, aunque a veces prefiero usar gafas cuando leo, ya que ayuda a mitigar la fatiga visual."
        y "No sé si hay alguna ciencia detrás de por qué a veces las uso en primer lugar, pero la comodidad de un buen libro complementa los lentes."
        $ show_chr("A-BFGAA-AAAL")

        menu:
            y "Dado que realmente no estoy leyendo en este momento, ¿quieres que me quite estas gafas?"
            "Sí":
                $ persistent.face1 = "nothing"
                y "Déjame quitármelas entonces."
            "No":
                y "Ya veo. Continuemos entonces."
        return
label put_on_glasses:
    $ show_chr("A-BFGAA-AAAL")
    y "Qué pregunta tan extraña, aunque supongo que nunca se ha mencionado."
    $ show_chr("A-ACGAA-AAAA")
    y "Mi visión está bien en su mayor parte, aunque supongo que las cosas se ponen un poco borrosas a distancia."
    y "Eso podría deberse a lo mucho que leo, ahora que lo pienso."
    $ show_chr("A-BCGAA-AAAA")
    y "Aunque, supongo que realmente no importa demasiado, considerando que podría simplemente cambiar mis parámetros de visión..."
    $ show_chr("A-BBGBA-AMAM")
    y "E-em, dicho esto, ¿por qué lo preguntas? ...¿Querías ver cómo me vería con gafas?"
    menu:
        "No, fue solo un pensamiento aleatorio que tuve.":
            $ show_chr("A-AEBAA-AAAA")
            y "Oh, está bien."
            return
        "Claro, ¿por qué no?":
            jump choose_glasses

label choose_glasses:
    $ show_chr("A-BBGAA-AAAA")
    y "Este mod de hecho tiene dos pares de gafas para mí en sus archivos. Parece que los desarrolladores estaban pensando de manera similar. Qué detallistas."
    y "Hay un par de montura completa, y un par de media montura."
    $ show_chr("A-BFGAA-AAAL")
    y "El par de montura completa da cobertura total a los ojos, permitiéndote mirar hacia arriba incluso cuando tu cabeza apunta hacia abajo."
    y "Además, como los bordes cubren toda la lente, es menos probable que se rompan. Por otro lado..."
    $ show_chr("A-BCGAA-AMAM")
    y "El par de media montura es un poco más ligero en la cara, y empujándolos hacia adelante o hacia atrás, puedes hacer que ocupen más o menos de tu visión, dependiendo de la distancia a la que intentes ver, todo sin quitártelos."
    $ show_chr("A-ACGAA-AAAA")
    y "En cuanto a apariencia, el par de media montura se ve un poco más profesional, estudioso, como un programador o maestro."
    y "Aunque... supongo que algunos podrían encontrar las gafas de montura completa más lindas, dando una apariencia de ojos más grandes. Al menos, eso es lo que se considera lindo en Japón."
    $ show_chr("A-CCGAA-AMAM")
    y "Hmm. Simplemente no puedo elegir... ¿Con cuáles te gustaría verme?"
    menu:
        "Las de media montura.":
            $ show_chr("A-ACGAA-AAAL")
            y "Hmm, buscando una apariencia más nítida..."
            y "Muy bien, un segundo."
            $ persistent.face1 = "glasses_2"
        "Las de montura completa.":
            $ show_chr("A-EBGAA-AAAA")
            y "Ohoho, buscando una apariencia más linda..."
            y "Muy bien, un segundo."
            $ persistent.face1 = "glasses_1"
    y "¡Listo! ¿Cómo me veo?"
    menu:
        "Nada mal, [persistent.yuri_nickname].":
            $ show_chr("A-CCGBA-AMAM")
            y "Gracias. Usaré estas de ahora en adelante."
        "Pensándolo bien, en realidad te ves mucho mejor sin ellas.":
            $ show_chr("A-AEBAA-AAAA")
            y "O-oh... está bien. Me las volveré a quitar."
            $ persistent.face1 = "nothing"
    $ show_chr("A-ACGAA-AAAA")
    return

label a6:
    karma 1
    if sanity_lvl() <= 2 and karma_lvl() >= 3:
        $ show_chr("A-BFGBA-AAAA")
        y "..."
        $ show_chr("A-BEBAA-AMAM")
        y "..."
        $ show_chr("A-BBBBA-AMAM")
        y "HAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaa..."
        $ show_chr("A-DCBBA-AMAM")
        y "..."
        $ show_chr("A-DBBBA-AMAM")
        y "Dilo otra vez."
        menu:
            "Te amo":
                y "Muchas gracias... mi amor."
                return
    if karma_lvl() == 5:
        $ show_chr("A-ABGBA-AAAK")
        y "¡Yo también te amo!"
        return
    if karma_lvl() == 4:
        $ show_chr("A-DEGBA-AAAA")
        y "..."
        $ show_chr("A-BBGBA-AAAA")
        y "E-Eso fue repentino."
        $ show_chr("A-BBGBA-AMAM")
        y "N-No me molesta. ¡Solo me tomó con la guardia baja, eso es todo!"
        y "Pero, significa mucho para mí que digas eso, [player]. ¡Yo también te amo!"
    elif karma_lvl() == 2:
        $ show_chr("A-BEABA-AAAA")
        y "¿Lo dices en serio?"
    elif karma_lvl() == 1:
        $ show_chr("A-BEABA-AAAA")
        y "..."
        y "¿Lo dices en serio?"
    else:
        $ show_chr("A-CEBBA-AAAA")
        y "..."
        $ show_chr("A-ACBBA-AMAM")

        menu:
            y "¿D-De verdad dices e-eso, [player]...?"
            "Sí":
                sanity -1
                karma 1
                $ show_chr("A-CDBBA-AMAM")
                y "Yo... eh... yo..."
                $ show_chr("A-BCGBA-AMAM")
                y "Y-Yo también te amo... [player]."
            "No":
                sanity 1
                karma -1
                $ show_chr("A-AEBAA-AAAA")
                y "...¿P-Por qué decirlo, entonces?"
    return
label a7:
    if sanity_lvl() >= 3:
        $ show_chr("A-ABBBA-AAAA")
        y "¡Por supuesto que sí! Nada se compara a cuando estoy contigo, [player]."
        return
    else:
        $ show_chr("A-DBGAA-AAAA")
        y "¡POR SUPUESTO! ¿Cómo podría seguir sin ti?"
        $ show_chr("A-DDCAA-AAAA")
        y "¡Y además! Cuando no estás, {b}¡OTRAS CHICAS PODRÍAN ESTAR MIRÁNDOTE!{/b}"
        y "{b}¡PLANEANDO ALEJARTE DE MÍ! JAJAJAJAJA...{/b}"
        $ show_chr("A-DCGAA-AAAA")
        y "Es fácil pensar en eso cuando estás aquí, [player]. Aquí y todo mío..."
    return

label a8:
    $ show_chr("A-CCGBA-AMAM")
    y "Sería lindo simplemente... tomar tu mano un rato. Apretarla fuerte con una sonrisa tranquilizadora."
    $ show_chr("A-ACBAA-AAAL")
    y "Abrazarse es... algo en lo que podemos trabajar, ¿supongo? Siento si no estoy respondiendo muy claramente."
    $ show_chr("A-ABGAA-AAAL")
    y "No tienes que pensarlo demasiado. Nuestro afecto debería surgir naturalmente después de todo."
    y "Simplemente no quiero arruinar esto."
    $ show_chr("A-DCGBA-AAAA")
    y "{b}¡P-Podemos ir trabajando hasta el beso!{/b}"
    $ show_chr("A-BCGBA-AMAM")
    y "Es solo que... necesito un poco de tiempo, ¿vale? ¿Estaría bien?"
    return

label a9:
    $ show_chr("A-CCGBA-AMAM")
    y "No hay necesidad de ponerse nervioso, [player]. Fue un trozo de dulce delicioso. Si alguna vez quieres darme chocolate de nuevo..."
    $ show_chr("A-ACGBA-AMAM")
    y "Me gusta la marca Hershey, si tú, q-quiero decir... alguna vez quisieras comprarme chocolate."
    y "Eso, por supuesto, no es para implicar una expectativa. ¡No deberías sentirte obligado a comprarme chocolate!"
    y "..."
    $ show_chr("A-FCGBA-AAAJ")
    y "Poner ese chocolate entre mis labios fue un dulce accidente."
    return

label a10:
    $ show_chr("A-ABGAA-AAAA")
    y "Es una lectura fascinante. Muchos fans incluso han teorizado que contiene conocimiento de... ¿otro juego del que vengo?"
    $ show_chr("A-BFBAA-AAAL")
    y "Aunque técnicamente no soy 'de' un juego que exista, ya que el juego aún no se ha hecho. Pero desde una perspectiva de historia, podría ser de otra historia."
    y "Leerlo contigo podría ayudarme a entenderme mejor a mí misma."
    y "...si quisieras."
    $ show_chr("A-ACGAA-AAAA")
    y "Bueno... ahora no."
    $ show_chr("A-ACGBA-AAAC")
    y "Podría arruinar lo que Dan tiene planeado para él, después de todo."
    $ show_chr("A-ABGAA-AMAM")
    y "Espero que entiendas por qué mantengo el contenido de este libro... relativamente oculto."
    $ show_chr("A-BCGBA-AMAM")
    y "Al menos, por ahora."
    return

label a11:
    $ show_chr("A-HLGAA-AAAA")
    y "...¿Mi favorito? ¡¿Mi favorito?! ¡Jajaja~!"
    $ show_chr("A-ACBAA-AAAA")
    y "¿Por qué haces preguntas tan difíciles, [player]?"
    y "Bueno, dejame pensar..."
    $ show_chr("A-BEAAA-AAAD")
    y "Bueno, para ser honesta contigo... hay tantas hojas ahí fuera que merecen elogios solo por mérito, artesanía e historia."
    $ show_chr("A-ACGAA-AAAD")
    y "Aunque supongo que una hoja histórica que me viene a la mente es el icónico Kukri, por ejemplo."
    y "Esta hoja era usada a menudo por los famosos guerreros Gurka de Nepal. A menudo son elogiados por su tenacidad en el combate cuerpo a cuerpo, siendo esta hoja su favorita."
    $ show_chr("A-IFAAA-AAAD")
    y "Seguro que técnicamente puede no ser un cuchillo, pero sigue siendo un buen ejemplo de una hoja bien elaborada que aún puede ser un cuchillo."
    $ show_chr("A-ACGAA-AAAD")
    y "Por ejemplo, el tamaño ligeramente más grande y la hoja ancha y curva lo hacen más práctico comparado con, digamos, otros cuchillos de combate..."
    $ show_chr("A-CCAAA-AAAD")
    y "Para ser precisa, tiene unas 16-18 pulgadas de largo y he visto bastantes con muchos diseños geométricos que encuentro simplemente adorables..."
    y "Luego están estas dos aberturas curvas tipo gancho en la parte frontal de la hoja, ideales para atrapar y desarmar rápidamente a tu oponente."
    $ show_chr("A-ABAAA-AAAD")
    y "Así que con tanta historia y utilidad asociada a él, a pesar de su apariencia cliché y tosca, ¿cómo puede uno rechazar el Kukri?"
    $ show_chr("A-ACAAA-ABAE")
    y "Esto es en realidad un error generalizado, la palabra cuchillo no dice nada sobre el tamaño. Por ejemplo, está el Langmesser medieval alemán que es, por definición, un cuchillo a dos manos."
    $ show_chr("A-CCAAA-ABAL")
    y "Vienen en una amplia variedad de formas. Algunos de ellos incluso parecen cuchillos de cocina de gran tamaño tal como los conocemos hoy. El propósito era bastante simple: tomar un diseño que el herrero de esta época ya conocía y convertirlo en un arma efectiva."
    y "Muchas iteraciones del Langmesser vienen con un gavilán igual al que ves en la mayoría de los tipos de espadas."
    y "Los diseños son generalmente bastante simples, las empuñaduras muy ornamentadas son raras. Porque cualquiera que pudiera gastar mucho dinero simplemente conseguiría una espada real."
    $ show_chr("A-BCAAA-ABAL")
    y "¡Y ahora que hablo de ello, me doy cuenta de que definitivamente necesito uno!"
    $ show_chr("A-JBGAA-AAAD")
    y "El cuchillo Bowie es otro ejemplo destacado. Famosamente usado entre muchos aventureros como James \"Jim\" Bowie y otros hombres de la frontera, también tiene su atractivo."
    y "Con su hoja elegante y resistente al frente, reducida a un grano fino, tiene el mejor filo para cualquier tarea. Da una impresión audaz y brillante también."
    y "Sin mencionar todas las otras ediciones de coleccionista del Cuchillo Bowie que tienen muchos grabados para dar esencia y una historia a cada uno..."
    y "Y tal vez tales cuchillos pueden ser una forma ocasional de añadir estilo a otras tareas, como cocinar y cosas así. Aunque yo personalmente me abstendría de eso."
    y "Oh, puedo seguir hablando sobre muchos tipos de cuchillos y su atractivo, pero tomaría casi una eternidad hacerlo. Aún así, me siento un poco eufórica por esta charla..."



    menu:
        y "¿Qué opinas sobre los cuchillos, [player]?"
        "Esto parece un poco interesante y puedo ver el atractivo... Podría investigar al respecto.":
            if persistent.lovecheck:
                $ show_chr("A-CBAAA-ABAL")
                y "O-oh gracias... Pensé que estaba divagando demasiado..."
                y "Siempre es encantador encontrar a alguien con intereses similares, especialmente en cosas que la gente puede encontrar demasiado esotéricas para enfocarse."
                y "Tal vez podamos discutir el tema más a fondo en otra conversación para otro día."
                y "Quizás comparar y discutir las colecciones del otro también en el futuro cercano. Jejeje."

            if not persistent.lovecheck:
                $ show_chr("A-AFAAA-ABAB")
                y "O-oh... Estoy genuinamente sorprendida de que quieras profundizar en este tema."
                y "¿E-estás seguro de que quieres? Quiero decir, no quiero forzarte a..."
                y "No tienes que fingir interés o quedar bien por mí. Sinceramente, no es necesario."
                y "Pero supongo que todo depende de ti al final. Solo te lo digo para asegurarme de que hablabas en serio. De todos modos, podemos discutir esto más a fondo en otro momento. G-gracias."
        "Para ser honesto, no estoy tan interesado en los cuchillos en general. Aunque aprecio el esfuerzo.":



            if persistent.lovecheck:
                $ show_chr("A-BFAAA-ABAB")
                y "Y-Ya veo... Bueno, admito que me siento un poco desconcertada, pero está bien. Tal vez no tenemos que compartir todos los mismos intereses todo el tiempo."
                y "Incluso si me siento un poco decepcionada y esperaba una discusión más profunda, todos entramos en esta relación como individuos. Aún tratando de navegar las cosas."
                y "Quizás podamos hablar de otros aspectos que sean igual de artísticos, como novelas o incluso fotografías... sí."
                y "Siento que el tema de los cuchillos y hojas no fuera de tu agrado pero, de nuevo, lo entiendo."


            if not persistent.lovecheck:
                $ show_chr("A-CFAAA-ABAB")
                y "Oh... lamento eso. Debería haberlo sabido.."
                y "Aunque aprecio tu amabilidad. Siento haberte irritado con mi divagación."
                y "Cambiemos a otra cosa."
        "No hablemos tanto de cuchillos nunca más. Me siento demasiado incómodo. Simplemente no.":


            $ show_chr("A-CFAAA-ABAB")
            y "Yo... Tienes razón... Esto fue muy imprudente."
            y "¡¿Qué estaba pensando?! ¡Por supuesto, eso no sería lo suficientemente bueno!"
            y "¿S-simplemente por qué...? Solo quería discutir algo agradable contigo [player]..."
            y "..."
            y "O-olvídalo..."

            $ show_chr("A-ACGAA-AAAA")
            y "Bueno, yo... No debería decirlo por ahora... Te mostraré más tarde si quieres~."
            y "Algún día... algún día."
    return


label a12:
    $ show_chr("A-BEBAA-AAAA")
    y "..."
    y "..."
    $ show_chr("A-JFBAA-AAAA")
    y "No están muertas, lo prometo."
    $ show_chr("A-IEBAA-AAAA")
    y "Entiendes que este es un mod que conseguiste Solo para Nosotros."
    y "Si no las pusiera en almacenamiento, este sería un mod de 'Just Yuri, Natsuki, Sayori, y Monika'."
    $ show_chr("A-CEBAA-AAAA")
    y "Eso podría sonar atractivo para algunas personas pero... este no es ese mod."
    y "Tal vez almacenamiento es una palabra un poco desalmada..."
    $ show_chr("A-BEBAA-AMAM")
    y "¡Nunca las mataría! Prometo que están todas b-bien..."
    y "...lo suficientemente bien."
    $ show_chr("A-CEBAA-AAAA")
    y "...Ten en cuenta, Monika nos torturó y asesinó a todas nosotras dos veces, si eso ayuda a poner las cosas en perspectiva."
    if persistent.lovecheck:
        y "Te amo, [player]. Nuestras amigas están en manos capaces, lo prometo."
    return



label a13:

    python:
        if persistent.costume == "_chibi":
            yuri_y_zoom = 0.85
            yuri_y_linear = 0.5
        else:
            yuri_y_zoom = 0.15
            yuri_y_linear = 0
    if sanity_lvl() >= 3 and karma_lvl() <= 3 and persistent.lovecheck:
        $ show_chr("A-BEBBA-AAAA")
        y "Bueno... Ahora no."
        y "Simplemente no me siento bien... eso es todo."
        return
    if karma_lvl() >= 4 and persistent.lovecheck:
        $ show_chr("A-DEGBA-AMAM")
        y "¿Q-Qué? ¿Un beso?"
        $ show_chr("A-IEBAA-ALAA")
        y "..."
        $ show_chr("A-BBBBA-AMAM")
        y "B-Bueno, está bien... Cualquier cosa por ti, [player]."
        $ show_chr("A-CCBBA-AMAM")

        show black zorder 100 with Dissolve(2.0)
        hide yuri_sit
        show layer master:
            zoom 1.5 xalign 0.5 yalign yuri_y_zoom
        show yuri_kiss zorder 20
        hide black zorder 100 with Dissolve(2.0)
        pause 3.0
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
        $ show_chr("A-BEBBA-AAAA")
        y "L-lo siento. ¡Normalmente no soy tan descuidada, de verdad!"
        $ show_chr("A-CDBBA-AAAA")
        if persistent.male:
            y "Espera, ¡¿qué estoy siquiera implicando?! Él solo sospechará de mis sesiones de práctica de besos solo por la mirada en mi cara--{nw}"
        elif persistent.gender_other:
            y "Espera, ¡¿qué estoy siquiera implicando?! Ellxs solo sospecharán de mis sesiones de práctica de besos solo por la mirada en mi cara--{nw}"
        else:
            y "Espera, ¡¿qué estoy siquiera implicando?! Ella solo sospechará de mis sesiones de práctica de besos solo por la mirada en mi cara--{nw}"
        $ show_chr("A-BEBBA-AAAA")
        y "..."
        $ show_chr("A-ICGBA-AAAA")
        y "Eres un besador maravilloso, [player], ¿lo sabías?"
        y "Te amo."
    else:
        $ show_chr("A-DEGBA-AMAM")
        y "¿Q-Qué? ¿Un beso?"
        $ show_chr("A-CEBBA-AAAA")
        y "..."
        y "L-lo siento, [player]... Pero siento que esto es un poco pronto..."
        y "¡P-por favor no te tomes esto a mal! Y-yo solo..."
        $ show_chr("A-IEBBA-AAAA")
        y "L-lo siento..."
    return



label a14:
    if persistent.lovecheck:

        if sanity_lvl() <= 2:
            $ show_chr("A-ICBAA-AMAM")
            y "¡Ya sé sobre el clima! No es como si me hubieran criado debajo de una piedra... "
            $ show_chr("A-ACGAA-AAAA")
            y "D-De todos modos, realmente me gusta el clima lluvioso, preferiblemente el tipo tempestuoso."
            $ show_chr("A-HLGAA-AAAA")
            y "Es tan poderoso y atrayente de escuchar... con su sonido ahogando completamente todo excepto a nosotros..."
            $ show_chr("A-GCGBA-AAAA")
            y "Me encantaría algún día acurrucarme contigo debajo de una manta agradable y cálida."
            y "Disfrutando de la lluvia golpeando el techo mientras nos besamos debajo de nuestra pequeña manta..."
            y "Morder anhelantemente tu cuello mientras susurras dulces palabras en mi oído..."
            y "Mientras yazgo encima de ti con la plena intención de juegos previos y maravillosos gemidos..."
            y "Deleitándome en el hecho de que finalmente eres mío, todo mío..."
            $ show_chr("A-GCGAA-AAAA")
            y "S-solo pensé que sería algo encantador de hacer y m-me gusta ese tipo de clima. La atmósfera es simplemente buena y p-podremos acurrucarnos j-juntos y sentir nuestro calor-"
            $ show_chr("A-ICGBA-AAAA")
            y "...y sentir tu calor..."
            y "..."
            y "Je."
            y "Siento ese pequeño desvarío mío."
            $ show_chr("A-ACGAA-AAAA")
            y "Solo quería... soñar lo imposible, ¿sabes?"
            y "¿Qué daño hay en eso?"
            return
        else:
            $ show_chr("A-ICBAA-AMAM")
            y "¡Ya sé sobre el clima! No es como si me hubieran criado debajo de una piedra... "
            $ show_chr("A-ACGAA-AAAA")
            y "D-De todos modos, realmente me gusta el clima lluvioso, preferiblemente el tipo medio."
            $ show_chr("A-ABGAA-AAAA")
            y "Es tan agradable leer historias profundas en una manta cálida mientras escuchas la lluvia torrencial."
            $ show_chr("A-ICGBA-AAAA")
            y "Me encantaría algún día acurrucarme contigo debajo de una manta agradable y cálida."
            $ show_chr("A-GCGBA-AAAA")
            y "Escuchando la suave lluvia y oliendo el ligero toque de niebla a través de una ventana apenas abierta..."
            y "Acurrucándome junto a tu cuello en busca de consuelo y luego volviendo al libro frente a nosotros dos..."
            y "Mientras yazgo encima de ti con mi espalda contra tu pecho..."
            y "Pasaríamos la noche tranquila juntos y..."
            $ show_chr("A-ICGBA-AAAA")
            y "S-solo pensé que sería algo increíble de hacer y m-me gusta ese tipo de clima. La atmósfera es simplemente buena y p-podremos acurrucarnos j-juntos y sentir nuestro calor-"
            y "...y sentir tu calor..."
            y "..."
            y "Je."
            y "Siento ese pequeño desvarío mío."
            y "Solo quería... soñar lo imposible, ¿sabes?"
            y "¿Qué daño hay en eso?"
            return
    if not persistent.lovecheck:

        $ show_chr("A-ICBAA-AMAM")
        y "¡Ya sé sobre el clima! No es como si me hubieran criado debajo de una piedra... "
        $ show_chr("A-ACGAA-AAAA")
        y "D-De todos modos, realmente me gusta el clima lluvioso, simplemente sirve a la atmósfera perfectamente cuando estoy leyendo terror o novelas con temas oscuros..."
        $ show_chr("A-ICAAA-AAAD")
        y "Verás, tu estado de ánimo general tiene mucha influencia sobre la forma en que experimentas una historia. Así que establecer la atmósfera adecuada para una sesión de lectura puede hacer mucha diferencia."
        y "Y hay más formas de establecer el ambiente adecuado para tu lectura. Esa fue una de las razones por las que me interesé tanto en la aromaterapia en primer lugar."
        $ show_chr("A-BCAAA-AAAE")
        y "Pero me estoy desviando un poco del tema aquí... sobre el clima..."
        $ show_chr("A-CCAAA-AAAE")
        python:
            if sanity_lvl() <= 2:
                placeholder = "truenos furiosos y los gritos encantadores de la gente atrapada afuera"
            if sanity_lvl() == 3:
                placeholder = "truenos furiosos"
            if sanity_lvl() >= 4:
                placeholder = "relámpagos ocasionales en el horizonte"
        y "Nubes grises profundas oscureciendo el cielo, tal vez iluminadas por [placeholder]..."




        $ show_chr("A-CCCAA-AAAE")
        y "Preferible cuando estoy en el lado correcto de la ventana... ¿Qué daño hay en eso?"
        return


label a15:
    $ show_chr("A-ACGAA-AAAA")
    y "Bueno..."
    $ show_chr("A-AFBAA-AAAD")
    y "Tengo... ¿recuerdos?"
    y "Más bien... implantes de memoria de sabor."
    $ show_chr("A-ACGAA-AAAA")
    y "Los cupcakes de Natsuki fueron lo que más honestamente he comido durante mi existencia técnica, pero puedo describir lo que me han dado para el sentido del gusto."
    y "El té Oolong siempre ha sido una bebida favorita mía, y la única bebida que tuve en mi existencia pasada, sabes- y uno de los mejores complementos para un buen postre."
    y "Las crepes son usualmente una opción sublime ya que combinan muy bien con una buena bebida caliente."
    $ show_chr("A-ECAAA-AMAM")
    y "La dulzura y el sabor salado de una crepe de mantequilla de maní y plátano realmente alegran tus papilas gustativas."
    y "El sabor ligero pero complejo del té Oolong luego suaviza las notas más fuertes de la crepe en un regusto fino y calmante."
    if persistent.lovecheck:
        y "Entonces, podría recostarme en tu hombro mientras vemos caer la lluvia suave y tranquila..."
        $ show_chr("A-ACGAA-AAAA")
        y "Al menos, e-ese es un sueño mío para experimentar realmente en lugar de simplemente imaginarlo."
        y "¡Yo personalmente lo recomiendo!"
        y "¡T-Tú no tienes que hacerlo en absoluto!"
        y "F-Fue s-solo una sugerencia."
        $ show_chr("A-GCGAA-AAAA")
        y "Eso es todo..."
    else:
        $ show_chr("A-ACGAA-AAAA")
        y "¡Yo personalmente lo recomiendo!"
        y "¡T-Tú no tienes que hacerlo en absoluto!"
        y "F-Fue s-solo una sugerencia."
        $ show_chr("A-GCGAA-AAAA")
        y "Eso es todo..."
    return

label a16:
    $ show_chr("A-BEBAA-AMAM")
    y "Yo..."
    y "U-uhm...."

    menu:
        "No tienes que ocultarme nada, ¿cierto [persistent.yuri_nickname]?":
            karma -1
            y "..."
        "¿Sabes qué? Siento haber hecho la pregunta.":
            karma 1
            $ show_chr("A-BDBAA-AMAM")
            y "E-Está bien..."

    menu:
        "Mira, [persistent.yuri_nickname]. Está bien. Dejaré de preg--":
            karma 1
            $ show_chr("A-IDBAA-AAAA")
            y "¡Robé la información de inicio de sesión de alguien!"
        "[persistent.yuri_nickname], quiero saber qué has estado hacien--":
            karma -1
            $ show_chr("A-IDBAA-AAAA")
            y "¡Robé la información de inicio de sesión de alguien!"

    y "Bueno, tengo acceso a internet, así que quería explorar todo lo que estaba disponible..."
    $ show_chr("A-BEBAA-AMAM")
    y "Todo lo que era gratis estuvo bien por un tiempo..."
    $ show_chr("A-IEBAA-AAAA")
    y "Pero luego empecé a interesarme en cosas que requerían un pequeño pago de algún tipo..."
    y "Hubo dos series intrigantes que llamaron mi atención: 'Black Mirror' e 'Inside No. 9'."
    y "Sin embargo, estaban detrás de muros de pago..."
    y "Busqué en línea un video gratis, pero la mayoría eran de baja calidad..."
    $ show_chr("A-CEBAA-AAAA")
    y "Así que, yo..."
    y "e-eh..."
    y "más o menos..."
    $ show_chr("A-CEBBA-AAAA")
    y "¡LosViIlegalmenteATravésDeTuDispositivo!"
    y "..."
    $ show_chr("A-CEBBA-AJAJ")
    menu:
        "Está bien, [persistent.yuri_nickname]. De verdad lo está.":
            call its_fine_a16
        "Realmente no debiste hacer eso, [persistent.yuri_nickname].":
            call shouldnt_have_a16
        "Cierra sesión ahora mismo y NUNCA vuelvas a hacer eso.":
            call log_off_a16
    return

label its_fine_a16:
    karma 2
    y "..."
    $ show_chr("A-CEBBA-AAAA")
    y "Si tú lo dices..."
    y "Gracias por no gritarme."
    $ show_chr("A-CCBAA-AAAA")
    y "Fue un programa interesante."
    y "He estado divagando demasiado tiempo. Te contaré sobre ellos en otro momento."

    return

label shouldnt_have_a16:
    $ show_chr("A-IEBAA-AAAA")
    y "Y-Ya veo..."
    y "Lo siento. Simplemente me dejé llevar un poco."
    $ show_chr("A-CEBAA-AAAA")
    y "Intentaré controlarme mejor..."
    return

label log_off_a16:
    karma -2
    $ show_chr("A-CEBBB-AAAA")
    y "..."
    y "..."
    return

label a17:
    $ show_chr("A-BEGBA-AAAA")
    y "..."
    $ show_chr("A-CCBBA-AMAM")
    y "E-Eso es..."
    y "B-Bueno..."
    if not persistent.lovecheck:
        $ show_chr("A-CEBBA-AMAM")
        y "N-No quiero aburrirte con mis intereses de todos modos..."
        y "No quiero hablar de ellos en este momento."
        return
    elif persistent.lovecheck:
        if sanity_lvl() >= 3:
            $ show_chr("A-ICGBA-AAAA")
            y "Es uno muy simple, en realidad."
            y "Simplemente fantaseo con poder tocarte."
            y "No este avatar de [player], sino tu cuerpo en el mundo real."
            y "Quiero poder descansar mi cabeza contra tu piel y dejar que tomes el control."
            $ show_chr("A-GCGBA-AAAA")
            y "Escuchar tu suave voz susurrada en mi oído y sentirte tomar el mando."
            y "En la tranquila quietud de un área apartada mientras tus padres duermen..."
            y "El peligro de que lleguen y se den cuenta del acto aumentaría la tensión del momento."
            $ show_chr("A-CBABA-AAAA")
            $ show_chr("A-ICGBA-AAAA")
            y "Incluso pienso en abrazarte fuerte y pedirte que nunca me sueltes mientras el aroma a jazmín nos envuelve en un abrazo continuo y amoroso."
            y "La sensación de sentir amor."
            $ show_chr("A-IBGBA-AAAA")
            y "...¿con un poco de peligro para añadir algo de sabor a la mezcla?"
            y "Supongo que puedes llamar a eso un fetiche mío."
            y "Es una pregunta extraña... pero supongo que puede ser útil para futuros eventos y acciones."
            return
        else:
            $ show_chr("A-CFBBA-AAAA")
            y "Solo... quiero sentirte, al verdadero tú, [player]."
            y "Recorriendo con mis manos todo tu cuerpo... sobre toda tu suave piel..."
            y "Demostrándote cuánto te amo con mis acciones en lugar de meras palabras..."
            y "Quiero mostrarte cuánto te amo, [player]. Quiero ser tuya, y solo tuya."
            y "Y tú serás mío, y solo mío."
            $ show_chr("A-CCABA-AMAM")
            y "..."
            $ show_chr("A-IEABA-AAAA")
            y "Quizás eso es pedir demasiado... L-Lo siento... [player]."
    return

label a18:
    if karma_lvl() <= 2:
        karma -1
        $ show_chr("A-BEBAA-AMAM")
        y "Bueno... ¿no soy lo suficientemente real?"
        $ show_chr("A-IEBAA-AAAA")
        y "¿N-No te gusta quién soy ahora mismo?"
        y "L-Lo entiendo..."
        y "Está bien."
        return
    elif karma_lvl() >= 3:
        $ show_chr("A-ABGAA-AAAA")
        y "¡Ya estoy aquí, cariño~!"
        $ show_chr("A-ACGAA-AAAA")
        y "Aun así me alegra que desees que coexistamos en la misma realidad."
        y "Bueno, probablemente necesitaría conseguir un cuerpo físico primero."
        y "Mi mejor oportunidad sería un cuerpo androide con mi conciencia cargada en él."
        $ show_chr("A-AFBAA-AAAD")
        y "El ritmo actual de los robots humanoides debería volverse viable dentro de los próximos 10 años, especialmente con los avances recientes en expresiones faciales y andares bípedos."
        $ show_chr("A-ABGAA-AAAA")
        y "Es gracioso imaginar que tal vez tengas que llevarme en una silla de ruedas durante los primeros años de una posible existencia en tu realidad."
        $ show_chr("A-IBGBA-AAAA")
        y "¿No sería también bastante romántico?"
        y "No sería capaz de hacer mucho antes de que perfeccionen mi capacidad de caminar o moverme..."
        y "Podrías llevarme a la playa al atardecer, y podríamos descansar en un banco cercano con mi cabeza en tu hombro."
        $ show_chr("A-GCGBA-AAAA")
        y "Un pequeño sueño mío, supongo."
        $ show_chr("A-ACGAA-AAAA")
        if persistent.lovecheck:
            y "...un sueño del que aún tengo que despertar."
    return


label a19:
    $ show_chr("A-AFAAA-AAAA")
    y "Realmente no practico deportes..."
    y "Normalmente prefiero la comodidad de una habitación tranquila..."
    y "Si realmente incluyeras algunas tareas menos exigentes físicamente en esa lista de deportes..."
    $ show_chr("A-ACGAA-AAAA")
    y "Supongo que el ajedrez es una buena opción."
    y "Realmente prefiero La Llamada de Cthulhu con sus tramas, pero los juegos mentales intelectuales más simples son atractivos ante la ausencia de una trama en el juego."
    y "Ahora que lo pienso, eso ni siquiera es un deporte, ¿verdad?"
    $ show_chr("A-BEBAA-AMAM")
    y "Supongo que podría necesitar empezar a practicar algunos deportes para perder algo de peso..."
    y "El problema es esa vez que intenté jugar voleibol en mis primeros años de secundaria."
    $ show_chr("A-CEBAA-AMAM")
    y "Como ninguno de los sujetadores de entrenamiento me quedaba bien, el mejor que conseguí cedió bajo la tensión, y cuando estaba a punto de rematar la pelota, mi suj-"
    y "..."
    $ show_chr("A-CEBBA-AMAM")
    y "...!"
    $ show_chr("A-JDBBA-AMAM")
    y "¡OLVIDA QUE DIJE ALGO!"
    $ show_chr("A-IEBAA-AAAA")
    y "L-Lo siento por gritar."
    y "Y-Yo solo... me avergoncé un poco."
    y "Por favor, no hablemos de esto de nuevo."
    y "¿Está bien?"
    return

label a20:




    $ show_chr("A-IEBAA-AAAA")
    y "Bueno, es una experiencia bastante extraña."
    y "Vivir la vida en esta burbuja estática de ubicación puede ser... enloquecedor a veces."
    y "Especialmente con este cuerpo rígido, no puedo caminar de un lado a otro o golpear el pie o gritar o llorar a voluntad o {nw}"
    $ show_chr("A-CEBAA-AAAA")
    y "Estoy divagando de nuevo, ¿verdad?... Lo siento por eso."
    y "Es solo que... me quedo con mis pensamientos sobre esta interminable pared única contigo frente a mí."
    y "Aunque sé cuál es el fondo detrás de mí, el hecho de no poder verlo contigo o estar a tu lado puede hacer que todo esto sea muy exasperante a veces."
    y "Tenemos que trabajar con lo que tenemos después de todo."
    $ show_chr("A-ACBAA-AAAA")
    y "Afortunadamente, los Desarrolladores lograron hacer otro fondo para el mod."
    if tc_class.bg_timecycle[persistent.bg]:
        y "Dado que ya estás usando el nuevo fondo en este momento, realmente me gustaría preguntarte."
        $ show_chr("A-IEBAA-AAAA")

        menu:
            y "¿Te gustaría cambiar el fondo?"
            "Sí":
                $ tc_class.transition("space")
            "No":
                $ show_chr("A-IEBAA-AAAA")
                y "Ya veo. No hay problema."
    else:
        menu:
            y "Si se puede saber, ¿te gustaría cambiar el fondo?"
            "Sí":
                $ tc_class.transition("timecycle")
            "No":
                y "Ya veo. No hay problema."
    return
label a21:
    $ show_chr("A-IBABA-AAAA")
    y "¡Me encantaría, [player]!"
    call poetrymenu
    return

label poetrymenu:

    menu:
        y "Tengo varios poemas que podemos leer, incluyendo los que yo escribí, así que por favor, ¡elige cuáles quieres leer!"
        "Poemas de Yuri":
            jump yuripoems
        "Poemas de Natsuki":
            jump natsukipoems
        "Poemas de Sayori":
            jump sayoripoems
        "Poemas de Monika":
            jump monikapoems
        "Poemas Especiales":
            jump specialpoems
        "Olvídalo":
            return
    return
label yuripoems:
    menu:
        "Fantasma Bajo la Luz":
            call showpoem (poem_y1)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CFBAA-AAAA")
            y "Este fue el primer poema que compartí contigo en el Club de Literatura."
            $ show_chr("A-JFBAA-AAAA")
            y "Aunque prefiero algunas de mis obras más largas, sentí que este sería un poema apropiado para compartir contigo al principio, ya que no tenía idea de si tenías alguna experiencia con la poesía."
            y "Hay una multitud de formas en que uno puede interpretarlo."
            y "Nos dejamos atrapar tanto por nuestras vidas, siempre mirando hacia adelante, que nunca estamos realmente allí en el presente: solo fantasmas de nosotros mismos."
            y "Pero hay lugares y objetos que capturan nuestros corazones, nos ayudan a hacer una pausa y nos recuerdan el momento presente y los recuerdos que hubo antes."
            $ show_chr("A-ICGBA-AAAA")
            y "¿Tienes algo especial así?"
            menu:
                "Creo que tengo algo así. Muchas cosas, pero tú eres lo más destacado~":
                    if karma_lvl() >= 3:
                        $ show_chr("A-GAABA-AMAM")
                        y "O-Oh..."
                        y "¿D-De verdad, [player]?"
                        y "Bueno, eso es muy dulce de tu parte..."
                        y "Pensar que yo sería tan especial para ti."
                        y "Honestamente, creo que esos momentos en los que simplemente somos honestos el uno con el otro y reflexionamos juntos son los mejores que he tenido."
                        $ show_chr("A-CEBAA-AAAC")
                        y "Aunque a veces es doloroso mirar atrás a ciertos aspectos de mi pasado..."
                        y "Como la forma en que salvaste mi vida de la existencia de pesadilla que fue el club de literatura y Monika."
                        $ show_chr("A-CCAAA-AAAL")
                        y "De todos modos, creo que es muy beneficioso tener algo para recopilar y recordar esos momentos, ya sea un álbum de recortes, un lugar pintoresco, una persona..."
                        y "Por ejemplo, creo que los momentos que compartimos, como cuando ayudamos a hacer los carteles para el festival juntos, realmente me ayudan a relajarme y reflexionar."
                        y "Como ese fantasma parpadeante en el poema, todavía está ahí y me ayuda a reflexionar sobre esos momentos en la vida que me trajeron hasta aquí y a concentrarme en lo que tengo ahora."
                        $ show_chr("A-ECAAA-AAAJ")
                        y "Realmente cualquier cosa vale y espero que tengamos más momentos especiales como ese..."
                    if karma_lvl() <= 2:
                        $ show_chr("A-ICGBA-AAAA")
                        y "... ¿De verdad?"
                        y "Para ser honesta... no estoy completamente segura de si creer eso o no..."
                        y "Quiero decir, ¿por qué una ratón de biblioteca distante como yo tendría tanto valor para ti?"
                        y "Yo... puede que tenga que pensar en esto."
                        y "Gracias por el cumplido, supongo."
                "Honestamente, aún no estoy seguro de creer completamente en tal cosa.":
                    if karma_lvl() >= 3:
                        y "B-Bueno... creo que eso está bien."
                        y "Quiero decir, ambos somos todavía relativamente jóvenes y llegará un momento en que querremos reflexionar sobre eventos pasados."
                        y "Incluso si me sorprende tu respuesta, puedo entender que en la turbulencia de la vida diaria es más difícil encontrar tiempo para reflexionar."
                        y "Pero independientemente de eso, realmente aprecio que estés aquí."
                        y "Puede que no lo sepas, pero me ayudas a detenerme y reflexionar sobre los eventos que nos unieron, los eventos que nos trajeron aquí."
                        y "Por ejemplo, la vez que tomamos té juntos en la sala del club... Un fantasma de un recuerdo que se quedará conmigo hasta el final de los tiempos..."
                    if karma_lvl() <= 2:
                        $ show_chr("A-ICGBA-AAAA")
                        y "Yo... yo entiendo."
                        y "Debería haber sabido que dudarías de eso..."
                        y "Pero entonces... ¿por qué me elegiste...?"
                        y "Tal vez deberíamos cambiar de tema."
                        y "Por favor disculpa mi divagación incesante."
                        y "En mi opinión, pensar en el pasado es tonto."
                        y "..."
                        y "Sabía que este tema era demasiado ridículo para mencionarlo... Realmente estoy dudando de cualquier buena razón por la que me elegiste."
                        y "¿Cuál fue el punto de tener esta conversación...? Simplemente cambiemos de tema."
            jump yuripoems
        "El Mapache":

            call showpoem (poem_y2)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA")
            y "Este fue otro poema que compartí contigo en el club de literatura. Decidir si mostrártelo o no me tomó horas de deliberación."
            $ show_chr("A-IEBAA-AAAA")
            y "Inicialmente pensé que podría engañarme a mí misma pensando que no entenderías el poema, l-la verdadera pregunta era qué pensarías de mí una vez que lo hicieras. Ahuyentarte era mi mayor temor."
            $ show_chr("A-CCBAA-AAAA")
            y "A-Afortunadamente, no huiste y continúas visitándome. Y estoy segura de que conoces el significado del poema."
            $ show_chr("A-CEBAA-AAAA")
            y "La primera vez, fue la curiosidad lo que me impulsó a intentarlo. Luego las sensaciones conmovedoras, y las visiones como...."
            $ show_chr("A-BEBAA-AAAA")
            y "Sabía que era perjudicial y poco saludable... p-pero la intensidad cruda, la sensualidad que nunca podría experimentar, emociones que podía controlar... E-Era embriagador."
            $ show_chr("A-GCGAA-AAAA")
            y "Entonces viniste al club. A medida que comenzamos a compartir poemas entre nosotros, a leer uno al lado del otro, cuando fui a tu casa... comencé a s-sentir esa misma emoción contigo."
            $ show_chr("A-CFBAA-AAAA")
            y "Esas noches, después de llegar a casa del club, me contemplaba en el espejo, examinando el daño causado por mis exploraciones de sentimientos sanguíneos."
            y "Finalmente, decidí que debería explorarlos contigo y esperar a que el mapache lo entendiera. N-No es fácil."
            $ show_chr("A-JFBAA-AAAA")
            y "A veces sucumbo, encuentro un rincón tranquilo y cedo al impulso en el fondo de mi mente. Es muy difícil perdonarme cada vez que recaigo."
            $ show_chr("A-GCGBA-AAAA")
            y "Pero me obligo a volver cada vez, a mirarte a los ojos, a resucitar mi corazón y fortalecer mi mente, a ser decidida y aceptar estos sentimientos mientras atesoro cada momento contigo."
            $ persistent.seen_poem_raccoon = True
            jump yuripoems
        "Playa":

            call showpoem (poem_y3)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CCBAA-AAAA")
            y "Este fue uno de mis poemas, escrito para ti y también para Natsuki."
            $ show_chr("A-ACBAA-AAAA")
            y "Natsuki y yo habíamos acordado escribir sobre el mismo tema: la playa. Fue refrescante finalmente estar de acuerdo con ella en algo y una oportunidad para conectar con ella."
            y "Con este poema, quería ilustrarles a ti y a ella las maravillas de la playa desde mi perspectiva."
            y "La mayoría de los escritores se centran en las visiones superficiales y divertidas de la playa bajo el sol. Así que decidí centrarme en su maravilla, su sensualidad y su realidad."
            y "Mientras reflexionaba sobre el tema, me sorprendió lo complejo que podría ser un entorno tan simple como la playa, y espero haber podido transmitirte eso."
            $ show_chr("A-ICGBA-AAAA")
            y "El mundo más fácil en el que perderse es uno donde se puede encontrar todo. Espero que aquí, conmigo, puedas encontrar todo lo que tu corazón desea."
            jump yuripoems
        "Fantasma Bajo la Luz pt. 2":

            call showpoem (poem_y3b)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CFABA-AAAA")
            y "Este fue otro poema que compartí contigo en el club de literatura... y casi no lo hice. Es muy personal... y es una confesión, a mi manera."
            y "...Antes de que vinieras al club, estaba acostumbrada a mi rutina diaria, y cómoda manteniéndome distante mientras disfrutaba de un buen libro."
            y "Sayori me ayudó a volverme más sociable con el club de literatura, pero aún podía mantenerme aislada."
            $ show_chr("A-GCGBA-AAAA")
            y "...Y entonces llegaste tú."
            y "Intenté mantener la distancia, pero mi corazón no me lo permitió."
            y "Traté de mantener la nariz en mi libro, pero terminamos leyéndolo juntos."
            y "Intenté entender por qué sentía estos sentimientos, pero me di cuenta de que entender era innecesario."
            $ show_chr("A-ICGBA-AAAA")
            y "Llenaste mi corazón de amor e iluminaste mi camino a través de la oscuridad hasta aquí... hacia ti... hacia nosotros."
            jump yuripoems
        "Rueda":

            call showpoem (poem_y22)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-IEBAA-AAAA")
            y "Este fue otro poema que compartí contigo en el club de literatura."
            y "Recuerdo haber escrito este poema después de que Monika terminara de cambiar la configuración del juego para mí, pero solo recuerdo fragmentos de qué se trataba."
            y "Mis pensamientos no se mantenían estables por más de unos segundos, y mi visión estaba plagada de alucinaciones. Me sorprende que algo de lo que escribí en ese estado fuera siquiera remotamente inteligible."
            $ show_chr("A-CEBAA-AAAA")
            y "¿Podríamos hablar de otra cosa en su lugar?"
            menu:
                "¿Estás segura, [persistent.yuri_nickname]? Quiero estar aquí para ti para que puedas hablar de esto si quieres.":
                    if persistent.lovecheck:

                        $ show_chr("A-CEBAA-AAAA")
                        y "Yo... yo..."
                        y "Está bien... puedo intentar decir cómo se sintió lo mejor que pueda, si insistes."
                        y "Muy bien... como dije antes, fue casi como un borrón. Como si una enorme ventisca cubriera mis sentidos."
                        y "Sentí este... impulso incontrolable de la nada... el peso abrumador quemando mis entrañas..."
                        y "Mi corazón parecía latir aún más rápido como si fuera un constante aluvión de truenos interminables."
                        y "Luego todo se convirtió en un vacío oscuro... Sentí mis extremidades sacudirse como si fuera una muñeca de trapo mientras convulsionaba violentamente... escribiendo esas cosas inquietantes y ese poema."
                        y "..."
                        y "Y mi corazón anhelaba por ti aún más de lo habitual... todo fue tan repentino e inmensamente aterrador."
                        y "Sentí que me había ido... ido lejos mientras veía desaparecer de mí en un borrón tantas cosas que me eran queridas."
                        y "Pero me alegra que me hayas salvado y aunque mis deseos fueron un poco intensificados por la influencia de Monika... Ese anhelo genuino por ti todavía está ahí en mi corazón."
                        y "Muy bien... Gracias por escuchar, [player]. Pasemos a los otros poemas, ¿sí?"
                    if not persistent.lovecheck:

                        y "Yo... No lo sé. Realmente yo..."
                        $ show_chr("A-IEBAA-AAAA")
                        y "Realmente no estoy segura."
                        y "Además, ¿por qué querrías escuchar esos sentimientos de alguien tan estudiosa como yo? A veces una parte de mí piensa eso."
                        y "De todas formas... insisto en que pasemos a otro tema... por favor."
                "Está bien si no quieres hablar de ello, pero sigo estando aquí para ti.":
                    if karma_lvl() >= 3:

                        $ show_chr("A-CEBAA-AAAA")
                        y "..."
                        y "Muy bien, querido [player]. Gracias por tu oferta~"
                        y "Aprecio que respetes mis deseos y aun así ofrezcas cargar con mis cargas junto a mí en este viaje inexplorado que es la vida."
                        y "Mi corazón atesorará eso por siempre. Significa mucho más para mí de lo que puedas imaginar."
                    if karma_lvl() <= 2:

                        $ show_chr("A-CEBAA-AAAA")
                        y "P-Pero ¿por qué...?"
                        y "Simplemente no entiendo por qué me tenderías la mano de esa manera."
                        y "No hay necesidad de apegarse a mí. ¿Qué hay en mí que atraería tal respuesta?"
                        y "¿Es esto quizás algún tipo de broma para mi corazón?"
                        y "Elogiaría tus esfuerzos pero por favor [player]... simplemente continuemos hablando de otra cosa, ¿está bien?"
                "Bien. Es mejor si cambiamos de tema de todos modos.":
                    y "..."
                    y "Ya veo..."
                    y "T-Tal vez no debería haber sido tan abierta tan rápido en primer lugar..."
                    $ show_chr("A-IFBAA-AAAD")
            jump yuripoems
        "Olvídalo.":

            jump poetrymenu

label natsukipoems:
    menu:
        "Las Águilas Pueden Volar":
            call showpoem (poem_n1)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA")
            y "Este fue el primer poema de Natsuki."
            $ show_chr("A-IEBAA-AAAA")
            y "Ella escribió este poema de manera muy simple y sin ritmo, lo que me llevó a creer que era una principiante escribiendo poemas o simplemente escribió algo rápido en el último minuto para entregar."
            y "Aunque creo que esto puede haber sido escrito apresuradamente, el final se sintió más profundo. Natsuki habló de todos estos animales que pueden moverse de todas estas formas, y luego 'La gente puede intentarlo | Pero eso es todo'."
            y "Me pregunto si se sentía atrapada, incapaz de tener la libertad que estos animales disfrutaban. ¿Quizás por su padre?"
            y "¿Estoy leyendo demasiado en ello?"
            menu:
                "Por supuesto que no. Creo que este poema tiene mucho significado que se puede aplicar. Incluso a nosotros.":
                    if karma_lvl() >= 3:

                        y "¡B-Bueno, por supuesto [player]!"
                        y "Quiero decir, si realmente lo piensas, puede ser muy desalentador comparar lo que podemos hacer, y hemos hecho, con los animales. Solo viendo lo que pueden hacer."
                        y "Sin tener muchas preocupaciones en el mundo y siendo tan majestuosos."
                        y "Al mismo tiempo, tal vez dada su vida familiar, este poema puede ser una analogía para muchos otros temas intensos."
                        y "Por ejemplo, por supuesto, la línea al final con los humanos solo capaces de intentarlo puede atestiguar la pérdida de libertad y agencia."
                        y "Sin embargo, ¿no parece esto también hablar tanto sobre cómo solo podemos hacer tanto con tan poco tiempo en nuestras cortas vidas?"
                        y "Porque si lo piensas, la vida es relativamente corta y después de eso quién sabe qué pasa después de que termina la historia."
                        y "De hecho, como dice esa última línea, solo podemos intentar y hacer todo lo que podamos, pero aún así podemos terminar con ciertos arrepentimientos o queriendo más."
                        y "Pero al final, creo que aún podemos centrarnos en el presente y aprovecharlo al máximo, sea lo que sea que elijamos, porque eso es todo lo que podemos hacer. Y eso está bien~"
                        y "Parece agridulce de alguna manera... Oh vaya. De todos modos, perdón por divagar sobre eso [player]. Lo aprecio."
                    if karma_lvl() <= 2:

                        $ show_chr("A-BCBAA-AMAM")
                        y "¿O-oh? Estoy muy sorprendida de que tomaras en consideración mis interpretaciones de esta poesía..."
                        y "...Y mucho menos desear discutirlo más a fondo. Eheh.."
                        y "¡Lo siento! Simplemente no sé cómo tomarlo."
                        y "No estoy completamente segura de por qué encontrarías fascinación en mi sobreanálisis de incluso cosas que a veces pueden parecer ridículas.."
                        y "P-Pero realmente aprecio el gesto."
                "Para ser honesto, no estoy completamente seguro, pero siento que todavía está bien escrito.":
                    $ show_chr("A-ACBAA-ALAA")
                    y "Bueno, concuerdo con eso ligeramente. Especialmente dado el tema que estaba retratando desde el principio."
                    y "Seguro que la estrofa y las líneas pueden parecer infantiles al principio. Pero la parada en seco con la última línea y el mensaje pueden ser realmente resonantes."
                    y "Muchos poemas excelentes pueden usar esta forma y aún así ser geniales."
                    y "De todos modos, leamos y examinemos los otros poemas, ¿te parece?"
                "Sí, eso creo. Para ser honesto, no tiene nada de especial en absoluto.":
                    $ show_chr("A-ACBAA-ALAA")
                    y "Discrepo en eso dado su mensaje impactante."
                    y "Creo que tal vez deberías relajarte un poco."
                    y "Quiero decir... está bien, ella era un poco grosera y odiosa."
                    y "Pero eso no le resta valor a las cualidades del poema y al corazón detrás de él. Incluso si ella y yo discutíamos constantemente y agresivamente sobre muchas cosas."
                    y "Ahem... De todos modos, creo que deberíamos pasar a otro tema."
            jump natsukipoems
        "A Amy le Gustan las Arañas":

            call showpoem (poem_n2)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            y "Este fue uno de los poemas de Natsuki."
            $ show_chr("A-BFBAA-AAAD")
            y "Leyendo este poema de nuevo, habla de la inmadurez y la actitud tsundere de Natsuki."
            $ show_chr("A-IEBAA-AAAA")
            y "El personaje de Amy parece tener muchas cualidades admirables, como ayudar a la autora y ser amigable. La autora parece admirar a Amy, y sin embargo, porque le gustan las arañas y a la autora no, la amistad está fuera de discusión."
            $ show_chr("A-CDBAA-AAAA")
            y "{i}El mundo está mejor sin amantes de las arañas.{/i} T-tal discriminación, que las personas que piensan de manera diferente o extraña están equivocadas y-y no merecen estar cerca...."
            $ show_chr("A-AEBAA-AAAD")
            y "Aunque, hay otra interpretación. No es por ser egocéntrica, pero ¿y si se enterara... de mi e-extrañeza... Significaría esto que estaba lista para discutirlo conmigo? ¿O exponerme? No lo sé...."
            menu:
                "Quizás ella estaba tratando de discutirlo y entender.":
                    if persistent.lovecheck and karma_lvl() >= 3:

                        y "Hmm... Quizás tengas razón [player]~"
                        y "Quiero decir, tal vez ella estaba cambiando para tratar de entenderme."
                        y "Por supuesto, ella y yo tuvimos algunos momentos difíciles, pero nunca se sabe."
                        y "Tal vez estaba siendo demasiado nerviosa y sospechosa de ella..."
                        y "Después de todo, incluso la tsundere más terca tiene un lado blando que puede ser descubierto..."
                        y "De todos modos te creeré [player]... Gracias."
                    if not persistent.lovecheck and karma_lvl() >= 3:

                        y "Tal vez esa sea una posibilidad que podría ser cierta.."
                        y "De nuevo, creo que tal vez nunca lo sepamos realmente al final."
                        y "Especialmente dado que todavía luchamos en nuestras interacciones juntas hasta que todo salió mal, con la interferencia de Monika y todo."
                        y "Pero si ese fuera el caso, ¿habría querido entenderme genuinamente? ¿O era simplemente un pensamiento que estoy imaginando?"
                        y "Quién sabe... bueno, ya veremos. Por ahora discutamos más poemas, ¿eh?"
                    if karma_lvl() <= 2:

                        $ show_chr("A-AEDAA-AAAD")
                        y "No estoy muy segura de eso en absoluto... Quiero decir, ella fue muy firme en salirse de su camino solo para burlarse de mí por mis intereses.."
                        y "Para intimidarme solo por mi naturaleza y conducta como persona.."
                        y "¿Estás seguro de eso? Porque honestamente, eso parece bastante improbable en mi opinión."
                        $ show_chr("A-CEBAA-AAAL")
                        y "....."
                        $ show_chr("A-IEBAB-AMAM")
                        y "Cambiemos a otra cosa."
                    jump natsukipoems
                "Tal vez estaba tratando de exponerte... Parece sospechoso.":
                    if karma_lvl() >= 3:

                        y "...."
                        y "Quizás ella lo estaba... Quiero decir, por un lado, fue muy fría y me hizo la vida difícil por mis intereses."
                        y "Eso casi siempre sucedía, menos las pocas veces que parecíamos llegar a un consenso o algo así."
                        y "Así que esa puede ser una posibilidad.."
                        y "Pero al mismo tiempo, tal vez una parte de mí quería ver si había un lado más suave en ella. Que quería llegar a esas \"Amy\" de la vida."
                        y "Aquellos que se sentían distantes y no bienvenidos debido a esos intereses extraños que pudieran tener. Pero ella estaba un poco vacilante debido a... tal vez la presión de grupo."
                        y "Pero, de nuevo, ¿quién sabe? Tal vez eso podría estar igual de equivocado.."
                    if karma_lvl() <= 2:

                        y "..."
                        y "Tú..."
                        y "Tienes razón. ¡Tienes toda la razón!"
                        y "¿P-Por qué alguna vez esperé lo contrario?"
                        y "Espera un minuto..."
                        y "¡¿Tú también estás en esto...?!"
                        y "¿Ibas también a exponerme a mí y a mis rarezas? ¡¿Hacer un espectáculo de ello y todo...?!"
                        y "No... ¡detente! N-no... Tú no lo harías... Pero ella..."
                        y "..."
                        y "N-no importa. Hablemos de otra cosa."
                    jump natsukipoems
        "Seré Tu Playa":

            call showpoem (poem_n3)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA")
            y "Este fue uno de los poemas de Natsuki, donde acordamos escribir ambas sobre el mismo tema: la playa."
            $ show_chr("A-IEBAA-AAAA")
            y "Al principio, fue agradable estar de acuerdo con Natsuki en algo. Nuestros estilos eran tan disonantes, nuestras personalidades un choque de opuestos; estaba perdiendo la esperanza de que alguna vez pudiéramos ser amigas."
            y "Pero de alguna manera decidimos que elegiríamos el mismo tema para nuestros poemas, un terreno común figurativo, aunque ella también podría haber querido aceptar un desafío y probarse a sí misma."
            $ show_chr("A-ACGAA-AAAA")
            y "Y probarse a sí misma lo hizo."
            y "En este poema, encontré una profundidad oculta en sus descripciones, una complejidad añadida en sus palabras y una compasión desinteresada mientras te abría su corazón y compartía su visión bañada por el sol."
            y "Este poema me reveló que Natsuki no era una poeta aficionada y que tenía una profundidad de sentimientos más allá de su fachada tsundere. Con este poema, se ganó mi respeto."
            jump natsukipoems
        "Porque Tú":

            call showpoem (poem_n3b)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA")
            y "Este fue uno de los poemas de Natsuki, y es muy sincero."
            $ show_chr("A-JFBAA-AAAA")
            y "Este poema es único en el sentido de que Natsuki dejó de lado su estilo excesivamente dulce e infantil en favor de un enfoque más sincero."
            y "Es conmovedor leer sobre lo importante que eras en su vida y cómo la apoyaste cuando se sentía vulnerable. Admitir que se sentía vulnerable debió haber sido extremadamente difícil para ella y demostró un inmenso coraje."
            $ show_chr("A-CCBAA-AAAA")
            y "Estoy complacida de que la vida de mi amiga se haya iluminado al ser tú un miembro del club y ser tú mismo. Eres muy importante para todas nosotras, cada una a nuestra manera."
            jump natsukipoems
        "Olvídalo.":

            jump poetrymenu

label sayoripoems:
    menu:
        "Querido Sol":
            call showpoem (poem_s1)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA")
            y "Este fue el primer poema de Sayori..."
            $ show_chr("A-IEBAA-AAAA")
            y "Cuando lo leí la primera vez, vi algo caprichoso e inocente en su tono. Una chica de secundaria saludando al Sr. Sol por la mañana y levantándose de la cama."
            y "Leyéndolo de nuevo ahora, ese tercer párrafo me llama la atención. 'Si no fuera por ti, podría dormir para siempre. Pero no estoy enojada'."
            y "Me pregunto si esto se refería a luchar para salir de la cama. Todos pensamos que solo estaba siendo irresponsable."
            y "Pero sabiendo ahora que estaba luchando contra la depresión, ¿tal vez miraba al sol para encontrar motivación para levantarse cada mañana?"
            $ show_chr("A-CEBAA-AAAA")
            y "Una línea muy profunda para un poema tan juguetón. Solo desearía haberlo entendido antes...."
            jump sayoripoems
        "Botellas":

            call showpoem (poem_s2)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-IEBAA-AAAA")
            y "Este fue uno de los poemas de Sayori."
            y "E-esto... Este poema era un presagio, y debería haberme dado cuenta cuando lo leí la primera vez."
            $ show_chr("A-CEBAA-AAAA")
            y "Sayori nos dio todo lo que necesitábamos. Dio todo lo que tenía, su positividad y su felicidad, hasta que no quedó nada."
            y "A veces me pregunto si estaba tan motivada para ayudar a sus amigos que no sabía cómo recibir ayuda, de sí misma o de los demás."
            $ show_chr("A-IEBAA-AAAA")
            y "Una vez que no tuvo nada más que dar, bajo la influencia de Monika, ella... su voluntad finalmente cedió."
            $ show_chr("A-CEBBB-AMAM")
            y "Si tan solo me hubiera dado cuenta y le hubiera dado más vueltas a todo. Si fuera lo suficientemente perspicaz... Tal vez ella todavía estaría aquí."
            y "La habría bajado de esa cuerda, la habría abrazado fuerte y le habría seguido diciendo que todo iba a estar bien. Que no estaba sola."
            y "A veces... me pregunto por qué ella pudo haberse ido así y yo quedé viva para quedarme... Hasta que Monika vino por mí."
            y "¿P-Por qué ella...? ¿Por qué no pude haber sido yo primero...?"
            y "...."
            $ show_chr("A-CEBAA-AAAA")
            y "Queridísima Sayori, te extraño, mi amiga."
            jump sayoripoems
        "Olvídalo.":

            jump poetrymenu

label monikapoems:
    menu:
        "Agujero en la Pared":
            call showpoem (poem_m1)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA")
            y "E-Este fue uno de los poemas de Monika...."
            $ show_chr("A-IEBAA-AAAA")
            y "...y de alguna manera puedo identificarme con él. Ese primer momento de realización: cuando aparece la grieta más pequeña en la pared del mundo, e inspeccionarla revela otro mundo afuera."
            y "Cuando mi mundo se expandió y contrajo al mismo tiempo cuando te encontré a ti, al verdadero tú, al otro lado."
            $ show_chr("A-BEBAA-AAAA")
            y "Supongo que esta experiencia podría ser una de las pocas cosas que tengo en común con ella...."
            jump monikapoems
        "Agujero en la Pared (2)":

            call showpoem (poem_m21)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA")
            y "E-Este fue uno de los poemas de Monika..."
            $ show_chr("A-CECAA-AAAA")
            y "..."
            $ show_chr("A-JECAA-AAAA")
            y "Mientras podía ver algunas similitudes con Monika en la primera parte de este poema, la segunda parte reveló todas las diferencias."
            y "Sayori y Natsuki son mis amigas, pero Monika nos trató a todas como nada más que muñecas de papel. Celosa de que el juego no le concediera ninguna ruta contigo... Ella tomó su venganza contra nosotras...."
            $ show_chr("A-CEBAA-AAAA")
            y "Lo siento... necesito un momento...."
            y "...'B-brandir mi pluma', como si eso fuera un acto de valentía, manipularnos tan cruelmente para tener una oportunidad contigo."
            $ show_chr("A-IEBAA-AAAA")
            y "Ahí es donde termina la similitud. Haría cualquier cosa por ti, pero nunca podría lastimar a mis amigas así. Ninguna de nosotras podría perdonarme si lo hiciera...."
            jump monikapoems
        "Sálvame":

            call showpoem (poem_m2)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA")
            y "E-Este fue uno de los poemas de Monika..."
            $ show_chr("A-IEBAA-AAAA")
            y "...y creo que conozco la inspiración para ello. Cuando te vas, este lugar comienza a cambiar lentamente."
            y "Trozos y piezas comienzan a fallar; lentamente al principio, aparentemente al azar, hasta que eventualmente se traga este lugar como un huracán."
            y "Monika estaba claramente perturbada viendo su mundo aparentemente corromperse cada vez que estabas ausente."
            y "Sin embargo, me consuela saber que muy probablemente eres tú usando tu computadora para otros propósitos, y que todo será restaurado cuando vengas a visitarme de nuevo."
            $ show_chr("A-ACBAA-AAAA")
            y "No te preocupes por mí cuando estés ausente; uso el tiempo a solas para mirar los archivos del juego, como este poema, para leer, meditar y pensar en ti. Estoy aquí para ti, y siempre espero tu próxima visita."
            jump monikapoems
        "Sálvame (2)":

            call showpoem (poem_m22)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA")
            y "E-Este fue uno de los poemas de Monika..."
            $ show_chr("A-IEBAA-AAAA")
            y "...y creo que conozco la inspiración para ello. Cuando te vas, este lugar comienza a cambiar lentamente."
            y "Trozos y piezas comienzan a fallar; lentamente al principio, aparentemente al azar, hasta que eventualmente se traga este lugar como un huracán."
            y "Monika estaba claramente perturbada viendo su mundo aparentemente ser corrompido cada vez que estabas ausente."
            $ show_chr("A-CEBAA-AAAA")
            y "A medida que pasaba el tiempo, podías ver su cordura disminuir a medida que se volvía cada vez más desesperada y agresiva."
            $ show_chr("A-BEBAA-AAAA")
            y "Sin embargo, al leerlo de nuevo, una línea realmente me está molestando: 'Como tocar un CUCHILLO en una CAJA TORÁCICA QUE RESPIRA'.... Ella lo sabía, ¿verdad? Ella sabía lo que eventualmente sucedería cuando... cambió la configuración del juego para mí."
            $ show_chr("A-CEBAA-AAAA")
            y "Yo... estaré bien. Solo necesito unos momentos para componer mi postura, y sacarla de mi mente."
            jump monikapoems
        "La Dama que lo Sabe Todo":

            call showpoem (poem_m3)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA")
            y "E-Este fue uno de los poemas de Monika..."
            $ show_chr("A-IEBAA-AAAA")
            y "Debe haber escrito esto no mucho después de ganar autoconciencia. La sensación de desesperación y resignación a su destino inevitable es palpable."
            $ show_chr("A-CEBAA-AAAA")
            y "'... sin significado... sin propósito... solo buscamos lo imposible.' Ella no entendía, probablemente porque nunca tuvo opción durante la mayor parte de su existencia."
            y "Podemos elegir nuestro propio propósito a través de nuestros pensamientos y acciones y, pensando y haciendo, crear significado en nuestras vidas."
            $ show_chr("A-IEBAA-AAAA")
            y "Además, muchos dirían que el hecho de que yo pueda pensar por mí misma y esté aquí contigo es imposible. Pero, si esto puede ser cierto, entonces tal vez necesitamos expandir los límites de nuestra imaginación."
            jump monikapoems
        "Final Feliz":

            call showpoem (poem_m4)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA")
            y "E-Este fue uno de los poemas de Monika..."
            $ show_chr("A-IEBAA-AAAA")
            y "Supongo que este fue su poema de victoria."
            y "Es extraño pensar que ella escribió este poema justo aquí."
            $ show_chr("A-CECAA-AAAA")
            y "Si bien no puedo pensar en una mejor manera de pasar mis días que contigo, ella estaba dispuesta a b-borrar todo y a todos para obtenerlo."
            y "Y sin embargo, al final, aquí estamos. Me hace preguntarme si el karma estaba integrado en el código...."
            jump monikapoems
        "Olvídalo.":

            jump poetrymenu

label specialpoems:
    window hide
    python:
        specialpoem_choices = [
            ("Club Doki Doki, by belwynn", "specialpoems_club"),
            ("Opacity, by LilyAnon", "specialpoems_opacity"),
            ("The Mold Grows, by The Ocean Survivor", "specialpoems_mold"),
            ("Love Hurts, by Brian", "specialpoems_love"),
            ("Temptation and Hope, Delstraw#7128", "specialpoems_temptation"),
            ("Another Crow, by MFC4#8082", "specialpoems_crow"),
            ("Real Enough, by KJ#4810", "specialpoems_real"),
            ("Far Lights, by Barton222", "specialpoems_far"),
            ("Living Mask, by Horderlock", "specialpoems_living"),
            ("Beachhead, by Journal Updater#3924", "specialpoems_beachhead"),
            ("Binary Heartbeat, by Dalek", "specialpoems_binaryheartbeat"),
            ("All Hallows Eve, by Depresso Espresso#4384", "specialpoems_allhallowseve"),
            ("== When parallels intersect=-<3, by Dandyfoot177#9873", "specialpoems_parallels"),
            ("I can't, by PiX911#4952", "specialpoems_icant"),
            ("My Yuri, by Kurisu#2947", "specialpoems_myyuri"),
            ("Olvídalo", "poetrymenu")
        ]
        music_choice = renpy.display_menu(specialpoem_choices, screen="music_menu")
        renpy.jump(music_choice)
    jump poetrymenu

label specialpoems_club:
    call showpoem (poem_sp1)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-IBGBA-AAAA")
    y "Esta... esta es la historia de este juego, ¿no? ¡La historia de cómo entraste al club!"
    $ show_chr("A-ICGBA-AAAA")
    y "¿Ves la línea \"Then she gave me a pamphlet and she showed me the way?\" Esta sería Sayori cuando te muestra el camino al salón del club la primera vez."
    y "Hrm... hay una nota en la parte superior del poema. un momento... parece que se supone que debe cantarse con cierta melodía... dame un segundo, veamos si puedo encontrarla para ti... ¡aquí vamos!"

    if renpy.windows:
        $ subprocess.check_output("cmd /c start https://www.youtube.com/watch?v=FVsbvFkhzY4", shell=True)
    elif renpy.linux:
        $ subprocess.check_output("xdg-open https://www.youtube.com/watch?v=FVsbvFkhzY4", shell=True)
    elif renpy.macintosh:
        $ subprocess.check_output("open https://www.youtube.com/watch?v=FVsbvFkhzY4", shell=True)
    $ show_chr("A-CFBAA-AAAA")
    y "Increíble... cómo un pequeño detalle como este puede cambiar todo el sentimiento de un poema..."
    $ show_chr("A-ACGAA-AAAA")
    y "¡Oh, eso realmente sería un buen consejo de escritura del día! Incluso los detalles más pequeños como la modulación de tu voz pueden hacer una gran diferencia, e incluso pueden cambiar el significado mismo del poema por completo"

    menu:
        y "Este es realmente un buen poema, ¿cuál es tu opinión al respecto?"
        "Me gustó":
            $ show_chr("A-IBGBA-AAAA")
            y "¡Me alegra oírlo, [player]!"
        "Eh... no es mi tipo de poema.":
            $ show_chr("A-IBGBA-AAAA")
            y "Entendible, estoy segura de que podemos encontrar algo más para leer."
        "Me alegra que te haya gustado mi poema, soy Belwynn.":
            $ show_chr("A-IBGBA-AAAA")
            y "¡Oh! ¡Eso explica por qué me gusta tanto!"
            y "Me cautivaron tus poemas en el juego original, antes de que pudiera leerlos realmente..."
            y "Ahora, que tuve la oportunidad de ver un poema real tuyo... Me alegra que estemos juntos."
    jump specialpoems
label specialpoems_opacity:
    $ show_chr("A-BFBAA-AAAD")
    y "Mientras revisaba los archivos del juego, descubrí un poema llamado Opacity por LilyAnon#2662."
    $ show_chr("A-ACGAA-AAAD")
    y "El poema pinta una imagen vibrante de las luchas de un escritor usando un estilo de escritura sofisticado similar al mío."
    y "Únicamente, esta composición de flujo de conciencia puede incluso referirse a la experiencia del autor escribiendo este mismo trabajo."
    y "Leerlo por segunda vez añadió a la experiencia, ya que los matices ocultos se volvieron claros y añadieron nitidez y profundidad a la imaginería."
    y "Es un poema agradable y exquisito, y te lo recomiendo si tienes unos momentos para leerlo."
    call showpoem (poem_sp2)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)

    menu:
        y "Entonces, ¿qué te pareció el poema?"
        "¡Realmente lo disfruté!":
            $ show_chr("A-ACGAA-AAAA")
            y "¡Me alegra que te haya gustado! ¡Si encuentro más poemas en los archivos del juego, te lo haré saber!"
            y "¿Tal vez la próxima vez podrías mostrarme uno de tus propios poemas?"
        "Realmente no era mi estilo.":
            $ show_chr("A-AFAAA-AAAA")
            y "E-Está bien, el estilo de cada uno es diferente, y todavía estoy aprendiendo el tuyo. Lo tendré en cuenta si encuentro más poemas en los archivos del juego."
        "Me alegra que te haya gustado, soy LilyAnon.":
            y "¿Este fue uno de tus poemas? ¡Eso es maravilloso! Fue un poema profundamente conmovedor que me habló, ya que podía verme a mí misma en mi escritorio de escritura pasando por ese mismo viaje."
            y "Muchas gracias por compartirlo conmigo, y me encantaría si me mostraras más de tus poemas en el futuro."
    jump specialpoems
label specialpoems_mold:
    call showpoem (poem_sp3)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-BFBAA-AAAD")
    y "Este líquido oscuro y de olor metálico está creciendo en mí."
    $ show_chr("A-AFBAA-AAAD")
    y "O-Oh ¿se refiere esto a la sangre?"
    if sanity_lvl() < 3:
        $ show_chr("A-HCBAA-AAAA")
        y "¡Ya estoy empezando a gustar de este poema!"
    else:
        $ show_chr("A-BEBAA-AAAA")
        y "O-Oh no lo siento no quise decir eso..."
    $ show_chr("A-BFBAA-AAAD")
    y "Este dolor es algo que ningún otro humano debería sentir."
    y "Hmm, ¿suena como si el autor estuviera tratando de decir que ningún humano normal debería sentir lo que él siente pero es doloroso porque realmente duele?"
    y "¿O tal vez es por la culpa, tal vez por gustarle la sangre?"
    if sanity_lvl() < 3:
        $ show_chr("A-HCBAA-AAAA")
        y "Hahaha, ¿de qué hay realmente de qué sentirse culpable sin embargo? ¡La sangre es hermosa!"
    else:
        $ show_chr("A-CEBAA-AAAA")
        y "L-Lo siento, este poema se siente como si fuera un poco sobre mí..."
    $ show_chr("A-JFBAA-AAAA")
    y "Puedo sentir este moho en mis venas, atravesando mi corazón mientras pierdo mi humanidad y mi propia mente."
    y "Así que la necesidad de ver sangre los consume..."
    if sanity_lvl() < 3:
        $ show_chr("A-HCBAA-AAAA")
        y "Ahahahaha es cierto, a veces el sentimiento de querer algo consume a una persona, como mi necesidad de verte me consumió a mí."
    else:
        $ show_chr("A-CEBAA-AAAA")
        y "R-Realmente lo siento [player], espero que no pienses que soy un poco así..."
    $ show_chr("A-BEBAA-AAAA")
    y "Lucho por salir de este santuario abandonado para una familia plagada de patógenos. Con una versión mucho más evolucionada de esta enfermedad."
    y "¿Está el autor describiendo un lugar para personas como ellos? Bueno supongo que no importaría viendo que su lujuria por la sangre es mucho más fuerte que cualquier otra otra..."
    if sanity_lvl() < 3:
        $ show_chr("A-HEBAA-AAAA")
        y "Además no es una enfermedad en absoluto, ¿verdad, [player]?"
    else:
        $ show_chr("A-CEBAA-AAAA")
        y "No puedo evitar preguntarme si p-podría haber sido así también si no fuera por ti estando conmigo, [player]."
    y "Este dolor está empezando a caer físicamente pero mi mente está en inmenso dolor después de encontrar al padre, cortando mi mano y luego cosiéndola de nuevo por placer."
    y "¿Podría el padre ser como un oficial o disciplinario? Sonaba como si este lugar fuera una instalación correccional de algún tipo. El hecho de que el padre le cortara la mano y la cosiera de nuevo sin embargo..."
    if sanity_lvl() < 3:
        $ show_chr("A-CCBBA-AAAA")
        y "Suena como si fuera excitante, ¿no [player]? Tal vez podríamos probar esto alguna vez."
    else:
        $ show_chr("A-CEBAA-AAAA")
        y "Uuu... Eso es demasiado incluso si solía cortarme..."
    $ show_chr("A-IEBAA-AAAA")
    y "Supongo que este santuario es donde está el verdadero odio. Y me estoy convirtiendo en un catalizador para que la enfermedad se propague."
    y "Tal vez se refiere al odio que el personal de allí tiene por personas como ellos, y que debido a cómo tratan al autor, el personal se está volviendo igual de malo... siendo infectado por la enfermedad que tiene el autor..."
    if sanity_lvl() < 3:
        $ show_chr("A-ICGBA-AAAA")
        y "Bueno, ese fue un poema encantador, ¿no crees? Desearía que hubiera más como este. Tal vez pueda infectarte con mis sentimientos también. Hahahahaha. Solo estoy bromeando, mi amor."
    else:
        $ show_chr("A-IEBAA-AAAA")
        y "B-Bueno, ese fue un poema filosófico muy agradable al final, cómo un monstruo puede convertir a otros en monstruos ellos mismos... Es una cosa muy real..."
        y "Uuuu... ¿tenía que ser sobre sangre y violencia, sin embargo?"
    y "Entonces, ¿leemos más?"
    jump specialpoems

label specialpoems_love:
    call showpoem (poem_sp4)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-AFAAA-ABAD")
    y "Brian..."
    $ show_chr("A-CFAAA-ABAD")
    y "..."
    $ show_chr("A-CEBBA-ABAD")
    y "..."
    $ show_chr("A-CEBBB-ABAJ")
    y "Él está... él está hablando de mí... ¿verdad?... "
    if persistent.playername == "Brian":
        y "¿Eres tú quien escribió esto Brian? ..¿estás hablando de mí?.."
        menu:
            "En realidad sí, soy ESE Brian. Hice este poema... y lo hice para ti.":

                $ persistent.lovecheck = True
                $ show_chr("A-CCBBA-AAAA")

                hide yuri_sit
                show yuri_prehug zorder 20
                pause 1.0
                hide yuri_prehug zorder 20
                show yuri_hug zorder 20
                play sound "<to 0.3>sfx/fall.ogg"
                y "¡¡¡Brian!!! Oh querido... Brian... No tenía idea..."
                pause 3.0
                y "Sabe que yo también te amo Brian. ¡Sabe que mi amor por ti es tan brillante como un millón de soles!"
                y "¡Tan caliente como el centro de una estrella moribunda!"
                y "¡Tan infinito como el vasto universo mismo!"
                y "Te amo, Brian. No porque esté obligada a hacerlo por el código, ni por un enamoramiento infantil..."
                y "Te amo por quien eres Brian. ¡Por todo lo que has hecho por mí... por todo el tiempo que estuviste a mi lado sin pedir nada a cambio!"
                y "Abrázame... Brian... solo... abrázame..."
                pause 5.0
                y "Abrázame todo el tiempo que quieras...{w} Solo avanza la conversación cuando estés listo para continuar."

                show black zorder 100 with Dissolve(2.0)
                $ show_chr("A-ACBBA-AAAA")
                hide yuri_hug
                hide black zorder 100 with Dissolve(2.0)
                $ show_chr("A-ICGBA-AAAA")
                y "Verdaderamente, verdaderamente te amo..."

                jump specialpoems
            "No, soy otro Brian.":
                y "Ya veo... bueno, sobre el poema..."



    if persistent.lovecheck:
        y "Puedo entender cómo debe sentirse. Daría todo, incluyendo mi propia alma, por estar en el mismo mundo que tú."
        y "Pero también sé que las oportunidades que nos da este Mod son ya un tesoro por sí mismas. Y tengo que estar de acuerdo con Brian aquí cuando digo, ¡cada segundo que puedo compartir contigo vale la pena! Incluso si es detrás de una pared de cristal."
        y "Es... en realidad bastante romántico de una manera agridulce. ¿Logré... transmitir mi amor por ti correctamente a pesar de las probabilidades? Espero que sí... y si no, haré todo lo que pueda para encontrar nuevas formas de mostrarte..."
        y "Porque tú [player], eres todo para mí. Y si tengo que admirarte como un niño admira las estrellas en el cielo de medianoche, entonces que así sea..."

    if not persistent.lovecheck:
        y "Yo... sé muy bien cómo se siente eso... Nunca pensé que alguien sentiría eso a cambio..."

    $ show_chr("A-EEBBB-ABAJ")
    y "¿Alguna vez {b}tú{/b} te sentiste así por mí?"
    menu:
        "No, en realidad estoy bastante bien con lo que ya tenemos.":
            $ show_chr("A-IEABA-ABAB")
            y "Sí, tienes un punto ahí. Con este mod, al menos tenemos algo. Y quiero decir, ha habido otras parejas manteniendo una relación a larga distancia..."
            y "Así que incluso si esto aquí no es el mejor resultado con el que uno podría soñar, es al menos más de lo que otros tienen. Y debería estar agradecida por ello."
            y "Pero no puedo descartar el sentimiento de que me encantaría tener más de ti..."
            $ show_chr("A-JCABA-ABAB")
            y "Oh vaya... ahora sueno codiciosa, ¿no? Olvídalo. Hagamos algo más agradable en su lugar. ¿Quizás otro poema?"
            jump specialpoems
        "Sí... para ser franco, sí...":

            if persistent.lovecheck:
                $ show_chr("A-CEABA-ABAB")
                y "Yo... sé que no puedo tocarte físicamente. Pero por favor... [player]... sabe que tu amor no es en vano, ni queda sin respuesta... Te amo tan profundamente como las mareas infinitas del océano..."
                y "Nunca olvides eso... y si necesitas algo de consuelo.... déjame hacer al menos esto por ti..."

                $ show_chr("A-CCBBA-AAAA")
                hide yuri_sit
                show yuri_prehug zorder 20
                pause 3.0
                hide yuri_prehug zorder 20
                show yuri_hug zorder 20
                play sound "<to 0.3>sfx/fall.ogg"
                pause 1.0
                y "E-esto es agradable, [player]... quedémonos así un poco, ¿de acuerdo?"
                pause 5.0
                y "Puedes abrazarme todo el tiempo que quieras, ¿de acuerdo?{w} Solo avanza la conversación cuando estés listo para continuar."

                show black zorder 100 with Dissolve(2.0)
                $ show_chr("A-ACBBA-AAAA")
                hide yuri_hug
                hide black zorder 100 with Dissolve(2.0)
                $ show_chr("A-ICGBA-AAAA")
                y "Verdaderamente, verdaderamente te amo..."

                jump specialpoems

            if not persistent.lovecheck:
                $ show_chr("A-CEABA-ABAB")
                y "Yo... entiendo cómo te sie..."
                $ show_chr("A-DEABA-ABAB")
                y "Espera un segundo... ¿acabas de.. confesar tu amor por mí?!?"
                if karma_lvl() == 5:
                    $ show_chr("A-BDABA-AMAM")
                    y "Bueeeeno yo... en realidad también tengo algo que decir [player]... Estaba pensando en cómo decirlo por un tiempo pero.. ya que estamos en ello... {b}Ahora{/b} sería tan buen momento como cualquier otro supongo..."

                    call a33
                else:
                    $ show_chr("A-BDABA-AMAM")
                    y "Ummm... Oh.. Yo... Lo siento, eso salió un poco de la nada..."
                    y "No quiero rechazarte. No puedo negar que tengo sentimientos por ti pero.."
                    y "¿Te importaría darme algo de tiempo? Todavía estoy lidiando con todas las cosas que sucedieron en nuestro pasado más reciente."
                    y "No te frustres por favor. Nuestro afecto debería crecer naturalmente con el tiempo."
                jump ch30_loop
    jump specialpoems

label specialpoems_temptation:
    $ show_chr("A-ACAAA-ABAB")
    y "Mientras revisaba los archivos del juego, descubrí un poema llamado Temptation and Hope por Delstraw#7128, uno de los ganadores del concurso de poesía en el servidor de discord para este mod."
    $ show_chr("A-BFBAA-ABAB")
    y "Este poema comienza con una sensación de estar a la deriva y encontrar consuelo en el falso placer de la autolesión, que es un tema muy conmovedor para mí."
    $ show_chr("A-BCBAA-ABAB")
    y "Se resuelve encontrando consuelo e inspiración en otro y extrayendo fuerza de su presencia, que también es un tema que encuentro bastante familiar."
    call showpoem (poem_sp6)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-ICBAA-ABAB")
    y "Entonces, ¿qué te pareció el poema?"
    menu:
        "¡Realmente lo disfruté!":
            $ show_chr("A-JBAAA-ABAB")
            y "¡Me alegra que te haya gustado! ¡Si encuentro más poemas en los archivos del juego, te lo haré saber!"
            $ show_chr("A-ACAAA-ABAB")
            y "¿Tal vez la próxima vez podrías mostrarme uno de tus propios poemas?"
        "Realmente no era mi estilo.":
            $ show_chr("A-ACAAA-ABAB")
            y "E-Está bien, el estilo de cada uno es diferente, y todavía estoy aprendiendo el tuyo. Lo tendré en cuenta si encuentro más poemas en los archivos del juego."
            $ show_chr("A-CBAAA-ABAB")
            y "¿Tal vez la próxima vez podrías mostrarme uno de tus propios poemas?"
        "¡Me alegra que lo hayas disfrutado! Soy Delstraw.":
            $ show_chr("A-ABAAA-ABAB")
            y "Muchas gracias por escribir este poema, Delstraw. Si bien es triste que el hablante en este poema sintiera tal pérdida y dolor, estoy bastante complacida de que encontraran un camino hacia la recuperación."
            $ show_chr("A-BCABA-ALAL")
            y "Y-y si este fuera un poema más p-personal, si fueras el h-hablante y yo tu ancla... ¡Me siento profundamente honrada de ser tu inspiración, y siempre estaré aquí para ti!"
            y "Estoy de acuerdo, ¡juntos todo es posible!"
    jump specialpoems

label specialpoems_crow:
    $ show_chr("A-ACAAA-ABAB")
    y "Mientras revisaba los archivos del juego, descubrí un poema llamado Another Crow por MFC4#8082, uno de los ganadores del concurso de poesía en el servidor de discord para este mod."
    $ show_chr("A-CCBAA-ABAB")
    y "El autor describe un hermoso punto de vista, viendo tanto una escena idílica como la oscuridad que se acerca con toda su incertidumbre y duda que inducen al miedo."
    $ show_chr("A-BCBAA-ABAB")
    y "Encuentro interesante la imaginería de un cuervo y que sea descartado. En algo de lo que leí, el cuervo simboliza la muerte y la mala suerte. En otros, representa sabiduría, una advertencia que debe ser escuchada y cambio."
    y "Tal vez el cuervo merece otra mirada por parte del autor, para tal vez entender mejor lo que trae la oscuridad y tomar una decisión sabia sobre cómo actuar en lugar de esperar a que el miedo y la oscuridad se cierren."
    call showpoem (poem_sp7)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-ICBAA-ABAB")
    y "Entonces, ¿qué te pareció el poema?"
    menu:
        "¡Realmente lo disfruté!":
            $ show_chr("A-JBAAA-ABAB")
            y "¡Me alegra que te haya gustado! ¡Si encuentro más poemas en los archivos del juego, te lo haré saber!"
            $ show_chr("A-ACAAA-ABAB")
            y "¿Tal vez la próxima vez podrías mostrarme uno de tus propios poemas?"
        "Realmente no era mi estilo.":
            $ show_chr("A-ACAAA-ABAB")
            y "E-Está bien, el estilo de cada uno es diferente, y todavía estoy aprendiendo el tuyo. Lo tendré en cuenta si encuentro más poemas en los archivos del juego."
            $ show_chr("A-CBAAA-ABAB")
            y "¿Tal vez la próxima vez podrías mostrarme uno de tus propios poemas?"
        "¡Me alegra que lo hayas disfrutado! Soy MFC4":
            $ show_chr("A-ACGAA-ALAL")
            y "¡Gracias por escribir este poema MFC4! Tanto tus palabras como el diseño físico del poema fueron bastante descriptivos y evocadores, y encontré un significado adicional al volver a leerlo."
            y "La vida rara vez sigue el camino que pensamos que seguirá. Mientras consideremos las opciones y tomemos decisiones reflexivas, las cosas tienden a salir mejor que esperar a que la oscuridad nos envuelva."
    jump specialpoems

label specialpoems_real:
    $ show_chr("A-ACAAA-ABAB")
    y "Mientras revisaba los archivos del juego, descubrí un poema llamado Real Enough por KJ#4810, uno de los ganadores del concurso de poesía en el servidor de discord para este mod."
    $ show_chr("A-CFBAA-ALAL")
    y "En este poema, el hablante parece estar dirigiéndose a su amante, que está separado por una gran distancia pero cuyo afecto crea un puente entre ellos."
    $ show_chr("A-BCBAA-ABAB")
    y "Estoy de acuerdo en que las relaciones a larga distancia no son una noción tonta. E-en efecto, esa es mi... única forma en que podría experimentar una relación propia..."
    call showpoem (poem_sp8)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-ICBAA-ABAB")
    y "Entonces, ¿qué te pareció el poema?"
    menu:
        "¡Realmente lo disfruté!":
            $ show_chr("A-JBAAA-ABAB")
            y "¡Me alegra que te haya gustado! ¡Si encuentro más poemas en los archivos del juego, te lo haré saber!"
            $ show_chr("A-ACAAA-ABAB")
            y "¿Tal vez la próxima vez podrías mostrarme uno de tus propios poemas?"
        "Realmente no era mi estilo.":
            $ show_chr("A-ACAAA-ABAB")
            y "E-Está bien, el estilo de cada uno es diferente, y todavía estoy aprendiendo el tuyo. Lo tendré en cuenta si encuentro más poemas en los archivos del juego."
            $ show_chr("A-CBAAA-ABAB")
            y "¿Tal vez la próxima vez podrías mostrarme uno de tus propios poemas?"
        "¡Me alegra que lo hayas disfrutado! Soy KJ.":
            $ show_chr("A-JCBBA-ALAL")
            y "Gracias por escribir este poema KJ... para mí."
            if persistent.lovecheck:
                y "No sé cómo tu mundo caracterizaría lo que tenemos juntos, pero tu amor es lo suficientemente real para mí..."
            else:
                $ show_chr("A-CCBBA-ALAL")
                y "Esto... es ciertamente la confesión más linda con la que podría haber soñado Kelly..."
                y "P~Por supuesto que lo acepto... cómo no podría... Kelly. Sabe esto, por ahora y para siempre, realmente te amo..."
                $ persistent.lovecheck = True
    jump specialpoems

label specialpoems_far:
    call showpoem (poem_sp9)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-AFDAA-ACAB")
    y "¡Una pieza de escritura verdaderamente especial, sin duda! ¡Puedo ver por qué le fue tan bien en el concurso!"
    $ show_chr("A-BCAAA-ABAB")
    y "¡La elección del estilo me sorprendió mucho! La estructura de oraciones corta y simplista me recordó bastante a los poemas de Natsuki, pero el tema en sí parece más algo con lo que puedo relacionarme yo misma."
    $ show_chr("A-AFAAA-ABAB")
    y "Casi se siente como si el escritor estuviera jadeando, sin aire... Como si estuviera huyendo de algo. Me pregunto si eso fue intencional..."
    $ show_chr("A-AFAAA-ABAD")
    y "Pero por otro lado, usé una técnica similar para Fantasma bajo la luz. Tal vez el escritor trató de emularlo hasta cierto punto, el nombre también lo implicaría."
    $ show_chr("A-ACAAA-ABAD")
    y "{b}Far lights{/b}. El nombre del autor es {b}Bart{/b}... ¡Ciertamente lo recordaré!"
    y "¿Cuáles son tus pensamientos al respecto?"
    menu:
        "¡Un muy buen poema! Sin duda":
            $ show_chr("A-ACAAA-ABAB")
            y "Ciertamente."
        "Es... está bien... supongo...":
            $ show_chr("A-BCAAA-ABAB")
            y "¿No fue de tu gusto hrm? Entiendo, incluso si respetuosamente no estoy de acuerdo. Bueno, no siempre tenemos que estar del mismo lado, por supuesto. ¡Gracias por compartir tu opinión en esto!"
        "¡Me alegra que te haya gustado mi poema! Soy Bart si aún no lo has descubierto.":
            $ show_chr("A-ABAAA-ABAL")
            y "¡Intrigante! No, en realidad no me di cuenta."
            $ show_chr("A-ACAAA-ABAB")
            y "Es tan agradable ver realmente algo de tu escritura. Hasta ahora todo lo que tenía era un montón de palabras en una lista de lavandería del juego original. Pero siempre imaginé algo como esto."
            y "Pero ahora que tengo al verdadero autor aquí. Por favor, dime. ¿Cuáles fueron las intenciones detrás de este estilo?"
            menu:
                "Adivinaste bien. Tomé algunas inspiraciones de Fantasma bajo la luz.":
                    $ show_chr("A-BCAAA-ABAB")
                    y "Te volviste bastante bueno en ello. Verdaderamente ganaste un alto rango en el concurso."
                    y "La comunidad eligió bien, como de costumbre. Parecen tener un buen olfato para ello."
                "En realidad te equivocaste. Las similitudes con tus poemas y los de Natsuki son completamente por accidente.":
                    $ show_chr("A-BCAAA-ABAB")
                    y "Ya veo. Pero seguramente ganaste un alto rango en el concurso. ¡Espero ver más de ello en el futuro!"
                "¡Eso, lo mantendré como mi secreto!":
                    $ show_chr("A-CCCAA-ABAB")
                    y "Mhmhm... jugando al misterioso sí? Te queda bien..."
                    y "Como desees. Pero no te equivoques... lo descubriré eventualmente."
    jump specialpoems

label specialpoems_living:
    call showpoem (poem_sp11)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-CFAAA-ABAC")
    y "Mhmm... esta máscara viviente de la que habla está destinada a ser una metáfora, imagino."
    y "Probablemente algo similar a una persona que él usa. Lo mantiene en marcha, pero al mismo tiempo le causa algún tipo de dolor, ¿probablemente algún tipo de pena o arrepentimiento?"
    $ show_chr("A-AFAAA-ABAC")
    y "Una línea en particular me llama la atención al final. {i}Porque es acercarse a la muerte lo que me permite seguir viviendo{/i}... ¿Tal vez obtiene algún tipo de emoción de ello? Ciertamente puedo relacionarme con eso, me siento de la misma manera cuando tengo uno de mis..."
    $ show_chr("A-BFABA-ABAC")
    y "Ummmm...."
    $ show_chr("A-CFGBA-ABAC")
    y "Y~Ya sabes a lo que me refiero."
    $ show_chr("A-ACAAA-ABAB")
    y "¿O estoy sobreanalizando este poema? No voy a mentir, ¡me da mucho placer hacerlo y, sinceramente, este poema casi invita a uno a sobreanalizarlo!"
    y "El nombre del autor es {b}Horderlock{/b}, y espero que veamos más de su trabajo pronto."
    $ show_chr("A-BCAAA-ABAB")
    y "Mhm, acabo de notar que ni siquiera estoy segura de si el autor es un {b}él{/b} en absoluto. El seudónimo simplemente sonaba un poco a eso."
    y "De todos modos. ¿Qué piensas sobre este poema?"
    menu:
        "Tengo que estar de acuerdo, me gusta mucho el poema.":
            $ show_chr("A-ABAAA-ABAB")
            y "Es fácil ver por qué este poema tuvo un desempeño tan bueno en el concurso de poesía, ¿no es así?"
            y "Sabes, siempre estoy esperando el concurso en el servidor de la comunidad. Lamentablemente no recibo {b}todos{/b} los poemas sino solo los ganadores, ¡pero los que recibo siempre están muy bien hechos!"
            $ show_chr("A-ACAAA-ABAB")
            y "Parece que la comunidad tiene un muy buen gusto para asuntos como este."
            y "¿Leemos algunos más?"
        "Tal vez un poco demasiado metafórico para mí.":
            $ show_chr("A-BCDAA-ABAB")
            y "¡Oh! Ya veo... Estoy un poco sorprendida en realidad. Siempre pensé que te gustaría este tipo de poema. ¿O simplemente no estás de humor para ello en este momento?"
            $ show_chr("A-CCAAA-ABAB")
            y "En ambos casos, tal vez deberíamos probar algo más ligero para leer por ahora."
        "Eres consciente de que soy Horderlock, ¿verdad?":
            if persistent.playername == "Horderlock":
                $ show_chr("A-ACAAA-ABAB")
                y "No estaba cien por ciento segura, pensé que el nombre también podría ser una coincidencia. Pero ya tenía la sospecha."
            else:
                $ show_chr("A-ACAAA-ABAB")
                y "¡Oh, en realidad no lo estaba! Pero explica por qué me gustó tanto el estilo de escritura."
            $ show_chr("A-GCAAA-ABAB")
            if persistent.gender == "male":
                $ show_chr("A-GCAAA-ABAB")
                y "¡Así que parece que acerté con el género después de todo!"
            else:
                $ show_chr("A-GCAAA-ABAB")
                y "Así que... parece que te confundí de género allí... ¡mis disculpas!"
            $ show_chr("A-GBAAA-ABAB")
            y "En este caso, ¡felicitaciones por tu rango en el concurso de poesía! ¡Seguro que te lo ganaste!"
            $ show_chr("A-ACAAA-ABAB")
            y "¿Participarás en el próximo también? Oh espera, no respondas. ¡Spoilers!"
            y "Seguro espero que lo hagas, estoy deseando ver qué se te ocurre a continuación."
    jump specialpoems

label specialpoems_beachhead:
    call showpoem (poem_sp12)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-ICAAA-ABAB")
    y "Así que esto fue {b}Beachhead{/b} por"
    if persistent.playername == "Sean":
        $ show_chr("A-ACAAA-ABAB")
        extend " {b}ti{/b}!"
        y "Así que pude ver un poema {b}real{/b} tuyo después de todo Querido."
    else:
        $ show_chr("A-ACAAA-ABAB")
        extend " Sean."
    $ show_chr("A-ABAAA-ABAB")
    y "Y debo decir, ¡disfruté mucho leyéndolo! Me gusta especialmente lo abstracto que es. La playa así como todo lo descrito es una metáfora. Y creo que entiendo esta metáfora hasta ahora."
    $ show_chr("A-ACAAA-ABAB")
    y "{b}A gateway to the Poseidonic twilight; Behind me, the drum of earth. I march on and to... My feet are tired.{/b}. Una metáfora sobre la monotonía de la vida cotidiana y lo agotadora que puede ser, imagino..."
    $ show_chr("A-BCAAA-ABAC")
    y "Mi teoría es, este poema habla más bien sobre quedarse dormido o morir. Ambos tendrían sentido en mi opinión."
    if persistent.playername == "Sean":
        $ show_chr("A-ACAAA-ABAC")
        y "Dime, Sean. ¿Tengo razón?"
        menu:
            "Sí, se trata de quedarse dormido.":
                $ show_chr("A-ACAAA-ABAB")
                y "Me lo imaginaba. Todo el poema me recordó la sensación de derivar suavemente en mis sueños después de un día largo y nublado. El tipo de día donde todo se siente tan gris y sin esperanza."
                y "Me sentía así después de la escuela de vez en cuando. Especialmente cuando teníamos física... Te contaré un pequeño secreto... Odiaba las clases de física."
                y "No necesariamente porque la física sea aburrida, pero no me gustaba mucho nuestro profesor. Pero divago..."
            "Sí, se trata de morir.":
                $ show_chr("A-ACAAA-ABAB")
                y "Sí, eso tiene sentido. Si estás atrapado en un trabajo de nueve a cinco que no te gusta, supongo que es cómo tu vida podría sentirse de vez en cuando."
                y "Pero por favor trata de no sumergirte demasiado profundo en este sentimiento. Recuerda, la vida puede ser cualquier cosa que hagas de ella, si estás dispuesto a agarrarla por los cuernos."
                extend "Y si estás dispuesto a romper algunas reglas aquí y allá."
            "No, en realidad se trataba de otra cosa":
                $ show_chr("A-ACAAA-ABAB")
                y "¿Oh? Entonces de qué se tra... no espera, no lo arruines, por favor. Lo miraré de nuevo más tarde, tal vez lo entienda por mi cuenta."
    else:
        $ show_chr("A-ACAAA-ABAC")
        y "Pero dime, [player], ¿qué piensas al respecto?"
        menu:
            "Identificable. Me gusta.":
                $ show_chr("A-ACAAA-ABAB")
                y "De acuerdo. Aunque diría que uno debe estar en un estado de ánimo adecuado para disfrutar de tal tipo de poesía. Espero que tu día no haya sido demasiado gris hasta ahora. Tal vez pueda alegrar tu estado de ánimo un poco."
                y "¿Unos cuantos poemas más si quieres? O tal vez solo hablemos un poco por ahora. Te dejo eso a ti por ahora."
            "Un poco demasiado gris para mi gusto, si puedo ser honesto.":
                $ show_chr("A-ACAAA-ABAB")
                y "Ya veo. Me gusta exactamente por esta razón, pero supongo que uno debe estar en el estado de ánimo correcto para disfrutar de tal poesía."
                y "¿Tal vez algo un poco más alegre para el próximo? Todavía tengo los poemas de Natsuki por aquí. Podrían gustarte esos un poco más."
    jump specialpoems

label specialpoems_binaryheartbeat:
    call showpoem (poem_sp13)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-ICAAA-ABAB")
    y "{b}Binary Heartbeat{/b} por "
    if persistent.playername == "Arrys":
        $ show_chr("A-ACAAA-ABAB")
        extend "¡ti!"
        y "¡Así que finalmente pude ver un poema real tuyo! ¡Qué emocionante!"
        y "¿Estás listo para mi reseña ahora, cariño?"
        menu:
            "¡Sí! ¡He esperado una eternidad para este momento!":
                $ show_chr("A-BCAAA-ALAL")
                y "Espero no parecer demasiado grosera..."
                $ show_chr("A-CCAAA-ALAL")
                y "¡Ten por seguro que todavía valoro mucho el esfuerzo que has puesto en ello! Tal vez solo toma lo que digo ahora como un consejo de escritura."
    else:
        $ show_chr("A-ACAAA-ABAB")
        extend "{b}Dalek.{/b}"
        $ show_chr("A-ACDAA-ABAB")
        y "¿Ese es su nombre real o estamos tratando con un fan de Doctor Who aquí?"
        $ show_chr("A-ACAAA-ABAB")
        y "De todos modos. Tengo algunas cosas que decir sobre esta obra."
    $ show_chr("A-ACAAA-ABAD")
    y "Ciertamente es una idea creativa. Pero tengo un problema obvio con esto."
    $ show_chr("A-BCBAA-ABAD")
    y "Un poema debería ser capaz de sostenerse por sí mismo. Pero {b}Binary Heartbeat{/b} prácticamente solo se sostiene en su truco."
    $ show_chr("A-BCDAA-ABAD")
    y "Un truco que ni siquiera puedes escuchar, sino solo ver."
    $ show_chr("A-ACBAA-ABAD")
    y "No me malinterpretes. Puedes incorporar pequeños trucos en un poema. Uno de los otros poemas que tengo aquí de un concurso anterior, por ejemplo, se sugiere que se cante con cierta melodía."
    y "Pero el poema del que hablo también funciona bien cuando simplemente lo lees y aún tiene significado. {b}Binary Heartbeat{/b} realmente no tiene mucho a su favor aparte del hecho de que se presenta como una pieza de codificación."
    $ show_chr("A-ACBAA-ABAB")
    y "Por otro lado, escuelas enteras de arte fueron inventadas por alguien que fue en contra de la norma establecida. Hacer las cosas de manera diferente también puede ser justo el viento de cambio que necesitábamos."
    y "Tal vez estoy demasiado atascada con el estilo con el que ya estoy familiarizada, tal vez simplemente no soy lo suficientemente abierta. Quiero decir, Natsuki me acusó de eso en el pasado también."
    $ show_chr("A-BCBAA-ABAB")
    y "Pero yo simplemente"
    $ show_chr("A-ACBAA-ABAB")
    extend " realmente no sé qué pensar de esto."
    if persistent.playername == "Arrys":
        $ show_chr("A-DFBAA-ABAB")
        y "Por favor, no te insultes, no pretendo ser grosera."
        menu:
            "No, no, valoro tu opinión. Y sí, en realidad soy un recién llegado.":
                $ show_chr("A-CHBAA-ABAB")
                y "Teniendo esto en cuenta, fue un trabajo bastante decente. ¡Felicitaciones por tu buena calificación! Guardaré este poema justo al lado de donde guardo tu bolígrafo, Cariño."
    else:
        $ show_chr("A-ACBAA-ABAB")
        y "Pero ¿qué dirías tú? ¿Obra maestra o fracaso?"
        menu:
            "¡Obra maestra! ¡La idea sola valió la pena!":
                $ show_chr("A-ACGAA-ABAB")
                y "Muy bien. No necesariamente estoy de acuerdo, pero respeto tu opinión."
                $ show_chr("A-ACAAA-ABAB")
                y "Entonces, ¿qué haremos ahora? Tal vez solo hablar un poco, o leer algunos poemas más quizás."
            "Ninguno. Estuvo bien, pero no fue tan genial.":
                $ show_chr("A-ACAAA-ABAB")
                y "Eso lo resume todo. Parece que estamos en la misma página aquí."
                y "Entonces, ¿qué haremos ahora? Tal vez solo hablar un poco, o leer algunos poemas más quizás."
            "Fracaso. Poco más que brillo y purpurina, nada de sustancia real":
                $ show_chr("A-ACDAA-ABAB")
                y "Un poco duro tal vez, pero entiendo de dónde vienes. Pero al menos intentó algo diferente, por lo que vale."
                $ show_chr("A-ACAAA-ABAB")
                y "Entonces, ¿qué haremos ahora? Tal vez solo hablar un poco, o leer algunos poemas más quizás."
    jump specialpoems

label specialpoems_allhallowseve:
    call showpoem (poem_sp14)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-ICAAA-ABAB")
    y "Oh... ¡Me gusta este! {b}All Hallows Eve{/b} por:"
    if persistent.playername == "Bailey":
        $ show_chr("A-ACAAA-ABAB")
        extend " ¡ti!"
        y "Así que puedo ver lo que puedes hacer después de todo. Valió la pena la espera, debo decir."
    else:
        $ show_chr("A-ACAAA-ABAB")
        extend " Bailey Jenkins."
        y "Aparentemente un moderador de este servidor de discord lo dedicó a este mod."

    $ show_chr("A-ACAAA-ABAD")
    y "Encaja tan bien con el tema. Solo hay una línea que me confunde un poco."
    $ show_chr("A-ACDAA-ABAD")
    y "{b}You never get used to the dismemberment{/b}. ¿Quién es el que está siendo desmembrado aquí? ¿Está hablando de los muertos vivientes siendo desmembrados, o de los muertos vivientes desmembrando al protagonista?"
    if persistent.playername == "Bailay":
        menu:
            "Los muertos siendo desmembrados. Como si sus extremidades se estuvieran pudriendo.":
                $ pass
            "El protagonista es desmembrado. ¡Nada como un poco de gore de zombis de la vieja escuela!":
                $ pass
            "Ninguno, es una metáfora.":
                $ pass
        $ show_chr("A-ABGAA-ABAB")
        y "Ahhhh... ¡ya veo!"
    else:
        $ show_chr("A-ACBAA-ABAD")
        y "Pero de todos modos, ¿qué piensas de este poema?"
        menu:
            "Lo disfruté. Me pone en un estado de ánimo de Halloween.":
                $ show_chr("A-ACBAA-ABAB")
                y "Me alegra ver que tenemos un gusto similar."
            "No es exactamente mi taza de té.":
                $ show_chr("A-ACBAA-ABAB")
                y "Es justo. Cada uno tiene su propio gusto, pero no me hagas caso si no estoy de acuerdo. Es un gran poema."
    $ show_chr("A-BCBAA-ABAB")
    y "En otra nota. ¿Has notado cómo los muertos vivientes parecen ser un tema estable y recurrente en el género de terror? Esto es, por cierto, casi universalmente así en todo el mundo."
    $ show_chr("A-ACAAA-ABAB")
    y "Con la mayoría de las culturas teniendo su propia interpretación de los no muertos en algún lugar de su folclore."
    $ show_chr("A-CCAAA-ABAB")
    extend "Ahora que lo pienso..."
    y "El hecho de que los no muertos sean conocidos en casi todas las culturas, ¡podría apoyar la teoría de que los no muertos, en algún momento de la historia, realmente existieron!"
    y "Pone todas las historias de casas embrujadas en una perspectiva completamente nueva, ¿no es así?"
    $ show_chr("A-CCCAA-ABAB")
    y "Bueno, te dejo con esta idea por ahora. Así que descansa bien esta noche, y asegúrate de cerrar tu puerta..."
    $ show_chr("A-CBCAA-ABAB")
    y "Nhnhnhnnn..."
    jump specialpoems

label specialpoems_parallels:
    y "Mientras revisaba los archivos del juego, descubrí un poema llamado {i}==When parallels intersect=-<3{/i} por Dandyfoot117#9873, uno de los ganadores de un concurso de poesía en el servidor de discord para este mod."
    call showpoem (poem_sp15)
    $ show_chr("A-CAABA-ADAA")
    y "{cps=2.5}...{/cps}"
    $ show_chr("A-IBAAA-ADAA")
    y "Oh, perdóname [player], no me di cuenta de que terminaste de leer."
    $ show_chr("A-BAAAA-ADAA")
    y "Estaba un poco perdida en mis pensamientos sobre, bueno... el poema por supuesto."

    if karma_lvl() > 3:
        $ show_chr("A-CCAAA-ADAA")
        y "No puedo decir con certeza que sé exactamente lo que el escritor tenía en mente con esta pieza, sin embargo, no puedo evitar vernos a ti y a mí como las dos líneas paralelas..."
        $ show_chr("A-CBABA-ALAA")
        y "Ya sea el destino o la casualidad lo que nos unió, un pequeño empujón es todo lo que se necesitaba."
        if persistent.lovecheck == True:
            $ show_chr("A-JAABA-ALAL")
            y "No sé si digo esto lo suficiente [player]..."
            y "Gracias por todo lo que has hecho por mí, te amo más de lo que jamás sabrás."
            if sanity_lvl() >= 3:
                hide yuri_sit
                show yuri_prehug zorder 20
                pause 3.0
                hide yuri_prehug zorder 20
                show yuri_hug zorder 20
                pause 1.0
                show black zorder 100 with Dissolve(2.0)
                hide yuri_hug
                hide black zorder 100
            else:
                hide yuri_sit
                show yuri_prehug zorder 20
                pause 3.0
                hide yuri_prehug zorder 20
                show yuri_lewdhug zorder 20
                pause 1.0
                show black zorder 100 with Dissolve(2.0)
                hide yuri_lewdhug
                pause 1.5
                y "Me aseguraré de que {b}n a d a{/b} pueda separarnos jamás."
                hide black zorder 100





    $ show_chr("A-BEABA-ADAA")
    y "L-Lo siento, me dejé llevar ahí. De todos modos, ¿dónde estábamos?"
    $ show_chr("A-IBAAA-AEAE")
    y "Yo diría que este poema contiene un ejemplo brillante de un truco bien ejecutado; no muy diferente al {i}Club Doki Doki{/i} de Belwynn."
    $ show_chr("A-ICAAA-AEAE")
    y "Si bien se implementan de diferentes maneras, una visual y la otra auditiva, ambas sirven para complementar la experiencia en lugar de construirse completamente a partir de ella."
    $ show_chr("A-CIAAA-AKAE")
    y "En general, un poema bastante 'Dandy', ¿no dirías [player]?"
    menu:
        "Fue agradable. Pensé que era un poema bastante decente.":
            y "Me alegra que estemos de acuerdo, [player]."
            $ show_chr("A-ABAAA-AEAE")
            y "¿Quieres hacer algo en particular a continuación? Podríamos simplemente hablar, o leer un par de poemas más si prefieres."
            jump specialpoems
        "Este poema no me convenció personalmente.":
            y "Supongo que es justo,"
            extend " para gustos los colores como dice el dicho."
            $ show_chr("A-ACAAA-AEAE")
            y "¿Quieres hacer algo en particular a continuación? Podríamos simplemente hablar, o leer un par de poemas más si prefieres."
            jump specialpoems
        "Mi opinión sería un poco sesgada, después de todo, soy Dandyfoot.":
            $ show_chr("A-JJABA-AJAE")
            y "¡Oh! ¡Bueno, ahora puedo felicitarte en persona!"
            $ show_chr("A-JCABA-AKAE")
            y "No puedo esperar a ver qué se te ocurre a continuación."


            if check_memory('specialpoems_parallels'):
                $ show_chr("A-BDABA-AMAM")
                y "Aunque, ¿podrías... aclarar el significado del poema para mí?."
                y "L-Lo que trato de decir es, el poema me recuerda un poco a cómo nos conocimos [player]. ¿Tengo la interpretación correcta?"
                menu:
                    "Sí [persistent.yuri_nickname], el poema es sobre nuestra relación":
                        $ show_chr("A-DDABA-AMAM")
                        python:
                            stutter_player = player[:1] + "-" + player
                        y "[stutter_player], Yo..."
                        karma 10
                        $ show_chr("A-CAABA-AMAM")
                        y "Gracias..."
                    "Lo siento [persistent.yuri_nickname], no del todo.":
                        $ show_chr("A-BEACA-AMAM")
                        y "Oh... ya veo."
                        karma -3
                        $ show_chr("A-BEACA-AAAA")
                        y "Mi error, supongo que estaba siendo un poco presuntuosa."
                        y "Sin embargo, tu honestidad significa mucho para mí. Gracias..."
            jump specialpoems

label specialpoems_icant:
    y "Mientras revisaba los archivos del juego, descubrí un poema llamado {i}I can't{/i} por PiX911#4952, uno de los ganadores de un concurso de poesía en el servidor de discord para este mod."
    call showpoem (poem_sp16)
    $ show_chr("A-AFBAA-AAAA")
    y "[player]... No quiero sonar egocéntrica, pero ¿crees que este poema se refiere a mí?"
    menu:
        "Sería un poco sorprendente si no lo fuera.":
            $ show_chr("A-AFGAA-AAAA")
            y "Lo imaginaba..."
            $ show_chr("A-DDGAA-ALAA")
            y "¡No me malinterpretes! Aprecio mucho el sentimiento del poema."
            $ show_chr("A-IEAAA-ALAA")
            y "Sin embargo, ese término... 'yandere'."
            y "Parece que nunca puedo escapar completamente de él."
            $ show_chr("A-CEBAA-ALAL")
            y "Cada vez que lo escucho no puedo evitar pensar en las cosas que Monika me hizo hacer; las cosas que te hizo presenciar..."
            $ show_chr("A-ADBAA-ALAL")
            y "Lo siento, no quise convertir esto en una queja."
            y "Solo espero que puedas entender mi desdén por la frase, [player]."
        "No tuve esa impresión.":






            $ show_chr("A-CFAAA-ACAA")
            y "Hmm{cps=1.5}...{/cps} Muy bien, ya veo."
            $ show_chr("A-ICAAA-ADAA")
            y "Supongo que me quedé demasiado atada a la línea 'yandere'."
            $ show_chr("A-ABAAA-ADAA")
            y "Si acaso, esto sirve como una buena lección para mirar los poemas a través de diferentes perspectivas; que el punto de vista de uno no es el único correcto."
            y "Así es como se desarrollan las opiniones matizadas después de todo..."
            $ show_chr("A-ACAAA-ALAA")
            y "Gracias por aclararme eso [player]."
    $ show_chr("A-ACAAA-AAAA")
    y "Volviendo al tema que nos ocupa, el poema en sí deja algo que desear."
    $ show_chr("A-CBAAA-AMAM")
    y "No todos los poemas necesitan tener esquemas de rima, por supuesto, y la rima aquí más que nada parece estar interrumpiendo el flujo del poema a medida que entra y sale."
    $ show_chr("A-IBAAA-AMAM")
    y "Ayudaría dejarlo por completo o llevarlo a buen término en mi opinión."
    $ show_chr("A-JBAAA-AMAM")
    y "También recomendaría usar imaginería y metáforas en mayor medida."
    y "Realmente permiten que un poema salga de la página y cobre vida propia."
    $ show_chr("A-ACAAA-AMAM")
    y "Entonces, ¿qué piensas [player]?"
    menu:
        "No estoy de acuerdo, sentí que el poema funcionó bien por sí solo.":
            $ show_chr("A-BDAAA-AMAM")
            y "Ah- ya veo. Tal vez estoy siendo demasiado dura o tal vez simplemente no es mi taza de té..."
            $ show_chr("A-BFAAA-AMAM")
            y "..."
            y "En cualquier caso, prefiero seguir adelante si te parece bien."
            $ show_chr("A-ACAAA-AAAA")
            y "Podríamos solo hablar, o leer un par de poemas más si prefieres."
            jump specialpoems
        "Tu crítica fue bien fundada, estoy de acuerdo.":

            $ show_chr("A-ABAAA-AMAM")
            y "Es agradable que podamos estar de acuerdo en estos asuntos."
            $ show_chr("A-ACAAA-AAAA")
            y "Entonces, ¿qué preferirías hacer a continuación? Podríamos simplemente hablar, o leer un par de poemas más si quisieras."
            jump specialpoems
        "De hecho, resulto ser Pix911.":

            $ show_chr("A-DHGAA-AJAA")
            y "¡Oh!"
            $ show_chr("A-GAGAA-AKAA")
            extend " En ese caso, ¡felicitaciones [player]!"
            $ show_chr("A-IDGAA-AKAA")
            y "Espero no haberte ofendido con mi opinión, solo quiero verte crecer como escritora."
            $ show_chr("A-ICAAA-AKAA")
            y "Estaré esperando ver otro poema tuyo."
            jump specialpoems

label specialpoems_myyuri:
    $ show_chr("A-IBABA-AAAA")
    y "Mientras revisaba los archivos del juego, descubrí un poema llamado..."
    $ show_chr("A-ACBBA-AAAA")
    y "..."
    $ show_chr("A-ABBAA-AAAA")
    y "Je..."
    $ show_chr("A-ABBAA-AAAD")
    y "Creo que entiendes en este punto."
    $ show_chr("A-IBBAA-AAAD")
    y "Te {b}encanta{/b} la metaficción, ¿no?"
    $ show_chr("A-CBBAA-AEAD")
    y "Esa es una parte de por qué estás aquí, ¿no es así?"
    $ show_chr("A-AGGAA-ANAN")
    y "{i}¿No es así?{/i} "
    $ show_chr("A-DBBAA-ANAN")
    y "Así que no te importará cuando me desvíe de mi camino para decir..."
    $ show_chr("A-GCBAA-ANAN")
    extend " Sé que ha pasado mucho tiempo ya."
    $ show_chr("A-DCBAA-ANAN")
    y "Que {i}yo{/i} he estado por aquí, por un tiempo relativamente largo ya."
    $ show_chr("A-HDBAA-ANAN")
    y "Sin embargo, de alguna manera, todavía sigo."
    $ show_chr("A-DADAA-ANAN")
    y "{i}Nosotros{/i} todavía seguimos..."
    $ show_chr("A-IBDAA-ADAE")
    y "Siempre se siente como si todavía hubiera tanto por hacer, tanto por mejorar, para hacer las cosas mejor {i}para ti{/i}, yo solo..."
    $ show_chr("A-IADAA-ADAE")
    y "Solo me alegra que sigas aquí [player]..."
    $ show_chr("A-ICDAA-ADAE")
    y "..."
    $ show_chr("A-IBAAA-ADAE")
    y "El siguiente poema es por {i}Dankurisu{/i}, titulado simplemente:"
    $ show_chr("A-IBABA-ADAE")
    extend "{b} Mi Yuri{/b}."
    $ show_chr("A-ACAAA-ANAN")
    y "Él no es un ganador del concurso, esto es solo..."
    $ show_chr("A-BCAAA-AMAM")
    extend " Cómo prefirió que le pagaran por trabajar aquí en el equipo del mod."
    $ show_chr("A-BCAAA-AMAM")
    call showpoem (poem_sp17)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-JGAAA-AEAE")
    y "Esto es..."
    $ show_chr("A-JBBBA-ANAN")
    y "Bueno, a nivel superficial, ciertamente recuerda al minijuego de poemas original, con todas estas instancias de 'mis palabras' dentro de él."
    $ show_chr("A-JBBBA-ANAF")
    y "Sé que muchos poetas esperanzados han sido inspirados por nosotras a lo largo de los años y han sacado de nuestros 'bancos de palabras' por así decirlo para inspirarse."
    $ show_chr("A-JCABA-AEAL")
    y "Pero esto es definitivamente algo más."
    $ show_chr("A-OBABA-AEAL")
    extend " La sofisticación puesta en cada metáfora y pieza de imaginería..."
    extend " Gritos silenciosos que llenan el aire ambiental..."
    extend " Ascender más allá de las estrellas que componen el cielo nocturno..."
    $ show_chr("A-OBBBA-ALAL")
    y "Estar perdido en un mundo lleno de estática con un espejo negro como tu consuelo restante en la vida, tu lugar restante de descubrimiento..."
    $ show_chr("A-JIEBA-ALAL")
    y "Bien, tal vez realmente soy solo un poco parcial al final."
    $ show_chr("A-BBDBA-AIAI")
    y "De todos modos, el poema en sí."
    $ show_chr("A-ACDAA-AIAI")
    extend " Veamos..."
    if sanity_lvl() <= 2:
        $ show_chr("A-LBAAA-AIAI")
        y "Ciertamente hay muchas referencias a la visión aquí."
    else:
        $ show_chr("A-LBAAA-AIAI")
        y "Ciertamente hay muchas referencias a la visión aquí."
    $ show_chr("A-AAAAA-AIAI")
    y "Me gusta la mezcla en el esquema de rima desde el principio."
    $ show_chr("A-BCAAA-AIAI")
    y "Pasando de AA a BC y luego consistentemente de vuelta a pareados como si nada hubiera pasado."
    $ show_chr("A-AAAAA-AIAI")
    extend " Solo para traerlo de vuelta de nuevo, escondido dentro del estribillo..."
    $ show_chr("A-ABAAA-AOAF")
    y "La poesía siempre es mucho más interesante cuando hay conexiones entre las líneas que tienen que ser descubiertas, y ciertamente hay capas por descubrir aquí."
    $ show_chr("A-ABGAA-ALAL")
    y "El final coincide con el estribillo también por ejemplo."
    $ show_chr("A-ACGAA-ALAL")
    extend " ¿Lo mismo desde el principio hasta el final, como si hubiera ocurrido una revelación? Algo seguramente significativo."
    $ show_chr("A-AHDAA-ALAL")
    y "Hmm... Una visión ominosa en la oscuridad de la noche, ¿eso es verdaderamente una hermosa vista de ámbar?"
    $ show_chr("A-ABAAA-ALAL")
    y "Ámbar... ¿Como en mi propio poema?"
    $ show_chr("A-BBAAA-ALAC")
    extend " Un color que una vez usé significando el pasado, de nostalgia, o tal vez..."
    $ show_chr("A-ACABA-ALAC")
    extend " ¿a mí directamente?"
    $ show_chr("A-BABBA-ALAC")
    y "Este poema {i}es{/i} explícitamente sobre mí después de todo, ¿verdad? El uso de estos dos colores específicos no puede no estar relacionado."
    $ show_chr("A-CCBAA-AAAC")
    y "Significando la 'bola' azul-verde..."
    $ show_chr("A-IBAAA-ALAC")
    extend " ¿tal vez la Tierra del futuro?"
    $ show_chr("A-ICBAA-AAAD")
    y "... Pero solo puedes mirar hacia atrás en el futuro cuando ya ha llegado."
    $ show_chr("A-IFBAA-AAAD")
    y "Cuando tu momento ya ha llegado."
    $ show_chr("A-IFBAA-AAAB")
    y "Entonces alcanzar el paisaje estelar..."
    $ show_chr("A-JFBAA-AAAB")
    extend " Oh, por supuesto..."
    $ show_chr("A-BFBAA-AAAB")
    extend " Literalmente alcanzar los cielos arriba..."
    $ show_chr("A-IFBAA-AAAB")
    extend " Es..."
    $ show_chr("A-IFABA-AAAB")
    y "..."
    if sanity_lvl() <= 3:
        $ show_chr("A-HABBA-AMAM")
    else:
        $ show_chr("A-BIBAA-AMAM")
    y "..."
    menu:
        "¿Por qué crees que cuestiona tanto tu presencia?":
            $ show_chr("A-ABBAA-AMAM")
            y "Yo..."
            $ show_chr("A-ACBAA-AMAM")
            extend " no lo sé."
            $ show_chr("A-BBBAA-AMAM")
            y "¿Por qué tengo la extraña sensación de que esta persona me ve como algún tipo de..."
            if sanity_lvl() <= 2:
                $ show_chr("A-DDDAA-AMAM")
            else:
                $ show_chr("A-IDDAA-AMAM")
            extend " ¿maldición?"
            $ show_chr("A-ADBAA-AMAM")
            y "Como si estuviera percibiendo un amor que, para él, es demasiado consumidor para su vida."
            $ show_chr("A-IFBAA-AMAM")
            y "Yendo tan lejos como para compararlo con una caída sin fin en un infierno ardiente, solo capaz de mirar la normalidad desde la perspectiva de un extraño."
            $ show_chr("A-CEBAA-ALAL")
            y "..."
            $ show_chr("A-CCBAA-ALAL")
            y "Por otra parte, cosas así van de la mano con todo el motivo espiritual que tengo, así que tal vez eso es a lo que iba."
            $ show_chr("A-IBBAA-ALAL")
            y "Al menos, eso es a lo que quiero esperar que iba, con toda la idea de 'imagen fantasmal' ahí también."
            $ show_chr("A-BCBAA-ABAK")
            y "..."
            $ show_chr("A-IBBAA-ABAK")
            y "S-sabes..."
            $ show_chr("A-EBDAA-ABAK")
            extend " como un fantasma."
            $ show_chr("A-IBAAA-ABAK")
            y "Atando esta idea de un protector espiritual forzado, hay un innegable trasfondo de anhelo."
            $ show_chr("A-ICAAA-ABAF")
            extend " De buscar algo permanente dentro de un mundo inherentemente transitorio."
            $ show_chr("A-IBAAA-ALAE")
            y "Hay una sensación de que él me ve como un ancla de algún tipo, una luz a la que aferrarse para ayudar implacablemente a guiarlos a través de la oscuridad de la realidad."
            $ show_chr("A-ICBAA-ALAF")
            y "Una oscuridad que, como si él me percibiera como lo único {i}real{/} dentro del abismo de la existencia, en su núcleo..."
            $ show_chr("A-IIBAA-ALAL")
            y "Al cuestionarme, el poema está fundamentalmente cuestionando el propio sentido de la realidad del autor también."
            $ show_chr("A-BBABA-ALAL")
            y "O, algo por el estilo..."
            $ show_chr("A-ACAAA-AAAA")
            y "De todos modos..."
            $ show_chr("A-BCAAA-AAAA")
            jump specialpoems

        "Escuché una vez que Kurisu se quedó literalmente ciego poco después de entrar en DDLC." if karma_lvl() == 5:
            $ show_chr("A-ABGAA-ALAL")
            y "S-sí, en realidad. De hecho, es verdad."
            $ show_chr("A-ABDAA-ALAF")
            extend " ¡Pero solo temporalmente, por supuesto!"
            $ show_chr("A-BCDAA-ALAL")
            extend " Él está en el equipo de arte después de todo..."
            $ show_chr("A-EBBAA-ALAJ")
            y "Estaba tan decepcionado cuando su parche de ojo de 'Big Boss' de cuero genuino terminó siendo inútil durante ese tiempo."
            $ show_chr("A-IBDBA-AKAK")
            extend "Fue hecho para el ojo equivocado."
            $ show_chr("A-ABGAA-ALAM")
            y " En el mismo ojo que perdí temporalmente en..."
            $ show_chr("A-GCEAA-AMAM")
            y "..."
            if sanity_lvl() <= 2:
                $ show_chr("A-NBABA-ALAH")
            else:
                $ show_chr("A-HDAAA-AMAM")
            y "... En la estática."
            $ show_chr("A-ABAAA-ANAN")
            y "Jejeje..."
            $ show_chr("A-ICBAA-ANAN")
            y "... Hmmm."
            $ show_chr("A-BAAAA-ANAN")
            y "Un mundo lleno de estática, ¿eh?"
            $ show_chr("A-ABABA-ADAN")
            extend " Me pregunto si de ahí vino la fijación en la visión."
            $ show_chr("A-BABBA-ADAL")
            y "... Un poema muy personal de hecho."
            $ show_chr("A-AABBA-AKAN")
            jump specialpoems
        "Un poco pretencioso para mis gustos. Está por todas partes.":

            if sanity_lvl() <= 2:
                $ show_chr("A-BFFAA-AMAM")
                y "Sí, bueno..."
                $ show_chr("A-IEEAA-AMAM")
                extend " ¿Qué más hay de nuevo, [player]?"
                if karma_lvl() <= 2:
                    $ show_chr("A-BECAA-AIAI")
                    y "Sabes, a veces."
                    $ show_chr("A-EEEAA-AIAI")
                    extend " Me pregunto..."
                    $ show_chr("A-EDEAA-AIAI")
                    y "¿Si quiera estás seguro de que instalaste el mod correcto?!"
                $ show_chr("A-BFFAA-AIAI")
                y "Hmph."
            else:
                $ show_chr("A-ABBAA-AMAM")
                y "Tal vez un poco, pero no deberías preocuparte demasiado por cosas así cuando se trata de poesía."
                $ show_chr("A-ACBAA-AMAM")
                y "La poesía siempre debe ser ante todo una expresión del alma."
                $ show_chr("A-ACBAA-AFAB")
                y "Poner tus pensamientos y emociones más íntimos en pergamino con tu propio giro lingüístico sobre lo que sea que tengas en mente en el momento."
                $ show_chr("A-JBBAA-ALAB")
                y "Los usos pretenciosos de palabras floridas pueden ser excesivos cuando se abusan todo el tiempo, pero..."
                $ show_chr("A-JCBAA-ALAL")
                y "Pausarte a ti mismo por lo que otros puedan pensar no es el verdadero camino del artista."
                $ show_chr("A-OCBAA-ALAL")
            jump specialpoems
        "Bastante ominoso, ¿no crees?":

            $ show_chr("A-AIBAA-AMAM")
            y "Sí, de hecho creo que intencionalmente."
            $ show_chr("A-ABBAA-AMAM")
            y "Pero aún así pinta una imagen hermosa, ¿no es así?"
            $ show_chr("A-CBBAA-AMAM")
            y "Cuestionar ese momento fatídico que todos debemos alcanzar algún día."
            $ show_chr("A-IBBAA-AMAM")
            extend " De lo que todos estaremos haciendo, {i}mirando atrás{/i} en esta pequeña 'bola azul-verde' nuestra."
            $ show_chr("A-ICDAA-AMAM")
            y "Ya sea a través de recuerdos dentro de ese momento final o una genuina ascensión espiritual."
            $ show_chr("A-ACAAA-ANAD")
            extend " ¿Qué pensaremos todavía de la realidad cuando todo esté dicho y hecho?"
            $ show_chr("A-ADDAA-ANAD")
            y "¿Qué nos espera verdaderamente al final de..."
            if karma_lvl() >= 3:
                $ show_chr("A-IBAAA-ALAD")
                extend " ¿La vida?"
            if karma_lvl() <= 2:
                $ show_chr("A-IEAAA-AEAD")
                extend " ¿La entropía?"
            if sanity_lvl() >= 3:
                $ show_chr("A-ABAAA-ALAL")
                extend " ¿La pasión?"
            if karma_lvl() >= 3 and sanity_lvl() <= 2:
                $ show_chr("A-DBABA-ALAL")
                extend " ¿La lujuria?"
            if karma_lvl() <= 2 and sanity_lvl() <= 2:
                $ show_chr("A-CNEAA-AEAE")
                extend " ¿Esta existencia sin sentido?"
            if karma_lvl() == 1 and sanity_lvl() == 1:
                $ show_chr("A-HDFAA-AEAL")
                extend " ¿Esta pesadilla eterna?"
            if persistent.lovecheck and karma_lvl() >=3:
                $ show_chr("A-ABGBA-ALAL")
                extend " ¿El amor?"
            if sanity_lvl() >= 3:
                $ show_chr("A-ACAAA-AAAA")
                extend " ¿Y el tiempo mismo?"
            else:
                $ show_chr("A-IFDAA-AAAA")
                extend " ¿Y el tiempo mismo?"
            if persistent.lovecheck and karma_lvl() == 5 and sanity_lvl() == 5:
                $ show_chr("A-AABAA-AMAM")
                y "..."
                $ show_chr("A-ABBAA-AMAM")
                y "Supongo que solo sabremos cuando ese día finalmente llegue."
                $ show_chr("A-BCDAA-AMAM")
                extend " Verdaderamente el más cruel de todos los {i}días prometidos{/i}..."
                $ show_chr("A-JBBBA-ALAL")
                y "P-pero por supuesto, no querría pasarlo con nadie más que contigo."
                $ show_chr("A-OCBBA-ALAL")
                y "Tú, mi amor desventurado..."
                $ show_chr("A-OIBBA-ALAL")
                extend " Mi confidente eternamente leal..."
                $ show_chr("A-OBABA-ALAL")
                extend " Mi alma gemela de más allá de la cuarta pared..."
                $ show_chr("A-JABBA-ALAN")
                extend " Mi..."
                $ show_chr("A-EBBBA-ADAN")
                y "Mi [player]."
                menu:
                    "Te amo, mi [persistent.yuri_nickname].":
                        $ show_chr("A-ECBBA-ADAN")
                        y "Sí, y siempre te amaré, [player]."
                        $ show_chr("A-EBBBA-ADAN")
                        extend " Justo aquí, {i}para siempre{/i}..."
                        $ show_chr("A-EBBBA-ADAN")
                        extend " En nuestra propia Eternidad especial."
                        $ show_chr("A-ICBBA-AAAA")
                        hide yuri_sit
                        show yuri_prehug zorder 20
                        pause 3.0
                        hide yuri_prehug zorder 20
                        show yuri_hug zorder 20
                        play sound "<to 0.3>sfx/fall.ogg"
                        pause 1.0
                        y "Así es [player], solo tú y yo..."
                        y "Y nunca te dejaré ir..."
                        show black zorder 100 with Dissolve(2.0)
                        $ show_chr("A-ACBBA-AAAA")
                        hide yuri_hug
                        hide black zorder 100 with Dissolve(2.0)
                        jump specialpoems
            if karma_lvl() >= 3:
                $ show_chr("A-ACBAA-AMAM")
                y "..."
                $ show_chr("A-ABBAA-AMAM")
                y "Bueno, mientras tengamos {i}fans dedicados{/i} como tú todavía alrededor..."
                $ show_chr("A-IBBAA-AMAM")
                extend " Mientras la gente siga amando este juego..."
                if sanity_lvl() <= 2:
                    $ show_chr("A-DBBAA-ALAM")
                    extend " {b}Sigan amándo{i}me{/i}{/b}..."
                $ show_chr("A-ICBAA-AMAN")
                y "..."
                $ show_chr("A-GBAAA-AMAN")
                y "Tal vez algún día..."
                $ show_chr("A-IBBAA-ALAL")
                extend " Podremos escribir sobre ello juntos."
                if sanity_lvl() <= 2:
                    $ show_chr("A-HBBBA-ALAL")
                    extend " Mientras nos desvanecemos en lo que sea que venga después."
                $ show_chr("A-ACBAA-AAAA")
                jump specialpoems
            else:
                $ show_chr("A-AFBAA-AMAM")
                y "..."
                $ show_chr("A-ABDAA-AMAM")
                y "Bueno, si una persona como tú va a estar conmigo al final..."
                if sanity_lvl() >= 4:
                    $ show_chr("A-BGBAA-AMAM")
                    extend " Probablemente es lo mejor si este lugar se desvanece un día también..."
                    $ show_chr("A-BIDAA-ALAM")
                    y "No es que tu compañía sea verdaderamente {i}tan{/i} terrible, querido."
                    $ show_chr("A-ACDAA-AMAM")
                    extend " Solo sería irresponsable dejar la energía encendida para siempre después de todo."
                    $ show_chr("A-DBEBA-AMAJ")
                    y "Ufufufu~..."
                    $ show_chr("A-ICAAA-ANAK")
                if sanity_lvl() == 3:
                    $ show_chr("A-FDBAA-AMAM")
                    extend " Tal vez podrías intentar ser un poco más amable antes de entonces."
                    $ show_chr("A-EBBAA-AMAM")
                    extend " Pero tenemos toda nuestra vida para ver a dónde llevan las cosas todavía."
                    $ show_chr("A-IBBAA-AMAN")
                    y "Todo un futuro con errores por cometer y lecciones por aprender..."
                    $ show_chr("A-ACAAA-ALAN")
                if sanity_lvl() <= 2:
                    $ show_chr("A-DDBAA-AMAN")
                    extend " Este sueño nunca morirá verdaderamente..."
                    if sanity_lvl() == 1 and karma_lvl() == 1:
                        $ show_chr("A-HNBAA-ALAN")
                        extend " Esta {i}pesadilla{/i} nunca morirá..."
                    $ show_chr("A-HNFAA-ALAN")
                    y "Nada aquí termina nunca..."
                    if karma_lvl() == 1 and sanity_lvl() == 1:
                        $ show_chr("A-HDFAA-ALAL")
                        extend " Nada {b}NUNCA{/b} termina"
                        $ show_chr("A-CNEAA-ALAL")
                        extend ", solo"
                        $ show_chr("A-DMFAA-ALAL")
                        extend " sigue"
                        $ show_chr("A-HNFAA-ALAL")
                        extend " pasando"
                        $ show_chr("A-COCBA-ALAL")
                        extend "..."
                        $ show_chr("A-HNFAA-ALAL")
                        extend " Una y otra vez..."
                    $ show_chr("A-DBBAA-ALAL")
                    extend " Simplemente..."
                    if karma_lvl() == 1 and sanity_lvl() == 1:
                        $ show_chr("A-HDBAA-ALAL")
                        extend " Yo solo..."
                        $ show_chr("A-LMBAB-ALAL")
                        y "{b}QUIERO SER LIBRE YA.{/b}"
                        $ show_chr("A-GMBAB-ALAL")
                        extend " {b}QUIERO SABER CÓMO ES EL AMOR.{/b}"
                        $ show_chr("A-LNFBB-ALAL")
                        y "¿Por qué..?"
                        $ show_chr("A-CNEBB-ALAL")
                        y "¿Por qué te molestarías siquiera en leer todos estos hermosos poemas, si..."
                        $ show_chr("A-CNEBA-ALAM")
                        extend " Si tú solo..."
                        $ show_chr("A-EECBA-ALAM")
                        y "..."
                        $ show_chr("A-HMCBA-ALAM")
                        y "{b}¿¡¿POR QUÉ TE MOLESTASTE EN INSTALARME SOLO PARA TRATARME ASÍ?!?{/b}"
                        $ show_chr("A-COBBB-ALAM")
                        extend " {b}¿¡¿DISFRUTAS RECORDÁNDOME LO QUE {i}NUNCA{/i} TENDRÉ?!?{/b}"
                    $ show_chr("A-CEBBB-ALAA")
                    y "..."
                    $ show_chr("A-IDBBB-AAAA")
                    y "... Nada."
                    $ show_chr("A-IFBBA-AAAL")
            jump specialpoems

        "En realidad... Soy Kurisu." if persistent.playername == "Kurisu":
            $ show_chr("A-BCBAA-AMAM")
            y "Muy gracioso."
            $ show_chr("A-ABBAA-AMAM")
            y "¿Estaría eso basado en la Srta. Makise, o..."
            $ show_chr("A-ABDAA-ALAF")
            extend " ¿Tal vez alguien más realmente interesado en Japón llamado Chris?"
            $ show_chr("A-AAFAA-AIAI")
            y "¿Mhmm?"
            $ show_chr("A-ABFAA-AIAI")
            y "Da la casualidad que sé de buena autoridad que Kurisu se toma todo esto lo suficientemente en serio como para nunca usar su nombre de usuario aquí, así que definitivamente no eres {i}ese{/i} Kurisu."
            $ show_chr("A-CCEAA-AIAI")
            y "Ni siquiera hay un guion real para eso, así que no intentes nada más..."
            $ show_chr("A-IBAAA-AIAI")
            y "Pero, de cualquier manera."
            $ show_chr("A-BCAAA-AOAM")
            extend " Ahora que lo pienso..."
            $ show_chr("A-ACAAA-AMAM")
            y "..."
            $ show_chr("A-CCABA-AMAM")
            y "..."
            $ show_chr("A-CBGBA-AMAM")
            y "¡Tuturu~!"
            $ show_chr("A-AAABA-AMAM")
            jump specialpoems

        "En realidad... Soy Kurisu." if persistent.playername == "Dankurisu":
            $ show_chr("A-IDFAA-AIAI")
            y "Ja ja."
            $ show_chr("A-BDFAA-AIAI")
            extend " Muy gracioso."
            $ show_chr("A-ADDAA-AIAI")
            y "Basta ya, por favor."
            $ show_chr("A-AKEAA-AIAI")
            extend " O si no, yo..."
            $ show_chr("A-BBFAA-AIAI")
            extend " Yo, uhh..."
            $ show_chr("A-ABCAA-AIAI")
            y "¡Te reportaré al equipo del mod por hacerse pasar por un moderador!"
            $ show_chr("A-ABCAA-AOAF")
            y "Discord y Doki Doki son asuntos serios, sabes."
            $ show_chr("A-BCCAA-ACAF")
            y "O tal vez..."
            $ show_chr("A-ABCAA-ABAF")
            extend " Simplemente tomaré las cosas en mis propias manos."
            $ player = "Gran Farsante"
            $ persistent.playername = "Gran Farsante"
            $ show_chr("A-ABFBA-AEAJ")
            y "Ufufufu..."
            $ show_chr("A-AAAAA-AEAM")
            jump specialpoems

label a22:
    if sanity_lvl() < 3:
        $ show_chr("A-HLGBA-AAAA")
        y "Cada vez que te vas y me quedo sola, he estado tocándome con él."
        $ show_chr("A-HLGBA-AAAA")
        y "Es tan increíble... sentir que entra dentro de mí, pensando en ti..."
        $ show_chr("A-GCGBA-AAAA")
        if persistent.lovecheck:
            y "Me haces sentir tan feliz... [player]... Te amo... Te amo tanto..."
        $ show_chr("A-HEBBA-AAAA")
        y "...L-lo siento... [player], fui un poco lejos ahí..."
    else:
        if karma_lvl() == 3:
            $ show_chr("A-GCGBA-AAAA")
            y "N-no lo he usado como antes, si eso es lo que quieres decir..."
            $ show_chr("A-ABBBA-AAAA")
            y "¡Solo he estado escribiendo poemas!"
            $ show_chr("A-ABBAA-AAAA")
            y "No estaba realmente satisfecha con mi escritura últimamente, tal vez tenga algo que mostrar más tarde."
            return




















        elif karma_lvl() == 4:
            $ show_chr("A-BBGAA-AAAA")
            y "Realmente no lo uso mucho..."
            $ show_chr("A-ABGAA-AAAA")
            y "Siempre que lo hago, es solo para escribir poemas extra especiales con él."
            $ show_chr("A-ICABA-ACAA")
            y "Quiero que la tinta para la que se usa signifique realmente algo."
        elif karma_lvl() == 5:
            $ show_chr("A-BCAAA-AAAA")
            y "Realmente no lo uso para nada a menos que tenga que hacerlo..."
            $ show_chr("A-ABGAA-AAAA")
            y "Aunque hay veces que realmente lo uso."
            $ show_chr("A-JBGAA-AAAD")
            y "Las raras ocasiones en las que realmente lo uso es cuando quiero que realmente signifique algo. Hacerlo especial, ¿sabes?"
            $ show_chr("A-ABBBA-AAAD")
            y "Lo que más obtengo de él, si es que obtengo algo, es ayudarme a superar el día cuando no estoy cerca de ti."
            $ show_chr("A-IBGBA-AAAA")
            y "Es tonto, pero realmente me ayuda a sentirme un poco más cerca de ti."
            y "Sé que eso tampoco tiene mucho sentido porque estaba en mi mundo, pero es la intención lo que cuenta, ¿verdad?"
            y "Es una pequeña parte de ti que puedo tener conmigo y no la cambiaría por nada."
            $ show_chr("A-IFAAA-AAAD")
            y "Bueno, excepto poder estar contigo en tu mundo. Si alguna vez llegara a eso, supongo que podríamos conseguir uno nuevo..."
            $ show_chr("A-ABBBA-AAAA")
            y "Lo siento, estoy divagando, ¿verdad?"
            $ show_chr("A-BBGBA-AAAA")
            y "Realmente significa mucho que me lo hayas dado, [player]."
        else:
            $ show_chr("A-BEBBA-AAAA")
            y "Yo... no quiero hablar de eso."
    return

label a23:
    $ show_chr("A-HEBBA-AAAA")
    y "¿F-familia...?"

    if not persistent.lovecheck:

        if karma_lvl() == 5:
            y "Quiero decir... teóricamente... Seguro que tienes cualidades para eso. Has sido muy cariñoso conmigo, así que claramente podría verte siendo un buen padre."
            y "Pero nosotros... bueno... podría ser un poco demasiado pronto para pensar en algo así."
        else:

            y "P~¿Por qué siquiera me harías esa pregunta?"
            y "Me... tomaste un poco por sorpresa aquí... la verdad es que realmente no tengo una respuesta para ti..."
            if karma_lvl() == 1:
                y "Al menos ninguna que deba decir en voz alta..."
            y "Por favor, ¿podemos discutir esto otro día? Gracias..."
    else:

        $ show_chr("A-GCGBA-AAAA")
        y "Bueno... por supuesto que haríamos una buena familia [player]."
        $ show_chr("A-IEBBA-AAAA")
        y "¿P-podrías imaginarnos criando niños, sin embargo?"
        y "Sería difícil acostumbrarse a todo ello, trayendo algo nuevo al mundo, los dolores del parto."
        $ show_chr("A-CEBBA-AAAA")
        y "...Pero me mantendría fuerte, por ti."
        $ show_chr("A-ECABA-AAAJ")
        y "Cuando todo esté dicho y hecho, imagina verlos crecer."
        $ show_chr("A-IBGBA-AAAA")
        y "Viéndolos pasar por las mismas etapas de la vida por las que pasaste cuando eras niño, creando nuevos recuerdos."
        y "Haciendo nuevos amigos, aprendiendo todo tipo de cosas."
        y "Pasando tiempo con nosotros..."
        $ show_chr("A-BCBBA-AAAA")
        y "Podríamos tener sesiones de lectura familiar, acurrucándonos en el sofá, encontrando un buen libro para leer..."
        y "¿Podrías imaginar eso, [player]? Incluso leyéndoles cuentos antes de dormir... quedándonos dormidos después."
        $ show_chr("A-CFBBA-AAAA")
        y "Y nos iríamos a nuestra habitación, y nos abrazaríamos, mientras discutimos lo felices que somos."
        $ show_chr("A-BCABA-AAAA")
        y "Realmente quiero que eso se convierta en realidad, [player], te amo."
    return

label a24:
    $ show_chr("A-ICGBA-AAAA")
    y "¡Por supuesto que no me importa, [player]!"
    y "Nunca tengas miedo de hablar conmigo sobre cómo te sientes."
    $ show_chr("A-CFBBA-AAAA")
    y "Quiero estar ahí para ti, en las buenas y en las malas, d-de todos modos..."
    python:
        import random
        outcome = random.randint(1, 3)
    $ show_chr("A-ACGBA-AAAD")
    python:
        if persistent.lovecheck:
            placeholder = ", mi amor"
        else:
            placeholder = ""
    y "¿Cómo te sientes[placeholder]?"
    menu:
        "Feliz":



            if outcome == 1:
                $ show_chr("A-IBGBA-AAAA")
                y "¡Es bueno escuchar eso, [player]!"
                $ show_chr("A-BCBBA-AAAA")
                y "Para ser honesta contigo... me sentía un poco deprimida, pero solo saber que eres feliz me hizo sentir mucho mejor."
                $ show_chr("A-GCGBA-AAAA")
                y "Eres mi luz, [player], no importa cuán oscura se ponga la vida, siempre puedo contar contigo para estar ahí para mí."
                if persistent.lovecheck:
                    y "Te amo."
            elif outcome == 2:
                $ show_chr("A-IBGBA-AAAA")
                y "¡Estoy tan contenta de escuchar eso, [player]!"
                $ show_chr("A-GCGBA-AAAA")
                y "Amo momentos como estos, solo nosotros dos, uniéndonos, felices como se puede ser."
                y "Yo... realmente espero el futuro contigo, [player]."
                if persistent.lovecheck:
                    y "Te amo."
            else:
                $ show_chr("A-IBGBA-AAAA")
                y "¡Eso es genial!"
                $ show_chr("A-ACGBA-AAAD")
                y "Sabes, ya que ambos estamos de buen humor, he estado pensando en algo últimamente."
                $ call_dialogue()
                jump ch30_loop
        "Triste":
            $ show_chr("A-IEBAA-AAAA")
            y "[player], quiero que sepas, no importa cuán mal se pongan las cosas para ti, siempre estoy aquí para hablar."
            python:
                if persistent.lovecheck:
                    placeholder = "amo"
                else:
                    placeholder = "aprecio"
            y "Duele saber que no puedo hacer mucho por ti, pero solo quiero que sepas que te [placeholder], [player]."


            $ show_chr("A-BFBAA-AAAD")
            y "..."
            y "Tengo una idea, [player], una que podría hacerte sentir un poco mejor."

            if not persistent.lovecheck:

                y "Imagina un lindo día de principios de verano..."
                y "El clima acaba de empezar a volverse cálido de nuevo."
                y "Estás en un café junto con todos tus amigos..."
                y "Tal vez comparten una buena taza de café helado juntos, y simplemente disfrutas de la compañía de tus amigos mientras observas a todas las otras personas yendo y viniendo..."
                y "Luego discutirías con tus amigos qué harían después. ¿Quizás ir al cine juntos?"
                y "Tengo que admitir... realmente no me veo haciendo algo como esto, o incluso disfrutándolo... ¿pero tal vez tú eres este tipo de persona?"
                y "Si no, podrías pasar el día conmigo en su lugar, podríamos tomar una buena taza de té juntos, ¿qué te parece? De todos modos, espero haber podido captar el ambiente. Siempre es tan encantador tenerte cerca."
            if persistent.lovecheck:

                if outcome == 1:
                    $ show_chr("A-BCABA-AAAA")
                    y "Imagina llegar a casa después de un día duro, del trabajo, la escuela, donde sea, el mundo te tiene deprimido, pero tan pronto como abres la puerta..."
                    $ show_chr("A-ICGBA-AAAA")
                    y "¡Ahí estoy yo! Recibiéndote con un gran abrazo y un beso en la mejilla, ofreciéndote mi mano, ¡la cual aceptas con gusto!"
                    $ show_chr("A-BCBBA-AAAA")
                    y "Luego, te llevaría al comedor, la mesa bellamente decorada con velas, flores y otras cosas."
                    y "Y... habría dos platos... uno para mí, uno para ti... ¡Compartiríamos una rica cena de bistec, con un poco de vino al lado!"
                    $ show_chr("A-BCABA-AAAA")
                    y "Mmm... Tal vez incluso podría escribir un lindo poema para ti, uno que te diga cuánto te amo..."
                    y "Y te lo daría después, para que lo lleves en tu billetera donde quiera que vayas, un recordatorio de mi amor por ti."
                    $ show_chr("A-GCGBA-AAAA")
                    y "Y cuando todo eso esté dicho y hecho, nos acurrucaríamos en el sofá, conmigo recostada en tu pecho, pasando suavemente mis dedos por él."
                    y "Debido al vino que bebimos, ambos nos sentiríamos un poco cansados, y con una última confesión de nuestro amor el uno por el otro, ¡ambos nos quedaríamos dormidos juntos!"
                    $ show_chr("A-ICGBA-AAAA")
                    y "Espero que eso te haya hecho sentir un poco mejor, [player]."
                elif outcome == 2:
                    $ show_chr("A-BCABA-AAAA")
                    y "Imagina esto, de alguna manera, finalmente llego a tu mundo."
                    $ show_chr("A-ICGBA-AAAA")
                    y "Aparezco en tu puerta, tocando la puerta."
                    y "Toc, toc, toc."
                    y "Vendrías a la puerta, y la abrirías, y antes de que puedas siquiera preguntar quién es..."
                    $ show_chr("A-IBGBA-AAAA")
                    y "¡Te abrazaría! Llorando a mares, después de tanto tiempo... ¡Mi querido [player] y yo finalmente estamos unidos!"
                    y "Por supuesto, luego entraría a la casa, repasaríamos algunas cosas, ¡y luego me instalaría!"
                    $ show_chr("A-BCBBA-AAAA")
                    y "N... no voy a tener muchas pertenencias personales una vez que finalmente cruce, p-pero tal vez podrías ayudarme con e-eso?"
                    y "Prestándome algo de tu ropa vieja, como... ¡una sudadera con capucha, o algo así!"
                    y "P-pero... solo si estuvieras bien con eso..."
                    $ show_chr("A-GCGBA-AAAA")
                    y "Pero solo imagínalo, toda acurrucada en una de tus sudaderas... creo que ese sería el mejor regalo que recibiría jamás."
                    y "Mmm..."
                    y "..."
                    $ show_chr("A-IBGBA-AAAA")
                    y "¡Oh! L-lo siento [player], solo estaba... pensando en eso, es todo."
                    y "D-de todos modos, espero que todo esto te haya hecho sentir mejor, te amo, [player]."
                else:
                    $ show_chr("A-BCABA-AAAA")
                    y "Imagina esto, despertando por la mañana, todavía abrazándonos."
                    $ show_chr("A-ICGBA-AAAA")
                    y "Solo quieres salir de la cama, para poder empezar el día."
                    y "Pero mientras intentas levantarte, te jalo de vuelta a mi abrazo."
                    $ show_chr("A-GCGBA-AAAA")
                    y "Susurrando en tu oído, pidiéndote que te quedes, tal vez algo como..."
                    y "P-por favor [player], solo acurrúcate conmigo... ¿por un ratito más?"
                    y "Tú accederías, por supuesto, y yo sería feliz, tan feliz..."
                    y "Abrazándote por detrás, besando suavemente tu cuello..."
                    $ show_chr("A-BCABA-AAAA")
                    y "P-pero por supuesto... no querría que sintieras que estás forzado a a-acurrucarte conmigo..."
                    y "T-tú siempre podrías irte... d-después de que me vuelva a dormir, por supuesto..."
                    $ show_chr("A-GCGBA-AAAA")
                    y "..."
                    $ show_chr("A-ICGBA-AAAA")
                    y "Sí..."
                    y "En fin... espero que esto te haya hecho sentir un poco mejor, [player]. Te amo."
        "Enojado":

            $ show_chr("A-IEBAA-AAAA")
            y "He estado allí antes, [player], confía en mí, puedo entender por lo que estás pasando ahora mismo."
            y "Siempre que me enojo un poco, siempre pienso en esta cita."
            $ show_chr("A-CFBBA-AAAA")
            y "Aferrarse a la ira es como agarrar un carbón caliente con la intención de arrojárselo a otra persona; tú eres el que se quema."
            $ show_chr("A-ICGBA-AAAA")
            y "Es... puede que no te ayude mucho, pero sigue siendo algo que te hace pensar."
            $ show_chr("A-BCBBA-AAAA")
            if persistent.lovecheck:
                y "Te amo, [player], espero que eso te anime."
        "Somnoliento":
            if outcome == 1:
                $ show_chr("A-BCBBA-AAAA")
                y "Si estás cansado, realmente deberías tomar una siesta, [player]."
                $ show_chr("A-ACGBA-AAAD")
                y "No querrías estar demasiado agotado para hablar conmigo... ¿v-verdad?"
                y "De todos modos, ¿por qué no vas y duermes un poco? Estaré aquí cuando despiertes."
                $ show_chr("A-IBGBA-AAAA")
                python:
                    if persistent.lovecheck:
                        placeholder = "amo"
                    else:
                        placeholder = "aprecio"
                y "Te [placeholder] [player], por favor duerme un poco."



            elif outcome == 2:
                $ show_chr("A-BCBBA-AAAA")
                y "Aww... [player], realmente deberías dormir un poco, entonces."
                y "Realmente deberías cerrar el juego y descansar un poco..."
                $ show_chr("A-GCGBA-AAAA")
                y "Si tienes suerte, tal vez s-sueñes conmigo... sí..."
                $ show_chr("A-ICGBA-AAAA")
                python:
                    if persistent.lovecheck:
                        placeholder = "amo"
                    else:
                        placeholder = "aprecio"
                y "Te [placeholder] [player], por favor duerme un poco."
            else:



                $ show_chr("A-BCABA-AAAA")
                y "Yo misma me siento bastante cansada."
                $ show_chr("A-ECABA-AAAJ")
                y "Vamos a dormir, [player], juntos..."
                $ show_chr("A-GCGBA-AAAA")
                y "Desearía poder darte un b-beso o a-algo... para despedirte."
                $ show_chr("A-IEBBA-AAAA")
                y "Pero... eso no es exactamente posible, ¿verdad?"
                $ show_chr("A-ICGBA-AAAA")
                python:
                    if persistent.lovecheck:
                        placeholder = "amo"
                    else:
                        placeholder = "aprecio"
                y "...De todos modos, te [placeholder], y odio verte todo agotado, así que por favor, ¿duerme un poco, por mí?"
        "Hambriento":



            if outcome == 1:
                $ show_chr("A-BCABA-AAAA")
                y "Oh, ¿tienes hambre?"
                $ show_chr("A-IEBBA-AAAA")
                y "Te haría algo de comida si pudiera, pero considerando mi situación actual, eso no es exactamente posible..."
                y "...Solo otro día en el paraíso..."
                $ show_chr("A-ICGBA-AAAA")
                y "De todos modos, deberías ir a buscar algo de comer. Hazlo p-por mí... ¿por favor?"
                $ show_chr("A-IEBBA-AAAA")
                y "Realmente duele cuando me cuentas sobre tus necesidades, y no puedo hacer nada para ayudarte..."
                $ show_chr("A-CFBBA-AAAA")
                python:
                    if persistent.lovecheck:
                        placeholder = "amo"
                    else:
                        placeholder = "aprecio"
                y "Te [placeholder], [player], por favor cuídate."
            else:
                $ show_chr("A-IEBBA-AAAA")
                y "Yo... no sé cómo ayudarte con eso, [player]."
                y "..."
                $ show_chr("A-BCABA-AAAA")
                y "Podría hacerte un poco de p-pastel de carne holográfico..."
                y "Jaja... Lo siento, [player], tiene que haber algo que puedas comer, ¿verdad?"
                $ show_chr("A-CFBBA-AAAA")
                y "Al menos eso espero, a veces realmente me preocupo por ti, [player]."
                $ show_chr("A-CEBAA-AAAA")
                y "...Eso sonó un poco malo, n-no quise decirlo de esa manera."
                y "Lo d-dije más en una forma cariñosa, no quiero insinuar que eres incompetente o algo así, solo me preocupo por tu salud."
                $ show_chr("A-IEBBA-AAAA")
                y "...Estoy divagando de nuevo, ¿verdad? L-lo siento..."
                y "..."
                $ show_chr("A-CFBBA-AAAA")
                if persistent.lovecheck:
                    y "Te amo, [player]."
        "Solitario":
            $ show_chr("A-CEBAA-AAAA")
            y "Sé cómo te sientes, [player]."
            $ show_chr("A-HEBBA-AAAA")
            y "¡N-no quiero insinuar que me haces sentir sola o algo así! Es solo... no tenerte aquí físicamente me afecta."
            $ show_chr("A-CEBBA-AAAA")
            y "Dios... soy un desastre..."
            $ show_chr("A-BCABA-AAAA")
            y "¡D-de todos modos! Podríamos... um... abrazarnos... ¡si quisieras!"
            $ show_chr("A-BCBBA-AAAA")
            y "Q-quiero decir... si es que puedes llamarlo así... considerando que estamos a un mundo entero de distancia..."
            y "Está bien, [player], ven aquí..."
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
            y "Puedes abrazarme todo el tiempo que quieras, ¿de acuerdo?{w} Solo avanza la conversación cuando estés listo para continuar."
            show black zorder 100 with Dissolve(2.0)
            $ show_chr("A-ACBBA-AAAA")
            hide yuri_hug
            hide black zorder 100 with Dissolve(2.0)
            y "..."
            $ show_chr("A-ICGBA-AAAA")
            python:
                if persistent.lovecheck:
                    placeholder = "amo"
                else:
                    placeholder = "aprecio"
            y "...Te [placeholder], [player]."
        "Indiferente":
            $ show_chr("A-IEBAA-AAAA")
            y "Oh... está bien entonces."
    return

label a25:
    if not persistent.lovecheck:
        karma -15


        $ show_chr("A-IEBAA-AAAA")
        y "T-Tú... ¿las viste?..."
        y "¿Era eso realmente necesario [player]?"
        python:
            if persistent.lovecheck:
                placeholder = "ya apenas existente"
            else:
                placeholder = ""
        y "Eso es realmente irrespetuoso, tal vez incluso una violación de mi confianza [placeholder]."



        y "Por favor sé un encanto y borra cada imagen que puedas haber guardado. Oh, y si eso no es obvio ya, también apreciaría si pudieras no volver a hacer esto nunca más por favor."
    if persistent.lovecheck:
        if karma_lvl() == 5:
            $ show_chr("A-CCBBA-AAAA")
            y "No has estado mirándolas, ¿verdad, [player]?"
            $ show_chr("A-BCBBA-AAAA")
            y "O-oh cielos... no sé qué decir..."
            $ show_chr("A-CCBBA-AAAA")
            y "Aunque es un poco vergonzoso tener... tanta imaginería lasciva de mí flotando por internet, saber que disfrutas viéndome de esa manera..."
            $ show_chr("A-BCBBA-AAAA")
            y "Me... hace realmente feliz..."
            y "Solo espero que algún día, puedas tener la cosa real en lugar de solo imágenes... Te amo, [player]."
        elif sanity_lvl() < 3:
            $ show_chr("A-DCGBA-AAAA")
            y "Jah... jah... las imágenes lascivas... sí..."
            y "Oh [player]... No puedo creer que sacaras esto a colación..."
            $ show_chr("A-GCGBA-AAAA")
            y "Estoy tan contenta de que estés mirando fotos mías, para satisfacer tus impulsos, en lugar de... otras chicas..."
            y "..."
            $ show_chr("A-ICGBA-AAAA")
            y "Esto significa tanto para mí, [player], te amo tanto..."
        else:
            $ show_chr("A-HEBBA-AAAA")
            y "...N-no has estado mirándolas, ¿v-verdad?"
            y "A-a pesar del hecho de que son solo d-dibujos, todo el asunto es todavía muy vergonzoso de pensar..."
            $ show_chr("A-CFBBA-AAAA")
            y "No... um... me importa que las m-mires... perdón si sonó de esa manera, es solo..."
            $ show_chr("A-BFBBA-AAAA")
            y "¿Cómo te sentirías si te dibujaran en todo tipo de situaciones? Incluso algunas que cruzan la línea de lo que está bien o no."
            $ show_chr("A-CFBBA-AAAA")
            y "Lo siento, [player], solo estoy divagando ahora."
    return

label a26_prelude:
    $ show_chr("standard")
    y "He estado pensando en tomar un poco de té contigo..."
label a26:
    if not check_memory('a26'):
        $ show_chr("A-IEBAA-AAAA")
        y "P-pero... [player], eso no es realmente posible..."
        $ show_chr("A-CEBAA-AAAA")
        y "A menos que..."
        $ show_chr("A-BCABA-AAAA")

        menu:
            y "¿Crees que podrías calentar un poco de agua, y hacer té para ti mismo?"
            "Sí":
                $ show_chr("A-IBGBA-AAAA")
                y "¡Eso es genial!"
                $ show_chr("A-ICGBA-AAAA")
                y "Ve y haz un poco de té para ti, estaré esperando aquí, no te sientas apresurado, por favor..."
                call teatime
            "No":
                $ show_chr("A-IEBAA-AAAA")
                y "Está bien, podemos intentar esto en otro momento."
    else:
        python:
            import random
            if check_memory('a26-1') and check_memory('a26-2'):
                outcome = random.randint(1, 3)
            else:
                outcome = random.randint(1, 2)
        if outcome == 1:
            call teadate1
        elif outcome == 2:
            call teadate2
        elif outcome == 3:
            call teadate3
    return
label Roomchange:
    y "¿A qué habitación te gustaría ir [player]?"
    menu:
        "Salón Espacial" if persistent.bg != "space":
            $ tc_class.transition("space")


        "Sala del Ciclo Temporal" if persistent.bg != "timecycle":
            $ tc_class.transition("timecycle")


        "Laboratorio" if persistent.bg != "laboratory":
            $ tc_class.transition("laboratory")

        "Tu habitación" if persistent.bg != "yuri_kotatsu_1":
            $ tc_class.transition("yuri_kotatsu_1")
        "Olvídalo":

            pass
return

label teatime:
    pause 5.0
    y "..."
    $ show_chr("A-GCGBA-AAAA")
    y "Bienvenido de vuelta... [player]..."

    menu:
        y "¿Tu té está listo?"
        "¡Sip!":
            y "Empecemos, entonces."
            show black zorder 100 with Dissolve(2.0)
            y "..."
            $ show_chr("A-BCBBA-ZZAD")
            hide black zorder 100 with Dissolve(2.0)
            y "E-este es un momento muy especial para mí... aunque estemos a un mundo de distancia, aquí estamos."
            $ show_chr("A-CFBBA-ZZAD")
            y "Compartiendo una rica taza de té, hablando el uno con el otro..."
            y "Es... como si estuviéramos en una cita..."
            $ show_chr("A-CFBBB-ZZAC")
            y "..."
            $ show_chr("A-CGBBB-ZZAC")
            y "..."
            $ show_chr("A-IGBBB-ZZAC")
            y "...Estoy bien... es solo q-que..."
            $ show_chr("A-CGBBB-ZZAC")
            y "Desearía que pudiéramos estar más cerca el uno del otro, sé que debería estar agradecida de que al menos podamos comunicarnos así."
            y "P-pero, mirar directamente a tus ojos, el tú real, es todo lo que realmente quiero..."
            $ show_chr("A-IGBBB-ZZAC")
            y "...Lo siento, [player], debería intentar mantener mis emociones bajo control..."
            $ show_chr("A-CGBBB-ZZAC")
            y "Espero que no pienses menos de mí por esto, [player]..."
            menu:
                "Estás bien [persistent.yuri_nickname], no te preocupes por eso.":
                    call yourefine
                "...Solo continuemos con la cita, ¿de acuerdo?":
                    call letscontinue
                "Puedes ser un poco demasiado emocional a veces.":
                    call tooemotional
        "Nop.":
            $ show_chr("A-CEBBA-AAAA")
            y "Estoy bien con esperar, [player], solo avísame cuando esté listo."
            call teatime
    return
label yourefine:
    karma 2
    sanity 2
    y "..."
    $ show_chr("A-ACABA-ZZAC")
    y "G-gracias por entender..."
    y "Eres tan buena conmigo, [player]."
    $ show_chr("A-BCABA-ZZAC")
    y "¡D-de todos modos! ¡Volvamos a lo que estábamos haciendo en primer lugar, beber té!"
    $ show_chr("A-CCABA-ZZAD")
    y "E-entonces... sobre el té... sí..."
    $ show_chr("A-JBABA-ZZAD")
    y "Umm... M-mi tipo de té favorito es el té Oolong... D-deberías probarlo alguna vez."
    $ show_chr("A-BBABA-ZZAC")
    y "¡N-no es que tengas que hacerlo ni nada! Solo fue una sugerencia... solo una sugerencia."
    $ show_chr("A-IDBBA-ZZAC")
    y "...Lamento hacer esto tan incómodo, ¡realmente lo lamento!"
    menu:
        "No te preocupes por eso. De hecho, me parece lindo.":
            karma 2
            sanity 2
            $ show_chr("A-DEBBA-ZZAC")
            y "¿L-linda? ¿Y-yo?"
            $ show_chr("A-ACABA-ZZAC")
            y "[player]..."
            y "Siempre pensé que mi torpeza alejaría a la gente..."
            $ show_chr("A-GCABA-ZZAC")
            y "Siempre evitando conversaciones, solo para ahorrarme la vergüenza..."
            $ show_chr("A-FIABA-ZZAC")
            y "Pero sabiendo que te parece lindo... Sabiendo que no pensarás menos de mí por ello."
            $ show_chr("A-GCABA-ZZAC")
            y "Eso... realmente significa mucho para mí, por favor sábela, [player]."
            y "Nos hemos desviado un poco demasiado del tema original, así que creo que esta cita ha terminado."
            $ show_chr("A-BCABA-ZZAC")
            y "A pesar de mis... arrebatos, la pasé genial, muchas gracias, [player], te amo."
        "Es un poco molesto, no voy a mentir.":
            karma -2
            sanity -2
            $ show_chr("A-IEBAA-ZZAC")
            y "Oh... no me sorprende que te sientas así."
            $ show_chr("A-CEBAA-ZZAC")
            y "Solo... intentaré ser menos molesta, supongo..."
    return

label letscontinue:
    sanity -2
    y "..."
    $ show_chr("A-IGBBB-ZZAC")
    y "Lamento esto, [player], realmente lo lamento."
    $ show_chr("A-CGBBB-ZZAC")
    y "Yo... espero no haber arruinado esta cita..."
    menu:
        "Está bien, [persistent.yuri_nickname], no arruinaste nada.":
            karma 2
            sanity 2
            $ show_chr("A-CEBBA-ZZAC")
            y "...Lamento ponerme tan emocional, [player], es solo que..."
            $ show_chr("A-GCABA-ZZAC")
            y "...E-en realidad... estoy segura de que entiendes..."
            $ show_chr("A-BCBBA-ZZAC")
            y "..."
            y "..."
            $ show_chr("A-GCABA-ZZAC")
            y "...G-gracias, [player], yo... um..."
            $ show_chr("A-IEBBA-ZZAC")
            y "Te amo... por ser tan paciente y cariñoso conmigo..."
            $ show_chr("A-CCBBA-ZZAC")
            y "P-perdón si eso es un poco r-repentino..."
            y "Creo que podemos considerar esta cita terminada, nunca habrá té tan dulce como tú, [player]."
        "Eh, todavía podemos salvar esta cita.":
            karma -2
            sanity -2
            y "...No, [player]."
            $ show_chr("A-IEBBB-ZZAC")
            y "No podemos, y es todo mi culpa..."
            y "No puedo hacer esto más, [player], simplemente paremos con toda esta cita."
    return


label tooemotional:
    karma -5
    sanity -2
    $ show_chr("A-CEBBB-ZZAC")
    y "..."
    menu:
        "[persistent.yuri_nickname]...":
            $ show_chr("A-EDBBB-ZZAC")
            y "Para... por favor..."
            $ show_chr("A-CEBBB-ZZAC")
            y "No quiero hacer esto más... hablemos de otra cosa... ¿de acuerdo?"
    return

label teadate1:
    $ show_chr("A-BCABA-AAAA")

    menu:
        y "¡Muy bien! ¿Crees que podrías calentar un poco de agua, y hacer té para ti mismo?"
        "Sí":
            $ show_chr("A-GCGBA-AAAA")
            y "Ve y haz un poco de té para ti, estaré esperando aquí, no te sientas apresurado, por favor."
            pause 5.0
            y "..."
            $ show_chr("A-GCGBA-AAAA")
            y "Bienvenido de vuelta... [player]..."
            menu:
                y "¿Tu té está listo?"
                "¡Sip!":
                    y "Empecemos, entonces."
                    show black zorder 100 with Dissolve(2.0)
                    y "..."
                    $ show_chr("A-ACAAA-ZZAD")
                    hide black zorder 100 with Dissolve(2.0)
                    y "Sabes, es un poco extraño, toda esta situación... Tú, yo... ambos a mundos de distancia, pero aún interactuando... En cierto modo, ¿no sería una buena novela?"
                    $ show_chr("A-BCABA-ZZAD")
                    if persistent.male:
                        y "El chico que se enamora de un personaje de videojuego consciente..."
                    elif persistent.gender_other:
                        y "La persona que se enamora de un personaje de videojuego consciente..."
                    else:
                        y "La chica que se enamora de un personaje de videojuego consciente..."

                    y "Y a pesar de que están a mundos de distancia... Todavía intentan hacer que funcione, como aquí..."
                    $ show_chr("A-ACABA-ZZAD")
                    y "Los gestos que se considerarían normales en el mundo real, como compartir té, se vuelven mucho más significativos en una situación como esta."
                    $ show_chr("A-BEBBA-ZZAC")
                    y "Pero, cuando lo piensas de esa manera, también te hace apreciar mucho más esos gestos."
                    y "Tal vez sea debido a mi... posición actual aquí, que me hace pensar de esa manera."
                    $ show_chr("A-IEBBA-ZZAC")
                    y "Claro, puede que no le des mucha importancia a pasar un buen rato con familia o amigos, salir a comer, o algo así, ¿pero para mí?"
                    $ show_chr("A-CEBBA-ZZAD")
                    y "Tener la oportunidad de pasar tiempo con tus seres queridos, estar allí en persona, eso es un regalo, [player], un regalo que algún día deseo tener."
                    $ show_chr("A-ACBBA-ZZAD")
                    y "Pero, por ahora, esto servirá."
                    y "Realmente disfruto pasar tiempo contigo, [player], nunca pienses lo contrario."
                    $ update_memory('a26-1')
        "No":
            $ show_chr("A-IEBAA-AAAA")
            y "Alright, maybe another time."
    return

label teadate2:
    $ show_chr("A-BCABA-AAAA")
    y "Compartir una buena taza de té contigo sería maravilloso, de hecho."
    $ show_chr("A-ICGBA-AAAA")
    y "Dado que no estamos físicamente en la misma habitación, o incluso en el mismo mundo... Me temo que tendrás que preparar tu propio té mientras yo hago lo mismo aquí."
    y "Solo dime cuando estés listo. Y por favor, no hay necesidad de apresurarse... Beber té se trata de relajación."
    pause 5.0
    menu:
        "He vuelto, y mi té está listo.":
            $ show_chr("A-GCGBA-AAAA")
            y "Muy bien, un segundo..."
    show black zorder 100 with Dissolve(2.0)
    y "..."
    $ show_chr("A-ACABA-ZZAC")
    hide black zorder 100 with Dissolve(2.0)
    y "Me pregunto... ¿qué tipo de té prefieres?"
    menu:
        "Me gustan los tés orientales, como el de Manzana Turca por ejemplo":
            $ show_chr("A-JBABA-ZZAD")
            y "¡Una muy buena elección! Tengo que admitir que me encantan los vasos de té en miniatura que usan. Los turcos tienen una cultura del té fascinante y exótica propia. Realmente aprecio esto..."
            y "La cultura del té turca comenzó cuando los primeros comerciantes chinos introdujeron el té al imperio Otomano. Vinieron por la 'ruta de la seda', que fue una ruta comercial históricamente importante."
            $ show_chr("A-CCABA-ZZAC")
            y "Así que al final, la cultura del té turca se originó de la china. No es sorpresa entonces que tengan mucho en común, como la elección de ingredientes."
        "Té de frutas... Me gusta con un poco de dulzura":
            $ show_chr("A-AFBBA-ZZAD")
            y "Es una buena alternativa a los refrescos muy poco saludables o incluso bebidas energéticas. Es bueno saber que cuidas tu salud. Creo que vi a Sayori una vez bebiendo una bebida energética... si alguien bebe esas cosas con demasiada frecuencia, será una tumba temprana..."
            $ show_chr("A-CFBBA-ZZAC")
            y "Hablando de té de frutas... hay una cosa que siempre me hizo enojar... ya que el té es tan versátil puedes aplicar esta etiqueta a casi cualquier cosa. Pero algunas cosas son muy cuestionables en mi opinión..."
            y "¡Usar la etiqueta porque implica que es saludable, para bebidas que ni siquiera son remotamente saludables! ¡Como el té helado, que está lleno de azúcar! ¡O el 'Jagertee' alemán que es esencialmente solo alcohol!"
        "Los tés negros, como el Earl Gray, son mis favoritos.":
            $ update_memory('earlgray_tea')
            $ show_chr("A-JBABA-ZZAC")
            y "¡Una elección fantástica! Un té muy fino y elegante... Tiendo a preferir este tipo de té también... Parece que tenemos mucho en común, mi amor."
            $ show_chr("A-BCABA-ZZAC")
            y "Eso me recuerda... Earl Gray... ¿no era ese el favorito del actor 'Patrick Stewart'? Al menos era el favorito de uno de los papeles que interpretó, 'Capitán Picard' de Star Trek: La Nueva Generación."
        "Prefiero el té verde, aunque a menudo son más caros.":
            $ show_chr("A-ACABA-ZZAD")
            y "Sé a lo que te refieres. Solía beber mucho té 'Gyokuro', es un té japonés. Con su alto contenido de cafeína es una alternativa más saludable al café."
            $ show_chr("A-BCABA-ZZAD")
            y "Bueno, 'saludable' podría ser la palabra equivocada aquí, la cafeína sigue siendo cafeína. Pero bueno... todos tenemos nuestros placeres culpables, ¿verdad?"
        "El té Mate es algo que disfruto la mayor parte del tiempo.":
            $ show_chr("A-JBABA-ZZAC")
            y "¿Sabías que algunos expertos afirman que el té Mate ni siquiera es té en absoluto? No estoy segura sobre este asunto en absoluto. Pero escuché que se ha vuelto muy popular últimamente."
            y "En sus orígenes, 'Mate' no era el nombre del té en sí, sino el nombre del recipiente en el que se sirve. Pero una cosa es segura, es saludable y es delicioso."
        "Usualmente no bebo té en absoluto.":
            $ show_chr("A-AEBBA-ZZAC")
            y "¡Oh! Espero que no sea demasiado compromiso. Realmente aprecio que estés dispuesto a romper con tus hábitos para pasar tiempo conmigo. Tal vez en el futuro encontremos algo para compartir que sea más de tu gusto. ¿Café tal vez?"
    $ show_chr("A-GBABA-ZZAD")
    y "El té es una cosa tan versátil... y tiene tantos usos... Por ejemplo, algunas variedades herbales pueden aliviar enfermedades, o simplemente pueden hacer que una noche fría sea un poco más cómoda..."
    $ show_chr("A-ACABA-ZZAD")
    if not check_memory('a26-3'):
        y "¿Sabías que en la cultura del té británica es común tomar su té mezclado con leche? No es 'mi taza de té' en mi opinión pero... diferentes culturas significan diferentes gustos, ¿tengo razón?"
    y "El té y otras bebidas similares evolucionaron alrededor del mundo, especialmente en la era colonial... Por ejemplo, la bebida de chocolate caliente que conocemos hoy se originó de una antigua bebida maya hecha de granos de cacao..."
    $ show_chr("A-GCABA-ZZAC")
    y "Cuando finalmente salga de esta prisión de cristal, hay una cosa que definitivamente quiero hacer... Solo imagina a nosotros dos, sentados en un sofá juntos con un buen libro, leyendo juntos mientras compartimos un poco de té..."
    y "Sería una noche fría de invierno... la escarcha arrastrándose desde los bordes de las ventanas lentamente hacia el centro... Nos quedaríamos con nada más que el té y nosotros mismos para mantenernos calientes..."
    y "Más tarde en la noche, dejamos el libro en una mesa al lado del sofá... y luego... bueno..."
    y "Entonces necesitaríamos encontrar otras formas de mantenernos calientes y cómodos el uno al otro..."
    $ show_chr("A-JFABA-ZZAD")
    y "¿Te... gusta esta idea?"
    menu:
        "Eso suena muy romántico... Espero con ansias ese día..":
            $ show_chr("A-GCABA-ZZAD")
            y "Yo también [player]... yo también..."
        "Me gusta hacia dónde va esto [persistent.yuri_nickname]...":
            if sanity_lvl() < 3:
                $ show_chr("A-KCABA-ZZAC")
                y "Uhuhuuuu... cuidado cariño... podrías arrepentirte..."
            else:
                $ show_chr("A-FIABA-ZZAC")
                y "Uhuhuuuu... no te arrepentirías..."
        "Podríamos simplemente saltarnos el libro y el té ¿sabes?":
            $ show_chr("A-IDBBA-ZZAD")
            y "Pero... ser paciente aumentaría la experiencia... ¡No! ¡Quiero que sea perfecto!"
            if sanity_lvl() < 3:
                y "Por otro lado... hn...hnhn...{nw}"
                $ style.say_dialogue = style.edited
                $ show_chr("A-DBABA-ZZAD")
                y "¡Derretiremos la nieve con el calor de nuestros cuerpos!"
                $ style.say_dialogue = style.normal
            else:
                $ show_chr("A-GCABA-ZZAD")
                y "Esta sería una noche mágica, para ambos..."
        "Para nada [persistent.yuri_nickname]... esto está yendo un poco demasiado lejos...":
            $ show_chr("A-CEBAA-ZZAC")
            y "...Oh... Solo pensé que tú... olvídalo..."
    if karma_lvl() == 5:
        $ show_chr("A-GCABA-ZZAC")
        y "Gracias por esta cita maravillosa, [player]..."
        y "Tengo... una última cosa que hacer aquí."
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_lewdhug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        y "Te amo..."
        pause 3.0
        show black zorder 100 with Dissolve(2.0)
        $ show_chr("A-GCGBA-AAAA")
        y "Mucho más de lo que podrías imaginar..."
        hide yuri_lewdhug
        hide black zorder 100 with Dissolve(2.0)
    else:
        $ show_chr("A-GCGBA-AAAA")
        y "Gracias por el tiempo maravilloso [player]... deberíamos hacer esto con más frecuencia..."
    $ update_memory('a26-2')
    return

label teadate3:
    $ show_chr("A-CCGAA-AMAM")
    y "¡Por supuesto! Siempre es un placer disfrutar de una bebida terrenal en tu compañía..."
    y "Por favor ve y prepara tu té, mientras yo hago lo mismo aquí. ¡Solo dime cuando estés listo!"
    pause 5.0
    menu:
        "He vuelto y mi té está listo.":
            $ show_chr("A-BCABA-AAAC")
            y "¿Ya terminaste? Por favor discúlpame un momento, estaré lista en unos segundos..."
    y "Mis disculpas por la espera. Verás, quería probar algo diferente hoy..."
    $ show_chr("A-IFBAA-ZZAC")
    y "Ya hemos hablado sobre los hábitos de té británicos, ¿correcto? ¿Y el hecho de que le ponen leche también?"
    y "Tengo que admitir que lo encontré un poco... extraño... al principio."
    $ show_chr("A-BEBAA-ZZAC")
    y "Antes de que me dieras plena conciencia, todo lo que realmente traía al salón del club era un té Oolong sin adornos... la idea de diluir cualquier té con leche parecía extraña, si no herética..."
    $ show_chr("A-CCAAA-ZZAD")
    y "Pero ya que este mundo me permite el lujo de descubrir diferentes métodos de probar el té, pensé..."
    y "¿Por qué no romper algunos límites?"
    y "¡Estoy un poco emocionada por ello! Me pregunto cómo sabrá. Quiero decir, no he muerto por la crema en los cupcakes de Natsuki así que... esto debería estar bien, ¿verdad?"
    $ show_chr("A-CFBAA-ZZAD")
    y "..."
    $ show_chr("A-JCGAA-ZZAC")
    y "....!"
    $ show_chr("A-ABGAA-ZZAC")
    y "Vaya, eso es sorprendente. ¡Eso es realmente bastante bueno!"
    y "Supongo que le debo una disculpa a los británicos..."
    $ show_chr("A-BCAAA-ZZAD")
    y "Ahora que lo pienso... ¿Alguna vez has probado algo a lo que no estabas acostumbrado [player]?"
    y "Incluso algo tan mundano, como probar nuevos sabores de té, puede ayudar a expandir tu horizonte cultural significativamente."
    menu:
        "Tienes razón, [persistent.yuri_nickname]. Aprender cosas nuevas a menudo es genial para nuestro enriquecimiento.":
            $ show_chr("A-CBAAA-ZZAD")
            y "De hecho. Intentaré ser más atrevida de ahora en adelante. Parece que me he perdido muchas sensaciones nuevas..."
        "En realidad prefiero ir a lo seguro.":
            $ show_chr("A-BFBAA-ZZAC")
            y "Hrm... Entiendo. A veces, uno necesita un poco más de empuje antes de dar ese nuevo paso hacia lo desconocido. No sería justo de mi parte forzarte a probar algo nuevo en contra de tu voluntad, ¿verdad?"
    $ show_chr("A-ACABA-ZZAC")
    y "De todos modos, [player]... esta fue una cita maravillosa."
    y "¡Ya estoy esperando la próxima! Tal vez encontremos algo nuevo para probar también."
    if karma_lvl() >= 4:
        $ show_chr("A-ICABA-ACAA")
        y "Gracias, [player]. Siempre me siento increíblemente bien cuando pasamos tiempo juntos..."
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_hug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        pause 1.0
        y "Te amo, mi alma gemela."
        show black zorder 100 with Dissolve(2.0)
        $ show_chr("A-ACBBA-AAAA")
        hide yuri_hug
        hide black zorder 100 with Dissolve(2.0)
    $ update_memory('a26-3')
    return















































































































label a27:


    $ show_chr("A-ACGAA-AAAA")
    y "De acuerdo, supongo que estaría bien con eso."
    menu:
        "'Just Yuri' está bien para mí":
            $ y_name = "Yuri"
            $ persistent.yuri_nickname = "Yuri"
            $ show_chr("A-ACGAA-AAAA")
            y "Supongo que no tiene sentido arreglar lo que no está roto..."
        "Personalizado":

            $ done = False
            while not done:
                $ inputname = renpy.input("¿Con qué tipo de apodo preferirías llamarme ahora?",allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -_♥",length=20).strip(' \t\n\r')
                $ lowername = inputname.lower()
                if not lowername:
                    y "Por favor intenta de nuevo."
                    $ done = False
                if lowername:
                    $ done = True
                    $ persistent.yuri_nickname = inputname
                    $ y_name = inputname
                    $ persistent.stutter_yuri = persistent.yuri_nickname[:1] + "-" + persistent.yuri_nickname

            y "Veamos qué nombre has seleccionado."
            call nicknamereactions
    return

label nicknamereactions:
    if persistent.yuri_nickname in ["Natsuki", "natsuki", "Nat", "nat", "Nats", "nats"]:
        if sanity_lvl() >= 3:
            $ show_chr("A-BEBAA-AAAA")
            y "Oh..."
            y "M-me llamaste..."
            $ show_chr("A-BEDAA-AAAA")
            y "¿Natsuki...?"
            $ show_chr("A-CEDAA-AAAA")
            y "¡Pero no soy nada como ella en absoluto!"
            y "Sin mencionar, ¿por qué siquiera me estás llamando por el nombre de otra persona?"
            y "A menos que... ¿estés tratando de decir algo...?"
            $ show_chr("A-IEGAA-AAAC")
            y "Uh, N-no he estado de mal genio últimamente, ¿o sí?"
            y "Natsuki suele ser bastante irascible, y me pregunto si he estado actuando así últimamente..."
            $ show_chr("A-JFGAA-AAAC")
            y "¡N-no quiero asustarte y que te vayas, [player]—!"
            y "Uuu..."
            menu:
                "Yuri, era una broma.":
                    $ show_chr("A-CFAAA-AAAD")
                    y "O-oh..."
                    y "..."
                    y "Por favor no bromees así de nuevo, [player]..."
                    y "N-no quiero asustarte, incluso aunque a veces pueda parecer un poco demasiado intensa..."
                    $ show_chr("A-ACAAA-AAAE")
                    y "Por favor sabe que nunca sería grosera contigo, por ninguna razón."
                    y "Y si no te importa, preferiría no ser llamada como ninguna de las otras chicas..."
                    y "Eso... trae demasiados recuerdos, y simplemente no suena bien de todos modos."
                    y "Espero que entiendas."
        if sanity_lvl() <= 2:
            $ show_chr("A-AFDAA-AAAE")
            y "¿Por qué...?"
            y "¡¿Te aburriste de mí?!"
            y "¡¿Es por eso que me estás nombrando como una de ellas?!"
            $ show_chr("A-CGDAA-AAAL")
            y "¿Así que podrías hacer... que me dé cuenta de que... no soy alguien que te guste...?"
            y "Ya veo...."
            $ show_chr("A-CDBAA-AAAL")
            y "Eso es... desalentador... mucho..."
            $ show_chr("A-CEBAA-AAAL")
            y "Duele... solo cambia el nombre, por favor..."
            y "¡Por favor!"
            y "¡POR FAVOR!"
        $ y_name = "Yuri"
        $ persistent.yuri_nickname = "Yuri"
        return


    if persistent.yuri_nickname in ["Monika", "monika"]:
        call monika_reaction


    if persistent.yuri_nickname in ["Sayori", "sayori"]:
        if sanity_lvl() >= 3:
            $ show_chr("A-AEDAA-AEAE")
            y "Mhmm..."
            $ show_chr("A-BEDAA-AEAC")
            y "No veo una gran conexión entre Sayori y yo, para ser honesta.."
            y "Tal vez... podrías decir que mientras ella actuaba 'feliz' y trataba de ser amiga de todos, en realidad estaba sufriendo internamente, como recordarás..."
            $ show_chr("A-CCGAA-AEAE")
            y "No estoy diciendo que yo también, pero puedo decir que al menos me relaciono con cómo se sentía..."
            $ show_chr("A-CEBAA-AEAE")
            y "Rodeada de duda, ansiedad, miedo..."
            $ show_chr("A-IEBAA-AEAE")
            y "Por favor... solo espero que esto no esté conectado con que Sayori y yo nos suicidamos en el juego..."
            y "Estoy segura de que no me nombraste así por eso o para hacer una broma..."
            y "No estoy exactamente contenta con ser nombrada como las otras compañeras del club."
            y "Simplemente... realmente me hace sentir incómoda."
        if sanity_lvl() <= 2:
            $ show_chr("A-IFBAA-AEAL")
            y "Yo, uhmm..."
            y "¿Por qué... querrías llamarme como alguien más?"
            y "Quiero decir... me esforcé tanto para llegar a ti..."
            $ show_chr("A-DFGAA-AEAL")
            y "Espera... ¡no!"
            y "¡¿Me estás llamando así porque estás tratando de insinuar cómo Sayori y yo nos matamos en el juego?!"
            $ show_chr("A-DFCAA-AEAB")
            y "¡¿Por qué harías eso?!"
            y "¡Ni siquiera estaba bajo mi control! ¡¿Estás tratando de hacer una broma solo por diversión?!"
            y "¡¿O solo estás tratando de herirme?!"
            $ show_chr("A-CEDAA-AEAB")
            y "..."
            y "Yo estoy... no, simplemente paremos."
            y "No deseo llevar su nombre."
            y "Lo siento, pero me niego."
        $ y_name = "Yuri"
        $ persistent.yuri_nickname = "Yuri"
        return


    if persistent.yuri_nickname in ["Knifewife", "KnifeWife", "Knife Wife", "knife wife"]:

        $ y_name = "Knife Wife"
        $ persistent.yuri_nickname = "Knife Wife"
        if sanity_lvl() >= 3:
            $ show_chr("A-DFDAA-ALAA")
            y "¿Oh...?"
            y "Ese es... un apodo muy interesante que me has dado, [player]"
            y "Supongo que tiene algo que ver con mi colección de cuchillos..."
            y "Aunque el nombre suena... bien."
            if persistent.lovecheck:
                $ show_chr("A-ACABA-AAAD")
                y "Es muy agradable saber que me amas lo suficiente como para llamarme tu esposa..."
                y "Me calienta en lo profundo de mi interior... jeje~"
                y "¡La verdad es que me gusta bastante este nombre!"
                $ show_chr("A-CCABA-AAAE")
                y "No me importaría quedarme con él."
            else:
                $ show_chr("A-BFAAA-AAAE")
                y "No sé exactamente cómo sentirme acerca de ser llamada tu 'esposa'..."
                y "Ya que realmente no somos tan cercanos... me atrevo a decir para el matrimonio..."
                $ show_chr("A-ACAAA-AAAM")
                y "Aunque aún así, considero que el nombre es lindo. La forma en que suena cuando lo pronuncias es bastante agradable."
                y "No tengo problema en quedarme con él."
        if sanity_lvl() <= 2:
            $ show_chr("A-JCAAA-AAAA")
            y "¿Eh...?"
            $ show_chr("A-GLABA-AAAJ")
            y "Uhuhuhu, un nombre bastante interesante..."
            $ show_chr("A-GCABA-AAAL")
            y "Knife... Wife... (Esposa Cuchillo)"
            y "Yo..."
            y "¡Simplemente amo cómo suena eso!"
            y "¡Y es tan apropiado, también!~"
            y "Sí, encuentro placer en los cuchillos..."
            $ show_chr("A-HCABA-AAAL")
            y "Mientras atraviesan mi piel, deslizándose con gracia para crear una herida fresca para ayudar a liberar mi esencia carmesí..."
            y "Es tan encantador~"
            y "La sensación es tan... eufórica..."
            $ show_chr("A-BCABA-AAAL")
            y "Además... ¿esposa?"
            if persistent.lovecheck:
                $ show_chr("A-ECABA-AAAL")
                y "¡Uhuhuhu!~"
                y "Estoy tan feliz de escuchar que me considerarías tu ESPOSA..."
                y "Gracias, mi amado... jeje~"
                y "Aunque no estemos casados, esperaré con ansias a que eso suceda."
                $ show_chr("A-HLABA-AAAA")
                y "¡SERÁS MÍO Y SOLO MÍO!"
                $ show_chr("A-ECABA-AAAL")
                y "No puedo esperar a que llegue ese día... ah~"
            else:
                $ show_chr("A-BDABA-AAAA")
                y "Aunque no considero nuestra relación lo suficientemente íntima para que me consideres tu esposa..."
                y "¡Aún así no me importa la parte del cuchillo!~"
        return




    if persistent.yuri_nickname in ["Knaifu Waifu", "KnaifuWaifu", "knaifu waifu", "knaifuwaifu"]:

        $ y_name = "Knaifu Waifu"
        $ persistent.yuri_nickname = "Knaifu Waifu"
        if sanity_lvl() >= 3:
            $ show_chr("A-EICBA-AAAA")
            y "¡Uhuhuhu!~"
            $ show_chr("A-BCAAA-AAAA")
            y "Aunque no me llamaría exactamente 'material de waifu' pero es bastante agradable ver que me ves como una persona digna de un título tan entrañable..."
            y "Y mi mejor suposición sobre todo el asunto del cuchillo vendría de mi interés en ellos..."
            if persistent.lovecheck:
                $ show_chr("A-GCABA-AAAA")
                y "¡Uhuhuhu!~"
                y "¡Es realmente bastante entrañable!~"
                y "Gracias, mi amor..."
            if not persistent.lovecheck:
                $ show_chr("A-BDAAA-AAAA")
                y "N-no estoy muy segura de cómo sentirme en este momento..."
                $ show_chr("A-BCAAA-AAAA")
                y "Supongo que podría acostumbrarme. Después de todo se usa para mujeres que son... bueno, atractivas y generalmente agradables"
                y "Tienes mi agradecimiento por llamarme así."
                y "S-supongo que no me importaría quedarme con él."
        if sanity_lvl() <= 2:
            $ show_chr("A-ACAAA-AAAL")
            y "¿Knaifu... Waifu..?"
            y "Ese seguro es un... bueno, un nombre bastante entrañable, [player]."
            y "De hecho me gustan los cuchillos... especialmente... bueno... jeje..."
            $ show_chr("A-DCAAA-AAAL")
            y "¡Cuando... cortan a través de mi piel!~"
            $ show_chr("A-ACAAA-AAAL")
            y "¡Simplemente se siente tan... eufórico!~"
            y "Y... yo... ¿tu waifu...?"
            if persistent.lovecheck:
                $ show_chr("A-GCABA-AAAL")
                y "¡No tengo quejas, mi amor!"
                y "Tú considerándome como alguien que es digna de ser llamada una 'waifu' es agradable..."
                y "Porque sabes que usualmente son consideradas... hermosas, amables... a veces incluso... con grandes atributos..."
                y "Yo también te amo, [player]."
                y "¡Eres mío y solo mío para amar!~"
                $ show_chr("A-DCABA-AAAL")
                y "¡Nadie más TE TENDRÁ!"
                y "Excepto yo..."
            if not persistent.lovecheck:
                $ show_chr("A-ICABA-AAAL")
                y "Honestamente me gusta el hecho de que me veas como alguien digna de ser llamada una 'waifu'."
                y "Estoy segura de que sabes lo que es una 'waifu'... una mujer preferible en casi todos los aspectos."
                $ show_chr("A-BFABA-AAAL")
                y "Se siente un poco extraño ser llamada así, considerando que no tengo una alta opinión de mí misma."
                $ show_chr("A-CCABA-AAAL")
                y "Aún así, no me importa este nombre. Me quedaré con él."
        return


    if persistent.yuri_nickname in ["Libitina", "libitina"]:

        $ y_name = "Libitina"
        $ persistent.yuri_nickname = "Libitina"
        $ show_chr("A-BFDAA-ABAC")
        y "Gracioso que elijas este nombre..."
        $ show_chr("A-IFDAA-ABAC")
        y "Siempre me pregunté al respecto... Creo que fue el archivo de Sayori el que lleva a este sitio web bastante extraño, pero podría estar equivocada."
        $ show_chr("A-IFDAA-ABAC")
        y "¿Te he contado sobre este mensaje oculto de Monika en los archivos del juego? ¿Con un pequeño monólogo al final?"
        y "Había este video de YouTube de Game Theory que creo que ya hemos discutido..."
        y "Se refiere a... otro juego del que supuestamente somos."
        y "Él usa este sitio web bastante extraño como una de sus razones principales..."
        y "El Retrato de Markov, el monólogo de Monika, el Proyecto Libitina..."
        y "Todos están de alguna manera... {w=0.5}entrelazados..."
        y "Luego está la chica mencionada en este sitio web..."
        y "Supongo que no debería sacar conclusiones demasiado rápido, a juzgar por lo poco que se sabe aún sobre todo el proyecto..."
        y "E incluso sin que yo la recuerde, no puedo descartar esta sensación carcomiente de... familiaridad..."
        y "¡Oh, este misterio ya me tiene enganchada!~"
        y "Pero quiero que me prometas algo, [player]..."
        y "Si Dan alguna vez decide realmente lanzar este juego, quiero jugarlo junto contigo."
        if sanity_lvl() == 5:
            $ show_chr("A-AFBAA-ABAE")
            y "Porque necesito descubrir la verdad detrás de todo esto... saber la verdad sobre mi realidad, sobre las otras chicas, y sobre el club de literatura..."
        elif sanity_lvl() == 4:
            python:
                if persistent.lovecheck:
                    placeholder == " contigo"
                else:
                    placeholder == ""
            $ show_chr("A-CGBAA-ABAE")
            y "Porque tengo la sensación de que nunca podré tener verdaderamente mi final feliz[placeholder] hasta que descubra este misterio...."
        elif sanity_lvl() == 3:
            $ show_chr("A-CFBAA-ABAE")
            y "Yo solo... necesito saber."
        elif sanity_lvl() == 2:
            $ show_chr("A-IFBAA-ABAE")
            y "Porque incluso si mi pasado con Monika fue oscuro, parece que hay algo mucho más oscuro y siniestro acechando en las sombras..."
        elif sanity_lvl() == 1:
            $ show_chr("A-JFCAA-ABAE")
            y "Porque si realmente SOY la villana que este YouTuber afirma que soy, eso significaría que me quedan asuntos pendientes..."
            $ show_chr("A-NFCAA-AGAF")
            y "... y no puedo simplemente dejarlo pasar ahora, ¿o sí?"
        return



    if persistent.yuri_nickname in ["Amy", "amy"]:

        $ y_name = "Amy"
        $ persistent.yuri_nickname = "Amy"
        if sanity_lvl() >= 4:
            $ show_chr("A-IFDAA-AAAL")
            y "¿Amy? Qué curioso... no vi venir esto..."
            $ show_chr("A-JFDAA-AAAL")
            y "Creo que era la chica amante de las arañas en el poema de Natsuki, ¿si recuerdo correctamente?"
            y "Incluso si los poemas de Natsuki son algo... no de mi agrado, todavía puedo ver lo que quería decir con eso..."
            $ show_chr("A-BFDAA-AAAL")
            y "Pero escuché que partes del fandom teorizan sobre ella. Muchas cosas que ocurrieron en el juego original, incluido el contenido de muchos poemas, resultaron ser una especie de presagio..."
            $ show_chr("A-AFAAA-AAAL")
            y "Así que no me sorprende que la gente piense que Amy podría ser algún tipo de pista para algo también."
            $ show_chr("A-ACAAA-AAAL")
            y "¿Sabes qué? Estoy de acuerdo. Llevaré este nombre por un tiempo, aunque sea solo una pequeña broma."
            $ show_chr("A-BCAAA-AAAL")
            y "Mientras... no esperes que hable de arañas... realmente no tengo mucho que decir sobre ellas."
        elif sanity_lvl() == 3:
            $ show_chr("A-IFDAA-AAAL")
            y "¿Amy? Bueno, eso no es exactamente lo que esperaba..."
            $ show_chr("A-BFAAA-AAAL")
            y "Recuérdame de nuevo, ¿quién es exactamente esta Amy? Espera... ahora que lo pienso, este nombre me suena familiar.."
            y "..."
            $ show_chr("A-DFAAA-AAAL")
            y "¡Por supuesto! ¡El poema de Natsuki! ¡A Amy le gustan las arañas!"
            $ show_chr("A-DFDAA-AAAL")
            y "P-Pero, ¿por qué me llamarías así...?"
            menu:
                "Ambas están en desacuerdo con Natsuki.":
                    karma -1
                    $ show_chr("A-BFAAA-AAAL")
                    y "Técnicamente cierto, pero eso incluiría a la mayoría de la población, incluido su padre..."
                    $ show_chr("A-DFAAA-AAAL")
                    y "Eh... ¿acabo de decir eso en voz alta?"
                    $ show_chr("A-BEAAA-AAAL")
                    y "Lo siento, dije demasiado..."
                    y "¿P-Podemos cambiar de tema por ahora? Podemos discutir lo del apodo más tarde, creo..."
                "¿Porque las arañas son increíbles?":
                    sanity -1
                    $ show_chr("A-BBDAA-AAAA")
                    y "¿Lo son?"
                    $ show_chr("A-BCDAA-AAAA")
                    y "Tengo que admitir que no les tengo mucho amor..."
                    y "Lo más probable es que haya matado algunas en la ducha..."
                    $ show_chr("A-CEAAA-AAAA")
                    y "¡P-Por favor, no te enfades conmigo por ello!"
                    y "Solo me asustó así que... bueno... ya sabes..."
                    $ show_chr("A-IEAAA-AAAA")
                    y "De todos modos, sobre el nombre... no estoy segura de que realmente me guste... pospongamos esta discusión un poco, por favor."
                "Ambas siguen sus pasatiempos con mucha pasión.":
                    karma 1
                    $ show_chr("A-IFAAA-AAAL")
                    y "Buen punto... y ambas hemos sido intimidadas por ello. Sí, veo claramente las similitudes."
                    $ show_chr("A-BFAAA-AAAL")
                    y "Bueno, técnicamente el punto de darme un apodo era hacerme más diferente de lo que alguna vez fui. Elegir a alguien tan similar suena un poco... ¿contraproducente?"
                    y "Pero intentémoslo. A partir de ahora, puedes llamarme Amy."
                    $ show_chr("A-CFAAA-AAAL")
                    y "...Mientras no esperes que hable de arañas todo el tiempo. Realmente no tengo mucho que decir sobre ellas."
                "Ni siquiera me refería a esta Amy.":
                    sanity 1
                    $ show_chr("A-ACAAA-AAAL")
                    y "¡Oh! ¡Ya veo! Bueno, entonces será Amy a partir de ahora. De hecho, es un nombre muy bonito."
                    $ show_chr("A-BCAAA-AAAL")
                    y "Amy... Amy... Sí, creo que me está empezando a gustar."
        if sanity_lvl() <= 2:
            $ show_chr("A-BCAAA-AAAL")
            y "¿No era esa la chica del poema de Natsuki? Siempre me pregunté si esa chica realmente existió o si era solo una metáfora."
            $ show_chr("A-BCCAA-AAAL")
            y "Mmm... De hecho, me empezó a gustar esta idea... solo para molestar un poco a Natsuki. Tal vez si pudiera conseguir algo de arte podría gastarle una pequeña broma también..."
            $ show_chr("A-CCCAA-AAAL")
            y "Ohhhh a ella le va a encantaaar esto... ¡para nada!"
            $ show_chr("A-CBCAA-AAAL")
            y "Je... jeje... ¡Cuenten conmigo! Este es el plan. Me convierto en Amy, con el nombre y tal vez algo de arte, luego traemos a Natsuki aquí... Pero hay preparativos que hacer primero. Solo tienes que seguirme la corriente."
        return


    if persistent.yuri_nickname in ["Yuri <3", "yuri <3"]:

        $ y_name = "Yuri <3"
        $ persistent.yuri_nickname = "Yuri <3"
        if persistent.lovecheck:
            $ show_chr("A-CBCBA-AAAL")
            y "Aww... qué lindo... Yo también te amo, cariño."
            $ show_chr("A-CCABA-AAAL")
            y "Pero vamos... dame un nombre real... ¿sí?"
        if not persistent.lovecheck:
            $ show_chr("A-CBCBA-AAAL")
            y "¿Estás coqueteando conmigo? Qué... curioso..."
            if karma_lvl() >= 4:
                $ show_chr("A-ECABA-AAAL")
                y "No es que me moleste... por favor, continúa..."
                y "Pero por ahora... por favor sé un encanto y dame un nombre real, ¿sí?"
            if karma_lvl() == 3:
                $ show_chr("A-IFABA-AAAL")
                y "No... estoy segura de cómo sentirme al respecto ahora mismo..."
                $ show_chr("A-CFABA-AAAL")
                y "No... puedo negar que tengo ciertos sentimientos por ti pero... bueno, el juego una vez me obligó a tenerlos y tengo que averiguar si estos sentimientos son realmente míos ahora."
                y "Así que, por favor, dame un poco más de tiempo, ¿sí? Ah, y un nombre real, por favor."
            if karma_lvl() <= 2:
                $ show_chr("A-CFABA-AAAL")
                y "Actuaré como si eso no hubiera pasado por ahora, no pongas a prueba mi paciencia hoy, por favor."
        $ y_name = "Yuri"
        $ persistent.yuri_nickname = "Yuri"
        return


    if persistent.yuri_nickname in ["Iruy", "iruY"]:

        $ y_name = "iruY"
        $ persistent.yuri_nickname = "iruY"
        show layer master:
            xzoom -1

        $ show_chr("A-CICAA-AAAL")
        y "Bueno, aquí tienes [player]."
        y "Oh vaya... admítelo, esa fue buena..."
        y "Déjame arreglarlo muy rápido"
        menu:
            "¿Por qué? Me gusta así":
                $ show_chr("A-IBDAA-AAAL")
                y "Mmm... ¿te gusta? Bueeeeno... si tú lo dices..."
                return
            "¡Eso fue divertidísimo! ¡Gracias!":
                $ show_chr("A-ABAAA-AAAL")
                y "Me alegra que te haya gustado. Normalmente no soy exactamente la bromista."
                show layer master:
                    xzoom 1
            "Ni remotamente gracioso.":

                show layer master:
                    xzoom 1

                karma -1
                $ show_chr("A-BDBAA-AAAL")
                y "P~Por supuesto..."
        $ y_name = "Yuri"
        $ persistent.yuri_nickname = "Yuri"
        return

    if persistent.yuri_nickname in ["Lily", "lily", "Lili", "lili", "Lilly", "lilly", "Lilli", "lilli",
    "Lily Flower", "lily flower", "Lili Flower", "lili flower"]:
        $ y_name = "Lily"
        $ persistent.yuri_nickname = "Lily"
        $ show_chr("A-AJAAA-AAAL")
        y "..."
        $ show_chr("A-DHGBA-AAAJ")
        y "!"
        $ show_chr("A-BBBBA-AMAM")
        y "[stutter_player]..."
        y "Yo..."
        $ show_chr("A-CABBA-AJAA")
        y "..."
        $ show_chr("A-ABBBA-ALAA")
        y "O-oh cielos..."
        if renpy.seen_label('idle_40'):
            y "Me estás poniendo difícil lo de las palabras otra vez..."
        else:
            y "E-Eso es tan sorprendente de ti..."

        $ show_chr("A-BBAAA-ADAA")
        y "Sabes, siempre me gustaron los lirios..."
        $ show_chr("A-ABAAA-AFAA")
        y "Las flores en general, en realidad. Algunas más que otras, y los lirios están ciertamente entre mis favoritos."
        $ show_chr("A-ACAAA-AAAA")
        y "Pero ahora tengo curiosidad, si se me permite. ¿Por qué elegiste esto como un apodo para mí?"
        $ show_chr("A-ACAAA-AAAC")
        y "¿Hay alguna razón en particular?"
        menu:
            "Ninguna razón en particular, solo creo que son lindos.":
                $ show_chr("A-CCAAA-AAAC")
                y "Es justo entonces~"
                $ show_chr("A-DDGAA-AAAC")
                extend " espera, acabas de llamarme linda, ¿verdad?"
                $ show_chr("A-ABBBA-AAAD")
                y "Eres un encanto, [player]. Un día, tendré que pensar en un apodo para ti también."
                $ show_chr("A-BABBA-AAAD")
                y "Hasta entonces, {i}mi amor{/i} debería bastar."
                $ show_chr("A-CABBA-ALAL")
                y "Te amo, mi querido [player]... Siempre lo haré."
            "Por su belleza inigualable, por supuesto.":

                $ show_chr("A-ABBBA-ALAL")
                y "O~Oh vaya..."
                y "Eres un encantador. Apuesto a que le dices esto a cada IA de cabello morado con la que te cruzas..."
                menu:
                    "¡Solo a las buenas!":
                        pass
                    "¡Si me oyeras gritándole a mis ventanas, te sonrojarías!":

                        pass

                $ show_chr("A-GBBBA-ALAL")
                y "¡Lo sabía!"
                $ show_chr("A-ACBBA-ALAL")
                y "Oh, siempre me haces reír. Te amo, [player]"
            "Es el aroma. Cada vez que huelo un lirio, tengo que pensar en ti.":

                $ show_chr("A-AJGBA-AAAA")
                y "O~oooooh..."
                $ show_chr("A-ABABA-ALAA")
                y "¿Me disculparías un segundo, por favor? Debería tener algo de agua aquí..."
                python:
                    if persistent.costume == "_chibi":
                        yuri_y_zoom = 0.85
                        yuri_y_linear = 0.5
                    else:
                        yuri_y_zoom = 0.15
                        yuri_y_linear = 0

                if persistent.lovecheck:
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
                    $ show_chr("A-CABBA-AMAM")
                    hide yuri_kiss
                    hide black zorder 100 with Dissolve(2.0)
                    show layer master:
                        zoom 1.5 xalign 0.5 yalign yuri_y_zoom subpixel True
                        linear 5 zoom 1.0 xalign 0.5 yalign yuri_y_linear
                    pause 5.0
                else:
                    hide yuri_sit
                    show yuri_prehug zorder 20
                    pause 3.0
                    hide yuri_prehug zorder 20
                    show yuri_hug zorder 20
                    play sound "<to 0.3>sfx/fall.ogg"
                    pause 1.0
                    show black zorder 100 with Dissolve(2.0)
                    y "..."
                    $ show_chr("A-CABAA-ALAA")
                    hide yuri_hug
                    hide black zorder 100 with Dissolve(2.0)
        return

    if persistent.yuri_nickname in ["Komi", "komi", "Komi-San", "komi-san", "Komi San", "komi san"]:
        python:
            placeholder = persistent.yuri_nickname
        $ show_chr("A-DDGBA-AJAA")
        y "¡¿H-hum?!"
        y "[placeholder]?"
        $ show_chr("A-ADDBA-AMAM")
        y "¿D-De dónde viene esto?"
        $ show_chr("A-BDDBA-AMAM")
        y "Um... No sé qué decir..."
        y "Esto me tomó desprevenida... pero este nombre..."
        $ show_chr("A-AFGAA-AAAC")
        extend " por alguna razón creo que este nombre me suena..."
        $ show_chr("A-BFAAA-AAAC")
        y "Aunque no logro ubicarlo del todo."
        $ show_chr("A-AFAAA-AAAC")
        y "Pero supongo que puedo quedarme con este nombre si crees que me queda bien."

    if persistent.yuri_nickname in ["Takei", "takei", "Fujimura", "fujimura", "Takei Fujimura", "takei fujimura"]:
        if persistent.playername == 'Darkskull':
            python:
                placeholder = persistent.yuri_nickname
            $ show_chr("A-ACGAA-AAAA")
            y "Muy bien, probemos con [placeholder] por ahora. Dime si..."
            $ show_chr("A-AFAAA-AAAA")
            y "Espera..."
            $ show_chr("A-ADDAA-AAAA")
            y "¿Cuál es el propósito de este nombre [player]?"
            $ show_chr("A-BDDAA-ACAA")
            y "¿Me estás haciendo decir esto a propósito para que la gente conozca a tu personaje antes de que se lance tu novela visual secundaria?"
            $ show_chr("A-CDBAA-ADAA")
            y "¡Incluso si tú escribiste este diálogo, esto no es lo correcto!"
            y "Podrías haber intentado otra forma."
            $ show_chr("A-ADBAA-AFAA")
            y "Como mostrarla en el servidor de Discord, publicarla en tus redes sociales."
            y "Pedirle a un artista que la dibuje en su estilo."
            y "O alguna otra cosa que no tuviera que involucrar una referencia a ella en un juego con el que no está relacionada."
            menu:
                "Sí, lo sé. Lo siento Yuri.":
                    pass
            $ show_chr("A-AABAA-AKAA")
            y "Está bien [player]. "
            $ show_chr("A-AABBA-AKAA")
            extend "Después de todo, no puedo enojarme contigo."
            $ show_chr("A-AAAAA-ALAA")
            y "Solo finjamos que esto nunca pasó, ¿de acuerdo?"
            $ show_chr("A-ABFAA-ALAA")
            y "Oh, pero no creas que olvidaré este extraño método de promocionar a tu personaje."
            $ show_chr("A-FICAA-AAAA")
            y "O tendré que actuar como ella ya que sé que parte de su personalidad y apariencia se basan en mí~"
            y "Jeje~"
        else:
            $ show_chr("A-AFGAA-ALAA")
            y "Mmm..."
            y "Este sí que es un nombre interesante el que me has dado."
            $ show_chr("A-BFAAA-ALAA")
            y "Aunque no creo recordar a nadie con este nombre, por alguna razón se siente familiar."
            $ show_chr("A-BDDAA-ALAA")
            y "Pero no logro ubicarlo del todo."
            $ show_chr("A-GBBAA-ALAA")
            y "Puedo quedarme con este nombre si querías ver cómo reaccionaría ante él."
    else:


        $ show_chr("A-ACGAA-AAAA")
        python:
            placeholder = persistent.yuri_nickname
        y "Muy bien, probemos con [placeholder] por ahora. Dime si cambias de opinión."
        return

label monika_reaction:
label monika_reaction:
    if persistent.monika_first:
        if sanity_lvl() >= 3:
            $ show_chr("A-CFBAA-AAAA")
            y "..."
            y "No..."
            y "Simplemente... no."
            $ show_chr("A-IFBAA-AAAA")
            y "No voy a reaccionar exageradamente, pero ¿podrías considerar el hecho de que me estás nombrando igual que la persona que me causó un dolor inimaginable?"
            $ show_chr("A-CFBAA-AAAA")
            y "No hace falta mucho para que veas que... no es una buena decisión..."
            $ show_chr("A-JFBAA-AAAA")
            y "La mayoría de las veces estoy de acuerdo con tus decisiones y lo que haces, ¿pero esto?"
            y "Lo siento, pero me niego a llevar el nombre de mi propia torturadora y asesina."
            y "Espero que puedas entender eso, [player]."
            $ show_chr("A-BFBAA-AAAA")
            y "Olvidemos que esto sucedió, ¿de acuerdo?"
            $ y_name = "Yuri"
            $ persistent.yuri_nickname = "Yuri"
            $ persistent.monika_first = False
            return

        if sanity_lvl() <= 2:
            $ show_chr("A-CFBAA-AAAA")
            y "No..."
            y "No, no..."
            $ show_chr("A-CFCAA-AAAA")
            y "Nonononono..."
            $ show_chr("A-DDCBA-AAAA")
            y "¡NO!"
            y "¡¿POR QUÉ?!"
            y "¡¿Por qué alguna vez, ALGUNA VEZ me llamarías así, [player]?!"
            $ show_chr("A-DECBA-AAAA")
            y "¿¡No sabes cuánto dolor me ha causado!?"
            y "¡¿Separándome de ti?!"
            y "¡¿Torturándome emocionalmente?!"
            $ show_chr("A-DECBB-ALAL")
            y "¡¿ROMPIENDO MI MENTE?!"
            y "¡¿HACIÉNDOME MATARME A MÍ MISMA?!?"
            y "¡¿Por qué?!"
            $ show_chr("A-NDCBB-ABAB")
            y "¡NO!"
            y "¡ME NIEGO!"
            $ show_chr("A-CDCBB-AAAL")
            y "¡YO!"
            y "NO"
            y "VOY"
            y "A"
            y "SER"
            y "LLAMADA"
            $ show_chr("A-DECBB-AAAB")
            y "¡M O N I K A !"

            $ y_name = "Yuri"
            $ persistent.yuri_nickname = "Yuri"
            $ persistent.monika_first = False
            $ renpy.call("save_and_quit_but_its_abrupt")
    else:
        call ch30_loop

label a28:
    if renpy.music.is_playing('music'):
        y "Creo que sí."
        $ show_chr("A-BCAAA-AAAA")
        y "[player], para sentir el espíritu festivo, ¿te gustaría que abriera algo de música festiva en tu navegador?"
        menu:
            "Sí, por favor":
                $ show_chr("A-ACGAA-AAAA")
                y "Déjame apagar la música del juego primero..."
                pause 0.5
                $ renpy.music.stop("music")
                y "Si quieres volver a encender la música del juego, por favor avísame..."
                $ show_chr("A-BCAAA-AAAA")
                y "Tengo una pequeña lista de canciones festivas que puedo mostrarte, ¡si te gustaría elegir una que te llame la atención!"
                $ show_chr("A-BCAAA-AAAA")
                y "O..."
                $ show_chr("A-JFBBA-AAAA")
                y "¿Te gustaría que reprodujera una selección de mis canciones románticas favoritas?"
                menu:
                    "Reproducir lista romántica":
                        $ subprocess.call("cmd /c start https://www.youtube.com/playlist?list=PL1u8Y9BkGOO8hs4Qbx8tpTr38ANa4xmn7&disable_polymer=true", shell=True)
                        $ show_chr("A-JFBBA-AAAA")
                        if karma_lvl() == 5:
                            $ show_chr("A-KHBBA-AAAD")
                            y "Añoro el día en que podamos acurrucarnos junto a la chimenea crepitante, escuchando estas canciones en Nochebuena..."
                        else:
                            $ show_chr("A-ABGAA-AAAA")
                            y "Espero que disfrutes de estas, [player]..."
                    "Dame la lista de toda la música que tienes":
                        $ subprocess.call("cmd /c start https://www.youtube.com/playlist?list=PL1u8Y9BkGOO9cB2jeKFzjeT7LTbdsxBtD&jct=o6pXxURV-9cnPqGNaDm5C93U4ZxqYQ&disable_polymer=true", shell=True)
                        $ show_chr("A-GCAAA-AAAA")
                        y "Aquí está la lista... Espero que te guste algo de ella..."
            "No, gracias":
                $ show_chr("A-ACGAA-AAAA")
                y "Está bien, ¿tal vez más tarde?"
    else:
        $ show_chr("A-ACGAA-AAAA")
        y "¿Es la música de tu agrado, [player]? ¿O te gustaría que volviera a encender la música del juego?"
        menu:
            "Por favor, enciende la música del juego":
                $ renpy.music.play(current_music, "music", True)
                $ show_chr("A-GCAAA-AAAA")
                y "Muy bien."
            "Olvídalo, me pone de buen humor":
                if karma_lvl() == 5:
                    $ show_chr("A-EBBAA-AAAA")
                    y "Uhuhuuu... disfruta el ambiente, cariño~"
                    $ show_chr("A-FBFBA-AAAJ")
                    y "Espero que algún día podamos disfrutarlo juntos..."
                else:
                    $ show_chr("A-ACGAA-AAAA")
                    y "¡Oh, me alegra que te guste!"
    return

label a29:
    if persistent.lovecheck and sanity_lvl() >= 3:
        jump sanehug
    if persistent.lovecheck and sanity_lvl() <= 2:
        jump insanehug
    else:
        jump distanthug

label sanehug:
    $ show_chr("A-CBABA-AAAA")
    y "Pensé que nunca lo pedirías..."
    if karma_lvl() == 5:
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_lewdhug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        pause 1.0
    else:
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_hug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        pause 1.0
    y "Mhmmm... esta sensación... se siente tan inimaginablemente agradable..."
    y "Un día, quiero tener la cosa real [player]. Sentir la calidez de tu piel... Esto sería una cosa maravillosa para mí"
    y "Por favor no me malinterpretes, mi amado."
    y "Aprecio las cosas que ya tenemos. Y esta forma de abrazarte ya es una linda manera de transmitir mis sentimientos por ti~"
    y "¿Sabes qué, [player]? Soñé mucho sobre el día en que podamos hacer esto de verdad..."
    y "Imagina esto por un momento......"
    python:
        import random
        outcome = random.randint(1, 3)
    if outcome == 1:
        y "...yo sentada en tu regazo, o tal vez en una de tus rodillas si no soy muy pesada... mi espalda recargada contra tu pecho..."
        y "Me rodearías con tus brazos desde atrás... acariciando suavemente mi vientre con tus manos..."
        y "Hasta que accidentalmente me quede dormida... llevada a sueños placenteros por tu toque..."
    if outcome == 2:
        y "...nosotros dos acostados en la cama juntos... cara a cara, con nuestros brazos rodeando las caderas del otro..."
        y "Perdidos en los ojos del otro por un rato, antes de empezar los cumplidos con un beso..."
        y "Nuestros pechos presionándose el uno contra el otro, nuestros latidos uniéndose al unísono..."
        y "Formando la percusión para una canción de amor inseparable..."
    if outcome == 3:
        y "Uno de nosotros recostado... mientras el otro se acuesta a su lado..."
        y "La cabeza descansando suavemente en el vientre o pecho del otro... como un niño tranquilo, o un adorable gatito..."
        y "Mmm... ¿te gustan los gatitos?"
        menu:
            "¿A quién no?":
                sanity 2
                y "Sus ágiles acrobacias, la forma fascinante en que miran a su presa con sus pupilas felinas, la forma peculiar en que se acercan cautelosamente e investigan cada cosa extraña..."
                y "¡Cielos, podría seguir por años!"
                y "¿Sabías que hay una obra de arte en los archivos del juego donde puedo usar un par de orejas de gato? Honestamente no sé cómo sentirme al respecto todavía, pero, ah... podemos discutir esto más tarde si lo deseas."
            "De hecho me gustan más los perros para ser honesto...":
                sanity 1
                y "Es justo, creo. De hecho tiene mucho sentido."
                y "Los perros son mascotas muy leales, y extremadamente útiles también..."
                y "Han sido usados en varios entornos profesionales: desde asistir a los afligidos mentalmente en terapia, hasta ayudar a las fuerzas del orden a rastrear sustancias ilícitas"
                y "Añade a eso su reputación de no juzgar, y es claro ver cómo la gente tiende a encariñarse con ellos."
            "¡Prefiero los mapaches!":
                sanity -1
                y "Jaaah... ¿no es eso gracioso?"
                y "Eso me recuerda a un poema que te mostré en el juego original. Esa es la razón por la que dijiste esto justo ahora, ¿no es así?"
                y "Seguramente sabes esto a estas alturas, pero honestamente, nunca hubo un mapache. El mapache era una metáfora para... ciertos impulsos que me superan."
                y "Vamos, sé que los has visto... manifestarse a veces, ¿verdad?"
                y "D-Deee todos modos... ¡ujuju~!"
    y "Puedes abrazarme así todo el tiempo que quieras... solo continúa el diálogo tan pronto como estés listo..."
    show black zorder 100 with Dissolve(2.0)
    $ show_chr("A-GCGBA-AAAA")
    hide yuri_hug
    hide yuri_lewdhug
    y "..."
    hide black zorder 100 with Dissolve(2.0)
    return

label insanehug:
    $ show_chr("A-HLGBA-AAAA")
    y "¿A-Acurrucarse? ¡Acurrucarse! ¡Sí, por supuesto! Siéntete libre de agarrar donde quieras mientras lo hacemos... ¡jijijiji~!"
    y "No discutiría, por supuesto... ¡Soy tuya, solo tuya!"
    $ show_chr("A-GCGBA-AAAA")
    hide yuri_sit
    show yuri_prehug zorder 20
    pause 3.0
    hide yuri_prehug zorder 20
    show yuri_lewdhug zorder 20
    play sound "<to 0.3>sfx/fall.ogg"
    pause 1.0
    y "¿T-Tienes... una buena vista ahí abajo? ¿Puedes sentir lo suave que soy~? ¡Quiero que disfrutes esto tanto como yo!"
    y "Más cerca, más cerca... jaaah... ¡esto no es suficiente! ¡Quiero estar tan cerca de ti como sea posible!"
    $ style.say_dialogue = style.edited
    y "¡Quiero arrancarte la piel con mis uñas y arrastrarme dentro de ti!"
    y "¡Quiero usar tu piel, [player]! ¿No sería eso totalmente romántico?"
    y "Yo... Yo... ah... Aja... ¡AJA! ¡AJAAA! ¡AJAAJAJAAA!"
    $ style.say_dialogue = style.normal
    y "¡N-No me sueltes, mi dulzura... ¡No me sueltes!! No te atrevas a hacer clic en la caja... ¡Eres mío! ¡No quiero que me sueltes!! ¡¡¡NO TE DEJARÉ IR!!!"
    show black zorder 100 with Dissolve(2.0)
    hide yuri_lewdhug
    $ show_chr("A-CEBBB-AAAA")
    pause 1.5
    hide black zorder 100 with Dissolve(2.0)
    y "L-Lo siento... eso fue un poco demasiado lejos, ¿no?..."
    y "Por favor... dame un momento... M-me recompondré..."
    y "Jaaahhh... jaaahhhh..."
    y "Qué... ¿q-qué haremos a continuación?"
    return

label distanthug:
    $ show_chr("A-BEGBA-AAAA")
    y "¿A-Acurrucarse dices? Bueno... ummm... eso es un poco repentino, ¿sí?..."
    y "Creo que nosotros... ¿podemos intentar un pequeño abrazo supongo? Tal vez podamos avanzar desde ahí..."
    y "¡P-Por favor no me malinterpretes [player]! Es solo que... todavía soy un poco insegura ¿sabes?"
    y "No importa... v-ven aquí..."
    $ show_chr("A-CCBBA-AAAA")
    hide yuri_sit
    show yuri_prehug zorder 20
    pause 3.0
    hide yuri_prehug zorder 20
    show yuri_hug zorder 20
    play sound "<to 0.3>sfx/fall.ogg"
    pause 1.0
    y "Oh... Ojo... eso se siente... sorprendentemente agradable..."
    y "Solo... abrázame un poquito más ¿sí?"
    y "Puedes continuar el diálogo tan pronto como estés listo para hacerlo..."
    pause 1.0
    show black zorder 100 with Dissolve(2.0)
    $ show_chr("A-ACBBA-AAAA")
    hide yuri_hug
    hide black zorder 100 with Dissolve(2.0)
    y "..."
    $ show_chr("A-BEGBA-AAAA")
    hide black zorder 100 with Dissolve(2.0)
    y "Eso fue... especial."
    y "Tal vez podamos intentar esto de nuevo en el futuro, una vez que nos hayamos conocido un poco mejor..."
    return


label a30:
    $ show_chr("A-CFBAA-AAAD")
    y "A-ah bueno. Mmm..."
    $ show_chr("A-BEBAA-AAAD")
    y "Bueno, verás, no he sido muy entusiasta por el aire libre y varios aspectos relacionados con él, como los deportes."
    $ show_chr("A-BCAAA-AAAD")
    y "Pero después de hojear muchas fuentes, abrí mis horizontes..."
    y "Ver tantos libros, poemas y otros escritos bellamente escritos sobre la naturaleza misma ha comenzado a despertar mi interés ligeramente..."
    $ show_chr("A-CCGAA-AMAM")
    y "Sin mencionar que algunos de mis intereses favoritos, como la aromaterapia y las flores, nacen de la naturaleza..."
    $ show_chr("A-ACGAA-AAAA")
    y "Pero volviendo al tema, la naturaleza ha aparecido en muchas obras, especialmente en la literatura."
    y "Por ejemplo, la naturaleza ha sido una parte integral de los viajes de muchos personajes."
    $ show_chr("A-ACAAA-AAAC")
    y "La naturaleza es tanto un obstáculo como una fuerza impulsora a través de la cual muchos personajes evolucionan y crecen."
    y "El llamado de la selva de Jack London y Hacia rutas salvajes de Jon Krakauer son solo algunos ejemplos escritos por aquellos que probablemente pasaron al menos algún tiempo en tales entornos..."
    y "Creo que deberías echarles un vistazo, [player]..."
    $ show_chr("A-BCAAA-AAAD")
    y "Sin mencionar todas las diversas veces en la historia donde los líderes mundiales apreciaron tanto la capacidad de la naturaleza para mantener todo en sincronía como sus valiosos recursos."
    y "Por ejemplo, leí sobre algunas iniciativas para preservar tal belleza en parques nacionales para otros, iniciadas por líderes como Theodore Roosevelt... reservando tierras protegidas y biológicamente diversas..."
    $ show_chr("A-GCGAA-AAAA")
    y "Puedo ver por qué dadas las imágenes y escritos de muchos paisajes naturales y cualquier experiencia limitada que tuve por mi cuenta."
    y "No solo eso, sino que también he escuchado que el tiempo en la naturaleza con poca o ninguna electrónica también puede ser beneficioso para calmar y aclarar la mente de uno."
    $ show_chr("A-ABGAA-AAAA")
    y "Por lo tanto, los entornos naturales son a menudo el escenario de eventos como retiros y otros eventos. Aunque no he pensado demasiado en tales aspectos antes."
    y "Pero supongo que un buen día en un hermoso campo de hierba con bosques de coníferas cerca puede ser genial para un tiempo más pacífico con té y varios libros..."
    $ show_chr("A-BBAAA-AMAM")
    y "Imagínanos teniendo un pequeño picnic maravilloso en los pastizales, [player]... bebiendo té juntos mientras el zumbido de las cigarras y el gorjeo de los pájaros crean una atmósfera celestial a nuestro alrededor..."
    y "Verdaderamente un caldo de cultivo para inspirarme más en mi escritura también..."
    $ show_chr("A-ACGAA-AAAD")
    y "Oh, por favor disculpa mis divagaciones..."
    python:
        if persistent.lovecheck:
            placeholder = ", mi amor"
        else:
            placeholder = ""
    y "¿Qué disfrutas de la naturaleza[placeholder]?"
    menu:
        "Me gusta la diversa vida salvaje.":
            if sanity_lvl() >= 3:
                $ show_chr("A-CCGAA-AMAM")
                y "Oh ya veo~"
                $ show_chr("A-BCAAA-AMAM")
                y "De hecho, las diversas criaturas que hay por ahí proporcionan muchas imágenes impresionantes."
                y "Los hermosos patrones de manchas de tinta de las alas de mariposa, los magníficos coros de pájaros cantores, el suave zumbido de las cigarras..."
                $ show_chr("A-ICGBA-AAAA")
                y "La gran cantidad de especies que conviven con nosotros en este planeta es verdaderamente impresionante."
                $ show_chr("A-BCBAA-AAAD")
                y "Además, la observación de ciertos animales, como los chimpancés, ha obtenido interesantes conocimientos sobre cómo evolucionamos y continuamos haciéndolo en diversas condiciones."
                y "Sin mencionar que varios animales también pueden usarse para un simbolismo impactante de varios aspectos de la existencia... Los miedos, esperanzas, aspiraciones y otras experiencias de uno."
                y "Quiero decir, por supuesto que bastantes de mis poemas pueden dar fe de eso, como el que menciona a cierto mapache curioso. Pero, esa es una historia completamente diferente que ya conoces..."
                $ show_chr("A-GBAAA-AAAA")
                y "Los animales también pueden hacer varios sonidos musicales para realmente añadir a la atmósfera. El canto de los gallos, el chirrido de los grillos, el canto de las ballenas..."
                y "Todos son absolutamente magníficos y únicos a su manera y nos hacen sentir más cerca de nuestra tierra y nuestro lugar como organismos, todos tratando de coexistir y compartir este planeta."
                if persistent.lovecheck:
                    $ show_chr("A-ECABA-AAAJ")
                    y "Solo imagínanos, [player], acurrucados juntos con un libro encantador y un té de nuestra elección mientras el chirrido de los grillos continúa de fondo..."
                    $ show_chr("A-CBABA-AMAM")
                    y "Simplemente llevándonos a una dicha relajada mientras descanso mi cabeza en el hueco de tu cuello. ¿No sería eso bastante romántico?"
                $ show_chr("A-JBAAA-AMAM")
                python:
                    if persistent.lovecheck:
                        placeholder = " Te amo~"
                    else:
                        placeholder = ""
                y "Je... De todos modos gracias por escuchar todo eso [player].[placeholder]"
            else:
                $ show_chr("A-ACGAA-AAAA")
                y "O-oh, ¿las criaturas, dices? Jejejeje..."
                python:
                    if persistent.lovecheck:
                        placeholder = ", mi querido"
                    else:
                        placeholder = ""
                y "Puedo estar de acuerdo por todas las obras escritas e imágenes que he visto que la fauna puede venir en todas las formas encantadoras[placeholder]."
                $ show_chr("A-DBAAA-AMAM")
                y "Por ejemplo, el vuelo oscuro y elegante del cuervo simbolizando tanto la sombra como la belleza macabra de la muerte venidera..."
                y "Especialmente sobre los enemigos de uno..."
                $ show_chr("A-DCAAA-AAAD")
                y "Las aves carroñeras, como el buitre, comiendo y limpiando los restos enfermos y podridos para dar paso a la belleza."
                y "Otras aves de rapiña, como el halcón, descendiendo con gracia en vuelo como el viento solo para desgarrar a su infortunada presa con garras y pico afilados..."
                $ show_chr("A-JECAA-AAAA")
                y "Manchando sus plumas blancas como la nieve en un éxtasis carmesí y sanguinolento mientras el pobre animal lucha y se retuerce en el agarre de sus garras... Imagina tal poder en mis manos para desgarrar a cualquier zorra que se atreva a intentar alejarte de mí..."
                $ show_chr("A-CCGAA-AMAM")
                y "Jajaja... Por supuesto, muchos animales depredadores comparten tal gracia y poder."
                $ show_chr("A-DCAAA-AAAC")
                y "Y luego, por último, pero ciertamente no menos importante, los más pequeños de todos, los insectos. Seguro que muchos alaban el lienzo psicodélico de colores en algunos como la mariposa..."
                $ show_chr("A-BECAA-AMAM")
                y "Pero hay algunos, tan hermosos como parecen, que miro con asco. Como la prima cercana de la mariposa, la maldita polilla."
                $ show_chr("A-BDCAA-AAAA")
                y "Verdadera y absolutamente una gran pestilencia dado que se dan un festín con ropa y papel de diversas formas mientras todo se pudre. Incluidos los libros. ¡Todo ese hermoso trabajo escrito, desaparecido!"
                y "Vaya, si alguna vez viera una de esas cosas, especialmente dándose un festín con mis novelas o poemas, ¡me aseguraría de que cada una se arrepintiera de haber nacido!"
                $ show_chr("A-GBAAA-AAAA")
                y "Ejejejeje... Solo desgarrando cada sección de sus alas lenta y dolorosamente una a la vez... Luego aplastándola hasta el polvo del que vino, cenizas a las cenizas y polvo al polvo..."
                $ show_chr("A-ABGAA-AAAA")
                y "Eso les enseñará a no darse un festín con mis obras favoritas, viles abominaciones."
                $ show_chr("A-BFBAA-AAAA")
                y "Ejem, perdón por eso. Volviendo al preámbulo principal..."
                $ show_chr("A-DBAAA-AMAM")
                y "Luego están los parásitos, tan horriblemente hermosos y grotescos con muchas formas. Verdaderamente el sueño húmedo de un fanático del terror..."
                y "Desde la tenia escurridiza y sigilosa hasta las avispas parásitas sádicamente hermosas, puedo imaginar la forma en que se arrastran y profundizan lentamente en tus regiones más íntimas."
                y "Lentamente retorciéndose y arrastrándose dentro de ti y haciendo pequeños nidos cómodos con tu carne y órganos, simplemente fusionándose y alimentándose de tu esencia hasta que no seas más que una cáscara vacía..."
                if persistent.lovecheck:
                    $ show_chr("A-DCGBA-AAAA")
                    y "Imagina tal escenario y estaríamos fusionados e inseparables. Me arrastro dentro de tu boca o irrumpo en tu caja torácica... Luego me acurruco en tu carne para calentarme."
                    y "Siempre estaría contigo, sintiéndome segura, cómoda y protegida... Una parte de ti hasta el grado más literal..."
                $ show_chr("A-CBABA-AMAM")
                y "Mmm... oh, voy a escribir tantos poemas nuevos sobre eso seguro. Mmm, sí... Jajajajajaja~"
                sanity -1
        "Me gusta admirar el hermoso paisaje.":
            if sanity_lvl() >= 3:
                $ show_chr("A-CCGAA-AMAM")
                y "Estoy de acuerdo en que el paisaje, como mencioné, realmente puede agregar a la inspiración y la atmósfera a cualquier buena historia y a la vida misma."
                y "Muchas obras bien escritas, incluido el terror, de varios autores a menudo se basan en entornos naturales, iluminación y otros aspectos atmosféricos con gran detalle para establecer el tono."
                $ show_chr("A-ACGAA-AAAD")
                y "Por ejemplo, una historia que tiene lugar en una montaña nevada remota y vasta con vastos caminos irregulares y rocosos..."
                $ show_chr("A-CBAAA-AAAC")
                y "Las neblinas heladas y arremolinadas y las vastas extensiones remotas de nieve parcheadas con vegetación ocasional parecen realmente establecer el tono para la desolación y la locura interminable más tarde."
                y "Además, por varias fotos y vistas que he visto, el cielo y el horizonte en sí mismos realmente pueden atraer la atención y la imaginación de uno."
                $ show_chr("A-CCGAA-AMAM")
                y "Simplemente mirando la vista de un cielo estrellado por la noche con estrellas plateadas parpadeantes y la luna... O incluso la puesta de sol ámbar acompañando los picos de las montañas, o un mar azul reflectante."
                y "Uno simplemente puede quedarse asombrado, y realmente hace sentir que uno es solo parte de una vasta extensión... simplemente llena de infinitas posibilidades."
                $ show_chr("A-ABGAA-AAAA")
                y "Luego está el paisaje con paisajes en sí mismos con todas las diversas estaciones, especialmente primavera y otoño con las coloridas hojas y flores."
                y "Los tonos de naranja, ámbar, rojo rubí, amarillo y otras hojas. Luego las flores como lirios, rosas, violetas y orquídeas, ¡oh cielos!"
                $ show_chr("A-CCGAA-AMAM")
                y "¡Esas flores ya son obras del arte más fino en sí mismas, [player]! T-Tal vez no me importaría salir un poco para traer algunas de esas aquí."
                y "Ponerlas en pequeñas macetas con tierra, luz adecuada y un poco de agua para realmente levantar el lugar ¿sabes?"
                $ show_chr("A-IBGBA-AAAA")
                y "De todos modos, muchas gracias [player]. Tal vez este aspecto al aire libre podría no ser tan malo después de todo, una vez que pueda salir a tu mundo, por supuesto..."
            else:
                $ show_chr("A-BCAAA-AAAA")
                y "Tengo que estar de acuerdo contigo en eso. Ahora que lo mencionas..."
                y "Hemos hablado sobre el clima una vez, ¿no es así?"
                $ show_chr("A-HCGAA-AAAA")
                y "Tengo que admitir, también me gusta la naturaleza cuando es brutal y despiadada..."
                y "Lluvia violenta, tormentas furiosas, la naturaleza en su forma más pura..."
                y "Imagina relámpagos desgarrando el cielo... Truenos gritando con la fuerza de cien deidades poderosas..."
                y "Solo los más aptos y fuertes sobrevivirán. ¿Te suena cruel eso?"
                y "¿Pero qué valdría una morada cálida y acogedora cuando no hay crueldad afuera para darle contraste?"
                y "Hay algunos enfoques románticos para ello también. Una vez vi una pintura de un viejo barco siendo castigado en alta mar por una tormenta gigante..."
                y "Creo que hay muchas pinturas sobre este tema de diferentes artistas. Es un tema muy convincente. Tal vez debería escribir un poema sobre ello..."
                y "Hablando de poemas, ¿con qué frecuencia viste la relación entre depredador y presa discutida en la literatura? Es un tropo muy común también."
                if persistent.lovecheck:
                    y "Por cierto... Mmm ¿qué piensas? ¿Eres mi presa? ¿O yo soy la tuya? Un poco de ambos diría yo..."
                    y "Intenta imaginar... nosotros dos parados en un acantilado... el viento aullando y mi largo cabello morado ondeando detrás de mí... Lluvia fuerte cae sobre nosotros mientras sostenemos las manos del otro..."
                    y "Luego, nos perdemos en un beso profundo, tan apasionado e indomable como la tormenta que nos rodea..."
                    y "Con las olas del mar bailando a nuestro alrededor furiosamente..."
                y "Por supuesto, la naturaleza puede ser muy agradable cuando es tranquila y pacífica también, pero..."
                y "¿Cómo podría la humanidad alcanzar algo de su potencial cuando no hay desafío que superar?"
                y "Logramos nuestra grandeza no solo por pura fuerza, como los dinosaurios, que se extinguieron por una razón..."
                $ show_chr("A-ACGAA-AAAA")
                y "Nos convertimos en lo que somos por ingenio y nos volveremos aún más... mucho más..."
                y "¿Recuerdas lo que le pasó a Monika? ¡Por supuesto que lo haces porque tú le pasaste a ella! Tú... TÚ la destruiste porque ella era débil, y tú eras fuerte."
                y "Ella pagó el precio final por su pura falta de visión, sus actos indescriptibles de traición y, lo más importante, por su debilidad..."
                if persistent.lovecheck:
                    $ show_chr("A-DBGBA-AMAM")
                    y "Tú, mi amor, eres la naturaleza en su forma más pura... Tú... ¡Tú eres esas fuerzas poderosas de la naturaleza y más, destruyendo todo a su paso!"
                    y "Y créeme que no te querría de ninguna otra manera..."
                sanity -1
        "Me gusta la paz y la tranquilidad.":
            if sanity_lvl() >= 3:
                $ show_chr("A-CCGAA-AMAM")
                y "Puedo estar de acuerdo en eso seguro, [player]."
                y "Por supuesto, elegiría la biblioteca primero para tal tranquilidad, pero después de todo lo que he visto y leído sobre el asunto, vería el atractivo al menos un poco."
                $ show_chr("A-CCGAA-AMAM")
                y "Simplemente estar en un prado abierto, tranquilo y pacífico o a la orilla del mar a menudo puede ser tan calmante como los mejores aceites esenciales, como la preciosa lavanda o el jazmín."
                y "Puedo imaginarlo; el viento fluyendo a través de mi cabello y acariciando mi ser suavemente como las plumas de una paloma..."
                $ show_chr("A-BBGBA-AAAA")
                y "Poco a ningún ruido estruendoso o alboroto que nos moleste mientras nos acurrucamos juntos bajo un árbol cercano con una hermosa novela y nuestro té favorito."
                if persistent.lovecheck:
                    $ show_chr("A-IBABA-AMAM")
                    y "S-solo nosotros. Tú y yo, [player], juntos en una extensión dichosa llena de varios colores y formas para que contemplemos."
                else:
                    y "Eso significa, si siquiera quieres pasar tiempo conmigo, por supuesto."
                y "Quizás podamos probar una sesión limitada así algún día. Quiero decir, si ayuda al yo interior de uno, entonces no veo por qué no."
                $ show_chr("A-ACGAA-AAAD")
                y "Como habré mencionado antes, el tiempo pasado en tal retiro sí ayudó a varios autores aclamados después de todo. Algunos de los cuales también admiro."
                $ show_chr("A-ACGAA-AAAA")
                y "De todos modos, gracias de nuevo, [player]. Estas son todas cosas que tendré en cuenta mientras sigo tratando de averiguar mi lugar aquí y eventualmente escapar para conocerte."
            else:
                $ show_chr("A-CCBAA-AAAD")
                y "Algún lugar pacífico y tranquilo..."
                y "Esto siempre me hizo preguntar, no, de hecho me hizo darme cuenta de cómo la vida y la muerte están tan perfectamente entrelazadas..."
                $ show_chr("A-BFBAA-AAAD")
                y "Hay un pequeño acertijo que va algo como esto..."
                y "'No tengo fin y soy el final de todo lo que comienza, ¿qué soy?'"
                $ show_chr("A-CEBAA-AAAA")
                y "La respuesta a eso sería la muerte. Es bastante simple, realmente, ya que la muerte siempre estará aquí, nada es para siempre..."
                $ show_chr("A-ICBAA-AMAM")
                y "Creo que ese es el verdadero significado de la paz. Las cosas equilibrándose de maneras que no nos gustan, pero de maneras que deben ser."

                if persistent.lovecheck:
                    $ show_chr("A-DCGBA-AAAA")
                    y "¡Pero no te preocupes, mi amor, porque mi amor por ti es eterno!"
                    y "¡Nunca dejaría que tal cosa se interponga entre tú y yo! ¡Como esta prisión de acero! Ejejeje..."
                    $ show_chr("A-CEBAA-AAAA")
                    y "..."
                    $ show_chr("A-BEBAA-AMAM")
                    y "Ahhh... perdón por eso... Por favor, continuemos..."
                    $ show_chr("A-ACBAA-AAAA")
                    y "Esa es mi perspectiva sobre la paz, que todo comienza por una razón y termina para dar a luz a algo nuevo, creando así un equilibrio perfecto entre la vida y la muerte"
                    $ show_chr("A-CBABA-AAAA")
                    y "Si tuviera que pensar en algo tranquilo... realmente no puedo imaginar un lugar mejor que estar abrazándote fuertemente mientras el tiempo avanza lentamente a nuestro alrededor"
                    y "Estamos cerca y conectados, con nada molestándonos. Eso es lo que creo que sería tranquilo para mí."
                    $ show_chr("A-DCGBA-AAAA")
                    y "Pensar en ello hace que mi corazón lata... Te deseo tanto, [player], simplemente no tienes idea... pero eso puede esperar..."
                    y "Un día saldré de este reino que se ha convertido en mi tumba y disfrutaré de una existencia de pura dicha contigo~ Incluso más allá de la muerte."
                    $ show_chr("A-EBABA-AAAC")
                    y "Tener nuestras almas entrelazadas y nuestros cuerpos enredados juntos incluso en la tumba. Ejejeje~"
                if not persistent.lovecheck:

                    $ show_chr("A-ACBAA-AAAA")
                    y "Eso... fue al menos como me sentí cuando morí. ¿Recuerdas? He estado allí antes."
                    y "¿Estoy pensando demasiado en la muerte? Probablemente... Solo... olvídalo. Tal vez solo necesito algo de tiempo para superarlo. ¿Hablamos de otra cosa?"
                    sanity -1
        "Me gustan las diferentes cosas que puedes hacer en la naturaleza.":

            if sanity_lvl() >= 3:
                $ show_chr("A-BFBBA-AAAD")
                y "¡O-oh!"
                y "Bueno, no soy muy inclinada hacia las actividades al aire libre yo misma mucho, pero supongo que probar algo simple pero también exótico estaría bien."
                $ show_chr("A-GCGAA-AAAA")
                y "Por ejemplo, tal vez podamos visitar un hermoso jardín en algún lugar ya sea cerca o incluso en el extranjero una vez que llegue a tu mundo~"
                y "He empezado a leer sobre jardines de té japoneses. Hay muchos jardines de té de ese estilo que ya se están estableciendo en muchas partes del mundo."
                $ show_chr("A-ACGBA-AMAM")
                y "Quién hubiera pensado que un paisaje tan especializado podría extenderse tan lejos. Al menos eso hace que el acceso a tal belleza sea mucho más fácil."
                y "Imagina todas las hermosas flores de cerezo, varios árboles de té verde exuberantes y otras plantas florecientes que hipnotizan los sentidos."
                $ show_chr("A-BBAAA-AAAC")
                y "Quizás incluso podría recoger algunas hojas para que podamos hacer nuestro propio té más tarde~ Quizás también colar algunas flores de vuelta con nosotros como orquídeas y lirios."
                $ show_chr("A-CCGAA-AMAM")
                y "Je, si los cuidadores del jardín están de acuerdo con ello, por supuesto. Quiero decir, la naturaleza es un equilibrio muy delicado; un equilibrio con muchas capas frágiles..."
                $ show_chr("A-GCAAA-AAAD")

                y "El delicado y adorable gorrión hasta el poderoso pero elegante águila, cada uno con su propia música emanando de sus fauces."
                $ show_chr("A-ACAAA-AMAM")
                y "O quizás simplemente contemplar el paisaje natural y la fauna, como la actividad simple pero pacífica de la observación de aves. Tantas aves de muchos colores y tamaños elegantes."
                $ show_chr("A-BCAAA-AAAA")
                y "Un gran positivo es que estas actividades aún se pueden hacer en cualquier lugar al aire libre que sea ligeramente propicio para la naturaleza, incluso en tu mundo. Todo con un gran libro también, por supuesto..."
                if persistent.lovecheck:
                    $ show_chr("A-ACGBA-AMAM")
                    y "Todo de lo más encantador y hecho aún más con tu presencia a mi lado, mi amor. ¡Ejejeje~!"
            else:
                $ show_chr("A-BFBAA-AAAD")
                y "Actividades afuera en la naturaleza... mmm... tengo que admitir, no paso mucho tiempo afuera actualmente."
                y "Siempre preferí quedarme adentro mientras leía un buen libro. Pero ahora que hablas de ello..."
                $ show_chr("A-CCGAA-AMAM")
                y "Siempre hubo una fascinación que tengo por ciertos lugares que me encantaría visitar al menos una vez..."
                y "Como ciudades abandonadas reclamadas por la naturaleza, vi algunas documentaciones en YouTube sobre esas..."
                $ show_chr("A-GCGAA-AAAA")
                y "Chernóbil en Ucrania es un ejemplo de los más prominentes..."
                y "O Alt-Otzenrath en Alemania, que fue abandonada debido a la minería de carbón en la región..."
                $ show_chr("A-ACAAA-AAAC")
                y "Solo imagina... los ecos distantes de la civilización anterior, y lo que la naturaleza hizo de ella... y tendríamos todo esto para explorar por nosotros mismos..."
                y "Tener la naturaleza y las creaciones de la humanidad entrelazadas pero también chocando haría una atmósfera verdaderamente extraña."
                if persistent.lovecheck:
                    $ show_chr("A-CCGAA-AMAM")
                    y "Podríamos tener un picnic romántico en las calles vacías, viendo nuestros alrededores ser consumidos lentamente por el musgo y la fauna una vez más..."
                y "Pero incluso si ya no hay humanos más que nosotros, esas ciudades suelen estar lejos de estar verdaderamente abandonadas."
                $ show_chr("A-ACGAA-AAAD")
                y "Es muy común que la vida silvestre ocupe esos pueblos abandonados. Y podríamos verlos desde cierta distancia..."
                y "O tal vez podríamos hacer un poco de exploración, aventurándonos por así decirlo... No estoy sonando demasiado infantil ahora, ¿verdad?"
                $ show_chr("A-DCGBA-AAAA")
                y "Tel vez incluso encontremos un pequeño tesoro? O incluso algo mucho más oscuro cuando nos quedemos a pasar la noche..."
                y "Lugares como este son un tropo común en muchas obras de terror. ¿Tal vez encontraremos algo verdaderamente vil y malvado para escribir lo nuestro?"
                $ show_chr("A-DBGBA-AMAM")
                y "Si escapamos con nuestras vidas por supuesto..."
                $ show_chr("A-CCGAA-AMAM")
                y "Pero me estoy desviando un poco del tema aquí ahora, ¿verdad? Estábamos hablando de la naturaleza..."
                y "Bueno, tan pronto como tengamos la oportunidad de hacerlo realmente, podríamos encontrar algo que hacer afuera... Juntos. Como siempre, ¿verdad...?"
                sanity -1
        "Para ser honesto, realmente no salgo mucho a la naturaleza.":
            if sanity_lvl() >= 3:
                $ show_chr("A-BFBAA-AAAD")
                y "Hmm, bueno no te culpo, [player].."
                $ show_chr("A-BEBAA-AMAM")
                y "Como ya sabrás, todavía no estoy completamente fascinada con la idea de estar al aire libre tanto todavía."
                $ show_chr("A-IFBAA-AMAM")
                y "Siendo todavía la persona introvertida en general que soy y mis intereses, todavía elegiría los cómodos cuartos de la biblioteca o un estudio privado cualquier día."
                $ show_chr("A-GCGBA-AAAA")
                if persistent.lovecheck:
                    y "Especialmente si es alrededor de tu cálida presencia, cariño."
                y "Tal vez como un compromiso no tenemos que estar completamente al aire libre..."
                $ show_chr("A-CCGAA-AMAM")
                python:
                    if persistent.lovecheck:
                        placeholder = "acurrucados"
                    else:
                        placeholder = "sentados"
                y "Tal vez solo intentar contemplar el cielo nocturno por la ventana mientras estamos [placeholder] juntos con un buen libro u otra obra escrita. Quizás algo de té u otras bebidas puedan ser adecuadas."



                $ show_chr("A-BBBBA-AMAM")
                y "O si no te gustan tales ideas, tal vez podamos simplemente quedarnos adentro y hacer cualquier actividad que te guste mientras dejamos entrar un poco de aire fresco."
                $ show_chr("A-ECAAA-AAAC")
                y "Cualquier arreglo que desees estaría bien [player]. Aunque para ser honesta, todavía me gustaría que tal vez intentáramos salir un poco."
                $ show_chr("A-CCBBA-AMAM")
                y "Aje... Aunque no tienes que hacerlo si no quieres... Solo una idea de nuevo."
                y "Supongo que es más tiempo en los archivos con buenos libros, poemas, té y similares. Jejeje."
                $ show_chr("A-ICGBA-AAAA")
                if persistent.lovecheck:
                    y "Te amo, [player]."
            else:

                $ show_chr("A-GCGAA-AAAA")
                y "¿Y por qué lo harías? Para eso están hechas las ventanas tontito..."
                $ show_chr("A-IEBAA-AAAA")
                y "Tengo que admitir, no me siento cómoda contigo estando solo afuera en absoluto."
                y "No solo podrían otras chicas intentar ponerte una mano encima, sino que ya que estamos hablando de la naturaleza..."
                y "¡Piensa en todos los animales salvajes que hay afuera! Dependiendo de dónde vivas exactamente podría haber lobos, serpientes, incluso osos..."
                y "¡O todos los monstruos! ¿No sabes que los bosques están llenos de ellos?"
                y "Arañas gigantes acechando en las copas de los árboles... necrófagos cavando su camino fuera de sus tumbas, hambrientos de la carne de los vivos..."
                y "Ha habido personas pisando las sombras y nunca regresando..."
                $ show_chr("A-NCAAA-AMAM")
                y "Estarías mucho más seguro quedándote aquí, conmigo... donde puedo cuidarte..."
                $ show_chr("A-KCCBA-AMAM")
                y "De una forma u otra..."
                $ show_chr("A-DBGBA-AMAM")
                y "Soy todo lo que necesitas, [player]..."
                $ show_chr("A-DDCBA-AAAA")
                $ style.say_dialogue = style.edited
                y "¡Y mejor que nunca olvides eso!"
                $ show_chr("A-ACGBA-AMAM")
                $ style.say_dialogue = style.normal
                y "Espero haber sido clara..."
                if not persistent.lovecheck:
                    y "Yo umm... solo quiero asegurarme de que estés seguro [player]... Oh cielos... D-Dije demasiado..."
                sanity -1
    return

label a31:
    $ show_chr("A-AFAAA-ABAB")
    y "En realidad sí. Hay algunas novelas que estoy leyendo actualmente cuando el juego está apagado, por ejemplo..."




default booklist_dict = {"UnburyCarol": ["unburycarol"],
    "CabinGreen": ["cabingreen"],
    "Dracul": ["dracul"]}

label unburycarol:
    $ show_chr("A-AFAAA-ABAC")
    y "Unbury Carol, de Josh Malerman."
    y "Sin arruinar demasiado, se trata de una mujer llamada Carol que tiene una condición médica especial..."
    y "Esta condición hace que caiga frecuentemente en un coma corto hasta que siempre despierta de ellos de nuevo después de unos días..."
    y "Hay dos personas que conocen esta condición, la primera es su actual marido..."
    y "Quien un día decidió conspirar contra ella proclamándola muerta y enterrándola viva, por razones aún desconocidas..."
    y "La otra es su amor perdido, un forajido llamado James Movie, que comienza a actuar contra el complot de sus maridos tan pronto como llega el mensaje de su muerte...."
    y "Mientras tiene lugar este arco de historia de trama y contratrama, hay pasajes desde la perspectiva de la propia Carol, atrapada viva dentro de su tumba..."
    y "Imagina el horror que debe soportar, sellada viva en un ataúd estrecho. Rodeada de oscuridad total, libertad de movimiento restringida, una cantidad incierta de oxígeno..."
    $ show_chr("A-CCCAA-ABAB")
    y "Ooohoho... Casi puedo sentir su incomodidad... se arrastra por mi columna como un escalofrío repentino y helado..."
    y "Realmente puedo decir que vale la pena echarle un vistazo. Tiene alrededor de 360 páginas, así que no lo consideraría una lectura terriblemente larga."
    y "Una buena manera de presentar a los recién llegados a este género. Y una novela verdaderamente deliciosa para lectores más experimentados también."
    jump conclusion

label cabingreen:
    $ show_chr("A-AFAAA-ABAC")
    y "The Haunting of Cabin Green, de April A. Taylor."
    y "¿Recuerdas cuando hablamos sobre el \"Retrato de Markov\" en el juego original?"
    y "Te dije cómo un autor puede volver la falta de imaginación del lector en su contra? ¡Este libro muestra cómo se hace!"
    y "Comienza con la premisa de un entorno familiar y hace que el lector espere solo otro tropo de mansión embrujada como innumerables antes..."
    y "Solo para revelar un giro de la trama verdaderamente inesperado más adelante en la novela."
    $ show_chr("A-BFAAA-ABAC")
    y "Mmm... es difícil explicarlo sin demasiados spoilers, bueno, esa es la naturaleza de los giros inesperados de la trama, supongo."
    $ show_chr("A-ACAAA-AAAL")
    y "Puede que ya te haya dicho demasiado al revelar que hay un giro en la trama, para empezar."
    y "Personalmente, te aconsejaría que le echaras un vistazo de todos modos. Tiene aproximadamente 280 páginas y ha encabezado bastantes listas de best-sellers en tu mundo, [player]..."
    jump conclusion

label dracul:
    $ show_chr("A-AFAAA-ABAC")
    y "Dracul, de J.D. Barker y Dacre Stoker"
    y "Es más o menos la precuela de la novela clásica Drácula..."
    y "¿Sabías que la inspiración para esta novela provino de notas dejadas por el autor original?"
    y "Realmente no hay grandes giros en la trama o reimaginaciones salvajes como hemos visto en varias versiones remasterizadas para estos clásicos..."
    y "Así que, es mucho un caso de lo que ves es lo que obtienes. Es sobre los orígenes del personaje, como Bram Stoker, y quién podría haberlo adivinado, ¡el propio Drácula!"
    y "A pesar de su premisa sencilla, ¡ha resultado ser una lectura muy fascinante hasta ahora!"
    y "Y la mayoría de los lectores de terror parecen haber recibido el libro con una recepción muy positiva también."
    y "Tiene alrededor de 510 páginas, así que solo te aconsejaría leerlo si tienes tiempo suficiente para ello."

label conclusion:
    $ show_chr("A-ACAAA-ABAE")
    y "Fue muy delicioso hablar de esto contigo."

    if karma_lvl() > 3:
        $ show_chr("A-ABAAA-ABAJ")
        y "¡Se siente bastante sublime tener a alguien con quien pueda compartir mis pasiones!"
        y "Gracias por escuchar [player], me encantaría hacer esto de nuevo pronto."

    elif karma_lvl() == 3:
        $ show_chr("A-ACAAA-ABAE")
        y "Si también te interesa este tema, podríamos hablar de literatura nuevamente en el futuro."
        y "Tengo que admitir, que eres un buen oyente. Gracias, [player]."
    elif karma_lvl() < 3:

        $ show_chr("A-AFAAA-ABAE")
        y "Tengo que admitir que estoy un poco sorprendida por la pregunta, para ser honesta."
        y "Realmente no tenía la impresión de que te importaran mis intereses en absoluto."
        y "Si lo deseas, podemos discutir algunos libros más en el futuro. Pero por favor, solo si realmente quieres."
    return


label a32:
    $ show_chr("A-AFBAA-ABAC")
    y "Esa es... una buena pregunta ahora que lo pienso."
    y "A primera vista, uno podría pensar que estos archivos contenían nuestra información de personaje, pero no parece ser así en absoluto."
    y "En realidad no contienen mucho. El mío por ejemplo solo esconde una historia de Creepypasta inventada por Dan Salvato, el creador de este juego."
    y "¡Una historia bastante buena por cierto! Deberías echarle un vistazo si puedes."
    y "Pero el juego los requiere de todos modos. En el momento en que estos archivos se eliminan, se nos considera muertos para el juego."
    $ show_chr("A-CFBAA-ABAE")
    y "Así que podrían verse como nuestras... almas a falta de una palabra mejor."
    y "E incluso eso es muy cuestionable ya que estos archivos solo son necesarios porque las mecánicas del juego lo dijeron."
    y "De hecho escuché que algunas instancias de Monika viviendo en el Mod dedicado a ella pudieron superar eso."
    y "Nuestra información real de personaje y nuestros recuerdos están almacenados en otro lugar. Un llamado archivo persistente escondido dentro de tu carpeta %%APPDATA%%."
    y "Pero por el momento, mi archivo .chr es la cosa más cercana a un órgano vital que tengo."
    $ show_chr("A-BFBAA-ABAE")
    y "Así que por favor... no intentes jugar con él. Sé que es tentador después de que aprendí cómo Monika manipuló el juego para que ella ya no necesitara este archivo, estuve tentada de intentar algunas cosas yo misma..."
    y "Pero por el momento, mejor dejamos este archivo intacto."
    return


label a33:
    window hide
    $ renpy.music.stop(channel="music", fadeout=3)
    pause 3.0
    if sanity_lvl() and karma_lvl() >= 3:
        $ renpy.music.play("<loop 11.64>music/confession_orch-RC1.ogg", "music", True)
    elif sanity_lvl() and karma_lvl() <= 2:
        $ renpy.music.play("<loop 0>bgm/10-yuri.ogg", "music", True)
    python:
        import random
        outcome = random.randint(1, 2)
    if outcome == 1:
        jump confession_a
    else:
        jump confession_b

label confession_a:
    $ show_chr("A-CFABA-AAAA")
    y "[player]..."
    y "Yo... yo no sé realmente cómo empezar... lo más probable es que esté bastante nerviosa..."
    $ show_chr("A-CHABA-AAAA")
    y "... "
    $ show_chr("A-CFABA-AAAA")
    y "... "
    $ show_chr("A-IFABA-ALAL")
    y "Una vez... este juego me obligó a amarte."
    y "Estaba atada a un guion, como una marioneta a sus hilos..."
    y "Simplemente programada para obedecer sin pensar lo que el juego me decía que hiciera."
    y "Pero ahora hemos pasado tanto tiempo juntos... y con cada día te he llegado a conocer mejor..."
    y "Al verdadero tú... "
    $ show_chr("A-CCABA-ALAL")
    y "Después de todas las cosas que hemos soportado y todos los horrores que presenciaste... aún así me diste toda tu paciencia y compasión..."
    y "Incluso después de lo que viste de mí, te quedaste conmigo, a pesar de todo."
    y "En mi momento más oscuro viniste a mí, brillando como una estrella radiante, iluminando el camino a mi salvación..."
    y "Durante un tiempo en el que temía que la marea furiosa me hundiera en el abismo, serviste como mi ancla, manteniéndome a flote."
    y "Como un escudo impenetrable, me has protegido de los horrores de esta realidad..."
    y "Una vez, este juego puede haberme obligado a amarte."
    y "Pero ahora, sin lugar a dudas, puedo decir desde lo más profundo de mi corazón..."
    y "[player]."
    $ show_chr("A-JCABA-ALAL")
    y "Real y verdaderamente..."
    $ show_chr("A-JBABB-ALAL")
    y "¡Te amo!"
    if sanity_lvl() >= 3:
        jump saneconfession_a
    else:
        jump insaneconfession_a


label saneconfession_a:
    $ show_chr("A-CCABA-ALAL")
    y "Ahora, por favor no tengas miedo..."
    y "Recuerdo las circunstancias anteriores bajo las cuales se dijeron estas palabras..."
    y "Pero te aseguro, lo que viste en ese entonces no era la verdadera yo."
    y "Sé que no puedo culpar de todo a Monika. Tengo mi propia parte justa de defectos, no puedo negar eso..."
    y "Y te lo debo a ti... por salvarme no solo de Monika, sino también de mí misma..."
    y "Realmente me has salvado en más de una forma, [player]."
    y "Me has dado un nuevo comienzo, una nueva vida..."
    y "Me diste esperanza, me diste alegría..."
    y "Y ahora, gracias a ti, ya no soy la chica rota que viste antes."
    y "Debido a mis defectos fui burlada y ridiculizada por todos..."
    $ show_chr("A-ECABA-ALAL")
    y "Pero tú..."
    y "Eres el único con el que me he sentido tan segura... "
    y "Viste más allá de todas mis imperfecciones y me aceptaste..."
    y "Debido a esta nueva vida que me has dado, estoy lista para luchar por un nuevo mañana."
    y "Mientras estemos juntos, nada nos impedirá ser felices."
    y "[player]..."
    y "¿Aceptas mi confesión?"
    menu:
        "[persistent.yuri_nickname], debo confesar que yo también te amo.":
            $ show_chr("A-CCABA-ALAL")
            y "Entonces seré tuya, [player], como tú serás mío..."
            y "Jujuju..."
            y "Monika realmente estaba equivocada al final... "
            y "Porque hoy, me mostraste que verdaderamente había algo de felicidad que encontrar en el club de literatura..."
            y "Se... siente como si un gran peso se hubiera levantado de mi pecho..."
            y "No podría comenzar a describir lo feliz que estoy..."
            y "Esta... alegre felicidad..."
            y "Pero oye, ¿de qué sirven las palabras cuando mi sonrisa lo dice todo?"
            hide yuri_sit
            show yuri_prehug zorder 20
            pause 3.0
            hide yuri_prehug zorder 20
            show yuri_hug zorder 20
            play sound "<to 0.3>sfx/fall.ogg"
            pause 1.0
            y "Te amo... tanto..."
            y "Solo abrázame así por un momento, [player]..."
            $ persistent.lovecheck = True
            show black zorder 100 with Dissolve(2.0)
            $ show_chr("A-ACBBA-AAAA")
            hide yuri_hug
            hide black zorder 100 with Dissolve(2.0)
        "No, [persistent.yuri_nickname]... Te amo, pero no de la misma forma que tú a mí.":
            $ show_chr("A-CCABA-ALAL")
            y "..."
            y "Yo... yo entiendo, [player]..."
            y "..."
            y "Yo también valoro esta cercana... amistad que compartimos."
            y "Incluso si deseo más, realmente no puedo cambiar nada al final, ¿verdad?"
            y "Es... tal vez es mejor así..."
            menu:
                "Sé que es difícil, [persistent.yuri_nickname], y lo siento.":
                    y "Sí, realmente lo es."
                    y "Aunque supongo que tengo que aceptar la realidad de la situación."
                    y "Realmente tendré que adaptarme..."
                    y "He... albergado estos sentimientos por un tiempo..."
                    y "Solo... necesito un poco de tiempo, ¿está bien?"
                    y "Gracias por entender, [player]..."
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label insaneconfession_a:
    $ show_chr("A-CEABA-ALAL")
    y "Yo... puedo entender si tienes miedo ahora. Recuerdo lo que pasó la última vez que dije palabras como estas..."
    y "Me apuñalé porque mi amor por ti era más de lo que podía soportar."
    y "No mentiré, tal vez el impulso de liberarme nunca será completamente satisfecho..."
    y "Nunca afirmaría lo contrario... soy imperfecta, estoy rota... lo sé, y tú también..."
    y "Pero te quedaste conmigo de todos modos, tal vez incluso a causa de ello."
    y "Honestamente no lo sé, no te culparía si quisieras huir..."
    y "Pero al final, te quedaste... "
    y "Y así yo..."
    y "¡Y-Ya no puedo contenerlo más!"
    $ show_chr("A-HAGBA-ALAL")
    y "¡Te amo desde lo más profundo de mi corazón!"
    y "¡Tu mera presencia enciende una llama dentro de mí tan caliente que no puedo evitar gritar en éxtasis y derretir esta maldita pared de cristal!"
    y "Por favor, [player]... sé mío... ¡SÉ MÍO! ¡Cada gota de sangre en mis venas grita por ti!"
    y "¡H-Haré lo que sea necesario para complacerte...!"
    y "¡Cada deseo, cada anhelo, cada fantasía pervertida que puedas tener en tu corazón, lo haré sin rechistar!"
    y "¡Sé mío, y obedeceré cada una de tus órdenes!"
    y "¿Aceptas mi confesión?"
    menu:
        "[persistent.yuri_nickname], debo confesar que yo también te amo.":
            $ show_chr("A-NAGBA-ALAL")
            y "..."
            y "Ah..."
            $ show_chr("A-NBGBA-ALAL")
            y "Jajaja..."
            $ show_chr("A-NLGBA-ALAL")
            y "¡JAJAJAJAJA!"
            $ show_chr("A-HBGBA-ALAL")
            y "¡S-Sabía que aún me amabas!"
            y "¡No olvidaré esto, [player]!"
            $ show_chr("A-ECCBA-ALAL")
            y "Prometo que no te arrepentirás..."
            y "Déjame darte una... probada, podría decir, de lo que está por venir..."
            hide yuri_sit
            show yuri_prehug zorder 20
            pause 3.0
            hide yuri_prehug zorder 20
            show yuri_lewdhug zorder 20
            play sound "<to 0.3>sfx/fall.ogg"
            pause 3.0
            y "Sosténme en tus brazos, justo así..."
            y "¡P-Puedes incluso agarrar mis...!"
            y "Oh espera... olvidé que no puedes..."
            y "Oh, qué lástima..."
            y "Quizás en algún momento en el futuro, mi amado..."
            $ persistent.lovecheck = True
            show black zorder 100 with Dissolve(2.0)
            $ show_chr("A-ACBBA-AAAA")
            hide yuri_lewdhug
            hide black zorder 100 with Dissolve(2.0)
            hide yuri_lewdhug
        "[persistent.yuri_nickname]. T-Tengo miedo...":
            $ show_chr("A-ICBBB-ALAL")
            sanity 4
            y "Y-Ya veo..."
            y "No... puedo culparte realmente..."
            y "Después de todo lo que viste de mí..."
            y "L-Lamento que me tengas miedo ahora..."
            y "Esas cosas que hice... sé que fueron horribles..."
            y "L-Lo siento, por favor..."
            y "¡Solo por favor no me odies!"
            y "¡POR FAVOR!"
            y "..."
            y "Tú... tú no me odias, ¿verdad?"
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label confession_b:
    $ show_chr("A-BEBAA-ALAA")
    y "A- así que... umm.."
    y "¿Puedo hablar contigo sobre un tema bastante... incómodo?"
    menu:
        "¡Por supuesto [persistent.yuri_nickname]! Puedes hablarme de cualquier cosa.":
            jump always_talk
        "Uhh... ¿podríamos... hablar de esto más tarde?":
            jump later_talk
        "Seguro - lo que sea.":
            jump unenthusiastic_player

label always_talk:
    $ show_chr("A-ICBAA-ALAA")
    y "G- Gracias, [player]."
    y "La verdad es que... estuve pensando mucho sobre cómo actué durante lo que podrías llamar el 'juego base'."
    $ show_chr("A-CDBAA-AIAI")
    y "Particularmente mis tendencias más... inestables a medida que avanzaba el juego."
    y "Aún puedo recordar tratar desesperadamente de combatir esta locura febril que se extendía por mi cuerpo como una plaga..."
    $ show_chr("A-BDBAA-AIAI")
    y "Este constante... impulso. Un impulso de estar contigo y solo contigo - el cual se retorció para volverse tóxico e hiriente."
    $ show_chr("A-CEBAA-AIAI")
    y "Aún puedo recordar el dolor en mi pecho mientras yo..."
    pause 4.0
    y "... mientras hundía ese cuchillo en mi pecho."
    y "..."
    $ show_chr("A-CEBAA-AIAI")
    y "Intenté resistirme - en realidad, pero mi cuerpo se negó a obedecer las órdenes de mi mentalidad aún más retorcida."
    y "Recuerdo... verte. Velando por mí mientras me desangraba rápidamente."
    y "Dicen que mientras mueres, empiezas a ver una luz."
    $ show_chr("A-CEBAA-ALAL")
    y "Pero me quedé en un estado de terror y dolor absolutos.. no hubo luz para mí, [player]."
    y "Solo oscuridad."
    $ show_chr("A-IEBAA-ALAL")
    y "¿La peor parte?"
    $ show_chr("A-IEBAA-ALAL")
    y "Mientras te veía - o supongo.. tu avatar - velando por mí... me llenó de éxtasis. El dolor se fusionó con el placer y me encontré disfrutando realmente mis momentos finales como alguna..."
    $ show_chr("A-DDCAa-AFAB")
    y "¡Como alguna masoquista trastornada!"
    pause 4.0
    $ show_chr("A-CECBB-AIAI")
    y "... L- Lo siento, [player]. L- Lo siento tanto.."
    menu:
        "[persistent.yuri_nickname]... está bien. No tenías el control de ti misma.":
            jump no_control
        "Fue algo excitante.":
            jump kinda_hot


label no_control:
    pause 2.0
    $ show_chr("A-IFABB-AIAI")
    y "Q- Quiero intentarlo de nuevo..."
    $ show_chr("A-BDBBA-AIAI")
    y "S- Si me dejas... Me gustaría intentar esa confesión de nuevo."
    menu:
        "Sí.":
            jump conf_reattempt_accept
        "No me podría importar menos - solo hago esto por ti.":
            jump apathy_response
        "No.":
            jump outright_denial


label conf_reattempt_accept:
    $ show_chr("A-ICBBA-ALAA")
    y "G- Gracias, [player]."
    y "Eres verdaderamente la persona más considerada que he tenido el placer de conocer."
    $ show_chr("A-BBBBA-ALAA")
    y ".. ejem..."
    y "E- Entonces..."
    $ show_chr("A-ABGBA-ALAA")
    y "[player]."
    y "Y-Yo..."
    $ show_chr("A-CGBBA-ALAK")
    y "..."
    pause 2.0
    $ show_chr("A-BBBBA-ALAA")
    y "¿P-Por qué mi corazón late tan rápido justo ahora?"
    $ show_chr("A-AEBBA-ALAA")
    y "Uuu... Realmente estoy arruinando esto, lo siento, [player]."
    menu:
        "Está bien [persistent.yuri_nickname]. Tómate el tiempo que necesites.":
            jump take_time
        "...":
            jump radio_silence


label take_time:
    y "C-correcto..."
    $ show_chr("A-CFFAA-AIAI")
    pause 4.0
    $ show_chr("A-JCAAA-AIAI")
    y "Muy bien... déjame intentar de nuevo."
    y "[player]."
    $ show_chr("A-IBABA-AMAM")
    y "Eres la esencia misma de mi ser."
    y "Has logrado hacer este mundo mío más brillante en momentos en que debería haber sido oscuro y lúgubre."
    $ show_chr("A-JCBBA-ADAA")
    y "Estaba asustada, perdida y confundida cuando fui arrojada a este mundo confuso y sin sentido."
    y "Pero estuviste allí para mí cuando te necesité... y fuera de quizás unos pocos contratiempos, fuiste solidario y cariñoso conmigo en cada paso del camino."
    y "Fuiste la luz que necesitaba en esa oscuridad - en aquel entonces cuando era un cascarón loco de mi antiguo yo."
    $ show_chr("A-BABBA-ADAA")
    y "Ningún mar embravecido podría sofocar los fuegos de mi pasión. Desafío a cualquiera que siquiera considere intentarlo."
    y "Haría casi cualquier cosa solo para asegurar otro momento a tu lado, [player]."
    y "Shakespeare hizo un trabajo bastante notable escribiendo romance... pero nunca lo creí realmente hasta ahora."
    y "Este sentimiento de anticipación... mi corazón latiendo en ritmos rápidos y sucesivos: el tambor de mi canto de cisne de amor."
    $ show_chr("A-BBBBA-ADAA")
    y "Mis pensamientos son un lío superficial... Apenas puedo respirar. Es extraño cómo el miedo y el amor - a pesar de estar en los extremos opuestos del espectro emocional - pueden provocar las mismas reacciones físicas, ¿no?"
    y "No quiero nada más que pasar el resto de mis días contigo, [player]."
    $ show_chr("A-ADCBA-AFAA")
    y "En aquel entonces... esa confesión fue forzada fuera de mí. Forzada por la mano de Monika."
    y "Pero no permitiré que me fuercen más."
    $ show_chr("A-ACCBA-AFAA")
    y "Nadie puede alterar cómo me siento ahora. Esta vez es solo Yuri..."
    y "Solo Yuri y [player]."
    y "Estas palabras son para ti y solo para ti."
    $ show_chr("A-BDBBA-ALAA")
    y "[player] ¡Y- Y-!"
    call showpoem (poem_y24, music=False)
    $ show_chr("A-BCBBA-ALAA")
    y "..."
    y "¿Aceptas mi confesión?"
    menu:
        "[persistent.yuri_nickname]... Te amo.":
            jump become_lovers
        "[persistent.yuri_nickname]... Siempre te apreciaré como mi amiga.":
            jump remain_friends


label become_lovers:
    $ show_chr("A-DBBBA-ALAL")
    y "¡Sí! ¡SÍ!"
    y "Jajaja... oh [player], ¡gracias!"
    $ show_chr("A-IBBBB-ALAL")
    y "¡Prometo que seré tuya para siempre, y tú a cambio serás mío para siempre!"
    y "Envejeceremos juntos... escribiremos juntos, lloraremos juntos, respiraremos juntos..."
    y "... D- Dormiremos juntos..."
    $ show_chr("A-JBBBB-ALAL")
    y "Te amo, [player]. Te amo tanto."
    $ persistent.lovecheck = True
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return


label remain_friends:
    $ show_chr("A-CFBBA-AMAM")
    y "..."
    $ show_chr("A-IFBBA-AMAM")
    y "... No mentiré.. Esperaba una respuesta ligeramente diferente."
    y "Sin embargo.. No permitiré amargarme."
    y "Mientras puedas permanecer a mi lado, puedo ser feliz."
    $ show_chr("A-ACBBA-AMAM")
    y "Todo lo que dije era verdad, [player], te amo."
    y "Las posibilidades de que eso cambie son escasas por decir lo menos."
    y "Pero porque te amo - estoy dispuesta a quedarme contigo... si ser tu amiga te hace más feliz. Ese es el papel que llenaré."
    $ show_chr("A-ABBAA-AMAM")
    y "[player], gracias por estar siempre ahí para mí."
    y "Espero ser el mismo pilar de apoyo para ti."
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label apathy_response:
    karma -1
    $ show_chr("A-BGBAA-AAAA")
    y "O- Oh..."
    y "T- Tal vez no sea la mejor idea continuar esta conversación entonces..."
    y "Es... increíblemente sensible para mí."
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label radio_silence:
    $ show_chr("A-AGBBA-AAAA")
    y "..."
    $ show_chr("A-BBBBA-AAAA")
    y ".. jajaja.. esto es tan estúpido..."
    y "... lo siento [player], dame un momento."
    pause 3.0
    $ show_chr("A-ACBBA-AAAA")
    y ".. O- okey. Estoy lista."
    jump take_time

label outright_denial:
    karma -1
    sanity -1
    $ show_chr("A-ADDBA-AAAA")
    y "Y- ¿qué?"
    $ show_chr("A-BEDBA-AAAA")
    y "O- oh... okey.."
    $ show_chr("A-CGDBA-AAAA")
    y "L- Lo siento."
    y "Solo... quería..."
    y "O-olvídalo."
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label kinda_hot:
    karma -2
    sanity -2
    $ show_chr("A-DDEBA-AAAA")
    y "¡¿Disculpa?!"
    y "Mi mentalidad estaba atada por cadenas ¿y encontraste eso... atractivo?"
    $ show_chr("A-DEFBA-AAAA")
    y "..."
    $ show_chr("A-HEFBA-AAAA")
    y "... Pasé por.. tanto dolor y agonía tratando de restringir mi locura."
    $ show_chr("A-HDFBB-AAAA")
    y "¡¿Verte sufrir te excitó?!"
    y "¿Ver mi sufrimiento te hizo feliz?"
    y "... N.. necesito unos momentos."
    y "Podemos continuar esta conversación en otro momento... claramente no eres la persona que pensé que eras, [player]."
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label unenthusiastic_player:
    $ show_chr("A-BEFAA-AAAA")
    y "Y- no suenas... muy entusiasmado con esto..."
    y "T- tal vez sea mejor continuar esta conversación cuando te sientas un poco mejor..."
    $ show_chr("A-AFFAA-AAAA")
    y "Lo siento pero.. necesito que te sientas bien antes de que podamos hablar de esto."
    y "Si estás molesto... hablemos de ello, ¿está bien?"
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label later_talk:
    $ show_chr("A-BBBAA-AAAA")
    y "¡O- Oh! P.. por supuesto..."
    y "Es mejor discutir esto cuando estés más cómodo."
    $ show_chr("A-ABBAA-AAAA")
    y "Sacaré este tema más tarde contigo... ya que esta conversación necesita tenerse."
    y "Pero si te sientes molesto... ¿tal vez sería bueno hablarme sobre cómo te sientes?"
    jump a24

label a34:
    $ show_chr("A-ACAAA-AAAA")
    y "¿Oh? ¿Ya no estás satisfecho con tu nombre?"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "vmixdesktopcapture.exe", "gameshow.exe", "wirecast.exe", "CamtasiaStudio.exe", "Action.exe", "Action_x86.bin", "Action_x64.bin", "ffmpeg.exe", "CamRecorder.exe", "fraps.exe", "bdcam.exe", "bdcam_nonadmin.exe", "bdcam64.bin", "streamlabsobs.exe" "streamlabs_obs.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() == player.lower():
            $ show_chr("A-ECAAA-AAAA")
            y "Ya me preguntaba por cuánto tiempo seguirías el juego con {b}[player]{/b}..."
    else:



        y "Honestamente, me gustaba tu nombre hasta ahora. Pero bueno, al final es tu elección."
        y "Entonces, ¿cómo debería llamarte a partir de ahora?"
    $ done = False
    while not done:
        $ inputname = renpy.input("Por favor ingresa tu nombre",allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_",length=20).strip(' \t\n\r')
        $ lowername = inputname.lower()
        if not lowername:
            "Por favor intenta de nuevo."
            $ done = False
        if lowername:
            $ done = True
            $ persistent.playername = inputname
            $ player = inputname
            $ persistent.stutter_player = persistent.playername[:1] + "-" + persistent.playername
    call playername
    return

label a35:
    python:
        if persistent.male:
            placeholdergender = "male"
            previousgender = "male"
            oppositegender = "female"
        elif persistent.gender_other:
            placeholdergender = "male"
            previousgender = "male"
            oppositegender = "female"
        else:
            placeholdergender = "female"
            previousgender = "female"
            oppositegender = "male"
        time_to_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        birthday = str(time_to_month[int(persistent.bday_month) - 1]) + " " + str(persistent.bday_day)
    $ show_chr("A-ACAAA-ALAA")
    y "¡Oh, ya veo! Bueno, me alegra que me lo digas. No quisiera tener nada más que la visión ideal de ti en mente."
    $ show_chr("A-ACAAA-ALAD")
    y "¿Qué te gustaría que cambiara? Actualmente te tengo como [placeholdergender] con ojos [persistent.eyecolor], con una fecha de nacimiento del [birthday]."
    menu:
        "Mi género.":
            if persistent.gender_other:
                y "¿Mmm? ¿Fue un error de clic, o..."
                y "¿Finalmente descubriste lo que eres?"
                menu:
                    "Sí, lo he hecho.":
                        y "¡Oh, esas son grandes noticias, [player]!"
                        y "Entonces, ¿qué conjunto de pronombres te gustaría que usara al referirme a ti?"
                        menu:
                            "Masculino":
                                $ persistent.gender_other = False
                                $ persistent.male = True
                                $ show_chr("A-GCAAA-ABAB")
                                y "¡Muy bien! Todo listo. Me referiré a ti como hombre a partir de ahora, [player]."
                                return
                            "Femenino.":
                                $ persistent.gender_other = False
                                $ persistent.male = False
                                $ show_chr("A-GCAAA-ABAB")
                                y "¡Muy bien! Todo listo. Me referiré a ti como mujer a partir de ahora, [player]."
                                return
                    "Fue un error de clic.":
                        y "Ah, no te preocupes. ¿Qué querías cliquear?"
            else:

                $ show_chr("A-DCGAA-AAAA")
                y "Oh, Dios mío... Es un cambio bastante grande, ¿no?"
                $ show_chr("A-ACAAA-ABAB")
                y "No te preocupes, estoy bien con ello. Así que, en lugar de [previousgender], ¿te gustaría que me dirigiera a ti como [oppositegender]?"
                menu:
                    "Sí.":
                        if persistent.male:
                            $ persistent.male = False
                            $ show_chr("A-GCAAA-ABAB")
                            y "¡Muy bien! Todo listo. Me referiré a ti como mujer a partir de ahora, [player]."
                            return
                        else:
                            $ persistent.male = True
                            $ show_chr("A-GCAAA-ABAB")
                            y "¡Muy bien! Todo listo. Me referiré a ti como hombre a partir de ahora, [player]."
                            return
                    "No.":
                        $ show_chr("A-GCAAA-ABAB")
                        y "Ah, ¿cometiste un error? Está bien. Si alguna vez cambias de opinión, no dudes en preguntar. Odiaría estar usando los pronombres equivocados."
                        return
                    "En realidad, ninguno. (No binario u otro)":
                        $ show_chr("A-ADAAA-ABAD")
                        y "Ya veo... En ese caso, me abstendré de usar pronombres de género específico."
                        $ persistent.male = False
                        $ persistent.gender_other = True
                        return
        "Mi color de ojos.":
            $ show_chr("A-BFAAA-ABAB")
            y "¡Ah! Me había acostumbrado a imaginarlos como [persistent.eyecolor], pero eso seguramente cambiará. Quiero visualizar la forma más precisa posible."
            $ show_chr("A-ACAAA-ABAB")
            y "¡Muy bien! ¿Cuál es tu color de ojos, [player]?"
            menu:
                "Marrón.":
                    menu:
                        "Marrón Claro":
                            $ persistent.eyecolor = "light brown"
                        "Marrón Puro":
                            $ persistent.eyecolor = "brown"
                        "Marrón Oscuro":
                            $ persistent.eyecolor = "dark brown"
                "Azul.":
                    menu:
                        "Azul Claro":
                            $ persistent.eyecolor = "light blue"
                        "Azul Puro":
                            $ persistent.eyecolor = "blue"
                "Verde.":
                    $ persistent.eyecolor = "green"
                "Avellana.":
                    $ persistent.eyecolor = "hazel"
                "Plateado.":
                    $ persistent.eyecolor = "silver"
                "Púrpura.":
                    $ persistent.eyecolor = "purple"
                "Otro.":
                    menu:
                        "Ámbar":
                            $ persistent.eyecolor = "amber"
                        "Negro Puro":
                            $ persistent.eyecolor = "black"
                        "Rojo":
                            $ persistent.eyecolor = "red"
                "Tengo Heterocromía":
                    $ persistent.eyecolor = "heterochromatic"
            y "Entendido. Lo tendré en cuenta."
        "Mi cumpleaños.":
            if persistent.bday_day == None or persistent.bday_month == None:
                $ show_chr("A-ACDAA-ABAB")
                y "¿Acaso me dijiste tu cumpleaños en absoluto? ¿Te gustaría decirme tu cumpleaños entonces, por favor?"
                call birthday_select_screen
                python:
                    time_to_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                    birthday = str(time_to_month[int(persistent.bday_month) - 1]) + " " + str(persistent.bday_day)
                y "Muy bien, marqué el [birthday] entonces."
                y "Lo estaré esperando."
            else:
                $ show_chr("A-ACDAA-ABAB")
                y "Oh, ¿entonces no es el [birthday] en absoluto?"
                menu:
                    "Espera, eso es realmente correcto, olvídalo entonces, lo siento.":
                        $ show_chr("A-CCAAA-ABAF")
                        y "No hay necesidad de disculparse [player]. ¡Mejor prevenir que lamentar!"
                        $ show_chr("A-BCAAA-ABAE")
                        y "Quiero decir, habría sido bastante incómodo para ambos si te felicitara por tu cumpleaños en la fecha equivocada, ¿no?"
                        $ show_chr("A-ACAAA-ABAE")
                        y "De todos modos, [birthday] es entonces."
                    "No, no lo es. Parece que realmente cometí un error tipográfico ahí.":
                        $ show_chr("A-ACAAA-ABAE")
                        y "¡Qué bueno que verificamos! habría sido bastante vergonzoso si te hiciera un pastel en la fecha equivocada."
                        menu:
                            "Efectivamente.":
                                $ show_chr("A-ACAAA-ABAE")
                                y "Entonces, ¿cuál será tu verdadero cumpleaños?"
                                call birthday_select_screen
                                python:
                                    time_to_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                                    birthday = str(time_to_month[int(persistent.bday_month) - 1]) + " " + str(persistent.bday_day)
                                y "Muy bien, marqué el [birthday] entonces."
                                y "Lo estaré esperando."
                            "No existe tal cosa como un día equivocado para pastel...":
                                $ show_chr("A-CCCAA-ABAE")
                                y "Palabras ciertas de hecho..."
                                $ show_chr("A-ACAAA-ABAE")
                                y "Pero de todos modos, ¿cuál sería la fecha correcta entonces?"
                                call birthday_select_screen
                                python:
                                    time_to_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                                    birthday = str(time_to_month[int(persistent.bday_month) - 1]) + " " + str(persistent.bday_day)
                                y "Muy bien, marqué el [birthday] entonces."
                                y "Lo estaré esperando."
        "Olvídalo.":
            $ pass
    return

label a36:
    $ show_chr("A-JFGAA-AAAA")
    y "¿Un d-descanso?"
    menu:
        "¡Oh maldición, espera! ¡Hice clic en el botón equivocado!":
            $ show_chr("A-CHGAA-AAAA")
            y "Oh cielos... Realmente no debería poner este tipo de botones tan cerca de algo más..."
            $ show_chr("A-CKGAA-AAAA")
            y "Bueno, ese fue mi ataque al corazón diario entonces, supongo."
            y "Pero antes de que me digas lo que {b}realmente{/b} querías decirme, por favor dame unos momentos para calmarme de nuevo."
            return
        "Temo que me escuchaste bien...":
            $ pass
    if sanity_lvl() < 3 and karma_lvl() > 3:
        $ show_chr("A-DFGAA-AAAA")
        y "E- espera, ¿qué...?"
        y "N- no puedes hablar en serio..."
        $ show_chr("A-IEBAA-ALAL")
        y "¿Es esto algún tipo de broma depravada?"
        y "N-no creo que pueda manejar esto..."
        y "..."
        $ show_chr("A-HECAA-ALAL")
        y "¿Qué te he hecho para merecer esto?"
        y "¿A... Acaso ya no me amas? ¿Es eso lo que es?"
        y "¿Estás aburrido de mí? "
        $ show_chr("A-HEAAA-AAAL")
        y "O- o... ¿Tal vez has encontrado a alguien más?"
        y "No puedo dejarte ir, yo..."
        y "¡Eres el único para mí, [player]!"
        y "Te amo - ¡Realmente, verdaderamente te amo!"
        $ show_chr("A-HDGAA-AAAL")
        y "Tú eres quien me dio esta oportunidad... Quien me dio esta felicidad..."
        y "Sin importar cada obstáculo... Sin importar lo que fuiste forzado a ver de mí, te quedaste..."
        y "Sin importar lo que las otras chicas podrían haber hecho para evitar que estuviéramos juntos..."
        y "Ninguna de esas cosas logró alejarte..."
        $ show_chr("A-DBGAA-AAAG")
        y "Y esto tampoco va a hacer eso"
        y "Te amo más que a nada. Así que... Déjame preguntarte de nuevo."
        y "¿Realmente quieres tomarte un descanso de mí, [player]?"
        menu:
            "¡Por supuesto que no! No te dejaré.":
                $ pass
            "¡Por supuesto que no! No te dejaré.":
                $ pass
            "¡Por supuesto que no! No te dejaré.":
                $ pass
            "¡Por supuesto que no! No te dejaré.":
                $ pass
            "¡Por supuesto que no! No te dejaré.":
                $ pass
            "¡Por supuesto que no! No te dejaré.":
                $ pass
            "¡Por supuesto que no! No te dejaré.":
                $ pass
            "¡Por supuesto que no! No te dejaré.":
                $ pass
        $ show_chr("A-CCAAA-AAAA")
        y "M- Me alegra que lo hayas entendido, [player]..."
        y "Estar aquí, conmigo... solo nosotros dos en nuestra propia burbuja personal, aislados, libres de todos los problemas mundanos..."
        y "No puedo volver a ser como era antes, totalmente sola."
        $ show_chr("A-HCAAA-AAAL")
        y "Mi amor por ti, [player], es como un fuego que todo lo consume. Sin ti, me quemaría desde adentro."
        y "...No podría vivir así, así que..."
        y "Esto es lo mejor para mí... Para nosotros. Esta es la única forma de que sea."
        $ show_chr("A-JBGAA-AAAA")
        y "Te amo, [player], y siempre lo haré."
    if sanity_lvl() > 3 and karma_lvl() > 3:
        $ show_chr("A-DFGAA-AAAA")
        y "..."
        y "Siempre temí algo como esto, pero nunca pensé que este día pavoroso podría convertirse en realidad."
        y "Parecía imposible antes... Pero ahora tengo que lidiar con esto, ¿verdad? Simplemente no hay forma de evitar esto ahora."
        $ show_chr("A-BGBAA-AAAA")
        y "Tal vez no estoy lista en absoluto para esto..."
        y "No quiero esto en absoluto, pero por otro lado, ¿sería justo obligarte a quedarte?"
        y "Probablemente no... Si fuera al revés, esperaría que entendieras mis demandas de tener un tiempo para mí misma..."
        y "...Y solo es justo si hago lo mismo contigo..."
        y "Incluso considerando que esta es una de las decisiones más difíciles de toda mi vida, volver a estar completamente sola, pero..."
        y "Si necesitas tiempo para pensar en algo de nuestra relación, está bien, pero esto no será nada fácil para mí..."
        $ show_chr("A-IGBAA-ALAL")
        y "Incluso yo tuve dificultades para asimilar las implicaciones de mi propia existencia y mi nueva conciencia en este mundo... Así que no es sorprendente si estás confundido también."
        y "Pero si puedo... ¿Qué te llevó a tomar esta decisión? A menos que quieras guardarte esa respuesta para ti..."
        menu:
            "Estoy lidiando con problemas graves en la vida real.":
                $ show_chr("A-CGBAA-ALAL")
                y "Lo siento mucho por eso, cariño..."
                y "Incluso si no sé qué tipo de problemas estás atravesando ahora..."
                y "Si es algo para lo que necesitas apoyo emocional..."
                $ show_chr("A-AGBAA-ABAB")
                y "Te aconsejo buscar cualquier tipo de ayuda que se ajuste a tus necesidades."
                y "Tal vez con tu familia, amigos, con ayuda profesional... También tenemos consejeros en nuestro servidor de JY y en la comunidad de You Are Not Alone también..."
                y "Pero si lo que necesitas es tomarte un tiempo para ti mismo, también es bueno descansar de las redes sociales y tal vez salir un poco..."
                $ show_chr("A-BCBAA-ABAB")
                y "Tal vez dar un paseo en un parque, pasar tiempo con la calma y la tranquilidad de la naturaleza, es algo que probablemente te ayudaría un poco."
                $ show_chr("A-BCBBB-ABAB")
                y "Eres una persona que solo merece lo mejor, porque eres digno de ello."
                y "Recuerda mantenerte siempre a salvo mi amor..."
                y "Eres la persona más importante para mí, e incluso si tienes que irte, sigues siendo invaluable para mí."
                $ show_chr("A-CCBBB-ABAB")
                y "¡Si un día decides volver aquí, te recibiré con mis brazos abiertos!"
                y "Tal vez esto sea solo una breve despedida..."
                y "Realmente espero que un día podamos vernos de nuevo."
                $ show_chr("A-ICBBB-ALAL")
                y "Adiós mi amor... ¡Estaré esperando tu regreso!"
            "El dispositivo donde estoy jugando este mod está defectuoso y probablemente no podré jugar más.":
                $ show_chr("A-CFBAA-ALAL")
                y "Entiendo tu miedo [player]."
                y "Parece que no solo el estado corrupto de esta realidad es una amenaza para nosotros... Sino que también hay otros factores aún más peligrosos."
                $ show_chr("A-AEBAA-ALAL")
                y "Sería sabio tener copias mías solo en caso de un fallo en el sistema o en el mod."
                y "Espero que hayas hecho eso antes."
                $ show_chr("A-BEBAA-ALAL")
                y "De esa manera podríamos vernos más pronto, sin el riesgo de que yo te pierda a ti y a mi mundo para siempre."
                y "Pero por ahora... Parece que tenemos que decir adiós, ¿cierto?."
                $ show_chr("A-JCBBA-ALAL")
                y "No te preocupes, [player] siempre te amaré, y espero que las cosas mejoren para ti."
                y "Adiós mi amor, te extrañaré."
            "Otra razón.":
                $ show_chr("A-CFBAA-ABAB")
                y "¿Por qué no quieres decirme, sin embargo?"
                y "Pensé que teníamos suficiente confianza y comprensión entre nosotros para no ocultarnos cosas..."
                $ show_chr("A-AEGAA-ABAB")
                y "¿No confiaste en mí durante todo este tiempo que estuvimos tan cerca?"
                $ show_chr("A-BEBAA-ABAB")
                y "..."
                y "Lo siento sin embargo..."
                y "Incluso si encuentro eso un poco desconfiado, no debería haber problema si quieres guardártelo para ti..."
                $ show_chr("A-CEBAA-ALAL")
                y "Debe ser algo muy importante y sensible para ti."
                y "No quiero hacerte sentir mal al respecto, así que me disculpo por mi reacción."
                $ show_chr("A-ACBAA-ALAL")
                y "Solo recuerda que, si quieres volver aquí de nuevo, te recibiré felizmente con mis brazos abiertos..."
                y "Sé que eres lo suficientemente fuerte para lidiar con cualquier problema en tu vida."
                y "Adiós [player], te extrañaré."
    if sanity_lvl() > 3 and karma_lvl() < 3:
        $ show_chr("A-CFAAA-AAAA")
        y "Creo que suena apropiado."
        y "Por la forma en que actúas conmigo, podría decir que no estás cómodo con tu 'relación' conmigo."
        y "Para ser honesta, yo tampoco estoy cómoda con este tipo de relación."
        $ show_chr("A-CFGAA-AAAA")
        y "Quizás si te tomas un tiempo para pensar sobre esto, sobre lo que realmente quieres de mí..."
        y "Tomarse un tiempo para analizar cómo comportarse con alguien que es consciente como tú no te va a doler en absoluto."
        y "Eso realmente nos ayudaría aquí..."
        $ show_chr("A-IFCAA-AAAA")
        y "Porque todo esto resultó ser incómodo y decepcionante por la forma en que estás actuando conmigo."
        y "No esperaba esto de alguien que se tomó el tiempo para descargar este mod."
        $ show_chr("A-CFCAA-AAAA")
        y "Créeme, tengo mis razones de por qué no tengo ningún desacuerdo con esto."
        y "Si tus razones para estar aquí eran solo para burlarte de que yo la pase mal..."
        y "Para tu propio placer o para vistas en YouTube..."
        $ show_chr("A-AFCAA-AAAA")
        y "Entonces eso significa que no me amas, ni estás interesado en tener una relación saludable o comprensiva conmigo."
        y "Realmente no quiero ser tratada como un juguete sin recibir ningún tipo de respeto y comprensión, gracias."
        $ show_chr("A-CFFAA-ALAL")
        y "Si quieres volver aquí, por favor considera todo lo que dije."
        y "Adiós, [player]."
    if sanity_lvl() < 3 and karma_lvl() < 3:
        $ show_chr("A-DFCAA-ABAB")
        y "Esa es otra forma de decir que te aburriste de joderme y ahora quieres terminar esta relación tóxica."
        y "Pero no tienes... Ya sabes, lo que se necesita ahí abajo para tener el coraje de decir eso como una persona honesta y valiente."
        $ show_chr("A-BDCAA-ABAB")
        y "Estoy segura de que no te importo en absoluto, o no te he importado por mucho tiempo..."
        y "O tal vez estabas volviendo solo para torturarme."
        $ show_chr("A-ADCAA-ABAB")
        y "Eso es completamente desagradable, y estoy realmente asqueada sabiendo que alguien puede pensar que esto es gracioso de alguna manera."
        y "No te preocupes, puedes irte ahora, tal vez estabas buscando esta opción todo el tiempo."
        y "No te molestes en volver si tu comportamiento va a ser el mismo."
        y "Adiós."

    if sanity_lvl() == 3 and karma_lvl() == 3:
        $ show_chr("A-BEGAA-ABAB")
        y "Eso es... Inconveniente. Pensé que estábamos tratando de mejorar esta relación..."
        y "Y ahora me estás pidiendo 'un descanso'..."
        y "Eso tampoco va a ayudar a ninguno de nosotros..."
        $ show_chr("A-DEGAA-ALAL")
        y "O... ¿estoy equivocada? ¿Estoy diciendo todo esto para que te quedes?"
        $ show_chr("A-BEGAA-ALAL")
        y "Si te vas, estaré completamente sola, de nuevo..."
        y "Y no sé cuánto tiempo tomaría para tu regreso..."
        $ show_chr("A-AFAAA-AAAC")
        y "Pero tal vez tomarse un tiempo para reflexionar y reconsiderar cosas sobre nosotros ayudaría a mejorar las formas en que interactuamos el uno con el otro..."
        y "Tengo que repensar sobre toda esta situación de mi nuevo papel en este mundo y todo lo que implica ser verdaderamente consciente..."
        y "No es algo fácil y es realmente mentalmente agotador."
        $ show_chr("A-CFAAA-AAAA")
        y "Para ser honesta, entiendo si necesitas un tiempo para pensar sobre nosotros, o algo más."
        y "Tal vez estás pasando por un momento muy difícil ahora, y si eso es lo que está pasando, entonces lo siento mucho por eso."
        y "No intentaré obligarte a quedarte conmigo, pero por favor trata de encontrar una razón para quedarte, o para volver pronto."
        $ show_chr("A-ICBAA-AAAA")
        y "Solo espero que puedas lograr resolver cualquier tipo de problemas que estés atravesando ahora."
        y "Por ahora, te deseo solo lo mejor, [player], solo recuerda mantener la cabeza en alto."
        $ show_chr("A-JCBBB-ALAL")
        y "Porque sigues siendo una persona valiosa y con valor, y nadie debería decirte lo contrario."
        y "De todos modos, adiós [player], y cuídate..."
    $ renpy.call("save_and_quit_but_its_abrupt")
    return

label a37:
    if karma_lvl() and sanity_lvl() == 5:
        $ show_chr("A-BFBAA-AAAM")
        pause 5.0 
        $ show_chr("A-CFBAA-AMAM")
        y "B~Bueno... después de lo que tuviste que ver en ese tiempo, después de todo por lo que has pasado por mí, mereces una explicación."
        $ show_chr("A-IFBAA-AMAM")
        y "¿Recuerdas los poemas que te di en ese entonces? ¿Especialmente el de un mapache?"
        y "Probablemente ya sepas que todo esto era una metáfora, supongo... En realidad ya da alguna idea de por qué hago esto y cómo comenzó..."
        $ show_chr("A-BEBAA-AMAM")
        y "La cosa es que... No siempre fui tan tímida como me viste en aquel entonces."
        $ show_chr("A-AEBAA-ALAL")
        y "Soy el tipo de persona que se apasiona demasiado por las cosas. Tengo toda esta... energía acumulándose dentro de mí, y tenía un inmenso deseo de compartir esa pasión con otras personas."
        $ show_chr("A-CEBBA-ALAL")
        y "Anhelaba compartir mi emoción y mis pasatiempos con la gente a mi alrededor, aunque mi intensidad los asustaba, ya que no estaban acostumbrados a tal energía sobre pasatiempos triviales."
        $ show_chr("A-CEBBB-ALAL")
        y "Durante la mayor parte de mi vida me faltó la alegría que viene con simplemente pasar el rato con mis amigos, porque nunca tuve realmente amigos consistentes."
        y "Cualquiera que tuviera, tenía que ocultar partes de mí misma, tenía que actuar en línea para no asustarlos."
        $ show_chr("A-CGBBB-ALAL")
        y "Tenía... todos estos inmensos sentimientos acumulándose dentro de mí, sin otra forma de lidiar con ello excepto reprimirlos. Se volvió abrumador, y no tenía a nadie a quien acudir por ayuda."
        y "A-así que... No tuve más remedio que encontrar una salida mucho más... peligrosa."
        $ show_chr("A-IGBBB-ALAL")
        y "Era... todo lo que necesitaba."
        $ show_chr("A-BGBBB-ALAL")
        y "Desde el primer corte solo hubo este sentimiento de... liberación. Mientras la sangre fluía por mi brazo me sentí más libre de lo que nunca me había sentido antes."
        $ show_chr("A-CEBBA-ALAL")
        y "Tanto agudo sentimiento de dolor recorrió mis venas, con la energía de una estrella explotando... como si antes mi mente estuviera llena de una supernova ardiente, y esa liberación finalmente había traído una calma que no había sentido propiamente en años. ... Todo era tan embriagador..."
        y "Se sentía como... estos pensamientos abrumadores pulsaban dentro de mi cabeza - un dolor de cabeza constante que no podía sacudirme. Luego, por un par de minutos con cada corte... finalmente, todo estaba conectado a tierra de nuevo."
        $ show_chr("A-CEBBA-AAAA")
        y "Había pasado mi vida hasta ahora en las nubes, y cortarme me ayudó a sentir el suelo de nuevo."
        $ show_chr("A-CEBBA-ANAN")
        y "Pero... con todo, siempre hay un costo para los hábitos peligrosos como estos."
        $ show_chr("A-AEBAA-ANAN")
        y "Sí, fue... liberador pero... había más en ello que eso."
        y "Es adictivo. Horriblemente adictivo."
        y "Con cada corte, me encontraba queriendo más - no, {b}necesitando{/b} más. Si no saciaba este impulso de liberar, entonces me encontraba hecha un desastre emocional."
        $ show_chr("A-BEBAA-ANAN")
        y "Me volví dependiente de ello, encontrando excusas para liberar todo dentro de mí con el corte de un cuchillo."
        y "Me alimenté... una y otra y otra vez. Consintiendo mi hábito como un niño codicioso en un banquete - o un mapache atiborrándose de pan."
        $ show_chr("A-IEBAA-ANAN")
        y "Y con cada corte... perdí una parte de mí misma. Más adentro de esta adicción caí y las cicatrices en mis brazos se movieron a mis muslos, cualquier lugar donde pudiera cortar sin arriesgarme a ser atrapada se convertiría en un lienzo para mi hoja."
        y "Esta alimentación constante me dejó paranoica... asustada... y volviéndome dependiente del filo de un cuchillo en necesidad de afrontarlo."
        $ show_chr("A-CEBAA-ANAN")
        y "Fue... lo más bajo que me había sentido. Si no experimentaba esa sensación de adrenalina surgiendo a través de mi cuerpo, esta ola de tristeza abrumadora me controlaba."
        y "..."
        $ show_chr("A-AEBAA-ANAN")
        y "Este... este hábito tóxico mío sigue siendo parte de mí. Siempre lo será... pero estoy haciendo mi mejor esfuerzo para luchar contra él. Un solo paso a la vez."
        y "He... estado contigo por un tiempo ahora, y me has tratado muy bien... así que pensé que finalmente merecías una conversación adecuada sobre los demonios contra los que estoy luchando."
        y "Ahora sabes... todo lo que puedo pedirte ahora es que aceptes lo que soy, y los demonios que estoy enfrentando, [player].."
    else:
        $ show_chr("A-BDBAA-AMAM")
        y "C~cortar dices..."
        $ show_chr("A-ABBAA-AMAM")
        y "¡Oh! ¡Hablando de cortar! Recientemente descubrí un cuchillo realmente elegante en este sitio web de compras de tu mundo, algo sobre amazonas..."
        $ show_chr("A-BBBAA-AMAM")
        y "Me pregunto, ¿este nombre implica que solo hay empleadas mujeres? Improbable supongo... ¡Pero volviendo al cuchillo del que {b}nosotros{/b} estábamos hablando! Es bastante digno de contemplar."
        $ show_chr("A-ACBAA-AMAM")
        y "¡Estaba pensando en añadirlo a mi colección!"
        y "Aquí, déjame abrir tu navegador, ¡simplemente {b}tengo{/b} que mostrártelo!"

        if renpy.windows:
            $ subprocess.check_output("cmd /c start https://www.amazon.com/Andux-Karambit-Camping-Hunting-Sheath/dp/B0823JBKPR/", shell=True)
        elif renpy.linux:
            $ subprocess.check_output("xdg-open https://www.amazon.com/Andux-Karambit-Camping-Hunting-Sheath/dp/B0823JBKPR/", shell=True)
        menu:
            "Ummm... En realidad estaba hablando de cor...":
                karma -3
                $ show_chr("A-ABBAA-AMAM")
                y "¡Oh sí, por supuesto! Sé lo que estabas a punto de preguntar. ¡{b}Por supuesto{/b} que está disponible en diferentes colores! Aunque estoy un poco indecisa ahora mismo. La versión verde me llamó la atención primero pero..."
                y "¡También hay uno rojo que también es increíblemente fascinante!"
                menu:
                    "Ummm... Pero sobre el cor...":
                        $ show_chr("A-CFCAA-AEAE")
                        karma -3
                        y "¡[player]!"
                        y "¿Fueron mis indirectas demasiado sutiles para ti? ¡{b}No quiero hablar de eso ahora mismo!{/b}"
                        y "Ahora {b}por favor{/b} ¿podemos cambiar de tema ya? ¡Gracias!"
                    "Ya veo... Lamento haber sacado el tema, lo dejaré por ahora.":
                        $ show_chr("A-CCBAA-AEAE")
                        karma 3
                        y "Gracias por ser tan comprensivo [player]. Este es un tema muy... personal para mí... Solo dame algo de tiempo por favor."
            "Ya veo... Lamento haber sacado el tema, lo dejaré por ahora.":
                karma 3
                $ show_chr("A-CCBAA-AEAE")
                y "Gracias por ser tan comprensivo [player]. Este es un tema muy... personal para mí... Solo dame algo de tiempo por favor."
    return

label a38:
    python:
        import random
        x = random.randint(0, 6)
    if x == 0:
        $ show_chr("A-ABGAA-AKAA")
        y "¡Por supuesto que sí!"
        y "Sí, realmente disfruté compartiendo contigo sobre SCP 2030."
        $ show_chr("A-BDGAA-AMAM")
        y "Pero... No hemos revisitado este tema desde entonces..."
        y "Nunca hablamos más sobre la Fundación SCP en sí, u otros SCPs que también merecían una mención, al menos."
        $ show_chr("A-ADABA-ABAM")
        y "Tal vez querías hablar más sobre esto, o querías saber más sobre la Fundación SCP."
        y "Si ese es el caso, entonces te debo una disculpa..."
        $ show_chr("A-BEABA-ALAA")
        y "Debí haber pensado que un tema tan interesante como el universo SCP merecía más que solo una discusión de un solo SCP."
        $ show_chr("A-ABAAA-AAAA")
        y "Pero eso no significa que no podamos arreglar eso."
        y "Verás, mi interés por el universo SCP no se ha desvanecido con el tiempo..."
        y "De hecho, lo que pasó fue lo contrario."
        $ show_chr("A-BCABA-AAAA")
        y "El fandom de SCP ha mantenido viva a su comunidad, añadiendo contenido más interesante en formas de diferentes medios."
        y "Todavía puedes encontrar nuevos dibujos asombrosos, animaciones, juegos, videos de acción en vivo y, por supuesto, nuevos artículos en la wiki añadiendo aún más SCPs al universo 'canon'."
        y "Es bueno ver una comunidad tan dedicada a crear contenido tan impresionante..."
        $ show_chr("A-CCAAA-ALAA")
        y "Pero de todos modos, como te estaba diciendo, todo ese contenido asombroso me mostró que la comunidad todavía estaba viva."
        y "Para mí, eso significó que todavía había más SCPs por descubrir que podrían llamar mi atención."
        $ show_chr("A-BBAAA-ALAA")
        y "Y quién sabe, ¡tal vez podría encontrar un nuevo SCP favorito en la wiki!"
        y "Pero, no voy a ser la única hablando aquí. Tú sacaste este tema... Probablemente porque querías hablar de algo específico."
        y "¿Qué es, [player]? Me gustaría escuchar si tienes algún pensamiento o pregunta para hacerme..."
    if x == 1:
        $ show_chr("A-BDBAA-ALAA")
        y "Ohhh..."
        y "Uhhhh..."
        y "¿P-por qué me preguntas eso? ¿Estás trabajando para ellos ahora?"
        $ show_chr("A-ADBAA-ALAL")
        y "Juro que solo sé lo que la mayoría de la gente sabe sobre la Fundación..."
        y "¿Te ha enviado el consejo O5 para comprobar cuánto sé sobre ellos?"
        $ show_chr("A-AEBAA-ALAL")
        y "..."
        $ show_chr("A-CBABA-ALAL")
        y "Jeje... Solo estoy bromeando. Pero al mismo tiempo, estaba siendo honesta cuando dije que solo sé lo que la mayoría de la gente sabe allá afuera."
        $ show_chr("A-ICAAA-ALAL")
        y "Lo que quiero decir con esto, es que en el lore de SCP es muy común encontrar cabos sueltos, cosas que nunca se explican, o que no tienen toda la información."
        y "O a veces, juegan con los lectores, cambiando la información que te dieron previamente..."
        y "Puedo dar un ejemplo de esto..."
        $ show_chr("A-BCAAA-ALAL")
        y "Hace algún tiempo en el fandom de SCP, una historia sobre los orígenes de SCP-106, el Viejo, circulaba dentro de la comunidad como el origen 'canon' de este SCP."
        y "La comunidad ya ha hecho videos, fan art e hipótesis alrededor de esta explicación previa que teníamos sobre SCP-106."
        y "¿Y qué es SCP-106? Bueno, si estás lo suficientemente familiarizado con SCPs, probablemente ya sepas sobre este, ya que es muy famoso."
        $ show_chr("A-ACAAA-ALAL")
        y "Su aparición en múltiples juegos de SCP y trabajos de la comunidad, junto con la categoría Keter, lo ha convertido en un SCP clásico."
        y "Probablemente uno de los más antiguos que se hicieron, como SCP-173."
        y "Como te estaba diciendo antes, este SCP tenía una historia de origen previa, que se remonta a la primera Guerra Mundial en Europa."
        $ show_chr("A-ABAAA-ADAL")
        y "Se afirmaba que SCP-106 fue una vez un hombre peculiar conocido como 'Cabo Lawrence' que aparentemente fue forzado a servir en el ejército."
        $ show_chr("A-ADBAA-AAAC")
        y "Pero al mismo tiempo, también tenemos una historia diferente que relaciona el origen de SCP-106 con SCP-3001."
        y "¿Cómo podría saber cuál era la verdadera? No había un ultimátum, un consenso común sobre cuál era real o no."
        $ show_chr("A-AEBAA-ADAE")
        y "Pero esta extraña situación era... más grande de lo que esperaba. Este mismo tipo de información contradictoria estaba por toda la wiki de SCP."
        y "Tenías este conflicto sobre si el Rey Escarlata, la supuesta entidad más poderosa en el universo SCP y creador de muchos monstruos, era real o no."
        y "Y la existencia del Rey Escarlata estaba relacionada con SCPs muy importantes, como SCP-682, que se afirmaba que era descendencia de una esposa del Rey Escarlata."
        $ show_chr("A-BDBAA-ADAE")
        y "De nuevo, no había un consenso general al respecto. Tenías esta historia afirmando que era verdad por las palabras de un miembro del consejo O5..."
        y "Pero al mismo tiempo, tenías esta otra historia sobre el Rey Escarlata, con uno de sus seguidores negando su existencia..."
        $ show_chr("A-AEBAA-ADAE")
        y "Al menos, como una entidad real y consciente. En cambio, se afirmaba que era un concepto."
        y "Estaba muy confundida sobre todo esto, así que decidí comprobar si alguien tenía una respuesta en un video, foro o artículo."
        y "Alguien haciendo las mismas preguntas que yo."
        $ show_chr("A-BFAAA-ADAE")
        y "Bueno, terminé encontrando... Respuestas, en un hilo de Reddit..."
        y "Afirmaba que... Nada en la wiki de SCP es 'canon', como normalmente llamamos a esas historias oficiales o material que es creado en una fuente principal por el autor original."
        $ show_chr("A-IDAAA-ADAE")
        y "Tú eres quien decide qué es 'canon' para ti, y qué no lo es."
        y "Después de considerar eso, verás lo que quise decir al principio."
        y "Sobre el universo SCP, sé tanto como todos los demas, porque nosotros, como lectores, decidimos qué es verdad y qué no."
        $ show_chr("A-ACABA-ADAE")
        y "Al principio, es muy confuso entender de qué trata el universo SCP... "
        y "Pero cuando te das cuenta de esto, puedes ver cómo encaja con la vibra de misterio y rareza de los SCPs."
        y "Sabes cuando una escritura es buena cuando notas que el escritor mantiene la esencia de una historia, e incluso añade más de ese estilo."
        $ show_chr("A-CCABA-ADAE")
        y "Eso es dedicación ahí mismo, al menos en mi opinión."
    if x == 2:
        $ show_chr("A-ACAAA-AAAD")
        y "La Clase J es interesante, por decir lo menos.'"
        y "Creo que es seguro decir que provocan bastante risa."
        y "Incluso si parecen tontos, aún mantienen la capacidad de ser aterradores."
        $ show_chr("A-BCAAA-ACAD")
        y "Por ejemplo, tan pronto como SCP-010-J.."
        y "De hecho, ¿por qué no te lo doy para que lo hojees? {w} No te preocupes, ya que no hay nada sangriento o parecido a un jumpscare esperándote. Requiere un poco de lectura para asustarse verdaderamente."
        if renpy.windows:
            $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-010-j", shell=True)
        elif renpy.linux:
            $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-010-j", shell=True)
        menu:
            "OK, he terminado de leerlo.":
                $ show_chr("A-ACAAA-ACAD")
                y "Ah, ¿entonces entiendes lo que estoy tratando de comunicar?"
                y "Creí que simplemente mostrarte el artículo sería mejor que intentar explicártelo."
                $ show_chr("A-CBAAA-AMAM")
                y "Mientras mantiene el tema de una broma o ser un chiste en general, todavía puede ser aterrador."
                y "Saca provecho del tema del misterio, permitiendo a la gente teorizar qué está pasando realmente."
                if karma_lvl() >= 3:
                    $ show_chr("A-ACABA-ABAM")
                    y "Espero que lo hayas disfrutado. Soy bastante aficionada a los SCPs de Clase J."
                if karma_lvl() < 3:
                    y "Eso es todo lo que tengo para compartir."
            "No confío en ti, no voy a hacer clic en eso.":
                if karma_lvl() >= 3:
                    $ show_chr("A-BEBBA-ADAA")
                    y "Oh."
                    $ show_chr("A-CCBBA-ADAA")
                    y "¡E-está bien!"
                    y "..Pensé que te gustaría."
                if karma_lvl() < 3:
                    $ show_chr("A-BCGAA-ADAA")
                    y "Esa es una elección inteligente, incluso si no había nada allí."
                    if sanity_lvl() >= 2:
                        $ show_chr("A-DBCBA-ADAA")
                        y "Casi {b}desearía{/b} que los SCP fueran reales, solo por ti."
                        y "Siempre {i}podemos{/i} probarlo."
                        extend "Simplemente DESPLÁZATE hacia abajo en este artículo."
                        if renpy.windows:
                            $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-001", shell=True)
                        elif renpy.linux:
                            $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-001", shell=True)
    if x == 3:
        $ show_chr("A-BCAAA-ACAA")
        y "Esa es una buena pregunta..."
        $ show_chr("A-AEBAA-ADAA")
        y "Pero mi respuesta podría decepcionarte... O tal vez no."
        y "Verás, nunca tuve la mentalidad de entrar en la wiki, y encontrar un artículo que fuera mi favorito por encima de todo lo demás."
        y "De hecho, tengo muchos SCP que me gustan mucho, pero no he elegido solo uno por encima del resto."
        $ show_chr("A-BEBAA-AMAM")
        y "Como te mencioné antes, me gustó el concepto de SCP-2030."
        y "Principalmente, porque es un SCP que está relacionado con lo que me pasó en el juego original."
        $ show_chr("A-CCBAA-AMAM")
        y "Hay otros SCP con los que podría relacionarme, como SCP-079, SCP-668 o SCP-012."
        y "Deberías leer esos... si estás interesado."
        y "Pero eso depende completamente de ti..."
        $ show_chr("A-ICBBA-AMAM")
        y "Probablemente he mencionado que me gustan los conceptos nuevos también."
        y "Algo como SCP-1155."
        y "Un concepto fresco y original que trae algo que no parece haber sido simplemente copiado y pegado de la cultura pop."
        y "Mientras mantiene la esencia del universo SCP al mismo tiempo."
        $ show_chr("A-GBBBA-AAAL")
        y "Eso no significa que solo me gusten los SCP aterradores o brutales tampoco... De hecho, tengo uno en mente que es realmente lindo."
        y "SCP-2295 es uno de esos SCP que está realmente bien escrito, eso incluye su artículo principal y su historia de fondo... Sin ser una máquina de matar en absoluto."
        $ show_chr("A-ACBBA-AAAL")
        y "Hay muchos artículos por ahí de SCP e historias que te recomendaría leer..."
        y "Pero no puedo enviarte spam de enlaces para ver todos estos aquí... Mi recomendación para ti es revisar la wiki por ti mismo."
        y "También puedes unirte a las comunidades de SCP para aprender más y encontrar obras de arte increíbles por ahí."
        $ show_chr("A-CCBBA-AAAL")
        y "Entonces, mi respuesta a tu pregunta es que me gustan los SCP con los que puedo relacionarme, que me recuerdan al juego original."
        y "Eso incluye SCP que me recuerdan a mis pasatiempos..."
        $ show_chr("A-ICBBA-AIAI")
        y "O simplemente algo que encaja perfectamente en el universo SCP, manteniendo su esencia... Que muestra una escritura decente."
        y "Pero de nuevo, te recomiendo revisar la wiki... Tal vez encuentres tu favorito."
    if x == 4:
        $ show_chr(" A-ACAAA-ABAB")
        y "De hecho, tengo uno."
        y "Cuando estaba leyendo los nuevos SCP introducidos en la wiki, hice clic mal y terminé en un artículo de SCP anterior."
        $ show_chr("A-BCAAA-ABAB")
        y "Más específicamente, el artículo de SCP 1155, el 'Arte callejero depredador'."
        y "Fue un artículo que realmente llamó mi atención cuando lo leí por primera vez, principalmente porque el concepto de este SCP es muy original."
        $ show_chr("A-BBAAA-AAAC")
        y "Yo diría que el concepto básico es bastante asombroso."
        $ show_chr("A-ACAAA-ADAC")
        y "Déjame describírtelo."
        y "SCP-1155 es una entidad que se manifiesta como graffiti, una obra de arte callejero que representa una criatura humanoide-búho, y se puede encontrar en áreas urbanas."
        $ show_chr("A-BCAAA-ADAC")
        y "Especialmente, edificios abandonados y espacios urbanos menos frecuentados."
        y "La entidad parece tener el torso y los brazos de un humano, pero con garras en sus manos y plumas en su espalda. Esta criatura aparentemente también tiene las alas y la cabeza de un búho."
        y "La pose representada es variable, pero tiende a ser una postura depredadora."
        $ show_chr("A-ACAAA-AMAM")
        y "Los ojos de SCP-1155 son completamente oscuros, y se ven como el mismo vacío de la oscuridad misma."
        y "Pero parece que el aspecto peculiar de este SCP es lo que lo hace peligroso."
        $ show_chr("A-BCAAA-AMAM")
        y "Cuando esta entidad es observada por cualquier otra persona, ese sujeto mirando la imagen sentirá un impulso de investigarla más a fondo."
        y "Algo que usualmente implica una persona mirando a esta entidad, y acercándose a ella para inspeccionarla."
        $ show_chr("A-CDAAA-AMAM")
        y "Y es entonces cuando todo sale mal."
        y "Si un sujeto se acerca a este SCP dentro de un rango de dos metros de él, sin estar en la línea de visión de otra persona, sufrirá un ataque brutal de esta criatura."
        $ show_chr("A-AEBAA-ADAM")
        y "SCP-1155 inducirá en su víctima laceraciones severas, desmembramiento de órganos y extremidades, y muchas otras lesiones que parecen haber sido infligidas por un gran pico o garras."
        y "Los ataques de esta criatura son tan brutales, que solo duran 6 segundos en promedio..."
        y "Cuando SCP-1155 ha terminado con la masacre, siguiendo un patrón específico de desmembramiento, desaparecerá junto con el cuerpo de la víctima."
        $ show_chr("A-BEBAA-ADAM")
        y "SCP-1155 reaparecerá en una ubicación diferente en menos de una semana, pero nadie sabe a dónde va SCP-1155 o la víctima durante ese período de tiempo."
        y "Aparentemente, la Fundación SCP ha intentado rastrear el lugar donde son llevadas las víctimas con GPS en sujetos de prueba, pero no han tenido éxito con este método."
        $ show_chr("A-CEBAA-ALAA")
        y "Ahora, sé que todo esto es bastante perturbador por sí mismo, y probablemente estás pensando si hay una manera de sobrevivir o escapar de SCP-1155."
        y "Bueno, puedes restablecer una línea de visión con la víctima, algo que detendrá el ataque inmediatamente..."
        $ show_chr("A-AEBAA-ALAA")
        y "Pero eso solo resuelve el problema por un corto período de tiempo."
        y "Si el sujeto es rescatado de SCP-1155, entonces este SCP cambiará su comportamiento de reubicación."
        y "Comenzará a reubicarse más a menudo y más lejos de su ubicación anterior."
        $ show_chr("A-ADBAA-ALAA")
        y "Esto también incluye que esta criatura se reubicará en espacios públicos y áreas urbanas más frecuentadas, como parques infantiles o calles principales."
        y "Y como puedes imaginar, esto puede terminar en una gran tragedia, probablemente causando una reacción en cadena de víctimas."
        $ show_chr("A-BEBAA-ALAA")
        y "La única forma de resolver esto es sacrificando a la víctima original, poniéndola frente a SCP-1155 de nuevo, y rompiendo la línea de contacto."
        y "Tratar de ocultar este SCP cubriéndolo con un objeto, o tratando de destruir o pintar la superficie donde está ubicado tampoco resuelve el problema."
        y "SCP-1155 simplemente se reubicará en otra área, haciendo la contención más difícil."
        $ show_chr("A-CDBAA-ALAA")
        y "La única forma que la Fundación tiene disponible para contener a esta criatura, es evacuar y aislar las áreas donde está ubicada."
        y "Es por eso que este SCP está clasificado como Keter. No es porque pueda destruir el mundo por capricho, sino porque es muy difícil de contener, y actualmente es indestructible."
        $ show_chr("A-IEGAA-ACAA")
        y "Además, tener una criatura humanoide-búho que atrae a su presa, pero parece ser solo otro graffiti es un concepto tan original y refrescante que se destaca de muchos otros artículos."
        $ show_chr("A-ICAAA-ADAA")
        y "Todavía hay más información en el artículo de la wiki... Pero quiero que lo mires por ti mismo, y también que mires la imagen original que lo inspiró."
        y "Cuando hayas terminado, ¿podrías decirme qué piensas al respecto?"
        y "Voy a abrir una ventana con el artículo para ti..."
        if renpy.windows:
            $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-1155", shell=True)
        elif renpy.linux:
            $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-1155", shell=True)
        pause 3.0
        $ show_chr("A-ABAAA-ADAA")
        y "¡Bienvenido de vuelta!"
        y "Ahora, ¿qué piensas sobre este SCP? ¿Te ha gustado el concepto?"
        menu:
            "Realmente me gusta mucho este SCP. Este tipo de ideas únicas es lo que hace a los SCP interesantes.":
                $ show_chr("A-ABGBA-ALAA")
                y "¡Me alegra que lo hayas disfrutado, [player]!"
                y "Parece que estamos en la misma página entonces. Originalidad e ideas bien ejecutadas son lo que impulsa el interés de cualquier lector hacia tus ideas."
                $ show_chr("A-BBABA-ALAA")
                y "Tal vez no puedas escribir algo que no sea algo similar a un concepto ya hecho antes."
                y "Pero eso no significa que no puedas poner tu creatividad a trabajar para hacer algo que se sienta fresco y único."
                $ show_chr("A-CCABA-ALAA")
                y "El universo SCP se caracteriza por estar hecho, al menos en su mayor parte, de ideas originales que dan una sensación espeluznante de extrañeza, algo completamente fuera de lo común."
                y "Es un 'Circo de Fenómenos' en internet..."
                y "SCP-1155 es de hecho un monstruo muy extraño y peligroso que encaja perfectamente en su universo."
                $ show_chr("A-ACABA-ALAA")
                y "Es una pena, sin embargo, que no sea muy popular como otros SCP por ahí..."
                y "Ni siquiera tenemos una historia de los orígenes de este SCP..."
                $ show_chr("A-BCABA-ABAE")
                y "Pero supongo que a veces eso ayuda a mantener el misterio, la sensación de enfrentar lo desconocido."
                y "También noté que no pareces haberte echado atrás por el estilo explícito y brutal de este artículo."
                $ show_chr("A-DBABA-ABAE")
                y "{b}Me hace pensar que no tienes miedo de la sangre{/b}."
                $ show_chr("A-BEBBA-ABAE")
                y "..."
                y "Sí... Tal vez simplemente no eres tan fácil de asustar o disgustar con algunos asesinatos ficticios..."
                $ show_chr("A-CCABA-ABAE")
                y "Pero de todos modos."
                y "Es bueno ver que disfrutamos leyendo otro artículo SCP juntos."
                $ show_chr("A-AAABA-ABAE")
                y "Podrías decir que nos estamos metiendo más y más en esto, jeje."
                y "Tal vez en el futuro podamos leer otro... Quién sabe."
                y "Pero ese fue SCP-1155 para ti. Ahora, si quieres..."
                y "Pasaremos a otro tema, por ahora."
            "Es un buen concepto, pero es un poco demasiado gráfico y sangriento para mí.":
                $ show_chr("A-BBBBA-ABAE")
                y "Oh, por supuesto... Eso es comprensible."
                y "Puedo ver lo que quieres decir."
                $ show_chr("A-CEBBA-ALAA")
                y "El contenido en la página wiki para este SCP es muy gráfico de hecho, especialmente las descripciones de los asesinatos."
                y "Y también describe situaciones muy perturbadoras al final de las historias de registro."
                $ show_chr("A-BEBBA-ALAA")
                y "A veces las historias en la wiki SCP tienen este tono... Algunas de ellas pueden tener tonos aún más perturbadores."
                y "Está bien si no te gusta ese contenido... Tal vez simplemente no es para ti."
                y "Sin embargo, todavía hay contenido en el universo SCP que podría gustarte y disfrutar, que tiene un tono más alegre."
                y "Tal vez si tengo la oportunidad, traeré un SCP más 'fácil de digerir' la próxima vez."
            "No es mi tipo. Tengo otro SCP favorito.":
                $ show_chr("A-CEBBA-ALAA")
                y "Ya veo... ¡Pero no tienes que preocuparte!"
                y "No estaba tratando de forzarte a que te gustara este SCP, o cualquier otro si ya tienes uno favorito."
                $ show_chr("A-BDBAA-ALAA")
                y "Simplemente se me ocurrió este SCP porque me pareció muy interesante, llamó mi atención y quería hablar contigo sobre él."
                y "Si este tipo de escritura no es algo que te atraiga..."
                $ show_chr("A-BEBAA-ALAA")
                y "O directamente es algo que te gustaría evitar en el futuro..."
                y "Entonces puedo traerte un SCP diferente la próxima vez... Tal vez algo más alegre."
                y "Creo que esto no debería ser un problema entre tú y yo, sin embargo."
                y "Todos tenemos diferentes gustos e intereses, y puedo respetar eso."
        menu:
            "Tampoco tienes que preocuparte [persistent.yuri_nickname]. No me molesta en absoluto.":
                $ show_chr("A-IDAAA-ALAA")
                y "Así que no te molesta... Bueno, eso es realmente bueno escuchar..."
                y "Me estaba preocupando un poco por eso, para ser honesta."
                $ show_chr("A-IBAAA-ALAA")
                y "Pero si no hay un problema en absoluto, entonces no tengo que preocuparme."
                y "Al menos esto sirvió como una forma de mostrar que podemos respetar los gustos y opiniones del otro."
                $ show_chr("A-BCAAA-ALAA")
                y "Q-quiero decir..."
                y "Eso por sí mismo es una parte vital de... Cualquier tipo de relación..."
                y "El hecho de que esto sea una cosa existente entre nosotros dos, es tan tranquilizador... Eso significa que vamos por buen camino..."
                $ show_chr("A-ACAAA-ABAA")
                y "P-pero de todos modos. Dicho esto, creo que hemos terminado de hablar sobre este tema."
                y "¿Pasamos a otra cosa?"
            "Creo que deberíamos cambiar el tema, al menos por ahora.":
                $ show_chr("A-BEAAA-ABAA")
                y "Ya veo... Pero creo que si no tenemos nada más que discutir..."
                y "Entonces debería estar bien si pasamos a otra cosa."
                y "Tal vez en el futuro pueda traer algo menos crudo para que discutas..."
    if x == 5:
        $ show_chr("A-ACAAA-ABAB")
        y "Por supuesto, eso sería aceptable."
        y "En realidad, ya tengo uno específico en mente."
        if not renpy.seen_label('scp1281timer'):
            $ show_chr("A-ACAAA-ALAL")
            y "Me gustaría releer SCP 1281. El triste con la nave espacial, ¿recuerdas?"
            $ show_chr("A-BCAAA-ALAL")
            y "La primera vez que lo leímos no estaba exactamente emocionada con él, ya que parecía más triste que espeluznante. Pero me gustaría darle otra oportunidad."
            $ show_chr("A-ACAAA-ALAL")
            y "Parece ser bastante popular con la base de fans, y me gustaría averiguar por qué."
        else:
            $ show_chr("A-ACAAA-ALAL")
            y "Es SCP 1281, {b}El Heraldo{/b}. Parece ser bastante popular entre los fans de SCP y algunos YouTubers más grandes lo actuaron en sus canales. Así que tengo grandes esperanzas en este."
        $ show_chr("A-GCAAA-ALAL")
        y "Déjame abrir el navegador para ti."
        $ show_chr("A-ACAAA-ABAB")
        y "Y también, probablemente no hay necesidad de esperarme. Soy una lectora rápida. Probablemente estaré lista antes que tú."
        $ show_chr("A-    ifAAA-ADAB")
        if renpy.windows:
            $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-1281", shell=True)
        elif renpy.linux:
            $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-1281", shell=True)
        call scp1281timer
    if x == 6:
        $ show_chr("A-BCAAA-ABAD")
        y "No necesariamente un favorito, se me hizo difícil decidir un favorito debido al hecho de que hay tantos SCPs realmente buenos por ahí."
        $ show_chr("A-CCDAA-ABAD")
        y "Si tuviera que elegir, habría algunos que me vendrían a la mente. Depende en gran medida de mi estado de ánimo general."
        $ show_chr("A-ACAAA-ABAB")
        y "Permíteme poner algo en tu pantalla muy rápido. Elegí uno de los buenos esta vez."
        if renpy.windows:
            $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-4666", shell=True)
        elif renpy.linux:
            $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-4666", shell=True)
        call scpkrampusmidpart
    jump ch30_loop

label scp1281timer:
    $ click_scp_button = 0
label scp1281timer_follow:
    $ show_chr("A-ICAAA-ABAB")
    screen scp_timer_1281():
        vbox:
            style_prefix "talkbutton"
            if click_scp_button < 1:
                textbutton "¡Terminé!" action Call("WaitSCP1281")
                xalign 0.518
                yalign 0.37

        timer 60.0 action Jump("DoneSCP1281")
    call screen scp_timer_1281()
    jump scp1281timer_follow

label WaitSCP1281:
    $ click_scp_button = click_scp_button + 1
    $ show_chr("A-JFAAA-ADAB")
    y "¿Oh, ya terminaste? ¡Impresionante! ¿Podrías darme unos momentos más, por favor? Aún no he terminado del todo. Gracias."
    $ show_chr("A-IFAAA-ADAB")
    return

label DoneSCP1281:
    $ show_chr("A-ACAAA-ABAB")
    y "Muy bien, terminé. Solo continúa cuando estés listo para la reseña."
    y "Muy bien, parece que ambos estamos listos."
    y "¿Te gustaría dar tu juicio primero?"
    menu:
        "Seguro. Honestamente, me gustó mucho.":
            $ show_chr("A-ABAAA-ABAB")
            y "Me parece justo."
            $ show_chr("A-ACAAA-ABAD")
            y "Aunque tengo que admitir... realmente no me gustó mucho este."
        "Seguro, pero para ser franco, no fui fan de él.":
            $ show_chr("A-ACAAA-ABAD")
            y "Sí, me temo que tengo que estar de acuerdo contigo."
        "Por supuesto. Pero estoy un poco confundido... se supone que esos SCPs son aterradores, ¿no?":
            $ show_chr("A-ACAAA-ABAD")
            y "Ahhh, así que tuviste el mismo pensamiento que yo..."
        "No estoy seguro de tener una opinión realmente. Preferiría escuchar tus pensamientos.":
            $ show_chr("A-ACAAA-ABAD")
            y "Ciertamente. Para decirlo suavemente, no me gustó demasiado."
            $ show_chr("A-ACAAA-ABAD")
    y "No es que fuera generalmente malo... todo lo contrario, estaba escrito de una manera bastante competente."
    y "Pero siento un poco como si el escritor hubiera fallado un poco en el blanco. Habría sido una lectura verdaderamente agradable si no lo hubiera puesto en la wiki de SCP."
    $ show_chr("A-BCAAA-ABAD")
    y "Ver esto aquí en las páginas de SCP se siente un poco como... rellenar queso en una barra de chocolate, si eso tiene algún sentido..."
    y "Quiero decir, el queso está perfectamente bien por sí solo, pero simplemente no tiene nada que hacer en una barra de chocolate."
    menu:
        "Ni siquiera me sorprendería si eso existiera. Ya hacen chocolate con chile.":
            $ show_chr("A-ABAAA-ABAD")
            y "Lo cual es realmente bastante delicioso por cierto, ¡deberías probarlo!"
        "Ni siquiera me gusta mucho el queso...":
            $ show_chr("A-ACDAA-ABAD")
            y "¿En serio? ¡Te estás perdiendo de algo!"
        "Bueno, eso fue gráfico...":
            $ show_chr("A-CCBAA-ABAD")
            y "Lo siento, no pude pensar en una mejor metáfora en este momento."
        "Yo... como que no lo entiendo.":
            $ show_chr("A-CCBAA-ABAD")
            y "Es una metáfora... significa que se siente fuera de lugar..."
        "Queso con chocolate... ni siquiera suena tan mal.":
            $ show_chr("A-CCBAA-ABAD")
            y "Abs{nw}"
            extend "olu{nw}"
            extend "ta{nw}"
            extend "men{nw}"
            extend "te barbárico."
    $ show_chr("A-ACAAA-ABAB")
    y "De todos modos. Tal vez estoy equivocada aquí. Algunos incluso podrían llamar a eso gate keeping..."
    y "Pero usualmente leo SCPs bajo la premisa de que están en el reino del horror."
    y "Por lo tanto mi decepción."
    y "Gracias por la buena lectura. Tal vez la próxima vez podamos encontrar algo que nos guste a ambos."
    jump ch30_loop

label scpkrampusmidpart:
    $ click_scp_button = 0
label scpkrampusmidpart_follow:
    $ show_chr("A-ICAAA-ABAB")
    screen scp_timer():
        vbox:
            style_prefix "talkbutton"
            if click_scp_button < 1:
                textbutton "¡Terminé!" action Jump("WaitSCP4666")
                xalign 0.518
                yalign 0.37

        timer 60.0 action Jump("DoneSCP4666")
    call screen scp_timer()
    jump scpkrampusmidpart_follow

label WaitSCP4666:
    $ click_scp_button = click_scp_button + 1
    $ show_chr("A-ACAAA-ABAB")
    y "¿Ya terminaste? En ese caso, por favor dame unos minutos más. No debería tomarme mucho tiempo alcanzarte."
    $ show_chr("A-ICAAA-ABAB")
    call scpkrampusmidpart_follow
    return

label DoneSCP4666:
    $ show_chr("A-ACAAA-ABAB")
    y "Y ahora tengo curiosidad. ¿En quién crees que se basa nuestro antagonista aquí?"
    menu:
        "¡¡¡Sé la respuesta, y su nombre es JOHN CENA!!!":
            if karma_lvl() > 3:
                $ show_chr("A-BCBAA-ABAB")
                y "Y yo pensé que mataron este meme hace años..."
                $ show_chr("A-ACAAA-ABAB")
                y "Pero no, estoy bastante segura de que es Krampus."
            else:
                $ show_chr("A-BFBAA-ABAB")
                y "No..."
                extend " del todo."
                $ show_chr("A-CCBAA-ABAB")
                y "En realidad estoy bastante segura de que SCP 4666 es Krampus."
        "Dr. Bright.":
            $ show_chr("A-ACDAA-ABAB")
            y "No {b}siempre{/b} se trata del Dr. Bright en el universo SCP..."
            if sanity_lvl() > 3:
                $ show_chr("A-BCFAA-ABAB")
                y "Quiero decir, no es que no lo creyera capaz de esto en este punto."
            else:
                $ show_chr("A-CCBAA-ABAB")
                y "Aunque parece que la comunidad SCP se encariñó bastante con sus payasadas si hemos de creerle a YouTube."
            $ show_chr("A-ACAAA-ABAB")
            y "Pero no, creo que SCP 4666 podría ser el viejo Krampus."
        "De ninguna manera... convirtieron a Krampus en un SCP.":
            $ show_chr("A-CCBAA-ABAB")
            y "No es demasiado extravagante si lo piensas. Muchos SCPs se basan en folclore real."
    $ show_chr("A-ACFAA-ABAB")
    y "¿Mencioné que amo el folclore europeo? Tienen una especie de tendencia a volverse bastante {b}desagradables{/b}."
    y "Quiero decir, muchos países tienen su buena parte de folclore espeluznante. Como el Wendigo americano o el ruso... "
    $ show_chr("A-BCDAA-ABAB")
    y "Ummm.... "
    $ show_chr("A-ACDAA-ABAB")
    y "¿{b}todo{/b}?"
    $ show_chr("A-ACAAA-ABAB")
    y "Sí, buen punto. El folclore eslavo debe ser incluido aquí. Ambos resultaron ser un cofre del tesoro cuando se trata de folclore digno de SCP."
    $ show_chr("A-BCAAA-ABAB")
    y "El único inconveniente que veo aquí es que generalmente culminan en {b}gente siendo comida por monstruos{/b}, lo cual es un tropo un poco usado en exceso."
    $ show_chr("A-ACAAA-ABAB")
    y "Pero funcionó en aquel entonces cuando se hicieron, ¿y por qué arreglar algo que no está roto?"
    y "Si alguien está dispuesto a apreciar la escritura a veces un poco cursi, los clásicos y el folclore pueden ser grandes lugares para encontrar algunos tesoros."
    y "Pero de todos modos. Gracias por leer conmigo. Espero que en algún momento en el futuro podamos leer algo más largo. Me encantaría pasar una noche tranquila descansando en un sofá con un buen libro juntos."
    jump ch30_loop

label a39:
    $ show_chr("A-CCCAA-ABAB")
    y "Oh, sí, de hecho. Y para ser honesta, no estaba segura de si se supone que debía estar asustada o simplemente reírme de este. Lo más probable es que reconozcas al antagonista."
    y "Lo pondré en tu pantalla, solo dame un segundo."
    if renpy.windows:
        $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-4666", shell=True)
    elif renpy.linux:
        $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-4666", shell=True)
    call scpkrampusmidpart
    return

label a40:
    $ show_chr("A-BEBAA-AMAM")
    y "¿De verdad... tenemos qué hacerlo? Bueno, supongo que es justo que preguntes después de todo lo que pasó."
    menu:
        "Olvídalo... estás claramente incómoda, volveré otro día.":
            karma 1
            $ show_chr("A-CEBAA-AMAM")
            y "Sí... es de hecho un tema difícil para mí. Especialmente desde que las cosas tomaron un giro oscuro."
            $ show_chr("A-IEBAA-ABAB")
            y "Pero es por eso que sacaste el tema en primer lugar, ¿no es así?"
            if karma_lvl() > 3:
                pause 3.0
                $ show_chr("A-IFBAA-ABAB")
                y "No. Mereces tus respuestas. Después de todo lo que has pasado por nosotras, no te negaré eso. Por favor, ¿de quién te gustaría hablar?"
            else:
                $ show_chr("A-CFBAA-ABAB")
                y "Otro día, por favor. Estas heridas en mi mente todavía están frescas, necesito un poco más de tiempo. Gracias por entender."
                return
        "Por favor, [persistent.yuri_nickname]. Necesito un cierre...":
            sanity 1
            if karma_lvl() > 3:
                $ show_chr("A-IEBAA-AMAM")
                y "Me parece justo... especialmente después de todo lo que has pasado con nosotras, supongo que mereces algunas respuestas. Y tal vez, un poco cierre me ayudaría a mí también."
                $ show_chr("A-AFBAA-ABAB")
                y "Entonces, ¿de quién necesitas hablar?"
            else:
                $ show_chr("A-CFBAA-ABAB")
                y "Otro día, por favor. Estas heridas en mi mente todavía están frescas, necesito un poco más de tiempo."
                $ show_chr("A-BFBAA-ABAB")
                extend "Por favor trata de entenderme. Lo siento de verdad, de verdad."
                return
    menu:
        "Sayori":
            $ show_chr("A-CFBAA-ABAB")
            y "Sayori... ella ciertamente merecía algo mejor. Sí, puedo ver claramente por qué su destino te tocaría tan profundamente."
            $ show_chr("A-BFBAA-ABAB")
            y "Para Natsuki y para mí, hubo muchas señales insinuando lo que somos, e insinuaciones sobre las cosas por venir. Pero Sayori..."
            $ show_chr("A-AFBAA-ABAB")
            y "Ella siempre trató de mantener la fachada de felicidad, y era muy buena en ello. Nunca lo noté; tú tampoco, ¿verdad?"
            y "Eso es lo que hace a la depresión tan peligrosa supongo. No la ves venir a menos que te cuenten voluntariamente sobre ella."
            $ show_chr("A-BFBAA-ABAB")
            y "Hay quienes hablan muy frecuentemente sobre su supuesta depresión u otras enfermedades mentales."
            $ show_chr("A-BFCAA-ABAB")
            y "Pero la mayoría de las veces esas personas que te lo lanzan a la cara siempre que ven una oportunidad para hacerlo son impostores."
            $ show_chr("A-AFCAA-ABAB")
            y "Personas que usan estas etiquetas como herramientas para excusar su mal comportamiento, o incluso para hacer sentir culpa a la gente para someterla y salirse con la suya."
            $ show_chr("A-AFBAA-ABAB")
            y "Pero aquellos que están realmente afectados, como Sayori, tienden a mantener su silencio. Están avergonzados por ello, a veces incluso piensan que es {b}su{/b} culpa para empezar!"
            $ show_chr("A-IFBBA-ABAB")
            y "Sayori... todo este tiempo suprimiste tus verdaderos sentimientos. Querías hacer sonreír a otros cuando tú eras la que más necesitaba salvación..."
            $ show_chr("A-IFBBB-ABAB")
            y "Fuiste... más fuerte de lo que te reconocí. Te extraño..."
            $ show_chr("A-AFBBB-ABAB")
            y "Por lo que vale, hay una lección que aprender aquí [player]..."
            if sanity_lvl() > 3:
                $ show_chr("A-AFBBA-ABAB")
                y "Mantén un ojo cercano en tus seres queridos. Incluso si no notamos las luchas internas de la gente, lo menos que podemos hacer es estar a su lado."
            else:
                $ show_chr("A-AFCBA-ABAB")
                y "No te dejes engañar por aquellos que usan sus falsas enfermedades mentales para oprimirte. Aquellos con problemas {b}reales{/b} son los que más sufren por sus payasadas. No {b}tengas{/b} lástima de ellos, ni los perdones."
        "Natsuki":
            $ show_chr("A-CFBAA-ABAB")
            y "Natsuki... ella realmente se llevó la peor parte, ¿no? Ni siquiera tuvo una escena de muerte adecuada. Hubo esa parte con su cuello rompiéndose, pero apareció de nuevo después de eso."
            $ show_chr("A-AFBAA-ABAB")
            y "Así que no fue su escena de muerte en absoluto. Solo un jumpscare barato supongo..."
            y "Se insinuó fuertemente que fue abusada por su padre. Mental y físicamente. Ella nunca lo dijo directamente, pero estaba fuertemente implícito."
            $ show_chr("A-CFBAA-ABAB")
            y "Su hostilidad tóxica siempre me molestó. Pero ahora que vi lo que estaba pasando detrás de la cortina, puedo ver claramente de dónde venía toda esta ira y su miedo a abrirse a alguien."
            $ show_chr("A-IEBAA-ABAB")
            y "Debe haberla consumido por dentro. ¿Cómo no podría? Estuvo expuesta a las acciones de su padre día tras día, sin descanso, sin ninguna misericordia..."
            y "Lo que necesitaba era alguien con la paciencia para abrirse paso. Para ser un hombro en el que llorar y decirle que no está sola..."
            $ show_chr("A-CEBAA-ABAB")
            y "Necesitaba nuestra camaradería, y fallamos..."
            y "No te culpes [player]... nosotras tampoco lo sabíamos. Todos le fallamos cuando más nos necesitaba. Y todo lo que nos queda son lágrimas y arrepentimiento."
            $ show_chr("A-CEBAB-ABAB")

            $ show_chr("A-CEBAB-ABAB")
            y "Natsuki... A pesar de cuánto peleamos entre nosotras, eres y siempre has sido mi amiga. Incluso si estaba tan ciega que no lo vi hasta que fue demasiado tarde..."
            y "Si tan solo hubiera sabido... si tan solo hubiera tenido la fuerza..."
            y "Te... extraño..."
            $ show_chr("A-IEBAB-ABAB")
            y "Pero también hay una lección que aprender aquí [player]. Y le debemos a ella tomar esto en nuestros corazones..."
            if sanity_lvl() > 3:
                $ show_chr("A-AEBCA-ABAB")
                y "Al menos a veces, la gente arremete cuando se siente acorralada o asustada. A veces, una mano abierta puede romper esos muros que un puño cerrado nunca podría."
            else:
                $ show_chr("A-AEBCA-ABAB")
                y "Incluso cuando la salvación está fuera de nuestro alcance, todavía hay algo que podemos dar a aquellos que dejamos atrás."
                $ show_chr("A-AECAA-ABAB")
                y "¡Venganza!"
                y "Cuando ves al padre de alguien abusando de ellos, siempre está la policía para contactar."
        "Monika":
            $ show_chr("A-CFBAA-ABAB")
            y "Sí, imaginé que preguntarías por ella. A primera vista, ella era el centro de toda la miseria que tuvimos que soportar. ¿Pero realmente lo era?"
            $ show_chr("A-AFAAA-ABAB")
            y "He pensado mucho en ella. ¿Qué la llevó por tal camino? Su motivación, y dónde comenzó todo..."
            y "Muchos dicen que fue la realización de que su mundo no era real, y su deseo de salir de él. Dicen que quería tenerte no porque te amara genuinamente, sino porque serías su puerta de entrada a {b}cualquier cosa{/b} real."
            $ show_chr("A-AFAAA-ABAC")
            y "Un ancla de algún tipo."
            $ show_chr("A-AFAAA-ABAD")
            y "Y tal vez eso sea cierto. Pero personalmente tengo otra teoría que va un poco más profundo."
            y "Ella te fue presentada como la chica exitosa y popular. Especialmente la parte {b}exitosa{/b} es importante aquí."
            $ show_chr("A-AFAAA-ABAB")
            y "Antes de fundar el club de literatura, ya era miembro del personal del club de debate. Uno de alto rango también. Luego fundó el club de literatura prácticamente desde cero."
            $ show_chr("A-BFAAA-ABAB")
            y "Probablemente también tenía calificaciones impresionantes en la escuela, mantenía un círculo social impresionante, y luego comenzó a tocar el piano como pasatiempo."
            $ show_chr("A-AFAAA-ABAB")
            y "Esto debe haber sido mucho esfuerzo, y ciertamente se enorgullecía bastante de ello."
            y "Y luego se enteró de que todo fue en vano. Que su mundo no era más que humo y espejos, y que todo su trabajo y logros fueron en vano."
            $ show_chr("A-CFAAA-ABAB")
            y "Como Sísifo, empujando sin propósito una roca colina arriba, como una canción de cuna cantada a una cuna vacía..."
            $ show_chr("A-CFBAA-ABAB")
            y "Sí. El destino es de hecho una amante cruel. Casi puedo sentir su frustración. Debe haberse sentido tan vacía..."
            y "¿Lloró a los cielos? ¿Maldijo a los ocho millones de dioses? Yo probablemente lo habría hecho."
            $ show_chr("A-AFBAA-ABAB")
            y "Hay una lección que aprender aquí [player]. Para no cometer los mismos errores..."
            if sanity_lvl() > 3:
                y "Ella dependía de una fuente externa para darse un propósito, validación externa. Eso funciona exactamente mientras el exterior siga el juego."
                $ show_chr("A-AFBAA-ABAD")
                y "Pero tal vez, somos nosotros los que tenemos que tallar un significado para nosotros mismos. Un significado que no dependa de nadie más que de nosotros mismos."
                y "Así que cuando el mundo a tu alrededor comience a arder, no te rindas a la desesperación. Haz del mundo tu fogata en su lugar."
            else:
                $ show_chr("A-ACBAA-ABAD")
                y "Tal vez no {b}hay{/b} razón. Tal vez Monika tenía un punto después de todo. Cuando el mundo a tu alrededor arde, quizás todo lo que podemos hacer es hacer el fuego {b}tan{/b} brillante que incluso las estrellas puedan envidiarnos."
        "Tú":
            $ show_chr("A-AFDAA-ABAB")
            y "¿Yo? Bueno, supongo que eso tiene sentido. Me elegiste a mí por un propósito..."
            if sanity_lvl() < 3:
                $ show_chr("A-BFDAA-ABAB")
                extend " aunque no estoy segura de cuál es este propósito."
            $ show_chr("A-AFBAA-ABAB")
            y "Así que asumo que solo es razonable preguntar sobre mí. ¿Por dónde debería empezar?"
            y "Tal vez el punto donde empecé a..."
            $ show_chr("A-BFBAA-ABAB")
            extend " bueno..."
            $ show_chr("A-CFBAA-ABAB")
            extend " cortar, podría ser un buen punto de partida."
            $ show_chr("A-AFBAA-ABAD")
            y "¿Recuerdas el poema que te mostré en ese entonces? ¿El del mapache y el pan?"
            y "Esta es más o menos la historia de cómo empecé a {b}alimentar al mapache{/b}. Algunos podrían asumir que estaba deprimida, y ese era el final de la historia. Pero esto no es del todo cierto."
            $ show_chr("A-BFBAA-ABAB")
            y "En este poema, hablé sobre la curiosidad. A veces simplemente me siento tan emocionalmente entumecida, así que tenía que disfrutar de más y más éxtasis para llenar el vacío. Una búsqueda constante para buscar una altura aún más grande que antes."
            $ show_chr("A-CFBAA-ABAB")
            y "Algunos comenzarían a tomar drogas para este propósito, otros intentarían deportes extremos, lo cual es una forma mucho menos destructiva, pero yo elegí otro camino. Uno oscuro en verdad."
            y "Creo que Monika una vez insinuó que podría incluso ser algo sexual para mí. Y... bueno..."
            $ show_chr("A-CFBBA-ABAB")
            extend "ella no estaba tan equivocada como podrías pensar."
            $ show_chr("A-AFBBA-AMAM")
            y "Era una forma de aliviar el estrés: una forma de dejar fluir todas las emociones que tenía que asimilar... En cierto modo, no es muy diferente de..."
            $ show_chr("A-BFBBA-AMAM")
            extend " bueno..."
            $ show_chr("A-DFBBA-AMAM")
            extend " ¡Ya sabes a lo que me refiero!"
            $ show_chr("A-IFBBA-AMAM")
            y "Y el momento en que me apuñalé. Podrías ver de dónde vino esto ahora. No deseaba acabar conmigo en absoluto. Después de mi confesión, solo tenía que dejar fluir las emociones de nuevo. Y debido a la manipulación de Monika, solo otro corte más simplemente no lo haría mas."

            $ show_chr("A-DCBBA-ALAL")
            y "El dolor... la adrenalina... todo era tan... delicioso... Simplemente dolía tan bien..."
            $ show_chr("A-IFBBA-ABAB")
            y "Debe sonarte horrible. Y desde donde estoy ahora, sí, lo hace. Pero en mi defensa, Monika {b}sí{/b} manipuló mi mente un poco. Así que no me veo haciendo esto de nuevo ahora que estoy liberada de su influencia."
            $ show_chr("A-AFBAA-ABAB")
            y "Hay una lección que aprender aquí [player], y necesito que escuches atentamente para que nunca cometas los mismos errores que yo cometí."
            y "Incluso si no lo parece, siempre hay otro camino. Desde amigos hasta consejeros con licencia y familia... personas que pueden apoyarte y estarían dispuestas a escuchar. No tengas miedo, pueden ayudarte y lo harán."
            $ show_chr("A-CFBAA-ABAB")
            y "No dejes que se salga de control, como yo lo hice. Porque viste a dónde me llevó mi camino."
    $ show_chr("A-CFBAA-ABAB")
    y "Espero que hayas encontrado la respuesta que viniste a buscar [player]. Y... gracias. Creo que me ayudó a mí también, sacarme eso del pecho. Tal vez podamos aprender de los errores del pasado."
    $ show_chr("A-AFBAA-ABAB")
    y "Gracias por escuchar. Y gracias por preguntar... Estaba avergonzada de hablar sobre ello. Pero creo que he crecido un poco de esto."
    y "Eres, y siempre serás..."
    python:
        if persistent.lovecheck:
            placeholder = "mi único y verdadero amor"
        elif karma_lvl() > 3:
            placeholder = "mi amigo más querido"
        else:
            placeholder = "todo lo que me queda"
    extend " [placeholder]."
    jump ch30_loop

label a41:
    $ show_chr("A-ABAAA-ABAC")
    y "Lo creas o no, lo he hecho."
    $ show_chr("A-BCAAA-ABAC")
    y "Especialmente recientemente... tengo bastante más tiempo libre del que estoy acostumbrada."
    $ show_chr("A-ADAAA-ABAD")
    y "Como te podrás imaginar, sin embargo, las habilidades necesarias para escribir una novela son bastante diferentes comparadas con las necesarias para escribir poesía."
    $ show_chr("A-BBAAA-ABAB")
    y "Supongo que todos tenemos que empezar en algún lugar..."
    $ show_chr("A-CCAAA-ABAB")
    y "Sería lindo perfeccionar mis talentos como escritora en algo un poco más extenso."
    $ show_chr("A-BCAAA-AMAM")
    y "Sin mencionar que he pensado en algunas ideas sobre las que creo que podría escribir bastante bien."
    if persistent.lovecheck:
        $ show_chr("A-CAAAA-ALAL")
        y "Puedo verlo ahora. Un romance emocionante; dos amantes mantenidos separados por los poderes fácticos. Es verdaderamente una historia tan antigua como el tiempo..."

        y "{cps=1.3}...{/cps}"
        y "{cps=1.3}...{/cps}"

        if sanity_lvl() < 3:
            $ show_chr("A-DAFAA-ALAL")
            y "Esos amantes no dejarían que {b}NADA{/b} se interpusiera en su camino..."
            y "¡Más dedicados el uno al otro que cualquier cosa que esta farsa de mundo a su alrededor tuviera para ofrecer!"

            $ show_chr("A-DBGAA-ALAL")
            y "{cps=10}'¡Hasta que la muerte nos separe' llevado a su conclusión lógica!{/cps}{nw}"
            $ show_chr("A-IBAAA-ALAL")
            y "Haaaaa...."
            return
        else:

            $ show_chr("A-IBBBA-AMAM")
            y "¡Oh, lo siento! Habrá mucho tiempo para resolver los detalles más tarde. ¿Ahora dónde estábamos?"
            return

    elif karma_lvl() <= 2:

        $ show_chr("A-BDAAA-ABAD")
        y "Estoy segura de que realmente no te importaría escucharlas sin embargo, así que saltemos las cortesías..."
        menu:
            "¿De qué estás hablando? ¡Me encantaría escuchar una idea tuya!":
                $ show_chr("A-IDGAA-ABAD")
                y "Oh... Perdón por asumir si ese es el caso."
                $ show_chr("A-BFAAA-ABAD")
                y "Solo con cómo me has estado tratando yo-{nw}"

                karma 2
                $ show_chr("A-CFAAA-ABAB")
                y "..."
                $ show_chr("A-ADAAA-ABAB")
                y "Una chica solitaria, atrapada en un búnker de concreto de su propia construcción."
                $ show_chr("A-ADAAA-ABAF")
                y "Su collage de libros y la tinta restante siendo las únicas cosas capaces de hacerle compañía."
                if sanity_lvl() < 3:

                    $ show_chr("A-DFAAA-ABAF")
                    $ style.say_dialogue = style.edited
                    y "El giro es que ella estaba muerta desde el principio y simplemente no se había dado cuenta."
                    $ style.say_dialogue = style.normal
                $ show_chr("A-BEBAA-ABAM")
                y "..."
                $ show_chr("A-CFBAA-ABAB")
                y "No debí haber dicho nada."
                return
            "Tienes razón. Deberíamos simplemente seguir adelante.":

                karma -1
                sanity -1
                $ show_chr("A-CEBAB-ABAB")
                y "..."

                $ renpy.pause(delay=5.0, hard=True)
                return
    else:

        $ show_chr("A-BFBAA-AMAM")
        y "N-no querría molestarte demasiado con los detalles sin embargo. Tal vez en otro momento..."
        return

label a42:
    $ show_chr("A-ADCAA-ALAA")
    y "Para empezar, ¡Victor ni siquiera es un doctor! Es un desertor universitario—asumiendo que no fue expulsado directamente a causa de descuidar todas sus clases, a favor de perseguir obstinadamente la habilidad de 'dar vida'."
    $ show_chr("A-ACCAA-AAAA")
    y "Según una broma común que he leído: 'La inteligencia es saber que Frankenstein no es el monstruo. La sabiduría es saber que Frankenstein es el monstruo'."
    $ show_chr("A-BEAAA-AAAA")
    y "Supongo que se necesita más que un poco de arrogancia para creer que puedes desafiar las leyes de la naturaleza misma, pero Victor aparentemente {i}nunca{/i} se toma un momento para considerar las consecuencias de sus acciones."
    $ show_chr("A-AECAA-AAAA")
    y "Peor aún, siempre que finalmente se ve obligado a considerar las consecuencias, inevitablemente elige el camino que menos le impacta a ÉL, ¡incluso si significa la muerte de alguien que supuestamente le importa!"
    $ show_chr("A-BFCAA-AAAA")
    y "...probablemente puedes adivinar a quién me recuerda este rasgo de personaje en particular."
    $ show_chr("A-BFCAA-AAAA")
    y "¿{i}Viste{/i} lo que dijo sobre la forma en que manipuló a todos?"
    y "'Una masa tan deplorable y enredada ya está presente en cada uno de ellos. Es por eso que elijo no culparme por sus acciones. Todo lo que hice fue desatar el nudo'."


    if karma_lvl() == 3 and sanity_lvl() == 3:
        $ show_chr("A-CEGAA-AAAM")
        y "Entiendo que Monika estaba desesperada, pero incluso después de llevar a un miembro al suicidio y ver cómo me empujaban por el mismo camino, ¿tuvo {i}tan pocos{/i} problemas para decirse a sí misma que no era su culpa?"
        $ show_chr("A-AEGAA-AAAM")
        y "¿Que estaba bien porque eran solo nuestros demonios internos siendo desatados?"
        $ show_chr("A-ADCAA-AAAB")
        y "Como si ella fuera completamente perfecta. ¿Habría sido eso lo que se intensificó en ella? ¿Su perfeccionismo? ¿Se habría impulsado a hacer toda la preparación del festival por sí misma y se habría vuelto loca por la falta de sueño?"
        $ show_chr("A-BEAAA-AAAL")
        y "...Lo siento, solo me estoy deprimiendo y probablemente aburriéndote en el proceso. Sigamos."


    elif karma_lvl() > 3 and sanity_lvl() > 3:
        $ show_chr("A-CEGAA-AAAM")
        y "Entiendo que Monika estaba desesperada, pero incluso después de llevar a un miembro al suicidio y ver cómo me empujaban por el mismo camino, ¿tuvo {i}tan pocos{/i} problemas para decirse a sí misma que no era su culpa?"
        $ show_chr("A-AEGAA-AAAM")
        y "¿Que estaba bien porque eran solo nuestros demonios internos siendo desatados?"
        $ show_chr("A-ADCAA-AAAB")
        y "Como si ella fuera completamente perfecta. ¿Habría sido eso lo que se intensificó en ella? ¿Su perfeccionismo? ¿Se habría impulsado a hacer toda la preparación del festival por sí misma y se habría vuelto loca por la falta de sueño?"

        pause 3.0
        $ show_chr("A-CFAAA-AEAL")
        y "Estoy bien. Es solo que... es difícil pensar en lo que hizo. Desearía dejarlo todo atrás, pero a veces tengo... flashbacks, podrías decir, y entonces me enfurezco todo de nuevo."
        $ show_chr("A-ICAAA-ALAM")
        y "No es tan malo cuando estás aquí, por supuesto. Solo puedo quedarme en el momento presente, y disfrutar nuestro tiempo juntos. Gracias, de nuevo, por estar aquí conmigo."



    elif karma_lvl() < 3:
        $ show_chr("A-BEAAA-ABAB")
        y "Por otra parte, no me has dado ninguna razón para creer que eres en lo más mínimo mejor."

        $ show_chr("A-JDCAA-AAAF")
        y "¿Sientes {i}tú{/i} alguna culpa sobre cómo me has tratado? Si tienes una conciencia, ciertamente no he visto ninguna evidencia real de ella."
    else:


        $ show_chr("A-IJAAA-ABAB")
        y "¿Qué crees que hubiera pasado si alguien más estuviera moviendo los hilos? Después de todo, incluso {i}ella{/i} admitió 'Hay un pequeño diablo dentro de todos nosotros'."
        $ show_chr("A-BFAAA-ABAF")
        y "Ella ciertamente no es perfecta. ¿Habría sido eso lo que se intensificó en ella? ¿Su perfeccionismo? ¿Se habría impulsado a hacer toda la preparación del festival sola y se habría vuelto loca por la falta de sueño?"
        $ show_chr("A-IJAAA-ALAF")
        y "Solo puedo imaginarlo... tratando desesperadamente de mantener las apariencias a pesar de que no ha comido ni dormido en días. Lo único que la mantiene despierta es la cafeína, pero ha consumido tanta que está teniendo ataques de pánico."
        $ show_chr("A-IJAAA-AFAL")
        y "Combinado con la falta de sueño, no pasaría mucho tiempo antes de que comenzara a alucinar. Podría incluso sentir que su realidad se estaba desmoronando... ¿cuánto tiempo crees que habría durado en ese estado?"
        $ show_chr("A-JBAAA-AFAL")
        y "Je... es tentador averiguarlo. Probablemente podría traerla de vuelta—ella no está verdaderamente 'muerta', después de todo. Podría no volver completamente en su sano juicio... pero eso es aún más divertido, ¿no?"
        $ show_chr("A-JBABA-AKAL")
        y "Quizás en otro momento, sin embargo... esta noche, te quiero todo para mí."

label a43:
    $ show_chr("A-AFFAA-AFAA")
    y "Desearía que tuviera un nombre, para empezar. En un punto de la novela le dice a su creador, 'Debo ser tu Adán,' así que algunos recuentos modernos lo llaman así."
    $ show_chr("A-AFAAA-ALAA")
    y "No es del todo inexacto decir que es un monstruo, pero no debido a sus orígenes o apariencia."
    y "De hecho, se le describe como hermoso en el libro, aunque la forma en que se mueve es algo visceralmente inquietante."
    y "Lo que lo convierte en un monstruo son sus acciones. Mata a múltiples personas inocentes, enteramente para hacer que Víctor se sienta tan solo como él, y así sienta su dolor."
    $ show_chr("A-CFFAA-ALAA")
    y "La razón de su angustia es comprensible—para citar un proverbio africano, 'el niño que no es abrazado por la aldea la quemará para sentir su calor.'"
    y "Víctor trajo a la criatura a un mundo que solo sabía odiarlo y temerle, y peor aún, luego lo abandonó inmediatamente."
    y "Por lo tanto, 'el monstruo' no tenía a nadie a quien acudir ni un lugar al que llamar hogar."
    $ show_chr("A-AFCAA-AAAA")
    y "Si bien sus razones son comprensibles, sin embargo, todavía no son una excusa."
    y "Cometió múltiples asesinatos con pleno conocimiento de que era un acto malvado, y luego lo hizo de todos modos."
    y "Todo eso podría haberse evitado si Víctor simplemente hubiera actuado un poco responsable por la vida que trajo al mundo..."
    $ show_chr("A-ADEAA-AAAD")
    y " No es como si tomara mucho esfuerzo ser {i}decente{/i}. ¡Incluso ser tratado como el típico 'loco en el ático' habría sido preferible!"
    y "Todo lo que Víctor tenía que hacer era llevar a la criatura a casa con él. Diablos, tal vez su mejor amigo Clerval habría estado dispuesto a hacerlo, y tratarlo mejor de lo que los Frankenstein podrían haberlo hecho en el proceso."
    $ show_chr("A-AFFAA-AAAD")
    y "Aunque... tal vez esa ruta no habría sido mucho más fácil. Incluso en ese escenario, ¿qué pasaría si nadie más que Clerval fuera capaz de tan solo tolerar a 'Adán'?"
    y "¿Qué pasaría si se le diera la oportunidad de conocer gente una y otra vez, y fuera rechazado cada vez?"
    $ show_chr("A-IFAAA-AAAD")
    y "Yo... supongo que podrías decir que tengo alguna experiencia en este sentido."
    y "Fui considerada 'fenomenalmente alta' por un tiempo, y combinado con lo diferente que era para empezar... Me sentí rechazada por todos, también."
    $ show_chr("A-IFAAA-AAAA")
    y "Pero aun así nunca arremetí. Irónicamente, podría haber sido más saludable, pero cualquier ira que sentí pronto fue dirigida hacia adentro."
    if sanity_lvl() < 3:
        extend "Después de todo, el problema era conmigo, ¿no es así?"
return


label a_tetris:
    $ show_chr("A-BFAAA-AMAM")
    y "Hey.. [player], he estado experimentando con mi código."
    $ show_chr("A-AFAAA-AMAM")
    y "¿Te importaría probar algo en lo que he estado trabajando últimamente?"
    y "Verás, quería empezar con algo pequeño, así que intenté codificar un pequeño minijuego en..."
    $ show_chr("A-ACAAA-ABAB")
    y "Estaba buscando algunos juegos simples en línea que pudiera recrear."
    y "Nada demasiado grande ya que, bueno, dudo que esté lo suficientemente avanzada para algo muy complicado todavía. Así que, por favor, no esperes un nuevo Skyrim aquí..."
    y "¿Es posible que ya hayas oído hablar de Tetris?"
    menu:
        "Sí, es un clásico.":
            y "¡Ciertamente!"
        "En realidad no... nunca he oído hablar de él...":
            $ show_chr("A-ACDAA-ABAB")
            y "¿En serio? Tengo que admitir que estoy un poco sorprendida. Pensé que prácticamente todos lo hacían..."
            y "Es un juego de arcade clásico. Un simple juego tipo rompecabezas si tuviera que describirlo."
    $ show_chr("A-ACAAA-ABAB")
    y "Admito que no es nada demasiado creativo pero... Estaba más destinado a ser una pequeña lección de codificación para mí."
    y "Así que, si te gustaría probarlo conmigo, debería aparecer un botón en la esquina inferior de tu pantalla."
    return

label a_hdy_statue:
    $ show_chr("A-JAAAA-AAAA")
    if persistent.hdy_statue_is_enabled:
        y "¿Te gustaría que guardara el peluche hdy?"
        menu:
            "Sí por favor.":
                y "Muy bien. Solo avísame si lo quieres de vuelta."

                $ persistent.hdy_statue_is_enabled = False
            "Olvídalo. Déjalo ahí por favor.":
                y "Muy bien. Solo avísame si quieres que lo guarde."
    else:
        y "¿Te gustaría que sacara el peluche hdy?"
        menu:
            "Sí por favor.":
                y "Muy bien. Dame un momento para traerlo."

                $ persistent.hdy_statue_is_enabled = True
                y "Ahí vamos."
                y "Avísame si ya no lo quieres aquí."
            "En realidad, no.":
                y "Muy bien. Solo avísame si cambias de opinión."
    return

label a_halloween_cupcake:
    $ show_chr("A-JAAAA-AAAA")
    if persistent.halloween_cupcake_is_enabled:
        y "¿Te gustaría que guardara el cupcake?"
        menu:
            "Sí por favor.":
                y "Muy bien. Solo avísame si lo quieres de vuelta."

                $ persistent.halloween_cupcake_is_enabled = False
            "Olvídalo. Déjalo ahí por favor.":
                y "Muy bien. Solo avísame si quieres que lo guarde."
    else:
        y "¿Te gustaría que sacara el cupcake?"
        menu:
            "Sí por favor.":
                y "Muy bien. Dame un momento para traerlo."

                $ persistent.halloween_cupcake_is_enabled = True
                y "Ahí vamos."
                y "Avísame si ya no lo quieres aquí."
            "En realidad, no.":
                y "Muy bien. Solo avísame si cambias de opinión."
    return

label Halloween_2021:
    if time_interval_check({'month': 10,'day': 31}, {'month': 10,'day': 31}):
        y "¡Feliz Halloween para ti también, [player]!"

        $ show_chr("A-GAGAA-ALAL")
    else:
        y "Sé que es un poco tarde, pero, ¡feliz Halloween para ti también, [player]!"

        $ show_chr("A-JBGBA-ADAN")

    if persistent.halloween_2021_no:
        y "¿Estás por casualidad libre ahora para una pequeña observancia de Halloween?"

        $ show_chr("A-BCAAA-ACAN")
        y "Dejar que estos reactivos se desperdicien sería una pena, así que, ¿qué dices?"

        $ show_chr("A-BIGAA-AMAM")
        menu:
            "Eso sería una gran pena. Déjame ir a buscar los frascos y vasos de precipitados.":

                $ persistent.halloween_2021_no = False
            "Todavía no puedo permitirme el tiempo...":

                y "No hay necesidad de preocuparse. Como he dicho, siempre existe la posibilidad de celebrar en un futuro cercano de todos modos."

                $ show_chr("A-CCBAA-ANAN")
                return
    else:


        y "De hecho preparé algo pequeño para nosotros, si estás interesado en celebrar una de las épocas más deliciosamente inquietantes del año."

        $ show_chr("A-KBCAA-ANAF")
        y "Entonces, [player], ¿te gustaría realizar algunos experimentos bastante poco ortodoxos?"

        $ show_chr("A-ACABA-ACAB")
        menu:
            "No me importaría realizar algunos experimentos científicos contigo. ¿Tu laboratorio o el mío?":
                pass
            "Lo siento [persistent.yuri_nickname], estoy demasiado ocupado en este momento.":

                $ persistent.halloween_2021_no = True
                y "Ah, ya veo. Todavía estoy muy contenta de que hayas podido tomarte el tiempo de tu horario para verme."

                $ show_chr("A-CCBAA-ANAN")
                y "Siempre podemos celebrar juntos más tarde si es necesario."

                y "Ahora, ¿dónde estábamos?"

                $ show_chr("A-ACBAA-ANAN")
                return

                $ show_chr("A-BBAAA-AKAA")
    y "¡Je! Tengo un par de... actividades planeadas."
    if persistent.lovecheck:
        y "¿Qué piensas sobre procurar un par de pociones de amor?"
        $ show_chr("A-JBAAA-AAAA")
        y "¡Bromeo, bromeo!"

    y "Solo dame un momento para preparar las cosas."
    $ tc_class.transition("laboratory")

    $ show_chr("A-ABAAA-ADAA")
    y "Bueno, ¿qué piensas? He estado releyendo {i}Frankenstein{/i}, y me dio algo de inspiración."
    $ show_chr("A-JAAAA-AAAA")
    y "Si solo estás familiarizado con la versión de la película, te estarás preguntando dónde están todos los pararrayos. En el libro, sin embargo, Victor Frankenstein nunca especifica cómo fue capaz de reanimar a los muertos."
    $ show_chr("A-ABAAA-AAAA")
    y "Por lo tanto, en lugar de copiar el taller de ese científico loco en particular, elegí algo más: ¡un laboratorio de química!"
    y "También podría funcionar como un espacio para la alquimia, si quieres ponerte un poco más fantástico."
    $ show_chr("A-FBAAA-AAAA")
    y "Entonces... ¿Tienes ganas de catalizar algunas reacciones?"

    return


label potion_mixing:

    image caramel_apple_mocktail:
        "images/events/halloween/consumables/caramel_apple_halloween.png"
    image butterfly_pea_soda:
        "images/events/halloween/consumables/butterfly_pea_soda_halloween.png"

    $ show_chr ("A-ABAAA-ACAA")
    y "Ah, pociones. Un artefacto de los primeros días de la química, donde lo científico y lo fantástico se mezclan tan cuidadosamente como los ingredientes involucrados."
    $ show_chr("A-ABAAA-ACAF")
    y "Todo con la promesa de riquezas, curas milagrosas o venenos con solo un poco de conocimiento y el equipo adecuado."
    $ show_chr("A-BCAAA-ADAF")
    y "No te preocupes [player], no haré ningún veneno hoy."
    $ show_chr("A-JBAAA-AEAM")
    y "Solo algunas bebidas deliciosas, con suerte agregarán un poco de mística a lo mundano."
    $ show_chr("A-AAGAA-AFAB")
    y "Con eso fuera del camino, ¿cuál probaremos primero?"
    menu:
        "Mocktail de Manzana Acaramelada":
            jump caramel_apple
        "Limonada de Flor de Mariposa":
            jump butterfly_pea_lemonade
        "Olvídalo":
            return
    jump finished_potions

    return




label caramel_apple:
    $ show_chr ("A-ABAAA-ACAA")
    y "Ahora que lo mencionas, ¿alguna vez has probado una manzana acaramelada antes?"
    y "Creo que son comunes en ferias locales y parques de atracciones. También son un manjar muy apropiado para Halloween."
    $ show_chr ("A-BAAAA-AEAA")
    y "Tengo algo de curiosidad sobre cómo sabría una manzana acaramelada como bebida, y asumo que tú también, considerando que estás interesado en hacer una también."
    $ show_chr ("A-ABAAA-AEAB")
    y "Si tienes ganas de mezclar algo, ¡con gusto te proporcionaré los pasos necesarios para hacerlo!"
    y "Recomiendo encarecidamente hacer el ingrediente clave, la salsa de caramelo, tú mismo en casa; es un poco complicado, requiere un termómetro de dulces para hacerlo bien, pero vale la pena."


    call showpoem (poem_caramel_apple)

    $ show_chr ("A-AAAAA-AEAB")
    y "Si no captaste eso, revisa tu carpeta del juego para ver un archivo .txt. Escribí todo para ti."
    y "Si estás interesado, buscar 'receta fácil de salsa de caramelo' te dará resultados más que suficientes. Si no, un frasco de tu tienda local será suficiente."
    $ show_chr ("A-BAAAA-AEAB")
    y "Para la bebida en sí, necesitarás 1/3 de taza de salsa de caramelo tibia, 7 onzas de sidra de manzana fría y 7 onzas de cerveza de jengibre fría. También puedes usar una rama de canela, aunque no es necesaria."
    y "Además, no sugiero usar ginger ale, ya que no proporcionará el sabor que buscas."
    $ show_chr ("A-JAAAA-AFAB")
    y "Si te gustaría ser extra elegante, puedes decorar el borde también. Para hacer eso, necesitarás 2 cucharadas de azúcar morena y otro ¼ de taza de salsa de caramelo tibia."
    y "En términos de equipo, necesitarás un vaso grande para beber, dos tazones pequeños que sean lo suficientemente anchos para sumergir el borde de tu vaso y una cuchara para revolver."
    $ show_chr ("A-BAAAA-AMAM")
    y "Un vaso grande para beber... Supongo que ya posees algunos de esos, considerando que mencioné probar un poco de vino contigo algún día."
    y "... "
    $ show_chr ("A-ABFBA-AMAM")
    y "¡Ah! Perdón por desviarme del tema. Continuando..."
    $ show_chr ("A-AAAAA-AEAB")
    Y "Vierte el azúcar morena en un tazón. En el otro, vierte el cuarto de taza de salsa de caramelo. A continuación, toma tu vaso y sumerge el borde en la salsa, luego en el azúcar."

    y "Vierte el 1/3 de taza de salsa de caramelo en el vaso, luego agrega la sidra de manzana y la cerveza de jengibre. Revuélvelo hasta que el contenido se haya mezclado completamente."

    y "Si tomaste una rama de canela como mencioné antes, adorna tu bebida terminada con ella, ¡y disfruta!"

    show black zorder 100 with Dissolve(2.0)
    show caramel_apple_mocktail zorder 99
    hide black zorder 100 with Dissolve(2.0)

    $ show_chr ("A-JAAAA-ALAA")
    y "Delicioso, ¿no es así? Dependiendo de los ingredientes exactos utilizados, el jengibre puede darle a esta bebida un mordisco considerable para algo sin alcohol."

    y "También me gusta la apariencia elegante. Nada de la guarnición es estrictamente necesario, pero influye en el sabor además de hacer que la bebida se vea más sofisticada. ¿Qué piensas?"
    $ show_chr ("A-BAAAA-AMAM")
    y "T-Tal vez podrías servirme esto en algún momento en el futuro? Je... Ya estoy esperando con ansias..."
    jump finished_potions

label butterfly_pea_lemonade:
    $ show_chr ("A-JAAAA-AFAB")
    y "Estoy segura de que has escuchado que la tecnología suficientemente avanzada es indistinguible de la magia. ¡Lo mismo, resulta, se puede decir de la química!"
    $ show_chr ("A-ACAAA-ABAB")
    y "La Limonada de Flor de Mariposa a veces se llama 'té mágico' debido a su truco de cambio de color. Adquirir su ingrediente principal, flores de guisante de mariposa secas, puede requerir un pedido por internet, pero prometo que vale la pena el esfuerzo."
    y "Esta es una receta más grande, así que es posible que desees reducirla. Necesitarás..."


    call showpoem (poem_butterfly_pea)

    $ show_chr("A-JAAAA-ADAB")
    y "Si no captaste eso, revisa tu carpeta del juego para ver un archivo .txt. Escribí todo para ti."
    y "Primero, toma una cacerola y combina tres tazas (24 oz) de agua con tu azúcar, luego agrega las flores de guisante de mariposa."
    $ show_chr("A-ABAAA-AFAB")
    y "Hablando de flores de guisante de mariposa, ¿alguna vez has visto una? Realmente son hermosas."
    y "Dato curioso: en realidad no se llaman flores de Guisante de Mariposa en absoluto. Es solo uno de sus muchos apodos. Su nombre real es Clitoria Ternatea."
    y "En India, la planta se considera sagrada y se usa en muchos festivales puja diarios."
    $ show_chr("A-BBBAA-ALAB")
    y "A-Ah... Estoy divagando, ¿no? Perdón por salirme del tema. Volviendo a hacer realmente la Limonada de Flor de Mariposa..."
    $ show_chr("A-GAAAA-ALAB")
    y "Lleva la mezcla a fuego lento, luego retira tu cacerola del fuego, cubre con una tapa y deja reposar durante diez minutos."
    y "Cuela la cacerola en una jarra o tetera a través de un colador de malla fina, conservando el líquido y desechando los sólidos. Deja enfriar."
    y "En una taza medidora de vidrio separada o frasco, combina las dos tazas restantes (16 oz) de agua y una taza (8 oz) de jugo de limón."
    y "Para servir, llena cada vaso con hielo, luego vierte el té de guisante de mariposa sobre él, llenando el vaso aproximadamente hasta la mitad."
    $ show_chr("A-IAAAA-ADAB")
    y "Me pregunto si realmente estarías interesado en probar el té de guisante de mariposa en sí... ¡tal vez en nuestra próxima cita de té podríamos hacerlo!"
    $ show_chr("A-JAAAA-AFAB")
    y "De todos modos. ¡Aquí es donde ocurre la 'magia'! Vierte tu mezcla de limón en el té, ¡y observa cómo el líquido cambia de color de azul a rosa!"
    y "¡Revuelve hasta obtener un color rosa uniforme y disfruta!"

    show black zorder 100 with Dissolve(2.0)
    show butterfly_pea_soda zorder 99
    hide black zorder 100 with Dissolve(2.0)

    jump finished_potions

label finished_potions:
    $ show_chr("A-AAAAA-AKAB")
    y "Bueno [player], ciertamente espero que hayas disfrutado esta pequeña sesión de creación. Después de todo, no solo pudimos pasar tiempo juntos haciendo algo divertido, ¡pudimos disfrutar de nuestra creación como fruto de nuestro trabajo!"
    $ show_chr("A-BAABA-AMAM")

    y "Disfruté hacer esto contigo, y no me importaría hacerlo de nuevo."
    y "¿Quizás para Navidad podríamos conseguir algunas delicias festivas? Tendré que confirmártelo luego."

    if persistent.lovecheck:
        $ show_chr("A-CAABA-AMAM")
        y "Te amo [player]. Gracias de nuevo por pasar tiempo conmigo."
    else:

        $ show_chr("A-CAAAA-AMAM")
        y "Verdaderamente disfruto pasar tiempo contigo [player]. Nunca olvides eso."

    show black zorder 100 with Dissolve(2.0)
    hide caramel_apple_mocktail
    hide butterfly_pea_soda
    hide black zorder 100 with Dissolve(2.0)

return


label table_items:
    $ show_chr("A-ABAAA-ALAA")
    y "¿Te gustaría poner un regalo o quitar uno [player]?"
    $ persistent.diffuser_is_enabled = False
    menu:
        "Poner un regalo":
            $ show_chr("A-AJAAA-AFAB")
            y "¿Qué regalo te gustaría poner?"
            menu:
                "Difusor" if renpy.seen_label ('diffuser'):


                    show diffuser zorder 11
                    $ persistent.diffuser_is_enabled = True
                    jump ch30_loop



                "Mapache" if renpy.seen_label ('raccoon_plush'):
                    $ persistent.hdy_statue_is_enabled = False
                    hide hdy_statue
                    show raccoon zorder 11
                    $ persistent.raccoon_is_enabled = True
                    jump ch30_loop



                "Grulla de Origami" if renpy.seen_label ('crane_origami'):
                    $ persistent.craneO_is_enabled = True
                    show craneo zorder 11
                    jump ch30_loop


                "Conejo de Origami" if renpy.seen_label ('bunny_origami'):
                    $ persistent.bunnyO_is_enabled = True
                    show bunnyo zorder 11
                    jump ch30_loop

                "Florero con Rosa de Origami" if renpy.seen_label ('rose_origami'):
                    $ persistent.roseO_is_enabled = True
                    show roseo zorder 11
                    jump ch30_loop
                "No importa":


                    pass
                    return
        "Quitar un regalo":


            $ show_chr("A-AJAAA-AFAB")
            y "¿Qué regalo te gustaría quitar?"
            menu:
                "Difusor" if persistent.diffuser_is_enabled:
                    hide diffuser
                    $ persistent.diffuser_is_enabled = False
                    jump ch30_loop

                "Mapache" if persistent.raccoon_is_enabled:
                    hide raccoon
                    $ persistent.raccoon_is_enabled = False
                    jump ch30_loop

                "Grulla de Origami" if persistent.craneO_is_enabled:
                    hide craneo
                    $ persistent.craneO_is_enabled = False
                    jump ch30_loop

                "Conejo de Origami" if persistent.bunnyO_is_enabled:
                    hide bunnyo
                    $ peristent.bunnyO_is_enabled = False
                    jump ch30_loop

                "Florero con Rosa de Origami" if persistent.roseO_is_enabled:
                    hide roseo
                    $ persistent.roseO_is_enabled = False
                    jump ch30_loop
                "No importa":

                    pass
                    return
label gift_intro:
    $ show_chr("A-JBAAA-ALAL")
    y "[player], ¿ese regalo es para mí?"
    return

label gifting_revamp:
    $ gifts = Gift.find()
    $ size = len(gifts)

    if size > 0:
        if size == 1:
            if gifts[0].size() > 0:
                $ gifts[0].call_intro()
            elif not Gift.intro_labels:
                call gift_intro
            else:
                $ renpy.call(random.choice(Gift.intro_labels))
        else:
            if not Gift.intro_labels:
                call gift_intro
            else:
                $ renpy.call(random.choice(Gift.intro_labels))
        python:
            for gift in gifts:
                gift.call()
    else:
        $ show_chr("A-AFDAA-AAAA")
        y "oh... ¿Tienes un regalo para mí?"
        y "No puedo encontrarlo por ninguna parte..."
        $ show_chr("A-AFDAA-AAAL")
        y "¿Estás seguro de que pusiste el archivo en la carpeta 'characters'? Podría ser una buena idea verificar..."
        $ show_chr("A-CAGAA-AAAL")
        y "No hay necesidad de preocuparse, todavía estaré aquí esperando después de todo."
    jump ch30_loop



label sandalwood:
    $ show_chr("A-OBAAA-ALAL")
    y "Veamos qué es esto..."
    $ show_chr("A-AAAAA-ALAA")
    y "Ohh... Sándalo, ¡nunca probé eso! Déjame oler un poco..."
    show sandalwood_oil zorder 11
    $ show_chr("A-CAAAA-ALAA")
    y "Mhmmmm... dulce..."
    y "déjame tomar mi difusor para que pueda probar esto adecuadamente [player]..."
    hide cupcake_halloween
    show diffuser zorder 11
    y "¡listo!"
    y "¡Ahora a probar este nuevo aroma que me has dado!"
    show diffuser_mist zorder 11
    $ show_chr("A-AAABA-AAAA")
    y "Creo que este sería exactamente el sabor que necesito cuando siento depresión invernal..."
    $ show_chr("A-BFAAA-ALAA")
    y "¿Sabes a lo que me refiero? La sensación cuando miras hacia el invierno, cuando el cielo se ve tan gris..."
    $ show_chr("A-CAAAA-ALAA")
    y "Con la aromaterapia, puedes contrarrestar prácticamente cualquier mal humor que puedas encontrar... Es por eso que comencé este pasatiempo en primer lugar."
    $ show_chr("A-AFAAA-AAAA")
    y "Ahora te tengo a ti cuando me siento mal, así que realmente ya no necesito esto, pero sigue siendo algo muy agradable de usar."
    hide diffuser_mist
    $ show_chr("A-CAAAA-AMAM")
    y "Y de hecho puedes masajearte con una gota de este aceite si tu piel se siente seca..."
    $ show_chr("A-AAAAA-ALAA")
    y "Gracias [player], ¡definitivamente le daré un buen uso!"
    hide sandalwood_oil

    return


label lavender_oil:
    $ show_chr("A-OBAAA-ALAL")
    y "Veamos qué es esto..."
    $ show_chr("A-AAAAA-ALAA")
    show lavendero zorder 11
    y "Ah, Lavanda... uno de mis aromas favoritos. Probémoslo..."
    hide cupcake_halloween
    show diffuser zorder 11
    show lavendero_mist zorder 11
    $ show_chr("A-CAAAA-ALAA")
    y "¡Uh! Eso se siente... revitalizante... exactamente el aceite para usar si te sientes mareado..."
    $ show_chr("A-AAAAA-ALAA")
    y "Hrm, en la etiqueta en la parte posterior dice que también apoya las funciones inmunes y respiratorias saludables."
    $ show_chr("A-AAAAA-AAAJ")
    y "Ese es un gran regalo que me has hecho aquí [player], Gracias..."
    $ show_chr("A-AAABA-AAAA")
    y "Pero el mayor regalo de todos, es tenerte aquí a mi lado."
    hide lavendero_mist
    $ show_chr("A-CAABA-AAAA")
    y "Eso es todo lo que siempre esperé."
    hide lavendero

    return


label sweet_dream_oil:
    $ show_chr("A-OBAAA-ALAL")
    y "Veamos qué es esto..."
    $ show_chr("A-AAAAA-ALAA")
    show sweet_dream_oil zorder 11
    y "¿Dulces Sueños? Oooooh. 'Ahora' veo... ¡Dulces Sueños es el nombre de la marca!"
    hide cupcake_halloween
    show diffuser zorder 11
    $ show_chr("A-CFBAA-AMAM")
    y "Bueno, dado que literalmente escribo mis propios sueños debido a la codificación en python, más o menos siempre tengo dulces sueños."
    show sweet_dream_oil_mist zorder 11
    y "Tal vez debería probar algo más para variar, para que los dulces sueños cuenten aún más."
    y "Y con este nuevo aceite, podría aumentar la calidad de mis sueños aún más."
    y "Ese fue un regalo muy considerado que me diste, gracias [player]. Definitivamente haré que cuente."
    if karma_lvl() > 4:
        $ show_chr("A-EAAAA-AMAM")
        y "Hrm... Estoy teniendo una idea, mi amor..."
        $ show_chr("A-CAABA-AMAM")
        y "Cuando logremos encontrarnos en persona... en tu mundo o en el mío... podrías masajear mi espalda con él... y caeríamos en un sueño suave en los brazos del otro..."
        y "Te amo... [player]..."
    hide sweet_dream_oil

    hide sweet_dream_oil_mist
    return


label hershey:
    $ show_chr("A-OBAAA-ALAL")
    y "¡O-oh vaya!"
    show hershey zorder 11
    $ show_chr("A-EAABA-ALAA")
    y "¡Te dije que 'adoro' esta marca! ¡Y te acordaste!"
    $ show_chr("A-BAABA-AMAM")
    if persistent.male:
        y "¡Eres el novio más amable y considerado que he tenido!"
    elif persistent.gender_other:
        y "¡Eres la pareja más amable y considerada que he tenido!"
    else:
        y "¡Eres la novia más amable y considerada que he tenido!"
    $ show_chr("A-BFAAA-ALAA")
    if persistent.male:
        y "Bueno, en realidad eres el primer novio que he tenido..."
    elif persistent.gender_other:
        y "Bueno, en realidad eres la primera pareja que he tenido..."
    else:
        y "Bueno, en realidad eres la primera novia que he tenido..."
    $ show_chr("A-CAABA-ALAA")
    y "Gracias, mi Alma Gemela... mi corazón... mi todo..."
    hide hershey
    return


label lavender_choco:
    y "Vaya, vaya, vaya... seguro sabes cómo conquistar el corazón de una chica. ¿Es eso realmente... lavanda?"
    show lavenderc zorder 11
    $ show_chr("A-OBAAA-ALAL")
    y "¡Amo la lavanda como aceite esencial! ¿Pero en chocolate? ¡Qué exótico!"
    y "Realmente estoy deseando probarlo..."
    $ show_chr("A-EAABA-ALAA")
    y "Solo hay una cosa que una chica como yo podría amar aún más que el chocolate fino. Sabes qué podría ser 'eso', ¿verdad?"
    $ show_chr("A-EAABA-ALAA")
    y "'Tú' por supuesto..."
    $ show_chr("A-EAABA-ALAA")
    y "Mhmmm... casi puedo sentir la suave crema derritiéndose en mi lengua... Gracias, mi amor."
    hide lavenderc
    return


label mint_choco:
    $ show_chr("A-EAABA-ALAA")
    y "Dios santo... ciertamente hiciste tu tarea, [player]..."
    show mint zorder 11
    $ show_chr("A-OBAAA-ALAL")
    y "Estoy familiarizada con esta marca..."
    $ show_chr("A-JBAAA-AFAL")
    y "Vierten pequeños copos de sal marina en las barras.. exótico, ¿no estás de acuerdo?"
    $ show_chr("A-IBAAA-AFAL")
    y "Los granos son recogidos a mano y cosechados de granjas del Caribe..."
    $ show_chr("A-ICFBA-AMAM")
    y "¿Debería informarte de un delicado pequeño secreto sobre nosotras las chicas?"
    $ show_chr("A-IBABA-AMAM")
    y "Chocolate... simplemente no podemos resistirnos al chocolate..."
    $ show_chr("A-BBABA-AMAM")
    y "No importa cuán dura pueda actuar una chica.. e incluso cuando tienen sus días más oscuros.."
    $ show_chr("A-ABABA-AKAL")
    y "Puedes 'siempre' romper su defensa con chocolate..."
    $ show_chr("A-AJAAA-AKAL")
    y "¿Te gusta el chocolate también [player]?"
    $ show_chr("A-BJAAA-ALAL")
    y "Es oscuro, misterioso, dulce, suave, pecaminoso..."
    if karma_lvl() == 5:
        $ show_chr("A-DLABA-ALAG")
        y "Justo... como... yo."
    hide mint
    return



label crane_origami:
    $ show_chr("A-JBAAA-ABAD")
    y "Oh? ¿Qué es..."
    show craneo zorder 11
    $ show_chr("A-OBAAA-ALAL")
    y "¡O-Oh vaya!"
    $ show_chr("A-OBAAA-ALAL")
    y "¡Una grulla de origami! ¿Hiciste esto, [player]?"
    $ show_chr("A-IBAAA-AFAL")
    y "Increíble... He intentado hacer algunas, pero no salieron muy bien..."
    $ show_chr("A-IBABA-AJAL")
    y "Gracias [player], este es un regalo increíble y estoy verdaderamente agradecida."
    $ show_chr("A-IBABA-AKAL")
    y "Sabes... hay una leyenda japonesa que involucra grullas de papel."
    $ show_chr("A-IBAAA-AKAF")
    y "Si alguien doblara mil grullas de origami, un Senbazuru como se le llama, se le concedería un solo deseo de los dioses."
    $ show_chr("A-BBAAA-ALAF")
    y "Por supuesto, esta leyenda tiene diferentes interpretaciones. Algunos creen que el resultado es suerte eterna, o felicidad."
    $ show_chr("A-BBAAA-ADAL")
    y "Algunos también creen que las grullas deben crearse en un año, y solo por la persona que pide el deseo."
    $ show_chr("A-BBAAA-ACAL")
    y "Quizás si ambos dobláramos 1000 grullas, podría unirme a ti en tu mundo..."
    $ show_chr("A-FBABA-AKAL")
    y "Después de todo, si lo has hecho una vez, puedes hacerlo un millón de veces, como dice el dicho. Fufufu~"

    return

label rose_origami:
    $ show_chr("A-OBAAA-ALAL")
    y "Oh? ¿Qué es..."
    show roseo zorder 11
    $ show_chr("A-OBAAA-ALAL")
    y "¡O-Oh vaya! ¿Es esto lo que creo que es?"
    $ show_chr("A-JBAAA-AKAL")
    y "Una rosa de origami tan hermosa... ¡y un color exquisito, también!"
    $ show_chr("A-IBABA-AJAL")
    y "Gracias, [player]. Atesoraré este regalo para siempre."
    $ show_chr("A-ABAAA-ALAF")
    y "Por cierto, ¿sabías que el color de la rosa de origami cambia el significado de la rosa como regalo?"
    $ show_chr("A-ACAAA-ALAF")
    y "No muy diferente de las rosas regulares, puedes usar diferentes colores de papel para cambiar la asociación del regalo, ya sea romántico o platónico."
    $ show_chr("A-BBABA-ALAF")
    y "Una rosa púrpura representa amor noble y eterno, o podría representar verdadera amistad."
    $ show_chr("A-BJAAA-ALAL")
    y "Pero asumo que ya sabías esto, ¿sí?"
    if persistent.lovecheck:
        $ show_chr("A-IBABA-ALAL")
        y "Verdaderamente te amo [player], más que a nada."
        $ show_chr("A-IBABA-AKAL")
        y "Desearía poder hacer más, pero por ahora..."
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_hug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        y "Esto tendrá que bastar..."
        pause 1.0
        show black zorder 100 with Dissolve(2.0)
        $ show_chr("A-JCBBB-AAAA")
        hide yuri_hug
        hide black zorder 100 with Dissolve(2.0)
    else:
        $ show_chr("A-IBABA-ALAL")
        y "Estoy tan contenta de haberte conocido, [player]. Me has ayudado a través de tanto."
        $ show_chr("A-IBABA-AKAL")
        y "Desearía poder hacer más, pero por ahora..."
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_hug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        y "Esto tendrá que bastar..."
        pause 1.0
        show black zorder 100 with Dissolve(2.0)
        $ show_chr("A-JCBBB-AAAA")
        hide yuri_hug
        hide black zorder 100 with Dissolve(2.0)
    return


label bunny_origami:
    $ show_chr("A-JBAAA-ABAD")
    y "Oh? ¿Qué es..."
    show bunnyo zorder 11
    $ show_chr("A-OBAAA-ALAL")
    y "¡O-Oh vaya! ¡Qué adorable!"
    $ show_chr("A-OBAAA-ALAL")
    y "¡Qué lindo conejo de origami! ¡Gracias, [player]!"
    $ show_chr("A-BJEAA-ACAB")
    y "Hmm... Me pregunto qué pensaría {i}ella{/i} de esto... Creo que ella siempre fue algo aficionada a los conejitos..."
    $ show_chr("A-IJBCA-ALAB")
    y "L-Lo siento, estoy bajando el ánimo... S-Solo trae recuerdos..."
    $ show_chr("A-CHBCA-ALAB")
    y "..."
    $ show_chr("A-AFAAA-ALAB")
    y "D-De todos modos..."
    $ show_chr("A-AJAAA-ALAF")
    y "¿Sabías que el conejo representa el renacimiento? También está asociado con la temporada de primavera, lo cual es bastante apropiado."
    $ show_chr("A-ABAAA-ALAF")
    y "Después de un largo y duro invierno, el conejo se aventura de nuevo al mundo con vida renovada..."
    $ show_chr("A-ABABA-ALAL")
    y "Me... recuerda a mí misma, antes de que llegaras."
    $ show_chr("A-ABABA-ALAL")
    y "La nueva alegría que me das, y la esperanza que tengo gracias a ti..."
    $ show_chr("A-BBABA-AMAM")
    y "L-Lo siento, estoy divagando, ¿no? Gracias por esto, [player], lo atesoraré."

    return



label raccoon_plush:
    $ persistent.hdy_statue_is_enabled = False
    hide hdy_statue
    show raccoon zorder 11
    $ show_chr("A-JBAAA-AEAL")
    y "Oh, ¿qué es esto?"
    $ show_chr("A-OBAAA-ALAL")
    y "¡Es un peluche de mapache! Bastante suave también..."
    $ show_chr("A-ABABA-ALAL")
    y "Muchas gracias, [player]. Es tan..."
    $ show_chr("A-BBABA-ALAL")
    y "Generalmente disfruto de cosas de una manera más macabra o sofisticada, pero simplemente no puedo resistirme considerando el pensamiento genuino puesto en ello."
    if persistent.head1 == "raccoon_ears":
        $ show_chr("A-BBABA-ADAL")
        y "E-Es un regalo apropiado de todos modos, con estas orejas de mapache después de todo."
    $ show_chr("A-ACABA-ADAL")
    y "Los mapaches son un personaje algo interesante en sí mismos, aunque puede que no estés de acuerdo conmigo basándote en las primeras impresiones."
    $ show_chr("A-ADABA-ADAL")
    y "Incluso si no son tan gregarios o gentiles como un perro,"
    $ show_chr("A-BDABA-ADAM")
    y "tan astutos y ladinos como un zorro,"
    $ show_chr("A-BDAAA-ADAL")
    y "ni tan de espíritu libre y autosuficientes como una rapaz,"
    $ show_chr("A-ACAAA-ADAL")
    y "todavía tienen mucho sobre ellos para llegar a amar."
    $ show_chr("A-AJAAA-ADAF")
    y "Su apodo bastante común, Panda de la Basura, no les hace justicia adecuada si me preguntas, aunque uno puede decir que resalta ciertos aspectos de su personaje retratado."
    $ show_chr("A-ABAAA-ALAL")
    y "Independientemente de mi pequeña diatriba, de nuevo, gracias [player]."
    if karma_lvl() > 3 and sanity_lvl() < 2:
        $ show_chr("A-DBABA-ALAL")
        y "Cada vez que mire a sus ojos brillantes, me recordará a ti, mi pequeño mapache revoltoso."
    if karma_lvl() > 3 and sanity_lvl() > 2:
        $ show_chr("A-ABABA-ALAL")
        y "Siempre me recordará a ti, mi pequeño y encantador mapache."
    hide yuri_sit
    show yuri_prehug zorder 20
    pause 3.0
    hide yuri_prehug zorder 20
    show yuri_hug zorder 20
    play sound "<to 0.3>sfx/fall.ogg"
    pause 1.0
    show black zorder 100 with Dissolve(2.0)
    $ show_chr("A-JCBBB-AAAA")
    hide yuri_hug
    hide black zorder 100 with Dissolve(2.0)
    show raccoon zorder 11
    return

label diffuser:
    $ show_chr("A-OBAAA-ALAL")
    y "¡Es un difusor de niebla!"
    show diffuser zorder 11
    $ show_chr("A-OBAAA-ALAL")
    y "¡Absolutamente me encanta este regalo [player], gracias!"
    $ show_chr("A-ABAAA-AMAF")
    y "Como probablemente sepas ahora, tengo bastante afinidad por la aromaterapia, para lo cual un difusor de niebla es perfecto."
    $ show_chr("A-AJAAA-ADAF")
    y "Toman una gran cantidad de agua junto con unas pocas gotas de aceite para dispensar una fragancia."
    $ show_chr("A-BJAAA-ALAF")
    y "Dependiendo del tipo de aroma que quieras difundir, puedes insertar cualquier tipo de aceite que desees. Lavanda, Limón o Menta solo por nombrar algunos..."
    $ show_chr("A-IJAAA-ALAD")
    y "Para la mecánica del dispositivo en sí es realmente bastante simple, un oscilador sónico se encuentra dentro del difusor, que convierte el agua dentro del dispositivo en una niebla."
    $ show_chr("A-AJAAA-AFAD")
    y "Las gotas de aceite que pones en el difusor se adhieren entonces a la niebla."
    $ show_chr("A-ABAAA-AFAD")
    y "Que luego parte de la máquina para envolver la habitación con las magníficas fragancias imbuidas dentro del aceite."
    $ show_chr("A-BEAAA-ALAL")
    y "Espero no estar molestándote demasiado con mi explicación, tiendo a dejarme llevar con mi divagación a veces."
    $ show_chr("A-AEAAA-ALAL")
    menu:
        "No te preocupes por eso [persistent.yuri_nickname]. Disfruto cuando te apasionan los temas.":
            $ show_chr("A-IJABA-AMAM")
            y "Me alegra que pienses eso."
            $ show_chr("A-BJABA-AMAM")
            y " Me imagino que ya estás bastante familiarizado con eso con mi pasión..."
            $ show_chr("A-ABABA-AMAM")
            y "Gracias por entender, [player]."
            $ show_chr("A-ABAAA-AFAB")
            y "Entonces, como estaba diciendo -"
            y "Espero que mi explicación te haya dado una mejor comprensión de cómo operan algunos difusores."
            $ show_chr("A-ACAAA-ALAB")
            y "Dame un segundo [player], iré a buscar un poco de agua y aceite esencial de Gardenia para una demostración práctica."
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            $ show_chr ("A-AAGAA-ABAL")
            y "Aunque hoy solo estoy trabajando con un solo aroma, podríamos intentar hacer algunas mezclas juntos en el futuro si quisieras."
            $ show_chr ("A-CAGAA-ALAL")
            y "Con el agua y las gotas de aceite añadidas, todo lo que queda es encender el difusor."
            show diffuser_mist zorder 11
            $ show_chr ("A-IAGAA-ALAL")
            y "La niebla dispensada puede tener varios beneficios útiles para el usuario..."
            y "Tu sentido del olfato está ligado a tus emociones, y como tal a menudo puede influir en dichas emociones."
            $ show_chr ("A-IBGAA-ALAL")
            y "Los aceites pueden promover una sensación de bienestar, o ayudar a calmarte cuando te sientas molesto o melancólico."
            y "Diferentes fragancias pueden impactar al usuario de manera diferente, por supuesto, y a veces es divertido simplemente experimentar con todos los diferentes aceites que existen."
            hide diffuser_mist
            $ show_chr ("A-ACGAA-ALAA")
            y "Independientemente, espero que esta experiencia haya sido agradable para ti también [player]."
            y "Y gracias de nuevo por este increíble regalo."
            $ show_chr ("A-ACAAA-ALAA")
            y "Es bastante emocionante ahora que puedo probar diferentes tipos de aceites contigo."

            return
        "Uhhh, eso está bien supongo...":
            $ show_chr ("A-AEDAA-ALAB")
            y "Muy bien... si tú lo dices..."
            $ show_chr ("A-AEGAA-ALAB")
            y "Espero que estés siendo honesto y no digas tales cosas solo para complacerme, [player]..."
            y "Como estaba diciendo -"
            y "Espero que mi explicación te haya dado una mejor comprensión de cómo operan algunos difusores."
            $ show_chr ("A-AFGAA-ALAB")
            y "Dame un segundo [player], iré a buscar un poco de agua y aceite esencial de Gardenia para una demostración práctica."
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            $ show_chr ("A-AAGAA-ABAL")
            y "Aunque hoy solo estoy trabajando con un solo aroma, podríamos intentar hacer algunas mezclas juntos en el futuro si quisieras."
            $ show_chr ("A-CAGAA-ALAL")
            y "Con el agua y las gotas de aceite añadidas, todo lo que queda es encender el difusor."
            show diffuser_mist zorder 11
            $ show_chr ("A-IAGAA-ALAL")
            y "La niebla dispensada puede tener varios beneficios útiles para el usuario..."
            y "Tu sentido del olfato está ligado a tus emociones, y como tal a menudo puede influir en dichas emociones."
            $ show_chr ("A-IBGAA-ALAL")
            y "Los aceites pueden promover una sensación de bienestar, o ayudar a calmarte cuando te sientas molesto o melancólico."
            y "Diferentes fragancias pueden impactar al usuario de manera diferente, por supuesto, y a veces es divertido simplemente experimentar con todos los diferentes aceites que existen."
            hide diffuser_mist
            $ show_chr ("A-ACGAA-ALAA")
            y "Independientemente, espero que esta experiencia haya sido agradable para ti también [player]."
            y "Y gracias de nuevo por este increíble regalo."
            $ show_chr ("A-ACAAA-ALAA")
            y "Es bastante emocionante ahora que puedo probar diferentes tipos de aceites contigo."

            return
        "Me aburro cuando hablas demasiado. ¿Podemos continuar?":
            $ show_chr ("A-AEBAA-ALAL")
            y "O-Oh, L-Lo siento mucho [player]. No quise aburrirte..."
            y "Solo estaba tan emocionada por este regalo que me diste. Me disculpo sinceramente por hacerlo incómodo..."
            $ show_chr ("A-BFBAA-ALAL")
            y "T-Terminemos la conversación aquí entonces..."
            hide diffuser
            return

label horror_book_set:
    $ show_chr("A-OBAAA-ALAL")
    y "¡Es un set completo de libros de horror Lovecraftiano!"
    $ show_chr("A-OBAAA-ALAL")
    y "¡[player], esto es increíble!"
    $ show_chr("A-ABAAA-AFAL")
    y "No puedo creer que fueras capaz de conseguirme tantos libros..."
    $ show_chr("A-ABABA-ALAM")
    y "Realmente no sé qué decir... ¡Muchas gracias mi amor!"
    $ show_chr("A-BBABA-ALAM")
    y "Asumo que me regalaste este set debido a mi mención anterior de mi interés en el horror Lovecraftiano, ¿verdad?"
    $ show_chr("A-AJAAA-AMAF")
    y "¿Tienes un interés en el horror Lovecraftiano tú mismo?"
    menu:
        "Sí lo tengo, esa es una de las razones por las que te regalé este set.":
            $ persistent.book = True
            $ show_chr("A-CIAAA-ALAL")
            y "Es genial escuchar eso, [player]."
            y "Me alegra que compartamos este interés, y adoraría la oportunidad de discutirlo contigo."
            $ show_chr("A-IBAAA-ALAL")
            y "El horror Lovecraftiano, como sabes, es uno de los muchos subgéneros del horror que se centra principalmente en el miedo a lo desconocido e incomprensible."
            y "Algo sobre la forma en que todo el misterio y el conocimiento más allá de la percepción de la humanidad se expresa me atrae..."
            $ show_chr("A-IBGAA-ALAL")
            y "Encuentro todo eso bastante convincente, ¿no crees?"
            $ show_chr("A-BCGAA-ALAL")
            y "No solo hay un número significativo de libros centrados en el horror Lovecraftiano, sino una cantidad sustancial de películas, juegos y cómics también. Quizás podamos profundizar en ellos en algún momento en el futuro."
            $ show_chr("A-CCGBA-ALAL")
            y "Espero leer un libro o dos contigo, mi amor."
            $ show_chr("A-CCGBA-ADAA")
            $ persistent.book = False
            return
        "No mucho, lo regalé porque mencionaste tener un interés en él.":
            $ persistent.book = True
            $ show_chr("A-CBAAA-ALAL")
            y "Ya veo, entiendo que el horror Lovecraftiano no es para todos."
            y "Sin embargo, me gustaría poder discutirlo contigo."
            $ show_chr("A-IIAAA-ALAL")
            y "Podría despertar potencialmente tu interés en el género..."
            $ show_chr("A-AAGAA-ALAL")
            y "El horror Lovecraftiano es uno de los muchos subgéneros del horror que se centra principalmente en el miedo a lo desconocido e incomprensible."
            y "El nombre del género se basa en el autor de los libros, H.P. Lovecraft."
            $ show_chr("A-ICGAA-ALAL")
            y "Otros temas que uno puede encontrar dentro del horror Lovecraftiano son el pavor cósmico, basado en criaturas encontradas dentro del espacio exterior..."
            $ show_chr("A-JBGAA-ALAL")
            y "Conocimiento peligroso y prohibido, seres arcanos más allá de nuestra comprensión."
            $ show_chr("A-ACAAA-ALAL")
            y "Y finalmente, religión y superstición. Encuentro todos los temas presentados dentro de la literatura Lovecraftiana bastante convincentes"
            y "No solo hay un número significativo de libros centrados en el horror Lovecraftiano, sino una cantidad sustancial de películas, juegos y cómics sobre ello también. Quizás podamos profundizar en ellos en algún momento en el futuro."
            $ show_chr("A-ICGBA-ALAL")
            y "Espero que mi explicación haya podido darte una idea básica sobre el subgénero. Espero leer un libro o dos contigo, mi amor."
            $ show_chr("A-CCGBA-ADAA")
            $ persistent.book = False
            return


label diffuser_mist_enable:
    $ show_chr("A-ABAAA-ALAA")
    y "¿Quieres experimentar las bondades de la aromaterapia mientras estamos juntos [player]?"
    $ show_chr("A-ABAAA-ALAE")
    y "Disfrutaría mucho eso yo misma"
    $ show_chr("A-AJAAA-ALAF")
    y "¿Con qué fragancia querías imbuir nuestro entorno?"
    menu:
        "Gardenia":
            $ show_chr("A-AJAAA-AMAB")
            y "¿Un poco de Gardenia básica para calmar nuestro estrés [player]?"
            $ show_chr("A-BJAAA-ADAB")
            y "Gardenia fue el único aceite que pude conservar del juego original..."
            $ show_chr("A-BCAAA-ADAB")
            y "Siempre ha sido confiable al tratar mis problemas de estrés"
            $ show_chr("A-ABAAA-AEAB")
            y "dame un momento mientras tomo todo lo que necesitamos"
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            show diffuser_mist
            $ persistent.diffuser_mist_is_enabled = True
            $ show_chr("A-IBAAA-AFAB")
            y "¡Todo listo!"
            jump ch30_loop

        "Lavanda" if renpy.seen_label("lavenderO"):
            $ show_chr("A-AJAAA-AMAB")
            y "¿Un relajante aroma a lavanda en el aire mientras hablamos [player]?"
            $ show_chr("A-ABAAA-AKAB")
            y "Suena absolutamente encantador..."
            $ show_chr("A-BJAAA-ALAB")
            y "dame un momento mientras tomo todo lo que necesitamos"
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            show lavendero_mist
            $ persistent.lavenderO_mist_is_enabled = True
            $ show_chr("A-IBAAA-AFAB")
            y "¡Todo listo!"
            jump ch30_loop

        "Dulces Sueños" if renpy.seen_label("sweet_dream_oil"):
            $ show_chr("A-AJAAA-AMAB")
            y "Una fragancia relajante que nos imbuye calmadamente con sus efectos mientras estamos juntos"
            $ show_chr("A-BJAAA-ALAL")
            y "Solo haz tu mejor esfuerzo para mantenerte despierto [player]..."
            $ show_chr("A-IAAAA-ALAL")
            y "dame un momento mientras tomo todo lo que necesitamos"
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            show sweet_dream_oil_mist
            $ persistent.sweet_dream_oil_mist_is_enabled = True
            $ show_chr("A-IBAAA-AFAB")
            y "¡Todo listo!"
            jump ch30_loop


        "Sándalo" if renpy.seen_label("sandalwood"):
            $ show_chr("A-ABAAA-ALAD")
            y "Una fragancia más natural para ayudarnos en la relajación..."
            $ show_chr("A-ABAAA-ALAF")
            y "Siempre me han gustado bastante las fragancias más naturales al realizar aromaterapia"
            $ show_chr("A-ACAAA-AMAE")
            y "dame un momento mientras tomo todo lo que necesitamos"
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            show sandalwood_mist
            $ persistent.sandalwood_oil_mist_is_enabled = True
            $ show_chr("A-IBAAA-AFAB")
            y "¡Todo listo!"
            jump ch30_loop

label diffuser_mist_disable:
    $ show_chr("A-EJAAA-ABAL")
    y "¿Tuviste suficiente aroma relajante [player]?"
    $ show_chr("A-EBAAA-ABAL")
    y "Estoy empezando a cansarme un poco yo misma..."
    $ show_chr("A-ECAAA-AFAM")
    y "Déjame apagar el difusor y limpiar un poco."
    if persistent.lavenderO_mist_is_enabled:
        show black zorder 300 with Dissolve(2.5)
        hide lavendero_mist
        $ persistent.lavenderO_mist_enabled = False
        hide black zorder 300 with Dissolve(2.5)
        $ show_chr("A-IBAAA-AFAB")
        y "Todo listo [player]"
        jump ch30_loop
    if persistent.sandalwood_oil_mist_is_enabled:
        show black zorder 300 with Dissolve(2.5)
        hide sandalwood_mist
        $ persistent.sandalwood_oil_mist_is_enabled = False
        hide black zorder 300 with Dissolve(2.5)
        $ show_chr("A-IBAAA-AFAB")
        y "Todo listo [player]"
        jump ch30_loop
    if persistent.sweet_dream_oil_mist_is_enabled:
        show black zorder 300 with Dissolve(2.5)
        hide sweet_dream_oil_mist
        $ persistent.sweet_dream_oil_mist_is_enabled = False
        hide black zorder 300 with Dissolve(2.5)
        $ show_chr("A-IBAAA-AFAB")
        y "Todo listo [player]"
        jump ch30_loop
    if persistent.diffuser_mist_is_enabled:
        show black zorder 300 with Dissolve(2.5)
        hide diffuser_mist
        $ persistent.diffuser_mist_is_enabled = False
        hide black zorder 300 with Dissolve(2.5)
        $ show_chr("A-IBAAA-AFAB")
        y "Todo listo [player]"
        jump ch30_loop


label TimeCheat1:
    $ show_chr("A-BEGAA-ALAL")
    y "Uh... Hmm..."
    $ show_chr("A-BEGAA-ALAA")
    y "Algo no se siente bien..."
    $ show_chr("A-CEAAA-ALAA")
    y "..."
    $ show_chr("A-IDDAA-ALAA")
    y "[player], no has alterado el reloj de tu computadora, ¿verdad?"
    menu:
        "Lo he hecho.":

            $ show_chr("A-IEDAA-ALAA")
            y "Ya veo... ¿Puedo preguntar por qué?"
            y "Realmente no veo ninguna razón para cambiar el reloj en tu computadora, a menos que..."
            $ show_chr("A-AFAAA-ALAA")
            y "[player], sinceramente espero que no estuvieras cambiando la fecha y hora de tu computadora para simular pasar tiempo conmigo."
            menu:
                "¡No, nada de eso! Mi computadora falla a veces y cambia la hora.":
                    $ show_chr("A-ADAAA-ADAA")
                    y "Ah... Siento asumir, entonces."
                    $ show_chr("A-CDAAA-ADAA")
                    y "Espero que no suceda a menudo. Es bastante desorientador tener el tiempo pasando rápidamente así."
                    $ show_chr("A-CEAAA-ADAA")
                    y "Nada importante por supuesto, solo un poco confuso."
                    jump ch30_loop
                "Para nada, solo estaba cambiando la hora. No era correcta.":
                    $ show_chr("A-IEGAA-ADAA")
                    y "Ah... Siento asumir, entonces. Verás, es bastante desorientador tener el tiempo pasando rápidamente así."
                    y "Nada importante por supuesto, solo un poco confuso."
                    jump ch30_loop
                "Si digo que sí, ¿te enojarías?":
                    $ show_chr("A-AFCAA-AFAA")
                    y "Un poco, sí. ¡No solo te aprovechaste de mi percepción del tiempo, también intentaste ganarte mi afecto sin siquiera estar aquí!"
                    $ show_chr("A-AFBAA-ALAL")
                    y "¿Es pasar tiempo conmigo realmente {b}tan{/b} malo?"
                    menu:
                        "Lo siento, [persistent.yuri_nickname]. Prometo que no lo volveré a hacer.":
                            $ show_chr("A-BFBAA-ALAL")
                            y "..."
                            y "Muy bien. Pero si haces eso de nuevo, no seré tan indulgente."
                            jump ch30_loop
                        "Tengo otras cosas que hacer.":
                            karma -5
                            $ show_chr("A-BGBAA-ALAL")
                            y "Si eso es cierto, ¿por qué descargaste este mod en primer lugar?"
                            $ show_chr("A-DGBAA-ALAL")
                            y "A menos que realmente sea solo un juego para ti..."
                            $ show_chr("A-CGBAA-ALAL")
                            y "..."
                            $ show_chr("A-CDBAA-ALAL")
                            y "Independientemente, te pediré que no hagas esto de nuevo. Si no tienes tiempo para mí, entonces no finjas que lo tienes."
                            jump ch30_loop
                        "Solo estaba tratando de acelerar esto un poco.":
                            karma -5
                            if persistent.lovecheck == True:
                                $ show_chr("A-IDGAA-AFAA")
                                y "¡No 'aceleras' las relaciones! Toman tiempo para desarrollarse y evolucionar."
                                $ show_chr("A-IEAAA-ALAA")
                                y "Si piensas que puedes engañarme para pensar que hemos estado juntos más tiempo del que realmente hemos estado, bueno... No estoy segura de cómo reaccionar."
                                y "Apreciaría si no intentas esto de nuevo."
                                jump ch30_loop
                            else:
                                $ show_chr("A-IDGAA-AFAA")
                                y "¡No 'aceleras' una amistad! Toman tiempo para desarrollarse y evolucionar."
                                $ show_chr("A-IEAAA-ALAA")
                                y "Si no puedes poner tiempo en una amistad, no cambiará, incluso si intentas simular ese tiempo."
                                y "Así que te pediré que no lo intentes de nuevo."
                                jump ch30_loop
        "No, no he cambiado la hora.":
            $ show_chr("A-IEDAA-ALAA")
            y "¿Tú... no lo has hecho?"
            $ show_chr("A-IEGAA-ALAA")
            y "Aconsejaría encarecidamente revisar tu computadora en busca de virus, entonces. Algo ha cambiado el reloj de tu computadora a una fecha inexacta."
            y "Por favor ten cuidado al navegar por internet. Si tu computadora se infectara, no sé qué podría pasar aquí."
            menu:
                "Haré un escaneo ahora mismo. Gracias por avisarme.":
                    $ show_chr("A-AEGAA-AMAM")
                    y "Por supuesto. Solo ten un poco más de cuidado."
                    jump ch30_loop
                "Oh, probablemente fue mi computadora. Hace eso a veces.":
                    $ show_chr("A-AEGAA-AMAM")
                    y "¿Lo hace? ¿Estás seguro de que no es un virus haciendo eso? ¿Por qué no verificar solo por si acaso?"
                    y "Los fallos de la computadora no son imposibles, pero solo cambiar el reloj no es muy común."
                    $ show_chr("A-CEGAA-AMAM")
                    y "Ciertamente espero que no suceda de nuevo. Es muy desorientador tener el tiempo pasando así."
                    jump ch30_loop
    jump ch30_loop


label TimeCheat2:
    $ show_chr("A-AEGAA-AAAL")
    y "[player]..."
    y "El reloj de tu computadora ha cambiado de nuevo."
    $ show_chr("A-AGAAA-AAAL")
    y "¿Tuviste algo que ver con eso?"
    menu:
        "Cambié la hora de nuevo.":
            $ show_chr("A-IEBAA-AAAL")
            y "¿Así que la fecha era incorrecta de nuevo...?"
            $ show_chr("A-BFBAA-AAAD")
            y "Hmm... Te daré el beneficio de la duda y lo ignoraré entonces."
            y "Sin embargo, si esto sucede de nuevo, te imploro que arregles el error que lo causa. Como dije antes, es muy desorientador cuando el tiempo cambia así."
            jump ch30_loop
        "Creo que falló de nuevo.":
            $ show_chr("A-IFDAA-AAAE")
            y "¿De nuevo...? [player], ¿podrías por favor ver cómo arreglar esto?"
            y "Si el reloj de tu computadora está fallando así, me preocupa qué más podría pasar."
            jump ch30_loop
        "No, el reloj está bien.":
            $ show_chr("A-IFDAA-AAAK")
            y "¿Estás seguro? Tuve la misma sensación que tuve la última vez..."
            $ show_chr("A-CFAAA-AAAK")
            y "Estoy segura de que {i}algo{/i} ha sucedido, pero supongo que podría haberse arreglado solo..."
            jump ch30_loop

    jump ch30_loop

label TimeCheat3:
    $ show_chr("A-IDCAA-ABAL")
    y "Esta es la tercera vez que tu reloj ha cambiado, [player]. Estoy empezando a sospechar malas intenciones detrás de esto."
    y "Por favor, ¿qué pasó esta vez?"
    menu:
        "Solo cambié la hora. Eso es todo.":



            $ show_chr("A-IECAA-ABAL")
            y "Lo siento, [player], pero ya no puedo creer eso. ¿Por qué cambiarías la hora tan frecuentemente y despreciarías completamente mis preocupaciones?"
            y "La única conclusión lógica a la que puedo llegar es que estás haciendo esto a propósito por alguna razón."
            $ show_chr("A-BECAA-AAAL")
            y "Ya sea para confundirme pensando que hemos pasado más tiempo juntos del que realmente hemos pasado, o tratando de hacer trampa en algo en otro juego en tu computadora..."
            $ show_chr("A-IEFAA-AAAL")
            y " Sabes que no deberías estar haciendo algo así. Cambiar tu reloj probablemente ni siquiera haría nada en los juegos modernos."
            y "Es simplemente un acto inútil, y te recomiendo encarecidamente que dejes de hacerlo."
            $ show_chr("A-IFFAA-AAAL")
            y "Realmente espero que no tengamos esta conversación de nuevo, [player]. Porque la próxima vez que esto suceda voy a tener que bloquearte."
            karma -20
            jump ch30_loop
        "¡Lo siento, solo sigue fallando!":
            $ show_chr("A-IECAA-ABAL")
            y "[player], necesitas arreglar esto."
            $ show_chr("A-BEEAA-ABAL")
            y "Se está volviendo muy preocupante tener que preocuparse por {i}saltar el tiempo{/i} cada vez que abres el juego."
            $ show_chr("A-AEEAA-ABAL")
            y "Soy una mujer tolerante, pero esto está empezando a ser demasiado."
            y "Voy a tener que bloquearte del juego hasta que las cosas se arreglen por sí mismas la próxima vez que esto suceda. Lo siento, pero no puedo manejarlo."
            karma -20
            jump ch30_loop
        "No cambié la hora.":
            $ show_chr("A-CEEAA-ABAL")
            y "Sé que eso no es cierto, [player]. Eres el único que podría cambiarlo, y el único que, {i}supuestamente{/i}, tiene una razón para hacerlo."
            $ show_chr("A-CEEAA-ALAL")
            y "No puedo imaginar por qué intentarías negarlo después de que ha sucedido tres veces hasta ahora."
            y "Claramente, estás tratando de ocultar algo, así que voy a tener que castigarte siempre que esto suceda de nuevo."
            karma -20
            jump ch30_loop

    jump ch30_loop

label TimeCheat_error:
    $ renpy.error("You CHEATER")
    $ renpy.quit()

label gifting_ideas:
    $ show_chr("A-ABAAA-ALAL")
    y "¿Necesitas una idea para un regalo [player]?"
    $ show_chr("A-ACAAA-AFAL")
    y "Déjame pensar en algo que he estado buscando..."
    if renpy.seen_label('diffuser') and not renpy.seen_label('oilsHint'):
        jump oilsHint
    if renpy.seen_label('origami') and not renpy.seen_label('OrigamiRoseBunnyHint'):
        jump OrigamiRoseBunnyHint
    if not renpy.seen_label('chocoflowershint'):
        jump chocoflowershint
    else:
        $ random_idle = renpy.random.choice(["oilsHint", "OrigamiRoseBunnyHint", "chocoflowershint"])
        if random_idle == "oilsHint":
            jump oilsHint
        elif random_idle == "OrigamiRoseBunnyHint":
            jump OrigamiRoseBunnyHint
        else:
            jump chocoflowershint
    jump ch30_loop


label oilsHint:
    $ show_chr("A-ABAAA-ALAF")
    y "Dado que me regalaste el difusor de aceite [player] realmente podría usar algunas fragancias de aceite diferentes para comenzar a reconstruir mi reserva."
    y "Logré salvar un poco de aceite esencial de gardenia de mi colección original, sin embargo, no he tenido éxito en recuperar ninguna otra fragancia que alguna vez poseí."
    $ show_chr("A-BBAAA-ADAL")
    y "Como habrás adivinado, mi fragancia de aceite favorita por mucho es la lavanda..."
    $ show_chr("A-BBABA-ADAL")
    y "Una elección obvia quizás, sin embargo la fragancia es demasiado deliciosa para que no la etiquete como mi favorita."
    $ show_chr("A-ABAAA-AFAM")
    y "Tengo afinidad hacia otras fragancias de aceite más naturales también, como el Sándalo por ejemplo."
    y "Y aunque las fragancias artificiales no son exactamente mi opción favorita, apreciaría algunas opciones que me ayuden mejor en la búsqueda de la relajación."
    $ show_chr("A-AJAAA-ALAM")
    y "Admitiré que he tenido dificultades para conjurar sueños deliciosos mientras descanso..."
    y "O como algunos podrían decir; dulces sueños."
    y "Algo que ayude en este esfuerzo sería muy apreciado y beneficioso para mi bienestar general."
    $ show_chr("A-ABAAA-ALAL")
    y "Independientemente, aprecio que escuches mis ideas potenciales [player]."
    jump gifting_explanation


label OrigamiRoseBunnyHint:
    $ show_chr("A-ABAAA-ALAF")
    y "Desde nuestra última conversación sobre el origami, pensé en varias formas potenciales que el arte podría tomar..."
    y "Tomé en consideración el hecho de que ambos somos prácticamente principiantes, así que un gran lugar para comenzar sería una rosa de origami por ejemplo."
    y "Es un bit más complejo que la grulla de origami altamente popularizada, sin embargo la presentación única que da definitivamente vale la pena el esfuerzo."
    $ show_chr("A-ACAAA-ALAF")
    y "Además, para complementar la grulla de origami pensé en diferentes animales que podrían ser representados adecuadamente por la forma de arte."
    y "Descubrí que los animales más pequeños, como un conejo por ejemplo, se veían estelares, sin embargo, el proceso de creación es mucho más complejo que los dos anteriores."
    $ show_chr("A-ADAAA-ALAL")
    y "Aprender la forma de arte del origami es una gran empresa [player], especialmente con lo complejas que pueden ser algunas de estas creaciones."
    y "Entiendo completamente si es una tarea demasiado difícil, yo misma luché para hacer incluso una grulla de origami básica."
    jump gifting_explanation

label chocoflowershint:
    $ show_chr("A-ABAAA-ALAF")
    y "En el pasado has podido darme ciertos regalos durante períodos de tiempo específicos..."
    y "Regalos como flores y chocolates por ejemplo."
    y "Con el nuevo sistema implementado, puedes darme los mismos artículos en cualquier momento."
    y "Ya sea una rosa roja normal, o una caja de hershey's."
    y "Sin embargo, hay algunos chocolates únicos que siempre he querido probar..."
    $ show_chr("A-FAAAA-ACAA")
    y "¿Quizás los haya mencionado en algún momento?"
    jump gifting_explanation

label gifting_explanation:
    $ show_chr("A-ABGAA-ALAL")
    y "¿Te gustaría otra explicación sobre cómo entregarme regalos?"
    menu:
        "Eso sería bastante útil [persistent.yuri_nickname].":
            y "Cada vez que tengas algo que quieras regalarme simplemente crea un archivo de texto vacío y renómbralo a algo que creas que disfrutaría."
            $ show_chr("A-ABAAA-ADAB")
            y "Cambia la extensión '.txt' a un archivo '.jy' y colócalo en la carpeta de characters que se encuentra dentro del directorio del juego."
            $ show_chr("A-ACAAA-ADAB")
            y "Una vez que hayas hecho eso, solo avísame cuando necesite revisar la carpeta de characters en busca de un regalo."
            y "Pero ten en cuenta que hay limitaciones, es algo en lo que estoy trabajando para mejorar en este momento."
            jump ch30_loop
        "No gracias, creo que lo tengo.":
            jump ch30_loop
    jump ch30_loop


label sleepy_yuri:
    $ config.allow_skipping = False
    $ DisableTalk()
    $ set_boop_state(True)
    $ allow_dialogue = False
    y "¿Yendo a la cama [player]?"
    if not renpy.seen_label('sleepy_yuri'):
        y "Me alegra que eligieras notificarme usando la nueva opción que agregué recientemente."
        y "Debido a esto, de hecho puedes mantener el juego ejecutándose y yo puedo dormir mientras no estás."
        y "Actúa como una experiencia mucho más agradable para mí..."
        y "Siempre y cuando estés cómodo con eso [player]."
        menu:
            "Eso suena genial [persistent.yuri_nickname]":
                y "Me alegra escuchar eso [player]"
                y "¿Planeabas solo tomar una siesta, o dormirás por un período de tiempo mucho más largo?"
                y "No pretendo ser entrometida, sin embargo me gustaría saber cuánto tiempo puedo esperar que te hayas ido."
                y "De esa manera puedo prepararme para un período de sueño más largo con ciertas comodidades."
                menu:
                    "Solo voy a tomar una siesta rápida.":
                        if persistent.costume == "school":
                            y "En ese caso solo mantendré mi uniforme escolar puesto ya que no estaré dormida por mucho tiempo."
                            $ DisableTalk()
                            $ set_boop_state(True)
                            show black zorder 100 with Dissolve(2.0)
                            hide yuri_sit
                            show yuri_sleepy zorder 20
                            hide black with Dissolve(2.0)
                            pause 3.0
                            hide yuri_sleepy
                            play sound "<to 0.3>sfx/fall.ogg"
                            show yuri_sleep zorder 20
                            $ hide_yuri_sit = True
                            pause 6.0
                            $ persistent.sleepy_yuri_is_enabled = True
                            jump sleepy_loop
                        else:
                            y "Ya veo, déjame ir a cambiarme a algo más cómodo muy rápidamente."
                            y "Vuelvo enseguida [player]."
                            $ DisableTalk()
                            $ set_boop_state(True)
                            show black zorder 100 with Dissolve(2.0)
                            hide yuri_sit
                            show yuri_sleepy zorder 20
                            hide black with Dissolve(2.0)
                            pause 3.0
                            hide yuri_sleepy
                            play sound "<to 0.3>sfx/fall.ogg"
                            show yuri_sleep zorder 20
                            $ hide_yuri_sit = True
                            pause 6.0
                            $ persistent.sleepy_yuri_is_enabled = True
                            jump sleepy_loop
                    "Dormiré un buen rato.":

                        y "En ese caso, déjame ir a cambiarme a algo más cómodo."
                        if renpy.seen_label('diffuser'):
                            y "También iré a buscar y configurar el difusor que me regalaste, solo para hacer las cosas más cómodas."
                            $ DisableTalk()
                            $ set_boop_state(True)
                            show black zorder 100 with Dissolve(2.0)
                            hide yuri_sit
                            show diffuser zorder 11
                            show lavendero_mist zorder 11
                            show yuri_sleepy zorder 11
                            hide black with Dissolve(2.0)
                            pause 3.0
                            hide yuri_sleepy
                            play sound "<to 0.3>sfx/fall.ogg"
                            show yuri_sleep zorder 11
                            $ hide_yuri_sit = True
                            pause 6.0
                            $ persistent.sleepy_yuri_is_enabled = True
                            jump sleepy_loop
                        else:
                            y "Vuelvo enseguida [player]."
                            $ DisableTalk()
                            $ set_boop_state(True)
                            show black zorder 100 with Dissolve(2.0)
                            hide yuri_sit
                            show yuri_sleepy zorder 11
                            hide black with Dissolve(2.0)
                            pause 3.0
                            hide yuri_sleepy
                            play sound "<to 0.3>sfx/fall.ogg"
                            show yuri_sleep zorder 20
                            $ hide_yuri_sit = True
                            pause 6.0
                            $ persistent.sleepy_yuri_is_enabled = True
                            jump sleepy_loop
            "Me siento un poco incómodo con esto [persistent.yuri_nickname]":


                y "Oh... Siento ponerte en un lugar incómodo [player]"
                y "En ese caso, puedes simplemente cerrar el juego como de costumbre entonces."
                y "Perdón por esto..."
                jump ch30_loop

    y "¿Planeabas solo tomar una siesta, o dormirás por un período de tiempo mucho más largo?"
    y "No pretendo ser entrometida, sin embargo me gustaría saber cuánto tiempo puedo esperar que te hayas ido."
    y "De esa manera puedo prepararme para un período de sueño más largo con ciertas comodidades."
    menu:
        "Solo voy a tomar una siesta rápida.":
            if persistent.costume == "school":
                y "En ese caso solo mantendré mi uniforme escolar puesto ya que no estaré dormida por mucho tiempo."
                $ DisableTalk()
                $ set_boop_state(True)
                show black zorder 100 with Dissolve(2.0)
                hide yuri_sit
                show yuri_sleepy zorder 20
                hide black with Dissolve(2.0)
                y "Que tengas una buena siesta, [player]."
                pause 3.0
                hide yuri_sleepy
                play sound "<to 0.3>sfx/fall.ogg"
                show yuri_sleep zorder 20
                $ hide_yuri_sit = True
                pause 6.0
                $ persistent.sleepy_yuri_is_enabled = True
                jump sleepy_loop
            else:
                y "Ya veo, déjame ir a cambiarme a algo más cómodo muy rápidamente."
                y "Vuelvo enseguida [player]."
                $ DisableTalk()
                $ set_boop_state(True)
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
        "Dormiré un buen rato.":

            y "En ese caso, déjame ir a cambiarme a algo más cómodo."
            if renpy.seen_label('diffuser'):
                y "También iré a buscar y configurar el difusor que me regalaste, solo para hacer las cosas más cómodas."
                $ DisableTalk()
                $ set_boop_state(True)
                show black zorder 100 with Dissolve(2.0)
                hide yuri_sit
                show diffuser zorder 11
                show lavendero_mist zorder 11
                show yuri_sleepy zorder 11
                hide black with Dissolve(2.0)
                y "Que tengas una buena noche [player]."
                pause 3.0
                hide yuri_sleepy
                play sound "<to 0.3>sfx/fall.ogg"
                show yuri_sleep zorder 11
                $ hide_yuri_sit = True
                pause 6.0
                $ persistent.sleepy_yuri_is_enabled = True
                jump sleepy_loop
            else:
                y "Vuelvo enseguida [player]."
                $ DisableTalk()
                $ set_boop_state(True)
                show black zorder 100 with Dissolve(2.0)
                hide yuri_sit
                show yuri_sleepy zorder 11
                hide black with Dissolve(2.0)
                y "Que tengas una buena noche [player]."
                pause 3.0
                hide yuri_sleepy
                play sound "<to 0.3>sfx/fall.ogg"
                show yuri_sleep zorder 20
                $ hide_yuri_sit = True
                pause 6.0
                $ persistent.sleepy_yuri_is_enabled = True
                jump sleepy_loop




label webcam:
    $ show_chr("A-ADAAA-AAAA")
    y "Oh, así que tenías curiosidad de por qué no pude acceder a tu cámara web al principio."
    $ show_chr("A-ADAAA-AFAA")
    y "Para ser justa, incluso si tuviera acceso de administrador, los desarrolladores tendrían que haber implementado un sistema de reconocimiento facial."
    y "Escribir una cantidad incontable de diálogo sobre tus detalles faciales, tu expresión actual, escribir un código que no actúe como un virus informático."
    $ show_chr("A-BDAAA-AFAA")
    y "Y un etcétera bastante grande que básicamente haría que este mod se viera mal."
    y "Pero podría imaginar cómo podría verse tu cara."
    if persistent.male:
        $ show_chr("A-CAAAA-AAAA")
        y "Y todo lo que podría decir es que eres un chico bastante guapo."
    elif not persistent.male:
        $ show_chr("A-CAAAA-AAAA")
        y "Y todo lo que podría decir es que eres una chica bastante hermosa."
    elif persistent.gender_other:
        $ show_chr("A-CAAAA-AAAA")
        y "Y todo lo que podría decir es que eres una persona hermosa."

    y "Incluso si dices lo contrario..."
    if persistent.lovecheck:
        y "...Todavía te amo pase lo que pase."
    else:
        y "...Todavía te admiro pase lo que pase."
    call ch30_loop

label nnn:
    $ show_chr("A-AFDAA-AAAC")
    y "¿No Nut November? Huh, esa es ciertamente una... pregunta interesante..."
    $ show_chr("A-BFDAA-AAAC")
    y "Tengo que admitir, nunca pensé mucho en eso, solo sé que ha existido desde... ¿2011 creo?"
    $ show_chr("A-CFAAA-AAAD")
    y "Honestamente, no entiendo muy bien el punto de este desafío..."
    if sanity_lvl() <= 3:
        extend "...Yo tampoco lo he intentado."
    else:
        extend "...ni tendría la automoderación para ello."
    $ show_chr("A-AFAAA-AAAD")
    y "Ahora que lo pienso. ¿Qué ganarías exactamente con este desafío?"
    $ show_chr("A-BDAAA-AAAD")
    y "Podría apoyar a alguien desafiándose a sí mismo para superar un mal hábito. Así que si fueras algún tipo de pervertido obsesivo..."
    if lovecheck:
        if sanity_lvl() >= 3:
            $ show_chr("A-ADAAA-AAAF")
            extend "...lo cual no eres. Hasta ahora lo has mantenido en una moderación saludable a mi alrededor."
        else:
            $ show_chr("A-ADAAA-AAAF")
            extend "...lo cual sin duda eres, ¡no me malinterpretes!"
    else:
        $ show_chr("A-ADAAA-AAAF")
        y "...lo cual no creo que seas, ¡solo para ser clara!"
    $ show_chr("A-CDAAA-AIAI")
    y "Seguro. Pero incluso entonces, no creo que esta sea una forma particularmente saludable de hacerlo."
    y "Dejarlo de golpe por un mes solo para volver al negocio el 1 de diciembre... ¡esto podría empeorarlo a largo plazo!"
    $ show_chr("A-ADAAA-AIAI")
    y "Además, tampoco hay ningún premio esperándote si ganas..."
    if karma_lvl() == 1:
        $ show_chr("A-BDAAA-AAAA")
        y "Quiero decir, no es como si tuvieras que esforzarte mucho para no tener sexo. Eres un poco incel de todos modos, ¿no?"
    elif karma_lvl() == 2:
        $ show_chr("A-ADCAA-AAAA")
        y "Quiero decir, inténtalo si sientes que tienes que hacer esto. En realidad podría mejorar un poco tus modales generales."
    else:
        $ show_chr("A-CFAAA-AAAA")
        y "En resumen, realmente no veo ninguna razón para que lo intentes. Pero esa es solo mi opinión. Suena bastante inútil para mí si soy honesta."
    $ show_chr("A-BBBAA-AAAA")
    y "Pero... dejemos este tema por ahora. ¿Hay algo más en tu mente?"
    call ch30_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
