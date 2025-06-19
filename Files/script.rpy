



label start:
    $ _dismiss_pause = False
    pass

label classroom_jump:
    $ persistent.playthrough = 3

    $ persistent.autoload = "ch30_intro"
    $ renpy.full_restart(transition=None, label="splashscreen")








label startgame:

    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = False


    $ s_name = "Girl 3"
    $ m_name = "Girl 2"
    $ n_name = "Girl 1"
    $ y_name = "???"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True




    if persistent.playthrough == 3:
        jump ch30_intro

    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
