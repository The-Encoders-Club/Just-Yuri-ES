default ch30_loop_type = "pool"
label repeat_idles:
    y "It seems we ran out of dialogues you haven't seen yet."
    $ ch30_loop_type = "pool"
    return












init -3 python:








    add_dialogue(Dialogue(
        label = 'repeat_idles',
        category = DialogueAPI.category_idle,
        conditions = ["ch30_loop_type == \"pool_nonrepeat\""],
        importance = -1,
        name = None,
        sub_category = None))







    add_dialogue(Dialogue(
        label = 'idle_1',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_3',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_4',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_5',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label(idle_4)"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_6',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 10'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_7',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_8',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_6')", "not renpy.seen_label('idle_8')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_9',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_10',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 20'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_11',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_12',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_6')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_13',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label = 'idle_14',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_10')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_15',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_2')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_16',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_10')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_17',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_18',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_8')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_19',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_20',
        category = DialogueAPI.category_idle,
        conditions = ['karma_lvl() >= 4', 'philosophy == True'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_21',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_20')", 'philosophy == True'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_22',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_18')", "renpy.seen_label('a18')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_23',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_15')", "not renpy.seen_label('idle_22')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_24',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 30'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_25',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_26',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_27',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_28',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_2')", "renpy.seen_label('idle_3')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_29',
        category = DialogueAPI.category_idle,
        conditions = ["not renpy.seen_label('idle_29')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_30',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_29')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_31',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_32',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_33',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_25')", "renpy.seen_label('a24')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_34',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_35',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label(idle_4)", "renpy.seen_label(idle_5)"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_36',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_37',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_38',
        category = DialogueAPI.category_idle,
        conditions = ['karma_lvl() >= 4'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_39',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_40',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 20'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_41',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_12')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_42',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_43',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 2', 'persistent.head1 != "cat_ears"'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_44',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_12')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_45',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_10')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_46',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_15')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_47',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_45')", "not renpy.seen_label('idle_47')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_48',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_45')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_49',
        category = DialogueAPI.category_idle,
        conditions = ["not renpy.seen_label('idle_49')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_50',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_51',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

















    add_dialogue(Dialogue(
        label = 'idle_54',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_55',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_3')", "renpy.seen_label('idle_45')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_56',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck', "renpy.seen_label('idle_55')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_57',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_56')"],
        importance = 0,
        name = None,
        sub_category = None))









    add_dialogue(Dialogue(
        label = 'idle_59',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_60',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_44')", "not check_memory('idle_60', 'first_boop')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_61',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 40'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_62',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('a1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_63',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('a1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_64',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_14')", "renpy.seen_label('idle_22')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_65',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_66',
        category = DialogueAPI.category_idle,
        conditions = ['karma_lvl() <= 4', "renpy.seen_label('a1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_67',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_68',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_69',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_70',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_71',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_72',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 10'],
        importance = 0,
        name = None,
        sub_category = None))









    add_dialogue(Dialogue(
        label = 'idle_74',
        category = DialogueAPI.category_idle,
        conditions = ['karma_lvl() == 5', "not renpy.seen_label('idle_74')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_75',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_32')", "not renpy.seen_label('idle_75')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_76',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 4', 'philosophy == True'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_77',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 10'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_78',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 3'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_79',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck', "renpy.seen_label('idle_34')"],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label = 'idle_80',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('a11')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_81',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_82',
        category = DialogueAPI.category_idle,
        conditions = ["((persistent.ingame_time.seconds // 3600) >= 5)"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_83',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_72')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_84',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_74'), 'philosophy == True'"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_85',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('Halloween_2021') or renpy.seen_label('hobbies')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_86',
        category = DialogueAPI.category_idle,
        conditions = ["karma_lvl()>3", "not renpy.seen_label('idle_84')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_87',
        category = DialogueAPI.category_idle,
        conditions = ["karma_lvl()>3", "renpy.seen_label('idle_84')", "not renpy.seen_label('idle_85')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_88',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('tropical_date')", "not renpy.seen_label('idle_88')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_89',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('tropical_date')", "not renpy.seen_label('idle_89')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_90',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

















    add_dialogue(Dialogue(
        label = 'idle_93',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_94',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_95',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_96',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_97',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_98',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_99',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_100',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_101',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_102',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_103',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_104',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_105',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_106',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_107',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'gaming_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gaming')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'poetry_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('poetry')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'fantsci_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('fantsci')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'noliteratureatall_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('noliteratureatall')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'tcg_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('tcg')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'folklore_and_myths',
        category = DialogueAPI.category_idle,
        conditions = ['karma_lvl() >= 3', 'sanity_lvl() >= 3'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'origami',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gifting_intro')"],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label = 'gifting_intro',
        category = DialogueAPI.category_idle,
        conditions = ["not renpy.seen_label('gifting_intro')"],
        importance = 15,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'horrorbookHint',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gifting_intro')", "not renpy.seen_label('horrorbookHint')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'raccoonHint',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gifting_intro')", "not renpy.seen_label('raccoonHint')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'diffuserHint',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gifting_intro')",  "not renpy.seen_label('diffuserHint')"],
        importance = 0,
        name = None,
        sub_category = None))










    add_dialogue(Dialogue(
        label = 'table_organization',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gifting_revamp')", "not renpy.seen_label('table_organization')"],
        importance = 15,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label = 'diffuser_enable',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('diffuser')", "renpy.seen_label('table_organization')", "not renpy.seen_label('diffuser_enable')"],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label = 'ouija',
        category = DialogueAPI.category_idle,
        conditions = ["""time_interval_check(
            {'month': 10,
                'day': 31},
            {'month': 11,
                'day': 6}
            )""",
            "renpy.seen_label('Halloween_2021')", 'not persistent.ouija_done'],
        importance = 0,
        name = None,
        sub_category = None))






    add_dialogue(Dialogue(
        label = "a1",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "¿Cómo te sientes hoy?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label = "a2",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Hoy te ves muy bien, [persistent.yuri_nickname].",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label = "a3",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "¿Qué opinas de nuestra relación hasta ahora?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label = "a4",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "¿En qué estás pensando?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label = "a5",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], ¿cómo está tu vista?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a6",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "Te amo, [persistent.yuri_nickname].",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a7",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "¿Me extrañas cuando no estoy, [persistent.yuri_nickname]?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a8",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "¿Cuáles son tus preferencias amorosas?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a9",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "A-Aquella vez que te puse ese chocolate en la boca...",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label = "a10",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Nunca llegamos a leer juntos Retrato de Markov, ¿verdad?",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label = "a11",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "A mí también me gustan los cuchillos. ¿Cuál es tu favorito?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a12",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_1')", "not renpy.seen_label('a12')"],
        importance = 0,
        name = "Lo que le hiciste al resto de las chicas estuvo MAL.",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label = "a13",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Hey, [persistent.yuri_nickname], ¿que tal si me besas?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a14",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "¿Cuál es tu tipo de clima favorito en mi mundo?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a15",
        category = DialogueAPI.category_talk,
        conditions = ["not renpy.seen_label('a15')"],
        importance = 0,
        name = "¿Alguna vez has comido algo, [persistent.yuri_nickname]?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a16",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "¿Tienes acceso a la televisión desde donde estás?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label = "a17",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "¿C-Cuáles son tus fetiches?",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "a18",
        category = DialogueAPI.category_talk,
        conditions = ["not renpy.seen_label('a18')"],
        importance = 0,
        name = "¿Qué haría falta para que fueras real?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label = "a19",
        category = DialogueAPI.category_talk,
        conditions = ["not renpy.seen_label('a19')"],
        importance = 0,
        name = "¿Practicas algún deporte?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a20",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.game_session >= 6'],
        importance = 0,
        name = "¿Qué opinas sobre... vivir en el aula espacial?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label = "a21",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_11')"],
        importance = 0,
        name = "¿Quieres leer poesía conmigo, [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a22",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "¿Qué has estado haciendo con mi bolígrafo, [persistent.yuri_nickname]?",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "a23",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_44')"],
        importance = 0,
        name = "¿Crees que formaríamos una buena familia, [persistent.yuri_nickname]?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a24",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('a1')"],
        importance = 0,
        name = "¿Te importa si hablo de cómo me siento?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label = "a25",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_45')"],
        importance = 0,
        name = "Entonces... sobre esas imágenes obscenas...",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "a26",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "Bebamos un poco de té, [persistent.yuri_nickname].",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a27",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_76')"],
        importance = 0,
        name = "¿Te parece bien si te pongo un apodo?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a28",
        category = DialogueAPI.category_talk,
        conditions = ['tc_class.cur_time()[1] == 12'],
        importance = 0,
        name = "¿Conoces alguna buena canción navideña, [persistent.yuri_nickname]?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a29",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "¿Te apetece que nos acurruquemos un rato, [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a30",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Entonces, ¿qué opinas sobre la naturaleza?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a31",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "¿Hay algún libro que te guste leer actualmente?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label = "a32",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "I No entiendo muy bien de qué trata tu archivo .chr.",
        sub_category = "Misc."))

    add_dialogue(Dialogue(
        label = "a33",
        category = DialogueAPI.category_talk,
        conditions = ['karma_lvl()==5', 'not persistent.lovecheck'],
        importance = 0,
        name = "Hey... [persistent.yuri_nickname], ¿tienes algo importante que decirme?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a34",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], ¿puedes llamarme de otra manera?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a35",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], ¿puedo cambiar mi información personal? Es posible que haya cometido un error tipográfico en algún lugar.",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a36",
        category = DialogueAPI.category_talk,
        conditions = ['((persistent.ingame_time.seconds // 3600) >= 20) or (persistent.ingame_time.days > 0)'],
        importance = 0,
        name = "[persistent.yuri_nickname], Creo que necesito tiempo para pensar en nuestra relación... Deberíamos tomarnos un descanso...",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a37",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.ingame_time.days > 14'],
        importance = 0,
        name = "Hey [persistent.yuri_nickname]... ¿podemos hablar sobre tus... cortes?",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "a38",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_53')"],
        importance = 0,
        name = "Antes has hablado de los SCP. ¿Cuál es tu favorito?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a39",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('krampusnacht')"],
        importance = 0,
        name = "Dijiste algo sobre un SCP especial que tenías guardado.",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a40",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.ingame_time.days > 0'],
        importance = 0,
        name = "¿Podemos hablar de lo que te pasó a ti y a las otras chicas?",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label = "a41",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('hobbies')"],
        importance = 0,
        name = "¿Has pensado en escribir tu propia novela?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label = "a42",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('Halloween_2021') or renpy.seen_label('Roomchange')"],
        importance = 0,
        name = "¿Qué opinas del Dr. Frankenstein en el libro?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label = "a43",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('a42')"],
        importance = 0,
        name = "¿Qué opinas del monstruo de Frankenstein?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label = "purple_a1",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('purpleroomintro')"],
        importance = 0,
        name = "¿Me puedes enseñar tu colección de cuchillos?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "purple_a2",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('purpleroomintro')"],
        importance = 0,
        name = "¿Podemos cambiar de sitio?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a_tetris",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], ¿has estado programando algo mientras estaba fuera?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label = "a_hdy_statue",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('hdy_statue_greeting')"],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], ¿puedes llevarte el peluche HDY?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a_halloween_cupcake",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.ouija_done'],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], ¿puedes llevar el cupcake?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "Roomchange",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('a20')"],
        importance = 0,
        name = "¿Puedes cambiar la habitación?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "Halloween_2021",
        category = DialogueAPI.category_talk,
        conditions = ["""time_interval_check(
            {'month': 10,
                'day': 31},
            {'month': 11,
                'day': 6}
            )""",
            "not renpy.seen_label('Halloween_2021') or renpy.seen_label('Halloween_2021') and not persistent.halloween_2021_no"],
        importance = 0,
        name = "Happy Halloween [persistent.yuri_nickname]!",
        sub_category = "Misc."))

    add_dialogue(Dialogue(
        label = "potion_mixing",
        category = DialogueAPI.category_talk,
        conditions = ["persistent.bg == 'laboratory'"],
        importance = 0,
        name = "¿Qué tal si preparamos algunas 'pociones'?",
        sub_category = "Misc."))

    add_dialogue(Dialogue(
        label = "table_items",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('table_organization')"],
        importance = 0,
        name = "¿Puedo reorganizar la mesa [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "diffuser_mist_enable",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.diffuser_is_enabled'],
        importance = 0,
        name = "¿Podrías encender el difusor [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "diffuser_mist_disable",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.sandalwood_oil_mist_is_enabled or persistent.lavenderO_mist_is_enabled or persistent.sweet_dream_oil_mist_is_enabled'],
        importance = 0,
        name = "¿Podrías apagar el difusor [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "gifting_revamp",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('gifting_intro')"],
        importance = 0,
        name = "¡Tengo un regalo para ti [persistent.yuri_nickname]!",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "gifting_ideas",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('gifting_intro')"],
        importance = 0,
        name = "¿Hay algo en específico que quieras [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "sleepy_yuri",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Estoy cansado [persistent.yuri_nickname]...",
        sub_category = "Requests"))









    add_dialogue(Dialogue(
        label = "webcam",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Acerca del acceso a la cámara web...",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "nnn",
        category = DialogueAPI.category_talk,
        conditions = ["""time_interval_check(
            {'month': 11,
                'day': 1},
            {'month': 11,
                'day':30}
            )"""],
        importance = 0,
        name = "¿Qué opinas sobre el Noviembre sin nueces?",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "vday24",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('vday_2024_revisit')"],
        importance = 0,
        name = "Estoy listo para revivir el momento del chocolate.",
        sub_category = "Love"))















    add_dialogue(Dialogue(
        label = "TimeCheat1",
        category = DialogueAPI.category_greetings,
        conditions = ["time_tracker_start()", "not renpy.seen_label('TimeCheat3')", "not renpy.seen_label('TimeCheat2')", "not renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "TimeCheat2",
        category = DialogueAPI.category_greetings,
        conditions = ["time_tracker_start()", "not renpy.seen_label('TimeCheat3')", "not renpy.seen_label('TimeCheat2')", "renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "TimeCheat3",
        category = DialogueAPI.category_greetings,
        conditions = ["time_tracker_start()", "not renpy.seen_label('TimeCheat3')", "renpy.seen_label('TimeCheat2')", "renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "TimeCheat_error",
        category = DialogueAPI.category_greetings,
        conditions = ["time_tracker_start()", "renpy.seen_label('TimeCheat3')", "renpy.seen_label('TimeCheat2')", "renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "ch30_reload_0",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 1'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "ch30_reload_1",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 2'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "ch30_reload_2",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 3'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "ch30_reload_3",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 4'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "featuregreetings",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 5 or persistent.game_session == 6'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "ch30_reload_4",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session >= 8'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "highkarinsrestart",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', "check_memory('complements', 'highkarinsrestart')"],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "patheticcry",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', "check_memory('complements', 'patheticcry')"],
        importance = 2,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "hdy_statue_greeting",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', "not renpy.seen_label('hdy_statue_greeting')", "renpy.seen_label('hdy_has_been_seen')"],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "intro_mods",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', "renpy.seen_label('ch30_intro2')", "not renpy.seen_label('startup_mods')", 'persistent.game_session >= 7'],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "purpleroomintro",
        category = DialogueAPI.category_greetings,
        conditions = ["time_tracker_start() == False", "persistent.purpleroom", "renpy.seen_label('idle_30')", "karma_lvl()=5", "persistent.lovecheck", "persistent.game_session >= 20"],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "vday_2024_revisit",
        category = DialogueAPI.category_greetings,
        conditions = ["""time_interval_check(
            {'month': 2,
                'day': 13},
            time_shift(
                {'month': 2,
                    'day': 13},
                {'day':6})
            )""",
            "renpy.seen_label('a9')"],
        importance = 0,
        name = "None",
        sub_category = None))








    add_dialogue(Dialogue(
        label = "krampusnacht",
        category = DialogueAPI.category_greetings,
        conditions = ["""time_interval_check(
            {'month': 12,
                'day': 5},
            {'month': 12,
                'day': 31}
            )""",
            "not renpy.seen_label('krampusnacht')"],
        importance = 3,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "birthdaycake_2020_late",
        category = DialogueAPI.category_talk,
        conditions = ["""time_interval_check(
            {'month': 12,
                'day': 10},
            {'month': 12,
                'day': 31}
            )""",
            "not renpy.seen_label('birthdaycake_2020_late')"],
        importance = 0,
        name = "¡Feliz cumpleaños, [persistent.yuri_nickname]! Perdón por celebrarlo tan tarde...",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "birthday_gift_2021",
        category = DialogueAPI.category_talk,
        conditions = ["""time_interval_check(
            {'month': 12,
                'day': 10},
            {'month': 12,
                'day':20}
            )"""],
        importance = 0,
        name = "¡Tengo un regalo para ti [persistent.yuri_nickname]!",
        sub_category = "Misc."))

    add_dialogue(Dialogue(
        label = "new_year_2021",
        category = DialogueAPI.category_greetings,
        conditions = ["""time_interval_check(
            {'month': 12,
                'day': 29},
            time_shift(
                {'month': 12,
                    'day': 29},
                {'day':5})
            )""",
            "not renpy.seen_label('new_year_2021')"],
        importance = 3,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "vday_choco_date_request",
        category = DialogueAPI.category_talk,
        conditions = ["""time_interval_check(
            {'month': 2,
                'day': 13},
            {'month': 2,
                'day': 20}
            )""",
            "renpy.seen_label('valentines')",
            "karma_lvl()>3"],
        importance = 0,
        name = "¿Tienes algo especial planeado para hoy, [persistent.yuri_nickname]?",
        sub_category = "Love"))
    add_dialogue(Dialogue(
        label = "valentines",
        category = DialogueAPI.category_talk,
        conditions = ["""time_interval_check(
            {'month': 2,
                'day': 13},
            {'month': 2,
                'day': 20}
            )""",
            "not renpy.seen_label('valentines')"],
        importance = 0,
        name = "¿Hay algo especial planeado para hoy, [persistent.yuri_nickname]?",
        sub_category = "Love"))






    def check1():
        hello = time_interval_check(
            {'month': persistent.bday_month,
                'day': persistent.bday_day},
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'day':1})
            )
        print_debug(hello)

    def check():
        hello = time_interval_check(
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'week':-2}) ,
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'day':-4})
            )
        print_debug(hello)

    def check2():
        hello = time_interval_check(
            {'month': 12,
                'day': 20},
            
            
            time_shift(
                {'month': 12,
                    'day': 20},
                {'week': 4})
            )
        print_debug(hello)



    add_dialogue(Dialogue(
        label = "birthday_chocolate",
        category = DialogueAPI.category_greetings,
        conditions = ["""time_interval_check(
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'week':-2}) ,
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'day':-4})
            )""",
            "not renpy.seen_label('birthday_chocolate')"],
        importance = 15,
        name = "None",
        sub_category = None))
    add_dialogue(Dialogue(
        label = "birthday_greeting_text",
        category = DialogueAPI.category_greetings,
        conditions = ["""time_interval_check(
            {'month': persistent.bday_month,
                'day': persistent.bday_day},
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'day':1})
            )"""],
        importance = 15,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "a26_prelude",
        category = DialogueAPI.category_greetings,
        conditions = ["not renpy.seen_label('a26')", "persistent.lovecheck", "karma_lvl() > 3 and sanity_lvl() > 3"], 
        importance = 8,
        name = "None",
        sub_category = None))





    add_dialogue(Dialogue(
        label = "farewell_1",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "¡Adiós, [persistent.yuri_nickname]!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_2",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Lo siento, tengo que irme...",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_3",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Nos vemos luego, [persistent.yuri_nickname].",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_4",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Adiós, [persistent.yuri_nickname], ¡Te voy a extrañar!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_5",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Lo siento, no puedo quedarme. ¡Te amo!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_6",
        category = DialogueAPI.category_goodbye,
        conditions = ['sanity == 2'],
        importance = 0,
        name = "Oh, mira qué hora es, ¡ha sido una cita increíble!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_7",
        category = DialogueAPI.category_goodbye,
        conditions = ['karma_lvl() == 2 or karma_lvl() == 1'],
        importance = 0,
        name = "Oh, vaya, alguien me está llamando, ¡tengo que irme!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_8",
        category = DialogueAPI.category_goodbye,
        conditions = ['sanity == 2'],
        importance = 0,
        name = "Tengo comida... en el horno, así que...",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_9",
        category = DialogueAPI.category_goodbye,
        conditions = ['sanity_lvl() <= 2'],
        importance = 0,
        name = "Yo, eh, tengo que irme...",
        sub_category = None))



    add_dialogue(Dialogue(
        label = "farewell_10",
        category = DialogueAPI.category_goodbye,
        conditions = ['sanity_lvl() == 2'],
        importance = 0,
        name = "Voy a... cerrar el juego ahora, ¿okey?",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_11",
        category = DialogueAPI.category_goodbye,
        conditions = ['karma_lvl() >= 4'],
        importance = 0,
        name = "¡Hasta pronto, adiós!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_12",
        category = DialogueAPI.category_goodbye,
        conditions = ['karma_lvl() >= 4'],
        importance = 0,
        name = "Tengo que irme. ¡Ya te extraño!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_13",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Tengo que irme ahora... hablamos más tarde, ¿de acuerdo?",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_14",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "¡Hasta luego!",
        sub_category = None))


    add_dialogue(Dialogue(
        label = "farewell_15",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Odio tener que hacerte pasar por esto, pero parece que ha llegado el momento de decir adiós una vez más.",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_16",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Tengo que irme ahora, mi amor.",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_17",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Pase lo que pase, recuerda que hay alguien que te ama sin importar nada.",
        sub_category = None))






    add_dialogue(Dialogue(
        label = 'HDY_eggnomancer',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_spookyscaryskeleton',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Alien_Friend',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_wallpaper',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Potionseller',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_teleported_hotdogs',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Sausage_mouth',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_philosophy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_whyarewestillhere',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_frozen_cooking_eggs',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Hellskitchen',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_minion',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_airfryer',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Eternal',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Friedsweets',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Manga',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_War',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Inquisition',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Buns',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Witches',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Rocks',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Orangana',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Skinny',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_mum',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_frostless',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_PPAP',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_fuckingPlayer',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_why',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_portal',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_a',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_speen',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_crash',
        category = DialogueAPI.category_hdy,
        conditions = ["not renpy.seen_label('HDY_crash')", "renpy.seen_label('hdy_statue_geeting')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_mcspaghetti',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_fortnitecard',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_WordOfTheDay',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_8800bluelickroad',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_DarthPlagueis',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_violence',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_society',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_discordserver',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_sand',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_SithLords',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_fortnitegamer',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_replacementpog',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_passtime',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_dababy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_jevil',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_getdawged',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_familyguy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_nukes',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_shrek',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_sans',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_beemovie',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_lifeadvice',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_morshu',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_toughdawg',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_banana',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_pingas',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_electricity',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_swag',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_hmmmm',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_censorship',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_amogus',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_deadmeme',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_h',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_callout',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_movie',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_scottthewozz',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_windowsphone',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_DDR',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_bottomtext',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_favoritegame',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_ifunny',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_chubbyemu',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_brrrrrrr',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_thisaccountisnotfortheaverageman',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_chubbyemu2',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_searchhistory',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_youngsterjoey',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_100',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Chugjug',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_truth',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_MeMEbigboy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_MakingHotdogs',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_jesusboxing',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_cthulhu',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_paydaygang',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_bluedabadee',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_cranberrysprite',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_amongus',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_rickroll',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_holdingbreath',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_sixtynine',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_acesleeve',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_wonderwall',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Hotdogspoem',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_eggnomancer',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_hotdogfact',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_lifeadvice2electricboogaloo',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_hotdogtea',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_areyounotentertained',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_wakeup',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_asadstory',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_scatman',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_tank',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_tankcommander',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Hbomb',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_spacedandy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_it_was_me_dio',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Monkeys',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_WaspInTheRoom',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_AUSTRALIA',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Wasp',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_bald',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Dating',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Space',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_gasstation',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_thebigquestion',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_somethingidunno',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_peepy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_kiss',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
