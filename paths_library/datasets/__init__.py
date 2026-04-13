#%%
#  import pathlib
from pathlib import Path
# from ...paths_library import path_initialization

class Dataset:
    "A Daily Erosion Project basic dataset path object with path_initialization method to make the path object and to add a verson string after an underscore. Used as a base class for specific dataset paths (acpf, basedata, etc), but can be used to make any string into a path object. Best not to use spaces for the version string"
   
    _path=None
    # def path_inititalization(path_initializatio):
    def path_initialization(self,path_variable:str|Path|None=None,version_string:str|None=None):
        
        if path_variable is not None and isinstance(path_variable,str|Path):
            if version_string==None:
                self.path=Path(path_variable)
            elif isinstance(version_string,str) or isinstance(version_string,Path):
                self.path=Path(f"{str(path_variable)}_{version_string}")
            else:
                raise TypeError(f"{self.__class__.__name__} version string not a string or None type")
        else:
            raise TypeError(f"{self.__class__.__name__} path_varibale not provided or not string or pathlib.Path type") 
            

    def __init__(self,path_variable:str|Path|None=None,version_string=None):
        if path_variable==None:
            path_variable=self._path
        self.path_initialization(path_variable,version_string)
        
      
class BaseData(Dataset):
    _path='Basedata_Summaries'
    # def __init__(self,version_string=None):
    #     super().__init__(self._path,version_string)
    #     # super().path_initialization(self._path,version_string)
  
class OtherManagements(Dataset):
    # _base_dir=
    _path='Man_Data_Other'
    # def __init__(self,version_string=None):
    #     super().__init__(self._path,version_string)
    #     # super().path_initialization(self._path,version_string)

class ACPF(Dataset):
    # _base_dir=
    _path='Man_Data_ACPF\\dep_ACPF'
    # _year=
    # def __init__(self,version_string=None):
    #     super().__init__(self._path,version_string)
    #     # super().path_initialization(self._path,version_string)
class Datasets:
    class ACPF(ACPF):
        "acpf filepath piece"
    class BaseData(BaseData):
        "basedata filepath piece"
    class OtherManagements(OtherManagements):
        "other management filepath piece"

#%%