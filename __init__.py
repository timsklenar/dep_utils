#%%
"""A module for the Daily Erosion Project to consolidate file structures, naming conventions and 
make it easier to run the same scripts on different machines.  First it will pull information 
from json formatted config files about what drives to use based on the active username and 
computer name, then populate classes with relavent attributes so that the user can call the default
value through Class().value or instantiate their own values through my_value = Class(needed,values,go,here).
The ideas behind this way of doing it is that the user can write scripts with the default values 
(pulled from the config files) in mind, but during testing can instantiate objects with different attribute 
values or even set them directly (e.g. Class.value = "something"). This allows maximum flexibility once the 
user is done testing the structure, as they can change either a local copy of config files and include the 
DEP_info.py and the modified files packaged up with the script (changing only the behavior of that script) 
or they can change the main config file (changing the behavior across all scripts using the DEP default
config files)."""

# import pathlib
from pathlib import Path
import platform
import os
from os.path import join as opj
import json
import datetime
import arcpy
import sys
import traceback
import logging
from .drives import Drives
from .basic_parameters import BasicParameters
from .user import User
from .defaults import Defaults
# """computer name"""
# current_computer=platform.node()
# # Get the directory of the current script
# base_dir = Path(__file__).parent

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
       

#%%

# class Drives:
#     _user_drives_dict=Defaults._user_drives_dict 
#     _drives=_user_drives_dict
#     # drives=_drives# class Drives:
        
#     # def default(self):
#     #     return self._default_dict
#     def __init__(self, drives: dict|None=None):
#         if drives == None:
#             self.drives=self._drives
#         elif isinstance(drives,dict):
#             self.drives=drives
#         else:
#             raise ValueError("Defaults.drives only accepts dict or None types")
#     # def __str__(self):
#     #     return self._drives
#     @property
#     def drives(self):
#         return self._drives
    
#     @drives.setter
#     def drives(self,drives):
#         if not isinstance(drives,dict):
#             raise TypeError("Defaults.drives object not a dict type.  Should be compname:username:Path object")
#         self._drives= drives

#%%

# class User:
#     _current_computer=platform.node()
#     _path=Path.home()
#     _name = _path.name
#     _drive=Defaults._user_drives_dict[_current_computer][_name]
#     path=_path
#     name=_name
#     drive=_drive
#     def __init__(self,username:str|None=None,user_directory:Path|str|None=None,processing_drive:Path|str|None=None):
#         if (username == None)&(user_directory == None)&(processing_drive == None):
#             # print("Using default info")
#             self.drive = self._drive
#             self.name = self._name
#             self.path = self._path
#         else:# (username != None)|(user_directory != None)|(processing_drive != None):
#             if processing_drive != None:
#                 if isinstance(processing_drive,Path):
#                     self.drive=processing_drive
#                 else:
#                     self.drive = Path(processing_drive)
#             if username != None:
#                 self.name = username
#             if user_directory != None:
#                 if isinstance(user_directory,Path):
#                     self.path=user_directory
#                 else:
#                     self.path = Path(user_directory)
#         # else:
#         #     raise TypeError("You must declare all attributes for DEP User objects or leave them all blank to use defaults")
    
#         def __str__(self):
#             return self.name
    
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
    
# class UserDrive:
#     _default_dict=defaults_dict
#     _computer_name=current_computer
#     _user_path=Path.home()
#     _username=User.name

#     def __init__(self,computer_name=None,username=None,drive_path=None):
#         if (computer_name == None)&(username == None)&(drive_path == None):
#             # print("Using default info")
#             self.computer = self._computer_name
#             self.username = self._username
#             self.path = self._default_dict[self._computer_name][self._username]
#         elif (computer_name != None)&(username != None)&(drive_path != None):
#             self.computer = computer_name
#             self.username = username
#             self.path = Path(drive_path)
#         else:
#             raise TypeError("You must declare all attributes for DEP UserDrive objects or leave them all blank to use defaults")
    
#     def __str__(self):
#         return self.path
    
#     # @property
#     # def default(self):
#     #     return self._default_dict
    
#     # @property
#     # def results(self):
#     #     return self._results
#     # @results.setter
#     # def results(self,results):
#     #     if not isinstance(results,dict):
#     #         raise TypeError("UserDrive object not a dict type.  Should be compname:username:Path object")
#     #     self._results = results


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



# logging.Logger.info


    # class ACPF:  
    #
    # 
# def PathInitialization(object,path_variable,version_string=None):
#     if version_string==None:
#         object.path=path_variable
        
#     elif isinstance(version_string,str):
#         object.path=f"{version_string}\\{path_variable}"
        
#     else:
#         raise TypeError(f"{object.__name__} version_string not a string")      
    
#     return object


class Dataset:
    "Daily Erosion Project datasets"
    def PathInitialization(self,path_variable,version_string=None):
        if version_string==None:
            self.path=Path(path_variable)
            
        elif isinstance(version_string,str):
            self.path=Path(f"{path_variable}_{version_string}")
            
        else:
            raise TypeError(f"{self.__class__.__name__} version_string not a string")      
        
        # return object
    # def PathInitialization(self,version_string=None):
    #     if version_string==None:
    #         self.path=self._path
            
    #     elif isinstance(version_string,str):
    #         self.path=f"{version_string}\\{self._path}"
            
    #     else:
    #         raise TypeError("BaseData version_string not a string")
        
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

# basicDict = {
# "depBase" : depBase,
# "acpfBase" : acpfBase,
# "acpfStart" : acpfStart,
# "basedataDir" : basedataDir,
# "otherBase" : otherBase,
# "mwHuc12s5070" : opj(basedataDir, 'Basedata_5070.gdb', MWHUC12_ACPF),
# "mwHuc8s5070" : opj(basedataDir, 'Basedata_5070.gdb', MWHUC8_ACPF),
# "mwHuc2s5070" : opj(basedataDir, 'Basedata_5070.gdb', MWHUC2_ACPF),

# "mwCounties5070" : opj(basedataDir, 'Basedata_5070.gdb','MW_Counties_PCS'),
# "mwStates5070" : opj(basedataDir, 'Basedata_5070.gdb','MW_States'),
# "main_wesm" : opj(basedataDir, 'WESM.gpkg','main.wesm'),
#     # huc_8_fields gdb
# "huc8_fields" : opj(acpfBase, 'fields_by_huc8.gdb')
# }

# class Midwest(BaseData):
    

        # if year == None:

       
    # elif int(ACPFyear) > 2022:
    #     MWHUC12_ACPF = 'MW_HUC12_v2023'
    #     MWHUC8_ACPF = 'MW_HUC8_v2023'
    #     MWHUC2_ACPF = 'MW_HUC2_v2022'
    # elif int(ACPFyear) > 2021:
    #     MWHUC12_ACPF = 'MW_HUC12_v2022'
    #     MWHUC8_ACPF = 'MW_HUC8_v2022'
    #     MWHUC2_ACPF = 'MW_HUC2_v2022'
    # elif int(ACPFyear) > 2018:
    #     MWHUC12_ACPF = 'MW_HUC12_v2019'
    #     MWHUC8_ACPF = 'MW_HUC8_v2019'
    #     MWHUC2_ACPF = 'MW_HUC2_v2019'
    # else:
    #     MWHUC12_ACPF = 'MW_HUC12_v2013'
    #     MWHUC8_ACPF = 'MW_HUC8_v2013'
    #     MWHUC2_ACPF = 'MW_HUC2_v2013'

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
    
        
# node, ACPFyear, huc12, outEPSG, interpType, cellSize, nowYmd, version = '' 

# class BasicParameters:
#     "static DEP data"
    
#     _year=int(datetime.date.today().year)
#     _HUC12 = f'MW_HUC12_v'
#     _HUC8 = f'MW_HUC8_v'
#     _HUC2= f'MW_HUC2_v'
#     def __init__(self,year: int|None=None):
#         if year==None:
#             self.year=self._year
#             self.HUC12=f"{self._HUC12}{self._year}"
#             self.HUC8=f"{self._HUC8}{self._year}"
#             self.HUC2=f"{self._HUC2}{self._year}"
        
#         else:
#             if year>2023:
#                 self.HUC12=f"{self._HUC12}{self._year}"
#                 self.HUC8=f"{self._HUC8}{self._year}"
#                 self.HUC2=f"{self._HUC2}{self._year}"
#             elif year==2023:
#                 self.HUC12=f"{self._HUC12}{year}"
#                 self.HUC8=f"{self._HUC8}{year}"
#                 self.HUC2=f"{self._HUC2}{year-1}"
#             elif year==2022:
#                 self.HUC12=f"{self._HUC12}2022"
#                 self.HUC8=f"{self._HUC8}2022"
#                 self.HUC2=f"{self._HUC2}2022"
#             elif 2021>=year>=2019:
#                 self.HUC12=f"{self._HUC12}2019"
#                 self.HUC8=f"{self._HUC8}2019"
#                 self.HUC2=f"{self._HUC2}2019"
#             else:
#                 self.HUC12=f"{self._HUC12}2013"
#                 self.HUC8=f"{self._HUC8}2013"
#                 self.HUC2=f"{self._HUC2}2013"
    
    
#     class DEM_method:
#         ZMEAN= 'mean18'
#         ZMINMAX= 'mnmx18'
#         ZMIN= 'min18'
#         ZMAX= 'max18'    

        
#     class Huc12s:
#         "lists of the huc12s for given years"
#         y2022 = ['051201130904', '051402020705', '050800020907', '071200030304', '071200030302', '071200011308', '040400010510', '040400010103', '040400010302', '040400010303', '040400010401', '040400010403', '040400010501', '040400010502', '040400010503', '040400010504', '040400010505', '040400010508', '071200011004', '071200011008', '040400010204', '040400010104', '040400010201', '040400010205', '071200010201', '071200030303', '071200030203', '071200030407', '071100090107', '102300030501', '040400010402', '071401010401', '071100090403', '071100090401', '071401010206', '102100100206', '102001011107', '102002020103', '102702010101', '102002020211', '102200031003', '040400010506', '071300111006', '102400010106', '051402060703', '040801010504', '040700030401', '041000100503', '080101000201', '040400010604', '040301140201', '040301140101', '040601040401', '040400020101', '040400010102', '040400010605', '040400010602', '040400010601', '040400010105', '040101010105', '042600000101', '040400010507', '041800000101', '041800000102', '090300010301', '040101010101', '040101010208', '040101010207', '040101011504', '040101010203', '040101011403', '040101010108', '040101010107', '040101011404', '040101011503', '040101011502', '040101010103', '040101010106', '040101011401', '040101010104', '040101011402', '040101010102', '040101011501', '040900020102', '040900020901', '040900020702', '040900020304', '040900010504', '040900020203', '040900020301', '040900020602', '040900020401', '040900020101', '040900020701', '040900010501', '040900040602', '040900040603', '040900040502', '040900040601', '040900040702', '040900040703', '040900040701', '040900021008', '040900021007', '040900021006', '040900021005', '040900040503', '040900040501', '040900020503', '040900021004', '040900021001', '040900020902', '040900020801', '040900021009', '040900020303', '040900020803', '040900020302', '040900020703', '040900021002', '040900020402', '040900020501', '040900020502', '040900020201', '040900020802', '040900021003', '040900020603', '040900020204', '040900020202', '040900020504', '040900020601', '041000130106', '041000130405', '041000130104', '041000130101', '041000130102', '041000130103', '041000130105', '041000130107', '041000130111', '041000130108', '041000130109', '041000130110', '041000130112', '041000130201', '041000130301', '041000130202', '041000130203', '041000130204', '041000130302', '041000130303', '041000130304', '041000130404', '041000130401', '041000130402', '041000130403', '041000130305', '041000130306', '041000130307', '041000130308', '041000130309', '041000130406', '041000130407', '041900000100', '040900010502', '101000042706', '101102050609', '101101010101', '101101012903', '042000021003', '042000021005', '042000021105', '042000021104', '042000021006', '042000021004', '042000021002', '042000021007', '042000021001', '042000021103', '042000021101', '042000021102', '042000020301', '042000020302', '042000020303', '042000020903', '042000020603', '042000020606', '042000020602', '042000020601', '042000020902', '042000020706', '042000020901', '042000020604', '042000020801', '042000020201', '042000020401', '042000020202', '042000020704', '042000020702', '042000020802', '042000020609', '042000020701', '042000020402', '042000020501', '042000020502', '042000020608', '042000020703', '042000020607', '042000020605', '040301020104', '040900010503', '042600000102', '041800000200', '042000020203', '042000020705', '042600000200', '051401010304', '101702040602', '070200080601', '090201060401', '090201060301', '103001010202', '103001010203', '051202070601', '080101000103', '080102010506', '102001030507', '102002020105', '102100090605', '102200040406', '102200010801', '102200030805', '102200031002', '102200031006', '101800091707', '101800140102', '070900021401', '071200060402', '050902030204', '040400010206', '042400020200', '101701040109', '101701040202', '101701040304', '101701040103', '101701040107', '101701040101', '101701040102', '101701040104', '101701040105', '101701040106', '101701040108', '101701040110', '101701040201', '101701040203', '101701040204', '101701040207', '101701040205', '101701040206', '101701040301', '101701040305', '101701040302', '101701040303', '071401010403', '071401010502', '041000010201', '041000010206', '040400010606', '071200011002', '040400010509', '071200030306', '040400010301', '041900000200', '090201030805']
#         y2019 = ['080203020101', '071100090201', '071100090301', '071402040501', '071402040506', '051201120204', '070200090301', '101702040504', '040400010603', '051201090801', '102300020301', '071200021201', '071200030104', '071200030107', '051201130901', '051201130902', '051201130903', '051201130904', '071200011308', '071200020703', '071402010206', '071200030304', '071200030305', '051402020705', '071300020104', '051201141004', '071300120401', '071000030403', '102400010106', '070600030704', '070700051804', '051402040501', '051402060507', '051402060508', '051402060509', '102500100303', '102500100304', '102500110303', '102500110304', '102500160804', '102701020906', '102701030510', '110100070804', '070400080904', '102300030501', '102801011707', '102801011708', '102801021404', '070300040403', '071000010502', '071000010801', '102802020410', '102901030205', '102901050204', '070102060903', '070300050404', '070400010209', '070102070401', '070400030601', '070400060502', '070600010504', '070102070602', '070200080503', '103001011204', '070102010101', '070102020504', '080103000101', '080103000102', '080103000103', '080103000104', '080103000201', '080103000202', '080103000203', '080103000204', '080103000301', '080103000302', '080103000303', '080103000304', '080103000305', '080103000306', '080103000307', '080103000308', '080103000309', '101900180606', '101800140808', '102500090701', '102500090703', '102500090901', '101900180703', '101900180705', '101900180706', '102001010901', '102001010902', '102001010903', '102001011004', '102001011005', '102001011101', '102001011102', '102500160301', '102500160303', '102001011106', '102001011107', '102001030206', '102002020101', '102002020103', '102702010101', '102002020211', '102702030401', '102702060101', '102702060301', '102702060901', '102100090503', '102200031003', '102200031005', '070700031401', '040301020102', '040301020103', '040301020105', '040301020106', '040301020107', '040301020108', '040301020109', '040301020110', '040301020201', '040301020204', '040301020205', '040301020305', '040301020401', '040301020403', '040301020404', '040301020405', '040301020406', '040301020407', '070400070701', '070500051205', '070500010904', '070500020704', '090203020104', '041800000200', '040103020109', '041800000100', '040103010504', '040103010503', '040103010601', '040103010602', '040103010603', '040103010607', '040103010608', '040103010705', '040103010806', '040103010807', '040103010901', '040103010902', '040103010903', '040103010904', '040103010906', '040103011002', '040103011003', '040103011004', '040103011008', '040103011101', '040103011105', '040103020703', '040103020705', '090300050302', '040101010802', '040102011604', '090300010302', '090300070501', '040102010602', '040101010401', '040101011301', '090300091423', '071402040504', '071402040505', '071402040502', '090203140101', '090203140102', '090203140103', '090203140104', '090203140105', '090203140106', '090203140107', '090203120606', '090203120601', '090203120502', '090203140408', '090203110702', '090203120602', '090203140604', '090203110701', '090203140504', '090203140603', '090203120501', '090203140508', '090203140606', '090203140607', '090203140409', '090203110803', '090203140407', '090203110703', '090203140808', '090203140405', '090203110804', '090203140801', '090203140507', '090203140608', '090203140809', '090203140602', '090203140406', '090203140806', '040400020503', '040400020502', '040400020501', '040400020401', '040400020403', '040400020306', '040400020102', '040400030606', '040400030601', '040301011203', '040301011202', '040301011109', '040301010705', '040301010704', '040301010703', '040301010702', '040301010605', '040301010604', '040301010205', '040301010101', '040302040405', '040302040401', '040302040106', '040301030205', '040301030104', '040301030103', '040301040506', '040301050607', '040301050606', '040301050605', '040301080913', '040400020101', '041900000002', '041900000001', '040302040101', '041800000300', '040301020104', '040301020101', '040301020402', '040301020111']
 
   
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


    
# class Basics:
#             _results=dict()
#             def __init__(self,ACPFyear, node=DEP.Computers.Remote.Cylo.Main, uversion = None):
#                 if uversion is not None:
#                     pass
#                 else:
#                     pass
#             def create_directory_paths(self,ACPFyear, node=DEP.Computers.Local.name, uversion = None):
#                 '''Creates the most basic DEP directories, ACPF directory and DEP base directory as strings'''
#                 # depBase - location of most DEP inputs and outputs
#                 # acpfBase - location of DEP/ACPF management data geodatabases
#                 # replace 10.27.15.155 with dep2.ae.iastate.edu, 2.5 GB connection instead of 1 GB
#                 # acpfStart = '\\\\dep2.ae.iastate.edu\\D$\\DEP'#\\Man_Data_ACPF\\dep_ACPF' + ACPFyear
#                 # depBase = '\\\\dep2.ae.iastate.edu\\M$\\DEP'
#                 acpfStart = 'M:\\DEP'# D drive points to '\\\\dep2.ae.iastate.edu\\D$\\DEP' (faster, smaller storage)
#                 depBase = acpfStart#'M:\\DEP'# M drive points to '\\\\dep2.ae.iastate.edu\\M$\\DEP' (bigger, slower storage)
#                 # if 'EL3354-02' in node.upper():# or 'DA214B-11' in node.upper():
#                 #     acpfStart = 'D:\\DEP'
#                 #     depBase = 'M:\\DEP'
#                 # elif 'EL3321-M10' in node.upper():
#                 #     # run everything local on laptop
#                 #     acpfStart = 'C:\\DEP'
#                 #     depBase = 'C:\\DEP'
#                 # else:
#                 #     acpfStart = '\\\\EL3354-02\\D$\\DEP'#\\Man_Data_ACPF\\dep_ACPF' + ACPFyear
#                 #     depBase = '\\\\EL3354-02\\M$\\DEP'

#                 # basedata never changes with version
#                 basedataDir = opj(acpfStart, 'Basedata_Summaries')

#                 # see above
#                 acpfBase = opj(acpfStart + uversion, 'Man_Data_ACPF\\dep_ACPF'+ ACPFyear)
#                 # otherBase is raster residue cover maps
#                 otherBase = opj(depBase, 'Man_Data_Other')
#                 depBase += uversion

#                 return acpfBase, depBase, basedataDir, otherBase, acpfStart

# class Datasets:
    
#     class PathDicts:
        
#%%

# """information needed for DEP paths to know what to do:
# computer you're working with
# user that's doing it
# what drive the data is on
# dataset that you're working with
# what type of information the dataset is 
# what year the dataset is from
# what resolution the dataset is in

# """


# class Tools:
#     class Raster(arcpy.Raster):
#         def AddMetadata(self,outDEM, paraDict, template_file_path, log: logging.Logger|None=None):
#             # Set the standard-format metadata XML file's path
#             # need to load metadata editor via 'import arcpy.metadata as md'
#             # outDEM = raster to receive updated metadata
#             # paraDict = dictionary of key/value pairs to be stored in metadata
#             #   values stored include things like analyst, lidar acquisition date, etc.
#             # template_file_path = a template to load a basic summary from
#             # log = otional logging of error messages to a log file
#             # scriptPath = sys.path[0]
#             try:
#                 src_file_path = template_file_path

#                 # Get the target item's Metadata object
#                 tgt_item_md = arcpy.metadata.Metadata(outDEM)    

#                 # Import the ACPF metadata content to the target item
#                 if not tgt_item_md.isReadOnly:
#                     tgt_item_md.importMetadata(src_file_path)
#                     tgt_item_md.title = os.path.split(outDEM)[1]
#                     tgt_item_md.credits = 'Analyst: %s' % os.getlogin()#getpass.getuser()

#                     src_desc = tgt_item_md.summary
#                     if src_desc == None:
#                         src_desc = ''
#                     for key, value in paraDict.items():  
#                         src_desc = src_desc + ('%s %s' % (key, value))
#                     tgt_item_md.summary = src_desc
                    
#                     tgt_item_md.save()

#             except TypeError as e:
#                 print('handling as exception')
#         ##        log.debug(e.message)
#                 tb_str=''.join(traceback.format_exception(None, e, e.__traceback__))
#                 # if sys.version_info.major == 2:
#                 #     arcpy.AddError(e.message)
#                 #     print(e.message)
#                 #     log.warning(e.message)
#                 # elif sys.version_info.major == 3:
                
#                 arcpy.AddError(tb_str)
#                 print(tb_str)
#                 if log is not None:
#                     log.warning(tb_str)

#                 # tb = sys.exc_info()[2]
#                 # tbinfo = traceback.format_tb(tb)[0]

#                 # Concatenate information together concerning the error into a message string
#                 # pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
#                 # # Return python error messages for use in script tool or Python Window
#                 # arcpy.AddError(pymsg)
#                 # # Print Python error messages for use in Python / Python Window
#                 # print(pymsg + "\n")
#                 # if log is not None:
#                 #     log.warning(pymsg)

#                 if arcpy.GetMessages(2) not in tb_str:
#                     msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
#                     arcpy.AddError(msgs)
#                     print(msgs)
#                     if log is not None:
#                         log.warning(msgs)

#             except:
#                 print('handling as except')
#                 # Get the traceback object
#                 tb = sys.exc_info()[2]
#                 tbinfo = traceback.format_tb(tb)[0]

#                 # Concatenate information together concerning the error into a message string
#                 pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
#                 # Return python error messages for use in script tool or Python Window
#                 arcpy.AddError(pymsg)
#                 # Print Python error messages for use in Python / Python Window
#                 print(pymsg + "\n")
#                 if log is not None:
#                     log.warning(pymsg)

#                 if arcpy.GetMessages(2) not in pymsg:
#                     msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
#                     arcpy.AddError(msgs)
#                     print(msgs)
#                     if log is not None:
#                         log.warning(msgs)

#     class Feature:
        
#         def HucSelectionString(self,pdcAcres, pdcSlope, thresh):

#             selStr = pdcAcres + ' >= 15 AND ' + pdcSlope + ' > 0 AND (( AGarea.VALUE_1 * 0.000247) / ' + pdcAcres + ' > %s)' %(thresh)

#             return selStr
#         def MakeCatchList(self,inCATCHFCls, isAG, pdChnl, pdCatch, nAG, inHUC,  log:logging.Logger):
#             '''Makes a list of catchments for DEP random sampling. Sorts results by
#             percent agriculture and threshold adjusts to minimize number of watersheds
#             processed.
#             This was copied from cmd_gen1Flowpath_v6.py on 2020-02-20 to minimize code copies'''
#             try:
#                 log.info("Select Catchments...")
#                 # Create column names
#                 pdcAcres = os.path.basename(pdCatch) + ".Acres"#"pdCatch" + huc12 + "_" + interpType + ".Acres"
#                 pdcSlope = os.path.basename(pdChnl) + ".Slope"#"pdChnl" + huc12 + "_" + interpType + ".Slope"
#                 pdcWSNO = os.path.basename(pdCatch) + ".WSNO"#"pdCatch" + huc12 + "_" + interpType + ".WSNO"


#                 # Tabulate Ag in each catchment (WSNO)
#                 taIsAg = arcpy.sa.TabulateArea(inCATCHFCls, "WSNO", isAG, "VALUE", "AGarea.dbf")
                        
#                 # catchLayer = arcpy.MakeFeatureLayer_management(inCATCHFCls, "CTCH.lyr")
#                 # channelLayer = arcpy.MakeFeatureLayer_management(pdChnl, "CHNL.lyr")
#                 # arcpy.AddJoin_management(catchLayer, "WSNO", taIsAg, "WSNO")
#                 # arcpy.AddJoin_management(catchLayer, "WSNO", channelLayer, "WSNO") 
                        
#                 catchLayer = arcpy.management.MakeFeatureLayer(inCATCHFCls, "CTCH.lyr")
#                 channelLayer = arcpy.management.MakeFeatureLayer(pdChnl, "CHNL.lyr")
#                 arcpy.management.AddJoin(catchLayer, "WSNO", taIsAg, "WSNO")
#                 arcpy.management.AddJoin(catchLayer, "WSNO", channelLayer, "WSNO") 

#                 # Select Catchments GT 25% Ag and 15 Acres
#                 thresh = .25#75
#                 maxCatch = 150
#                 minCatch = 100
#         ####        selStr = '"%s.Acres" >= 15 AND "%s.Slope" > 0 AND (( AGarea.VALUE_1 * 0.000247) / "%s.Acres" > %s)' %(os.path.basename(pdCatch), os.path.basename(pdChnl), os.path.basename(pdCatch), thresh)
#                 selStr = self.HucSelectionString(pdcAcres, pdcSlope, thresh)

#             ## switched to list comprehension to handle errors when no catchments returned (del row would fail)
#             ## bkgelder - 2019/03/20
#             ## revised again to use with statement (for handling 0 returns)
#             ## bkgelder - 2019/09/06
#         ##        CatchList = [str(int(row[0])) for row in arcpy.da.SearchCursor(catchLayer, ["pdCatch%s.WSNO" %(inHUC)], selStr)]
#                 CatchList = []
#                 with arcpy.da.SearchCursor(catchLayer, [pdcWSNO], selStr) as scur:
#         ####        with arcpy.da.SearchCursor(catchLayer, ["%s.WSNO" %(os.path.basename(pdCatch))], selStr) as scur:
#                     for srow in scur:
#                         CatchList.append(srow[0])
                                                        
                
#                 catchCount = len(CatchList)
#                 log.info("ag sub-catchment count: " + str(catchCount) + " at " + str(thresh))

#                 if catchCount > 0:
#                     # Set higher or lower Catchments % Ag criteria to focus on subcatchments (in high ag), area GT 15 Acres
#                     if (catchCount < minCatch) or (catchCount > maxCatch):
#                         if catchCount > maxCatch:
#                             while catchCount > maxCatch and thresh < 0.975:
#                                 thresh += 0.025
#                                 selStr = self.HucSelectionString(pdcAcres, pdcSlope, thresh)
#         ####                        selStr = '"%s.Acres" >= 15 AND "%s.Slope" > 0 AND (( AGarea.VALUE_1 * 0.000247) / "%s.Acres" > %s)' %(os.path.basename(pdCatch), os.path.basename(pdChnl), os.path.basename(pdCatch), thresh)
                        
#                                 CatchList = [str(int(row[0])) for row in arcpy.da.SearchCursor(catchLayer, [pdcWSNO], selStr)]
#         ####                        CatchList = [str(int(row[0])) for row in arcpy.da.SearchCursor(catchLayer, ["%s.WSNO" %(os.path.basename(pdCatch))], selStr)]
#                                 catchCount = len(CatchList)
#                                 log.info("   loop sub-catchment count: " + str(catchCount) + " at " + str(thresh))

#                         elif catchCount < minCatch:
#                             while catchCount < minCatch and thresh > 0.25:
#                                 thresh -= 0.025
#                                 selStr = self.HucSelectionString(pdcAcres, pdcSlope, thresh)
#         ####                        selStr = '"%s.Acres" >= 15 AND "%s.Slope" > 0 AND (( AGarea.VALUE_1 * 0.000247) / "%s.Acres" > %s)' %(os.path.basename(pdCatch), os.path.basename(pdChnl), os.path.basename(pdCatch), thresh)

#                                 CatchList = [str(int(row[0])) for row in arcpy.da.SearchCursor(catchLayer, [pdcWSNO], selStr)]
#         ####                        CatchList = [str(int(row[0])) for row in arcpy.da.SearchCursor(catchLayer, ["%s.WSNO" %(os.path.basename(pdCatch))], selStr)]
#                                 catchCount = len(CatchList)
#                                 log.info("   loop sub-catchment count: " + str(catchCount) + " at " + str(thresh))
#                 else:
#                     log.warning("agricultural sub-catchment count is 0, quitting")
                
#                 arcpy.management.Delete(catchLayer)
#                 arcpy.management.Delete(channelLayer)
                
#                 return(CatchList)
#             except:
                
#                 # Get the traceback object
#                 #
#                 tb = sys.exc_info()[2]
#                 tbinfo = traceback.format_tb(tb)[0]

#                 # Concatenate information together concerning the error into a message string
#                 #
#                 pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
#                 msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"

#                 # Return python error messages for use in script tool or Python Window
#                 #
#                 ##            arcpy.AddError(pymsg)
#                 ##            arcpy.AddError(msgs)

#                 # Print Python error messages for use in Python / Python Window
#                 #
#                 log.warning(pymsg)
#                 log.warning(msgs)

#                 log.warning('failure on: ' + inHUC)