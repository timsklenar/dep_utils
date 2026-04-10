import platform
from pathlib import Path
import json
from defaults import Defaults
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
    
class User:
    _current_computer=platform.node()
    _path=Path.home()
    _name = _path.name
    _drive=Defaults._user_drives_dict[_current_computer][_name]
    path=_path
    name=_name
    drive=_drive
    def __init__(self,username:str|None=None,user_directory:Path|str|None=None,processing_drive:Path|str|None=None):
        if (username == None)&(user_directory == None)&(processing_drive == None):
            # print("Using default info")
            self.drive = self._drive
            self.name = self._name
            self.path = self._path
        else:# (username != None)|(user_directory != None)|(processing_drive != None):
            if processing_drive != None:
                if isinstance(processing_drive,Path):
                    self.drive=processing_drive
                else:
                    self.drive = Path(processing_drive)
            if username != None:
                self.name = username
            if user_directory != None:
                if isinstance(user_directory,Path):
                    self.path=user_directory
                else:
                    self.path = Path(user_directory)
        # else:
        #     raise TypeError("You must declare all attributes for DEP User objects or leave them all blank to use defaults")
    
        def __str__(self):
            return self.name
    
    # @property
    # def default(self):
    #     return self._default_dict
    
    # @property
    # def results(self):
    #     return self._results
    # @results.setter
    # def results(self,results):
    #     if not isinstance(results,dict):
    #         raise TypeError("UserDrive object not a dict type.  Should be compname:username:Path object")
    #     self._results = results
  