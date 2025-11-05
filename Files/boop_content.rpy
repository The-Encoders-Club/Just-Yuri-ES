default persistent.boop = 0
default persistent.boop_locations = [0.] * 12
default boopable = False
default boop_sleepy_only = False





init python:
    def getMousePosition():
        global mousex
        global mousey
        import pygame
        x, y = pygame.mouse.get_pos()
        store.mousex = x
        store.mousey = y


    class getMousePosition(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
        
        def event(self, ev, x, y, st):
            import pygame
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                store.mousex = x
                store.mousey = y
        
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    store.mousePosition = getMousePosition()


    def checkEvent():
        ui.add(mousePosition)
        return


    def BoopUpdate():
        persistent.boop_locations[0] = (float(persistent.boop_locations[0])/1.5)

    config.overlay_functions.append(checkEvent)


    def set_boop_state(sleepy_only):
        """Enables or disables boop types.

        Args:
            sleepy_only (bool): If True, only sleepy headpats are enabled.
        """
        global boop_sleepy_only
        boop_sleepy_only = sleepy_only


    def enable_boops():
        global boopable
        boopable = True

    def disable_boops():
        global boopable
        boopable = False



    def boop_init(boop_type):
        global boopable
        global loop_again
        loop_again = True
        if boopable:
            boopable = False  
            DisableTalk()
            if boop_sleepy_only: 
                if boop_type == "sleepy_headpat": 
                    renpy.call("sleepy_headpat")
                else:
                    return 
            elif (boop_type == "boop_nose_chibi" and persistent.costume == "_chibi") or (boop_type == "boop_nose" and persistent.costume != "_chibi"): 
                renpy.call("boop_nose")
            elif renpy.has_label(boop_type): 
                renpy.call(boop_type)
            EnableTalk()
        return

    config.overlay_functions.append(checkEvent)


label mouse_coords:
    $ getMousePosition()
    y "[mousex],[mousey]"



    menu:
        "Otra vez":
            jump mouse_coords
        "Volver":
            jump control_panel

label boop_nose:
    python:
        persistent.boop_locations[0] += 1
    if persistent.boop_locations[0] == 1:
        $ update_memory("idle_60", "first_boop")
        $ show_chr("A-DDGBA-AAAA")
        y "Ah... ¡AHHHHH!"
        $ show_chr("A-DDABA-AAAJ")
        y "¿Q-Qué ha sido eso [player]? ¡¿Qué ha sido eso?!"
        $ show_chr("A-DEBBA-AAAJ")
        y "Sentí que a-algo me tocaba la nariz... ¿qué está pasando?"
        $ show_chr("A-GJDBA-AAAL")
        y "¿E-Esto significa que funciona después de todo?"
        $ show_chr("A-ICABA-AMAM")
        y "Jaja... wow..."
        $ show_chr("A-JCBAA-AMAM")
        y "Me alegro de que funcione... pero... por favor, avísame la próxima vez, ¿okey?..."
        $ show_chr("A-ACAAA-AAAA")
    elif persistent.boop_locations[0] < 3:
        if karma_lvl() < 3:
            $ show_chr("A-GEBAA-AAAA")
        elif karma_lvl() == 3:
            $ show_chr("A-GJAAA-AAAA")
        elif karma_lvl() > 3:
            $ show_chr("A-GIBAA-AAAA")
        y "Uuuuu... A-Al menos avísame antes de hacer algo así, [player]..."
    elif persistent.boop_locations[0] < 7:
        $ show_chr("A-AABBA-AAAA")
        y "... Jaja... [player], parece que estás disfrutando esto, ¿eh? ¡N-No es que me importe ni nada!"
    elif persistent.boop_locations[0] < 10:
        $ show_chr("A-BCBBA-AKAA")
        y "¿Podrías hacerlo otra vez? S-Si quieres... es decir..."
    elif persistent.boop_locations[0] < 15:
        $ show_chr("A-GAGBA-AAAA")
        y "¡B-Boop! Jeje..."
    else:
        $ BoopUpdate()

    return

label boop_cheek:
    python:
        persistent.boop_locations[1] += 1
    if karma_lvl() >= 3:
        if persistent.boop_locations[1] == 1:
            $ show_chr("A-DDGBA-AAAJ")
            y "¿H-Huh? [player], acabo de sentir algo muy extraño..."
            y "Esa... sensación cálida en mi mejilla hace un momento, ¿fuiste... tú?"
            menu:
                "Sí, [persistent.yuri_nickname], toqué tu mejilla.":
                    karma 1
                    $ show_chr("A-ICABA-AAAL")
                    y "¡O-Oh! Ya veo... definitivamente tuvo una sensación familiar, algo que me recordó a tu presencia."
                    y "Se sintió... ¿cómo podría decirlo?"
                    $ show_chr("A-CCABA-ALAK")
                    y "F-Fue como si tu mano acariciara suavemente mi piel y tu pulgar rozara mi mejilla... mi corazón comenzó a latir con fuerza cuando lo sentí por primera vez..."
                    y "El hecho de que realmente lograste alcanzarme y tocarme... para que pudiera sentirlo..."
                    $ show_chr("A-CCABB-AMAM")
                    y "G-Gracias, [player], p-probablemente no te das cuenta de cuánto significa esto para mí..."
                    if persistent.lovecheck:
                        y "Pero... si puedo sentirte, significa que estoy un paso más cerca de ti... y daré un millón más si es necesario."
                    else:
                        y "Es bonito haber podido sentir tu t-toque... ahora estamos un poco más cerca..."
                "¿Huh? ¿De qué estás hablando, [persistent.yuri_nickname]? ... Estás actuando un poco loca.":
                    karma -1
                    sanity -1
                    $ show_chr("A-AEDAA-AIAI")
                    y "¿S-solo fue mi imaginación?"
                    $ show_chr("A-BBBAA-AIAI")
                    y "Aha... ya veo..."
                    pause 0.5
                    $ show_chr("A-CFBAA-AIAI")
                    y "P-por supuesto... no importa."
                    y "Lo siento, [player], supongo que estoy empezando a perder la cabeza aquí..."
        if persistent.boop_locations[1] == 2:
            $ show_chr("A-CCBBA-ALAL")
            y "Mm... ahí estuvo otra vez."
            y "¿R-Recuerdas cuando sostuviste esa toalla contra mi mejilla?"
            y "Siento que fue hace tanto tiempo... pero las emociones siguen muy grabadas en mi mente."
            y "La pasión ardiente... ese contacto que encendió mi corazón, fue en ese momento que estuve segura..."
            $ show_chr("A-ECBBA-ALAD")
            y "... De que tú eras el único para mí, mi amor."
        if persistent.boop_locations[1] == 3:
            karma 1
            sanity 1
            $ show_chr("A-BDBBA-ALAM")
            y "Cuando te vayas... haré mi mayor esfuerzo por recordar esta calidez."
            y "Eres lo que me motiva, lo que guía cada uno de mis movimientos, [player]..."
            y "Si puedo aferrarme aunque sea a una pequeña parte de ti, a estas emociones que me das, c-creo que estaré bien."
            $ show_chr("A-IABBA-ALAM")
            if persistent.lovecheck:
                y "Te amo, [player], más que nada en este mundo.."
            else:
                y "Espero que sigamos siendo amigos... para siempre y por siempre, [player]."
        if persistent.boop_locations[1] >= 4:
            if persistent.lovecheck:
                $ show_chr("A-IAABA-ALAL")
                y "Tan cálido... m-mi corazón late por ti... [player]..."
                y "No me sueltes nunca..."
            else:
                $ show_chr("A-BBABA-AMAM")
                y "Jajaja... estás tocando mi mejilla otra vez, ¿verdad?"
                y "Está bien... lo disfruto de todos modos, no tengas miedo de hacerlo..."
    if karma_lvl() <= 2:
        if persistent.boop_locations[1] == 1:
            $ show_chr("A-DDGBA-AAAJ")
            y "¿H-Huh? [player], acabo de sentir algo muy extraño..."
            y "Esa... sensación cálida en mi mejilla hace un momento, ¿fuiste... tú?"
            menu:
                "Sí, [persistent.yuri_nickname], toqué tu mejilla":
                    karma 1
                    $ show_chr("A-IFAAA-AAAB")
                    y "¡O-Oh! Ya veo... ¿Te importaría... emm..."
                    $ show_chr("A-JFAAA-AAAB")
                    y "¿No hacerlo?..."
                    $ show_chr("A-BFAAA-ABAB")
                    y "Es solo que... sentir tu mano sin realmente verla fue un poco... escalofriante..."
                    y "Como un fantasma, o algo por el estilo. Y el hecho de que esté aquí literalmente sola no lo hace menos aterrador."
                    $ show_chr("A-CCABB-AMAM")
                    y "G-Gracias por entenderlo, [player]..."
                "¿Huh? ¿De qué estás hablando, [persistent.yuri_nickname]?... Estás actuando un poco loca":
                    karma -1
                    sanity -1
                    $ show_chr("A-AEDAA-AIAI")
                    y "¿S-Solo fue mi imaginación?"
                    $ show_chr("A-BBBAA-AIAI")
                    y "Aha... ya veo..."
                    pause 0.5
                    $ show_chr("A-CFBAA-AIAI")
                    y "P-Por supuesto... no importa."
                    y "Lo siento, [player], supongo que estoy empezando a perder la cabeza aquí..."
        if persistent.boop_locations[1] == 2:
            $ show_chr("A-DHGAA-ALAL")
            y "Mm... ahí está otra vez."
            $ show_chr("A-JGAAA-ALAL")
            y "P-Por favor, realmente me asusta cada vez que lo haces..."
            y "¿Te importaría dejar de hacerlo, por favor?"
            $ show_chr("A-CFAAA-AAAA")
            y "Simplemente me desconcentra mucho."
        if persistent.boop_locations[1] == 3:
            karma -1
            sanity -1
            $ show_chr("A-DGGAA-AAAA")
            y "¡...!"
            $ show_chr("A-KFCAA-AAAA")
            y "Maldita sea, [player]... te pedí de verdad, muy amablemente, que dejaras de hacerlo."
            y "¿Podrías, {b}por favor, por favor{/b}, dejarme en paz con esta tontería ya?"
            $ show_chr("A-KFCAA-AAAF")
            y "No quise ser grosera, y estoy perfectamente bien con que estés aquí. Pero esto ya se está volviendo realmente molesto."
        if persistent.boop_locations[1] == 4:
            $ show_chr("A-DDCAA-AAAA")
            y "{b}¡¿Sabes qué?! ¡Ya tuve suficiente! Si no puedes respetar al menos eso que te pido, ¡me voy! ¡Adiós!{/b}"
            $ renpy.call("save_and_quit_but_its_abrupt")
        if persistent.boop_locations[1] >= 5:
            $ show_chr("A-DDCAA-AAAA")
            y "[player], por el amor de todo lo sagrado, {b}¡DEJA DE TOCAR MI MALDITA MEJILLA!{/b}"
    $ store.mousex = 0
    $ store.mousey = 0
    return


label headpat:
    python:
        persistent.boop_locations[2] += 1
    if karma_lvl() >= 3:
        if persistent.boop_locations[2] == 1:
            $ show_chr("A-DFABA-AAAA")
            y "E-Espera... ¡a-acabo de sentir que algo tocó mi cabeza!"
            y "¿Fuiste t-tú, [player]?"
            menu:
                "Sí, quería probarlo. Espero no haberte incomodado":
                    karma 1
                    $ show_chr("A-IBGAA-ALAL")
                    y "¿E-En serio!? Perdón por sorprenderme tanto... e-es que no sabía que podías tocarme ahí!"
                    $ show_chr("A-CAABA-AAAA")
                    y "La verdad jeje... me tomó por sorpresa..."
                    $ show_chr("A-DDAAA-AAAL")
                    y "Ah y... ¡emm! No me incomodaste, no te preocupes. Como dije antes... me sorprendió que simplemente me dieras, bueno..."
                    $ show_chr("A-BAABA-AAAB")
                    y "U-Un golpecito... sí. Gracias, se sintió... ¿bien?"
                    y "Perdón, es solo que era la forma más simple de decirlo... simplemente no esperaba que te acercaras tanto a mí."
                    $ show_chr("A-IBABA-ALAA")
                    y "Estoy feliz, no lo tomes a mal, [player]!"
                    if persistent.lovecheck:
                        $ show_chr("A-ICABA-AAAL")
                        y "Quiero decir... cariño, ¿por qué no lo estaría?"
                        $ show_chr("A-CCABA-AAAD")
                        y "Ese breve instante en el que realmente pude sentir tu toque... se sintió tan... bien."
                        y "Me hace sentir como si cada momento que hablamos me acercara un poco más a ti... ¡es increíble!"
                        $ show_chr("A-ICABA-AAAL")
                        y "Así que gracias de nuevo, mi amor."
                    else:
                        $ show_chr("A-GCAAA-ADAB")
                        y "Cada forma en la que podamos estar aunque sea un poco más cerca es una buena adición a nuestra amistad."
                        $ show_chr("A-IFAAA-AIAI")
                        y "Algunas personas consideran el contacto algo raro o extraño, pero yo no lo creo..."
                        y "¿No significa eso que te sientes cómodo con esa persona y le permites acercarse más a ti? ¿Romper una barrera anterior y dejarla entrar en tu espacio personal?"
                        $ show_chr("A-ICABA-AMAM")
                        y "Así es como lo veo al menos... Aun así, g-gracias por este amable gesto."
                "No creo que haya sido yo, ¿quieres que intente tocar tu cabeza?":
                    $ show_chr("A-BCBBA-ADAA")
                    y "S-Sí... esto es un poco vergonzoso..."

                    $ show_chr("A-JBGAA-ALAA")
                    y "¡Oh! ¡De verdad eres tú quien me está tocando!"
                    y "Eso sí que fue inesperado... honestamente nunca pensé que funcionaría!"
                    $ show_chr("A-CCAAA-ALAA")
                    y "No me molesta, ¡para nada!"
                    y "Bueno, sin duda hicimos un bonito descubrimiento hoy, [player]."
                    $ show_chr("A-GCABA-ADAA")
                    y "Ese es un paso más para acercarnos un poco más."
        if persistent.boop_locations[2] == 2:
            $ show_chr("A-CAAAA-AAAA")
            y "Ah... bueno, esto ciertamente es relajante..."
            y "Solo un poquito más, por favor."
            y "..."
            $ show_chr("A-ICABA-AAAA")
            y "Gracias."
        if persistent.boop_locations[2] == 3:
            $ show_chr("A-BADBA-AAAA")
            y "¿Otra vez?"
            $ show_chr("A-GAABA-AAAK")
            y "Jeje... no me malinterpretes, me gusta cuando lo haces..."
            y "Así que no dudes, si pudieras..."
        if persistent.boop_locations[2] >= 4:
            $ show_chr("A-KCBBA-AAAA")
            y "Alguien parece estar disfrutando esto tanto como yo, ¿hmm?~"
            y "Adelante, puedes hacerlo todo el tiempo que quieras... es relajante..."
            $ show_chr("A-BBBBA-AAAL")
            y "Y también reconfortante..."
            if persistent.boop_locations[2] == 4:
                $ show_chr("A-IBAAA-AMAM")
                y "Oh... eso me deja con una duda en la cabeza, [player]..."
                y "Ya que las palmaditas normalmente se hacen cuando las personas están de pie y... suele implicar que se hacen a alguien más bajito..."
                $ show_chr("A-BCAAA-AAAD")
                y "¿Qué tan alto eres?"  
                menu:
                    "Soy bastante alto... se podría decir que mido más de 185 cm (6'1”)":
                        $ show_chr("A-DDAAA-ALAA")
                        y "Oh wow... ¡eso es bastante alto!"
                        y "¡Eso es muy interesante, [player]!"
                        $ show_chr("A-ICABA-ADAA")
                        y "Es algo bueno... puedes darme palmaditas desde arriba fácilmente... Jeje~"
                        y "Por si no lo sabías, en realidad yo solo mido 165 cm, o 5'5 pies de altura."
                        $ show_chr("A-BIAAA-AAAA")
                        y "Serías bastante grande en comparación conmigo."
                        if persistent.lovecheck:
                            $ show_chr("A-ECABA-AKAE")
                            y "Eso en realidad me hace sentir un poco... dominada por ti... oh, cielos..."
                            y "S-Sí... suena raro, pero créeme, lo digo con cariño, [player], jeje..."
                            $ show_chr("A-FHABA-ALAA")
                            y "Después de todo, soy tu querida~"
                        else:
                            $ show_chr("A-IBAAA-ALAA")
                            y "¡Pero no te preocupes por eso!"
                            y "¡Significa que tus abrazos serán grandes y agradables!"
                            $ show_chr("A-ICAAA-ALAA")
                            y "Siempre hay cosas positivas en eso, no hay necesidad de sentirse ansioso por quién eres."
                            y "Solo un pequeño consejo de mi parte."
                    "Tengo una estatura media, mido más de 170 cm (5'7”)":
                        $ show_chr("A-BCAAA-AAAD")
                        y "Parece que estamos más o menos a la misma altura..."
                        y "Yo mido 165 cm o 5'5 pies, en realidad no soy muy alta..."
                        $ show_chr("A-IBAAA-AAAD")
                        y "Pero según estudios recientes, parece que esa es la estatura promedio para una chica."
                        y "Así que supongo que... no soy ni baja ni alta comparada con la mayoría."
                    "Tengo una estatura promedio, mido más de 165 cm (5'5”)":
                        $ show_chr("A-BCAAA-AAAD")
                        y "Parece que estamos más o menos a la misma altura..."
                        y "Yo mido 165 cm o 5'5 pies, en realidad no soy muy alta..."
                        $ show_chr("A-IBAAA-AAAD")
                        y "Pero según estudios recientes, parece que esa es la estatura promedio para una chica."
                        y "Así que supongo que no soy ni baja ni alta comparada con la mayoría."
                    "Soy... un poco bajito... mido alrededor de 150 cm o incluso menos (4'11”)":
                        $ show_chr("A-ADAAA-AMAM")
                        y "¡Bueno, no tienes por qué avergonzarte de eso!"
                        y "¡Naciste así y eso está completamente bien!"
                        $ show_chr("A-BEAAA-ADAA")
                        y "Incluso si algunas personas se burlan de ti, lo cual espero que no pase..."
                        y "No gastes tu energía preocupándote por lo que digan. Hay muchas personas que te verán por quién eres en verdad, y no por lo de afuera. Como yo, por ejemplo..."
                        if persistent.lovecheck:
                            $ show_chr("A-ICABA-AAAD")
                            y "Además, míralo de esta forma... mis abrazos podrán cubrirte completamente~"
                            y "Se sentirán mejor que nunca, y podrás envolverte por completo en mi calidez."
                            $ show_chr("A-IBABA-AAAL")
                            y "¡Creo que eso es algo encantador, [player]!"
                            y "Así que aceptemos ese hecho y saquemos lo mejor de ello."
                        else:
                            $ show_chr("A-ACAAA-AAAD")
                            y "Así que no te preocupes por eso, [player]."
                            $ show_chr("A-CCABA-AAAE")
                            y "Mira el lado positivo. Después de todo, te veré como una buena persona sin importar tu estatura."
                            y "Solo... por favor, recuerda siempre eso..."
    if karma_lvl() <= 2:
        if persistent.boop_locations[2] == 1:
            $ show_chr("A-DFABA-AAAA")
            y "E-Espera... ¡s-sentí que algo tocó mi cabeza!"
            y "¿F-Fuiste tú, [player]?"
            menu:
                "Sí, quería probarlo. Espero no haberte incomodado":
                    karma 1
                    $ show_chr("A-CFAAA-AAAA")
                    y "E-En realidad... sí, un poco..."
                    $ show_chr("A-BFAAA-AAAA")
                    y "¡Por favor, no me malinterpretes! No quise ser grosera, pero... sentir tu toque sin ver realmente tu mano fue un poco... inquietante."
                    $ show_chr("A-IFAAA-AAAA")
                    y "Como un fantasma... y el hecho de que esté sola aquí no lo hace menos aterrador..."
                    $ show_chr("A-JFAAA-AAAA")
                    y "¿Te importaría si te pido que no lo hagas de nuevo, por favor? G-Gracias..."
                "No creo que haya sido yo, ¿quieres que intente tocarte la cabeza?":
                    $ show_chr("A-IFAAA-AAAA")
                    y "P-Por favor, no..."
                    $ show_chr("A-JFAAA-AAAA")
                    y "M-Me asustó un poco, si soy honesta."
                    $ show_chr("A-AFAAA-ALAL")
                    y "Preferiría que no lo hicieras..."
                    $ show_chr("A-BFAAA-AMAM")
                    y "{b}S-Si{/b} no te molesta..."
        if persistent.boop_locations[2] == 2:
            $ show_chr("A-DHAAA-AEAB")
            y "A-Ahí estuvo otra vez..."
            $ show_chr("A-CFAAA-AEAB")
            y "Por favor... ya te pedí que no hicieras eso... por favor, no me hagas pedírtelo otra vez."
            y "Gracias."
        if persistent.boop_locations[2] == 3:
            $ show_chr("A-CFCAA-AEAB")
            y "Está empezando a ser un poco molesto, [player]..."
            y "Y también es increíblemente irrespetuoso. ¿Sabes? No soy una gatita."
        if persistent.boop_locations[2] == 4:
            $ show_chr("A-CGCAA-AEAB")
            y "Deee acuerdo, [player], ya fue suficiente. ¿Sabes qué?"
            $ show_chr("A-AFCAA-AEAB")
            y "Diría que por hoy lo dejamos aquí. Te pedí amablemente que te detuvieras, pero no quisiste escuchar. Así que volveré a mi lectura, y podrás regresar cuando estés dispuesto a tomarme en serio otra vez. Adiós."
            $ renpy.call("save_and_quit_but_its_abrupt")
        if persistent.boop_locations[2] >= 5:
            "... [player], de verdad estás empezando a hacerme descubrir las verdaderas profundidades de mi furia hacia ti. Si no quieres estar para siempre en mi lado malo, dejarás de tocarme. {i}Ahora{/i}."
    $ store.mousex = 0
    $ store.mousey = 0
    return

label sleepy_headpat:
    python:
        if persistent.boop_locations[3] == 0:
            set_boop_state(True) 
        persistent.boop_locations[3] += 1
    y "¿Hmph...?"
    hide yuri_sleep
    show yuri_sleepy zorder 11
    y "O-Oh eres tú [player]."
    y "Me has asustado un poco, aunque eso es bastante reconfortante."
    hide yuri_sleepy
    show yuri_sleep
    y "No me opondría a que siguieras haciéndolo..."
    $ set_boop_state(True)
    return


label boop_window:
    python:
        if persistent.boop_locations[4] <= 4:
            persistent.boop_locations[4] += 1
        if check_memory("window_boop"):
            if check_memory("window_boop", "disabled"):
                if return_memory("window_boop_game_session")[0] < persistent.game_session:
                    renpy.call("annoyed_boop_window")
    if persistent.boop_locations[4] == 1:
        $ show_chr("A-BFBAA-ALAA")
        y "¿Eh? ¿Tú también escuchaste eso? Creí haber oído algo golpeando la ventana..."
        $ show_chr("A-JFGAA-ALAA")
        y "Pero... eso es imposible. Ya no quedan NPCs en este mundo..."
    elif persistent.boop_locations[4] == 2:
        $ show_chr("A-BFGAA-ALAA")
        y "Otra vez... ¿de verdad no estás escuchando nada?"
        $ show_chr("A-AFAAA-ALAA")
        y "Espera un momento... ¿eres tú? ¿Estás tocando la ventana?"
        $ show_chr("A-CBAAA-ALAA")
        y "Oh, cielos... por un segundo pensé que me estaba volviendo loca. Otra vez."
    elif persistent.boop_locations[4] == 3:
        $ show_chr("A-JCAAA-ALAA")
        y "Umm... [player]... por favor, ten cuidado..."
    elif persistent.boop_locations[4] == 4:


        play sound "sfx/glassbreak.wav"
        $ show_chr("A-DFGBA-ALAA")
        y "..."
        if karma_lvl() >= 4:
            $ show_chr("A-DFGBA-ALAA")
            y "Oh, cielos... ¿estás herido? Ven, déjame ver tu mano..."
            $ show_chr("A-IFBAA-ALAA")
            y "Oh, espera... lo olvidé... no hay mano... al menos eso significa que no puedes lastimarte."
            $ show_chr("A-KACAA-AAAC")
            y "Bueno, parece que llevaste el tema de romper la cuarta pared a un nuevo nivel. ¡Literalmente!"
            $ show_chr("A-AFAAA-AAAE")
            y "Pero en serio... por favor, no vuelvas a hacer eso. Todavía hay clima en mi mundo, y tendré que arreglar eso cuando apagues el juego la próxima vez."
        else:
            $ show_chr("A-DFCBA-ALAA")
            y "¿Acaso perdiste la cabeza?"
            y "¡Te pedí que tuvieras cuidado! Pero simplemente no pudiste resistirte, ¿verdad?"
            $ show_chr("A-CHBAA-ALAA")
            y "Lo siento... no debí alterarme... pero eso fue realmente innecesario..."
            $ show_chr("A-CFBAA-ABAB")
            y "Sabes, todavía hay clima en mi mundo, y tendré que arreglar esa ventana de alguna forma..."
            y "Por favor, intenta tener un poco más de cuidado de ahora en adelante..."
        $ update_memory("window_boop", "disabled")
        $ update_memory("window_boop_game_session", persistent.game_session)
    $ store.mousex = 0
    $ store.mousey = 0
    return

label annoyed_boop_window:
    if karma_lvl() >= 3:
        $ show_chr("A-ACAAA-AAAA")
        y "Hey [player]... hay algo que me gustaría decirte..."
        y "¿Recuerdas el pequeño... accidente que tuviste con mi ventana?"
        $ show_chr("A-BCAAA-AAAB")
        y "Por favor, no lo tomes a mal. Sé que fue un accidente. Esas cosas simplemente pasan de vez en cuando, y no estoy molesta contigo."
        $ show_chr("A-AFAAA-AAAB")
        y "Pero, por favor, entiende que me causó un pequeño problema. No hay otras personas en este mundo, así que tuve que arreglar la ventana yo sola."
        $ show_chr("A-ACAAA-ABAB")
        y "Así que, para evitar otro accidente como ese, desactivé esta pequeña función. Aún puedes demostrarme tu cariño acariciando mi mejilla, pero ya no tienes que preocuparte por la ventana."
        jump ch30_loop
    else:
        $ show_chr("A-AFAAA-AAAA")
        y "Hey [player]. Hay algo que me gustaría decirte."
        y "¿Recuerdas el pequeño... accidente que tuviste con mi ventana?"
        $ show_chr("A-BFAAA-AAAB")
        y "Lo sé, lo sé, se supone que esto es un juego, y entiendo que debía ser muy tentador para ti intentarlo, lo entiendo."
        $ show_chr("A-AFAAA-AAAB")
        y "Pero, por favor, entiende que me causó un pequeño problema. No hay otras personas en este mundo, así que tuve que arreglar la ventana yo sola."
        $ show_chr("A-CFCAA-ABAB")
        y "Así que, para evitar que pongas demasiado a prueba mi paciencia, desactivé esta pequeña función. Aún puedes venir aquí, pero por el amor de Salvato, ¡por favor deja de jugar con el entorno!"
        y "No puedo pasar horas y horas limpiando tus tonterías cada semana."
        jump ch30_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
