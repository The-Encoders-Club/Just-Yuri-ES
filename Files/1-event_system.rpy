


















































init -998 python:
    class EventAPI:
        event_handlers = {}
        
        @staticmethod
        def register(event_class, *callbacks):
            if not inspect.isclass(event_class):
                print_fatal(TypeError("Se esperaba una clase de evento, pero en su lugar se obtuvo una instancia"))
                return
            
            if not event_class in EventAPI.event_handlers:
                EventAPI.event_handlers[event_class] = EventHandler(event_class, callbacks)
            else:
                EventAPI.event_handlers[event_class].register(callbacks)
        
        @staticmethod
        def call(event: Event):
            if event.__class__ in EventAPI.event_handlers:
                EventAPI.event_handlers[event.__class__].call(event)
            else:
                print_error(NameError("No se pudo ejecutar el evento " + str(event.__class__.__name__) + " ya que el este no fue registrado antes de convocarlo"))
        
        @staticmethod
        def is_registered(event_class):
            return event in EventAPI.event_handlers

init -999 python:
    class Event:
        id = None
        canceled = False
        def cancel(self):
            self.canceled = True

    class EventHandler:
        event = None
        callbacks = []
        
        def __init__(self, event : Event, callbacks):
            self.event = event
            self.callbacks = []
            self.register(callbacks)
        
        def register(self, callbacks):
            print_debug("Registando " + str(len(callbacks)) + " callback(s) para event " + self.event.__name__)
            for callback in callbacks:
                if callback and not callback in self.callbacks and type(callback) != tuple:
                    print_debug("  - Registrando callback: " + repr(callback))
                    self.callbacks.append(callback)
        
        def call(self, event : Event):
            for callback in self.callbacks:
                try:
                    callback(event)
                except BaseException as exception:
                    print("No se pudo ejecutar event " + self.event.__name__ + " ya que la función generó un error al ejecutarse")
                    print_error(exception, new_traceback=False)

init -997 python:



    def callback_start():
        EventAPI.call(StartEvent())

    def callback_label(label_name, called):
        global current_label; current_label = label_name
        event = LabelEvent(str(label_name), called)
        EventAPI.call(event)
        
        if event.label_name == "_quit":
            callback_quit()
            return
        if event.label_name == "save_and_quit":
            callback_safe_quit()
            return

    def callback_quit():
        persistent.crash = False
        EventAPI.call(QuitEvent())

    def callback_safe_quit():
        persistent.crash = False
        EventAPI.call(SafeQuitEvent())

    def callback_exit():
        old_persistent = load_persistent(save_directory)
        if old_persistent:
            print("Realizando copias de seguridad de archivos persistentes...")
            if not os.path.exists(backup_directory):
                os.makedirs(backup_directory)
            now = datetime.datetime.today()
            save_persistent(old_persistent, backup_directory, "persistent_backup-" + str(now.year) + "-" + str(now.month) + "-" + str(now.day))
            print("- ¡Hecho!")
        
        EventAPI.call(ExitEvent())

    def callback_crash():
        EventAPI.call(CrashEvent())

    def callback_tick():
        EventAPI.call(callback_tick_event)
        callback_tick_event.ticks += 1

    if persistent.crash:
        crashed = True
        callback_crash()
    else:
        crashed = False
        persistent.crash = True
        renpy.save_persistent()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
