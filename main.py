from ezmanga import menu
from ezmanga import *

try:   
   if __name__ == '__main__':
      menu = menu.Menu()
except:
      os.system("python3 -m pip install -r requirements.txt")
