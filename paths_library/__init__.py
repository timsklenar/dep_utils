#%%
from pathlib import Path
from defaults import Defaults
from .user import User
from .drives import Drives
from .computers import Computers
from .datasets import Datasets,Dataset,BaseData,ACPF,OtherManagements
# from .path_initialization import path_initialization


class PathLibrary:
    _processing_directory=User.drive/Defaults._processing_dir
    _dep_dir=User.drive/Defaults._DEP_dir

    class Datasets(Datasets):
        "DEP dataset paths"
    class Computers(Computers):
        "All the DEP computers in one"
    class User(User):
        "Paths and info for the current user on current computer"
    class Drives(Drives):
        "The default processing drives for the current user for each DEP computer"
    def __init__(self,processing_directory:str|Path|None=None,dep_directory:str|Path|None=None):
        if processing_directory==None:
            processing_directory=self._processing_directory
        elif not isinstance(processing_directory,str|Path):
            raise TypeError(f"{self.__class__.__name__} processing_directory must be str, Path or None type")
        if dep_directory == None:
            dep_directory=self._dep_dir
        elif not isinstance(dep_directory,str|Path):
            raise TypeError(f"{self.__class__.__name__} processing_directory must be str, Path or None type")
        self.Datasets()    
#%%