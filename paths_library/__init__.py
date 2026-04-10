from .user import User
from .drives import Drives
from .computers import Computers
from .datasets import Dataset,BaseData,ACPF,OtherManagements

class PathLibrary:
    class Dataset(Dataset):
        
    class Computers(Computers):
        "All the DEP computers in one"
    class User(User):
        "Paths and info for the current user on current computer"
    class Drives(Drives):
        "The default processing drives for the current user for each DEP computer"

