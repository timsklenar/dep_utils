import platform
from pathlib import Path
import json
"""computer name"""
current_computer=platform.node()
# Get the directory of the current script
base_dir = Path(__file__).parent.parent

# Access a file in a 'data' folder next to the script
drive_file = base_dir / ".dep_config" / "dep_computer_drive_defaults.json"

# # Access a file one level up from the script
# parent_file = base_dir.parent / "config.json"

# with data_file.open() as f:
#     print(f.read())
# Path("dep_config/dep_defaults.json")
"""loading default config jsons to populate intial class attribute values"""
with drive_file.open() as defaults:
    raw_defaults_dict=json.load(defaults)
drive_defaults_dict={}

for computer,users in raw_defaults_dict.items():
    drive_defaults_dict[computer]={}
    for user,drive in users.items():
        drive_defaults_dict[computer][user]=Path(drive)

del computer,users,user,drive

class Defaults:
    _user_drives_dict=drive_defaults_dict
    _acpf_year=2023
    _processing_dir="DEP_Proc"
    _DEP_dir="DEP"
    