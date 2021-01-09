from ezmanga import *
from ezmanga import manga as my


class Menu:
   
      
   def __init__(self):
      
      menu = CursesMenu("EZManga v.1","Select Option: ")
      listManga = FunctionItem("Menu Manga", self.menuManga, [])
      searchManga = FunctionItem("Search Manga", self.searchManga, [])
      downloadManga = FunctionItem("Download Manga", self.downloadManga, [])
      menu.append_item(listManga)
      menu.append_item(searchManga)
      menu.append_item(downloadManga)
      menu.start()
      menu.join()
      
      
   def menuManga(self):      
      
      isManga = True  
      while(isManga):
         
         ez = my.Manga()
         ez.getManga()
         
         opt = input("\n[?] Continue ? (y/n): ")
         if opt == "y" or opt == "Y":
            ez.getManga()
         elif opt == "n" or opt == "N":
            isManga = False            
         else:
            opt = input("[?] Continue ? (y/n): ")
                        
            
   
   def searchManga(self):
      
      
      isManga = True
      while(isManga):
      
         ez = my.SearchManga()
         ez.search()
         
         opt = input("\n[?] Continue ? (y/n): ")
         if opt == "y" or opt == "Y":
            ez.search()
         elif opt == "n" or opt == "N":
            isManga = False            
         else:
            opt = input("[?] Continue ? (y/n): ")


   def downloadManga(self):
      
      print("Coming Soon ^_^")
      x = input("[ Press Any Key To Continue... ]")











         
         