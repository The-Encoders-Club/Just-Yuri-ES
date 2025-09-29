








init -999 python:

    submods = {}
    submods.mods = {}
    submods.mod_count = 0

    submods.modinfo_template = {
        "name": "",
        "id": "",
        "version": "1.0.0",
        "dependencies": [],
        "developer_mode": False
    }


    getting_started_content = """¡Bienvenido a la comunidad de submodding! - Versión de documentos 1.0.0

Si estás viendo esto por primera vez, estos archivos se generan automáticamente cada vez que a una carpeta de submod le falta un archivo modinfo.json.
Para crear un submod, cambia cualquier información que desees en el archivo modinfo.json, crea tu primer archivo .rpy y comienza a implementar lo que se te ocurra.

Para una breve introducción a Ren’Py, consulta: https://www.renpy.org/doc/html/quickstart.html#the-ren-py-launcher  
Si planeas crear un submod más avanzado, también podrías necesitar conocimientos de Python. Un buen lugar para aprender lo básico es: https://www.w3schools.com/python/python_intro.asp

Para añadir diálogos al menú de conversación, usa el método add_dialogue y proporciónale tu propia instancia de Dialogue:

label test_label:
    $ show_chr("A-ABGBA-AAAA")
    y "¡Hola!"

init python:
    add_dialogue(Dialogue("test_label", DialogueAPI.category_talk, name="Saludar a Yuri", sub_category="Saludos"))

Puedes obtener el código de sprite a través del panel de control cuando actives el modo desarrollador.

Este mod contiene varias APIs para ayudar a acelerar el desarrollo, ya que la fuente de Just Yuri está algo desordenada en este momento. Rectificaremos ese desorden con el tiempo.  
Puedes encontrar las fuentes aquí: https://github.com/DarkskullDawnZenith/JustYuri

En el futuro, esta documentación estará más completa y será más amigable para el usuario, pero por ahora solo cubrirá lo mínimo necesario.

Puedes eliminar estos documentos si quieres liberar espacio para tu mod. Si alguna vez necesitas regenerarlos, borra el archivo modinfo.json y reinicia el juego. ¡Diviértete!
"""

    modinfo_setup_content = """{
    ####################################################################################
    # This is what the Just Yuri mod reads to figure out what this submod is.          #
    # This is always automatically generated when a modinfo.json file is not detected. #
    ####################################################################################

    # The name of your submod. This will show up in game in the mods menu.
    "name": "",

    # The unique id of your submod. This is used in the dependencies blocks of other mods.
    "id": "",

    # The version of your submod. This can be anything you want, but keep it close to the format #.#.#
    "version": "1.0.0",

    # The unique ids of each submod that this submod requires.
    # If any id is present here and the mod isn't loaded, the game will crash and display any mods that are missing
    # Also supports putting a single string as well if you don't want to use a list
    "dependencies": [],

    # Whether to enable debug mode for Just Yuri. Adds additional information to the logs and allows access to the control panel
    "developer_mode": false
}
"""








    def parse_mod_id(name):
        match = regex.match("[a-z0-9\\_\\-]*", name.lower().replace(" ", "_"))
        return match.group(0) if match != None else "unknown"

    class Submod:
        name = None
        id = None
        version = "1.0.0"
        description = None
        dependencies = []
        icon = None
        path = None
        
        def __init__(self, mod_name, mod_id, path):
            self.name = mod_name
            self.id = mod_id
            self.path = path
            
            self.icon = Transform(os.path.join(config.gamedir, "images", "default_submod.png"), size=(100,100), fit="contain")

    print("Comprobando submods...")
    request_dev_access = False
    dev_access = False






    submods_dir = os.path.join(config.gamedir, "submods")
    placeholder_dir = os.path.join(submods_dir, "_placeholder")
    print("submods_dir is:", submods_dir)


    if not os.path.isdir(submods_dir):
        print("Creando carpeta submods...")
        try:
            os.makedirs(submods_dir, exist_ok=True)
        except Exception as e:
            print(f"Error al crear el directorio submods en {submods_dir}: {e}")



    if os.path.isdir(submods_dir) and not os.path.isdir(placeholder_dir):
        print("Creando carpeta placeholder...")
        try:
            os.makedirs(placeholder_dir, exist_ok=True)
            
            
            placeholder_info_path = os.path.join(placeholder_dir, "modinfo.json")
            with open(placeholder_info_path, 'w', encoding='utf-8') as f:
                placeholder_info = submods.modinfo_template.copy()
                placeholder_info["name"] = "Placeholder"
                placeholder_info["id"] = "placeholder"
                json.dump(placeholder_info, f, indent=4)
            
            
            placeholder_icon_path = os.path.join(placeholder_dir, "icon.png")
            source_icon_path = os.path.join(config.gamedir, "images", "default_submod.png")
            print(f"Intentando copiar el icono desde: {source_icon_path} to {placeholder_icon_path}")
            try:
                if os.path.isfile(source_icon_path):
                    copyfile(source_icon_path, placeholder_icon_path)
                    print("¡Icono copiado con éxito!")
                else:
                    print(f"Error: Archivo de ícono fuente no encontrado en {source_icon_path}")
            except Exception as e:
                print(f"Se ha producido un error al copiar el icono del placeholder: {e}")
            
            
            
            placeholder_docs_dir = os.path.join(placeholder_dir, "documentation")
            if not os.path.isdir(placeholder_docs_dir):
                os.makedirs(placeholder_docs_dir, exist_ok=True)
            
            
            getting_started_path_placeholder = os.path.join(placeholder_docs_dir, "0 - Empezando.txt")
            modinfo_setup_path_placeholder = os.path.join(placeholder_docs_dir, "Configuración de Modinfo.txt")
            
            try:
                print("  - Creando placeholder '0 - Empezando.txt'...")
                with open(getting_started_path_placeholder, 'w', encoding='utf-8') as f:
                    f.write(getting_started_content)
            except Exception as e:
                print(f"  - No se pudo crear el placeholder. '0 - Empezando.txt': {e}")
            
            try:
                print("  - Creando placeholder 'Configuración de Modinfo.txt'...")
                with open(modinfo_setup_path_placeholder, 'w', encoding='utf-8') as f:
                    f.write(modinfo_setup_content)
            except Exception as e:
                print(f"  - No se pudo crear el placeholder 'Configuración de Modinfo.txt': {e}")
        
        except Exception as e:
            print(f"Error al crear placeholder en {placeholder_dir}: {e}")


    if os.path.isdir(submods_dir):
        for directory in os.scandir(submods_dir):
            if not directory.is_dir() or directory.path == placeholder_dir:
                continue
            
            print("Modo de escaneo: " + directory.name)
            submods.mod_count += 1
            mod_docs_dir = os.path.join(directory.path, "documentation")
            mod_error_path = directory.path 
            mod_info_path = os.path.join(directory.path, "modinfo.json")
            mod_icon_path = os.path.join(directory.path, "icon.png")
            
            print("mod_docs_dir:", mod_docs_dir)
            print("mod_info_path:", mod_info_path)
            print("mod_icon_path", mod_icon_path)
            
            submod = Submod(directory.name, parse_mod_id(directory.name), mod_error_path)
            
            
            if not os.path.isfile(mod_info_path):
                print("  - Mod " + submod.id + " no contiene un archivo modinfo.json. Creando archivos predeterminados...")
                
                
                if not os.path.isdir(mod_docs_dir):
                    print("  - Creación del directorio de documentación...")
                    try:
                        os.makedirs(mod_docs_dir, exist_ok=True)
                    except Exception as e:
                        print(f"  - No se pudo crear el directorio de documentación: {e}")
                        
                        print_error(e, path=mod_error_path)
                
                
                if os.path.isdir(mod_docs_dir):
                    getting_started_path = os.path.join(mod_docs_dir, "0 - Empezando.txt")
                    modinfo_setup_path = os.path.join(mod_docs_dir, "Configuración de Modinfo.txt")
                    
                    
                    try:
                        print("  - Creando '0 - Empezando.txt'...")
                        with open(getting_started_path, 'w', encoding='utf-8') as f:
                            f.write(getting_started_content)
                    except Exception as e:
                        print(f"  - Error al crear '0 - Empezando.txt': {e}")
                        print_error(e, path=mod_error_path) 
                    
                    
                    try:
                        print("  - Creando 'Configuración de Modinfo.txt'...")
                        with open(modinfo_setup_path, 'w', encoding='utf-8') as f:
                            f.write(modinfo_setup_content)
                    except Exception as e:
                        print(f"  - Error al crear 'Configuración de Modinfo.txt': {e}")
                        print_error(e, path=mod_error_path) 
                else:
                    print("  - Se omite la creación del archivo de documentación porque el directorio no existe.")
                
                
                
                print("  - Creando modinfo.json...")
                try:
                    with open(mod_info_path, 'w', encoding='utf-8') as file:
                        modinfo = submods.modinfo_template.copy()
                        modinfo["name"] = submod.name or "" 
                        modinfo["id"] = submod.id or ""     
                        json.dump(modinfo, file, indent=4)
                    print("  - ¡Se ha terminado de crear los archivos predeterminados!")
                except Exception as e:
                    print("  - Error al crear modinfo.json")
                    print_error(e, path=mod_error_path)
            
            
            if os.path.isfile(mod_info_path):
                try:
                    with open(mod_info_path, 'r', encoding='utf-8') as file: 
                        modinfo = json.load(file)
                        submod.name = str(modinfo.get("name", submod.name))
                        submod.id = str(modinfo.get("id", submod.id))
                        submod.version = str(modinfo.get("version", submod.version))
                        submod.description = modinfo.get("description", submod.description)
                        submod.dependencies = modinfo.get("dependencies", submod.dependencies)
                        request_dev_access = modinfo.get("developer_mode", request_dev_access)
                        
                        if submod.description is not None:
                            submod.description = str(submod.description)
                        if isinstance(submod.dependencies, str):
                            submod.dependencies = [submod.dependencies]
                        elif not isinstance(submod.dependencies, list):
                            submod.dependencies = []
                
                except json.JSONDecodeError as e:
                    print(f"  - No se pudo cargar modinfo.json: formato JSON no válido - {e}")
                    print_error(e, path=mod_error_path)
                except Exception as e:
                    print(f"  - No se pudo cargar modinfo.json: {e}")
                    print_error(e, path=mod_error_path)
            
            
            if os.path.isfile(mod_icon_path):
                print("  - Mod " + submod.id + " tiene un icono. Cargando imagen...")
                try:
                    submod.icon = Transform(mod_icon_path, size=(100, 100), fit="contain")
                except Exception as e:
                    print("  - No se pudo cargar icon.png")
                    print_error(e, path=mod_error_path)
            
            
            renpy.image(submod.id + ":icon", submod.icon)
            submods.mods[submod.id] = submod
            print("  - Mod ID: " + submod.id + ", Version: " + submod.version)
            print("  - Dependencias: " + str(submod.dependencies))

    else:
        print(f"Advertencia: El directorio de submods {submods_dir} no existe o no es accesible. Se omite la carga de submods.")



    print("Comprobando si hay dependencias que faltan en los submods cargados...")
    should_continue = True
    missing_dependency_errors = []

    for key, submod in submods.mods.items():
        if len(submod.dependencies) > 0:
            for dependency in submod.dependencies:
                parsed_dependency_id = parse_mod_id(dependency)
                if parsed_dependency_id not in submods.mods:
                    error_message = f"El submod '{submod.id}' carece de dependencia '{parsed_dependency_id}'"
                    print(f"  - {error_message}")
                    missing_dependency_errors.append({
                        "submod_id": submod.id,
                        "missing_dependency": parsed_dependency_id,
                        "path": submod.path
                    })
                    print_error(KeyError(error_message), path=(submod.path, config.basedir))
                    should_continue = False

    if not should_continue:
        print_fatal(KeyError("Uno o más submods carecen de dependencias. Consulte el archivo error.log o la salida de la consola para obtener más detalles."))


    if request_dev_access:
        print("Uno o más mods han solicitado el modo desarrollador. Activando el modo desarrollador...")
        config.developer = True 
        dev_access = True 

    print("¡Carga de mods completada! Se han cargado " + str(submods.mod_count) + " mod(s)")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
