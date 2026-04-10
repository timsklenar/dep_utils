#%%
#  import pathlib
from pathlib import Path

class Dataset:
    "A Daily Erosion Project dataset object"
    _path=None
    
    def path_initialization(self,path_variable:str|Path|None=None,version_string:str|None=None):
        
        if path_variable is not None:
            if version_string==None:
                self.path=Path(path_variable)
            elif isinstance(version_string,str) or isinstance(version_string,Path):
                self.path=Path(f"{str(path_variable)}_{version_string}")
            else:
                raise TypeError(f"{self.__class__.__name__} version string not a string or None type")
        else:
            raise UnboundLocalError(f"{self.__class__.__name__} path_varibale not provided") 
            
              
        
    
    
    def __init__(self,path_variable:str|Path|None=None,version_string=None):
        self.path_initialization(path_variable,version_string)
        
      
class BaseData(Dataset):
    _path='Basedata_Summaries'
    def __init__(self,version_string=None):
        super().__init__(self._path,version_string)
        # super().path_initialization(self._path,version_string)
  
class OtherManagements(Dataset):
    # _base_dir=
    _path='Man_Data_Other'
    def __init__(self,version_string=None):
        super().__init__(self._path,version_string)
        # super().path_initialization(self._path,version_string)

class ACPF(Dataset):
    # _base_dir=
    _path='Man_Data_ACPF\\dep_ACPF'
    # _year=
    def __init__(self,version_string=None):
        super().__init__(self._path,version_string)
        # super().path_initialization(self._path,version_string)
#%%