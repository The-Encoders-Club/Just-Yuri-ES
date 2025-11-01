


init python:
    def dumpPersistentToFile(dumped_persistent,dumppath):
        
        
        
        
        
        
        
        dumped_persistent=vars(dumped_persistent)
        
        fo = open(dumppath, "w")
        
        for key in sorted(dumped_persistent.iterkeys()):
            fo.write(str(key) + ' - ' + str(type(dumped_persistent[key])) + ' >>> '+ str(dumped_persistent[key]) + '\n\n')
        
        fo.close()

label import_ddlc_persistent:
    python:

        from renpy.loadsave import dump, loads
        from glob import glob


        if renpy.macintosh:
            rv = "~/Library/RenPy/"
            check_path = os.path.expanduser(rv)

        elif renpy.windows:
            if 'APPDATA' in os.environ:
                check_path =  os.environ['APPDATA'] + "/RenPy/"
            else:
                rv = "~/RenPy/"
                check_path = os.path.expanduser(rv)

        else:
            rv = "~/.renpy/"
            check_path = os.path.expanduser(rv)

        ddlc_save_path = glob(check_path + 'DDLC/persistent')
        if not ddlc_save_path:
            ddlc_save_path = glob(check_path + 'DDLC-*/persistent')

    $ quick_menu = False
    scene black
    with Dissolve(1.0)


    if ddlc_save_path:
        $ ddlc_save_path = ddlc_save_path[0]
        "Se han encontrado datos guardados de Doki Doki Literature Club en [ddlc_save_path]."
        menu:
            "¿Desea importar los datos guardados de Doki Doki Literature Club a [config.name]?\n(DDLC no se verá afectado)"
            "Sí, importar datos guardados de DDLC.":
                pause 0.3
                pass
            "No, no importar.":
                pause 0.3
                return
    else:


        "No se han encontrado datos guardados de Doki Doki Literature Club."
        menu:
            "Los datos guardados no se importarán en este momento."
            "Okey":
                pause 0.3
                return

    python:


        import codecs
        f=open(ddlc_save_path,"rb")
        s = codecs.decode(f.read(), encoding='zlib', errors='strict')
        f.close()

        old_persistent=loads(s)

































































        if old_persistent.playthrough is not None:
            persistent.playthrough = old_persistent.playthrough









        if old_persistent._chosen is not None:
            persistent._chosen=old_persistent._chosen




        if old_persistent._seen_audio is not None:
            persistent._seen_audio=old_persistent._seen_audio





        if old_persistent._seen_ever is not None:
            persistent._seen_ever=old_persistent._seen_ever




        if old_persistent._chosen is not None:
            persistent._seen_images=old_persistent._seen_images




        if old_persistent._seen_translates is not None:
            persistent._seen_translates=old_persistent._seen_translates




        if old_persistent.clear is not None:
            persistent.clear=old_persistent.clear



        if old_persistent.clearall is not None:
            persistent.clearall=old_persistent.clearall







        if old_persistent.ghost_menu is not None:
            persistent.ghost_menu=old_persistent.ghost_menu
            persistent.seen_ghost_menu = old_persistent.seen_ghost_menu



        if old_persistent.monika_kill is not None:
            persistent.monika_kill=old_persistent.monika_kill



        if old_persistent.monika_reload is not None:
            persistent.monika_reload=old_persistent.monika_reload



        if old_persistent.monikatopics is not None:
            persistent.monikatopics=old_persistent.monikatopics



        if old_persistent.playername is not None:
            persistent.playername=old_persistent.playername
        player=persistent.playername



        if old_persistent.seen_eyes is not None:
            persistent.seen_eyes=old_persistent.seen_eyes



        if old_persistent.seen_sticker is not None:
            persistent.seen_sticker=old_persistent.seen_sticker



        if old_persistent.special_poems is not None:
            persistent.special_poems=old_persistent.special_poems



        if persistent.steam is not None:
            persistent.steam=old_persistent.steam



        if old_persistent.tried_skip is not None:
            persistent.tried_skip=old_persistent.tried_skip








    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
