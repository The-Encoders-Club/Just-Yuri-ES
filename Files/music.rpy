
define audio.space = "[current_music]"





init python:
    from os import walk
    def change_music(name, speed = 0.5):
        """
        This function changes the music by doing a fadeout on the current music channel, and fading in the new music on another parallel music channel.
        The hope for this is to create a relatively smooth transition from one track to the other with less downtime
        """
        if renpy.music.is_playing(channel="music2"):
            renpy.music.stop(channel="music2", fadeout=speed)
            renpy.music.play(name, channel="music", loop=True, fadein=speed)
        else:
            renpy.music.stop(channel="music", fadeout=speed)
            renpy.music.play(name, channel="music2", loop=True, fadein=speed)

    def standard_music():
        """
        This is the standard music held within Just Yuri.
        Call this function to return from the standard Just Yuri music set the appropriate music, depending on the current time.
        """
        tc = tc_class.cur_time_to_tc(persistent.bg)
        possible_music = []
        if tc == "_sunrise":
            possible_music.append("<loop 29.44>music/jy_music/eternity_loop.ogg")
        elif tc == "_day":
            possible_music.append("<loop 64.69>music/jy_music/introversion_loop.ogg")
        elif tc == "_sunset":
            possible_music.append("music/jy_music/starset.ogg")
        elif tc == "_night":
            possible_music.append("<loop 84.07>music/jy_music/enotronics_loop.ogg")
        else:
            possible_music.append("<loop 18.08>music/jy_music/hello_again_loop.ogg")
        
        print_debug(possible_music)
        return random.choice(possible_music)

    def custom_music_list(all_options = True):
        """
        This function returns back a list of tuples.
        The first element of each tuple is the message associated with the music
        The second element will be the file path to the music file, whether that be in .rpa or some other folder.

        The empty second element corresponds to automatically choosing the standard music in standard_music()
        """
        show_chr("A-AAAAA-AAAA")
        f = []
        for (dirpath, dirnames, filenames) in walk(config.basedir + "/music"):
            f.extend(filenames)
            break
        musicmenu = []
        for i in f:
            if i.find(".ogg") == -1 and i.find(".mp3") == -1 and i.find(".wav") == -1 and i.find(".flac") == -1:
                pass
            else:
                musicmenu.append((i, "<loop 0>../music/" + i))
        if all_options:
            musicmenu.append(("¡Reproducir Okay Everyone! (Versión de Yuri)", "<loop 4.444>bgm/5_yuri.ogg"))
            musicmenu.append(("Reproducir Stagnant Air", "<loop 96.04>/music/jy_music/Stagnant_Air_Loop.ogg"))
        musicmenu.append(("Creo que prefiero la música no personalizada", ""))
        musicmenu.append(("No importa", "nevermind"))
        return musicmenu

    def choose_music(all_options = True):
        """
        This function displays the menu screen for music options and returns the result of that to music_choice
        current_music is the global variable which is responsible for the current music playing, and contains the path to the current music.
        persistent.custom_music is a variable loaded on startup which, if not None, automatically plays the music that is associated with the filepath contained within it.
        """
        global current_music
        music_choice = renpy.display_menu(custom_music_list(all_options), screen="music_menu")
        if music_choice == "":
            current_music = standard_music()
            persistent.custom_music = None
        elif music_choice == "nevermind":
            renpy.call("ch30_loop")
        else:
            persistent.custom_music = music_choice
            current_music = persistent.custom_music
        change_music(current_music, 5.0)

    def get_pos(channel='music'):
        """
        This function returns position in current song playing.
        """
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    if persistent.custom_music != None and len(persistent.custom_music.split(">")) != 1 and renpy.loadable(persistent.custom_music.split(">")[1]):
        current_music = persistent.custom_music
    else:
        persistent.custom_music = None
        current_music = standard_music()


label change_music:
    $ DisableTalk()
    $ boopable = False
    $ show_chr("A-ABGAA-ACAA")

    menu:
        y "¿Te gustaría cambiar la música?"
        "Sí":
            menu:
                y "¿Te gustaría una explicación?"
                "Sí":
                    $ show_chr("A-BCAAA-ACAA")
                    y "Interesante."
                    $ show_chr("A-ADAAA-AAAF")
                    y "Lo primero que debes hacer es colocar tu archivo de música dentro de la carpeta /music."
                    y "Si no tienes una carpeta /music, simplemente crea una junto a la carpeta /game, pero no dentro de ella."
                    y "Asegúrate de que el archivo de música esté en formato .ogg, .mp3, o .wav."
                    y "Ten en cuenta que incluir símbolos en el nombre del archivo podría dañar el sistema de música, así que trata de evitarlo, [player]."
                    y "Además, procura no incluir demasiados archivos de música."
                    $ show_chr("A-ADAAA-AAAA")
                    menu:
                        y "¿Listo?"
                        "Sí":
                            if custom_music_list() == []:
                                $ show_chr("A-BFAAA-AAAN")
                                y "Parece que no tienes nada en la carpeta por ahora..."
                                $ show_chr("A-BBBAA-AAAN")
                                y "Está bien. Esperaré a que los pongas, de todas formas."
                            else:
                                $ choose_music()
                        "No":
                            $ show_chr("A-GCBAA-AAAA")
                            y "Ya veo."
                            $ show_chr("A-ABBAA-AAAA")
                            y "No hay prisa. Tómate tu tiempo."
                "No":
                    $ choose_music()
        "No":
            $ show_chr("A-GCBAA-AAAA")
            y "Está bien entonces."
            $ show_chr("A-ABBAA-AAAA")
            y "No hay necesidad de apresurarse."
    call ch30_loop
screen music_menu(items, orientation="vertical"):
    zorder 1

    style_prefix "choice"

    frame at music_menu_animation:
        background None

        xmaximum 600
        xpadding 10
        xalign 1.0

        has viewport
        scrollbars orientation
        draggable True
        mousewheel True

        vbox:
            xfill True
            for i in items:
                textbutton i.caption at music_button_zoom:
                    action i.action
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

