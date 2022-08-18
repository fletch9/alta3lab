import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('MAGIC 8 BALL!', font='starwars'),
       'yellow', attrs=['bold'])