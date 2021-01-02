from pathlib import Path
from PIL import Image

base_folder = Path(__file__).parent.absolute()
root_folder = Path(Path.joinpath(base_folder,"test_data"))
pc_folder = Path(Path.joinpath(root_folder,"PC"))
phone_folder = Path(Path.joinpath(root_folder,"Phone"))
other_folder = Path(Path.joinpath(root_folder,"Other"))

if not root_folder.exists():
    root_folder.mkdir()
if not pc_folder.exists():
    pc_folder.mkdir()
if not phone_folder.exists():
    phone_folder.mkdir()
if not other_folder.exists():
    other_folder.mkdir()

wallpapers = list(root_folder.glob("*.jpg"))
wallpapers.extend(root_folder.glob("*.jpeg"))
wallpapers.extend(root_folder.glob("*.png"))

for wallpaper in wallpapers:
    img = Image.open(wallpaper)
    if img.size[0] < img.size[1]:
        print(wallpaper,"|","Phone")
    elif img.size[0] > img.size[1]:
        print(wallpaper,"|","PC")
    else:
        print(wallpaper,"|","Other")
