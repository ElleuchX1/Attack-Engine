 

LOGO="""
  ___   _    _                 _             _____                _              
 / _ \\ | |  | |               | |           |  ___|              (_)             
/ /_\\ \\| |_ | |_   __ _   ___ | | __ ______ | |__   _ __    __ _  _  _ __    ___ 
|  _  || __|| __| / _` | / __|| |/ /|______||  __| | '_ \\  / _` || || '_ \\  / _ \\
| | | || |_ | |_ | (_| || (__ |   <         | |___ | | | || (_| || || | | ||  __/
\\_| |_/ \\__| \\__| \\__,_| \\___||_|\\_\\        \\____/ |_| |_| \\__, ||_||_| |_| \\___|
                                                            __/ |                
                                                           |___/                 

- OFFENSIVE SECURITY TOOL # 2020 - 2021
"""



from rich.tree import Tree
import time
from rich import print
from rich.console import Console
import os 

import logging
from rich.logging import RichHandler


log = logging.getLogger("rich")
clear = lambda: os.system('clear')
console = Console()
clear()
console.print(LOGO)
console.print('\n')
console.print("\t"+"[1] Information Gathering")
console.print("\t"+"[2] Fuzzing ")
console.print("\t"+"[3] Checking for Vulnerabilies")
console.print("\t"+"[4] Exploiting Vulnerabilies")
console.print("\t"+"[5] CMS Checking")
console.print("\t"+"[6] Miscellaneous")
console.print("\n\tWRONG INPUT !!! TRY AGAIN .", style="red bold blink2")
time.sleep(10)
clear()
console.print(LOGO)
console.print('\n')