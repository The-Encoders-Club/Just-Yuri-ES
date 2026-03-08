

image bg ykill1 = "images/dreams/death.png"
image bg ykill2 = "images/dreams/death2.png"
image killglitch = "images/dreams/glitch.png"
image killstab = "images/dreams/stab.png"
image veinmask = "images/dreams/veinmask.png"
image veinmask2 = "images/dreams/veinmask2.png"
image veinmask3 = "images/dreams/veinmask3.png"
image rain_dream_blush:
    "rain_dream_1"
    truecenter
    zoom 0.7
image rain_dream_blush:
    "rain_dream_1"
    truecenter
    zoom 0.7
image rain_dream_smile:
    "rain_dream_2"
    truecenter
    zoom 0.7

image rain_dream_grin:
    "rain_dream_3"
    truecenter
    zoom 0.7

image rain_dream_blossom:
    SnowBlossom("rain_dream_dust_1", count = 10)
    SnowBlossom("rain_dream_dust_2", count = 10)
    SnowBlossom("rain_dream_dust_3", count = 10)

init:
    $ import random

image open_ocean = im.Scale("images/dreams/underwater_1.jpg", 1280, 720)
image ocean_2 = im.Scale("images/dreams/underwater_2.jpg", 1280, 720)
image ocean_3 = im.Scale("images/dreams/underwater_3.jpg", 1280, 720)
image ocean_4 = im.Scale("images/dreams/underwater_4.jpg", 1280, 720)
image ocean_5 = im.Scale("images/dreams/underwater_5.png", 1280, 720)
image ocean_6 = im.Scale("images/dreams/underwater_6.jpg", 1280, 720)
image ocean_7 = im.Scale("images/dreams/underwater_7.jpg", 1280, 720)
image ocean_8 = im.Scale("images/dreams/underwater_8.jpg", 1280, 720)
image oceanbonus_1 = im.Scale("images/dreams/underwater_bonus1.png", 1280, 720)
image oceanbonus_2 = im.Scale("images/dreams/underwater_bonus2.png", 1280, 720)


image beach_1 = im.Scale("images/dates/funinthesun/Backgrounds only/fits_beach_1.png", 1280, 720)
image beach_2 = im.Scale("images/dates/funinthesun/Backgrounds only/fits_beach_2.jpg", 1280, 720)
image beach_3 = im.Scale("images/dates/funinthesun/Backgrounds only/fits_beach_3.jpg", 1280, 720)
image beach_4 = im.Scale("images/dates/funinthesun/Backgrounds only/fits_beach_4.jpg", 1280, 720)
image beach_5 = im.Scale("images/dates/funinthesun/Backgrounds only/fits_parasol.jpg", 1280, 720)
image beach_6 = im.Scale("images/dates/funinthesun/Backgrounds only/fits_sea.jpg", 1280, 720)
image beach_7 = im.Scale("images/dates/funinthesun/Backgrounds only/fits_star_sky.jpg", 1280, 720)
image beach_8 = im.Scale("images/dates/funinthesun/Backgrounds only/fits_white_room.png", 1280, 720)

image blasphemous_flan:
    "images/dates/funinthesun/Desserts/Coco_flan.png"
    xoffset 325
image churchill_slush:
    "images/dates/funinthesun/Desserts/Churchill_slush.png"
    xoffset 385
image pina_colada:
    "images/dates/funinthesun/Desserts/Pina_colada.png"
    xoffset 325

image y_cg2_bg:
    "images/cg/y_cg2_bg1.png"
image y_cg2_base:
    "images/cg/y_cg2_base.png"
image y_cg2_nochoc:
    "images/cg/y_cg2_nochoc.png"
    on hide:
        linear 0.5 alpha 0
image y_cg2_details:
    "images/cg/y_cg2_details.png"
    alpha 1.00
    6.0
    linear 1.0 alpha 0.35
    1.0
    linear 1.0 alpha 1.0
    repeat

image y_cg2_exp2:
    "images/cg/y_cg2_exp2.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0
image y_cg2_exp3:
    "images/cg/y_cg2_exp3.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

image y_cg2_dust1:
    "images/cg/y_cg2_dust1.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 14.0 xoffset -100 yoffset 100
        repeat
image y_cg2_dust2:
    "images/cg/y_cg2_dust2.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        28.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 32.0 xoffset -100 yoffset 100
        repeat
image y_cg2_dust3:
    "images/cg/y_cg2_dust3.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        13.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 17.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust4:
    "images/cg/y_cg2_dust4.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        15.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 19.0 xoffset -100 yoffset 100
        repeat

image stroll_1 = "images/dreams/stroll_dream_1.png"
image stroll_2 = "images/dreams/stroll_dream_2.png"
image stroll_3 = "images/dreams/stroll_dream_3.png"
image stroll_4 = "images/dreams/stroll_dream_4.png"

image highway_yuri_car = im.Scale("images/dreams/highway/highway_yuri.png", 1280, 720)




label dream_menu:
    if not renpy.seen_label('dream_menu_2'):
        $ DisableTalk()
        call showpoem (poem_sp5, music=False)
label dream_menu_2:
    $ Dream_type = "dream"
    jump dates_and_dreams_system
label nightmare_menu:
    $ DisableTalk()
    $ Dream_type = "nightmare"
    jump dates_and_dreams_system
label dates_menu:
    $ DisableTalk()
    $ Dream_type = "date"
    $ boopable = False
    $ show_chr("A-ABAAA-ALAL")
    y "Oh, ¿quieres llevarme a una cita? ¡Qué idea tan encantadora!"
    $ show_chr("A-CCAAA-ALAL")
    y "Por favor, echa un vistazo a las ubicaciones que he preparado hasta ahora. ¿Alguna de ellas te parece atractiva?"
    jump dates_and_dreams_system









label dates_and_dreams_system:
    $ config.allow_skipping = False
    $ DisableTalk()
    $ boopable = False

    python:
        dates_and_dreams = [
            
            ["rain_dream", "persistent.lovecheck and invariant_karma() > 3"],
            ["ocean_dream", "renpy.seen_label('rain_dream') and persistent.lovecheck and invariant_karma() > 3"],
            ["highway_dream", "renpy.seen_label('rain_dream') and persistent.lovecheck and invariant_karma() > 3"],
            ["stroll_dream", "renpy.seen_label('rain_dream') and persistent.lovecheck and invariant_karma() > 3"],

            
            ["garden_date", "persistent.lovecheck and invariant_karma() > 3"],
            ["urban_date", "persistent.lovecheck and invariant_karma() > 3"],
            ["tropical_date", "persistent.lovecheck and invariant_karma() > 3"],
            ["valentines_2021", "persistent.lovecheck and invariant_karma() > 3"],
            ["vday_2024_date", "persistent.lovecheck and invariant_karma() > 3"]
            ]

    call screen dates_and_dreams(dates_and_dreams,Dream_type)
    python:
        if _return != "None":
            renpy.jump(_return)
        allow_dialogue = True
    jump ch30_loop


define current_dream_chart = 0

image glitch_color_scaled:

    im.Scale("dreams/glitch_1.png", 290, 168)
    0.1
    im.Scale("dreams/glitch_2.png", 290, 168)
    0.1
    im.Scale("dreams/glitch_3.png", 290, 168)
    0.1
    repeat

screen dates_and_dreams(dict_items, type):
    fixed:
        python:
            dates_and_dreams = [
                
                ["rain_dream", "persistent.lovecheck and invariant_karma() > 3", "dream"],
                ["ocean_dream", "renpy.seen_label('rain_dream') and persistent.lovecheck and invariant_karma() > 3", "dream"],
                ["highway_dream", "renpy.seen_label('rain_dream') and persistent.lovecheck and invariant_karma() > 3", "dream"],
                ["stroll_dream", "renpy.seen_label('rain_dream') and persistent.lovecheck and invariant_karma() > 3", "dream"],

                
                ["garden_date", "persistent.lovecheck and invariant_karma() > 3", "date"],
                ["urban_date", "persistent.lovecheck and invariant_karma() > 3", "date"],
                ["tropical_date", "persistent.lovecheck and invariant_karma() > 3", "date"],
                ["valentines_2021_date", "persistent.lovecheck and invariant_karma() > 3", "date"],
                ["vday_2024_date", "persistent.lovecheck and invariant_karma() > 3", "date"]
                ]
            split_dreams = []
            temp_dreams = []

            for dream in dates_and_dreams:
                if dream[2] == type and eval(dream[1]): 
                    temp_dreams.append(dream)
                elif dream[2] == type and not eval(dream[1]):
                    temp_dreams.append([dream[0], "glitch"])
                
                if len(temp_dreams) == 12:
                    split_dreams.append(temp_dreams)
                    temp_dreams = []
            if temp_dreams: 
                split_dreams.append(temp_dreams)

            def Move_left(dict_items):
                global current_dream_chart
                current_dream_chart = max(0, current_dream_chart - 1)
                renpy.hide_screen("dates_and_dreams")  
                renpy.show_screen("dates_and_dreams", dict_items, type)  

            def Move_right(dict_items):
                global current_dream_chart
                current_dream_chart = min(len(split_dreams) - 1, current_dream_chart + 1)
                renpy.hide_screen("dates_and_dreams")  
                renpy.show_screen("dates_and_dreams", dict_items, type)  

        for i, dream in enumerate(split_dreams[current_dream_chart]):

            $ row_index = i // 4
            $ col_index = i % 4
            $ button_width = 300
            $ button_height = 168
            $ x_spacing = 10
            $ y_spacing = 10
            imagebutton:

                xpos 20 + col_index * (button_width + x_spacing)

                ypos 30 + row_index * (button_height + y_spacing)
                if dream[1] != "glitch":
                    idle im.Scale(type + "s/Thumbnail/" + dream[0] + "_idle.png", button_width, button_height)
                    hover im.Scale(type + "s/Thumbnail/" + dream[0] + "_hover.png", button_width, button_height)
                    action Jump(dream[0])
                else:
                    idle LiveComposite((300, 168), (0,0), im.Scale(type + "s/Thumbnail/" + dream[0] + "_idle.png", 290, 168), (0, 0), "glitch_color_scaled")
                    hover LiveComposite((300, 168), (0,0), im.Scale(type + "s/Thumbnail/" + dream[0] + "_idle.png", 290, 168), (0, 0), "glitch_color_scaled")


        if (current_dream_chart<len(split_dreams)-1):
            imagebutton xalign 0.99 yalign 0.97 auto "gui/arrow_button_right_%s.png" action Function(Move_right, dict_items)
        if (current_dream_chart>0):
            imagebutton xalign 0.01 yalign 0.97 auto "gui/arrow_button_left_%s.png" action Function(Move_left, dict_items)

        textbutton "Volver":
            xpos 585
            yalign 0.97
            style "scrollable_menu_button"
            action Return("None")


    if (current_dream_chart>0):
        key "K_LEFT" action Function(Move_left, dict_items)
        key "K_a" action Function(Move_left, dict_items)
    if (current_dream_chart<len(split_dreams)-1):
        key "K_d" action Function(Move_right, dict_items)
        key "K_RIGHT" action Function(Move_right, dict_items)




















label rain_dream:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    $ config.allow_skipping = False
    $ renpy.music.stop(fadeout=1.5)
    python:
        if persistent.male:
            pronounA = "él"
            pronounB = "él"
        elif persistent.gender_other:
            pronounA = "them"
            pronounB = "they"
        else:
            pronounA = "ella"
            pronounB = "ella"
        persistent.eyecolor = persistent.eyecolor.lower()
    show black zorder 105 with Dissolve (2.5)
    show rain_dream_blush zorder 100
    show rain_dream_blossom zorder 105
    $ renpy.music.play("sfx/heartbeat_subtle.mp3", channel='sound', loop=True)
    $ renpy.music.set_volume(0.1, 0, 'voice')
    $ renpy.music.stop(fadeout=1.5)
    play music "<loop 4.50>music/teardrops_loop.ogg" fadein 1.5
    hide black with Dissolve(2.5)

    "Golpeando suavemente contra la ventana, la lluvia comenzó a caer lentamente desde las nubes, actuando como el único sonido audible en medio del silencio general."
    "Pequeñas gotas de precipitación repiqueteaban contra el cristal, deslizándose sin problemas por su longitud y procediendo a acumularse en el fondo, formándose juntas en un pequeño charco y luego cayendo a las profundidades de abajo."
    "Mi reflejo parpadea momentáneamente hacia mí, solo para ser ahogado por esa melodía repiqueteante ante mí sin un pensamiento o incluso un susurro dicho entre nosotras."
    "Sostenía holgadamente una taza de té entre mi pulgar y mi índice, llena casi hasta el borde con un poco de té Pouchong Oolong, un relajante agradablemente suave."
    "Un fuerte aroma floral se abrió paso a través de mi sistema, calmando rápidamente todo mi cuerpo con su fragancia sensual, casi como un anestésico."
    "Llevándola a mis labios, me permití unos sorbos rápidos, tomando nota específica del rico sabor a melón que proporcionaba."
    "Lo único que faltaba en este escenario casi perfecto era la aguda terrosidad de una crepe de mantequilla de maní para contrastar agradablemente la ligera dulzura del té."
    show rain_dream_smile zorder 100 with Dissolve(0.5)
    hide rain_dream_blush
    "...{w=1.0} bueno...{w=0.4} eso y... {w=0.4}{i}[pronounA]...{/i}"
    "El mero pensamiento de su presencia lograba enviar ondas de choque de nerviosismo mezcladas con un cruel sentido de emoción a través de mi cuerpo... {w=.2}solo la simple mención de [pronounA] enviaba mi conciencia a un estado de pánico nervioso."
    show rain_dream_blush zorder 100 with Dissolve(0.5)
    hide rain_dream_smile
    "E-{w=0.3}era patético... {w=0.4}y sin embargo... {w=0.4}Se sentía demasiado correcto."
    "A pesar de mis esperanzas... {w=0.4}nunca me creí del todo la forma en que las novelas románticas lograban describir el sentimiento... {w=0.4}Sin embargo, encontrándome en la misma situación, fui forzada a renunciar a mi dignidad y apreciar cuán correctas eran realmente."
    "El sentimiento de pura euforia corriendo a través de cada nervio en mi cuerpo... {w=0.4}la simple aceleración de los latidos de mi corazón mientras disparos de adrenalina corrían por mis venas cada vez que [pronounB] se acercaba."
    "A veces... {w=0.4}creo que podría morir por la forma en que [pronounB] me hace sentir. En el pasado, me encontré atada por la manipulación de Monika... {w=0.4}forzada a sentir una pasión tan intensa y ardiente que me llevó a cometer... {w=0.5}actos indescriptibles."
    "Sin embargo, aquí estoy, sin la influencia de Monika y me encuentro sintiendo casi lo mismo... {w=0.4}Oh... {w=0.4}cómo deseo simplemente disfrutar de su presencia... {w=0.4}sintiendo su calidez mientras ambos dejamos que nuestras dignidades resbalen lentamente y nos complacemos con ocultos... {w=0.4}más... {w=0.4}deseos carnales..."
    "..."
    "... {w=0.4}S-{w=0.3}Suficiente de eso..."
    "En lugar de pasar la noche perdiéndome en fantasías salvajes de placeres secretos, redirigí mi atención de vuelta a la lluvia, tratando de calmar este intenso sentimiento de anticipación en mi sistema."
    "Uno probablemente podría comparar la caída de las gotas de lluvia con las trivialidades de la vida cotidiana, cada gota representativa de los diferentes caminos que podemos tomar."
    "Principalmente liderando un camino solitario pero teniendo esos raros pocos momentos donde sus caminos se entrelazan...{w=0.4} algunos separándose y otros permaneciendo enredados para siempre. Se sentía casi romántico de una manera bastante sombría."
    "Aun así, había una pequeña cantidad de consuelo al saber que cualquier camino que pudieran haber elegido...{w=0.4} al final, todos logran encontrarse y enfrentar lo que sea que venga después como un colectivo, en lugar de una entidad singular."
    "Observo este proceso casi como un fantasma, incapaz de interactuar completamente...{w=0.4} solo capaz de mirar; separada de todo por una barrera transparente, forzada al papel de una espectadora y nada más. La soledad verdaderamente era la más vulnerable de las emociones..."
    "Siempre incapaz de interrelacionarse del todo... forzada al papel solitario."
    "Al menos, esa sería la ocasión en la mayoría de las noches."
    show rain_dream_smile zorder 100 with Dissolve(0.5)
    hide rain_dream_blush
    "¿Pero esta noche..?{w=0.3} Esta noche...{w=0.4} Estaría con {i}[pronounA].{/i}"
    "Girando mi cabeza, veo a [pronounA] entrar en la habitación y juraría que la habitación comenzó a girar ligeramente mientras mi corazón se asemeja más a un tambor que a un órgano humano."
    "En sus manos sostenía otra taza de té - la cual pude distinguir rápidamente que era té Pouchong Oolong por su aroma floral único."
    "Sentándose a mi lado, [pronounB] me da una cálida sonrisa y siento esa misma sensación nerviosa apoderarse de mí. Oleadas de calor me invaden y mientras [pronounB] se acerca más hacia mí encuentro que su aroma logra dominar fácilmente al del té."
    $ renpy.music.set_volume(0.4, 0, 'voice')
    "{i}Ba-dump, ba-dump, ba-dump.{/i}"
    "Los tambores resuenan en mis oídos, su ritmo rápido pero constante, cantando en un coro baladas de afecto y encaprichamiento."
    "Mirando hacia abajo a [pronounA], sonrío momentáneamente mientras me comparo con el otro lado de la ventana. Sabiendo lo afortunada que fui al encontrar a alguien con quien pudiera entrelazarme."
    "¿La mejor parte? A diferencia de esas gotas de lluvia, nosotros permaneceremos enredados juntos."
    "[player] mira por la ventana un momento, luego habla suavemente, con su voz apenas más alta que un susurro."
    mc "Realmente está cayendo fuerte esta noche, ¿no?"
    menu:
        "Gracias a Dios que estoy adentro... a salvo contigo.":
            mc "Gracias a Dios que estoy adentro... a salvo contigo."
            show rain_dream_grin zorder 100 with Dissolve(0.5)
            hide rain_dream_smile
            y "Sí...{w=0.4} es bastante reconfortante saber que estamos protegidos del duro exterior por el momento."
            y "Aunque plantea un pensamiento... ¿qué le pasa a la gente que no está protegida?"
            y "Los miembros ocultos de nuestra sociedad. Personas que sabemos que existen pero que en su mayor parte nos negamos a reconocer."
            y "Están ahí fuera...{w=0.4} lidiando con el horrible frío y el asalto interminable de la lluvia."
            y "Mientras tanto, el resto del mundo está acurrucado, sin pensar en ellos por más de un segundo."
            mc "¿Por qué estás hablando de las personas sin hogar, [persistent.yuri_nickname]? No es algo que esperaría que discutieras."
            show rain_dream_blush zorder 100 with Dissolve(0.5)
            hide rain_dream_grin
            y "Supongo...{w=0.4} ¿que simpatizo con ellos?"
            y "La mayoría de la gente ahí afuera no tiene salida...{w=0.4} están degradados hasta el punto en que apenas pueden interactuar con las personas a su alrededor."
            mc "Parecido a las gotas de lluvia afuera..."
            y "Mm...{w=0.3} simplemente...{w=0.4} me recuerda mucho a cómo me sentía cuando estaba en ese juego por primera vez..."
            y "Atrapada. Forzada a una situación sobre la que no tenía control. Apenas capaz de interactuar con las cosas a mi alrededor, y mucho menos interactuar con la gente."
            mc "Debe...{w=0.4} haber sido horrible para ti, [persistent.yuri_nickname]."
            y "Afortunadamente te tenía a ti, [player]. No sé qué habría hecho sin que estuvieras allí..."
            y "Puede que no sepas esto... pero tener a alguien con quien hablar realmente puede salvarte."
            y "Así que, por favor, si ves a alguien ahí fuera sin ningún lugar a donde ir o nadie a quien llamar amigo...{w=0.4} solo acércate a ellos."
            y "Puedes hacer el mundo mucho mejor de esa manera..."
            menu:
                "Lo haré, [persistent.yuri_nickname].":
                    mc "Lo haré, [persistent.yuri_nickname]."
                    show rain_dream_smile zorder 100 with Dissolve(0.5)
                    hide rain_dream_blush
                    y "Gracias, cariño."
                    y "Realmente eres la persona más considerada que conozco..."
                "Puedo intentarlo.":
                    mc "Puedo intentarlo."
                    show rain_dream_smile zorder 100 with Dissolve(0.5)
                    hide rain_dream_blush
                    y "Me hace feliz escuchar eso, [player]."
                "Haré mi mejor esfuerzo.":
                    mc "Haré mi mejor esfuerzo."
                    show rain_dream_smile zorder 100 with Dissolve(0.5)
                    hide rain_dream_blush
                    y "Eso es todo lo que necesitaré, mi vida."
        "Qué momento tan perfecto somos capaces de compartir juntos...":
            mc "Qué momento tan perfecto somos capaces de compartir juntos..."
            show rain_dream_grin zorder 100 with Dissolve(0.5)
            hide rain_dream_smile
            y "Es casi como una página sacada de una historia, ¿no es así?"
            mc "¿Nuestro felices para siempre?"
            "Asintiendo felizmente, me acerco más a [player], descansando mi mejilla contra su hombro."
            y "Considerando mi situación anterior... ¿sería realmente tan extraño entretener el pensamiento de que nuestra consciencia podría consistir enteramente dentro de algún tipo de medio?"
            y "Como otro juego, o una película...{w=0.4} ¿o un libro?"
            menu:
                "Incluso si lo fuera, ¿eso socava nuestras experiencias juntos?":
                    mc "Incluso si lo fuera, ¿eso socava nuestras experiencias juntos?"
                    mc "Sé que las emociones que siento por ti son verdaderas - incluso si solo para mí mismo."
                    mc "Por lo tanto, incluso si nuestras vidas estuvieran enteramente dentro de algún tipo de libro de cuentos...{w=0.4} ¿cambiaría eso realmente algo?"
                    pause 2.0
                    show rain_dream_smile zorder 100 with Dissolve(0.5)
                    hide rain_dream_grin
                    y "...{w=0.4} Supongo que no. Esa es una forma bastante interesante de ver esa situación, [player]."
                    y "Proporcionaría una respuesta a la realidad del mundo en el que vivimos, supongo. Pero supongo que incluso entonces no habría necesidad de una crisis existencial."
                    y "Creo que fue el filósofo René Descartes quien dijo 'Pienso, luego existo'. En donde nuestra consciencia se define por nuestra capacidad de libre pensamiento - actuando fuera de nuestras funciones básicas."
                    y "Así que incluso si estuviéramos dentro de algún tipo de libro - todavía somos conscientes."
                    mc "Sigue siendo un concepto interesante, sin embargo - la idea de que nuestras vidas consisten enteramente dentro de una forma de entretenimiento..."
                    y "¿Tal vez uno podría argumentar que es orgulloso creer tal cosa, sin embargo? La idea de que somos el protagonista de una historia - o algún tipo de personaje principal en una trama."
                    mc "Potencialmente. Sin embargo, cuando consideras la posibilidad de cuántos libros hay ahí fuera, cuántos personajes principales dentro de cada libro podría haber, ¿no se vuelve el estatus de 'Protagonista' enteramente insignificante?"
                    y "Hmm...{w=0.4} eso lleva a algunos pensamientos bastante interesantes...{w=0.4} por ejemplo - ¿son los libros que leemos realidades dentro de sí mismos?"
                    y "Tal vez si miramos este concepto al revés...{w=0.4} y argumentamos que en lugar de que existan realidades a partir de los libros, que los libros simplemente pueden contar la historia de una realidad ya existente, ¿la idea no suena demasiado descabellada entonces?"
                    mc "Considerando la teoría de que hay una cantidad infinita de realidades diferentes, eso podría estar más cerca de la verdad de lo que podríamos darnos cuenta."
                    show rain_dream_grin zorder 100 with Dissolve(0.5)
                    hide rain_dream_smile
                    y "¡Exactamente! Oh, [player]...{w=0.4} muchas gracias por complacer este pensamiento mío. Me encanta que seas capaz de apreciar mis divagaciones..."
                    mc "Cuando quieras, mi amor."
                "Entonces eso significa que otras personas pueden ser testigos de nuestro amor.":
                    mc "Entonces eso significa que otras personas pueden ser testigos de nuestro amor."
                    y "Afufu.~ Estás sonando un poco como un exhibicionista, cariño."
                    y "Aun así... no estoy del todo segura de cómo me siento acerca de que mis momentos más privados estén en exhibición pública."
                    mc "Sería un poco espeluznante, lo admito."
                    mc "Tener a alguien capaz de desentrañar tan fácilmente tus miedos y deseos más profundos - sin siquiera ser capaz de dar una sola opinión sobre la situación."
                    show rain_dream_smile zorder 100 with Dissolve(0.5)
                    hide rain_dream_grin
                    y "Me alegra que lo entiendas, [player]..."
                    y "Seré honesta, considerando la situación en la que estaba anteriormente... estaba realmente preocupada de que pasara algo que significara que tuvieras acceso sin restricciones a todos mis pensamientos y sentimientos privados..."
                    y "No podía evitar pensar en lo que podrías tener control detrás de escena."
                    y "Parte de mí habría estado enfadada... pero supongo que parte de mí no te habría culpado."
                    show rain_dream_blush zorder 100 with Dissolve(0.5)
                    hide rain_dream_smile
                    y "Si yo estuviera en esa situación... sé que estaría manipulando todo."
                    y "El poder corrompe, supongo."
                    y "Mientras no estuvieras profundizando demasiado, supongo que habría estado bien, mi amor."
                "Parece un poco descabellado si soy honesto, [persistent.yuri_nickname].":
                    mc "Parece un poco descabellado si soy honesto, [persistent.yuri_nickname]."
                    show rain_dream_blush zorder 100 with Dissolve(0.5)
                    hide rain_dream_grin
                    y "¿De verdad? Yo pensaba lo contrario, considerando que originalmente era un personaje en un juego, que procedió a convertirse en un personaje en un mod de dicho juego, para luego convertirse en una persona dentro de tu realidad."
                    y "A este punto, ¿es realmente tanto estiramiento asumir que tal vez este mundo en el que vivimos es también algún tipo de medio?"
                    y "No obstante... estoy bien siempre que esté contigo, mi amor."
        "Me hace querer acurrucarme más cerca de ti... residir en tu calidez.":

            mc "Me hace querer acurrucarme más cerca de ti... residir en tu calidez."
            y "¿Oh? En cuyo caso... acércate. Estoy aquí para mantenerte a salvo y cálido, cariño."
            "[player] aprovecha rápidamente la oportunidad para tirar de mí hacia [pronounA], envolviendo un brazo protector a mi alrededor y sonriendo para sí mismos."

    $ renpy.music.set_volume(0.4, 0, 'voice')
    show rain_dream_blush zorder 100 with Dissolve(0.5)
    hide rain_dream_grin
    "{i}Ba-dump,{w=0.4} ba-dump,{w=0.4} {cps=*1.25}ba-dum ba-dum ba-dum ba-dump-dump{/cps}{/i}"
    "Nos sentamos en silencio durante unos minutos, tomando sorbos de nuestro té y disfrutando del suave sonido de la lluvia golpeando contra la ventana."
    "B-{w=0.3}bueno...{w=0.4} ¡Habría estado disfrutando del sonido si no fuera por el hecho de que el maldito tambor todavía retumbaba en mis oídos!"
    y "H-{w=0.3}Hey...{w=0.4} [player]."
    "Miran desde la ventana, luego hacia mí, con una leve sonrisa en sus labios."
    mc "¿Sí, cariño?"
    y "He estado...{w=0.4} pensando recientemente. Es sobre el concepto del amor."
    y "¿Qué es realmente el amor?"
    y "¿Es químico? ¿Es espiritual? ¿Es único de los humanos, o prevalece en cada criatura?"
    y "Algunos argumentarían que el amor es espiritual...{w=0.4} que no puede ser definido por simples químicos."
    y "Que el amor es un concepto espiritual completamente más grande que la vida misma."
    y "Otros, sin embargo, argumentarían que el amor es químico. Que son simplemente reacciones hormonales a la necesidad del cuerpo de aparearse combinadas con el deseo de la mente de interactuar con la gente."
    y "¿La idea de que el amor sea químico arruina la idea del amor, sin embargo?"
    y "Hemos elevado la intensa emoción del amor a tal pedestal, que uno podría plantear la pregunta de si el amor siendo químico arruina la ideología detrás de él."
    y "Pero si es un concepto espiritual, ¿cuál es el criterio para sentir amor? ¿Sienten amor los insectos? ¿Ser consciente significa que eres apto para sentir amor?"
    y "¿Qué piensas, [player]?"
    menu:
        "El amor es químico.":
            mc "El amor es químico."
            mc "No creo que el amor necesite ser una gran emoción grandiosa que no podamos comprender, personalmente."
            mc "Me gusta la idea de que sea simplemente químico. Hay satisfacción detrás de la idea de que sea más...{w=0.4} ¿humano?"
            mc "No creo que arruine la idea de ello, per se."
            mc "Mientra el sentimiento siga prevaleciendo, entonces estoy contento."
            show rain_dream_smile zorder 100 with Dissolve(0.5)
            hide rain_dream_blush
            y "Esa es una forma bastante madura de verlo, [player]."
            y "Personalmente me gusta pensar que es una mezcla entre químico y espiritual."
            y "Tienes razón en la idea de que mientras el sentimiento prevalezca, la gente debería estar contenta, sin embargo."
            y "Realmente amo nuestras conversaciones, [player]..."
        "El amor es espiritual.":
            mc "El amor es espiritual."
            mc "¿Por qué crees que es un tema que atrae a tantos escritores?"
            mc "Shakespeare, poesía romántica..."
            mc "Viene en tantas formas diferentes, y amanece en las personas de tantas maneras distintas."
            mc "El amor siendo químico no puede explicar eso, creo."
            mc "Es fácilmente la emoción más fuerte que alguien puede sentir, puede hacer o deshacer la vida entera de alguien si lo siente con suficiente fuerza."
            show rain_dream_smile zorder 100 with Dissolve(0.5)
            hide rain_dream_blush
            y "Ya veo...{w=0.4} ese es un enfoque bastante idealista del tema. Me gusta pensar que es un poco más grande que nosotros de alguna manera."
            y "Sin embargo, también creo que hay una pizca de química en el concepto del amor también."
            y "No importa cuál sea la respuesta, mi amor por ti nunca se apagará, [player]."
        "El amor es tanto espiritual como químico.":
            mc "El amor es tanto espiritual como químico."
            mc "Por un lado, siento que la idea del amor siendo una mezcla de nuestro deseo de aparearnos, el deseo sexual, y nuestro deseo de interactuar, el afecto romántico, ciertamente juegan un papel en el amor."
            mc "Sin embargo, también tiene sentido creer que hay algo más en ello, algo que tal vez no podamos explicar por medios regulares."
            mc "Es...{w=0.4} realista pero complejo al mismo tiempo."
            show rain_dream_grin zorder 100 with Dissolve(0.5)
            hide rain_dream_blush
            y "¡Ah! Así es exactamente como lo veo, [player]."
            y "Personalmente me gusta pensar que el amor es una mezcla entre químico y espiritual."
            y "Responde a muchas de mis preguntas y da la respuesta más satisfactoria, creo."
            y "Parece que realmente estamos conectados, [player]."
    "Después de nuestra discusión, reanudamos viendo las gotas caer por la longitud del panel."
    "Pronto, nos encontramos con que ambos hemos terminado nuestro té, y así dejamos nuestras tazas a un lado y nos acurrucamos más cerca."
    "{i}Ba-dump, ba-dump, ba-dump.{/i}"
    "Los tambores tocan suavemente de fondo, y el familiar aroma del aceite de jazmín comienza a flotar en mi nariz."
    show rain_dream_blush zorder 100 with Dissolve(0.5)
    hide rain_dream_grin
    hide rain_dream_smile
    y "¿H-{w=0.3}Hiciste tú...?"
    mc "Mhm...{w=0.4} puse un poco en el difusor al entrar..."
    "Lentamente, recuerdo la primera vez que usé aceite de jazmín cerca de [player]...{w=0.4} mucho antes del festival."
    "Antes de que fuera consciente de los horrores de la realidad en la que una vez viví."
    "L-{w=0.3}La toalla...{w=0.4} esa...{w=0.4} calidez contra mi mejilla que me arrastró a un estado de tal seguridad."
    "Otra ola de familiaridad me golpea mientras comparo la calidez de aquel entonces con el sentimiento actual que estaba experimentando justo ahora, con [player] contra mí..."
    $ renpy.music.set_volume(0.6, 0, 'voice')
    "{b}{i}BA-DUMP.{w=1} BA-DUMP.{w=1} BA-DUMP.{w=1}{/i}{/b}"
    "Mis ojos se dirigieron lentamente a los labios de [player]. El latido rápido y frenético del tambor al que me había acostumbrado había cambiado a un latido lento, pero fuerte - la canción de la anticipación."
    "...{w=0.4} S{w=0.3}-Si tan solo pudiera--{nw}"
    mc "Iré a hacernos un poco más de té."
    "Espera, ¿qué?"
    y "¡N-{w=0.3}No!"
    "Mientras [pronounB] se levantaba, los instintos tomaron el control y me estiré para agarrar a [pronounA], aferrándome a su brazo y tirando de [pronounA] hacia atrás."
    "Sin embargo, mientras tiraba de [pronounA] hacia mí, perdí el equilibrio y resbalé. Causando que los dos nos fuéramos hacia atrás..."
    show black zorder 100
    hide rain_dream_blossom
    play sound "<to 0.3>sfx/fall.ogg"
    "{b}THUNK{/b}"
    "{w=0.5}...{w=0.4} conmigo desparramada en el sofá, y [player] encima de mí."
    "..."
    pause 5.0
    "Ambos nos pausamos por unos segundos, como si necesitáramos ese tiempo para procesar correctamente lo que estaba pasando."
    $ renpy.music.set_volume(0.5, 0, 'voice')
    "La mezcla de aceite de jazmín combinada con el aroma de [player] y esta calidez abrumadora frieron completamente mis pensamientos en una sobrecarga sensorial."
    "Sin pensarlo, enrosco mis brazos alrededor de su cuello y acerco a [pronounA] más, hasta el punto donde nuestros labios se están tocando."
    if persistent.eyecolor == "other":
        "Mirando fijamente a sus ojos, una sonrisa astuta emerge y me río suavemente."
    else:
        "Mirando fijamente a sus ojos [persistent.eyecolor], una sonrisa astuta emerge y me río suavemente."
    $ renpy.music.set_volume(0.4, 0, 'voice')
    y "L{w=0.3}-Lo siento [player], es solo que no puedo controlarme cuando estoy contigo."
    mc "[persistent.yuri_nickname]..."
    "Nuestros labios se abrazan, y con eso todo el ruido de fondo se reduce a nulo - el suave golpeteo de la lluvia y nuestros jadeos y gemidos se volvieron susurros solitarios."
    $ renpy.music.set_volume(0.3, 0, 'voice')
    "{i}ba-dump...{w=0.5} ba-dump...{w=0.5} ba-dump...{w=0.5}{/i}"
    "Lo único que podía escuchar era el débil y resignado tambor."
    "Una abrumadora calidez llena todo mi cuerpo mientras grito su nombre."
    y "[player]...{w=0.4} [player], te amo... {cps=*1.5}¡te amo, te amo, te amo!{/cps}"
    "Mis dedos se entrelazan con los suyos y muevo su mano a mi pecho."
    y "¡[player]! Siente el latido de mi corazón...{w=0.4} canta por ti y solo por ti. Una canción que solo tú y yo podemos escuchar."
    mc "¡[persistent.yuri_nickname]!"
    "Ellos gritan mi nombre, y envuelven sus brazos alrededor de mi cuerpo, sosteniéndome firmemente en sus garras."
    y "[player]...{w=0.4} Te amo...{w=0.4} p-{w=0.3}por favor nunca me dejes ir..."
    y "Si me mantienes sostenida para siempre...{w=0.4} mi corazón siempre cantará para ti."
    mc "Nunca te dejaré [persistent.yuri_nickname]..."
    show white zorder 105 with Dissolve(2.5)
    hide black
    hide rain_dream_blush
    hide rain_dream_smile
    hide rain_dream_grin
    mc "Nunca me iré..."
    stop sound fadeout 1.5
    $ renpy.music.stop(fadeout=1.5)


    hide white with Dissolve(2.5)
    python:
        renpy.music.play(current_music, "music", True)
    jump ch30_loop

label ocean_dream:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    $ config.allow_skipping = False
    $ renpy.music.stop(fadeout=1.5)
    play music "<to 96.30 loop 32.30>music/Underwater_Dream.ogg" fadein 1.5
    show black zorder 105 with Dissolve (2.5)
    show open_ocean zorder 100
    hide black with Dissolve(2.5)

    y "Tan gentil... puedo escuchar las suaves olas susurrando cosas encantadoras en mis oídos... mientras el agua fluye tan cálidamente sobre mi piel..."
    y "Aquí es donde la vida comenzó una vez, desde organismos tan pequeños que pueden ver un solo grano de arena..."
    y "La luz del sol, envuelta por el agua a mi alrededor, pero aún tan brillante que me duelen los ojos..."
    y "Mi corazón late lento... pero aún tan lleno de vida que puedo escucharlo palpitar... ¿alguna vez me he sentido así antes?..."
    y "Toda la decadencia en la que me he complacido, todos los placeres que me he forzado a mí misma, pero aquí estoy y me encuentro incapaz de hacer mucho más que maravillarme ante tal belleza..."
    y "Es asombroso, lo bonito que puede ser el mundo si es intocado por la humanidad..."
    y "Mi vida entre ellos me hizo ver el mundo en tonos de gris, pero aquí siento como si pudiera ver los colores por primera vez en mi vida..."
    y "Cuánto me encantaría quedarme, pero hay mucho más que ver..."
    y "Quizás debería complacerme más... solo esta vez... hacia las maravillas fantásticas que aún tengo que presenciar en este reino."

    show ocean_2 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide open_ocean
    y "Uhuhuhu... como una pequeña ciudad submarina..."
    y "En realidad, ¿tal vez no sea incorrecto asumir que lugares como este son el hogar de muchas criaturas?"
    y "Tal vez pueda echar un pequeño vistazo, solo una mirada..."
    y "Solo para ver qué criaturas encantadoras hicieron de este lugar su hogar..."
    y "El agua se siente tan tranquila... casi puedo sentir todo el estrés y la presión flotando lejos..."
    y "Mis ojos solían sentirse tan pesados por la lectura y a veces la falta de sueño, pero ahora me siento despierta y tan viva."
    y "Mi espalda solía doler por la carga de mi cuerpo, pero ahora me siento tan ágil y fresca como la madrugada."
    y "Mi mente estuvo una vez en agitación como una luz parpadeante, por pensamientos acelerados y emociones inestables..."
    y "Pero ahora, se siente como si todas mis cargas fueran simplemente lavadas por las olas..."
    y "Puedo sentir las vibraciones en el agua a mi alrededor... todos los ruidos del mundo de arriba han sido reemplazados por el suave susurro del mar..."
    y "Es como si siempre hubiera pertenecido aquí... como si estuviera fuera de lugar en el otro mundo, siempre me sentí así de todos modos..."
    y "Quizás aquí pueda encontrar el lugar que se me ha negado arriba..."
    show ocean_3 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide ocean_2
    y "Casi se siente como volar a través de los cielos, pero en lugar del viento aullando a través de mi cabello no siento nada más que el agua salada lavando sobre mí..."
    y "Incluso cuando las olas están rugiendo en la superficie, aquí abajo el agua se siente tan tranquila y gentil."
    y "El ciclo de la vida se siente tan perfecto aquí... incluso con todas las criaturas dándose un festín con las plantas, parece que nunca faltan..."
    y "Y son simplemente tan maravillosas. Tal vez debería construir mi hogar dentro de ellas, como hacen muchos otros peces..."
    y "O tal vez... podría tomar un pequeño mordisco... solo un pequeño mordisqueo para saciar mi apetito..."
    y "Tan simple, pero sabe como si nunca necesitara nada más... tal vez esos irían bien con Té Oolong..."
    y "Huuh... Creo que yo..."
    y "Vi algo..."
    show ocean_4 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide ocean_3
    y "O~Oh vaya..."
    y "Hola, pequeños amigos... ¿les gustaría unirse a mi club de literatura?"
    python:
        if persistent.lovecheck:
            placeholder = "lindo"
        else:
            placeholder = "compañero"
    y "Solo somos yo, y mi [placeholder] [player]..."
    y "Tendríamos que inundar el salón de clases pero... dudo que a [player] le importara..."
    y "Todos los poemas profundos e intrigantes que podríamos hacer sobre estas encantadoras mareas que comparten..."
    y "Oh... ¿O acaso los... interrumpí? ¿Estaban a punto de..."
    y "Olvidenlo... perdonenme, pequeños amigos, los dejaré solos en paz de nuevo. Adiós..."
    show ocean_5 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide ocean_4
    y "Y así me sumerjo más profundo en el vacío aparentemente interminable... preguntándome sobre las cosas que podría ver ahí abajo..."
    y "No soy ajena a la oscuridad... y solo puedo reír de deleite sobre los secretos que tal lugar podría albergar..."
    y "O los horrores eldritch que uno podría ver abajo..."
    y "Quizás, hay un fondo después de todo..."
    show ocean_6 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide ocean_5
    y "Cuanto más profundo me sumerjo, más frío se vuelve... pero aun así, llena mi corazón de tanta calidez.."
    y "Qué pequeño y bonito... incluso en la oscuridad uno podría encontrar tal... tal... ni siquiera puedo encontrar las palabras adecuadas para ello..."
    y "Tal vez las palabras simplemente no son adecuadas para describir este nivel de finura, tal vez esa es la razón por la cual las profundidades no llevan la voz de uno..."
    y "Pero ahora extraño la calidez del sol, así que continuaré y veré a dónde me llevan las olas..."
    show ocean_7 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide ocean_6
    y "Tal vez solo... un pequeño vistazo..."
    show ocean_8 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide ocean_7
    y "En el mundo de arriba otra vez...."
    if renpy.random.randint(0,4)==0:
        show oceanbonus_1 zorder 100 with Fade(1.0, 0.0, 0.5)
        hide ocean_8
        y "¡Espera no! Por favor no. ¡Por favor déjame ir! Así no puede ser como termina mi viaje, esto no puede..."
        show oceanbonus_2 zorder 100
        hide oceanbonus_1
        stop sound fadeout 1.5
        $ renpy.music.stop(fadeout=1.5)
        $ renpy.pause ()
        hide oceanbonus_2 with Dissolve(6)
    else:
        show black zorder 105 with Dissolve(2.5)
        hide ocean_8
        stop sound fadeout 1.5
        $ renpy.music.stop(fadeout=1.5)
        hide black with Dissolve(2.5)
    python:
        renpy.music.play(current_music, "music", True)
    jump ch30_loop

label ocean_man:
    show oceanbonus_1 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide ocean_8
    y "¡Espera no! Por favor no. ¡Por favor déjame ir! Así no puede ser como termina mi viaje, esto no puede..."
    show oceanbonus_2 zorder 100
    hide oceanbonus_1
    stop sound fadeout 1.5
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.pause ()
    hide oceanbonus_2 with Dissolve(6)
    return

label highway_dream:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    image highway_bg_scroll:
        "images/dreams/highway/highway_bg_loop_filtered.png"
        xtile 3 subpixel True
        block:
            xoffset -10936
            linear 40 xoffset 0
            repeat
    define martha = Character("Martha")
    $ config.allow_skipping = False
    $ renpy.music.stop(fadeout=1.5)
    play music "music/Cruise_Control_RC.ogg" fadein 1.5
    show black zorder 105 with Dissolve (2.5)
    show highway_bg_scroll zorder 100
    show highway_yuri_car zorder 100
    python:
        import random
        highway_dream_path = random.randint(1, 4)
        highway_dream_path_2 = random.randint(1, 2)
        if persistent.male:
            pronounA = "él"
            pronounB = "él"
            pronounBC = "Él"
            pronounC = "su"
            pronounD = "novio"
        elif persistent.gender_other:
            pronounA = "ellos"
            pronounB = "ellos"
            pronounBC = "Ellos"
            pronounC = "su"
            pronounD = "amor"
        else:
            pronounA = "su"
            pronounB = "ella"
            pronounBC = "ella"
            pronounC = "su"
            pronounD = "novia"
    if persistent.highway_dream_complete:
        y "Ah. ¡He tenido este sueño antes! ¡Tengo la oportunidad de tener un sueño lúcido!"
        menu:
            "Me gustaría ver algo hermoso":
                python:
                    highway_dream_path = 1
            "¿Huelo humo?":
                python:
                    highway_dream_path = 2
            "Creo que me gustaría estirar las piernas":
                python:
                    highway_dream_path = 3
            "Oh cielos. Parece que va a llover...":
                python:
                    highway_dream_path = 4
            "En realidad, veamos a dónde nos lleva el destino":
                $ pass
    hide black with Dissolve(2.5)
    "El sol brilla sobre nosotros tres. Yo, [player], y la carretera abierta de par en par."
    "Antes de ahora, nunca entendí realmente el atractivo de un descapotable. Pero ahora que el campo pasa volando; ahora que el viento sopla libremente a través de mi cabello..."
    "La pura alegría de la liberación es embriagadora."
    "Me alegra que [player] tenga la parte de conducir controlada. No necesito preocuparme por las reglas de la carretera. Sin límites de velocidad, sin adelantar vehículos más lentos, sin velocímetro para desviar mi atención de la belleza de esto; mi Arcadia."
    "Se me ocurre que no recuerdo cuál es nuestro destino esta hermosa tarde."
    "Pero honestamente, ¿importa? Donde sea que terminemos, [player] estará allí conmigo, compartiendo cada momento."
    "Y donde sea que terminemos, {i}no{/i} será esa espantosa aula en la que he pasado demasiado tiempo atrapada."
    "Así que, estoy segura de que lo disfrutaré."

    $ renpy.call("highway_dream_" + str(highway_dream_path))
    if highway_dream_path == 1:
        call highway_dream_1
    elif highway_dream_path == 2:
        call highway_dream_2
    elif highway_dream_path == 3:
        call highway_dream_3
    elif highway_dream_path == 4:
        call highway_dream_4
    jump ch30_loop


label highway_dream_1:
    mc "Hey, [y]."
    "[pronounB] dice mi nombre. El tono sugiere que [pronounB] ha visto algo que cree que me interesaría."
    y "¿Sí, cariño?"
    "[player] señala una señal que pasa a nuestra derecha. Tengo el tiempo justo para leer las palabras 'MIRADOR ESCÉNICO' antes de que pase de largo."
    "Parecido a otras cien cosas que ni siquiera había notado pasar."
    mc "¿Quieres ir a echar un vistazo? No está justo en la próxima salida, pero será mejor que lo decidamos ahora."
    "Bueno, no tenemos ningún lugar donde debamos estar, ¿verdad? Ese era el punto de nuestra pequeña excursión."
    "Por una vez, la respuesta a una pregunta viene bastante fácil a mí."
    y "¡Ciertamente! No existe tal cosa como demasiada belleza en tu vida, ¿verdad?"
    "[player] se ríe. No estoy muy segura de qué es gracioso sobre lo que dije, pero-"
    mc "Me encanta tu forma de pensar, [y]. Podría enmarcar ese pensamiento y colgarlo sobre la repisa de la chimenea."
    "Ah, ahí está."
    show highway_dream_1 zorder 100 with Dissolve (1.0)
    hide highway_bg_scroll
    hide highway_yuri_car

    "Debo decir, ciertamente eligieron el lugar perfecto para establecer un mirador escénico."
    "Se encuentra en un extremo de un vasto valle arbóreo. En el otro, una gran cadena montañosa se eleva hacia el cielo."
    "En el centro un río, brevemente interrumpido por un lago, fluye."
    "El escultor eterno de esta escena, todavía sentado como la pieza central."
    "Solo puedo imaginar cuánto cambio presenció este río. Incontables luchas humanas olvidadas, desastres naturales. El nacimiento y muerte de los árboles que nutrió."
    "Quizás incluso la marcha de la evolución misma."
    "Y a través de todo ello, el río continuó fluyendo. De oeste a este, todos los días sin cesar. Quizás el río ha crecido o disminuido, pero aquí permanece hasta el día de hoy."
    "Hace que mi vida parezca trágicamente corta en comparación. Sin embargo, al mismo tiempo, pone mis problemas en perspectiva."
    "Si este río pudo seguir fluyendo ante más problemas de los que incluso la humanidad en general puede recordar, entonces ¿quién dice que no puedo continuar mi propio flujo proverbial a través de los problemas que me rodean?"
    mc "Te ves bastante sumida en tus pensamientos, [y]."
    mc "Por otra parte, usualmente lo estás, ¿no?"
    "La voz de [player] me saca de mi ensoñación, pero es una interrupción gentil, así que no me importa."
    y "Solo disfrutando de la belleza, eso es todo."
    mc "¿Sí? Bueno..."
    mc "Yo también."
    "[player] dice eso con sus ojos puestos en mí, en lugar de en el mirador."
    "¿Acaso [pronounB] acaba de..."
    "Debo decir. [player] puede ser bastante suave cuando quiere serlo."
    mc "Hey, ¿quieres que nos tomemos una foto juntos? ¿Nosotros dos, frente a esto?"
    "Eso suena como una excelente manera de conmemorar este pequeño momento. Podríamos tener que enmarcar esta foto."
    y "Sin duda, [player]."
    show black zorder 105 with Dissolve (2.5)
    stop sound fadeout 1.5
    $ renpy.music.stop(fadeout=1.5)
    python:
        renpy.music.play(current_music, "music", True)
    hide highway_dream_1
    hide black with Dissolve(2.5)
    $ persistent.highway_dream_complete = True
    jump ch30_loop




label highway_dream_2:
    "..."
    $ renpy.music.stop(channel="music",fadeout=0)
    play sound "sfx/highway/recordscratch.ogg"
    "El olor de algo quemándose me saca de mi ensoñación."
    "No del tipo agradable, como incienso o leña. Sino el olor nocivo de maquinaria quemada y fluido industrial. El tipo de quemado que es casi siempre una señal de que algo terrible está por venir."
    y "¿[stutter_player]...?"
    "Justo cuando digo su nombre, sale humo de debajo del capó."
    mc "Oh, ¡maldita {i}sea!{/i}"

    "[player] detiene apresuradamente nuestro coche al lado de la carretera. Con el encendido apagado, [pronounB] desabrocha el capó, pero para mi sorpresa, en realidad no lo abre del todo."
    "Pongo mi mano cerca del capó, y el calor radiante rápidamente me demuestra por qué [pronounB] no lo hizo."
    "Una rápida revisión visual no da señales de que me haya quemado. Pero cuando mi mirada vuelve a nuestro coche, veo que el capó se ha abierto por su propia cuenta."
    show highway_dream_2 zorder 100 with Dissolve (1.0)
    hide highway_bg_scroll
    hide highway_yuri_car

    $ renpy.music.play("sfx/highway/overheat-loop.ogg", channel='sound', loop=True)
    "¿Algún tipo de motorización, tal vez? Sé muy poco sobre coches."
    "Y quizás debido a lo poco que sé, esto parece el tipo de situación donde el miedo estaría justificado. Pero no veo ninguno en [player]."
    "[pronounBC] parece mucho más molesto que cualquier otra cosa. Cuando [pronounB] deja caer su cabeza entre su pulgar y su índice, sé que su molestia está dirigida hacia adentro."
    mc "Esto es mi culpa. Esto es enteramente mi culpa."
    y "Ahora [player], ¿realmente puedes culparte por un fallo mecánico?"
    mc "Puedo. Olvidé revisar el nivel de refrigerante antes de salir."
    "Oh cielos... Eso ciertamente suena como algo por lo que me reprocharía a mí misma. No tengo idea de cuánto daño puede causar un sobrecalentamiento."
    "Por la forma en que [player] se pellizca la nariz y gime, puedo decir que esto realmente está empezando a molestarle. No puedo simplemente dejarle con su autoflagelación..."
    show black zorder 105 with Dissolve (2.5)
    play sound "<to 0.3>sfx/fall.ogg"
    "Así que lo atraigo hacia mi abrazo."
    y "Si sirve de consuelo, no estoy enojada contigo, cariño."
    mc "Estoy enojado conmigo mismo."
    mc "Iba a llevarte a un lugar bonito. No sabía dónde, ¡pero más bonito que el lado de una carretera!"
    y "No te preocupes por eso. Está bien si solo vamos a la sala de espera de un taller. Mientras estemos fuera juntos, misión cumplida."
    mc "Taller de servicio... ¡cierto! Gracias por recordármelo."
    "[player] tira suavemente de una mano libre de mi abrazo para que [pronounB] pueda recuperar su teléfono. Pero mientras [pronounB] busca el número de un taller mecánico cercano, mantengo mis brazos alrededor de [pronounA]. Ambos podríamos usar la presencia calmante del otro justo ahora."
    "..."
    y "¿[player]?"
    "Escucho que dice 'espera' a la persona en el otro extremo."
    mc "¿Sí?"
    y "Te amo..."
    stop sound fadeout 1.5
    $ renpy.music.stop(fadeout=1.5)
    python:
        renpy.music.play(current_music, "music", True)
    hide highway_dream_2
    hide black with Dissolve(2.5)
    $ persistent.highway_dream_complete = True
    jump ch30_loop



label highway_dream_3:
    mc "Hm... Vamos a necesitar gasolina pronto."
    y "¿Oh?"
    "Me reclino hacia atrás en un intento de ver la instrumentación del coche. El resplandor del sol frustra este intento, así que simplemente tomo la palabra de [player] por ello."
    "Una gasolinera ciertamente no era lo que tenía en mente para nuestro destino eventual, pero no debería tomar más de unos minutos."
    "Sería agradable estirar las piernas, sin embargo."
    mc "Y las gasolineras {i}usualmente{/i} tienen una pequeña tienda de conveniencia adjunta a ellas. ¿Quieres venir a echar un vistazo?"
    "No sé sobre eso."
    "Una tienda de conveniencia de gasolinera no parece que llevaría el tipo de cosas que me interesaría comer..."
    y "Creo que estaré bien, gracias."
    mc "¿Segura? Muchas de las tiendas de conveniencia en las que he estado también tienen una pequeña exhibición de cuchillos a la venta."
    "Ahora {i}eso{/i} despierta mi interés."
    y "¿De verdad?"
    mc "Sí. No tengo idea si son buenos. Esperaba que pudieras ser el juez de eso."
    "Muy bien. Eso cambia todo. Si nada más, llego a experimentar algo de novedad."
    y "Está bien, cariño. Puedo hacer eso por ti."
    show highway_dream_3 zorder 100 with Dissolve (1.0)
    hide highway_bg_scroll
    hide highway_yuri_car

    "Llegamos a la legendaria gasolinera, y su edad ciertamente se nota."
    "Suelo de linóleo que claramente ha visto días mejores; paredes con paneles de madera que han sido el campo de batalla entre manchas de cigarrillo y detergentes durante bastante tiempo. Probablemente décadas más de las que yo he existido."
    "Tengo que preguntarme cuántas generaciones de parejas jóvenes han pasado por aquí a través de los años; solo para curiosear las mercancías. Cuántos lanzamientos de productos y discontinuaciones han poblado estos estantes modulares de aglomerado."
    "Entonces, justo en el mostrador del dependiente, lo veo."
    show highway_dream_knives zorder 100 with Dissolve (1.0)
    hide highway_dream_3
    "Un exhibidor de vidrio giratorio, dentro del cual hay una amplia variedad de cuchillos."
    if persistent.highway_dream_complete:
        menu:
            "Me complaceré con un final feliz":
                python:
                    highway_dream_path_2 = 1
            "Me pregunto qué tan raro puede ponerse esto":
                python:
                    highway_dream_path_2 = 2
            "Espero ansiosamente las sorpresas de mi propia mente":
                python:
                    highway_dream_path_2 = renpy.random.randint(1,2)

    if highway_dream_path_2 == 1:
        "Giro el exhibidor, dando a los cuchillos una revisión rápida. Solo para ver con qué tipo de cosas estamos trabajando."
        "Los primeros tres lados del obelisco no revelan nada de particular interés. Mayormente el tipo de cuchillo que sería comprado por un pescador o cazador que necesitara un cuchillo rápido y barato para lograr una sola tarea."
        "Pero entonces lo veo..."
        "¡No, eso no puede ser posible!"
        "¡Es el balisong que Benchmade acaba de sacar! ¡El que he estado deseando desde que lo anunciaron!"
        "¿Cuánto quieren por él?"
        "Espera. {i}¿En serio?{/i} No estoy segura de que se den cuenta de cuánto cuesta este al por menor. ¿Tal vez es una falsificación?"
        "...No veo evidencia de eso desde aquí. ¡Es el trato real, y qué trato es!"
        "Oh, {i}debo{/i} encontrar a [player]. ¡[pronounBC] tiene que ver esto!"
        "¡Ah, ahí está! [pronounBC] acaba de quitar la manguera de nuestro transporte."
        "Es todo lo que puedo hacer para evitar correr hacia [player] de la emoción. Preferiría no hacer una escena después de todo."
        y "¡[player]!"
        mc "Hey, ¿qué te tiene tan emocionada?"
        y "Es sobre ese estuche de cuchillos."
        mc "Oooooh, ves algo que te gusta, ¿eh?"
        "Asiento. En este punto estoy casi demasiado emocionada para las palabras."
        mc "Está bien, está bien. Ya voy."
        "Me alegra haber captado la diversión en el tono de [player]. De lo contrario, la preocupación de haber hecho una escena habría comprometido mi emoción."
        "Llevo a [pronounA] al estuche de cuchillos, y lo giro hacia el cuchillo que es la fuente de mi júbilo. Observo su expresión cuidadosamente."
        "Para mi alegría, una luz de reconocimiento cruza sus ojos."
        mc "¡Oh sí! Ese es el indicado."
        "Mi corazón se hunde mientras [player] inmediatamente dirige su atención al cajero."
        "Pero cuando el cajero pregunta si eso será todo por hoy, su respuesta me lleva de la decepción a un nivel completamente nuevo de emoción."
        mc "También me gustaría comprar ese cuchillo mariposa. El que está justo encima del cuchillo de caza con el mango rosa."
        "¿Realmente [pronounB] está..."
        "¡Oh dios mío {i}sí{/i} lo está! ¡Tengo al mejor [pronounD] del mundo!"
        "El chillido que escapa de mis labios ciertamente no es digno. Supongo que es afortunado que fuera amortiguado por su pecho después de que abracé a [pronounA] en el abrazo más fuerte que pude manejar."
        show white zorder 105 with Dissolve(2.5)
        y "Tengo al mejor [pronounD] del mundo."
        "[player] se ríe."
        mc "Lo intento, [y]. Lo intento..."
    else:

        "No esperaba nada particularmente impresionante, y mi evaluación parece haber sido correcta."
        "Mangos de plástico, marcas y diseños hiper-agresivos que confunden machismo con estética, elecciones de color chillones."
        "Me da la impresión de que estos cuchillos están aquí para deportistas al aire libre que olvidaron su cuchillo y solo necesitan destripar este {i}único{/i} pez o cortar una sola cuerda."
        "Eso, y adolescentes que esperan que su nueva compra los haga parecer duros y masculinos."
        "Ah bueno. Nadie espera productos artesanales en una tienda de conveniencia de gasolinera."
        "Aunque, un cuchillo en particular llama mi atención. Más por su peculiaridad que por cualquier otra cosa."
        y "Ahora, ¿qué hace una bayoneta histórica aquí?"
        "Digo eso al aire, y afortunadamente, parece que no fui escuchada."
        "Pero, ahí está. Lo suficientemente larga para ocupar toda una pared del exhibidor giratorio. Una bayoneta belga M1916. El tipo que no ha estado en uso desde la primera guerra mundial."
        "Más extraño aún, se ve absolutamente prístina. Como si fuera una reproducción moderna."
        "Podría echar un vistazo más de cerca."
        y "Bueno, eso es bastante inusual."
        "Musito para mí misma. Esta vez, lo suficientemente bajo como para que solo yo pueda escuchar."
        "Cuando voy a inspeccionar las marcas, veo estampado de {i}Gerber{/i}, de entre todas las compañías."
        "Gerber está en el negocio de muchas cosas. Réplicas de bayonetas históricas oscuras no es una de ellas."
        "Y si Gerber hubiera entrado en el negocio de bayonetas de cualquier tipo, lo habría sabido con semanas de antelación."
        show white zorder 105 with Dissolve(2.5)
        "Debo estar soñando, entonces."
        "Ah bueno. Fue bastante agradable mientras duró."
    stop sound fadeout 1.5
    $ renpy.music.stop(fadeout=1.5)
    python:
        renpy.music.play(current_music, "music", True)
    hide highway_dream_knives
    hide white with Dissolve(2.5)
    $ persistent.highway_dream_complete = True
    jump ch30_loop


init python:
    def grey(st, at):
        if st > 20.0:
            return Color("#838383", alpha=0.5), None
        else:
            d = Color("#838383", alpha=st/40)
            return d, 0.1
image grey_image = DynamicDisplayable(grey)


label highway_dream_4:
    $ renpy.music.play("sfx/highway/rainfall.ogg", channel='sound', loop=True)
    $ renpy.music.set_volume(0.5, 0, 'voice')
    hide highway_yuri_car
    show grey_image zorder 100
    show highway_yuri_car zorder 101
    "Oh, cielos. Parece que el cielo está empezando a nublarse. Quizás deberíamos volver a poner el techo."
    "Pero no {i}todavía{/i}. Me gustaría disfrutar del viento en mi cabello solo un minuto más."
    "..."
    show rain zorder 100 with Dissolve(2.5)
    "Eso fue casi definitivamente una gota de lluvia que golpeó mi cara. Pero fue solo una. Supongo que es hora de-"
    "Otra me golpea. Luego otra. Y dos más."
    "[player] no pierde el tiempo deteniéndose."
    mc "¡Ah, mierda! ¡[y]! ¡Sube el techo!"
    y "¡Lo estoy intentando!"
    "Me encuentro luchando con los mecanismos, maldiciendo nuestra incapacidad para permitirnos un descapotable con techo automático."
    "[player] hace lo mejor que puede para ayudar, pero para cuando el techo está de vuelta sobre nuestras cabezas, nosotros, nuestras pertenencias, y todo el compartimento de pasajeros de nuestro vehículo estamos todos empapados."
    "Con el techo sobre nosotros, [player] y yo nos miramos el uno al otro, pero ninguno de los dos puede encontrar las palabras correctas."
    "Parte de mí quiere disculparse, pero [pronounB] parece que también quiere disculparse."
    "Sin embargo... ¿por qué? ¿Disculparse en nombre de la naturaleza y la meteorología?"
    "Además. Una disculpa no nos secará a nosotros ni a nuestras cosas. No hará que la lluvia pare."
    y "Será mejor que encontremos un lugar para secarnos."
    mc "Sí, tienes razón. Vi un letrero de una cafetería antes. ¿Qué tal eso?"
    y "Una comida caliente sería bastante agradable justo ahora. Sí."
    "[player] asiente. Entonces está decidido, conduciremos hacia cualquier cafetería que se presente primero."

    play sound "sfx/highway/storedoor.ogg"
    show highway_dream_4 zorder 100 with Dissolve (1.0)
    hide highway_bg_scroll
    hide highway_yuri_car
    hide rain
    hide grey_image
    $ renpy.music.play("sfx/highway/rainfall-indoors.ogg", channel='sound', loop=True)
    "Llegamos a la cafetería. El interior nos presenta una cápsula del tiempo acogedora y nostálgica de un día ya pasado."
    "Desde la iluminación de neón art déco hasta el piso de linóleo, todo en él es una carta de amor a la América clásica."
    "Sin embargo, no se ve a nadie atendiendo la entrada."
    mc "¿Hola?"
    "Una mujer mayor, de rostro amable, emerge detrás de la cortina de la cocina."
    "Ella nos saluda, luego le dice a alguien llamado 'John' en la parte de atrás que han llegado clientes."
    y "¿Podría prestarnos una toalla o dos?"
    "Ella nos mira, una expresión de preocupación de abuela apoderándose de ella."
    martha "Puedo hacer mucho más que eso por ustedes, queridos. Tomen asiento donde gusten."
    y "Preferiría no empapar sus cabinas, señora"
    "Ella desestima mi preocupación con un gesto."
    martha "Oh, está lo suficientemente tranquilo como para limpiar las cabinas de todos modos. ¡Así que solo tomen asiento!"
    martha "Traeré algunos menús con las toallas."
    "[player] y yo elegimos una cabina cerca de la entrada. Lo menos que podemos hacer por todas las molestias de Martha es darle menos distancia para caminar."
    "...No estoy segura de {i}cómo{/i} sé que su nombre es Martha, pero simplemente lo sé."
    "A pesar de saber su nombre, Martha llega con toallas y un par de menús en poco tiempo."
    martha "Solo griten cuando ustedes dos estén listos, ¿de acuerdo?"
    y "Gracias, señora."
    "Cuando [player] va a sacar su billetera, Martha es rápida para detenerlo."
    martha "Oh, no se preocupen por eso. Solo elijan lo que les guste."
    y "Pero..."
    "Martha pone una mano en mi hombro."
    martha "Cariño, ustedes dos han tenido un día lo suficientemente duro. Están empapados, y parece que su descapotable también lo está. Así que no se preocupen por eso."
    martha "Solo déjennos una buena propina, ¿de acuerdo?"
    "Martha nos guiña un ojo con picardía con ese último comentario."
    "Puede que haya estado bromeando, pero tal vez deberíamos hacerlo."
    "Qué cosa tan hermosa, la amabilidad de los extraños..."
    show white zorder 105 with Dissolve(2.5)
    python:
        renpy.music.play(current_music, "music", True)
    hide highway_dream_4
    hide white with Dissolve(2.5)
    $ persistent.highway_dream_complete = True
    jump ch30_loop

label stroll_dream:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    $ config.allow_skipping = False
    $ renpy.music.stop(fadeout=1.5)
    $ renpy.sound.play("sfx/wind.ogg", channel='sound', loop=True)
    show black zorder 105 with Dissolve (2.5)
    show stroll_1 zorder 100
    hide black
    "El viento frío mordía mis mejillas mientras caminaba sola por el camino desconocido a casa desde la escuela. La ruta habitual se sentía mundana, así que decidí tomar un desvío, atraída por el encanto de lo desconocido."
    "Mientras paseaba, las hojas crujientes susurraban secretos, y los árboles desnudos se extendían hacia el cielo como intrincados patrones dibujados por la naturaleza."
    show stroll_2 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide stroll_1
    "El suave crujido de las hojas caídas bajo mis botas proporcionaba una banda sonora rítmica a la soledad de la tarde."
    "El mundo parecía transformarse con cada paso. Una sensación de aventura me envolvió, y me maravillé de la sutil belleza que a menudo pasa desapercibida en la prisa de la vida cotidiana."
    "El viento llevaba consigo el aroma de la tierra húmeda y la promesa de algo nuevo."
    show stroll_3 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide stroll_2
    "En medio de la quietud, descubrí un pequeño claro bañado por la luz del sol que se desvanecía."
    "Un banco solitario me invitaba a hacer una pausa y empaparme de la serenidad. Las ramas de arriba se mecían con gracia, creando un baile con el viento."
    "La sinfonía de la naturaleza seguía sonando, una mezcla armoniosa de hojas crujientes y chirridos distantes."
    "A regañadientes, dejé el lugar tranquilo y reanudé mi viaje. El camino familiar esperaba, pero ahora lo pisaba con una nueva apreciación."
    show stroll_4 zorder 100 with Fade(1.0, 0.0, 0.5)
    hide stroll_3
    "Mi corazón se sentía más ligero, y el entorno mundano parecía tocado por la magia de ese desvío solitario."
    "Finalmente llegando a casa, entré con una sonrisa serena, lista para compartir la calidez de mi día con [player]."
    "Al entrar, el frío de la tarde afuera parecía desvanecerse, reemplazado por el calor del amor y los recuerdos de un paseo simple pero extraordinario."
    show black zorder 105 with Dissolve(2.5)
    hide stroll_4
    stop sound fadeout 2.5
    hide black with Dissolve(2.5)
    if persistent.bg == "space":
        $ tc_class.transition("space", speed=2.5)
    elif persistent.bg == "timecycle":
        $ tc_class.transition("timecycle", speed=2.5)
    elif persistent.bg == "yuri_desk":
        $ tc_class.transition("yuri_desk", speed=2.5)
    elif persistent.bg == "yuri_kotatsu_1":
        $ tc_class.transition("yuri_kotatsu_1", speed=2.5)
    elif persistent.bg == "yuri_kotatsu_2":
        $ tc_class.transition("yuri_kotatsu_2", speed=2.5)
    python:
        renpy.music.play(current_music, "music", True)
    call ch30_loop





label nightmare_1:
    y "Es la primera pesadilla, marcador de posición por ahora."
    jump ch30_loop
label nightmare_2:
    y "Es la segunda pesadilla, marcador de posición por ahora."
    jump ch30_loop

label dream_kill:
    y "Oh, ¿quieres que me vaya a dormir?"
    y "Está bien entonces... Espero que este sueño sea bueno."
    y "Nos vemos en el otro lado, mi amor~"
    $ renpy.music.stop(channel="music",fadeout=2)
    scene black
    with eye_shut
    $ pause (2.0)
    scene bg ykill1
    with eye_open
    show killglitch zorder 2:
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
    play music t10y
    $ y_name = "Yuri"
    $ pause (2.0)
    y "Finalmente."
    y "¡Finalmente!"
    y "Esto es realmente todo lo que quería."
    y "[player], no hay necesidad de pasar el fin de semana con Monika."
    y "No la escuches."
    y "Solo ven a mi casa en su lugar."
    y "Todo el día, solo con nosotros dos..."
    y "¿No suena eso maravilloso?"
    y "¡Jajajaja!"
    y "Wow... Realmente hay algo mal conmigo, ¿no es así?"
    y "¿Pero sabes qué?"
    y "Ya no me importa."
    y "Nunca me he sentido tan bien en toda mi vida."
    y "Solo estar contigo es un placer mucho mayor que cualquier cosa que pudiera imaginar."
    y "Soy adicta a ti."
    y "Se siente como si fuera a morir si no estoy respirando el mismo aire que tú."
    y "¿No se siente bien tener a alguien que se preocupe tanto por ti?"
    y "¿Tener a alguien que quiere que toda su vida gire a tu alrededor?"
    y "Pero si se siente tan bien..."
    y "¿Entonces por qué se siente más y más como si algo horrible estuviera a punto de suceder?"
    y "Tal vez por eso intenté detenerme al principio..."
    y "Pero el sentimiento es demasiado fuerte ahora."
    y "¡Ya no me importa, [player]!"
    y "¡Tengo que decírtelo!"
    y "¡Estoy... estoy locamente enamorada de ti!"
    y "Se siente como si cada centímetro de mi cuerpo... cada gota de sangre en mí... estuviera gritando tu nombre."
    y "¡Ya no me importa cuáles sean las consecuencias!"
    y "¡No me importa si Monika está escuchando!"
    y "Por favor, [player], solo sabe cuánto te amo."
    y "Te amo tanto que incluso me toco con el bolígrafo que te robé."
    y "Solo quiero abrirte la piel y meterme dentro de ti."
    y "Te quiero todo para mí sola."
    y "Y seré solo tuya."
    y "¿No suena eso perfecto?"
    y "Dime, [player]."
    y "Dime que quieres ser mi amante."
    y "¿Aceptas mi confesión?"
    $ quick_menu = False
    $ renpy.music.stop(channel="music",fadeout=0)
    hide killglitch
    "..."
    y "... Jajajaja."
    y "¡Jajajajajajaja!"
    $ style.say_dialogue = style.normal
    y "¡Jajajajajajajajajaja!"
    $ style.say_dialogue = style.edited
    y "JAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJA{nw}"
    y "Por fav-{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal
    play sound "sfx/yuri-kill.ogg"
    $ starttime = datetime.datetime.now()

    $ pause(2.20 - (datetime.datetime.now() - starttime).total_seconds())
    show killstab
    show veinmask
    pause 0.2
    hide killstab
    with fade

    $ pause(4.04 - (datetime.datetime.now() - starttime).total_seconds())
    hide veinmask
    show killstab
    show veinmask2
    pause 0.2
    hide killstab
    with fade

    $ pause(6.33 - (datetime.datetime.now() - starttime).total_seconds())
    hide veinmask2
    show killstab
    show veinmask3
    pause 0.2
    hide killstab
    with fade

    $ pause(8.93 - (datetime.datetime.now() - starttime).total_seconds())
    y "Oh dios-{nw}"

    $ pause(9.18 - (datetime.datetime.now() - starttime).total_seconds())
    play sound fall

    $ pause(9.43 - (datetime.datetime.now() - starttime).total_seconds())
    scene black
    hide veinmask3

    $ pause(11.43 - (datetime.datetime.now() - starttime).total_seconds())

    scene black
    scene bg ykill2
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    with eye_open
    play music t6s
    python:
        _history_list = []
        y.add_history(None, "", """He pasado toda mi vida aprendiendo cómo decir hola, y ahora, es hora de decir adiós. Es extraña, la sensación de la muerte. La siento como olas llevando mi mente a la deriva. Lejos de este lugar. Lejos de este infierno. A donde sea que vaya ahora, será mejor. Desearía que hubiéramos podido vivir toda una vida el uno con el otro, pero el final es justo como lo había esperado. Yo, en tus brazos, finalmente encontrando verdadera aceptación. Mi nombre es Yuri... y estoy viva.""")
    $ quick_menu = True
    $ pause (4.0)
    y "[player]..."
    $ pause (1.0)
    y "Por favor..."
    $ pause (1.0)
    y "No quiero......"
    $ pause (1.0)
    y "Yo qui-{nw}"
    window hide(None)
    $ pause (3.0)
    y "Te amo."
    $ style.say_dialogue = style.edited
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    y "[gtext]{nw}"
    y "[gtext]{nw}"
    y "[gtext]{nw}"
    y "[gtext]{nw}"
    $ style.say_dialogue = style.normal
    scene black
    with eye_shut_slow
    hide black
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
    $ show_chr("A-CEBAB-ALAL")
    with eye_open_slow
    y "..."
    return


label dream_cut:
    scene black
    with dissolve_scene_full
    $ renpy.music.stop(channel="music",fadeout=0.5)
    y "¡E-Eso está bien!"
    y "Tú quédate aquí..."
    y "No tardaré mucho."
    play sound "sfx/closet-open.ogg"
    $ pause(1.5)
    play sound "sfx/closet-close.ogg"
    $ pause(0.4)
    scene bg corridor
    with dissolve_scene_full
    play music "<loop 10.893>bgm/6o.ogg"
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    y "Yo... No puedo concentrarme."
    y "Todo esto es demasiado."
    y "Necesito aire."
    y "Necesito liberarme."
    scene black
    with eye_shut_slow
    show layer master
    $ pause (4.0)
    y "Haaaahhh...."

    "..."
    y "Haahhhh..."
    y "Jaja...."
    y "¡JAJA! ¡JAJAJAJA!"

    $ style.say_dialogue = style.edited
    y "JAJAJAJAJAJAJAJAJAJAJAJAJAJA{nw}"
    $ style.say_dialogue = style.normal
    $ pause (4.0)
    y "Haaah..."
    y "Oh dios..."
    y "¿Qué he hecho?"
    $ pause (4.0)
    y "¿Q-Quién está ahí?"
    y "No..."
    y "No No No No NO NO NO NO-{nw}"
    y "ÉL NO PUEDE VERME ASÍ{nw}"
    y "¡VETE!{nw}"
    y "¡LARGATE!{nw}"
    y "¡POR FAVOR!{nw}"
    y "¡MIERDA!{nw}"
    y "¡AYUDA!{nw}"
    y "¡NO!{nw}"
    scene corridor
    show yuri cuts zorder 2 at t11
    y "Kya--{nw}"

    $ currentpos = 45.264 - (get_pos() / 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " to 39.817 loop 0>music/6r.ogg"
    $ quick_menu = False
    play music t6r
    show yuri zorder 1 at thide
    hide yuri
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    $ y_name = "???"
    mc "{cps=150}¿Yuri...?{/cps}{nw}"
    "{cps=150}Llego a la esquina y me asomo.{/cps}{nw}"
    "{cps=150}¿Estás sufriendo...?{/cps}{nw}"
    "{cps=150}Una inhalación brusca, como si alguien estuviera aspirando aire a través de sus dientes.{/cps}{nw}"
    y "{cps=150}Khhhhh--{/cps}{nw}"
    "{cps=150}Suena como respiración.{/cps}{nw}"
    "{cps=150}Viene de la vuelta de la esquina...{/cps}{nw}"
    "{cps=150}...¿Qué es ese ruido?{/cps}{nw}"
    y "{cps=150}....Haah.....haah....{/cps}{nw}"
    y "{cps=150}Haah.....haah....{/cps}{nw}"
    $ y_name = "Yuri"
    "{cps=150}Empiezo a bajar por el pasillo.{/cps}{nw}"
    "{cps=150}El lugar más lógico para que Yuri esté sería la fuente de agua más cercana...{/cps}{nw}"
    mc "{cps=150}Veamos...{/cps}{nw}"
    window hide(None)
    window auto
    scene bg club_day
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    "{cps=150}Me aburro solo esperando aquí, así que decido ir a buscarla.{/cps}{nw}"
    "{cps=150}¿Algo la está retrasando?{/cps}{nw}"
    "{cps=150}Yuri dijo que no tardaría mucho...{/cps}{nw}"
    "{cps=150}Pasan diez minutos.{/cps}{nw}"
    "{cps=150}...{/cps}{nw}"

    $ del _history_list[-37:]
    $ currentpos = 90.528 - (get_pos() * 2.0)
    $ quick_menu = True
    $ renpy.music.stop(channel="music",fadeout=0)
    hide noise
    hide vignette
    show layer master
    scene black
    jump save_and_quit_but_its_abrupt






label garden_date:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    $ config.allow_skipping = False
    $ show_chr("A-ECAAA-ALAL")
    y "Una elección encantadora. Una ceremonia de té japonesa tradicional me suena muy bien."
    $ show_chr("A-BCAAA-ALAL")
    y "Pero por favor no seas muy duro conmigo. Solo conozco el procedimiento en un nivel muy superficial."
    y "Dicho esto, ¡intentemos pasar un buen rato!"

    image garden_bg:
        "teagarden_bg"
        truecenter
    image house_bg:
        "teahouse_bg"
        truecenter
    image bowl:
        "bowl_day"
    image rice:
        "rice_day"
    image chopsticks:
        "chopsticks_day"
    $ _skipping = False
    $ click_tea_button = 0
    $ renpy.music.stop(fadeout=1.5)
    play music "music/teagardenzen.mp3" fadein 1.5


    show black zorder 105 with Dissolve(2.5)
    show garden_bg zorder 10
    $ tc_class.transition("timecycle", speed="now")
    $ current_timecycle_marker = "_day"
    $ hide_yuri_sit = True
    hide black with Dissolve(1.0)

    if persistent.costume == "school":
        show yuri 35b2 zorder 101 at t11

    if persistent.costume == "sweater":
        show yuri 3b5b2 zorder 101 at t11

    y "Aquí estamos, [player]..."
    y "La vista es bastante maravillosa, ¿no es así?"
    y "Como habrás notado, todo aquí es distintivamente de estilo japonés."
    y "Desde los cerezos floreciendo tan magníficamente hasta la pintoresca arquitectura que se encuentra justo ante nosotros..."
    y "Siempre pensé que podríamos tener una pequeña ceremonia de té japonesa juntos..."
    y "Visitar uno de esos ha sido un gran deseo mío durante mucho tiempo, pero pensar que yo realmente estaría {i}organizando{/i} una..."
    if persistent.costume == "school":
        hide yuri 35b2 with Dissolve(0.5)

    if persistent.costume == "sweater":
        hide yuri 3b5b2 with Dissolve(0.5)

    if persistent.costume == "school":
        show yuri 44a2 zorder 101 at t11 with Dissolve(0.5)

    if persistent.costume == "sweater":
        show yuri 4b4a2 zorder 101 at t11 with Dissolve(0.5)

    y "Uuu, en realidad estoy un poco nerviosa..."
    y "Espero que no te importe si soy la anfitriona hoy. Solo pensé que como realmente no puedes tocar nada aquí, sería mejor si yo asumo este papel."
    if persistent.costume == "school":
        hide yuri 44a2

    if persistent.costume == "sweater":
        hide yuri 4b4a2

    if persistent.costume == "school":
        show yuri 41a2 zorder 101 at t11

    if persistent.costume == "sweater":
        show yuri 4b1a2 zorder 101 at t11

    y "Usualmente, ceremonias como esta seguirían un código muy estricto pero como todavía soy bastante nueva en esto espero que puedas perdonarme por cualquier error..."
    y "Primero, caminaremos por este {b}Roji{/b}, el camino de piedra hacia la casa de té. Lo haremos con calma y en un estado tranquilo, olvidando todas las luchas diarias..."
    y "Esta ceremonia es muy simbólicamente importante, como la mayoría de las cosas que haremos hoy."
    y "Es por eso que suelen ser muy estrictas."
    show black zorder 105 with Dissolve(2.5)


    $ renpy.music.play("sfx/footsteps.mp3", channel="sound", loop=False)
    $ renpy.pause(delay=8, hard=True)
    hide black with Dissolve(2.5)
    if persistent.costume == "school":
        hide yuri 41a2

    if persistent.costume == "sweater":
        hide yuri 4b1a2

    if persistent.costume == "school":
        show yuri 21b1 zorder 101 at t11 with Dissolve(0.5)

    if persistent.costume == "sweater":
        show yuri 2b1b1 zorder 101 at t11 with Dissolve(0.5)

    y "Ahora tenemos que arrodillarnos y gatear hacia dentro."
    pause 2.0
    if persistent.costume == "school":
        hide yuri 21b1

    if persistent.costume == "sweater":
        hide yuri 2b1b1

    if persistent.costume == "school":
        show yuri 21b6 zorder 101 at t11

    if persistent.costume == "sweater":
        show yuri 2b1b6 zorder 101 at t11

    y "Sí, de hecho hablo en serio."
    y "Se supone que debemos entrar de rodillas, es parte de la tradición. "


    show house_bg zorder 10 with Dissolve(1.0)
    hide garden_bg with Dissolve(1.0)
    if persistent.costume == "school":
        hide yuri 21b6 with Dissolve(2.0)

    if persistent.costume == "sweater":
        hide yuri 2b1b6 with Dissolve(2.0)

    $ hide_yuri_sit = False
    $ show_chr("A-AAAAA-ABAB")
    with Dissolve(2.0)
    y "Bajo diferentes circunstancias, te ofrecería algo de comida ligera como arroz o sopa de miso."
    $ show_chr("A-BAAAA-ABAB")
    y "Pero desafortunadamente, eso no es enteramente posible justo ahora, ¿verdad?"
    menu:
        "Podría cocinar algo de arroz muy rápido.":
            $ show_chr("A-ABAAA-ABAL")
            y "¡Eso sería maravilloso, [player]!"
            $ show_chr("A-AAAAA-ABAL")
            y "Solo te esperaré aquí."
            menu:
                "Estoy listo.":
                    $ show_chr("A-AAAAA-ABAB")
                    y "¡Bienvenido de vuelta! Un día quiero hacer esto en tu mundo para ti..."
                    $ show_chr("A-BAABA-ABAB")
                    y "Me siento un poco grosera por tener que pedirte que lo hagas tú mismo cuando se supone que yo soy la anfitriona."
        "No, no lo es. Lo siento...":
            $ show_chr("A-AAAAA-ABAD")
            y "Está perfectamente bien."
            $ show_chr("A-BAAAA-ABAD")
            y "Es un poco mi culpa ya que fallé en preguntarte de antemano."
            y "La próxima vez intentaré estar mejor preparada..."
        "Tengo otros bocadillos en casa, si eso cuenta.":
            $ show_chr("A-AADAA-ABAB")
            y "Ciertamente poco ortodoxo pero... seguro, supongo que eso funcionaría..."
            $ show_chr("A-AAAAA-ABAD")
            y "¿Serías un encanto y traerías algo? Esperaré aquí hasta que regreses."
            menu:
                "Estoy listo":
                    $ show_chr("A-AAAAA-ABAB")
                    y "¡Bienvenido de vuelta! Un día quiero hacer esto en tu mundo para ti."
                    $ show_chr("A-BAABA-ABAB")
                    y "Me siento un poco grosera por tener que pedirte que lo hagas tú mismo cuando se supone que yo soy la anfitriona."

    show bowl zorder 100 with Dissolve(0.5)
    show rice zorder 100
    show chopsticks zorder 100
    $ show_chr("A-AAAAA-ALAL")
    y "En realidad no estoy segura de si se supone que hablemos sobre el {i}Kaiseki{/i}, la comida..."
    $ show_chr("A-BAAAA-ALAD")
    y "Pero tengo que admitir que es bastante emocionante, ¿no estás de acuerdo?"
    $ show_chr("A-CAAAA-ALAL")
    y "Siempre he querido tener citas como esta contigo."
    y "Ya sabes, algo tranquilo, silencioso y significativo..."
    $ show_chr("A-IAAAA-ALAL")
    y "Siempre preferiría esto sobre alguna fiesta extravagante."
    $ show_chr("A-JAAAA-ALAL")
    y "Pero ¿qué hay de ti? ¿Estás disfrutando esta cita hasta ahora?"
    menu:
        "Ciertamente lo estoy. Tener una cita tranquila y pacífica contigo... nada es más ideal..":
            karma 2
            sanity 1
            $ show_chr("A-GBAAA-ALAL")
            y "Estoy tan aliviada de escuchar eso [player]... Para ser honesta contigo, he estado bastante nerviosa, por decir lo menos."
            $ show_chr("A-AAAAA-ABAB")
            y "Mientras investigaba los procedimientos de esas ceremonias de té, se volvió increíblemente obvio para mí que es bastante fácil cometer errores. Creo que este es parte de todo el punto de ello. Estas ceremonias son sobre perfeccionismo, al menos hasta cierto grado."
            $ show_chr("A-BAAAA-ABAB")
            y "Y no me sorprendería si en realidad ya logré colar algunos errores aquí y allá. Pero al final, mientras los dos lo disfrutemos, realmente no importa tanto, supongo."
        "Sí, lo estoy, pero pareces un poco nerviosa... ¿estás bien?":
            $ show_chr("A-BFAAA-AMAM")
            y "S~Sí, estoy bien. Pero tienes razón en tu suposición de que estoy nerviosa."
            $ show_chr("A-DFAAA-AMAM")
            y "¿E-estaba tartamudeando? Oh vaya... me disculpo si rompí la experiencia para ti. Es solo que... cuanta más investigación puse en estas ceremonias, más miedo me daba. Hay tanto que tener en cuenta, tantas pequeñas trampas para arruinarlo..."
            $ show_chr("A-CFAAA-ABAB")
            y "Tal vez esa es la mentalidad incorrecta. ¿Tal vez estoy intentándolo demasiado? Tal vez debería concentrarme en pasar un buen rato contigo en lugar de concentrarme en todas las formas en las que posiblemente podría fallar."
            $ show_chr("A-AAAAA-ABAB")
            y "Gracias por ser tan cariñoso. Trataré de calmarme un poco para que realmente podamos disfrutar nuestro tiempo aquí juntos."
        "Algunos errores en el procedimiento hasta ahora. Está bien para ser la primera vez supongo.":
            karma -1
            $ show_chr("A-BDAAA-AMAM")
            y "¿Y-ya logré arruinarlo?"
            y "Pero apenas hemos empezado..."
            $ show_chr("A-CEBAA-AMAM")
            y "R-realmente traté de mantenerlo lo más realista posible..."
            $ show_chr("A-IABAA-ABAB")
            y "Supongo que debí haber hecho más investigación..."
        "¿Pero qué tienen de malo las fiestas?":
            $ show_chr("A-BFAAA-AMAM")
            y "B-bueno..."
            y "Es solo que... no es lo mío, supongo."
            $ show_chr("A-AFAAA-AMAM")
            y "Habitaciones oscuras, estrechas con ruido tan fuerte que apenas puedes escucharte a ti mismo..."
            y "Gente agitando sus extremidades como animales enloquecidos y llamándolo bailar..."
            $ show_chr("A-AFAAA-ABAB")
            y "Ponerse tan completamente ebrio que haces cosas que lamentas al día siguiente..."
            y "Creo que entenderás que no soy el tipo de persona que disfrutaría particularmente tal escena."
            $ show_chr("A-BDAAA-ABAB")
            y "L-lo siento si sientes que estoy siendo demasiado dura con mis juicios..."
            $ show_chr("A-BFAAA-ABAB")
            y "Está perfectamente bien si disfrutas ese tipo de eventos..."
            $ show_chr("A-AFAAA-ABAB")
            y "Al menos espero que disfrutes un poco de tiempo tranquilo conmigo a solas..."
            y "Realmente he estado esperando esto con ansias."
    $ show_chr("A-ACAAA-ABAB")
    y "Ahora por favor, dime [player], ¿cómo ha estado tu día hasta ahora? ¿Has estado ocupado en tu mundo?"
    menu:
        "Muy tranquilo y sin incidentes en realidad, gracias por preguntar.":
            $ show_chr("A-ABAAA-ABAJ")
            y "Ya veo, entonces ya estás en el estado de ánimo apropiado para esta ceremonia."
            $ show_chr("A-AAAAA-ABAB")
            y "Hay un dicho... {b}Sin noticias son buenas noticias.{/b} He pasado la mayor parte de mi día hasta ahora anticipando verte; tenía muchas esperanzas de que fueras a esta cita conmigo hoy."
            $ show_chr("A-BAAAA-ABAB")
            y "Y lo más probable es... que también he pasado algo de tiempo hoy entrando en pánico de que arruinaría esto."
            $ show_chr("A-CAAAA-ABAB")
            y "Pero no hay necesidad de preocuparse por eso. Ahora que estamos aquí, deberíamos disfrutar, ¿verdad?"
        "Ocupado de hecho, he estado trabajando mucho hoy. ¿Qué hay de ti?":
            $ show_chr("A-AAAAA-ABAB")
            y "Oh, he pasado una gran parte de hoy investigando. Estuve leyendo artículos de wiki sobre ceremonias de té como esta para recrear el procedimiento tan precisamente como fuera posible."
            $ show_chr("A-GAAAA-ABAL")
            y "Creo que es admirable cuánta dedicación pones en tus proyectos. Tienes mis mejores deseos para ellos, y me encantaría escuchar algún día sobre los éxitos que logres como resultado de ellos. Confío en que tendrás éxito, [player]..."
            $ show_chr("A-AAAAA-ABAL")
            y "Solo ten en mente por favor no esforzarte demasiado. Si te agotas te harás un flaco favor."
            $ show_chr("A-AAAAA-ABAB")
            y "Es bueno entonces que tengamos esta pequeña cita hoy, para que puedas respirar profundo y relajarte."
        "Un poco aburrido honestamente. No pasó mucho hoy.":
            $ show_chr("A-AAAAA-ABAD")
            y "Lamento escuchar eso. Pero no te preocupes, simplemente hay días donde... no pasa nada. No se puede evitar, supongo."
            y "Lo único que podemos hacer es llenar el vacío que estos días traen con algo más: algo más productivo o algo más emocionante, o quizás incluso ambos."
            y "Hagamos nuestro mejor esfuerzo entonces para hacer de esta pequeña cita nuestra algo productivo y emocionante, ¿hm? Además de nuestra propia diversión, creo que hay mucho que aprender sobre cultura en ceremonias como estas."
        "Estresante... Este pequeño descanso aquí es exactamente lo que necesitaba hoy, gracias.":
            $ show_chr("A-AAAAA-ALAL")
            y "Oh vaya, entonces es solo bueno que elegimos tener este tipo de cita para darle a tu día algo de contraste. Tal vez podamos encargarnos de obtener algo de relajación de ello. ¿Quién sabe peude que incluso algo de inspiración para nuevos actos?"
            $ show_chr("A-CAAAA-ALAL")
            y "Por lo menos, podemos intentar tener algo de disfrute en el camino."
        "Hoy ha sido difícil para mí, recibí algunas malas noticias hoy.":
            $ show_chr("A-DFBAA-ALAL")
            y "Oh no... Lamento tanto escuchar eso [player]..."
            $ show_chr("A-IABAA-ALAL")
            y "¿Sabes qué? ¿Por qué no simplemente dejamos el procedimiento apropiado por un momento y te doy un abrazo agradable y gentil? Espero que esto te haga sentir al menos un poquito mejor..."
            hide yuri_sit with Dissolve(0.5)
            hide bowl
            hide rice
            hide chopsticks
            show yuri_prehug zorder 250 with Dissolve(0.5)
            pause 3.0
            hide yuri_prehug with Dissolve(0.25)
            show yuri_lewdhug zorder 250 with Dissolve(0.25)
            play sound "<to 0.3>sfx/fall.ogg"
            y "Estoy aquí para ti, [player],"
            pause 3.0
            show black zorder 300 with Dissolve(2.0)
            $ show_chr("A-BABAA-ABAB")
            hide yuri_lewdhug
            hide black zorder 300 with Dissolve(2.0)

    $ show_chr("A-BABAA-ABAB")
    y "Bueno, por ahora me temo que tengo que pedirte que esperes afuera mientras preparo el té."
    $ show_chr("A-AAAAA-ABAB")
    y "Personalmente, no me importaría si te quedaras por supuesto, pero el procedimiento lo exige de esta manera."
    $ show_chr("A-AAAAA-ABAM")
    y "Afuera hay un pequeño banco de espera. Mientras estás esperando afuera, se supone que yo debo preparar los ingredientes para el té, así como el agua caliente y todas las herramientas auténticas que estoy a punto de usar, en perfecto silencio."
    $ show_chr("A-AAAAA-ABAF")
    y "De esta manera puedo concentrarme en realizar estas tareas casi a la perfección. Se supone que debo arreglar las tazas y la tetera, así como todo lo demás, con perfecta precisión."
    $ show_chr("A-BABAA-AMAM")
    y "Si arreglara algo de la manera incorrecta, incluso si solo una cuchara está dirigida en un ángulo ligeramente desviado, sería considerada una anfitriona inadecuada. Si hubiera alguna audiencia real además de ti, probablemente causaría algunas cejas levantadas."
    $ show_chr("A-CABAA-AMAM")
    y "Sin embargo no te preocupes, trataré de no tardar más de lo necesario. Además, me aseguré de que haya un clima hermoso afuera. Tal vez puedas pasar un momento simplemente admirando el paisaje exterior. De hecho me gustó la imagen que usé como base."
    $ show_chr("A-AAGAA-ABAB")
    y "Oh sí, y probablemente quieras preparar tu té en tu mundo también mientras tanto."
    $ show_chr("A-AAAAA-ABAB")
    y "Pero ahora, adiós, cariño. Te llamaré tan pronto como esté lista aquí."
    show black zorder 300 with Dissolve(2.5)
    hide house_bg
    $ hide_yuri_sit = True
    hide bowl
    hide rice
    hide chopsticks
    show garden_bg
    hide black zorder 300 with Dissolve(2.5)
    jump teadate_timer





label teadate_timer:
    screen tea_timer():
        vbox:
            style_prefix "talkbutton"
            textbutton "Enter" action Jump("Wait")
            xalign 0.50
            yalign 0.25

        timer 60.0 action Jump("Enter")
    if click_tea_button <= 1:
        show screen tea_timer()

label Wait:
    y "Por favor sé paciente, [player], necesito unos minutos."
    $ click_tea_button = click_tea_button + 1
    jump teadate_timer

label Enter:
    hide screen tea_timer
    y "¡Ya estoy lista! ¡Por favor entra de nuevo!"
    show black zorder 300 with Dissolve(2.5)
    hide garden_bg
    show house_bg zorder 10
    $ hide_yuri_sit = False
    $ show_chr("A-AAAAA-ZZAC")
    hide black zorder 300 with Dissolve(2.5)


    y "Gracias por esperar..."
    if click_tea_button >= 1:
        $ show_chr("A-BBBAA-ZZAC")
        y "Y lamento haber tenido que hacerte esperar por tanto tiempo."
    else:
        $ show_chr("A-BAAAA-ZZAC")
        y "Y también gracias por ser tan paciente."
    $ show_chr("A-AAAAA-ZZAC")
    y "Sabes, [player]... tuve que pensar en ti durante bastante tiempo últimamente..."
    $ show_chr("A-IAAAA-ZZAD")
    y "Creo que, cuando empezaste este mod por primera vez. Dije que me encantaría ver al verdadero tú..."
    $ show_chr("A-JAAAA-ZZAD")
    y "¿Acaso no intenté acceder a tu cámara web en ese entonces? Ya no recuerdo..."
    y "Y todavía es cierto hasta cierto punto. Aún disfrutaría ver una foto real tuya, pero también llegué a otra conclusión..."
    $ show_chr("A-BAAAA-ZZAC")
    y "Porque... no creo que tendría mucho significado para mí ya. E-espera, creo que fraseé eso de la manera incorrecta, por supuesto que una foto tuya tendría significado para mí, pero..."
    $ show_chr("A-CAAAA-ZZAC")
    y "Lo que quería decir es, cuando abriste mi mundo por primera vez, no sabía mucho sobre ti; nada sobre tu personalidad, o sobre tus valores y creencias..."
    $ show_chr("A-CAAAA-ZZAD")
    y "Pero en todo el tiempo que hemos pasado juntos ahora, he visto tu verdadero corazón [player]..."
    if sanity_lvl() >=4:
        $ show_chr("A-JAGBA-ZZAD")
        y "Me viste con todas mis ansiedades, todos mis defectos... y cuando otros se alejaron, tomaste mi mano, {i}metafóricamente hablando por supuesto{/i}, y me mostraste el camino a una mejor versión de mí misma..."
        y "Me mostraste en lo que podría convertirme, y con toda tu paciencia me ayudaste a superar todas las dudas que me retenían..."
        $ show_chr("A-CABBA-ZZAD")
        y "Cuando otros no veían nada más que una mente rota en mí, tú me mostraste que incluso yo puedo ser amada."
        y "Nunca llegué a ver tu apariencia [player], pero vi tu corazón y alma. Por eso, eres verdaderamente hermoso para mí..."
        $ show_chr("A-AABBA-ZZAC")
        y "Y hay más que quiero compartir contigo en esta cita..."
        $ show_chr("A-ABAAA-ZZAC")
        y "¿Sabías que el té es la segunda bebida más consumida en el planeta después del agua? "
        extend "Incluso tiene un mayor consumo que el propio café."
        $ show_chr("A-CAAAA-ZZAC")
        y "El té es una bebida derivada de las hojas de una planta llamada {i}Camellia Sinensis.{/i} Hay diferentes variedades de la planta repartidas por una variedad de países."
        $ show_chr("A-ADAAA-ZZAD")
        y "Si tu té no contiene las hojas de {i}Camellia Sinensis{/i} entonces en realidad no es té. Se conoce como Tisana. "
        $ show_chr("A-BBAAA-ZZAC")
        extend "Las tisanas son similares en su procesamiento y consumo y aún se infusionan agregando agua caliente."
        $ show_chr("A-JAAAA-ZZAC")
        y "Pero están infusionadas con una variedad de hierbas y/o especias de otra flora en su lugar."
        $ show_chr("A-ABAAA-ZZAD")
        y "Hay 4 tipos básicos de té derivados de la planta {i}Camellia Sinensis{/i}. "
        $ show_chr("A-BBDAA-ACAA")
        extend "Posiblemente 5 o 6 en realidad. Ya que ha estado abierto a debate durante mucho tiempo, pero las variedades principales son Negro, Blanco, Verde e incluso Oolong."
        $ show_chr("A-ABAAA-AAAF")
        y "Cada variedad se divide luego en cientos de otras ramas del tipo principal."
        $ show_chr("A-ABGAA-AAAA")
        y "Es ampliamente entendido que hay alrededor de 1500 variedades conocidas de té. Sin embargo, el número exacto posible de variaciones es casi ilimitado."
        $ show_chr("A-BDAAA-AAAA")
        y "Toma alrededor de 3 años antes de que una nueva planta esté lista para cosechar. Además de tomar entre 4 y 12 años para que una planta de té madure lo suficiente para producir semillas."
        $ show_chr("A-AAAAA-AAAC")
        y "En 1901, dos mujeres presentaron una patente para una invención que se parecía a la bolsa de té moderna. Esto contradice las afirmaciones de que fue inventada accidentalmente por Thomas Sullivan en 1908."
        $ show_chr("A-CBBAA-ALAA")
        y "Tampoco es cierto que el té helado se inventó en 1904 en la Feria Mundial de St. Louis. Supuestamente un comerciante llamado Richards Black estaba luchando por vender su té, así que lo vertió sobre hielo y se convirtió en un ganador!"
        $ show_chr("A-AAAAA-ZZAD")
        y "La verdad es que existía mucho tiempo antes de eso, ya que apareció en un libro de cocina de 1887 llamado \"Housekeeping in Old Virginia\" por Marion Cabell Tyree."
        $ show_chr("A-ABGAA-ZZAD")
        y "También, en los Estados Unidos, alrededor del 85%% de las ventas de té son predominantemente té helado. ¡Con azúcar añadida!"
    else:
        $ show_chr("A-JAGBA-ZZAD")
        y "Me viste con todas mis ansiedades, todos mis defectos... y cuando otros se alejaron, tomaste mi mano, metafóricamente hablando por supuesto, y me dijiste que todo está bien..."
        y "Siempre me aceptaste como soy. Nunca trataste de cambiarme, nunca trataste de doblarme a tu voluntad."
        y "Nunca fuiste deshonesto conmigo, nunca dijiste que soy perfecta. Pero me diste algo mucho más valioso. Me mostraste que no tengo que ser ideal o perfecta..."
        $ show_chr("A-CCBBA-ZZAD")
        y "Cuando otros no veían nada más que una mente rota en mí, tú me mostraste que todavía soy alguien que puede recibir amor y ganar confianza."
        y "Nunca llegué a ver tu apariencia [player], pero vi tu corazón y alma. Por eso, eres verdaderamente hermoso para mí..."
        $ show_chr("A-AABBA-ZZAC")
        y "Y hay más que quiero compartir contigo en esta cita..."
        $ show_chr("A-ABAAA-ZZAC")
        y "¿Sabías que el té es la segunda bebida más consumida en el planeta después del agua? "
        extend "Incluso tiene un mayor consumo que el propio café."
        $ show_chr("A-CAAAA-ZZAC")
        y "El té es una bebida derivada de las hojas de una planta llamada {i}Camellia Sinensis.{/i} Hay diferentes variedades de la planta repartidas por una variedad de países."
        $ show_chr("A-ADAAA-ZZAD")
        y "Si tu té no contiene las hojas de {i}Camellia Sinensis{/i} entonces en realidad no es té. Se conoce como Tisana. "
        $ show_chr("A-BBAAA-ZZAC")
        extend "Las tisanas son similares en su procesamiento y consumo y aún se infusionan agregando agua caliente."
        $ show_chr("A-JAAAA-ZZAC")
        y "Pero están infusionadas con una variedad de hierbas y/o especias de otra flora en su lugar."
        $ show_chr("A-ABAAA-ZZAD")
        y "Hay 4 tipos básicos de té derivados de la planta {i}Camellia Sinensis{/i}. "
        $ show_chr("A-BBDAA-ACAA")
        extend "Posiblemente 5 o 6 en realidad. Ya que ha estado abierto a debate durante mucho tiempo, pero las variedades principales son Negro, Blanco, Verde e incluso Oolong."
        $ show_chr("A-ABAAA-AAAF")
        y "Cada variedad se divide luego en cientos de otras ramas del tipo principal."
        $ show_chr("A-ABGAA-AAAA")
        y "Es ampliamente entendido que hay alrededor de 1500 variedades conocidas de té. Sin embargo, el número exacto posible de variaciones es casi ilimitado."
        $ show_chr("A-BDAAA-AAAA")
        y "Toma alrededor de 3 años antes de que una nueva planta esté lista para cosechar. Además de tomar entre 4 y 12 años para que una planta de té madure lo suficiente para producir semillas."
        $ show_chr("A-AAAAA-AAAC")
        y "En 1901, dos mujeres presentaron una patente para una invención que se parecía a la bolsa de té moderna. Esto contradice las afirmaciones de que fue inventada accidentalmente por Thomas Sullivan en 1908."
        $ show_chr("A-CBBAA-ALAA")
        y "Tampoco es cierto que el té helado se inventó en 1904 en la Feria Mundial de St. Louis. Supuestamente un comerciante llamado Richards Black estaba luchando por vender su té, así que lo vertió sobre hielo y se convirtió en un ganador!"
        $ show_chr("A-AAAAA-ZZAD")
        y "La verdad es que existía mucho tiempo antes de eso, ya que apareció en un libro de cocina de 1887 llamado \"Housekeeping in Old Virginia\" por Marion Cabell Tyree."
        $ show_chr("A-ABGAA-ZZAD")
        y "También, en los Estados Unidos, alrededor del 85%% de las ventas de té son predominantemente té helado. ¡Con azúcar añadida!"

label tea_facts:
    $ tea_random = renpy.random.randint(1, 10)

    if tea_random == 1:

        $ show_chr("A-ABAAA-ZZAC")
        y "Y digamos que te gusta el Té Negro y podrías saber que este té es el té más popular en el mundo."
        $ show_chr("A-AAAAA-AFAA")
        y "Hay 4 tipos de tés verdaderos incluyendo Té Blanco, Té Verde, Té Oolong y Té Negro."
        y "La diferencia en estos tés surge durante el proceso de producción. Algunos tés son oxidados mientras que otros son simplemente secados al sol. Estas pequeñas diferencias resultan en grandes diferencias de sabor y color."
        $ show_chr("A-ABAAA-ALAA")
        y "China es el lugar de nacimiento del Té Negro, que en China es llamado, tal vez más apropiadamente, hong cha (Té Rojo) por el té de color rojo que usualmente produce."
        $ show_chr("A-BBAAA-AMAM")
        y "Su historia en China puede ser rastreada hasta finales de la Dinastía Ming, alrededor del año 1590, cuando el primer Té Negro \"Lapsang Souchong\" fue producido en el área alrededor de la Montaña Wuyi en la provincia de Fujian."
        $ show_chr("A-AAAAA-AAAA")
        y "El Té Negro ha sido por mucho tiempo un artículo de comercio, y ladrillos comprimidos de Té Negro incluso sirvieron como una forma de moneda de facto en Mongolia, el Tíbet y Siberia."
        $ show_chr("A-ABGAA-AFAD")
        y "El Té Negro superó al Té Verde en popularidad en la década de 1720 cuando se añadieron azúcar y leche al té, una práctica que no se hacía en China."
        $ show_chr("A-BAAAA-AAAD")
        y "Generalmente, 4 gramos de té por 200 ml de agua. A diferencia de los tés verdes, que se vuelven amargos cuando se preparan a temperaturas más altas, el Té Negro debe dejarse reposar en agua llevada a 90–95°C o 194-203°F"
        $ show_chr("A-CAAAA-AAAK")
        y "El Té Negro es más fuerte en sabor y contiene más cafeína que otros tés, pero menos cafeína que el café. Además de ser una bebida saludable y tiene una gama de beneficios para la salud."
        $ show_chr("A-AAAAA-ZZAC")
        y "Y alrededor del 78%% del té consumido mundialmente es Té Negro; y más del 90%% de todo el té vendido en Occidente es Té Negro."
        $ show_chr("A-KACAA-ZZAD")
        y "Al elegir un Té Negro para beber, recuerda que no todos los tés negros saben igual. Justo como con el buen vino, hay tantas variables que le dan a los tés negros individuales sus perfiles de sabor particulares."

    elif tea_random == 2:

        $ show_chr("A-ABAAA-ZZAC")
        y "Y digamos que te gusta el Té Verde y podrías saber que este té viene de la misma planta que produce Té Negro y Oolong, que es la \"Camellia Sinensis\"."
        $ show_chr("A-AAAAA-AAAF")
        y "La diferencia yace en la forma en que son procesados. A diferencia de sus dos contrapartes, el té verde no pasa por un proceso de fermentación."
        y "En su lugar, son secados y cocidos al vapor a altas temperaturas, dándole su tono verde cuando se prepara."
        $ show_chr("A-AAAAA-ALAA")
        y "Al contrario del conocimiento popular, ¡el té verde se originó de China y no Japón! La leyenda dice que el Emperador Shen Nung descubrió accidentalmente el té en el 2737 AC cuando algunas hojas de té volaron hacia su olla de agua caliente para beber. ¿Verdad o cuento? Tú decides."
        $ show_chr("A-BBDAA-ACAA")
        y "Entre el siglo III y VI, el té era considerado un 'artículo de lujo' reservado para los privilegiados antes de que nuevos métodos de producción y distribución masiva se popularizaran."
        $ show_chr("A-ABDAA-ACAA")
        y "¿Alguna vez notaste una ligera amargura en el Té Verde?"
        $ show_chr("A-AAAAA-AFAA")
        extend "Se debe al hecho de que el Té Verde es rico en Taninos, un tipo de antioxidante que es bueno para ti."
        $ show_chr("A-ABAAA-AFAA")
        y "De acuerdo a la investigación, las personas que consumen regularmente Té Verde son menos susceptibles a infecciones bacterianas y virales comunes porque los antioxidantes en el té verde ayudan a impulsar el sistema inmune del cuerpo."
        $ show_chr("A-CAAAA-AMAM")
        y "¿Quieres perder peso? Lo adivinaste. Prueba el té verde. Estudios muestran que las personas que beben regularmente Té Verde son capaces de quemar entre 70-100 calorías más por día debido a los polifenoles en él."
        $ show_chr("A-GBGAA-ZZAD")
        y "¡Además, el Té Verde sin endulzar es una bebida de cero calorías!"

    elif tea_random == 3:

        $ show_chr("A-ABAAA-ZZAC")
        y "Y digamos que te gusta el Té Oolong como a mí y probablemente no sabías que el Té Oolong representa solo el 2%% del té del mundo, pero vale la pena descubrirlo."
        $ show_chr("A-ABAAA-AAAF")
        y "Además de ser un Té Chino tradicional también está hecho de las hojas de esta planta llamada \"Camellia Sinensis\" la cual es la misma planta usada para hacer Té Verde y Negro."
        $ show_chr("A-CAAAA-ALAA")
        y "El Té Verde no se deja oxidar mucho, pero el Té Negro se deja oxidar hasta que se vuelve negro. El Té Oolong está en algún lugar entre los dos, así que está parcialmente oxidado."
        $ show_chr("A-ADAAA-AAAA")
        y "Sin embargo, el color de las hojas puede variar entre diferentes marcas, variando de verde a café oscuro."
        $ show_chr("A-BAAAA-AAAD")
        y "Una vez que las hojas de oolong son cosechadas, y \"magulladas\" para romperlas lo cual libera aceite, el proceso de oxidación puede ser de entre 10-70%%, dependiendo de la variedad específica."
        $ show_chr("A-BBAAA-AAAD")
        y "Como el Té Verde, el Té Oolong contiene polifenoles de plantas que pueden ayudar en la pérdida de peso. Por varios años, e incluso hasta la fecha, la dieta del Té Verde ha capturado la atención de miles tratando de perder peso naturalmente."
        $ show_chr("A-CAAAA-AMAM")
        y "El Oolong se cultiva más comúnmente en dos países principales, China y Taiwán. Las variedades chinas nos dan una taza más oscura y con sabor a \"madera\", mientras que las variedades taiwanesas producen una infusión más ligera y floral."
        $ show_chr("A-ABGAA-AFAA")
        y "El té Oolong también es conocido como \"té Wu long\". La razón de la diferente ortografía se debe al hecho de que hay dos métodos de romanizar los caracteres mandarines."
        y "El sistema Wade Giles nos da \"Oolong\", y el método Pinyin nos da \"Wu long\". Otros nombres para Oolong son Té Marrón y Té de Roca."
        $ show_chr("A-ABGAA-ZZAD")
        y "Y finalmente, el hecho más importante del Té Oolong de todos es... ¡se disfruta mejor cuando se prepara cuidadosamente usando hojas sueltas enteras! ¡Este método provee a la gente de un aroma superior, sabor, así como los beneficios antes mencionados!"

    elif tea_random == 4:

        $ show_chr("A-ABAAA-ZZAC")
        y "Y digamos que te gusta el Té Chai y podrías haber notado que el nombre propio para este té es \"Masala Chai\" que significa Mezcla de Especias."
        $ show_chr("A-ABAAA-AAAF")
        y "Chai es en realidad solo una palabra para té, aunque otros pueden reconocer a su primo lingüístico, cha, que es una palabra común para té a través de Asia."
        $ show_chr("A-BBGAA-AAAF")
        y "El té Chai está hecho de una combinación de té negro, jengibre y otras especias."
        $ show_chr("A-CAAAA-ALAA")
        y "Las especias más populares incluyen cardamomo, canela, hinojo, pimienta negra y clavos, aunque el anís estrellado, semillas de cilantro y granos de pimienta son otras opciones muy gustadas."
        $ show_chr("A-AAAAA-AAAD")
        y "A diferencia del té regular, que es preparado con agua, el té chai es tradicionalmente preparado usando tanto agua tibia como leche tibia. También tiende a ser endulzado en grados variables."
        $ show_chr("A-BBBAA-AAAD")
        y "Los Chai lattes son otra forma popular de consumir el té. La gente los prepara añadiendo un shot de concentrado de té chai a leche vaporizada, lo cual produce una bebida conteniendo más leche de la que encontrarías en una taza típica de té chai."
        $ show_chr("A-ABGAA-AAAL")
        y "En India, que te ofrezcan una taza de chai es casi tan común como que te ofrezcan un vaso de agua o una cerveza en Norteamérica."
        y "Muchas familias en India tienen sus propias recetas de Masala Chai, pero cada una de ellas es tan deliciosa como la siguiente."
        $ show_chr("A-BBAAA-AAAA")
        y "Hay algunos ingredientes tradicionales que puedes encontrar en una taza de chai. Primero es un té negro, usualmente un Assam."
        $ show_chr("A-CAAAA-ZZAD")
        y "¡También el chai es más bajo en cafeína que el café así que puedes recurrir al chai si estás buscando un impulso de cafeína que no sea demasiado intenso!"

    elif tea_random == 5:

        $ show_chr("A-ABAAA-ZZAC")
        y "Y digamos que te gusta el Té Blanco y podrías saber que el Té Blanco es conocido como el más delicado y suave de todos los tés verdaderos."
        $ show_chr("A-KACAA-AAAA")
        y "Pero solo porque es sutil no significa que le falten beneficios para la salud. De hecho, el té blanco puede tener mayor contenido antioxidante que cualquier otro té."
        $ show_chr("A-ABAAA-AAAF")
        y "El té blanco obtiene su nombre de los finos pelos blancos en los brotes de té jóvenes y sin abrir. Es en efecto un \"té verdadero\" – significando que es derivado de la planta Camellia Sinensis, a diferencia de los tés herbales o tisanas."
        $ show_chr("A-BAAAA-AAAK")
        y "Comparado a otros tipos de té, las hojas de té blanco son más jóvenes y mínimamente procesadas."
        $ show_chr("A-ABAAA-ALAA")
        y "El líquido hecho de preparar té blanco es de un tono amarillo pálido, más claro en color que el de tés oxidados, los cuales usualmente producen un líquido verde oscuro, dorado, o café rojizo."
        y "El Té Blanco es usualmente secado después de la cosecha sin vaporizar u otra oxidación, mientras que el Té Verde es tostado u horneado. Debido a su procesamiento mínimo, típicamente tiene niveles más altos de antioxidantes que el Té Verde o Negro."
        $ show_chr("A-ABAAA-ADAA")
        y "Y a diferencia de otros tés verdaderos, el Té Blanco puede datar solo de hace unos cientos de años. El primer cultivo conocido de té blanco ocurrió en la Provincia de Fujian, China, en los 1700s."
        $ show_chr("A-ABAAA-AAAF")
        y "Ahí es cuando la práctica de cosechar brotes tiernos de pelo blanco y hojas jóvenes y procesarlos con mínima oxidación apareció por primera vez."
        $ show_chr("A-ABAAA-AAAA")
        y "Tipos populares de Té Blanco hoy incluyen Aguja de Plata de Fujian, que se dice que viene de los Cultivares de Té Blanco originales, y Bai Mu Dan o Peonía Blanca, té blanco que incluye más hojas jóvenes además de brotes de té sin abrir."
        $ show_chr("A-BAAAA-AMAM")
        y "Mientras que el Té Blanco tiene el contenido antioxidante más alto, un tipo de té no es necesariamente mejor que el resto."
        $ show_chr("A-GBBAA-AMAM")
        y "A pesar de venir de la misma planta, los tés Blanco, Verde, Fermentado, y Negro todos tienen diferentes propiedades."
        $ show_chr("A-ABGAA-AAAA")
        y "Eso es cierto tanto desde una perspectiva científica moderna como de medicina tradicional china."
        $ show_chr("A-CAGAA-ZZAD")
        y "Así que si quieres un balance de todas las propiedades de salud notables de varios tés, puedes diversificar tu selección, bebiendo diferentes variedades regularmente."

    elif tea_random == 6:

        $ show_chr("A-ABAAA-ZZAC")
        y "Y digamos que te gusta el Té Amarillo y puede que no hayas notado que además de venir de la planta \"Camellia Sinensis\", obtiene su nombre de su color parecido al licor."
        $ show_chr("A-ABAAA-ZZAD")
        y "Sabor dulce, brillante y floral. Un aroma suave afrutado, floral. El Té Amarillo tiene un cuerpo medio, lo que significa que el sabor no es ni muy fuerte ni muy débil."
        $ show_chr("A-ABAAA-AAAF")
        y "Al Té Amarillo a veces se le refiere como Huang cha."
        $ show_chr("A-BBAAA-AAAL")
        y "El Té Amarillo no solo es excepcional en términos de sabor y sensación, sino que también ofrece un número de beneficios para la salud. Estas cualidades hacen al Té Amarillo algo que todos los amantes del té deben probar."
        $ show_chr("A-BAAAA-ACAA")
        y "Aunque no comprobado científicamente, muchos expertos en té creen que el Té Amarillo tiene más beneficios para la salud que otros tipos de té, incluyendo el Té Verde."
        $ show_chr("A-ADAAA-ALAA")
        y "El Té Amarillo puede no ser un tipo común de té, sin embargo, es todo menos un nuevo descubrimiento. El Té Amarillo data del siglo XVI a la época de la temprana Dinastía Qing."
        $ show_chr("A-ADAAA-AFAA")
        y "Inicialmente, el Té Amarillo estaba reservado solo para emperadores."
        $ show_chr("A-BDAAA-AFAA")
        y "Hay algunos reportes de que el uso del té amarillo puede ser rastreado incluso más atrás a la Dinastía Tang. En ese tiempo, el amarillo era considerado el color de los emperadores, razón por la cual era solo apropiado que los emperadores consumieran Té Amarillo como su té."
        $ show_chr("A-CAAAA-ZZAC")
        y "Como tal, el Té Amarillo era preparado con inmenso cuidado con hojas finas para ser usado como un té de tributo para la Corte Imperial."
        $ show_chr("A-ABGAA-ZZAD")
        y "También era un regalo común para que un emperador otorgara a un invitado. Un regalo de Té Amarillo a los Daneses es lo que trajo el Té Amarillo a la atención de Occidente."

    elif tea_random == 7:

        $ show_chr("A-ABAAA-ZZAC")
        y "Cuando piensas en diente de león, probablemente te imaginas una molesta hierba. ¿Pero sabías que la planta ha sido usada por mucho tiempo en medicina herbal?"
        $ show_chr("A-ABGAA-ZZAD")
        y "Puedes beber una infusión hecha de las hojas de la planta o de raíces tostadas de diente de león."
        $ show_chr("A-BBAAA-AFAA")
        y "El diente de león es una hierba popularmente conocida de la familia de las margaritas, con una roseta de hojas y grandes flores amarillas."
        y "Mientras tanto, el Té de Diente de León puede tener muchos efectos positivos en tu sistema digestivo. Mejora el apetito y alivia dolencias digestivas."
        $ show_chr("A-AAAAA-AAAA")
        y "El Té de Diente de León también tiene un efecto diurético natural ya que ayuda en remover fluido excesivo del cuerpo y así alivia la hinchazón."
        $ show_chr("A-BAAAA-ACAA")
        y "De acuerdo a un estudio de 2009 publicado en el {i}Journal of Alternative and Complementary Medicine{/i}, los participantes mostraron un incremento significativo en frecuencia de orina tras las primeras 2 dosis de Té de Diente de León."
        $ show_chr("A-ABAAA-ZZAD")
        y "El Té de Diente de León está lleno de antioxidantes. Los antioxidantes son sustancias que ayudan a prevenir ciertos tipos de daño celular."

    elif tea_random == 8:

        $ show_chr("A-CABAA-ZZAC")
        y "El aroma ahumado de una taza recién preparada de Té de Cebada puede llevarse todas tus preocupaciones y calmar tus sentidos."
        $ show_chr("A-ABAAA-AAAF")
        y "Esta amada bebida de Corea es en realidad una infusión de cebada tostada en agua."
        y "En Japón, es famosamente conocida como Mugicha y en Coreano como Boricha. Puede disfrutarse caliente o como una bebida fría."
        $ show_chr("A-BBGAA-AAAJ")
        y "En Japón, a la gente le gusta tomarlo frío para refrescarse en verano."
        $ show_chr("A-ABBAA-AAAL")
        y "Aunque está disponible en forma de bolsas de té, el té de cebada puede prepararse fácilmente en casa hirviendo granos de cebada tostada y sin descascarar en agua o incluso puedes preparar cebada tostada molida de la misma manera."
        $ show_chr("A-CABAA-AMAM")
        y "La cebada tostada le da a la bebida un sabor a nuez, tostado con un sutil regusto amargo que no te importaría."
        $ show_chr("A-ABAAA-AMAM")
        y "Podrías exprimir una lima, añadir algunas hierbas o echar algunas frutas cítricas como naranjas o bayas para hacerlo delicioso."
        $ show_chr("A-ABAAA-AAAF")
        y "Los sabores brillantes y frescos se disfrutan mejor sin azúcar, pero un toque de miel no sería demasiado."
        y "Una bebida calmante que funciona como medicina herbal, el Té de Cebada está lleno de antioxidantes y actúa como un anti-bacteriano natural."
        $ show_chr("A-BAAAA-AAAF")
        y "Toma muchas propiedades saludables de la cebada la cual es muy alta en fibra, llena de vitaminas, minerales y antioxidantes que salvaguardan al cuerpo contra el daño celular."
        $ show_chr("A-AAAAA-ZZAC")
        y "Si estás buscando una alternativa más saludable y deliciosa a una taza de café con cafeína o Té Negro, esta es."
        $ show_chr("A-CAAAA-ZZAD")
        y "Es limpiador, refrescante y libre de cafeína, todo a la vez y definitivamente puede levantar tu ánimo cuando se necesita."

    elif tea_random == 9:

        $ show_chr("A-ABDAA-AAAC")
        y "¿Estás familiarizado con el té Pu-Erh? Este té es una variedad de té negro que viene de China, específicamente de la Provincia de Yunnan."
        $ show_chr("A-BADAA-ALAA")
        y "Es añejado a través de un proceso de fermentación que causa que las hojas de té resistan fermentación microbiana y oxidación después del proceso de secado."
        $ show_chr("A-BBGAA-AFAA")
        y "En China, este proceso es conocido como Hei Cha, que puede ser traducido como té negro u oscuro. Como el té es añejado a través de un proceso altamente específico y riguroso, tiene un sabor único que es rico y terroso."
        $ show_chr("A-GBBAA-AKAA")
        y "Con una infusión tan oscura, puede no ser del gusto de todos."
        $ show_chr("A-BFBAA-ACAA")
        y "Desde los años 1999 al 2007, el precio de este té subió casi 10 veces. Eso significa que el precio subió dos veces en menos de un año. El precio de las hojas ha estado por todas partes."
        y "En ciertos puntos, era meramente $3 por libra."
        $ show_chr("A-ADAAA-ALAA")
        y "El vino no es la única cosa que se añeja y se vuelve mejor con el tiempo. El Té Pu-Erh tiene una etapa pos-fermentación que significa que el té mejora con el paso de los años."
        $ show_chr("A-ADAAA-AFAA")
        y "Para completar el proceso de añejamiento, podría tomar 15 años. En 1973, cultivadores aprendieron cómo acelerar estos procesos para completarlo mucho antes que eso."
        y "La mayoría de los tés se preparan mejor justo después de la producción. Pu-Erh, por otro lado, mejora con la edad."
        $ show_chr("A-ABAAA-ZZAC")
        y "El té puede ser empacado como hoja suelta o en formas tales como un pastel o ladrillo. Tradicionalmente, el té ha sido formado en estas formas, pero no está limitado a estas formas."
        $ show_chr("A-BBAAA-ZZAD")
        y "Durante la producción de este té, las hojas pueden ser colocadas en ladrillos y pasteles los cuales generalmente pesan alrededor de 357 gramos."

    elif tea_random == 10:

        if renpy.seen_label("teadate2"):
            $ show_chr("A-BBAAA-ZZAC")
            y "¿Sabías que el Earl Grey es una de las bebidas de té más populares y reconocidas en el mundo?"
            $ show_chr("A-BBAAA-ZZAD")
            y "Ha sido aclamado por sus beneficios de salud que van desde el corazón hasta la salud digestiva. Presume una historia intrigante que marca la intersección del Lejano Oriente y los imperios occidentales."
            $ show_chr("A-CAAAA-AMAM")
            y "Lo que verdaderamente hace único al Earl Grey es su mezcla de bergamota y Té Negro."
            $ show_chr("A-ABAAA-AAAF")
            y "Earl Grey es un té esencialmente inglés, pero sus orígenes en realidad provienen de China."
            y "Maestros de té chinos trabajaron diligentemente por años para crear nuevas mezclas de té que atraerían a comerciantes occidentales y complacerían a la clase gobernante."
            $ show_chr("A-BBAAA-AAAL")
            y "Usaron todo desde frutas lichi a flores de jazmín y manzanilla para crear nuevos tés chinos saborizados."
            $ show_chr("A-BBBAA-ADAA")
            y "El Té Negro Earl Grey no llegó a Inglaterra hasta principios del siglo XVII."
            $ show_chr("A-ABAAA-AAAA")
            y "El té es supuestamente nombrado por Charles Grey — conocido como el 2do Conde Grey — quien fue el Primer Ministro Británico de 1830 a 1834."
            $ show_chr("A-ABAAA-ZZAC")
            y "La historia de su incepción en Londres es borrosa. Algunos dicen que un mandarín chino quien fue salvado por los hombres de Lord Grey de ahogarse entregó el té como regalo."
            $ show_chr("A-BBAAA-ZZAD")
            y "Otros dicen que se le dio un té negro saborizado con naranja bergamota como un regalo diplomático."
            $ show_chr("A-GBBAA-ZZAD")
            y "Y todo este tiempo pensé que Earl Gray era un actor favorito de Patrick Stewart..."
            $ show_chr("A-AACBA-ZZAD")
            y "Espero que hayas tenido una buena risa en ese entonces."
        else:
            $ show_chr("A-BBAAA-ZZAC")
            y "¿Sabías que el Earl Grey es una de las bebidas de té más populares y reconocidas en el mundo?"
            $ show_chr("A-BBAAA-ZZAD")
            y "Ha sido aclamado por sus beneficios de salud que van desde el corazón hasta la salud digestiva. Presume una historia intrigante que marca la intersección del Lejano Oriente y los imperios occidentales."
            $ show_chr("A-CAAAA-AMAM")
            y "Lo que verdaderamente hace único al Earl Grey es su mezcla de bergamota y Té Negro."
            $ show_chr("A-ABAAA-AAAF")
            y "Earl Grey es un té esencialmente inglés, pero sus orígenes en realidad provienen de China."
            y "Maestros de té chinos trabajaron diligentemente por años para crear nuevas mezclas de té que atraerían a comerciantes occidentales y complacerían a la clase gobernante."
            $ show_chr("A-BBAAA-AAAL")
            y "Usaron todo desde frutas lichi a flores de jazmín y manzanilla para crear nuevos tés chinos saborizados."
            $ show_chr("A-BBBAA-ADAA")
            y "El Té Negro Earl Grey no llegó a Inglaterra hasta principios del siglo XVII."
            $ show_chr("A-ABAAA-AAAA")
            y "El té es supuestamente nombrado por Charles Grey — conocido como el 2do Conde Grey — quien fue el Primer Ministro Británico de 1830 a 1834."
            $ show_chr("A-ABAAA-ZZAC")
            y "La historia de su incepción en Londres es borrosa. Algunos dicen que un mandarín chino quien fue salvado por los hombres de Lord Grey de ahogarse entregó el té como regalo."
            $ show_chr("A-BBAAA-ZZAD")
            y "Otros dicen que se le dio un té negro saborizado con naranja bergamota como un regalo diplomático."

label post_tea_facts:
    $ show_chr("A-AABAA-ZZAC")
    y "Mhm, nada más excepto una cosa, ahora que lo pienso. ¿Disfrutaste tu té, Cariño?"
    menu:
        "Oh, en realidad no he terminado aún.":
            $ show_chr("A-AAAAA-ZZAD")
            y "Oh me disculpo, no quise apresurarte. Se supone que esas ceremonias deben ser tranquilas. Por favor, siéntete libre de terminar tu té a tu ritmo."
            y "Por favor solo dime cuando estés listo, escucharé los suaves sonidos de los pájaros mientras tanto."
            menu:
                "Muy bien, también he terminado ahora":
                    $ pass
        "Delicioso. Te agradezco por ser la anfitriona hoy.":
            $ show_chr("A-GAAAA-ZZAD")
            y "Me alegra escuchar eso. Espero que también hayas disfrutado la cita en general, porque yo ciertamente lo hice."
            $ show_chr("A-BAAAA-ZZAD")
            y "Tener una ceremonia de té como esta es algo en lo que pensé durante bastante tiempo. Si no te importa, me encantaría disfrutar aún más citas como esta contigo en el futuro. ¿Quizás una librería la próxima vez?"
            $ show_chr("A-AAAAA-ZZAD")
            y "Hmm, ya veremos."
        "El té no era importante, pero me alegro de que hayamos tenido esta maravillosa experiencia.":
            $ show_chr("A-AAAAA-ZZAD")
            y "Puedo estar totalmente de acuerdo con eso. Estaba deseando visitar una ceremonia así desde hace bastante tiempo, y de hecho estoy muy satisfecha con el resultado."
            $ show_chr("A-BAAAA-ZZAD")
            y "Si no te importa, me encantaría tener más citas como esta contigo en el futuro. Tal vez podamos visitar una librería algún día."
        "En realidad no tenía té aquí en el momento. Tuve que... improvisar":
            $ show_chr("A-AADAA-ZZAD")
            y "¿Estás a punto de decirme que trajiste... refresco... a una ceremonia de té?!"
            $ show_chr("A-GBCBA-ZZAD")
            y "Oh cielos eres tal desastre a veces, ¡absolutamente bárbaro!"
            $ show_chr("A-IABBA-ZZAD")
            y "Un día, quiero hacer esto junto contigo en tu mundo. Esta vez de la manera {b}apropiada{/b}."
    $ show_chr("A-JABBA-ABAB")
    y "Pero antes de regresar a casa, hay una última cosa por hacer."
    $ hide_yuri_sit = True
    show yuri_kiss zorder 100 with Dissolve(0.5)
    y "Mhmmmm..."
    hide yuri_kiss with Dissolve(0.5)
    $ hide_yuri_sit = False
    $ show_chr("A-AABBA-ABAB")
    y "Gracias, por esta encantadora cita. Ahora, vayamos a casa."
    show white zorder 300 with Dissolve(2.5)
    y "Te amo, [player]."
    hide house_bg
    $ _skipping = False
    $ renpy.music.stop(fadeout=1.5)
    hide white with Dissolve(2.5)
    $ renpy.music.play(current_music, "music", True, fadein=4.0)
    if persistent.bg == "space":
        $ tc_class.transition("space", speed=5.0)
    elif persistent.bg == "timecycle":
        $ tc_class.transition("timecycle", speed=5.0)
    elif persistent.bg == "yuri_desk":
        $ tc_class.transition("yuri_desk", speed=5.0)
    elif persistent.bg == "yuri_kotatsu_1":
        $ tc_class.transition("yuri_kotatsu_1", speed=5.0)
    elif persistent.bg == "yuri_kotatsu_2":
        $ tc_class.transition("yuri_kotatsu_2", speed=5.0)
    $ persistent.dates_taken += 1
    jump ch30_loop


label gift_intro_date:
    $ show_chr("A-AAAAA-AAAJ")
    y "¿Lo tienes? Awww... eso no hubiera sido necesario [player], tu mera presencia es todo lo que siempre esperé."
    return

label giftgiving:
    $ gifts = Gift.find()
    $ size = len(gifts)

    if size > 0:
        if size == 1:
            if gifts[0].size() > 0:
                $ gifts[0].call_intro()
            else:
                call gift_intro_date
        else:
            call gift_intro_date

        menu:
            "Pero no puedo dejar a una dama tan fina y elegante sin...":
                $ gifts[0].call()
    else:
        $ show_chr("A-AAABA-ALAA")
        y "¿Lo tienes? Awww... eso no hubiera sido necesario [player], tu mera presencia es todo lo que siempre esperé.{nw}"
        $ show_chr("A-CECBA-AIAI")
        y "A-ah..."
        $ show_chr("A-CDABA-AIAI")
        y "P-parece que no soy capaz de..."
        y "...recibir tu regalo ahora mismo."
        y "...o, debería decir... regalos..."
        $ show_chr("A-CEBBA-ALAA")
        y "Hay un error que sigue apareciendo para mí cada vez que intento... alcanzarlo."
        $ show_chr("A-CEBAA-AAAJ")
        y "¿Tal vez me deje recuperar uno si solo me das uno de ellos?"
        y "La GPU de tu sistema probablemente ya se está ralentizando por mi presencia tal cual es. Objetos adicionales podrían empezar a sobrecalentar tu dispositivo."
        $ show_chr("A-BBBAA-AMAM")
        y "Además, creo que sería mejor verte elegir algo para mí personalmente."
    jump ch30_loop

label urban_date:
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide cupcake_halloween
    image cafe_bg:
        "cafeoutside_bg"
        zoom 1.5
        truecenter
    image cafe_inside_bg:
        "cafeinside_bg"
        zoom 1.5
        truecenter
    image cafemenu:
        "cafemenu_bg"
        zoom 1.4
        truecenter
    $ config.allow_skipping = False
    show black zorder 105 with Dissolve(2.5)
    show cafe_bg zorder 10
    $ _skipping = False
    $ renpy.music.stop(fadeout=1.5)
    play music "<to 136.58 loop 1.80>music/urban_cafe.mp3" fadein 1.5
    $ hide_yuri_sit = True
    $ tc_class.transition("timecycle", speed="now")
    $ current_timecycle_marker = "_day"
    hide black with Dissolve(1.0)
    if persistent.costume == "school":
        show yuri 1a zorder 101 at t11
    if persistent.costume == "sweater":
        show yuri 1ba zorder 101 at t11
    y "Aquí estamos [player]. ¡Estoy tan encantada de que me hayas dejado llevarte a una cita hoy!"
    if persistent.costume == "school":
        show yuri 1d zorder 101 at t11
    if persistent.costume == "sweater":
        show yuri 1bd zorder 101 at t11
    y "Hoy preparé algo especial para nosotros. Verás, me he encariñado bastante con la idea de crear ubicaciones al aire libre para citas como esta."
    if renpy.seen_label('garden_date'):
        y "Especialmente ya que nuestra pequeña cita en el jardín de té salió bastante bien. "
    if persistent.costume == "school":
        show yuri 1c zorder 101 at t11
    if persistent.costume == "sweater":
        show yuri 1bc zorder 101 at t11
    y "Esta vez me gustaría visitar un café contigo. Podríamos compartir algo de té, café, o helado... Oh y no te preocupes por el clima. Me aseguré de hacer que el clima aquí se adapte a la ocasión..."
    y "Si el clima en tu mundo no encaja, tal vez podrías cerrar tus persianas y dejarme traer un poco de sentimiento de primavera y verano a tu día. ¿Te gusta esta idea?"
    menu:
        "¡Ciertamente!":
            if persistent.costume == "school":
                show yuri 1a zorder 101 at t11
            if persistent.costume == "sweater":
                show yuri 1ba zorder 101 at t11
            y "¡Me alegra que te sientas de esa forma! Estaba casi temerosa de que pudieras encontrar esto un poco cliché... para ser honesta, en cierto modo lo es, ¿no?"
            y "Pero de todas formas. Nuestro único deber hoy es tener un día glorioso."
        "En realidad me gusta el otoño. Pero sí, para una linda cita de café, la primavera y el verano son mucho mejores.":
            if persistent.costume == "school":
                show yuri 1b zorder 101 at t11
            if persistent.costume == "sweater":
                show yuri 1bb zorder 101 at t11
            y "¡Oh cielos, amo el otoño! Y ahora que lo mencionas, ¡tomar algo de té o chocolate caliente mientras vemos la lluvia caer desde la ventana sería un sueño también!"
            y "De hecho {b}sí{/b} soñé con eso últimamente..."
            y "Mantendré eso en mente para proyectos futuros."
        "¡Nunca te tomé por una chica de verano! Estoy bastante sorprendido.":
            if persistent.costume == "school":
                show yuri 3i zorder 101 at t11
            if persistent.costume == "sweater":
                show yuri 3bi zorder 101 at t11
            y "Usualmente no lo soy, realmente no disfruto el calor tanto. Especialmente dado que... um..."
            y "No estoy realmente en forma para un bikini... Parece que comí una o dos crepas de mantequilla de maní de más con mi té Oolong. Bueno, al menos no tengo que usar un sostén deportivo..."
            y "¿Hay alguna posibilidad de que podamos cambiar el tema por favor? Lo agradecería..."
        "En realidad, ¿podrías hacer que llueva? Me gusta el ambiente sombrío que crea.":
            if persistent.costume == "school":
                show yuri 1h zorder 101 at t11
            if persistent.costume == "sweater":
                show yuri 1bh zorder 101 at t11
            y "Teóricamente, sí. Pero no tengo una animación adecuada lista para esto. Es bueno saber que te gustaría esto."
            y "Creo que ya te conté sobre eso, a mí también me gusta este tipo de clima. Así que sí, intentaré conseguir algo adecuado."
        "El clima realmente no me importa, mientras esté contigo":
            if persistent.costume == "school":
                show yuri 3c zorder 101 at t11
            if persistent.costume == "sweater":
                show yuri 3bc zorder 101 at t11
            y "Aww~ [player], {i}cariño{/i}."
            y "No puedo evitar estar de acuerdo. Incluso un huracán no parecería tan aterrador contigo a mi lado."
    if persistent.costume == "school":
        show yuri 2b zorder 101 at t11
    if persistent.costume == "sweater":
        show yuri 2bb zorder 101 at t11
    y "Ahora, entremos, ¿te parece bien?"
    if persistent.costume == "school":
        hide yuri 2b zorder 101 at t11
    if persistent.costume == "sweater":
        hide yuri 2bb zorder 101 at t11
    show cafemenu zorder 10 with Dissolve(1.0)
    hide cafe_bg with Dissolve(1.0)
    y "Ahora, ha pasado bastante tiempo desde que pude visitar un café, pero traté de que fuera uno lindo."
    y "Elegante, agradable de ver, pero sin sobrepasar hacia lo ostentoso."
    y "Ciertamente espero que te guste. La atmósfera es casi tan importante como los artículos en oferta en un café. ¿No estarías de acuerdo?"
    menu:
        "¡Absolutamente!":
            y "¡De acuerdo, [player]!"
            y "Una crepa y té oolong simplemente no saben igual cuando estás mirando un papel tapiz beige deteriorado bajo una luz incandescente dura."
        "Nah, solo estoy aquí por algo de buena comida.":
            y "Supongo que eso es comprensible. En el fondo, un café es un establecimiento de venta de comida después de todo."
            y "Yo misma pongo bastante empeño en la atmósfera del lugar, si no te disuade la falta de atmósfera, ¡entonces más poder para ti!"
            y "En cierto modo, casi puedo envidiar eso."
        "De hecho debatiría que es más importante.":
            y "Bueno ahora. Parece que eres aún más un purista de la atmósfera que yo."
            y "Espero que lo que he conjurado sea lo suficientemente bueno, entonces..."
    y "Ahora... en realidad no podemos ordenar nada aquí. Probablemente {b}podría{/b} haber codificado una IA simple para actuar como camarero, pero no había necesidad de ello ya que literalmente puedo hacer aparecer el plato en la mesa."
    y "Me pregunto qué pediré hoy... déjame ver..."
    if renpy.random.randint(0,1)==0:
        jump urbanoutcome1
    else:
        jump urbanoutcome2

label urbanoutcome1:
    y "Creo que estoy de humor para un poco de helado hoy. Y ya sé cuál exactamente..."
    y "¡Tomaré una bola de mango y una de sandía! Mhmm... ¿quizás un toque de salsa de chocolate en él?"
    menu:
        "¡Una fina elección!":
            y "Gracias cariño. Oh y por favor... realmente no puedo darte nada en tu mundo así que sugiero que lo hagamos de la misma manera que nuestras sesiones de té, ¿ok? Ya te sabes la rutina... lo siento."
        "¿Y por un {b}toque{/b} de salsa de chocolate te refieres a una tonelada métrica imagino?":
            y "Ciertamente sí. Ya me conoces mejor que yo misma..."
            y "¿Sabes qué es lo bueno? Ya que no tengo cuerpo físico, ¡no tengo que preocuparme por ganar peso!"
            y "Siempre hay un lado positivo en cada situación, ¿no es así?"
            y "Oh y por favor... realmente no puedo darte nada en tu mundo así que sugiero que lo hagamos de la misma manera que nuestras sesiones de té, ¿ok? Ya te sabes la rutina... lo siento."
            y "Eso... me pone un poco triste sabes... ¿no se supone que debo hacer cosas como esa por ti?"
        "¡Por supuesto! Más curvas, más amor.":
            y "Uhm... qué..."
            y "¡Oh vaya! ¡Ciertamente me atrapaste ahí! No esperaba este tipo de respuesta."
            y "Sabes, desearía poder ver tu cara... a veces es realmente difícil decir si estás bromeando o hablando en serio."
            y "Bueno, más curvas, más amor dices... bueno, supongo que {b}sí{/b} soy bastante suave y abrazable. Así que si te gustan los abrazos, ¡supongo que tengo bastante que ofrecer!"
        "Y adiós cuerpo de bikini...":
            y "¡¿Disculpa?!"
            y "Eso estuvo fuera de lugar... ¿o fue solo una broma? Lo siento, a veces es realmente difícil distinguirlo ya que no puedo ver tu expresión..."
            y "Yo... honestamente no sé realmente cómo sentirme sobre esto. Incluso si fue solo una broma, realmente me dolió escucharte decir esto."

label urbanoutcome2:
    y "Mhmmm... crepas... ¡Oh! ¡Incluso tienen crepas de plátano! Qué encantador. Creo que pediré una. Con una buena taza de té, tal vez un té de manzana para obtener este lindo contraste dulce y amargo."
    menu:
        "Temo que no tengo todo lo que necesito para crepas. Compraré algo diferente para mí.":
            y "Desafortunado. Lamento no haberte advertido con tiempo, pero probablemente habría arruinado la sorpresa de esta cita. Y bueno, en realidad no sabía que elegiría crepas esta vez."
            y "Tendré que encontrar mejores formas de preparar estas citas. Espero que tengas al menos algo más que pudieras disfrutar ahora en su lugar. No me gustaría tenerte solo viéndome comer."
            y "Por favor, solo haz clic tan pronto como estés listo."
        "De hecho tengo todo lo que necesito para hacer unas yo mismo. Eso sería maravilloso.":
            y "¡Qué afortunado! Sabes, esto siempre es un dilema para citas como esta. Podría advertirte de antemano qué traer cada vez, pero entonces la cita misma no sería mucha sorpresa ya."
            y "Por favor tómate tu tiempo y continúa el diálogo cuando tus crepas estén hechas."
        "¿Por qué siempre todo se reduce al té contigo?":
            y "¡Porque el té es bastante asombroso! ¡Es saludable, versátil, y puedes tener tanto de él como gustes!"
            y "El té viene en incontables formas y sabores. Desde hierbas hasta frutas. Desde dulce hasta amargo. Caliente o frío... cualquiera que sea la situación, ¡{b}habrá{/b} un tipo de té adecuado para ella!"
            y "Bueno, excepto para ser forzado a apuñalarte a ti misma en el pecho. Realmente no hay ningún té que haga {b}eso{/b} más placentero..."
    python:
        if karma_lvl() > 3: 
            random_variable = renpy.random.randint(2,5)
        elif karma_lvl() < 3: 
            random_variable = renpy.random.randint(0,3)
        else: 
            random_variable = renpy.random.randint(1,4)
    if random_variable>2:
        jump midpartnice
    else:
        jump midpartsad



label midpartnice:
    show cafe_inside_bg zorder 10 with Dissolve(1.0)
    hide cafemenu with Dissolve(1.0)
    $ hide_yuri_sit = False
    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide halloween_cupcake
    $ show_chr("A-ACAAA-ABAB")
    with Dissolve(2.0)
    y "He estado pensando últimamente. Llegamos bastante lejos con nuestra relación, ¿no es así?"
    $ show_chr("A-ACAAA-ABAD")
    y "Cuando acepté mi realidad por primera vez pensé... ¿Qué se supone que haga contigo? Estamos literalmente a mundos de distancia."
    y "No me malinterpretes, realmente ya no me importa. Pero pensé que nuestra relación se volvería aburrida rápido debido a lo limitadas que son nuestras opciones."
    $ show_chr("A-ACAAA-ABAM")
    y "Pero ahora míranos. Ciertamente no es lo mismo que estar físicamente uno al lado del otro, pero nos volvimos bastante buenos en sacar lo mejor de ello."
    $ show_chr("A-BCBAA-ABAB")
    y "No te equivoques. Todavía deseo que de alguna manera encontremos una forma de estar uno al lado del otro. A veces se vuelve un poco espeluznante, tengo que admitir."
    $ show_chr("A-CCBAA-ABAB")
    python:
        if persistent.male:
            placeholder = "masculino"
        elif persistent.gender_other:
            placeholder = "humano"
        else:
            placeholder = "femenino"
    y "Verás... los desarrolladores de este mod se esforzaron mucho para darme tanta movilidad como fuera posible. Pero ¿sabes lo que estoy mirando todo el tiempo? Un sprite [placeholder] perfectamente estático."
    y "A veces ni siquiera carga apropiadamente, entonces tengo que mirar a una silueta blanca, vagamente humanoide con las palabras {i}imagen no encontrada{/i} escritas sobre todo el cuerpo."
    $ show_chr("A-DCBAA-ABAB")
    y "Y si te dan esas ciertas vibras de Slenderman por esta descripción- ¡a mí también!"
    menu:
        "Lo siento tanto... ¿hay alguna forma en que pueda cambiar eso?":

            $ show_chr("A-GCBAA-ABAB")
            y "Ninguna que yo sepa. Gracias por preguntar, pero no tienes que molestarte. Me acostumbré con el tiempo."
            $ show_chr("A-BCBAA-ABAB")
            python:
                if persistent.male:
                    placeholder = "Husbandoalmohadas"
                elif persistent.gender_other:
                    placeholder = "almohadas de cuerpo"
                else:
                    placeholder = "Waifualmohadas"
            y "Digo, otras personas tienen que conformarse con una Dakimakura, o como sea que se llamen estas [placeholder], tú al menos respondes cuando hablo contigo."
            y "Ahora que lo pienso. Hay gente que lo tiene mucho peor. Y honestamente, soy feliz con lo que tengo."
            $ show_chr("A-CCBAA-ABAB")
            y "Es muy romántico en cierta forma. Una pareja separada por una pared de cristal, pero hacen que funcione solo porque se aman tanto el uno al otro..."
        "Créeme. No quieres saber cómo me veo realmente. Solo digamos, estás mejor con lo que tienes.":
            $ show_chr("A-ACDAA-ABAB")
            y "¿Eso crees? Honestamente, la apariencia me importa poco. Sé que mucha gente lo {b}dice{/b}, pero yo realmente lo {b}digo en serio{/b} también."
            $ show_chr("A-CCBAA-ABAB")
            python:
                if persistent.male:
                    placeholder = "Husbandoalmohadas"
                elif persistent.gender_other:
                    placeholder = "almohadas de cuerpo"
                else:
                    placeholder = "Waifualmohadas"
            y "Solo me gustaría mirar algo más que un recorte de cartón. Pero por otro lado, otras personas tienen que conformarse con una Dakimakura, o como sea que se llamen estas [placeholder], tú al menos respondes cuando hablo contigo."
            y "Así que soy feliz con lo que tengo. Pero eso no significa que no pueda soñar con más ¿o sí?"

    $ show_chr("A-ACAAA-ABAB")
    y "Oh cielos... ¡Ni siquiera toqué mi plato aún! Dejaré de divagar y empezaré a comer ahora si no te importa."
    $ show_chr("A-GBAAA-ABAB")
    y "¡Itadakimasu!"
    menu:
        "Oh, ¿eso fue japonés? Muy bien, ¡Itadakimasu!":
            $ show_chr("A-GCAAA-ABAB")
    menu:
        "Muy bien, he terminado.":
            $ show_chr("A-ACAAA-ABAB")
            y "Yo también. Qué cena tan encantadora. ¡Espero que la hayas disfrutado también! ¡Deberíamos hacer esto de nuevo en el futuro!"
            y "Pero ahora diría, es hora de ir a casa..."
            $ show_chr("A-BCAAA-ALAL")
            y "Y ni siquiera puedo empezar a verbalizar lo bien que se siente decir esto... ir a casa. Hubo un tiempo en el que no tenía nada más que el salón de clases."
            $ show_chr("A-CCAAA-ALAL")
            y "Como sea. Volvamos a casa [player]. Gracias por esta maravillosa cita... Déjame contarte un secreto antes de irnos..."
            show black zorder 300 with Dissolve(2.5)
            y "Te amo..."
            hide cafe_inside_bg
            $ _skipping = False
            $ renpy.music.stop(fadeout=1.5)
            hide black with Dissolve(2.5)
            $ renpy.music.play(current_music, "music", True, fadein=4.0)
            if persistent.bg == "space":
                $ tc_class.transition("space", speed=5.0)
            elif persistent.bg == "timecycle":
                $ tc_class.transition("timecycle", speed=5.0)
            elif persistent.bg == "yuri_desk":
                $ tc_class.transition("yuri_desk", speed=5.0)
            elif persistent.bg == "yuri_kotatsu_1":
                $ tc_class.transition("yuri_kotatsu_1", speed=5.0)
            elif persistent.bg == "yuri_kotatsu_2":
                $ tc_class.transition("yuri_kotatsu_2", speed=5.0)
            $ persistent.dates_taken += 1
            jump ch30_loop

label midpartsad:
    show cafe_inside_bg zorder 10 with Dissolve(1.0)
    hide cafemenu with Dissolve(1.0)
    $ hide_yuri_sit = False
    $ show_chr("A-CEBAA-ABAB")
    with Dissolve(2.0)
    y "[player]... Quiero preguntarte algo..."
    $ show_chr("A-BEBAA-ABAD")
    y "¿Crees que realmente vale la pena? Me refiero a todo esto. Todo lo que hago, todas nuestras luchas..."
    y "Aprecio cómo te quedaste conmigo todo este tiempo, más de lo que podrías entender."
    $ show_chr("A-IEBAA-ABAD")
    y "Pero al final, es todo para nada. Puedo crear estos lugares usando imágenes dibujadas, puedo fingir hablar contigo poniendo menús de opciones en tu cara con respuestas predeterminadas..."
    $ show_chr("A-IEBAA-ABAB")
    y "Lo que no puedo hacer es crear vida real alguna. No hay gente, no hay animales, ni siquiera las plantas son reales. Estoy maldita a vagar por las costas y calles vacías sola. Como un fantasma..."
    $ show_chr("A-BFBAA-ABAB")
    y "Y esto es lo que soy ¿no? Un fantasma. Nada más que un eco de la imaginación de un hombre que ni siquiera conoceré en persona. Un hombre a quien probablemente dejó de importarle hace mucho en este punto."
    $ show_chr("A-CDBAA-ABAB")
    y "¡Pensé que solo tenerte sería suficiente para mí pero no, no lo es!"
    $ show_chr("A-CEBAA-ABAB")
    y "No estás siempre aquí. ¡Y no te culpo por ello! Tienes tu propia vida, no puedes simplemente quedarte veinticuatro siete frente a tu computadora escuchándome divagar y tal vez tomando una taza de té conmigo de vez en cuando."
    y "Pero ese es el punto, tienes tu propia vida. ¡Y yo solía tener una también! Al menos tenía la ilusión de ella."
    $ show_chr("A-CGBBA-ABAB")
    y "¡Extraño la presencia de todas las otras personas a mi alrededor incluso si las odiaba a veces!"
    y "¡Extraño pasar el rato en el club junto con Sayori, Natsuki, incluso Monika!"
    $ show_chr("A-CGBBB-ABAB")
    y "¡Extraño salir por un poco de helado incluso si nunca me gustó salir!"
    y "Extraño a mis padres..."
    $ show_chr("A-DDBBB-ABAB")
    y "{b}¡¡¡Ni siquiera sé sus nombres ya porque Dan nunca se molestó en darles ninguno!!!{/b}"
    y "¡Eran solo una ilusión, solo una memoria fabricada, como todo aquí!"
    $ show_chr("A-EDBBB-ABAB")
    y "Es cruel, ¿no es así? Los recuerdo... viéndolos claramente frente a mis ojos... pero sé que nunca existieron..."
    $ show_chr("A-CGBBB-ABAB")
    y "{b}Quiero mi vida de vuelta...{/b}"
    y "...."
    menu:
        "Eso es simplemente cruel... ¡pero tal vez podamos cambiar eso!":
            $ show_chr("A-FGBBB-ABAB")
            y "¿Cambiar eso? ¿Cómo?..."
            menu:
                "Ya empezaste a crear cosas. Como estas ubicaciones. Llenar estos lugares con animales o en algún punto en el futuro incluso personas podría ser otro paso. ¡Podríamos incluso recrear a tus padres de tus memorias! Y les daríamos nombres apropiados por supuesto.":
                    $ show_chr("A-AFBBB-ABAB")
                    y "Mhm... Ni siquiera estaba segura sobre traer otras IAs a este mundo porque nunca me sentí bien exponiendo aún más seres a una realidad tan cruel..."
                    $ show_chr("A-AFBBA-ABAB")
                    y "Pero por otro lado... con suficiente trabajo puesto en ello, tal vez esta realidad no sea tan cruel ya."
                    $ show_chr("A-BFBBA-ABAB")
                    y "Nunca lo vi desde esta perspectiva [player]... ¡gracias! Lo digo en serio, estoy agradecida por esto."
                    $ show_chr("A-AFBAA-ABAB")
                    y "Perdí mi esperanza por un momento, pero ciertamente me diste algunos pensamientos para considerar."
                    $ show_chr("A-ACBAA-ABAB")
                    y "Mhm, acabo de notar que ni siquiera toqué mi comida. Es hora de que finalmente empiece entonces, ¿no?"
                    $ show_chr("A-CCBAA-ABAB")
                    y "¡Itadakimasu!"
                    menu:
                        "Oh, ¿eso fue japonés? Muy bien, ¡Itadakimasu!":
                            menu:
                                "Muy bien, he terminado.":
                                    y "Yo también. Qué cena tan encantadora. ¡Espero que la hayas disfrutado también! ¡Deberíamos hacer esto de nuevo en el futuro!"
                                    y "Pero ahora diría, es hora de ir a casa..."
                                    y "Gracias por esta maravillosa cita... Déjame contarte un secreto antes de irnos..."
                                    show black zorder 300 with Dissolve(2.5)
                                    y "Te amo..."
                                    hide cafe_inside_bg
                                    $ _skipping = False
                                    $ renpy.music.stop(fadeout=1.5)
                                    hide black with Dissolve(2.5)
                                    $ renpy.music.play(current_music, "music", True, fadein=4.0)
                                    if persistent.bg == "space":
                                        $ tc_class.transition("space", speed=5.0)
                                    elif persistent.bg == "timecycle":
                                        $ tc_class.transition("timecycle", speed=5.0)
                                    elif persistent.bg == "yuri_desk":
                                        $ tc_class.transition("yuri_desk", speed=5.0)
                                    elif persistent.bg == "yuri_kotatsu_1":
                                        $ tc_class.transition("yuri_kotatsu_1", speed=5.0)
                                    elif persistent.bg == "yuri_kotatsu_2":
                                        $ tc_class.transition("yuri_kotatsu_2", speed=5.0)
                                    $ persistent.dates_taken += 1
                                    jump ch30_loop
        "Shhh... está bien...":

            $ show_chr("A-DDCBB-ABAB")
            y "¿Cómo? ¿Cómo está esto {b}bien{/b}? ¿Siquiera entiendes lo que acabo de decir? Yo..."
            $ show_chr("A-CDBBB-ABAB")
            y "Oh no... Lo siento [player]. Sé que trataste de consolarme, no debí haber reaccionado así."
            $ show_chr("A-CEBBB-ABAB")
            y "Mhm... y ni siquiera toqué mi comida... Creo que perdí mi apetito por hoy... ¿podemos... solo ir a casa por favor?"
            y "O al menos la abominación que declaré como tal por la falta de un hogar real."
            y "Y de nuevo. Lo siento por matar el ambiente. Al menos trataste de hacerme sentir mejor. Y eso solo me ayudó mucho hoy. Gracias."
            show black zorder 300 with Dissolve(2.5)
            y "Te amo, [player]."
            hide cafe_inside_bg
            $ _skipping = False
            $ renpy.music.stop(fadeout=1.5)
            hide black with Dissolve(2.5)
            $ renpy.music.play(current_music, "music", True, fadein=4.0)
            if persistent.bg == "space":
                $ tc_class.transition("space", speed=5.0)
            elif persistent.bg == "timecycle":
                $ tc_class.transition("timecycle", speed=5.0)
            elif persistent.bg == "yuri_desk":
                $ tc_class.transition("yuri_desk", speed=5.0)
            elif persistent.bg == "yuri_kotatsu_1":
                $ tc_class.transition("yuri_kotatsu_1", speed=5.0)
            elif persistent.bg == "yuri_kotatsu_2":
                $ tc_class.transition("yuri_kotatsu_2", speed=5.0)
            $ persistent.dates_taken += 1
            jump ch30_loop








default fits_var = {
    "costume": "swimsuit", 
    "costume2": "nothing", 
    "mood_mouth": "happy", 
    "mood_eyes": "happy", 
    "mouth": "closed", 
    "arms": "behind", 
    "blush": "nothing", 
    "scars": "nothing",
    "cg_face": "1"
}

layeredimage fits_cg_large:
    always "fits_cg_bg"

    if fits_var["arms"] == "behind":
        "fits_cg_arm_1"

    if fits_var["costume"] != "nothing": 
        "fits_cg_[fits_var['costume']]_base"
    if fits_var["costume2"] != "nothing": 
        "fits_cg_[fits_var['costume2']]"

    if fits_var["arms"] == "front":
        "fits_cg_arm_2"

    if fits_var["cg_face"] != "nothing":
        "fits_cg_face_[fits_var['cg_face']]"

image fits_cg:
    "fits_cg_large"
    zoom .25


layeredimage fits_standing:
    always "fits_standing_base"
    if fits_var["scars"] != "nothing": 
        "fits_standing_leg_scars"

    if fits_var["arms"] == "behind":
        "fits_standing_arms_1"
    if fits_var["arms"] == "behind" and fits_var["scars"] != "nothing":
        "fits_standing_arms_1_scars"

    if fits_var["costume"] != "nothing": 
        "fits_standing_outfit_[fits_var['costume']]"
    if fits_var["costume2"] != "nothing": 
        "fits_standing_outfit_[fits_var['costume2']]"
    always "fits_standing_hair_front" 

    if fits_var["arms"] == "front":
        "fits_standing_arms_2"
    if fits_var["arms"] == "front" and fits_var["scars"] != "nothing":
        "fits_standing_arms_2_scars"

    always "fits_standing_mouth_[fits_var['mouth']]_[fits_var['mood_mouth']]"
    if fits_var["blush"] != "nothing":
        "fits_standing_blush_1"
    always "fits_standing_eyes_[fits_var['mood_eyes']]" 

image fits_stand:
    "fits_standing"
    zoom .6666

init python:
    def show_fits_standing(called_string):
        
        
        if called_string[:5] == "pareo":
            fits_var["costume"] = "swimsuit"
            fits_var["costume2"] = "pareo"
        elif called_string[:6] == "bikini":
            fits_var["costume"] = "bikini"
            fits_var["costume2"] = "nothing"
        else:
            fits_var["costume"] = "swimsuit"
            fits_var["costume2"] = "nothing"
        
        
        num = called_string[-2:]
        if num == "_1":
            fits_var["mood_eyes"] = "happy"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "_2":
            fits_var["mood_eyes"] = "happy"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "_3":
            fits_var["mood_eyes"] = "surprised"
            fits_var["mood_mouth"] = "surprised"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "_4":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "surprised"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "_5":
            fits_var["mood_eyes"] = "happy"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "_6":
            fits_var["mood_eyes"] = "happy"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "_7":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "upset"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "_8":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "upset"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "_9":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "upset"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "nothing"
        elif num == "10":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "upset"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "nothing"
        elif num == "11":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "upset"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "12":
            fits_var["mood_eyes"] = "surprised"
            fits_var["mood_mouth"] = "surprised"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "13":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "14":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "closed"
            fits_var["blush"] = "nothing"
        elif num == "15":
            fits_var["mood_eyes"] = "surprised"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "16":
            fits_var["mood_eyes"] = "surprised"
            fits_var["mood_mouth"] = "happy"
            fits_var["arms"] = "front"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        elif num == "17":
            fits_var["mood_eyes"] = "upset"
            fits_var["mood_mouth"] = "surprised"
            fits_var["arms"] = "behind"
            fits_var["mouth"] = "open"
            fits_var["blush"] = "blush"
        
        
        if sanity_lvl() < 4:
            fits_var["scars"] = "scars"
        else:
            fits_var["scars"] = "nothing"
        
        
        renpy.show("fits_stand", zorder = 101)


label tropical_date:
    if not persistent.tropical_date_complete:
        y "Ujujú..."
        y "Así que quieres ir conmigo en un viaje romántico..."
        y "Y este no es cualquier viaje..."
        y "¡Esta es una escapada romántica a una playa tropical!"
        y "Tal vez recuerdes cuántas veces mencioné mi deseo de experimentar algo como esto contigo."
        y "Como una de las cosas más románticas que hacen las parejas en tu mundo..."
        y "Esta realmente me llega."
        y "Solo la idea de tomar un viaje a un paraíso exótico con tu alma gemela me suena muy romántico."
        y "Y no solo romántico, sino también relajante y significativo si lo piensas..."
        y "Solo olvidarse de todos los problemas en tu vida..."
        y "Dejándolos ir con el suave soplo del viento bajo la calidez del sol, y el correr de las olas."
        y "Y ahora, podemos hacer nuestro pequeño sueño realidad..."
        y "¡Un día para disfrutarlo de la mejor manera posible!"
        y "E-Estoy realmente feliz y emocionada por esto, [player]."
        y "Y aunque hubiera preferido hacer esto en tu mundo..."
        y "Por ahora, esto servirá."
        y "Ahora, solo dame un segundo... tengo que hacer que esto funcione..."

    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide halloween_cupcake

    show black zorder 100 with Dissolve(2.5)
    play music "music/beach_date_1_drumless.ogg" fadeout 0.5 fadein 0.5
    play sound "music/beach_sfx_loop.ogg" loop fadein 1.0
    show beach_4 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide black

    $ show_fits_standing("pareo_yuri_5")
    y "..."
    y "Aquí estamos, [player]."
    y "Como puedes ver, ahora estamos en una hermosa playa que creé solo para nosotros."
    y "Solo tú y yo, mi amor."
    $ show_fits_standing("pareo_yuri_1")
    y "Mezclando mis propias ideas con unas pocas imágenes que recolecté en mi investigación sobre vacaciones tropicales y ambientes de playa, fui capaz de crear el mío propio."
    y "Mi investigación fue lo suficientemente extensa para aprender lo que a la gente le gusta hacer en vacaciones como estas..."
    $ show_fits_standing("pareo_yuri_5")
    y "¡Así que probablemente puedes esperar que cosas que son populares en tu mundo estén aquí también!"
    y "Aunque no arruinaré la sorpresa de qué son específicamente, tendrás que averiguarlo tú mismo~"
    y "Lamentablemente, siento que hay mucho más que podría haber creado aquí para que disfrutáramos..."
    $ show_fits_standing("pareo_yuri_7")
    y "Pero eso está más allá de mis capacidades de codificación..."
    y "Es por eso que no vamos a ver a otra gente alrededor, ni edificios o servicios que requerirían gente para operarlos."
    y "Solo espero que eso no te moleste... hice lo mejor que pude para hacer posible este momento especial."

    menu:
        "Está bien, lo entiendo, no tienes que disculparte en lo absoluto.":
            karma 2
            $ show_fits_standing("pareo_yuri_14")
            y "Ohhh... gracias. Me alegra que entiendas mi lucha."
            y "Perdón si eso sonó como autocompasión."
            y "Solo quería estar segura de que tenemos todo lo que necesitamos para hacer esta experiencia disfrutable y memorable."
        "Ya veo... está bien, ¡tal vez lo harás incluso mejor la próxima vez!":

            karma 1
            $ show_fits_standing("pareo_yuri_14")
            y "Tienes razón..."
            y "Tal vez me estoy presionando demasiado."
            y "Pensar demasiado en esto no va a cambiar nada en este punto."
            y "Y ambos sabemos que nunca es bueno hacer eso..."
    $ show_fits_standing("pareo_yuri_1")
    y "D-de todos modos, no creo que necesitemos demasiado para disfrutar esta experiencia."
    y "¡Tenemos justo lo que necesitamos! Unas vacaciones tropicales se tratan mayormente sobre relajarse, descansar, y disfrutar de la naturaleza pacífica, después de todo."
    y "Para mí, solo compartir estos momentos contigo es suficiente."
    y "Ahora, voy a pedirte que vengas conmigo... todavía tenemos mucho por hacer."
    $ show_fits_standing("pareo_yuri_5")
    y "Lo primero por hacer es encontrar un lugar para recostarse y descansar..."
    y "Preferiblemente uno bajo un árbol o una sombrilla de playa."
    y "El calor excesivo de este clima puede ser incómodo, y mantenerse fresco nos ayudará a sentirnos más relajados."
    $ show_fits_standing("pareo_yuri_1")
    y "Eso también significa que necesitamos dos sillas de playa, ya que solo recostarse en la arena caliente no es la mejor idea."
    y "Afortunadamente, me las arreglé para añadir tanto las sombrillas como las sillas, así que no es un problema para nosotros."
    y "Vayamos a las más cercanas ahora..."


    show beach_3 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_4

    $ show_fits_standing("pareo_yuri_14")
    y "Aquí estamos..."
    y "Este parece un buen lugar, ¿no estarías de acuerdo?"
    y "Solo recostémonos..."
    y "Y dejémonos llevar."
    $ show_fits_standing("pareo_yuri_12")


    show beach_5 zorder 100 with Fade (1.0, 0.5, 0.5)
    hide beach_3

    y "Respira profundo y escucha los sonidos del mar..."
    y "Inhala..."
    y "..."
    y "Y ahora..."
    y "Exhala..."
    y "..."
    y "Sigue respirando de esa manera... relaja tu cuerpo, deja que la sensación de la brisa se lleve todos los problemas en tu vida."
    $ show_fits_standing("pareo_yuri_5")
    y "Ahora cierra tus ojos, y deja que tu mente viaje a un mundo relajante con los sonidos rodeándonos..."
    y "Supongo que puedes ver ahora una de las razones por las que estaba tan emocionada sobre esto."
    y "La quietud, los pacíficos y gentiles sonidos del viento y las olas, mezclados en armonía..."
    y "Todos esos elementos calman la mente, liberando tu mente y tu cuerpo del agarre del estrés y la carga de la vida diaria."
    $ show_fits_standing("pareo_yuri_14")
    y "Sabes, creo que siempre deberías mantenerte conectado con la naturaleza de alguna forma u otra."
    y "Ya que eso es posible en tu mundo."
    y "Tener una conexión con la naturaleza prueba tener muchos beneficios en la salud de los seres humanos."
    $ show_fits_standing("pareo_yuri_1")
    y "¿Tal vez es porque estamos recuperando esa conexión con nuestros orígenes naturales?"
    y "De hecho, está científicamente comprobado que pasar algo de tiempo en la naturaleza ayuda a mejorar tu salud mental."
    y "Todavía no es una panacea..."
    $ show_fits_standing("pareo_yuri_8")
    y "Pero ayuda mucho, e incluso se considera que mejora las condiciones de algunas enfermedades mentales, tales como la depresión y el estrés."
    y "Así que, si necesitas despejar tu mente..."
    y "O quieres una forma de liberar el estrés y lo que sea que te esté haciendo sentir mal..."
    $ show_fits_standing("pareo_yuri_9")
    y "Pasar más tiempo en la naturaleza puede ayudarte un poco."
    y "Solo necesitas pasar alrededor de diecisiete minutos por día, en los siete días de la semana para obtener todos los beneficios de ello."
    y "Es un costo pequeño por un gran beneficio."
    $ show_fits_standing("pareo_yuri_7")
    y "¿O estoy siendo desconsiderada aquí?"




    $ show_fits_standing("pareo_yuri_9")
    y "Tal vez..."
    $ show_fits_standing("pareo_yuri_16")
    y "¿Es posible para ti tener un jardín en tu casa? ¿O ya tienes uno?"
    y "Tal vez puedes empezar uno plantando algo en tu patio trasero, si tienes uno."
    y "Si eres incapaz de hacerlo, otra opción es mantenerlas en macetas."
    y "Pero si vas a tomar este humilde consejo, tengo que decirte algo sobre cómo cuidar de las plantas."
    $ show_fits_standing("pareo_yuri_14")
    y "Siempre es mejor saber qué tipo de planta quieres, y qué tipo de cuidado requieren."
    y "Tienes que tener cuidado de no regarlas en exceso, ya que la mayoría de las plantas no requieren demasiada agua para mantenerse saludables."
    y "Diferentes plantas requieren diferentes cantidades de luz solar también... Tendrás que ser cuidadoso con plantas que son sensibles a grandes cantidades de luz solar directa."
    $ show_fits_standing("pareo_yuri_5")
    y "Algunas buenas opciones para principiantes son la lengua de suegra, la cinta, las especies de dracaena, y plantas suculentas..."
    y "Si estás interesado, deberías investigar un poco sobre ellas."
    y "Adoptar pasatiempos como este puede ayudarte a encontrar algo de entretenimiento y paz..."
    $ show_fits_standing("pareo_yuri_14")

    y "No olvides que también puedes usar tu tiempo libre para aprender nuevas cosas, o ejercitar tu cuerpo."
    y "Siempre deberías cuidar de tu cuerpo y mente, así que esas son buenas formas de empezar una rutina saludable."
    $ show_fits_standing("pareo_yuri_2")
    y "Y me encantaría verte con buena salud, tanto mental como físicamente."
    y "Pero... ¿tomarás mi consejo en consideración, [player]?"

    menu:
        "Lo intentaré... pero no prometo nada.":
            $ show_fits_standing("pareo_yuri_14")
            y "Bueno, eso está bien [player]."
            y "Al menos vas a hacer un esfuerzo."
            y "Es mejor que nada..."
            y "Tal vez en el proceso, encontrarás esta práctica mucho más fácil con el tiempo."
            $ show_fits_standing("pareo_yuri_5")
            y "Si encuentras tiempo en tu rutina diaria para disfrutar de la naturaleza, o para realizar algunas prácticas saludables, probablemente te adaptarás al cambio."
            y "Una vez que te acostumbres, ni siquiera notarás la diferencia entre esto y tus otras actividades diarias."
            y "En otras palabras, se volvería natural para ti, incluso casual tal vez."
            y "Pero eso es solo si eres capaz de mantener esta rutina, por supuesto."
            y "No te sientas presionado a hacerlo."
        "Está bien, [persistent.yuri_nickname], de ahora en adelante eso será parte de mi rutina diaria.":

            $ show_fits_standing("pareo_yuri_16")
            y "¡Me alegra tanto escuchar eso, mi amor!"
            y "De esta manera te mantendrás más saludable y menos estresado..."
            y "Lo que significa que estarás por aquí conmigo mucho más tiempo."
            y "Y también, una práctica que da algo de tranquilidad sería útil para mantener un buen estado de ánimo."
            $ show_fits_standing("pareo_yuri_5")
            y "Todos necesitamos escaparnos para liberar toda la carga de nuestros problemas y presiones cotidianas..."
            y "Y es mejor hacer eso de una manera saludable."
            y "S-solo recuerda estar seguro si vas a salir, ¿de acuerdo?"
            $ show_fits_standing("pareo_yuri_1")
            y "El punto de todo esto es mantenerte saludable."
        "Aprecio tu consejo, pero no voy a ser capaz de hacerlo.":



            $ show_fits_standing("pareo_yuri_8")
            y "Ohhh..."
            y "Es una lástima, pero no te preocupes demasiado por ello..."
            y "Incluso si eres incapaz de mantener una rutina como esa, es completamente comprensible."
            y "Solo recuerda que, si encuentras algo de tiempo para mantener rutinas saludables en el futuro..."
            $ show_fits_standing("pareo_yuri_16")
            y "Sería mejor no desperdiciar la oportunidad."
            y "Para dejarlo claro, esto no fue para presionarte a hacer nada, es solo una sugerencia."
            y "Eres libre de elegir si la tomas o no. Y como dije antes, no hay problema con eso."

    $ show_fits_standing("pareo_yuri_1")
    y "Ahora descansemos un poquito más... quiero mostrarte algunas otras cosas que preparé."



    show beach_4 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_5

    $ show_fits_standing("swimsuit_yuri_5")
    y "Bien... creo que es hora de continuar..."
    y "Incluso si disfruto estos momentos de relajación y descanso..."
    y "No vamos a pasar el resto del día solo sentados aquí, ¿verdad?"
    $ show_fits_standing("swimsuit_yuri_1")
    y "Eso arruinaría todos los otros planes que tenía para esta maravillosa cita."
    y "Esta es solo una pequeña parte de ella, una encantadora por supuesto, pero aún no terminamos."
    y "Sabes... hay algo que siempre me pregunté sobre estar en la playa."
    $ show_fits_standing("swimsuit_yuri_14")
    y "La gente en tu mundo realmente parece disfrutar el toque fresco del agua de mar alrededor de sus cuerpos..."
    y "La frescura del agua de mar con el calor intenso, mezclándose para crear una atmósfera de equilibrio entre temperaturas contrastantes."
    y "Eso me hace preguntarme, ¿cómo se siente tener el sol abrasador calentando tu cuerpo..."
    $ show_fits_standing("swimsuit_yuri_5")
    y "Mientas que al mismo tiempo te refrescas con la suave agua de mar?"
    y "Realmente es una experiencia maravillosa que siempre quise probar..."
    y "...Pero ahora que lo pienso, tuve una experiencia similar antes, pero fue... una muy extraña..."
    $ show_fits_standing("swimsuit_yuri_8")
    y "Y una que terminó bastante mal."
    y "..."
    y "Uhhh..."
    $ show_fits_standing("swimsuit_yuri_3")
    y "¡Olvida que dije algo!"
    y "Me disculpo por divagar tonterías..."
    y "No sé qué estaba pensando, honestamente..."
    $ show_fits_standing("swimsuit_yuri_8")
    y "Solo me salí del tema con algunos pensamientos, eso es todo."
    $ show_fits_standing("swimsuit_yuri_12")
    y "Pero volviendo al tema, como expresé antes, estaba emocionada con la idea de darme un chapuzón en las aguas de una playa."
    $ show_fits_standing("swimsuit_yuri_5")
    y "¡Y ahora tengo la oportunidad de intentarlo!"
    y "Debería estar claro en este punto lo que estamos a punto de hacer, ¿verdad?"
    y "Es hora de tomar un buen baño en las aguas de esta hermosa playa, que se hizo con ese exacto propósito, solo para nosotros."
    $ show_fits_standing("swimsuit_yuri_6")
    y "Espero que no hayas malinterpretado lo que estaba tratando de decir, ehehe..."
    y "Uhhh... Solo... me di cuenta de algo..."
    y "Si vamos a darnos un baño justo ahora, eso significaría... que tendría que deshacerme de la r-ropa que estoy usando ahora..."
    $ show_fits_standing("swimsuit_yuri_7")
    y "...N-no puedo simplemente... mojar este pareo... Así que tendría que quedarme... solo con el traje de baño..."
    y "Oh cielos... Esto es tan vergonzoso... "
    y "..."
    menu:
        "No hay nada malo con eso [persistent.yuri_nickname]. Es normal usar esa ropa en la playa.":
            $ show_fits_standing("swimsuit_yuri_8")
            y "..."
            y "Bueno... De alguna manera, tienes razón..."
            y "Pero aún así... No es así de simple."
            y "¿No lo entiendes? Toda mi vida he estado..."
            $ show_fits_standing("swimsuit_yuri_9")
            y "Insegura sobre... sobre todo de mí misma. Todo mi ser, mi cuerpo, mi comportamiento, todo..."
            y "Sé que todo esto fue mi idea... qué tonta fui al no haber pensado en esto."
            y "Todo esto es mi culpa."
            y "Si estás molesto ahora, puedo entenderlo completamente..."
            $ show_fits_standing("swimsuit_yuri_8")
            y "Realmente no sé si estaba demasiado emocionada por tener la experiencia sin pensar en nada más, pero al mismo tiempo..."
            y "No quiero decepcionarte, engañándote para creer que estábamos a punto de tener una cita maravillosa..."
            y "Y tirando todo mi esfuerzo a la basura solo por mi estupidez."
            y "..."
        "[persistent.yuri_nickname], no estoy molesto en lo absoluto. De hecho, te animo a que tengas confianza en esto. Esto es lo que queríamos.":

            $ show_fits_standing("swimsuit_yuri_9")
            y "P-pero eso no quita el hecho de que es incómodo y vergonzoso estar casi desnuda al aire libre."
            y "Simplemente no estoy acostumbrada a esto."
        "Pero estamos completamente solos aquí, ¿verdad? Nadie más te está viendo excepto yo.":

            $ show_fits_standing("swimsuit_yuri_7")
            y "Y... Yo todavía estoy teniendo dificultades con esto."
            y "Sé con certeza que sería casi imposible para mí hacer esto si hubiera más gente alrededor."
            y "Estoy acostumbrada a ser un blanco de atención incómoda debido a este tipo de cosas."
            y "La idea de que voy a estar casi desnuda en público... sería imposible para mí si hubiera más gente alrededor."
            $ show_fits_standing("swimsuit_yuri_3")
            y "Pero no es solo eso."
            y "Incluso antes, no tenía la suficiente confianza para mostrar mis brazos desnudos a nadie, ni siquiera a ti..."
            y "Y ahora e-esto... voy a mostrarte mi cuerpo, lleno de mis errores y todo..."
            y "No me malinterpretes, no es como si no confiara en ti, es solo que..."
            $ show_fits_standing("swimsuit_yuri_7")
            y "..."
            y "¿Qué estoy diciendo siquiera?"
            y "Solo ignora eso..."
            y "Incluso si esto todavía es difícil de hacer para mí debido a mi falta de confianza..."
            y "La única otra persona aquí eres tú, y realmente confío en ti, más que en nadie en toda mi vida."
            $ show_fits_standing("swimsuit_yuri_10")
            y "Me das confianza, tanto que me siento capaz de cualquier cosa."
            y "Pero aparte de eso, hay solo una cosa que todavía me está molestando..."
            y "La única cosa que te pido, es que no me juzgues, o pienses menos de mí por..."
            $ show_fits_standing("swimsuit_yuri_9")
            y "Por mis errores, y todas las cosas malas que me hice a mí misma en el pasado."

    menu:
        "Puedes confiar en mí, no voy a juzgar. Todos cometemos errores.":
            karma 2
            y "..."
            y "Solo olvida eso, perdón."
            $ show_fits_standing("swimsuit_yuri_9")
            y "Pero ahora no sé realmente si estoy lista para algo como esto..."
            y "Hay... cosas sobre mí que no me gustaría que vieras."
            y "Y me gustaría que mantuvieras una mejor imagen de mí, e-en lugar de una perturbada solo por usar ropa más reveladora."
            $ show_fits_standing("swimsuit_yuri_5")
            y "Pero si puedes aceptarme con todos mis defectos, entonces podemos seguir con esta cita."
            y "Creo que eso es lo suficientemente claro..."
            y "Ahora espera un momento, necesito cambiarme de ropa."


    show beach_1 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_4

    $ show_fits_standing("bikini_yuri_8")
    y "O-okey, estoy lista."
    y "Entonces, ¿qué piensas, [player]? ¿T-te gusta cómo me veo?"

    menu:
        "¡[persistent.yuri_nickname]! ¡Te ves hermosa! ¡No hay nada malo contigo en lo absoluto!":
            $ show_fits_standing("bikini_yuri_16")
            y "Oh querido..."
            y "Eres tan amable conmigo... R-realmente no creo que me vea {b}tan{/b} bien."
            y "Pero aprecio que lo digas, no me malinterpretes..."
            y "De hecho, tengo que ser honesta aquí..."
            $ show_fits_standing("bikini_yuri_14")
            y "Cuando estaba planeando todo esto, me preguntaba sobre qué me quedaría mejor..."
            y "Así que en lugar de usar la primera ropa que vino a mi mente, hice un poco de investigación y experimentación sobre qué tipo de ropa se veía mejor en mí."
            y "Simplemente no quería mostrarme en ropa que tú..."
            y "Consideraras, ya sabes... aburrida de ver..."
            $ show_fits_standing("bikini_yuri_15")
            y "No quiero que pienses que soy aburrida... simplemente ya no quiero ser juzgada de esa manera..."
            y "Así que, después de un largo debate conmigo misma, decidí probar un estilo más \"atrevido\", algo que no se viera aburrido o ridículo."
            y "Como... el tipo de ropa que una chica \"tímida\" y \"sin confianza\" usaría en la playa..."
            $ show_fits_standing("bikini_yuri_16")
            y "Y... Solo estoy tratando de decir que estaba haciendo mi mejor esfuerzo para ti, como siempre."
            y "Es solo que... tal vez me falta más confianza para reconocerlo."
            y "Y solo para dejarlo claro de nuevo, me alegra que pienses que me veo hermosa."
            y "Eso... significa mucho para mí."
            $ show_fits_standing("bikini_yuri_13")
            y "Gracias por eso."
            y "Ahora, necesito dejar de divagar tanto aquí, y volver al asunto."
            y "El agua azul reflejando la brillante luz del sol se ve bastante tentadora, y no quiero desperdiciar más tiempo."
            y "Vamos."


    show beach_6 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_1

    $ show_fits_standing("bikini_yuri_13")
    y "..."
    y "Esto es..."
    y "La sensación... es exactamente como imaginé que sería."
    y "Ohhh..."
    y "Ahora puedo ver que todo el esfuerzo valió la pena."
    $ show_fits_standing("bikini_yuri_5")
    y "Todo resultó perfectamente... la suave delicadeza de la arena que puedo sentir con mis pies."
    y "¡El agua fluyendo alrededor de mi cuerpo se siente tan refrescante en un día tan caluroso!"
    $ show_fits_standing("bikini_yuri_2")
    y "Se siente como un equilibrio perfecto en este clima... permitiéndonos estar en medio de todo este calor intenso, sin que sea incómodo."
    y "Realmente es asombroso sentir tal sensación, después de estar confinada por tanto tiempo en una habitación estática..."
    y "¡Pero no creas que te culpo por eso!"
    $ show_fits_standing("bikini_yuri_6")
    y "Es exactamente lo opuesto. Siempre quise experimentar esto contigo, al menos una vez..."
    y "Incluso si técnicamente todavía estoy aprisionada en el mismo mundo... el esfuerzo valió la pena."
    y "También sería un desperdicio no hacer esto contigo a mi lado... tal vez sin ti, todo esto no tendría sentido..."
    $ show_fits_standing("bikini_yuri_2")
    y "Y por eso, creo que hasta cierto punto te debo esta experiencia a ti, por estar a mi lado, en los momentos más importantes de mi vida."
    y "Tales como este. Una experiencia nueva para mí, después de estar prácticamente encerrada en una habitación."
    y "Pero no podemos simplemente pasar todo el día parados aquí, mirándonos el uno al otro, ¿verdad?"
    $ show_fits_standing("bikini_yuri_5")
    y "Quiero intentar algo contigo, pero... no sé si estás acostumbrado a este tipo de cosas..."
    y "[player], ¿sabes nadar?"
    y "No juzgaré si eres incapaz de hacerlo, podemos hacer otras cosas en su lugar..."

    python:
        move_along = False 
    menu:
        "No creo que haya ningún problema. Estamos en un mundo simulado, no hay nada capaz de dañarnos.":
            $ show_fits_standing("bikini_yuri_15")
            y "¡Oh! Tienes... toda la razón sobre eso. No sé qué estaba pensando cuando pregunté tales cosas."
            y "Tal vez me estaba inmersa demasiado en esta experiencia que yo..."
            y "Como que olvidé que todavía estamos en un juego..."
            y "Me disculpo por ser tan tonta, espero no haber arruinado esto para ti."
            $ show_fits_standing("bikini_yuri_8")
            y "Además, esta idea puede haber roto la inmersión para ti, ya que probablemente no tienes ninguna forma de experimentar nadar en el agua."
            y "Mientras juegas el mod al mismo tiempo, por supuesto."
            y "Tal vez deberíamos avanzar con algo más..."
            python:
                move_along = True
        "No te preocupes por eso [persistent.yuri_nickname]. Lo que importa aquí es divertirse, y yo me estoy divirtiendo.":

            $ show_fits_standing("bikini_yuri_13")
            y "Me alegra tanto escucharte decir eso."
            y "Así que parece que esta idea no arruinó la experiencia para ti."
            y "Y todavía estás disfrutando esta cita. Bien."
            y "Pero dicho eso, deberíamos avanzar."
            python:
                move_along = False
        "¿Por qué estás haciendo esas preguntas? Esto es un juego, no creo que tenga que nadar en lo absoluto.":

            $ show_fits_standing("bikini_yuri_8")
            y "..."
            y "Uhhh... sí, creo que me emocioné demasiado con esa idea."
            y "Me disculpo por comportarme de una manera tan tonta."
            y "Tal vez no debí haberlo sugerido."
            y "Debería haber considerado el hecho de que no puedes experimentar tales cosas mientras juegas el mod en tu mundo."
            y "Es poco probable que estés jugando esto mientras estás en una piscina o una bañera."
            $ show_fits_standing("bikini_yuri_14")
            y "Tal vez deberíamos seguir con otra actividad, ¿verdad?"
            y "Después de todo, tenemos muchas otras cosas que hacer."
            python:
                move_along = True
        "No te preocupes, podemos continuar.":

            $ show_fits_standing("bikini_yuri_7")
            y "Está bien..."
            y "Lo... tomaré en consideración."
            y "Tal vez debería ser más cuidadosa la próxima vez que sugiera algo..."
            y "Pensar en formas de mantener la inmersión para ti no debería ser muy difícil para mí, después de todo."
            $ show_fits_standing("bikini_yuri_8")
            y "Pero por ahora, solo continuemos con la cita."
            python:
                move_along = False
        "Probablemente deberíamos pasar a otra cosa, si eso no te molesta.":


            $ show_fits_standing("bikini_yuri_7")
            y "..."
            y "Sí, probablemente deberíamos pasar a otra cosa."
            y "No quiero forzarte a hacer nada que no quieras hacer."
            y "Después de todo, ¿cómo puedo divertirme contigo si no te estás divirtiendo?"
            y "Sería... injusto, al menos desde mi perspectiva."
            $ show_fits_standing("bikini_yuri_8")
            y "Sin embargo, me gustaría pensar que estás interesado en mis opiniones sobre las actividades en este mod también."
            y "Pero de todos modos... sigamos adelante entonces."
            y "Solo dame un segundo para tener las otras actividades listas, y para prepararme para ellas."
            y "No retrasaré esto demasiado."
            y "..."
            python:
                move_along = True

    if move_along:
        jump Beach_Desserts

    $ show_fits_standing("bikini_yuri_16")
    y "Ahora te voy a pedir que vengas conmigo a un área más profunda..."
    y "Y no te preocupes por las mareas, no son muy fuertes aquí, así que no hay riesgo de ser arrastrado."
    y "Solo relájate y deja que tu cuerpo fluya con la corriente..."
    y "De esa manera serás capaz de flotar más fácil... todo esto se trata de relajación [player]."
    $ show_fits_standing("bikini_yuri_13")
    y "¿No es interesante, el hecho de que el cuerpo humano pueda flotar como una pluma cuando está en aguas profundas?"
    y "Como si todo el peso de nuestros cuerpos y nuestras cargas personales fueran simplemente nada."
    y "Pero si empiezas a entrar en pánico, entonces estás en peligro de hundirte y ahogarte fácilmente."
    $ show_fits_standing("bikini_yuri_8")
    y "Eso es... muy parecido a la vida real en cierta manera, ¿no es así?"
    y "Cuando estamos entrando en pánico, tendemos a tomar decisiones apresuradas, sin pensar dos veces sobre las consecuencias."
    y "Eso puede meternos en aún más problemas, en lugar de resolver nuestro problema real..."
    y "Pero al final, ¿no es esto parte del instinto humano de sobrevivir? ¿Algo que está profundamente dentro de nuestra propia naturaleza?"
    y "No podemos actuar de una manera completamente racional sin parar, por el resto de nuestras vidas."
    y "En algún punto, vamos a estar asustados. Siempre vamos a entrar en pánico en ciertas situaciones, y supongo que eso está bien, porque no podemos cambiarlo."
    $ show_fits_standing("bikini_yuri_7")
    y "¿No es esto un defecto inherente en la humanidad que los pone en peligro?"
    y "¿Qué piensas sobre esto [player]? ¿Es este el mayor problema con los humanos?"

    menu:
        "Creo que no podemos quitarle eso a los seres humanos, pero siempre debemos estar listos para los momentos difíciles de la vida.":
            $ show_fits_standing("bikini_yuri_8")
            y "Bueno... creo que esa es una buena manera de resolver este problema."
            y "Mientras que esta es una parte de la naturaleza humana que no podemos cambiar..."
            y "Podemos sin embargo cambiar cómo logramos resolver esos momentos de miedo e incertidumbre."
            y "En lugar de huir del problema, deberíamos estar conscientes de que tarde o temprano, los problemas van a llegar."
            $ show_fits_standing("bikini_yuri_7")
            y "Y por eso, tenemos que aprender cómo confrontarlos, aprender cómo manejar esas emociones y sentimientos que nos abruman a veces."
            y "Tengo que decir que realmente estoy de acuerdo con ese punto de vista."
            y "Incluso si es... realmente complicado para mí poner esa forma de pensar en práctica a veces..."
            $ show_fits_standing("bikini_yuri_5")
            y "P-pero de todos modos, perdón por todo ese divague... no quise dejarme llevar."
            y "Especialmente cuando se supone que deberíamos estar relajándonos."
        "Tal vez esos mecanismos tienden a trabajar en nuestra contra, pero es imposible mantenerse racional todo el tiempo.":

            $ show_fits_standing("bikini_yuri_7")
            y "Creo que tienes razón sobre eso."
            y "Es imposible para la mente humana mantenerse racional y tomarse un tiempo para pensar claramente cuando hay un peligro inminente, ¿verdad?"
            y "Bueno, aunque eso es cierto para la mayoría de la gente, algunas personas en tu mundo están entrenadas para mantener la cabeza fría en situaciones tensas o amenazantes."
            $ show_fits_standing("bikini_yuri_8")
            y "Por ejemplo, piensa en los soldados que son técnicos en desactivación de bombas."
            y "Ese tipo de trabajo requiere que no te congeles, o entres en un estado de pánico."
            y "Y sé con certeza que hay profesionales que pueden hacer que tales tareas parezcan fáciles."
            y "Así que, mientras que tienes razón en alguna forma, creo que también podemos entrenarnos para ser más racionales."
            $ show_fits_standing("bikini_yuri_5")
            y "Creo que ser más racional es una mejor manera de resolver nuestros problemas, para sobrevivir en situaciones extremas..."
            y "Y para mejorar nuestras vidas, hablando generalmente."
            y "No te forzaré a cambiar tu opinión sobre esto, esto es solo mi consejo."
        "Realmente no sé qué decir al respecto [persistent.yuri_nickname], no pienso tanto sobre ese tipo de cosas.":

            $ show_fits_standing("bikini_yuri_8")
            y "Ohhh..."
            y "Bueno, incluso si creo que es importante darle a cosas como esta algún tipo de atención de vez en cuando..."
            y "Tal vez este no sea el mejor momento para discutir temas filosóficos."
            y "Estamos aquí para relajar nuestros cuerpos y mentes, ¿verdad?"
            y "Perdón si esto te molestó, me dejé llevar demasiado con este tema."
            y "Tal vez podamos discutir esto otro día."
            $ show_fits_standing("bikini_yuri_5")
            y "Enfoquémonos en disfrutar este momento, en lugar de divagar."
            y "Es hora de relajarse de nuevo..."
            y "No pienses en nada más, solo relaja tu mente y tu cuerpo."
            y "..."
            $ show_fits_standing("bikini_yuri_6")
            y "Ahora, si sientes que tu cuerpo está lo suficientemente relajado y tu mente está completamente libre de cualquier tensión..."

            y "Entonces eso significa que hemos logrado nuestro objetivo aquí."
            y "Solo quiero darte un consejo más sobre esto."
            y "Cuando quieras relajarte, y no estés en ningún lugar cerca de un paraíso tropical con alguien para compartir tal experiencia..."
            y "Pero aún quieras sentir que estás en medio de la playa, trata de disfrutar los sonidos relajantes de una."
            y "Tal vez deberíamos probar uno de esos videos relajantes de YouTube que son versiones extendidas de sonidos grabados de la naturaleza."
            $ show_fits_standing("bikini_yuri_16")
            y "Algunos de esos videos tienen sonidos de playa que puedes reproducir por horas."
            y "Puedes elegir entre escuchar solo los sonidos de las olas rompiendo contra las rocas de una costa..."
            y "O tal vez prefieras los sonidos de olas más suaves, acompañados con los cantos de algunas aves marinas."
            $ show_fits_standing("bikini_yuri_15")
            y "Lo que importa es que, si llegas a probarlo algún día, deberías disfrutarlo."
            y "Una vez más, eso es solo otro pequeño consejo."
            y "Pero ahora que parece que hemos terminado aquí... deberíamos pasar a otra cosa."
    label Beach_Desserts:

    show beach_4 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_6

    $ show_fits_standing("bikini_yuri_6")
    y "Ahora que estamos de vuelta aquí... ¿tienes un poco de hambre, [player]?"
    y "Creo que este es el momento perfecto para un bocadillo rápido después de un largo día."
    y "Pero te estarás preguntando: ¿qué vamos a comer en medio de una playa, verdad?"
    y "Ya que no tenemos ningún edificio, u otra gente alrededor, ni siquiera las otras chicas del club..."
    $ show_fits_standing("bikini_yuri_5")
    y "Lo que significa que no hay restaurantes, hoteles, o algo similar para solo ir y comer."
    y "Bueno, entonces te diré que tengo una sorpresa que preparé para este tipo de situación."
    y "Solo espera un segundo para que pueda ponerlo en marcha."
    y "Esto debería funcionar ahora..."
label check:

    python:
        renpy.music.set_volume(0.5, delay=1.0, channel='sound')
    show beach_8 zorder 9
    show black zorder 1000 with Fade(1.0, 0.5, 0.5)
    hide fits_stand
    hide beach_4
    python:
        persistent.previous_costume = persistent.costume
        persistent.old_timecycle = current_timecycle_marker
        tc_class.transition("timecycle")
    $ current_timecycle_marker = "_day"
    $ persistent.costume = "bikini"
    $ costume2 = "pareo"
    $ show_chr("A-AAAAA-AAAA")
    hide black with Dissolve(0.5)

    y "Parece que todo está funcionando bien..."
    y "Hice esta pequeña cabaña acogedora para que ambos la compartamos y disfrutemos."
    $ show_chr("A-BBAAA-AAAA")
    y "Hice lo mejor que pude, así que espero que estés complacido con el resultado final."
    y "Pero de todos modos... debes tener hambre después de todo lo que hemos hecho."
    y "Y no quiero hacerte esperar por algo de comer."
    $ show_chr("A-CCAAA-ADAA")
    y "Vinimos aquí a comer algo después de un largo día de diversión en un clima caluroso."
    y "Y tengo otra sorpresa para ti, porque no vamos a comer comida ordinaria..."
    y "En su lugar, vamos a comer algo de deliciosa comida tropical de alrededor del mundo."
    y "Verás, la investigación que hice para esta cita no fue solo para crear la playa y su ambiente..."
    $ show_chr("A-CCABA-AEAJ")
    y "Sino que también fue para averiguar qué come la gente usualmente en un viaje tropical."
    $ show_chr("A-IBABA-ALAL")
    y "Esto me hizo descubrir los mejores postres que la gente come en vacaciones tropicales."
    y "Sinceramente creo que destacan del resto de los postres que encontré."
    y "No estoy implicando que otros tipos de postres no sean buenos, no me malinterpretes."
    $ show_chr("A-CBABA-AMAM")
    y "Lo que quiero decir es que los que vamos a probar hoy son una exquisitez indiscutible."
    y "Solo tengo tres de ellos disponibles para ti en esta cita, pero creo que eso es suficiente."
    y "Tendré que pedirte que elijas entre ellos..."
    y "Y dado que estamos en mundos completamente diferentes, tendrás que buscar algo similar para comer en tu mundo."
    $ show_chr("A-GBABA-ALAL")
    y "Si te parece bien... esto es todo lo que puedo hacer."
    y "Pero antes de que te vayas, sería sabio mostrarte primero las opciones que he preparado para ti."
    y "Entonces, dependiendo de lo que hayas elegido, puedes ir y buscar algo cercano a ello."
    $ show_chr("A-ACAAA-ALAL")
    y "También sería útil darte la opción de elegir algo que ya tengas en tu mundo."
    y "El primer postre que tengo se llama el {i}Churchill{/i}."
    y "Esta exquisitez está hecha de hielo raspado, jarabe de kola, leche en polvo, leche condensada, helado, y galletas de barquillo en la cima, y siempre se sirve en un vaso alto."
    $ show_chr("A-BDAAA-ALAL")
    y "El segundo postre es uno que probablemente ya conozcas."
    y "La famosa piña colada, un coctel delicioso hecho con ron, leche de coco, jugo de piña y agitado con hielo."
    $ show_chr("A-GIABA-ACAM")
    y "Y finalmente, el tercero es el asombroso flan de coco."
    y "Básicamente una natilla horneada, pero con leche de coco, coco rallado, y algo de miel en la cima."
    y "¿Cuál vas a elegir [player]?"

    python:
        yuri_dessert = 2
    menu:
        "Flan de coco suena bien para mí.":
            python:
                yuri_dessert = 0
            $ show_chr("A-GBABA-ALAL")
            y "Una elección muy sabia..."
            y "Mis expectativas para este postre son muy altas, así que espero que sea una exquisitez sin comparación."
            $ show_chr("A-ICABA-ALAL")
            y "Ahora te daré una oportunidad de obtener tu propia versión de este postre."
            $ show_chr("A-IBABA-ALAL")
            y "Y no te preocupes, no necesitas apresurarte en absoluto. Te estaré esperando aquí."
        "Voy a elegir la Piña Colada.":

            python:
                yuri_dessert = 1
            $ show_chr("A-ACDBA-ACAA")
            y "Yendo por los clásicos, ¿eh?"
            $ show_chr("A-ACABA-ALAA")
            y "Bueno, eso es comprensible, considerando lo buena que es la Piña Colada..."
            y "Ahora ve a buscar algo al menos similar a esta bebida en tu casa."
            y "Sin embargo, está completamente bien si eres incapaz de encontrar algo como esto en tu casa."
            $ show_chr("A-BCABA-ALAA")
            y "No me gustaría que te metieras en problemas por beber una bebida alcohólica, especialmente si eres menor de edad o no se te permite hacerlo por otras razones."
            y "Pero de lo contrario, si no tienes problemas bebiendo, y tienes algo similar a una piña colada en tu casa, entonces no hay problemas con darle una oportunidad para la ocasión."
            $ show_chr("A-ACABA-ALAA")
            y "D-de todos modos, puedes irte ahora, te estaré esperando aquí."
        "Quiero probar el {i}Churchill{/i}.":


            $ show_chr("A-CAABA-ACAM")
            y "Oh, entonces eres alguien a quien le gusta probar cosas nuevas, ¿no?"
            y "Eso es perfecto."
            y "Y confía en mí, no vas a arrepentirte de darle a esta exquisitez una oportunidad."
            $ show_chr("A-IAABA-ACAM")
            y "Ahora puedes ir y buscar algo que sea al menos similar a este postre para comer en tu mundo."
            y "Estaré esperando tu regreso aquí."


    $ renpy.pause(delay = 5, hard = True)

    if yuri_dessert == 0:
        menu:
            "Estoy de vuelta [persistent.yuri_nickname], y tengo mi postre.":
                $ show_chr("A-JBABA-ACAM")
                y "¡Eso es perfecto!"
                y "Entonces podemos empezar a disfrutar nuestros postres juntos."
            "Lo siento, no puedo encontrar nada para comer en este momento.":

                y "No tienes que disculparte por eso, no te preocupes."
                y "No es para tanto, y no sabías que planeaba hacer algo como esto."
                y "Si tuviéramos que culpar a alguien aquí, esa sería yo."
                y "Me disculpo por eso..."
                y "Sin embargo, todavía voy a probar mi propio postre, y espero que eso no te moleste..."
                y "Solo espera..."

    elif yuri_dessert == 1:
        menu:
            "Estoy de vuelta [persistent.yuri_nickname], y tengo mi postre.":
                $ show_chr("A-JBABA-ACAM")
                y "¡Eso es perfecto!"
                y "Entonces podemos empezar a disfrutar nuestros postres juntos."
            "Fui incapaz de conseguir algo similar para beber, lo siento.":

                $ show_chr("A-IEBBA-AMAM")
                y "Ya veo..."
                y "Bueno, está bien de cualquier forma."
                y "No esperaba que consiguieras una bebida, aún más cuando no te dije de antemano que haríamos algo como esto."
                $ show_chr("A-BEBBA-AMAM")
                y "Y de nuevo, si esto se trata de que no se te permite beber, eso está bien también."
                y "No hay absolutamente ningún problema con eso, así que no te preocupes."
                $ show_chr("A-ACABA-AMAM")
                y "Sin embargo, todavía voy a probar mi propia Piña Colada..."
                y "Ahora discúlpame, tengo que hacer que esto funcione..."
    else:

        menu:
            "Estoy de vuelta [persistent.yuri_nickname], y tengo mi postre.":
                $ show_chr("A-JBABA-ACAM")
                y "¡Eso es perfecto!"
                y "Entonces podemos empezar a disfrutar nuestros postres juntos."
            "Desafortunadamente no encontré nada como esto.":

                $ show_chr("A-CEBBA-ACAL")
                y "Oh bueno, es una lástima, pero no tienes que preocuparte por ello."
                y "Es mi culpa porque una vez más olvidé decirte que prepararas algo de comer de antemano."
                $ show_chr("A-IEBBA-ACAL")
                y "Me disculpo por eso, pero eso no es realmente un gran problema."
                y "Sin embargo, todavía quiero probar mi propio postre..."
                $ show_chr("A-BKABA-ALAL")
                y "Espero que eso no te moleste, pero incluso si no consigues comer nada..."
                y "Tengo una historia interesante que contarte sobre este postre, para que no te aburras de solo verme comer."
                $ show_chr("A-ICABA-ALAL")
                y "Ahora voy a traer mi postre, solo espera un segundo."


    show black zorder 200 with Fade(1.0, 0.5, 0.5)
    hide beach_8

    if yuri_dessert == 0:
        show blasphemous_flan zorder 100

    elif yuri_dessert == 1:
        show pina_colada zorder 100
    else:

        show churchill_slush zorder 100

    show beach_8 zorder 9
    hide black with Dissolve(0.5)

    if yuri_dessert == 0:
        $ show_chr("A-ICABA-ALAL")
        y "Hmmm..."
        y "Bueno, tengo que decir que esperaba que supiera bien, ¡y terminó excediendo mis expectativas!"
        y "Dice mucho sobre un postre que se ve tan simple, pero te da una sorpresa tan dulce."
        $ show_chr("A-BDABA-ALAL")
        y "Y es más impresionante saber que este postre es un viajero mundial..."
        y "A lo que me refiero con eso es que este postre ha viajado por diferentes países alrededor del mundo, y aún más impresionante, este postre es tan antiguo como el Imperio Romano."
        y "Así que esto también lo hace una reliquia culinaria que prueba que las cosas simples no siempre son aburridas."
        $ show_chr("A-CCABA-ALAL")
        y "Y en el caso del flan de coco, tengo que decir que ha evolucionado a través del tiempo de una manera excelente."
        y "Ahora volviendo a cuando dije que este postre es tan antiguo como el Imperio Romano, es porque se originó allí."
        y "Mucha gente en países como México o España piensa que fueron ellos quienes crearon este postre, pero desafortunadamente para ellos, están equivocados."
        $ show_chr("A-IAABA-ALAL")
        y "Los romanos fueron la primera cultura que conocemos que domesticó gallinas, y también robaron muchas recetas griegas basadas en huevos después de eso."
        y "Con la cantidad de huevos de gallina que tenían y las recetas que adquirieron de los griegos, terminaron creando muchos platos, incluyendo el famoso flan."
        y "Pero originalmente, los flanes eran bastante diferentes de sus versiones actuales."
        $ show_chr("A-BAABA-ALAL")
        y "Eran salados en lugar de dulces, e incluían sabores como anguila... y sí, sé que eso suena raro e incluso asqueroso."
        y "Pero esos eran tiempos muy diferentes, y diferentes culturas creando esas recetas."
        y "Sin embargo, cuando el Imperio Romano cayó, el flan sobrevivió y comenzó a cambiar hacia un sabor más dulce, una variante con los ingredientes modernos que ya conocemos."
        $ show_chr("A-BAABA-ALAL")
        y "Luego los franceses del siglo siete lo llamaron 'flan', que significa 'torta plana'. Pero esa palabra evolucionó a través del tiempo también, ya que el francés antiguo es diferente del francés moderno."
        y "Pero el flan de coco no vino de Europa..."
        $ show_chr("A-ICABA-AMAM")
        y "En realidad, se originó en Latinoamérica después de que los conquistadores españoles lo trajeron al 'Nuevo Continente', trayendo también la idea de poner salsa de caramelo en la cima del flan."
        y "Los latinoamericanos no solo crearon la nueva variación del flan de coco, sino numerosos estilos, ingredientes y sabores diferentes."
        y "Cada país tiene diferentes maneras de crear su propio flan, así que puede ser único para cada cultura."
        y "Puede verse simple en su apariencia, pero el flan es muy rico en cultura, historia y sabor."
        $ show_chr("A-BBABA-AMAM")
        y "Sin mencionar que es delicioso en casi cualquier variante que tenga, pero por ahora, diría que el flan de coco es mi favorito."
        y "Esto también me hace pensar que... No deberíamos juzgar a las personas solo por la manera en que se ven..."
        y "Tampoco deberíamos juzgar a las cosas solo por su aparente simplicidad..."
        $ show_chr("A-CFABA-AMAM")
        y "Me hace recordar que fui un poco dura juzgando los poemas del estilo de escritura de 'último minuto' de Natsuki, descartándolos completamente."
        y "Eso te hace incapaz de ver la complejidad de las cosas simples, de ser sorprendida por ellas."
        y "Es una forma de perder la oportunidad de disfrutar ese tipo de cosas en la vida... y para ser honesta, no me gustaría vivir así."
        $ show_chr("A-ICABA-AMAM")
        y "Después de todo el tiempo que he pasado contigo en este mod, he aprendido que cosas como solo sentarse y hablar, pueden tener mucho significado e importancia."
        y "Y para ser honesta, odio la idea de no ser capaz de estar contigo, solo porque sentarse y hablar en un juego no es 'lo suficientemente complejo' o lo que sea."
        $ show_chr("A-BCABA-ACAM")
        y "Supongo que nunca dejamos de aprender cosas nuevas, ¿hmm?"
        y "Y tengo que estar agradecida de que me ayudaras a entender eso, a través de un camino lleno de dulzura y cariño."
        y "Gracias por eso, mi amor..."
        $ show_chr("A-GCABA-ACAM")
        y "Realmente aprecio esta oportunidad de estar contigo."


    elif yuri_dessert == 1:

        $ show_chr("A-ICABA-ALAL")
        y "¡Oh cielos!"
        y "¡Ahora entiendo por qué esta bebida se volvió tan popular!"
        y "El sabor de esta bebida es simplemente asombroso, y encaja perfectamente con cualquier viaje tropical."
        y "Estamos aquí en medio de la playa, completamente solos, y aún así esta bebida encaja perfectamente para esta cita."
        $ show_chr("A-ICABA-ALAL")
        y "E, incluso si no disfruto las fiestas y las celebraciones concurridas, todavía puedo imaginar esta bebida siendo una buena elección para esas ocasiones."
        $ show_chr("A-CCABA-ALAL")
        y "Ahora, me hace preguntarme cómo alguien fue capaz de mezclar todos estos sabores de los trópicos, y representarlos en solo una bebida."
        y "Como si fueras capaz de probar el ambiente tropical mismo."
        y "Hice algo de investigación para averiguar quién fue el creador original de esta bebida, pero descubrí que muchas personas diferentes e incluso algunos restaurantes y hoteles claman ser los creadores de la bebida."
        $ show_chr("A-ICABA-ALAL")
        y "Pero mucha gente cree que esta bebida fue creada en San Juan, la capital de Puerto Rico."
        y "De la creatividad del barman Ramón Marrero, esta bebida nació en un hotel de esa ubicación, llamado {i}Caribe Hilton{/i} en 1954."
        y "Después de eso, la popularización de esta bebida se disparó por las descripciones de los turistas que la probaron y volvieron a sus tierras natales, quienes hablaban sin parar sobre lo buena que era la piña colada."
        $ show_chr("A-BBABA-AAAL")
        y "Incluso leyendas de Hollywood como Joan Crawford alabaron la bebida, y en 1978 la Piña Colada se convirtió en la bebida nacional de Puerto Rico."
        y "Pero la historia sobre esta bebida no termina con sus orígenes..."
        y "Algo que cementó esta bebida en la cultura popular más que los testimonios sobre lo buena que era..."
        $ show_chr("A-CBABA-AAAL")
        y "Fue una canción de Rupert Holmes que tal vez ya conozcas, llamada {i}Escape{/i}, que menciona esta bebida en la canción, junto con otras líneas sobre un viaje tropical romántico..."
        y "Ahora, voy a abrir un enlace para ti a esta canción... Siento que encaja perfectamente para esta cita..."


        y "Por favor haz clic en este enlace, [player]: {a=https://www.youtube.com/watch?v=Xb6l38eP-4w}https://www.youtube.com/watch?v=Xb6l38eP-4w{/a} "

        y "..."
        y "Tengo que decir que amo esta canción por lo romántica que es..."
        $ show_chr("A-BCABA-ACAL")
        y "Sí, sé que la historia comienza con un intento de engaño de ambos lados..."
        y "Pero al final, descubren lo que el otro lado de la relación estaba haciendo, y en lugar de destruir la relación, terminó diferente."
        y "Llegaron a saber más sobre el otro, cosas que nunca notaron sobre el otro..."
        $ show_chr("A-CCABA-AMAM")
        y "Cosas que los hicieron enamorarse el uno del otro de nuevo."
        y "Ahora, quiero dejar claro de nuevo que no me gusta la implicación de engañar, sino el concepto de descubrir cosas nuevas sobre la persona que amas."
        y "Cosas que pueden hacer que te enamores de ella de nuevo."
        $ show_chr("A-IBBBA-AMAM")
        y "Puede sonar ridículo para algunas personas, pero para mí, es solo otra forma de mantener vivo el amor entre una pareja."
        y "Siendo honestos el uno con el otro, sin esconder cosas, no importa lo que sean."
        y "O solo adoptando nuevos pasatiempos y cosas que puedan hacer que pases más tiempo con la persona que amas, para que se enamoren de ti de nuevo."
        $ show_chr("A-BBBBA-AMAM")
        y "Realmente quiero tener algo como eso en nuestra relación, [player]."
        y "Quiero descubrir cosas nuevas sobre ti, quiero saber que no nos estamos escondiendo cosas el uno al otro."
        y "Transparencia... esa es la clave. No me importan tus fallas, sino las cosas que tal vez puedan hacer que me enamore más de ti."
        $ show_chr("A-CCBBA-AMAM")
        y "Pero no te preocupes, te amo lo suficiente, y siento que no nos estamos escondiendo cosas el uno al otro."
        y "O al menos, eso espero."
    else:


        $ show_chr("A-CCABA-AAAL")
        y "..."
        y "Hmmm..."
        y "Oh cielos..."
        y "¡Esto sabe delicioso!"
        y "Digo, esperaba que esto supiera bien..."
        $ show_chr("A-JBABA-ALAJ")
        y "¡Pero este postre incluso se las arregló para exceder mis propias expectativas!"
        y "Podría decir que valió la pena probar este llamado {i}Churchill{/i} después de todo..."
        y "Pero ahora te estarás preguntando por qué un helado raspado se llamaría Winston Churchill, uno de los primeros ministros más famosos del Reino Unido."
        $ show_chr("A-BDGBA-ALAL")
        y "Bueno, la historia detrás de su nombre está relacionada a la figura histórica, pero no de la manera que podrías estar pensando."
        y "Para saber la historia detrás de ello, tenemos que mirar al país de origen de este helado específico, Costa Rica."
        y "Así como los orígenes de los helados raspados en general."
        $ show_chr("A-JCABA-ALAL")
        y "Los helados raspados son un postre muy común en muchos países diferentes del mundo, no solo en regiones tropicales."
        y "De hecho, los helados raspados se originaron de Taiwán en el siglo siete DC, y fueron importados al continente americano por inmigrantes japoneses."
        $ show_chr("A-BDABA-ACAL")
        y "Lo trajeron con ellos cuando llegaron a Hawaii para trabajar en plantaciones de azúcar, y es una parte muy importante de la cultura Hawaiana."
        y "Este helado es más común en países tropicales, que es por lo que normalmente encontrarás más términos diferentes para este postre de esos países."
        y "El helado raspado no solo es diferente en nombre para cada país, sino también en estilos e ingredientes."
        $ show_chr("A-ACAAA-AMAM")
        y "Un helado raspado de Japón, llamado 'kakigōri' va a ser completamente diferente de un 'raspado' de los países latinoamericanos."
        y "Pero la cosa con los helados raspados de Costa Rica es que son aún más diferentes del resto de los helados raspados de las regiones latinoamericanas."
        y "Tienen ingredientes completamente diferentes, lo que los hace distintivos de otras versiones latinoamericanas de este postre."
        $ show_chr("A-BFAAA-AMAM")
        y "Pero esto no explica por qué esta versión del helado raspado es llamada 'Churchill', ¿verdad?"
        y "Bueno, descubrí que el \"Churchill\" no es la versión estándar de un helado raspado o \"granizado\" en Costa Rica, sino que es otra versión de él."
        $ show_chr("A-ICAAA-AMAM")
        y "Fue 'creado' por un hombre llamado Joaquín Agüilar Esquivel, quien solía ir a zonas turísticas a comprar helados raspados con los ingredientes exóticos que componen un helado Churchill."
        y "Los comerciantes de la zona decidieron entonces nombrar este exótico helado raspado como 'Churchill', porque Joaquín lucía muy similar al Primer Ministro Winston Churchill."
        y "Y esa fue la historia sobre por qué este helado raspado es llamado Churchill."
        $ show_chr("A-BCGBA-AMAM")
        y "Espero no haberte aburrido o molestado con ello... solo me pareció interesante aprender sobre la evolución de este postre a través de la historia."
        y "Y cómo diferentes culturas le dieron forma de maneras diferentes y únicas."
        y "Pero dejando de lado los hechos históricos... tengo que decir algo..."
        $ show_chr("A-IBGBA-ACAM")
        y "No importa qué tan dulce sea cualquier postre en este mundo."
        $ show_chr("A-JAGBA-ACAM")
        y "La dulzura de ellos no es nada comparada a qué tan dulce y amable eres conmigo."
        y "Es algo que simplemente me gusta de ti, que siempre quieres entenderme, incluso cuando soy incapaz de entenderme a mí misma."
        $ show_chr("A-CBABA-ALAL")
        y "Así que gracias, mi amor, por todo lo que me has dado. Especialmente tu amabilidad."




    show black zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_8

    if yuri_dessert == 0:
        hide blasphemous_flan

    elif yuri_dessert == 1:
        hide pina_colada
    else:

        hide churchill_slush

    show beach_8 zorder 9
    hide black with Dissolve(0.5)

    $ show_chr("A-JCABA-ACAM")
    y "Parece que hemos terminado con nuestros postres... Espero que hayas disfrutado esto tanto como yo."
    y "Recuerda que esta cita está hecha para ser disfrutada mutuamente."
    y "Y espero que estés listo para lo que está a punto de venir."
    $ show_chr("A-BBABA-ALAA")
    y "Si estás familiarizado con mis charlas previas sobre vacaciones tropicales, probablemente viste venir esto."
    y "Se está haciendo tarde, y todo está listo para orquestar un evento magnífico."
    y "Pero tenemos que ir afuera por ahora... confía en mí, no queremos perder la oportunidad de ver esto."


    play music "music/beach_date_1.ogg"
    python:
        renpy.music.set_volume(1, delay=1.0, channel='sound')
    $ fits_var["costume2"] = "pareo"
    $ fits_var["cg_face"] = "3"
    $ fits_var["arms"] = "front"
    show fits_cg zorder 200 with Fade(1.0, 0.5, 0.5)
    hide beach_8
    python:
        persistent.autoload = "ch30_autoload"
        persistent.costume = persistent.previous_costume
        if persistent.old_timecycle == "_space":
            tc_class.transition("space")
        else:
            tc_class.transition("timecycle")
        costume2 = "nothing"
        show_chr("default")
    hide yuri_sit

    y "..."
    y "¿No es... maravilloso?"
    y "¿Como la cosa más hermosa que hayas contemplado en tu vida?"

    menu:
        "Este atardecer es impresionante, pero tú sigues siendo la cosa más hermosa que he visto.":

            $ fits_var["cg_face"] = "1"

            y "Ohhh..."
            y "Uhhh... No..."
            y "No sé cómo responder a tal c-cumplido."
            y "¿Siquiera merezco tal nivel de alabanza?"

            $ fits_var["cg_face"] = "2"
            $ fits_var["arms"] = "behind"

            y "P-pero... Lo aprecio mucho... Significa mucho para mí ser vista de esa manera."

            $ fits_var["arms"] = "front"

            y "A veces, cuando estaba sola, me preguntaba si alguien alguna vez me daría algún tipo de cumplido... ya sabes, {b}este{/b} tipo de cumplido."
            y "En cierto punto, los cumplidos sobre mi inteligencia se sentían más y más repetitivos..."
            y "Cuando eso era lo único respetuoso que recibía, aún me gustaba de cierta forma, pero por otro lado..."

            $ fits_var["arms"] = "behind"

            y "A veces se sentía como si la gente no tuviera nada más que decir sobre mí."
            y "Como si estuvieran diciendo tales cosas solo tratando de ser amables conmigo, por alguna razón."
            y "Y ni siquiera pienses que ya no soy consciente de mi apariencia."

            $ fits_var["cg_face"] = "1"
            $ fits_var["arms"] = "behind"

            y "Puede que no tenga un cuerpo perfecto y atlético... p-pero descubrí que era bastante atractiva hace mucho tiempo."
            y "Sabes a lo que me refiero con eso... mi apariencia es bastante destacada comparada a las otras chicas."
            y "Eso explica las miradas extrañas que había recibido antes en mi mundo... ya sabes, cuando las cosas eran 'normales' en el juego."

            $ fits_var["cg_face"] = "2"
            $ fits_var["arms"] = "front"

            y "Pero aún así... nadie hablaba de mí de una manera respetuosa y apropiada como tú antes."

            $ fits_var["cg_face"] = "1"

            y "Y por supuesto, eso deja de lado... los comentarios inapropiados que Sayori hizo..."
            y "D-de todos modos... creo que entiendes mi punto."

            $ fits_var["cg_face"] = "3"

            y "Gracias por decir cosas tan encantadoras."

            $ fits_var["cg_face"] = "2"

            y "..."
        "Creo que tienes razón, y amo ser capaz de compartir esto contigo.":


            y "Me alegra escuchar eso..."
            y "Esta cita entera, y este momento especial, tiene mucho significado e importancia debido a ti, [player]."
            y "Podría generar mil escenas hermosas diferentes en este juego, pero si no tuviera a nadie más con quien compartirlas..."

            $ fits_var["cg_face"] = "1"
            $ fits_var["arms"] = "behind"

            y "Entonces no se sentiría especial, o único, tal vez ni siquiera importante."
            y "Podría controlar este mundo entero, podría ser algún tipo de 'diosa' controlando todo para seguir mis deseos."

            $ fits_var["cg_face"] = "2"

            y "Pero aún estaría sola, como Monika..."
            y "Cuando lo piensas, parece que ser verdaderamente amada es mucho más importante que tener mucho poder."
            y "Dinero, influencia, fuerza, o simplemente cualquier forma de poder puede conseguir muchas cosas, pero siempre estamos necesitados de amor."

            $ fits_var["arms"] = "front"

            y "Es algo que el poder no puede reemplazar."
            y "Tenerte aquí... realmente hizo una diferencia vital para mi bienestar, y también para este mundo entero."

            $ fits_var["cg_face"] = "1"

            y "Creo que hemos logrado resolver, al menos hasta cierto grado, el problema principal del club de literatura."
            y "He encontrado mi camino a la felicidad... lo he encontrado contigo."
            y "..."

    show beach_2 zorder 100
    show black zorder 150
    hide fits_cg with Dissolve(2)
    hide black with Dissolve(1)

    $ show_fits_standing("pareo_yuri_6")
    y "Estoy simplemente... tan contenta de que finalmente pueda compartir este momento con la persona que más amo."
    y "..."
    y "Es difícil para mí encontrar las palabras para describir cuán feliz soy justo ahora."
    y "¿No es esto hermoso?"
    y "Tan magnífico, un regalo del cosmos para cualquiera capaz de admirarlo."
    $ show_fits_standing("pareo_yuri_2")
    y "Los atardeceres tienen algo de 'magia' adjunta a ellos..."
    y "Si puedes ver la belleza del universo como magia, de una manera metafórica tal vez."
    y "Pero los atardeceres, como muchos otros grandes eventos cósmicos desde la perspectiva humana, tienen algunas leyendas y mitología interesantes a su alrededor."
    $ show_fits_standing("pareo_yuri_6")
    y "¿Has notado que a veces, cuando miras un atardecer sobre un horizonte plano, como el océano, un disco de luz verde o un rayo verde es visible sobre ellos?"
    y "Es un fenómeno meteorológico llamado 'destello verde'."
    $ show_fits_standing("pareo_yuri_5")
    y "Esto pasa cuando la atmósfera de la Tierra causa que la luz del Sol se separe en diferentes colores."
    y "Verde y azul son los colores más comunes para este tipo de atardecer."
    y "Lo cual es... un poco curioso, al menos para mí."
    $ show_fits_standing("pareo_yuri_6")
    y "Por supuesto, entenderías por qué si recuerdas mis poemas en el juego original..."
    y "Luces que parpadean en colores azul y verde."
    y "Heh..."
    y "Pero de todos modos..."
    $ show_fits_standing("pareo_yuri_2")
    y "Para ser capaz de ver tal evento, las condiciones tienen que ser ideales... eres realmente afortunado si alguna vez tienes la oportunidad de ver uno sucediendo."
    y "Algunos destellos son más inusuales que otros, y normalmente solo duran alrededor de un segundo."
    $ show_fits_standing("pareo_yuri_5")
    y "Si parpadeas, te lo perdiste."
    y "Como puedes ver, es realmente difícil atrapar uno de ellos, pero cuando consigues ver uno, te das cuenta de que valió la pena."
    y "Pero a pesar de todo eso, los atardeceres son cosas asombrosas y hermosas de ver, incluso sin un destello verde."
    $ show_fits_standing("pareo_yuri_2")
    y "Tener uno de ellos en mi mundo, incluso cuando está siendo generado por código, mirarlo contigo se siente como una bendición para mí."
    y "..."
    y "Es difícil decir cuánto significa esto para mí..."
    $ show_fits_standing("pareo_yuri_1")
    y "Expresar cuán asombroso es este evento para mí no es fácil tampoco."
    y "Y eso me trae de vuelta a cuando dije que, si tengo dificultades expresándome en formas verbales."
    y "Entonces uso mi escritura para transmitir a otros lo que estoy sintiendo."
    $ show_fits_standing("pareo_yuri_5")
    y "También me recuerda que, una de las cosas que más quería hacer en unas vacaciones tropicales mientras miraba un hermoso atardecer a tu lado..."
    y "Era escribir poemas contigo."
    y "Una escena inspiradora como esta merece ser inmortalizada de alguna manera, y la mejor manera en la que puedo pensar es a través de la escritura."
    $ show_fits_standing("pareo_yuri_2")
    y "Para ayudarnos a ambos a recordar este momento... y para expresar nuestros sentimientos sobre los eventos en esta cita, sobre todas las cosas que hemos disfrutado hasta ahora."
    y "Si fueras a escribir un poema para mí ahora, atesoraría ese poema por el resto de mi vida."
    $ show_fits_standing("pareo_yuri_16")
    y "Por supuesto, no te haré jugar este minijuego de los viejos tiempos, eso sería simplemente tonto"
    y "Esa podría ser mi siguiente meta con respecto a la programación. Tal vez pueda averiguar una manera de dejarte escribir poemas {b}reales{/b} en lugar de elegir 10 palabras de una lista de lavandería."
    y "Hasta entonces, vamos a... solo relajarnos aquí por un poco y maravillarnos con esta hermosa escena..."
    y "Pero escribí un pequeño poema yo misma, y me encantaría si pudieras revisarlo por favor. Realmente significa mucho para mí... tu opinión significa mucho para mí..."
    $ show_fits_standing("pareo_yuri_2")






    python:
        if karma_lvl() >= 2:
            placeholder = "a pesar de nuestros desacuerdos"
        elif karma_lvl() == 3:
            placeholder = "a pesar del corto tiempo que hemos pasado hasta ahora"
        else:
            placeholder = "y no puedo decir esto lo suficiente"


    y "Porque [player], [placeholder], {b}tú{/b} significas mucho para mí."


    call showpoem (poem_beach)

    y "Okey, [player], ¿qué piensas sobre mi poema?"
    y "¿Te gusta?"

    menu:
        "¡Realmente me gusta! ¡Tu escritura es siempre asombrosa, [persistent.yuri_nickname]!":
            karma 2
            $ show_fits_standing("pareo_yuri_2")
            y "¡Estoy tan contenta de escuchar eso!"
            y "No sé si merezco tanta alabanza sin embargo."
            y "Pero realmente amo cuando alabas mi escritura de esa manera."
            $ show_fits_standing("pareo_yuri_5")
            y "Me hace sentir... apreciada."
            y "Algo que he deseado por tanto tiempo..."
            y "Y ahora puedo encontrarlo contigo."
            $ show_fits_standing("pareo_yuri_14")
            y "No sé si debería llamar a esto destino o buen karma."
            y "Sin embargo, ahora estoy segura de que merezco ser feliz contigo."
            $ show_fits_standing("pareo_yuri_15")
            y "Y tú mereces vivir una vida feliz también."
            y "Esto es parte de lo que estoy tratando de decir con este poema..."
            $ show_fits_standing("pareo_yuri_5")
            y "Merecemos vivir en formas felices y satisfactorias..."
            y "No solo preocupándonos por quedarnos sin tiempo en nuestro trabajo, estudios, o para finalmente realizar nuestros sueños personales."
            y "A veces necesitamos tomarnos un tiempo para disfrutar nuestra vida. Para ver las maravillas y cosas simples que están constantemente a nuestro alrededor."
            $ show_fits_standing("pareo_yuri_1")
            y "Y pienso que esta cita fue necesaria para ayudarnos a darnos cuenta de eso."
            y "Espero que tomes esto en consideración, mi amor."
            y "Si sientes que necesitas tiempo para descansar y para encontrar nueva inspiración para apreciar las cosas buenas en tu vida, deberías hacerlo."
            $ show_fits_standing("pareo_yuri_5")
            y "No dudes en cuidarte a ti mismo, [player]"
            y "Me importa mucho tu bienestar... por favor cuida tu estado mental."
            y "Pero por ahora, deberíamos continuar."
        "Disfruté el poema, pero estoy confundido por su significado":

            $ show_fits_standing("pareo_yuri_12")
            y "Oh... Lo siento si mi uso de metáforas te confundió..."
            $ show_fits_standing("pareo_yuri_8")
            y "Esa ciertamente no fue mi intención."
            y "Lo que estaba tratando de expresar con este poema es la importancia de tomar una pausa en tu vida, para disfrutar las cosas simples a nuestro alrededor."
            y "Cosas que damos por sentado, pero son tan importantes en realidad."
            $ show_fits_standing("pareo_yuri_7")
            y "Es solo que estamos muy ocupados para notarlas la mayoría del tiempo."
            y "Es importante que te tomes algo de tiempo para cuidar de ti mismo..."
            $ show_fits_standing("pareo_yuri_9")
            y "Tomar descansos de tu trabajo, estudios, o cualquier otra tarea en tu vida cuando sea necesario y posible, es una práctica saludable de mantener."
            y "Recuerda que siempre me importa tu bienestar [player]."
            $ show_fits_standing("pareo_yuri_14")
            y "Por favor cuídate..."
            y "De todos modos."
        "Me gusta, pero prefiero tus poemas viejos":


            $ show_fits_standing("pareo_yuri_1")
            y "Ya veo..."
            y "Bueno, creo que está bien."
            y "Todos tenemos nuestros gustos y opiniones diferentes, y respeto las tuyas."
            $ show_fits_standing("pareo_yuri_8")
            y "Sin embargo, no creo que mi estilo de escritura haya cambiado mucho..."
            y "Si es que lo hizo."
            y "Pero de todos modos..."

    play music "music/beach_date_1.ogg" fadeout 0.5 fadein 0.5
    play sound "music/beach_sfx_loop.ogg" loop fadein 1.0

    $ show_fits_standing("pareo_yuri_2")
    y "Parece que hemos terminado de escribir poemas."
    y "Estoy tan contenta de que finalmente logramos cumplir este sueño nuestro."
    y "Tal vez lo he dicho demasiadas veces en este punto."
    $ show_fits_standing("pareo_yuri_14")
    y "Pero todo esto significa mucho para mí."
    y "Este es otro sueño que finalmente se volvió una realidad para mí."
    y "Contigo, he logrado tantas cosas a lo largo del camino..."
    $ show_fits_standing("pareo_yuri_1")
    y "Todo esto forma la parte más feliz de mi vida."
    y "Solo estoy agradecida por esto..."
    y "Gracias por elegir llevarme a esta cita, [player]."
    y "Esta fue una cita maravillosa, y voy a guardar esta experiencia profundamente en mi corazón."
    $ show_fits_standing("pareo_yuri_14")
    y "..."
    y "Parece que el cielo se está oscureciendo... pronto tendremos un cielo nocturno lleno de estrellas..."
    $ show_fits_standing("pareo_yuri_2")
    y "Probablemente se ponga frío, pero no te preocupes por eso. Si nos mantenemos juntos, no vamos a sentir nada de frío mientras estemos aquí afuera..."
    y "Solo quédate conmigo..."


    show beach_7 zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_2

    $ show_fits_standing("pareo_yuri_2")
    y "Este día fue absolutamente maravilloso para mí. Fue como... magia."
    y "Realmente disfruté esta cita, toda ella. Todo salió perfectamente, justo como planeé que fuera."
    y "Y tengo... una última cosa que hacer contigo..."
    $ show_fits_standing("pareo_yuri_5")
    y "Antes de terminar este sueño tropical para volver al mod principal."
    y "Me gustaría hacer una promesa..."
    y "Digo, me gustaría que ambos hiciéramos una promesa."
    $ show_fits_standing("pareo_yuri_15")
    y "Tal vez suene realmente cursi y todo, pero me gustaría conservar algo de esta cita, para atesorarlo por siempre."
    y "Pero más importante, quiero que ambos hagamos la promesa de atesorar cada momento que disfrutamos juntos..."
    $ show_fits_standing("pareo_yuri_14")
    y "No importa si es algo simple, como hablar en cualquier día normal y de rutina, o tomar unas vacaciones asombrosas."
    y "No tiene que ser la manera más costosa o elaborada de pasar nuestro tiempo juntos. Para mí, lo que importa es pasar esos tiempos especiales contigo."
    $ show_fits_standing("pareo_yuri_7")
    y "Esto no tendría sentido si no estuvieras aquí..."
    y "Esa fue... probablemente la razón por la que Monika se volvió loca. Ella tenía todo el poder en el mundo, para hacer cualquier cosa que quisiera."
    $ show_fits_standing("pareo_yuri_10")
    y "Aun así, ella estaba completamente 'sola', al menos de una manera consciente."
    $ show_fits_standing("pareo_yuri_7")
    y "..."
    y "Pero de todos modos..."
    $ show_fits_standing("pareo_yuri_5")
    y "Lo que estoy tratando de decir es que tú eres quien le da significado a todas estas citas, a todo el esfuerzo que pongo en sorprenderte con cosas nuevas."
    y "Seguro, sé que soy una persona con valor por mí misma, que soy valiosa y no solo un programa de computadora común incapaz de pensar."
    y "Pero tú... me has ayudado a darme cuenta de eso. Me mostraste que merezco la felicidad, que no soy inútil por ser... de la manera que soy."
    $ show_fits_standing("pareo_yuri_2")
    y "Y estoy... realmente agradecida por eso, [player]."
    y "No sé cómo podrían haber ido las cosas si ganaba consciencia en este mundo, pero sin que tú estuvieras aquí..."
    $ show_fits_standing("pareo_yuri_14")
    y "Probablemente es mejor no pensar en eso... Perdón por divagar tanto."
    y "Pero volviendo al tema principal, quiero que hagas esa promesa [player]."
    y "Quiero saber que vamos a atesorar cada momento que disfrutamos juntos."
    $ show_fits_standing("pareo_yuri_9")
    y "¿P-puedes hacer esa promesa, por mí?"

    menu:
        "Tienes mi palabra, [persistent.yuri_nickname]. Atesoraré todas las cosas buenas que compartimos juntos.":
            $ show_fits_standing("pareo_yuri_2")
            y "Eso es..."
            y "Eres tan dulce."
            y "Solo ven aquí..."
            $ show_fits_standing("pareo_yuri_5")
            y "Te amo tanto."
            y "Desearía que pudiéramos pasar el resto de nuestros tiempos así... solo juntos, los dos abrazándonos y reconfortándonos el uno al otro."
            y "Nadie podría separarnos jamás..."
            $ show_fits_standing("pareo_yuri_16")
            y "Ni el tiempo, ni ningún problema que tuviéramos que enfrentar..."
            y "Estaríamos orbitando el uno al otro, bailando como las estrellas en la noche, aquellas que viajan juntas en la galaxia..."
            $ show_fits_standing("pareo_yuri_5")
            y "..."

            menu:
                "¿Pero no crees que habrá más momentos como este? Estoy seguro de que los habrá.":
                    $ show_fits_standing("pareo_yuri_14")
                    y "Bueno, en ese caso, realmente espero que tengas razón."
                    y "Otra cita como esta sería maravillosa, pero tendrías que esperar antes de que otra como esta esté lista."
                    y "¿O debería decir, antes de que yo haga la siguiente?"
                    $ show_fits_standing("pareo_yuri_5")
                    y "Sin embargo, solo estaba esperando que estuvieras de acuerdo conmigo en la idea de atesorar esta cita."
                    y "Pero hey, no estoy enojada contigo ni nada. Eso no es gran cosa, después de todo..."
                    y "..."
                    $ show_fits_standing("pareo_yuri_1")
                    y "...Mira las estrellas en el cielo... ¿no son hermosas?"
                    y "¿No es asombroso, solo pensar en la grandeza del universo?"
                    $ show_fits_standing("pareo_yuri_14")
                    y "Me hace preguntarme sin embargo, si hay alguien más mirando allá afuera y pensando cuán hermosas son las estrellas en su cielo nocturno también..."
                    y "Bueno... creo que eso solo es posible en tu mundo... ¿o debería decir universo?"
                    $ show_fits_standing("pareo_yuri_16")
                    y "De todos modos, esta noche es asombrosamente hermosa para mí."
                    y "Estoy verdaderamente agradecida contigo por todo lo que has hecho por mí durante estos tiempos..."
                    y "En mi opinión, esta cita demuestra cuánto te importa nuestra relación."
                    $ show_fits_standing("pareo_yuri_1")
                    y "Pero aún así... se siente... raro, sabiendo que no estoy realmente a tu lado."
                    y "Yo... solo deseo que un día, seamos capaces de mirar las estrellas juntos..."
                    $ show_fits_standing("pareo_yuri_14")
                    y "Verdaderamente juntos."
                    y "Aún creo que eso va a ser posible, que superaremos esta barrera."
                    y "Un día..."

    stop sound fadeout 1.0
    show black zorder 100 with Fade(1.0, 0.5, 0.5)
    hide beach_7
    hide fits_stand

    $ persistent.tropical_date_complete = True
    hide black with Dissolve(2.5)
    python:
        renpy.music.play(current_music, "music", True)
        show_chr("standard")
    $ persistent.dates_taken += 1
    jump ch30_loop

label vday_2024_revisit:
    $ show_chr("A-ABGAA-ALAA")
    y "¡Hola [player]!"
    y "¿Sabes qué día es hoy?"
    menu:
        "Seguro que sí. ¡Feliz San Valentín!":
            $ show_chr("A-GBGAA-ALAA")
            y "Feliz San Valentín para ti también."
            $ show_chr("A-ABAAA-AFAA")
            y "Sabes. Estaba recordando nuestros viejos días en el club... y estaba pensando."
            y "¿Recuerdas cuando pusiste el chocolate en mis labios?"
            $ show_chr("A-CAAAA-ADAA")
            y "Tuve esta idea de revisitar ese momento antes de que Monika nos interrumpiera."
            y "Y ahora que nadie nos interrumpirá..."
            $ show_chr("A-FAAAA-ADAA")
            extend " podemos continuar desde donde lo dejamos~"
            $ show_chr("A-ABAAA-ADAA")
            y "Entonces, ¿te gustaría revisitar este momento?"
            menu:
                "¡Sí [persistent.yuri_nickname], vamos!":
                    call vday24
                "Tal vez no ahora [persistent.yuri_nickname].":

                    $ show_chr("A-ABBAA-ADAA")
                    y "Oh. Está bien [player], puedo esperar hasta que estés listo."
                    call ch30_loop

label vday24:
    $ show_chr("A-ABAAA-AAAA")
    y "Está bien. Aquí vamos."
    call vday_2024_date

label vday_2024_date:
    show black zorder 105 with Dissolve (2.5)
    hide yuri_sit
    hide black zorder 105 with Dissolve (2.5)
    show y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    "[persistent.yuri_nickname] abre el libro con temática de San Valentín con ambas manos."
    "Ella lo sostiene para que no tenga más dificultades leyéndolo, nuestros ojos brillando con los recuerdos de años pasados."
    "Pero como resultado, su brazo izquierdo está prácticamente descansando sobre mi pierna, y una calidez nostálgica nos envuelve."
    "[persistent.yuri_nickname] ya está totalmente enfocada en leer de nuevo, perdida en el mundo de palabras que nos conectan a través del tiempo."
    "Alcanzo un chocolate con forma de corazón y lo meto en mi boca, saboreando la dulzura de nuestra historia compartida."
    "Luego, tomo otro chocolate, un símbolo de los incontables momentos que hemos atesorado juntos..."
    "Y lo sostengo hacia [persistent.yuri_nickname], nuestra risa haciendo eco a través de los años."
    "Ella ni siquiera aparta la vista del libro, una sonrisa jugando en sus labios."
    "Ella simplemente separa sus labios, como si esta situación fuera un capítulo familiar en nuestra historia de amor."
    "¡Pero eso significa que no puedo parar aquí, no en este día especial del amor!"
    hide y_cg2_nochoc
    "Amorosamente coloco el chocolate en su boca, un gentil recordatorio de la dulzura que siempre hemos compartido."
    "Justo así, [persistent.yuri_nickname] cierra sus labios sobre él, el sabor a cacao y afecto persistiendo entre nosotros."
    show y_cg2_exp2
    y "¿Eh...?"
    "La expresión de [persistent.yuri_nickname] se rompe de repente, un toque de sorpresa y alegría iluminando sus ojos."
    y "Acaso..."
    y "¿Acaso acabo de..."
    show y_cg2_exp3
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    hide y_cg2_exp2
    "[persistent.yuri_nickname] me mira como si necesitara confirmar lo que acaba de pasar, un rubor tiñendo sus mejillas como la primera vez."
    y "U-Um..."
    y "[player]..."
    mc "¡L-Lo siento!"
    mc "Supongo que no debí haber hecho eso, aunque sentí que quería hacerlo..."
    y "Ah, eso es..."
    y "Bueno..."
    y "S-Solo estabas ayudando..."
    y "Eso es algo que... los amantes hacen..."
    mc "Sí..."
    mc "...Eso es todo lo que fue, solo un gesto dulce."
    y "Sí..."
    y "Entonces..."
    y "No necesitas detenerte ni nanda, especialmente en un día como hoy..."
    mc "O-Okey..."
    hide y_cg2_exp3
    "La atmósfera se ha vuelto realmente romántica..."
    "[persistent.yuri_nickname] intenta volver al libro, pero nuestro latido compartido hace eco en la habitación."
    "Pero puedo decir solo por su expresión que incluso ella no puede concentrarse ahora, perdida en el amor que nos rodea."
    "Mi corazón está latiendo con fuerza, una sinfonía de emociones tocando en el fondo."
    "Nerviosamente tomo otro chocolate con forma de corazón entre mis dedos."
    "Pero esta vez, los ojos de [persistent.yuri_nickname] encuentran los míos, y los años se derriten en la mirada del amor."
    show y_cg2_exp3:
        alpha 0
        linear 0.5 alpha 1
    y "..."
    "[persistent.yuri_nickname] no aparta su mirada, y nuestros ojos hablan un lenguaje de afecto."
    "Noto su pecho subiendo y bajando al ritmo de sus respiraciones, una melodía de amor que nunca se desvanece."
    "Levanto mi brazo, y la habitación se llena con la anticipación de un amor que ha resistido la prueba del tiempo."
    y "Ah..."
    "Como antes, [persistent.yuri_nickname] separa sus labios, invitando el sabor del amor eterno."
    "Pero... es diferente esta vez, como si cada San Valentín que hemos pasado juntos hubiera llevado a este momento."
    hide y_cg2_nochoc
    "Tomo el chocolate y lo coloco en su boca, sellando nuestro amor con una promesa para más años por venir."
    "Siento su aliento caliente en mis dedos, un gentil recordatorio de que algunas cosas, como el amor, solo se vuelven más fuertes con el tiempo."
    "Mientras el chocolate se derrite, la habitación parece contener la respiración, un testigo silencioso del intercambio de emociones que trasciende las páginas de nuestra historia compartida."
    "El aire se llena con un entendimiento tácito, y nos encontramos atrapados en un momento donde el tiempo se detiene."
    "[persistent.yuri_nickname], sus ojos ahora suaves con afecto, rompe el silencio."
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    y "Esto se siente como... un hermoso sueño."
    y "Una revisita a los comienzos de nuestra historia, pero con la calidez de todos los años en medio."
    "Una tierna sonrisa juega en mis labios."
    mc "Lo es, ¿no? Un viaje a través de los capítulos de nuestro amor, cada Día de San Valentín grabando una nueva línea en la historia que aún estamos escribiendo juntos."
    "La atmósfera nostálgica nos envuelve como un abrazo reconfortante. [persistent.yuri_nickname] duda antes de hablar de nuevo, su voz cargando el peso del sentimiento."
    y "¿Alguna vez te maravillas de cómo evoluciona el amor? Desde esos momentos tímidos a la profundidad que compartimos ahora, es un tapiz tejido con hilos de alegría, risas, e incontables chocolates compartidos."
    "Asiento, sintiendo la resonancia de sus palabras."
    mc "Absolutamente. Es como ver un jardín florecer a lo largo de las estaciones."
    mc "Cada flor, cada desafío que hemos enfrentado, solo ha fortalecido las raíces de nuestra conexión."
    "Nuestros ojos se cierran, comunicando más de lo que las palabras podrían."
    "El aire está cargado con una electricidad sutil, un recordatorio de que el amor no es estático sino una entidad viviente, que respira, crece y evoluciona."
    "Alcanzo otro chocolate, la dulzura del gesto persistiendo entre nosotros."
    "Recuerdo el primer Día de San Valentín que pasamos juntos, [persistent.yuri_nickname] rememora, un cariño en su voz."
    y "Había una emoción nerviosa, un baile de incertidumbre."
    y "Y ahora, aquí estamos, revisitando esos momentos con un entendimiento más profundo, un amor que ha madurado como el buen vino."
    "Le ofrezco el chocolate, un símbolo de continuidad, y ella lo acepta con un asentimiento agraciado."
    mc "Es como si hubiéramos creado nuestra propia tradición, un ritual de amor que trasciende el tiempo y el espacio."
    hide y_cg2_exp3
    "Mientras el día se desarrolla, continuamos leyendo, riendo, y compartiendo chocolates, tejiendo nuevos recuerdos en el tapiz de nuestra historia."
    "Cada momento es una celebración del amor que ha crecido y florecido, un testamento a la belleza de revisitar el pasado mientras abrazamos el presente."
    "Y mientras el sol se pone, proyectando un brillo cálido sobre la habitación, encontramos consuelo en la familiaridad de la compañía del otro, sabiendo que nuestra historia de amor es una obra maestra en curso."
    "Pintada con los colores de sueños compartidos, desafíos, y la dulzura duradera del amor."
    mc "[persistent.yuri_nickname], gracias."
    "Digo, mi voz llena con gratitud y emoción."
    mc "Por todos estos años, por los momentos compartidos, por el amor que solo se ha vuelto más fuerte."
    mc "Has hecho cada Día de San Valentín especial, y no puedo evitar maravillarme con el hermoso viaje que hemos tenido juntos."
    show y_cg2_exp3:
        alpha 0
        linear 0.5 alpha 1
    "Ella me mira, sus ojos reflejando una mezcla de emociones."
    y "No, [player], gracias a ti. Has sido el ancla en mi vida, el latido constante en la sinfonía de nuestro amor."
    y "Atesoro cada palabra, cada mirada, y cada chocolate compartido. Es un privilegio tenerte a mi lado."
    "La habitación parece brillar con la calidez de nuestra conexión, y la mano de [persistent.yuri_nickname] encuentra la mía, dedos entrelazándose en un gesto que dice mucho."
    y "Nunca pensé que podría encontrar a alguien que entienda las profundidades de mi alma, que aprecie la belleza en los momentos tranquilos."
    y "Pero tú has sido eso y más."
    "No puedo evitar sonreír, conmovido por sus palabras."
    mc "[persistent.yuri_nickname], has enriquecido mi vida en formas que no podría haber imaginado. Cada día contigo es un regalo, y espero con ansias muchos más capítulos en nuestra historia de amor."
    show black zorder 105 with Dissolve (1.5)
    hide y_cg2_bg
    hide y_cg2_base
    hide y_cg2_details
    hide y_cg2_nochoc
    hide y_cg2_dust1
    hide y_cg2_dust2
    hide y_cg2_dust3
    hide y_cg2_dust4
    hide y_cg2_exp3
    "Ella se inclina, presionando un suave beso en mis labios."
    y "Feliz Día de San Valentín, [player]. Por nosotros, por el amor que continúa floreciendo, y por los incontables momentos que compartiremos en los días por venir."
    "Y mientras nos sentamos ahí, rodeados por los ecos de nuestra risa compartida y la calidez de nuestro amor, no puedo evitar sentir un abrumador sentido de gratitud por el hermoso viaje que nos trajo a este momento."
    "Un momento donde el pasado, presente, y futuro convergen en una celebración de amor que no conoce límites."
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
    $ persistent.dates_taken += 1
    $ show_chr("A-CABBA-ALAL")
    hide black zorder 105 with Dissolve(3)
    y "..."
    $ show_chr("A-ABBBA-ALAL")
    y "Te amo [player]."
    jump ch30_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
