#%%
# """A module for the Daily Erosion Project to consolidate file structures, naming conventions and 
# make it easier to run the same scripts on different machines.  This top level module consolidates submodules
# into one interface, populates classes with relevant attributes and is structured so that the user can call the default
# value through Class().value or instantiate their own values through my_value = Class(needed,variables,go,here).
# The ideas behind this way of doing it is that the user can write scripts with the default values 
# (pulled from the config files) in mind, but during testing can instantiate objects with different attribute 
# values or even set them directly (e.g. Class.value = "something" or Class._value = "whatever). 
# This allows maximum flexibility once the user is done testing the structure, as they can change either 
# a local copy of config files and include the dep_utils folder and the modified files packaged up with the 
# script they're working on (changing only the behavior of that script) or they can change the values in the main config file 
# (changing the behavior across all scripts using the DEP default config files).  To get the maximum benefit of 
# intellisense type IDE features, put the dep_utils package folder in the site-packages folder of the environement you're
# using (usually lives somewhere like C:\Users\{username}\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\Lib\site-packages)"""

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

from basic_parameters import BasicParameters
from defaults import Defaults
from paths_library import PathLibrary
from paths_library.drives import Drives
from paths_library.user import User
from paths_library.computers import Computers
from paths_library.datasets import Datasets,Dataset
from tools_library import ToolsLibrary
import inspect

BasicParameters()
Defaults()
PathLibrary()
Drives()
User()
Computers()
# Datasets()


# class Management:
#     _acpf='Man_Data_ACPF\\dep_ACPF'
#     _other='Man_Data_Other'
#     def __init__(self,version_string=None):
#         if version_string==None:
#             self.acpf=self._acpf
#             self.other=self._other
#         elif isinstance(version_string,str):
#             self.acpf=f"{version_string}\\{self._acpf}"
#             self.other=f"{version_string}\\{self._other}"
#         else:
#             raise TypeError("Management version_string not a string")
# class Datasets(Datasets):
#         "Paths to datasets"
#         def __init__(self):
#             for name, cls in inspect.getmembers(self):
#                 cls.path=    

def append_version_string(pathlike:str|Path|None=None,version_string:str|None=None):
    "converts a paths to strings, combines with version_string and turns back into a path"
    if version_string==None:
            version_string=""
    elif not isinstance(version_string,str):
        raise TypeError(f"version_string type must be str (to append to end of DEP path) or None (to use default DEP path)") 
    if isinstance(pathlike,Path):
        pathlike=str(pathlike)
    elif not isinstance(pathlike,str):
        raise TypeError(f"pathlike type must be str or path")
    
    
    return Path(f"{pathlike}{version_string}")


class DEP:
    "a big ol' meta class to bring all the other classes into one spot"
    _processing_directory=User.drive/Defaults._processing_dir
    _directory=User.drive/Defaults._DEP_dir

    def __init__(self,version_string:str|None=None):
        # if version_string == None:

        #     self.path=Path(f"{str(self._base)}")
        #     self.proc=P
           
        self.path=append_version_string(pathlike=self._directory,version_string=version_string)#Path(f"{str(self._base)}{version_string}")
        self.proc=append_version_string(pathlike=self._processing_directory,version_string=version_string)
    class ToolsLibrary(ToolsLibrary):
        "DEP tools"
    class BasicParameters(BasicParameters):
        "Basic parameters used in the DEP including huc12 lists from different years and Default values for configuration"
        class Defaults(Defaults):
            "Default values for DEP parameters"
    class PathLibrary(PathLibrary):
        "Library of all the DEP paths and methods associated"
        
    
    # class Computers(Computers):
    #     "All the DEP computers in one"
    # class Drives(Drives):
    #     "The default processing drives for the current user for each DEP computer"
    # class User(User):
    #     "Paths and info for the current user on current computer" 
    # class Datasets(Datasets):
    #     "Paths to datasets"
    # class Dataset(Dataset):
    #     "A Daily Erosion Project basic dataset path object with path_initialization method to make the path object "
    #     "and to add a verson string after an underscore. Used as a base class for specific dataset paths (acpf, basedata, etc),"
    #     "but can be used to make any string into a path object. Best not to use spaces for the version string"
        
        # class BaseData(BaseData):
        #     class Midwest(Midwest):
        #         class HUC12(Midwest):
        #             def __init__(self, year: int | None = None,versioning_string: str | None=None):
        #                 super().__init__(year)
        #                 self.path=Path(BaseData().path)/self.HUC12
         
    # class Tools(Tools):
        # "Daily Erosion Project custom functions"  
    # class 
    # current_user=cylo_dict["username"]

    
#%%
