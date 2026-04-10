#%%
from pathlib import Path
from .user import User
from .drives import Drives
from .computers import Computers
from .datasets import Datasets,Dataset,BaseData,ACPF,OtherManagements
# from .path_initialization import path_initialization


class PathLibrary:
    class Datasets(Datasets):
        "DEP dataset paths"
    class Computers(Computers):
        "All the DEP computers in one"
    class User(User):
        "Paths and info for the current user on current computer"
    class Drives(Drives):
        "The default processing drives for the current user for each DEP computer"

#%%