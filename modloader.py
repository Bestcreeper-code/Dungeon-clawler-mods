<<<<<<< HEAD
import shutil
import os
import tkinter as tk
from tkinter.filedialog import askdirectory
import json

tk.Tk().withdraw()

Mod_folder = ""
Game_Data_Folder = "C:/Program Files (x86)/Steam/steamapps/comemon/Dungeon Clawler/Windows/DungeonClawler_Data"
script_dir = os.path.dirname(os.path.abspath(__file__))
config_file = script_dir + "config.json"

print("\033[7m\033[33mHello and welcome to the First Dungeon Clawler mod loader\033[0mn\n\n")

def save_paths(mod_folder, game_data_folder):
    config = {
        "mod_folder": mod_folder,
        "game_data_folder": game_data_folder
    }
    with open(config_file, "w") as f:
        json.dump(config, f)

def load_paths():
    global Mod_folder, Game_Data_Folder
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            config = json.load(f)
            Mod_folder = config.get("mod_folder", "")
            Game_Data_Folder = config.get("game_data_folder", "")

def copy_and_replace(source_path, destination_path):
    if os.path.exists(destination_path):
        os.remove(destination_path)
    shutil.copy2(source_path, destination_path)
    print("done")

def setup():
    global Mod_folder, Game_Data_Folder
    while not os.path.exists(Game_Data_Folder):
        print("\033[31mDungeonClawler_Data folder not found\033[0m\n")
        print("Select your DungeonClawler_Data folder\n")
        fn = askdirectory()
        while fn == "":
            fn = askdirectory()
        print("Game Data Folder:", fn)
        Game_Data_Folder = fn
    print("\033[32mDungeonClawler_Data folder found\033[0m")
    save_paths(Mod_folder, Game_Data_Folder)
    print("Select your mod file\n")
    fn = ""
    fn = askdirectory()
    while fn == "":
        fn = askdirectory()
    Mod_folder = fn
    print("Mod File:", fn)
    
    save_paths(Mod_folder, Game_Data_Folder)
    selector(Game_Data_Folder,Mod_folder)

def selector(Game_Data_Folder,Mod_folder):
    while True:
        print("Mods:")
        print("\033[44m\033[37m",os.listdir(Mod_folder),"\033[0m")
        selected_mod = input("\033[33mchoose a mod\nor\ntype 'settings' to change the folders\n\033[0m")
        if selected_mod == "settings":
            setup()
            break
        selected_mod = Mod_folder + "/" + selected_mod + "/sharedassets0.assets"
        print(selected_mod)
        copy_and_replace(selected_mod, (Game_Data_Folder + "/sharedassets0.assets"))

load_paths()

if Mod_folder == "":
    setup()
else:
    selector(Game_Data_Folder,Mod_folder)
=======
import shutil
import os
import tkinter as tk
from tkinter.filedialog import askdirectory
import json

tk.Tk().withdraw()

Mod_folder = ""
Game_Data_Folder = "C:/Program Files (x86)/Steam/steamapps/comemon/Dungeon Clawler/Windows/DungeonClawler_Data"
script_dir = os.path.dirname(os.path.abspath(__file__))
config_file = script_dir + "config.json"

print("\033[7m\033[33mHello and welcome to the First Dungeon Clawler mod loader\033[0mn\n\n")

def save_paths(mod_folder, game_data_folder):
    config = {
        "mod_folder": mod_folder,
        "game_data_folder": game_data_folder
    }
    with open(config_file, "w") as f:
        json.dump(config, f)

def load_paths():
    global Mod_folder, Game_Data_Folder
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            config = json.load(f)
            Mod_folder = config.get("mod_folder", "")
            Game_Data_Folder = config.get("game_data_folder", "")

def copy_and_replace(source_path, destination_path):
    if os.path.exists(destination_path):
        os.remove(destination_path)
    shutil.copy2(source_path, destination_path)
    print("done")

def setup():
    global Mod_folder, Game_Data_Folder
    while not os.path.exists(Game_Data_Folder):
        print("\033[31mDungeonClawler_Data folder not found\033[0m\n")
        print("Select your DungeonClawler_Data folder\n")
        fn = askdirectory()
        while fn == "":
            fn = askdirectory()
        print("Game Data Folder:", fn)
        Game_Data_Folder = fn
    print("\033[32mDungeonClawler_Data folder found\033[0m")
    save_paths(Mod_folder, Game_Data_Folder)
    print("Select your mod file\n")
    fn = ""
    fn = askdirectory()
    while fn == "":
        fn = askdirectory()
    Mod_folder = fn
    print("Mod File:", fn)
    
    save_paths(Mod_folder, Game_Data_Folder)
    selector(Game_Data_Folder,Mod_folder)

def selector(Game_Data_Folder,Mod_folder):
    while True:
        print("Mods:")
        print("\033[44m\033[37m",os.listdir(Mod_folder),"\033[0m")
        selected_mod = input("\033[33mchoose a mod\nor\ntype 'settings' to change the folders\n\033[0m")
        if selected_mod == "settings":
            setup()
            break
        selected_mod = Mod_folder + "/" + selected_mod + "/sharedassets0.assets"
        print(selected_mod)
        copy_and_replace(selected_mod, (Game_Data_Folder + "/sharedassets0.assets"))

load_paths()

if Mod_folder == "":
    setup()
else:
    selector(Game_Data_Folder,Mod_folder)
>>>>>>> 1767c8b10bccbb2d31cc4f97c0f7f0c16e896dcc
