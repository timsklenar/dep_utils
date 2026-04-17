from pathlib import Path
from ..user import User
## A bunch of nested classes allow storage of the DEP computer/user information in one place
class Cylo:
    ## "data storage server managed by Ryan McGeehee"
    class Main:
        "main DEP data repository, read only except for managers (bkgelder)"
        path=Path("\\\\abe-cylo\\dep\\DEP")
    class Dev:
        "DEP development directory, read and write enabled for DEP team members"
        path=Path("\\\\abe-cylo\\depdev")
    ## this dynamically pulls the isu username of the current user by findinng their default user folder name
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
