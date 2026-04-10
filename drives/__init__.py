# import pathlib
from pathlib import Path
import platform
import json
from ..defaults import Defaults
# """computer name"""
# current_computer=platform.node()
# # Get the directory of the current script
# base_dir = Path(__file__).parent.parent

# # Access a file in a 'data' folder next to the script
# drive_file = base_dir / ".dep_config" / "dep_computer_drive_defaults.json"

# # # Access a file one level up from the script
# # parent_file = base_dir.parent / "config.json"

# # with data_file.open() as f:
# #     print(f.read())
# # Path("dep_config/dep_defaults.json")
# """loading default config jsons to populate intial class attribute values"""
# with drive_file.open() as defaults:
#     raw_defaults_dict=json.load(defaults)
# drive_defaults_dict={}

# for computer,users in raw_defaults_dict.items():
#     drive_defaults_dict[computer]={}
#     for user,drive in users.items():
#         drive_defaults_dict[computer][user]=Path(drive)

# del computer,users,user,drive

# class Defaults:
#     _user_drives_dict=drive_defaults_dict
   
class Drives:
    _user_drives_dict=Defaults._user_drives_dict 
    _drives=_user_drives_dict
    # drives=_drives# class Drives:
        
    # def default(self):
    #     return self._default_dict
    def __init__(self, drives: dict|None=None):
        if drives == None:
            self.drives=self._drives
        elif isinstance(drives,dict):
            self.drives=drives
        else:
            raise ValueError("Defaults.drives only accepts dict or None types")
    # def __str__(self):
    #     return self._drives
    @property
    def drives(self):
        return self._drives
    
    @drives.setter
    def drives(self,drives):
        if not isinstance(drives,dict):
            raise TypeError("Defaults.drives object not a dict type.  Should be compname:username:Path object")
        self._drives= drives
