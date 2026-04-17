#%%
#  import pathlib
from pathlib import Path
from basic_parameters import BasicParameters
import inspect
from paths_library.computers import Cylo
from defaults import Defaults
# from ...paths_library import path_initialization

class Dataset:
    "A Daily Erosion Project basic dataset path object with path_initialization method to make the path object and to add a verson string after an underscore. Used as a base class for specific dataset paths (acpf, basedata, etc), but can be used to make any string into a path object. Best not to use spaces for the version string"
   
    _path=None
    # def path_inititalization(path_initializatio):
    def path_initialization(self,dir_path:str|Path|None=None,version_string:str|None=None):
        
        if dir_path is not None and isinstance(dir_path,str|Path):
            if version_string==None:
                self.path=Path(dir_path)
            elif isinstance(version_string,str|Path):
                self.path=Path(f"{str(dir_path)}_{version_string}")
            else:
                raise TypeError(f"{self.__class__.__name__} version string not a string or None type")
        else:
            raise TypeError(f"{self.__class__.__name__} path_varibale not provided or not string or pathlib.Path type") 
            
    # The default Dataset._path value is set to None and the path initialization will throw an error if no directory path is 
    # declared. Doing it this way makes a newly instantiated Dataset object throw an error if a vaule for directory
    # path isn't declared, but for the child classes of specific dataset objects (ACPF, other man data, basedata, etc)
    # they all have their own default _drive_path, _folder_path, and _path varibles. When collected into the Datasets object 
    # below, _drive_path is set to the Cylo folder containing the data.  This can be changed directly by manipulating the 
    # ._path (changing the default path value for all ACPF objects for instance) and then calling Class().path
    # or for a single object by instantiating an object with a declared dir_path variable, for example:
    # my_acpf=ACPF("c:\my\\acpf\\folder") and then accessing the my_acpf.path attribute
    def __init__(self,dir_path:str|Path|None=None,version_string=None):
        if dir_path==None:
            dir_path=self._path
        self.path_initialization(dir_path,version_string)
        
      
class BaseData(Dataset):
    _drive_path=Path("")
    _folder_path=Path('Basedata_Summaries')
    _path=_drive_path/_folder_path

    def __init__(self, dir_path: str | Path | None = None, version_string=None):
        super().__init__(dir_path, version_string)
        self.counties_5070=self.path/'Basedata_5070.gdb'/'MW_Counties_PCS'
    # def __init__(self,version_string=None):
    #     super().__init__(self._path,version_string)
    #     # super().path_initialization(self._path,version_string)
    # "mwCounties5070" : opj(basedataDir, 'Basedata_5070.gdb','MW_Counties_PCS'),
    # "mwStates5070" : opj(basedataDir, 'Basedata_5070.gdb','MW_States'),
    # "main_wesm" : opj(basedataDir, 'WESM.gpkg','main.wesm'),
  
class OtherManagements(Dataset):
    # _base_dir=
    _drive_path=Path("")
    _folder_path=Path('Man_Data_Other')
    _path=_drive_path/_folder_path
    
    # def __init__(self,version_string=None):
    #     super().__init__(self._path,version_string)
    #     # super().path_initialization(self._path,version_string)

class ACPF(Dataset):
    # _base_dir=
    _drive_path=Path("")
    _folder_path=Path("Man_Data_ACPF")
    _year=str(Defaults._acpf_year)
    _acpf_year_folder=Path(f"dep_ACPF{_year}")
    _path=_drive_path/_folder_path/_acpf_year_folder
    
    
    def __init__(self, year:int|str|None=None, 
                 dir_path: str | Path | None = None, 
                 version_string:str|None=None):
        
        print(self._year)
        print(year)

        if year == None:
            self.year=self._year
        elif not isinstance(year,int|str):
            raise TypeError(f"{self.__class__.__name__} year not string or int type") 
        else:
            self.year=year
        
        print(self.year)
        print(year)

        self.acpf_year_folder=Path(f"dep_ACPF{self.year}")
        
        print(self.acpf_year_folder)
        if dir_path == None:
            dir_path=self._path
        elif not isinstance(dir_path,str|Path):
            raise TypeError(f"{self.__class__.__name__} dir_path not string or pathlib.Path type") 
        else: 
            dir_path=Path(dir_path)/self.acpf_year_folder
        if not (version_string,str):
            raise TypeError(f"{self.__class__.__name__} version_string not string or None type") 
        # self.path=self.path/self.acpf_year_folder
        super().__init__(dir_path, version_string)
        
        self.huc8_fields=self.path/"fields_by_huc8.gdb"

    #     self.
    #         basicDict = {
    # "depBase" : depBase,
    # "acpfBase" : acpfBase,
    # "acpfStart" : acpfStart,
    # "basedataDir" : basedataDir,
    # "otherBase" : otherBase,
    

    # "mwCounties5070" : opj(basedataDir, 'Basedata_5070.gdb','MW_Counties_PCS'),
    # "mwStates5070" : opj(basedataDir, 'Basedata_5070.gdb','MW_States'),
    # "main_wesm" : opj(basedataDir, 'WESM.gpkg','main.wesm'),
    #     # huc_8_fields gdb
    # "huc8_fields" : opj(acpfBase, 'fields_by_huc8.gdb')
    # }

    
    # _year=
    # def __init__(self,version_string=None):
    #     super().__init__(self._path,version_string)
    #     # super().path_initialization(self._path,version_string)
class Datasets:
    "instantiating Datasets(path/to/somewhere) sets the ._path default of the contained datasets to the path provided "
    _drive_path=Cylo.Main.path
    class ACPF(ACPF):
        "acpf filepath piece"
    class BaseData(BaseData):
        "basedata filepath piece"
    class OtherManagements(OtherManagements):
        "other management filepath piece"

    def set_default_dataset_path(self,drive_path: str|Path|None=None):
            
            if isinstance(drive_path,Path) or isinstance(drive_path,str):
                for name, cls in inspect.getmembers(self):
                        if inspect.isclass(cls) and issubclass(cls,Dataset):
                            cls._path=drive_path/cls._path
            else:
                raise TypeError(f"{self.__class__.__name__} drive_path must be string, pathlib.Path or None type (for default Cylo path)")  
    
    # def init_dataset_paths(self,drive_path: str|Path|None=None):
            
    #         if isinstance(drive_path,Path) or isinstance(drive_path,str):
    #             for name, cls in inspect.getmembers(self):
    #                     if inspect.isclass(cls) and issubclass(cls,Dataset):
    #                         cls._path=drive_path/cls._path
    #         else:
    #             raise TypeError(f"{self.__class__.__name__} drive_path must be string, pathlib.Path or None type (for default Cylo path)")  

    def __init__(self,drive_path: str|Path|None=None):
            if drive_path == None:
                drive_path=self._drive_path
            elif not isinstance(drive_path,str|Path):
                raise TypeError(f"{self.__class__.__name__} drive_path must be string, pathlib.Path or None type (for default Cylo path)")  
            else:
                self.drive_path=drive_path
                print(self.drive_path)
            self.set_default_dataset_path(drive_path)
   
#%%