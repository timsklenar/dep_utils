#%%
"""A module for the Daily Erosion Project to consolidate file structures, naming conventions and 
make it easier to run the same scripts on different machines.  This top level module consolidates submodules
into one interface, populates classes with relevant attributes and is structured so that the user can call the default
value through Class().value or instantiate their own values through my_value = Class(needed,variables,go,here).
The ideas behind this way of doing it is that the user can write scripts with the default values 
(pulled from the config files) in mind, but during testing can instantiate objects with different attribute 
values or even set them directly (e.g. Class.value = "something" or Class._value = "whatever). 
This allows maximum flexibility once the user is done testing the structure, as they can change either 
a local copy of config files and include the dep_utils folder and the modified files packaged up with the 
script they're working on (changing only the behavior of that script) or they can change the values in the main config file 
(changing the behavior across all scripts using the DEP default config files).  To get the maximum benefit of 
intellisense type IDE features, put the dep_utils package folder in the site-packages folder of the environement you're
using (usually lives somewhere like C:\Users\{username}\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\Lib\site-packages)"""

# import pathlib
from pathlib import Path
# import platform
# import os
from os.path import join as opj
# import json
# import datetime
# import arcpy
# import sys
# import traceback
# import logging
from .drives import Drives
from .basic_parameters import BasicParameters
from .user import User
from .defaults import Defaults


#A bunch of nested classes allow storage of the DEP computer/user information in one place
class Cylo:
    # "data storage server managed by Ryan McGeehee"
    class Main:
        "main DEP data repository, read only except for managers (bkgelder)"
        path=Path("\\\\abe-cylo\\dep")
    class Dev:
        "DEP development directory, read and write enabled for DEP team members"
        path=Path("\\\\abe-cylo\\depdev")
    #this dynamically pulls the isu username of the current user by findinng their default user folder name
    class Personal:
        "your personal cylo directory, go nuts!"
        _path=Path(f"\\\\abe-cylo\\Cylo-{User.name}")
        path=_path
        def __init__(self,username:str|None=None):
            if username == None:
                self.path=Path(f"\\\\abe-cylo\\Cylo-{User.name}")
            else:
                self.path=Path(f"\\\\abe-cylo\\Cylo-{username}")
class Computers:
    class Remote:
        "DEP servers and such"
        class Cylo(Cylo):
           "data storage server managed by Ryan McGeehee" 
        
    
    class Local:
        "the machine currently running this code"
        name=User._current_computer
        user_directory_path=User.path
        username=User.name
        processing_drive_path=User().drive


class Dataset:
    "Daily Erosion Project datasets"
    def PathInitialization(self,path_variable,version_string=None):
        if version_string==None:
            self.path=Path(path_variable)
            
        elif isinstance(version_string,str):
            self.path=Path(f"{path_variable}_{version_string}")
            
        else:
            raise TypeError(f"{self.__class__.__name__} version_string not a string")      
        
        
class BaseData(Dataset):
    _path='Basedata_Summaries'
    def __init__(self,version_string=None):
        super().PathInitialization(self._path,version_string)
  
class OtherManagements(Dataset):
    # _base_dir=
    _path='Man_Data_Other'
    def __init__(self,version_string=None):
        super().PathInitialization(self._path,version_string)

class ACPF(Dataset):
    # _base_dir=
    _path='Man_Data_ACPF\\dep_ACPF'
    # _year=
    def __init__(self,version_string=None):
        super().PathInitialization(self._path,version_string)

class Management:
    _acpf='Man_Data_ACPF\\dep_ACPF'
    _other='Man_Data_Other'
    def __init__(self,version_string=None):
        if version_string==None:
            self.acpf=self._acpf
            self.other=self._other
        elif isinstance(version_string,str):
            self.acpf=f"{version_string}\\{self._acpf}"
            self.other=f"{version_string}\\{self._other}"
        else:
            raise TypeError("Management version_string not a string")
    
   
class DEP:
    "a big ol' meta class to bring all the other classes into one spot"
    processing_directory=User.drive/"DEP_Proc"
    class BasicParameters(BasicParameters):
        "Basic parameters used in the DEP including huc12 lists from different years and Default values for configuration"
        class Defaults(Defaults):
            "Default values for DEP parameters"
    class Computers(Computers):
        "All the DEP computers in one"
    class Drives(Drives):
        "The default processing drives for users by computer"
    class User(User):
        "Paths and info for the current user on current computer" 
    # class Dataset(Dataset):
    #     "Paths to datasets"
    #     class BaseData(BaseData):
            # class Midwest(Midwest):
            #     class HUC12(Midwest):
            #         def __init__(self, year: int | None = None,versioning_string: str | None=None):
            #             super().__init__(year)
            #             self.path=Path(BaseData().path)/self.HUC12

    # class Tools(Tools):
        # "Daily Erosion Project custom functions"  
    # class 
    # current_user=cylo_dict["username"]

    
#%%
