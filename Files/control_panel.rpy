label control_panel:
    python:
        if not dev_access:
            renpy.call("save_and_quit_but_its_abrupt")
    menu:
        "¿A dónde ir?"
        "Centro de expresión":
            $ persistent.costume = "school"
            $ persistent.current_timecycle = "_day"
            $ show_chr("standard")
            call screen make_expression
        "Llamada de diálogo":
            call caller_loop
        "Menú activo":
            $ call_dialogue(ch30_loop_type, "actives")
        "Cap_30 salto de bucle":
            call ch30_loop
        "Sistema KS":
            menu:
                "Mostrar puntos KS":
                    y "Sanity = [persistent.sanity_points], Karma = [persistent.karma_points]"
                "Cambiar karma/cordura":
                    call alter_ks
                "No importa":
                    $ pass
        "Sistema Time_Tracker":
            call alter_time_tracker
        "Borrado de la memoria de etiquetas vistas":
            python:
                forget_label = renpy.input("¿Qué etiqueta vista quieres olvidar?")
                if forget_label.strip() != "":
                    if renpy.seen_label(forget_label):
                        y("Olvidando... [forget_label]")
                        del renpy.game.persistent._seen_ever[forget_label]
                    else:
                        y("Nunca había visto [forget_label] antes.")
        "Juego cerrado":
            jump save_and_quit
    jump control_panel

label caller_loop:
    menu:
        "Bienvenido al bucle de diálogo"
        "Activar tipo de diálogo aleatorio":
            menu:
                "¿Qué tipo de diálogo?"
                "Activador inactivo":
                    $ call_dialogue(ch30_loop_type, "idles")
                "Saludo de activación":
                    $ call_dialogue(ch30_loop_type, "greetings")
                "Despedida de Trigger":
                    $ call_dialogue(ch30_loop_type, "farewells")
        "Restablecer memoria":
            $ reset_memory()
        "Llamada al diálogo":
            python:
                jumper = str(renpy.input("¿A qué diálogo quieres llamar?"))
                if renpy.has_label(jumper):
                    renpy.call_in_new_context(jumper)
                else:
                    y(str(jumper) + " no existe.")
        "Volver al Panel de control":
            jump control_panel
    jump caller_loop

label alter_ks:
    menu:
        "¿Desea modificar estos valores basándose en puntos o nombres ks_convert_?"
        "Puntos":
            jump alter_1
        "ks_convert_":
            jump alter_2

label alter_1:
    menu:
        "Todo lo siguiente aumenta los puntos en 10"
        "Aumentar el karma":
            $ persistent.karma_points = persistent.karma_points + 10
        "Aumentar la cordura":
            $ persistent.sanity_points = persistent.sanity_points + 10
        "Disminuir el karma":
            $ persistent.karma_points = persistent.karma_points - 10
        "Disminuir la cordura":
            $ persistent.sanity_points = persistent.sanity_points - 10
        "Restablecer cordura y karma a 0":
            $ persistent.sanity_points = 0
            $ persistent.karma_points = 0
        "Aumento personalizado":


            jump custom_increase
        "Disminución personalizada":
            jump custom_decrease
        "Volver al panel de control":


            "Eh. Supongo que no hace falta que hagamos eso."
            jump control_panel
    "Hecho"
    jump alter_1

label custom_increase:
    menu:
        "¿Qué valor hay que aumentar?"
        "Karma":
            jump custom_karma_increase
        "Cordura":
            jump custom_sanity_increase
        "Volver":
            jump alter_1

label custom_decrease:
    menu:
        "¿Qué valor hay que reducir?"
        "Karma":
            jump custom_karma_decrease
        "Cordura":
            jump custom_sanity_decrease
        "Volver":
            jump alter_1
label custom_karma_increase:
    python:
        amount = renpy.input("Introduce la cantidad para aumentar el karma (entre -100 y 100):")
        try:
            amount = int(amount)
            if -100 <= amount <= 100:
                persistent.karma_points += amount
                y("El karma ha aumentado en [amount]. Nuevos puntos de karma: [persistent.karma_points]")
            else:
                y("Importe no válido. Debe estar entre -100 y 100.")
        except ValueError:
            y("Entrada no válida. Por favor introduzca un número.")
    jump alter_1

label custom_sanity_increase:
    python:
        amount = renpy.input("Introduce la cantidad para aumentar la cordura (entre -100 y 100):")
        try:
            amount = int(amount)
            if -100 <= amount <= 100:
                persistent.sanity_points += amount
                y("La cordura aumentó en [amount]. Nuevos puntos de cordura: [persistent.sanity_points]")
            else:
                y("Importe no válido. Debe estar entre -100 y 100.")
        except ValueError:
            y("Entrada no válida. Por favor introduzca un número.")
    jump alter_1

label custom_karma_decrease:
    python:
        amount = renpy.input("Introduce la cantidad para reducir el karma (entre -100 y 100):")
        try:
            amount = int(amount)
            if -100 <= amount <= 100:
                persistent.karma_points += amount  
                y("El karma ha disminuido en [amount]. Nuevo karma: [persistent.karma_points]")
            else:
                y("Importe no válido. Debe estar entre -100 y 100.")
        except ValueError:
            y("Entrada no válida. Por favor introduzca un número.")
    jump alter_1

label custom_sanity_decrease:
    python:
        amount = renpy.input("Enter amount to decrease Sanity (between -100 and 100):")
        try:
            amount = int(amount)
            if -100 <= amount <= 100:
                persistent.sanity_points += amount 
                y("La cordura disminuyó en [amount]. Nueva cordura: [persistent.sanity_points]")
            else:
                y("Importe no válido. Debe estar entre -100 y 100.")
        except ValueError:
            y("Entrada no válida. Por favor introduzca un número.")
    jump alter_1

label alter_2:
    menu:
        "¿Cambiar el karma o la cordura?"
        "Karma":
            menu:
                "Nivel de karma 5":
                    $ persistent.karma_points = lvl_to_point(5)
                "Nivel de karma 4":
                    $ persistent.karma_points = lvl_to_point(4)
                "Nivel de karma 3":
                    $ persistent.karma_points = lvl_to_point(3)
                "Nivel de karma 2":
                    $ persistent.karma_points = lvl_to_point(2)
                "Nivel de karma 1":
                    $ persistent.karma_points = lvl_to_point(1)
                "No importa":
                    "Eh. Supongo que no hace falta que hagamos eso."
        "Cordura":
            menu:
                "Nivel de cordura 5":
                    $ persistent.sanity_points = lvl_to_point(5)
                "Nivel de cordura 4":
                    $ persistent.sanity_points = lvl_to_point(4)
                "Nivel de cordura 3":
                    $ persistent.sanity_points = lvl_to_point(3)
                "Nivel de cordura 2":
                    $ persistent.sanity_points = lvl_to_point(2)
                "Nivel de cordura 1":
                    $ persistent.sanity_points = lvl_to_point(1)
                "No importa":
                    "Eh. Supongo que no hace falta que hagamos eso."
        "Volver al panel de control":
            jump control_panel
    "Hecho"
    jump alter_2

label alter_time_tracker:
    menu:
        "Mostrar hora actual en el juego":
            y "[persistent.ingame_time]"
        "Establecer la hora del juego":
            $ ingame_time_seconds_temp = 3600*int(renpy.input("¿Número de horas?\n"))
            $ ingame_time_days_temp = int(renpy.input("¿Número de días?"))
            $ persistent.ingame_time = datetime.timedelta(seconds = ingame_time_seconds_temp, days = ingame_time_days_temp)
            y "[persistent.ingame_time]"
    jump control_panel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
