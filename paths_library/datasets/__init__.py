#%%
#  import pathlib
from pathlib import Path
from basic_parameters import BasicParameters
import inspect
from paths_library.computers import Cylo
from defaults import Defaults
from defaults import turn_warnings_on,turn_warnings_off
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
    _warnings_flag=True

    from defaults import turn_warnings_off as turn_warnings_off
    from defaults import turn_warnings_on as turn_warnings_on

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
    _warnings_flag=True

    from defaults import turn_warnings_off as turn_warnings_off
    from defaults import turn_warnings_on as turn_warnings_on

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
    _warnings_flag=True

    from defaults import turn_warnings_off as turn_warnings_off
    from defaults import turn_warnings_on as turn_warnings_on

    
    def __init__(self, year:int|str|None=None, 
                 dir_path: str | Path | None = None, 
                 version_string:str|None=None):
        
        
        if year == None:
            self.year=self._year
        elif not isinstance(year,int|str):
            raise TypeError(f"{self.__class__.__name__} year not string or int type") 
        else:
            self.year=year
        

        self.acpf_year_folder=Path(f"dep_ACPF{self.year}")
        
        if self._warnings_flag==True:
            print(self.acpf_year_folder)
        
        if dir_path == None:
            dir_path=self._drive_path/self._folder_path/self.acpf_year_folder
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
    _init_flag=False
    _warnings_flag=True

    from defaults import turn_warnings_off as turn_warnings_off
    from defaults import turn_warnings_on as turn_warnings_on
    
    class ACPF(ACPF):
        "acpf filepath piece"
        def __init__(self, year: int | str | None = None, dir_path: str | Path | None = None, version_string: str | None = None):
            super().__init__(year, dir_path, version_string)
        # def __init__(self,drive_path: Path|str|None=None):
        #     if drive_path==None:
        #         dir_path=Datasets._drive_path/self._folder_path
        #     elif isinstance(drive_path,str|Path):
        #         dir_path=drive_path/self._folder_path
        #     else:
        #         raise TypeError((f"{self.__class__.__name__} drive_path must be string, pathlib.Path or None type (for default Cylo path)")  )
        #     super().__init__(dir_path=dir_path)
    class BaseData(BaseData):
        "basedata filepath piece"
        def __init__(self, dir_path: str | Path | None = None, version_string=None):
            super().__init__(dir_path, version_string)
    class OtherManagements(OtherManagements):
        "other management filepath piece"
        def __init__(self, dir_path: str | Path | None = None, version_string=None):
            super().__init__(dir_path, version_string)

    def set_default_dataset_drive(self,drive_path: str|Path|None=None,warning_flag:bool|None=None):
            # print(drive_path)
            if drive_path==None:
                self.drive_path=self._drive_path
            elif isinstance(drive_path,Path|str):
                self.drive_path=drive_path
            else:
                raise TypeError(f"{self.__class__.__name__} drive_path must be string, pathlib.Path or None type (for default Cylo path)")  
            if warning_flag==None:
                warning_flag=self._warnings_flag
            
            if warning_flag == True:
                print(f"Datasets drive set to {self.drive_path} as default. To change use Datasets().set_default_dataset_drive('path/to/somewhere')")
            ACPF._drive_path=Path(self.drive_path)
            OtherManagements._drive_path=Path(self.drive_path)
            BaseData._drive_path=Path(self.drive_path)
    
    # def init_dataset_paths(self,drive_path: str|Path|None=None):
            
    #         if isinstance(drive_path,Path) or isinstance(drive_path,str):
    #             for name, cls in inspect.getmembers(self):
    #                     if inspect.isclass(cls) and issubclass(cls,Dataset):
    #                         cls._path=drive_path/cls._path
    #         else:
    #             raise TypeError(f"{self.__class__.__name__} drive_path must be string, pathlib.Path or None type (for default Cylo path)")  

    def __init__(self,drive_path: str|Path|None=None,warning_flag:bool|None=None):
            if self._init_flag==False:
                if drive_path == None:
                    self.drive_path=self._drive_path
                elif not isinstance(drive_path,str|Path):
                    raise TypeError(f"{self.__class__.__name__} drive_path must be string, pathlib.Path or None type (for default Cylo path)")  
                else:
                    self.drive_path=drive_path
                if warning_flag==None:
                    warning_flag=self._warnings_flag
                elif not isinstance(warning_flag,bool):
                    raise TypeError(f"{self.__class__.__name__} warning_flag must be None type (for default) or boolean")  
                # print(self.drive_path)
                
                self.set_default_dataset_drive(self.drive_path,warning_flag=warning_flag)
                Datasets._init_flag=True
                # print(f"Datasets drive set to {self.drive_path} as default. To change use Datasets().set_default_dataset_drive('path/to/somewhere')")
            
#%%