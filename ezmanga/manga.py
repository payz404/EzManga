from ezmanga import *

class Manga():
   
   
   def __init__(self):
      
      os.system('clear')
      self.url = "https://mangapark.net/"
      
      
            
   def getManga(self):
      
     
      console = Console()
      s = requests.Session()
      r = s.get(self.url).text
      scrap = BeautifulSoup(r, 'html5lib')
      content = scrap.find_all('div',class_="item", limit=10)
      
      i = 0
      count = len(content)
      
      table = Table(show_header=True, header_style="magenta")
      table.add_column("[cyan]No[/cyan]", style="dim")
      table.add_column("[blue]Title[/blue]")
      table.add_column("[green]Chapter[/green]")
      table.add_column("[magenta]Last Update[/magenta]", justify="right")
      
      link = ""
      for manga in content:
         
            
         judul = manga.a['title']
         title = judul.split(',')[0].rstrip()
         chapter = manga.find('a', class_="visited")
         ch = chapter.text
         update = manga.find_all('i')[1].text
         getLink = manga.find('a', class_="visited")
         i += 1
         link += self.url+getLink["href"]+" "                        
         table.add_row(f"[cyan]{i}[/cyan]",f"[blue]{title}[/blue]",f"[green]{ch}[/green]",f"[magenta]{update}[/magenta]")
                 
      
      console.print( "\n:popcorn: EZ Manga by @im.payz :popcorn:", justify="center")   
      console.print(table)
      isSelect = int(input("\n[?] Select Manga (1-10): "))
      
      linkManga = link.split(" ")[isSelect-1]
      isOpen = input("[?] Continue to read manga ? : (y/n): ")
      if isOpen == "y" or isOpen == "Y":
         print("[+] Loading...")
         os.system(f"xdg-open {linkManga}")
      elif isOpen == "n" or isOpen == "N":
         pass
      else:
         isOpen = input("[?] Continue to read manga ? : (y/n): ")
      
      
      
   
   
class SearchManga(Manga):
   
   
   def __init__(self):
   
      super().__init__()
   
   def search(self):
   
   
      console = Console()
      key = input("[?] Search Manga: ")
      query = key.replace(" ", "+")
      s = requests.Session()
      r = s.get(self.url+"search?q="+query).text
      scrap = BeautifulSoup(r, 'html5lib')
      content = scrap.find('a',class_="cover")
      judul = content['title']
      title = judul.split(",")[0]
      chapter = scrap.find('a', class_="visited").b.text
      
      manga = scrap.find('h3', class_="d-flex justify-content-between")    
      update = manga.find_all('i')[1].text
      
      
      
      table = Table(show_header=True, header_style="magenta")
      table.add_column("[cyan]No[/cyan]", style="dim")
      table.add_column("[blue]Title[/blue]")
      table.add_column("[green]Chapter[/green]")
      table.add_column("[magenta]Last Update[/magenta]", justify="right")
      table.add_row(f"[cyan]1[/cyan]",f"[blue]{title}[/blue]",f"[green]{chapter}[/green]",f"[magenta]{update}[/magenta]")
      console.print( "\n:popcorn: EZ Manga by @im.payz :popcorn:", justify="")   
      console.print(table)
      
      getLink = scrap.find('a', class_='visited') 
      linkManga = self.url+getLink["href"]
      isOpen = input("[?] Continue to read manga ? : (y/n): ")
      if isOpen == "y" or isOpen == "Y":
         print("[+] Loading...")
         os.system(f"xdg-open {linkManga}")
      elif isOpen == "n" or isOpen == "N":
         pass
      else:
         isOpen = input("[?] Continue to read manga ? : (y/n): ")
      
      
      
      


      
      
         
         
         
         
         
         
         
         
         
         
      