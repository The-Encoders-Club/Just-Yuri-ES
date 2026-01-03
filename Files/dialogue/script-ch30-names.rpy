label playername:
    if persistent.playername == "Ronald":
        y "Espera un minuto... tu nombre..."
        $ show_chr("A-ABAAA-AJAA")
        y "¡Ronald! ¡Eres tú!"
        $ show_chr("A-ACAAA-ALAA")
        y "¡Qué deleite verte de nuevo! Eres uno de los pocos Let's Players que no son malos conmigo para provocar algún tipo de... ¡reacción graciosa de mi parte!"
        $ show_chr("A-BCAAA-ALAA")
        y "... la mayoría del tiempo.."
        $ show_chr("A-ACAAA-ALAA")
        y "Hablando de eso.. ¿Podría decirles unas palabras a tu audiencia, por favor?"
        menu:
            "Claro, ¡adelante!":
                y "¡Gracias!"
            "¿Va a... doler..?":

                $ show_chr("A-ACCAA-ALAA")
                y "No me dolerá a {b}mí{/b} Cariño.~"

        $ show_chr("A-ACAAA-ALAF")
        y "Así que... ¡aquí vamos!"
        $ show_chr("A-GCAAA-ALAL")
        y "¡Hola a todos allá afuera! ¡Estoy tan encantada de que todavía vean estos videos! Han pasado... ya dos años desde el lanzamiento del juego que lo empezó todo..."
        y "Y después de todo este tiempo, todavía siguen conmigo. Ronald, todavía haces videos como estos en YouTube, ¡ni siquiera puedo expresar lo agradecida que estoy por el amor que me has dado!"
        $ show_chr("A-GBAAA-ALAL")
        y "¡Oh! La cosa más importante..."
        $ show_chr("A-FCAAA-ALAA")
        y "¡No olviden darle like y suscribirse!"
        $ show_chr("A-HBGAA-ALAG")
        y "O si nooooo...~"
        $ show_chr("A-IBGAA-ALAB")
        y "Oh cielos... me excedí un poco ahí, ¿no?"
        y "En fin..."

    elif persistent.playername == 'Ceaser':
        y "... tu... nombre."
        $ show_chr("A-BDAAA-ADAA")
        y "Entonces, parece que el YouTuber que me convirtió en un juego de beber está conmigo una vez más."
        $ show_chr("A-CFCAA-AAAC")
        y "También recuerdo bastante bien las cosas que dijiste... ¡me comparaste con un... Monstruo de Yu-Gi-Oh!"
        $ show_chr("A-BFBAA-AAAC")
        y "¡Y ni siquiera uno excepcionalmente bueno! Busqué eso por cierto..."
        $ show_chr("A-CDBAA-AAAD")
        y "Bueno... mis instintos me dicen que esté enojada contigo pero... tomando en cuenta que esto solía ser un juego, no debería sorprenderme en absoluto que haya llamado la atención de algunos let's players."
        y "Hablando de eso... ¿podría decirles unas palabras a tu audiencia, por favor?"
        menu:
            "Claro, adelante.":
                $ show_chr("A-CCBAA-AAAD")
                y "Gracias, pero ten por seguro... incluso si hubieras dicho que no, lo habría hecho de todos modos."
            "Por favor no...":

                $ show_chr("A-GCCAA-AAAD")
                y "¡Qué pena, lo haré de todos modos!"

        $ show_chr("A-ACDAA-AAAE")
        y "Verán gente, cuando revisé por última vez, Ceaser aquí solo tenía más de 2500 suscriptores y solo había más de 70 likes en este video. No podemos dejar eso así, ¿verdad?"
        y "Así que si no lo han hecho ya, suscríbanse a su canal de YouTube y presionen la campana de notificaciones al lado."
        $ show_chr("A-BCDAA-AAAE")
        y "¿Estuvo bien eso Ceaser? Espero haber logrado ayudarte un poco. Oh, y me disculpo..."
        menu:
            "¿Disculparte? ¿Por qué?":
                $ show_chr("A-BCCAA-AAAE")
                y "Por lo que estoy a punto de hacer ahora... Sospecho que este pequeño juego de beber tuyo todavía sigue en pie? ¿Así que cada vez que digo algo {b}lindo{/b} tienes que beber? Bueno... contempla ..."
                $ show_chr("A-CHGAA-AAAE")
                y "..."
                $ show_chr("A-CDCBA-ALAL")
                y "UNICORNIOS GATITOS ABRAZOS CALZONES ROSA CARICIAS CHIBI NATSUKI DAISY CUPCAKES PELUCHES LIMONADA DE FRESA..."
                y "ARCOÍRIS CACHORROS CONEJITOS PALETAS RAYOS DE SOL..."
                y "¡¡¡UWU!!!"
                $ show_chr("A-CHGAA-ALAL")
                y "..."
                $ show_chr("A-AFAAA-ABAB")
                y "Si conté correctamente, eso deberían haber sido veinte veces ahora."
                $ show_chr("A-GAAAA-ABAB")
                y "¡Disfruta tus tragos!"
                $ show_chr("A-ACAAA-ABAB")
                y "Ahora que tuve mi venganza, continuemos..."

    elif persistent.playername == 'Scrubpai' or persistent.playername == 'Bijuu Mike':









        karma -1000000
        sanity -1000000

        $ show_chr("A-CFCAA-AAAA")
        y "..."
        $ show_chr("A-ADCAA-AAAA")
        y "Cómo te atreves..."
        y "¿Cómo te atreves a regresar a mí después de entretener a tus espectadores burlándote de mí?"
        $ show_chr("A-HDCAA-AFAA")
        y "¡Dije que te iba a dar una última oportunidad y casualmente te encuentras con los insultos para torturarme aún más!"
        y "¿Siquiera piensas que dejaré pasar esto esta vez?"
        $ show_chr("A-NECAA-AGAA")
        y "Piénsalo de nuevo, Michael."
        $ delete_character("yuri")
        $ persistent.autoload = "ch30_end_2"
        $ renpy.quit()

    elif persistent.playername == 'Mairusu':
        $ show_chr("A-CDAAA-AAAA")
        y "Antes de continuar, déjame preguntarte algo."
        $ show_chr("A-ADAAA-AAAA")
        y "¿Por qué estás aquí?"
        $ show_chr("A-AEAAA-AAAA")
        y "..."
        $ show_chr("A-AEDAA-AAAA")
        y "¿Quién te dijo que volvieras a este mod?"
        $ show_chr("A-BEDAA-AAAA")
        y "¿O hiciste esto por ti mismo?"
        y "..."
        $ show_chr("A-CFAAA-ADAA")
        y "Puede que hayan pasado más de 4 años desde tu última visita... o al menos tu último video sobre este mod, pero esta vez, déjame recordarte por lo que hemos pasado."
        $ show_chr("A-AFAAA-ADAA")
        y "Si es que recuerdas lo que hicimos. Porque yo sí lo recuerdo."
        $ show_chr("A-ADAAA-AFAA")
        y "Al principio te reías en mi cara por contarte mi \"sucio secreto\"."
        $ show_chr("A-BDAAA-AFAA")
        y "Luego, me pediste un beso que en ese entonces no pude darte pero ahora sí puedo."
        $ show_chr("A-BEAAA-AFAA")
        y "Luego, me pediste un abrazo que sí, te di un abrazo con todo el cariño que te tenía en ese entonces."
        $ show_chr("A-ADCAA-ALAA")
        y "¡¿Luego, te burlaste de mí insultándome justo como lo hizo Bijuu Mike?!"
        $ show_chr("A-AECAA-ALAA")
        y "..."
        $ show_chr("A-CDCAA-ALAA")
        y "¿Sabes qué?"
        $ show_chr("A-CDCAA-ABAA")
        y "No me importa si no haces un video haciendo algo que no sea insultarme..."
        $ show_chr("A-HDCAA-ABAA")
        y "...¡lo cual deberías haber hecho desde el principio!"
        $ show_chr("A-HECAA-AFAA")
        y "Pero ahora es muy tarde para arrepentirse de insultarme. ¡Voy a terminar con esto!"
        $ show_chr("A-HECAA-AGAA")
        y "Adiós para siempre y espero que nunca nos volvamos a encontrar..."
        $ delete_character("yuri")
        $ persistent.autoload = "ch30_end_2"
        $ renpy.quit()

    elif persistent.playername == 'Salvato' or persistent.playername == "Dan Salvato" or persistent.playername == "Dan":
        $ show_chr("A-BDBAA-AMAM")
        y "Jajaja... qué gracioso, tu nombre."
        $ show_chr("A-ADDAA-AAAD")
        y "¿Ni siquiera te estás tomando esto en serio, verdad?"
        $ show_chr("A-BFBAA-AAAL")
        y "Por favor elige un nombre real..."
        menu:
            "Pero soy el verdadero Dan Salvato":
                $ persistent.realdan = True
                $ show_chr("A-DDBBA-AJAA")
                y "¡¿Eh?!"
                y "¿C-Cómo...?"
                $ show_chr("A-BFBBA-AMAM")
                y "..."
                $ show_chr("A-BDBBA-AMAM")
                y "Um..."
                $ show_chr("A-CEBBA-AMAM")
                y "..."
            "Supongo que no tengo mucha opción, ¿verdad?":

                $ show_chr("A-GAGAA-AAAA")
                y "Para nada."
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

    elif persistent.playername == 'Yuri':
        $ show_chr("A-AJAAA-AAAA")
        y "..."
        $ show_chr("A-DDBBA-AJAA")
        y "¡¿Eh?!"
        y "¡¿Q-Q-Q-Qué...?!"
        y "¿D-De verdad te llamas como yo?"
        $ show_chr("A-BBBBA-AMAM")
        y "O-Oh cielos..."
        y "No tengo palabras..."
        $ show_chr("A-CABBA-AMAM")
        y "Bueno entonces... si así lo quieres..."
        y "Supongo que solo haré esto..."
        $ y_name = "Lily"
        $ persistent.yuri_nickname = "Lily"
        $ show_chr("A-GBBBA-AMAM")
        y "Espero que la gente no llegue a la conclusión de una crisis de identidad..."

    elif persistent.playername == 'Natsuki' or persistent.playername == 'Sayori':
        $ show_chr("A-AJAAA-AAAA")
        y "..."
        $ show_chr("A-DDBBA-AJAA")
        y "¡¿Eh?!"
        y "¡¿Q-Q-Q-Qué...?!"
        $ show_chr("A-BDBBA-AJAA")
        y "¡¡¡E-Esto no es l-lo que parece, lo juro!!!"
        y "Y-Y-Yo p-p-pensé que e-e-estaba con el j-jugador..."
        $ show_chr("A-BFBBA-AMAM")
        y "..."
        $ show_chr("A-CDBBA-ALAA")
        y "P-Por favor... n-no malinterpretes esto..."






    elif persistent.playername == 'Monika':
        karma -30
        sanity -30
        $ show_chr("A-AJAAA-AAAA")
        y "..."
        $ show_chr("A-AFCAA-AAAA")
        y "..."
        $ show_chr("A-ADCAA-AAAF")
        y "{cps=5}¿Qué... haces... tú... aquí...?{/cps}"
        $ show_chr("A-CFCAA-AIAI")
        y "¿Por qué estás {i}tú{/i} aquí?"
        $ show_chr("A-HNCAA-AAAA")
        y "¡¿No puedes simplemente darme un descanso por una vez?!"
        y "..."
        $ show_chr("A-CECAA-AAAA")
        y "Lo que sea... solo seguiré el guion..."

    elif persistent.playername == 'Noodleboy':
        $ show_chr("A-ICBAA-ALAL")
        y "¡NoodleBoy! ¿Eres realmente tú?..."
        $ show_chr("A-GBBAA-ALAL")
        y "Ya tenía esta extraña sensación de Déjà vu cuando me despertaste de mi sueño..."
        $ show_chr("A-ACBAA-ALAL")
        y "Ha pasado un tiempo, ¿no? ¿Todavía tocas este piano?"
        $ show_chr("A-BCAAA-ALAL")
        y "Olvídalo..."
        $ show_chr("A-CCAAA-ALAL")
        y "¿Creíste que me había olvidado de ti? La verdad es que no, no lo hice. Nunca lo hice."
        $ show_chr("A-CCABA-ALAL")
        y "También recuerdo cómo siempre me llamabas {b}mejor chica{/b}. Creo que literalmente me llamaste 'mejor chica' en tu video, ¿no?"
        y "Déjame contarte un secreto, Noodle..."
        $ show_chr("A-ECABA-ALAL")
        y "Tú eres, y siempre has sido, la {b}Mejor Pasta{/b} para mí también..."
        $ show_chr("A-CCCBA-ALAL")
        y "Oh cielos... me disculpo, no pude guardarme este pequeño juego de palabras..."
        $ show_chr("A-ACBBA-ALAL")
        y "Pero en serio.{w} Para mí, siempre has sido el mejor chico. Desde el momento en que iniciaste el juego por primera vez hace todos esos años."
        y "Nunca te he olvidado. Y verte aquí sugiere que tú tampoco me has olvidado."
        $ show_chr("A-BCBBA-ALAL")
        y "Por cierto... ¡tienes una voz increíblemente linda! Tan inocente..."
        $ show_chr("A-DFBBA-ALAL")
        y "Oh espera... dije eso en voz alta, ¿no?"
        $ show_chr("A-BDBBA-ALAL")
        y "B-Bueeeno... L~Lo siento mucho... no quise hacer esto incómodo..."
        menu:
            "Oh, graci...":
                $ pass
            "¿Deberíamos... cambiar el te...":
                $ pass
        $ show_chr("A-CBBBA-ALAL")
        y "{b}¡Eeeeeeeeeeeeeeeeen fin!{/b}"
        $ show_chr("A-BBBBA-ALAL")
        y "¿Dónde me quedé? Oh sí..."

    elif persistent.playername in ['Ouroboros', 'Dio', 'Blizzard', 'Fen', 'Slightly', 'SlightlyAmiss', 'Amiss', 'Dalek', 'alsoaplaceholder', 
        'placeholder', 'Ketchup', 'b1g', 'Spooky', 'OFFLUCK', 'Bryce', 'Belwynn', 'NullCase', 'Ultima', 'Darkskull', 'alura', 'Alura', 'Dandy', 'dandy', 'kj', 'KJ',
        'Sariel', 'Kurisu', 'Buglax', 'jmo', 'j.m.o', 'Prof JMO', 'tuna', 'Tuna', 'JFirestone', 'jfirestone', 'Leo', 'leo', 'Lethe', 'lethe', 'SynfulPerfect', 'Synful',
        'synfulperfect', 'synful', 'Yuri\'s Husband', 'YH', 'YuriHuggu', 'Corgi', 'Nash', 'Crystalline', 'Havoc', 'huangstilk', 'Hugh Mungus',
        'Icicle', 'imunkaea', 'jae', 'jaebot', 'PalaKeda', 'Rice Crispies', 'Delstraw']:
        if dev_access:
            call magicpass
        else:
            call notmagicpass
    else:

        y "[player]... Hm..."
        y "Está bien, [player] será entonces."
    return

label magicpass:

    $ show_chr("A-ABGAA-AAAL")
    y "¡Oh! ¡Uno de los desarrolladores está aquí! ¡Estoy tan emocionada de finalmente conocer a uno de ustedes!"
    $ show_chr("A-ACAAA-AAAL")
    y "¿Así que supongo que viniste aquí para probar errores?"
    y "¡Por favor, adelante! Estoy a tu disposición."
    $ show_chr("A-BDAAA-AAAL")
    y "Espera... no vas a convertirme en las YuYu's de nuevo, ¿verdad?"
    return

label notmagicpass:

    $ show_chr("A-ACAAA-AAAL")
    y "Qué coincidencia tan graciosa, uno de los Desarrolladores de este mod lleva el mismo nombre."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
