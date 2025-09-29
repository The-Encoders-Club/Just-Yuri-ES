
default blocked_dialogues = []


init -998 python:



    class DialogueAPI:
        
        
        
        
        category_talk = "actives"
        category_goodbye = "farewells"
        category_greetings = "greetings"
        category_idle = "idles"
        category_hdy = "hdy"

















































































































































    def controlled_random(dlist, selection_detail):
        global blocked_dialogues
        size_of_blocked_dialogues = 5
        
        dlist_no_block = list(set(dlist) - set(blocked_dialogues))
        if dlist_no_block == []:
            if blocked_dialogues == []:
                return None
            else:
                chosen_dialogue = blocked_dialogues.pop(-1)
        
        else:
            chosen_dialogue = random.choice(dlist_no_block)
        
        if len(blocked_dialogues) > size_of_blocked_dialogues:
            blocked_dialogues.pop(-1)
        blocked_dialogues.insert(0, chosen_dialogue)
        return chosen_dialogue























































init -999 python:

    import datetime
    from time_module import time_shift, time_interval_check






    dialogue_db = {}
    queued_dialoguee = []


    if persistent.dialogue_memory == None:
        persistent.dialogue_memory = {}



    class Dialogue:
        
        def __init__(self, label, category, conditions = [], importance = 0, name = None, sub_category = None):
            
            self.label = label
            
            self.category = category
            
            self.conditions = conditions
            
            if label in persistent.dialogue_memory:
                self.memory = persistent.dialogue_memory[label]
            else:
                self.memory = []
            
            
            
            
            
            self.importance = importance
            
            self.name = name
            self.sub_category = sub_category
        
        
        
        
        
        
        def conditions_met(self):
            if not self.conditions:  
                return True  
            
            for condition in self.conditions:
                try:
                    if not eval(condition):
                        print_debug("Condición no cumplida para " + self.label + ": " + condition)
                        return False
                except Exception as e:
                    return False  
            
            return True  


    def add_dialogue(dialogue_class):
        dialogue_db[dialogue_class.label] = dialogue_class

    def call_dialogue(selection_method = "pool", selection_detail = "idles", screener = False):
        
        if selection_method == "specific":
            if renpy.has_label(selection_detail):
                if screener:
                    print(dialogue_db[selection_detail].conditions)
                    print(dialogue_db[selection_detail].conditions_met())
                else:
                    print_debug("calling: " + selection_detail)
                    renpy.call(selection_detail)
            else:
                print_debug(selection_detail + ": label does not exist")
                renpy.error(selection_detail + ": label does not exist")
                return
        
        elif selection_method == "pool":
            
            
            dialogue_list = []
            importance_value = -100
            for dialogue_name in dialogue_db.keys():
                current_dialogue = dialogue_db[dialogue_name]
                if current_dialogue.category == selection_detail:
                    if current_dialogue.conditions_met():
                        
                        
                        
                        
                        
                        if current_dialogue.importance == importance_value:
                            dialogue_list.append(dialogue_name)
                        elif current_dialogue.importance > importance_value:
                            dialogue_list = [dialogue_name]
                            importance_value = current_dialogue.importance
            
            if screener:
                print(dialogue_list)
                return
            
            
            if selection_detail in ["idles", "greetings", "hdy"]:
                selected_dialogue = controlled_random(dialogue_list, selection_detail)
                
                if selection_detail == "idles":
                    persistent.current_yuriidle = selected_dialogue
            
            elif selection_detail == "actives":
                active_dict = {}
                for dialogue_name in dialogue_list:
                    current_dialogue = dialogue_db[dialogue_name]
                    if current_dialogue.sub_category in active_dict:
                        
                        active_dict[current_dialogue.sub_category].append((current_dialogue.name, current_dialogue.label))
                    else:
                        active_dict[current_dialogue.sub_category] = [(current_dialogue.name, current_dialogue.label)]
                
                
                scroll_button_items = list(active_dict.keys()) 
                for i, item in enumerate(scroll_button_items):
                    scroll_button_items[i] = [item, 0]
                
                
                selected_dialogue = renpy.call_screen(
                    "three_choice_menu", 
                    active_dict, 
                    scroll_button_items, 
                    [("¿Estaría bien si cambiara un poco la música?", "change_music"), ("No importa", "prompt_menu"), ("¿Por qué no te cambias de ropa, Yuri?", "changeoutfit")],
                    random.sample(list(active_dict.keys()), len(active_dict)), 
                    "no", 
                    0)
            
            elif selection_detail == "farewells":
                farewell_options = []
                for dialogue_name in dialogue_list:
                    farewell_options.append((dialogue_db[dialogue_name].name, dialogue_name))
                if len(dialogue_list) > 3:
                    farewell_options = random.sample(farewell_options, k=3)
                farewell_options.append(("No importa", "return"))
                selected_dialogue = renpy.display_menu(farewell_options)
            
            
            
            
            if selected_dialogue != "return":
                print_debug("calling: " + selected_dialogue)
                renpy.call(selected_dialogue)
            
            
            
            
            if selection_detail == "idles" or selection_detail == "hdy":
                persistent.current_yuriidle = 0
            loop_again = True
            return
        else:
            print_debug(selection_method)
            y("Método de elección no encontrado")
            return






    def update_memory(memory_name, memory = ""):
        
        if memory_name in persistent.dialogue_memory:
            if memory != "":
                if persistent.dialogue_memory[memory_name] == [""]:
                    persistent.dialogue_memory[memory_name] = [memory]
                else:
                    persistent.dialogue_memory[memory_name].append(memory)
        else:
            persistent.dialogue_memory[memory_name] = [memory]

    def remove_memory(memory_name, memory = ""):
        if memory_name in persistent.dialogue_memory:
            
            if memory == "":
                persistent.dialogue_memory.pop(memory_name, None)
            
            elif memory in persistent.dialogue_memory[memory_name]:
                persistent.dialogue_memory[memory_name].remove(memory)


    def check_memory(memory_name, memory = ""):
        if memory_name in persistent.dialogue_memory:
            if memory == "":
                return True
            elif memory in persistent.dialogue_memory[memory_name]:
                return True
            else:
                return False
        else:
            return False

    def return_memory(memory_name):
        if memory_name in persistent.dialogue_memory:
            return persistent.dialogue_memory[memory_name]
        else:
            print_error(memory_name + " no se encuentra en persistent.dialogue_memory. No se pudo devolver la memoria.")

    def reset_memory():
        persistent.dialogue_memory = {}
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
