import json
import shutil
from PIL import Image
from pathlib import Path
from datetime import datetime

settings_file = open("settings.json","r").read()
settings = json.loads(settings_file)

base_folder = Path(__file__).parent.absolute()
root_folder = Path(Path.joinpath(base_folder,settings['folders']['root']))
pc_folder = Path(Path.joinpath(root_folder,settings['folders']['pc']))
phone_folder = Path(Path.joinpath(root_folder,settings['folders']['phone']))
other_folder = Path(Path.joinpath(root_folder,settings['folders']['other']))

if not root_folder.exists():
    print("[",datetime.now(),"]",root_folder,"does not exist. Creating now...")
    root_folder.mkdir()
if not pc_folder.exists():
    print("[",datetime.now(),"]",pc_folder,"does not exist. Creating now...")
    pc_folder.mkdir()
if not phone_folder.exists():
    print("[",datetime.now(),"]",phone_folder,"does not exist. Creating now...")
    phone_folder.mkdir()
if not other_folder.exists():
    print("[",datetime.now(),"]",other_folder,"does not exist. Creating now...")
    other_folder.mkdir()

start_time = datetime.timestamp(datetime.now())

wallpapers = list(root_folder.glob("*.jpg"))
wallpapers.extend(root_folder.glob("*.jpeg"))
wallpapers.extend(root_folder.glob("*.png"))

for wallpaper in wallpapers:
    wallpaper = str(wallpaper)
    img = Image.open(wallpaper)
    if img.size[0] < img.size[1]:
        print("[",datetime.now(),"]","Moving",wallpaper,"to Phone")
        shutil.move(wallpaper,str(phone_folder))
    elif img.size[0] > img.size[1]:
        print("[",datetime.now(),"]","Moving",wallpaper,"to PC")
        shutil.move(wallpaper,str(pc_folder))
    else:
        print("[",datetime.now(),"]","Moving",wallpaper,"to Other")
        shutil.move(wallpaper,str(other_folder))

end_time = datetime.timestamp(datetime.now())
print("[",datetime.now(),"]","Done in",round(end_time - start_time,2),"seconds.")
