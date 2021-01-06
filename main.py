import json
import shutil
from PIL import Image
from pathlib import Path
from datetime import datetime

base_folder = Path(__file__).parent.absolute()

settings_file = open(Path.joinpath(base_folder,"settings.json"),"r").read()
settings = json.loads(settings_file)

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

def moveFile(src,dest):
    src = str(src)
    dest = str(dest)
    print("[",datetime.now(),"]","Moving",src,"to",dest.split("/")[-1])
    try:
        shutil.move(src,dest)
    except shutil.Error as err:
        print("[",datetime.now(),"]","ERROR:",str(err)+".", "Skipping...")

for wallpaper in wallpapers:
    img = Image.open(wallpaper)
    if img.size[0] < img.size[1]:
        moveFile(wallpaper,phone_folder)
    elif img.size[0] > img.size[1]:
        moveFile(wallpaper,pc_folder)
    else:
        moveFile(wallpaper,other_folder)
        

end_time = datetime.timestamp(datetime.now())
print("[",datetime.now(),"]","Done in",round(end_time - start_time,2),"seconds.")
