from pathlib import Path

base_folder = Path(__file__).parent.absolute()
root_folder = Path(Path.joinpath(base_folder,"test_data"))
pc_folder = Path(Path.joinpath(base_folder,"test_data/PC"))
phone_folder = Path(Path.joinpath(base_folder,"test_data/Phone"))
other_folder = Path(Path.joinpath(base_folder,"test_data/Other"))

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
