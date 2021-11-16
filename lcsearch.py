import os
import platform
from os import listdir
from os.path import isfile, join
try :
  from colorama import Fore, Style
except : 
  print("Colorama not installed !!!")
  try: 
    os.system("pip install colorama")
    from colorama import Fore, Style
  except:
    print("Error, please contact dev")

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
dim = Style.DIM
reset = Style.RESET_ALL
path = os.getcwd()
test_path = path + "//db"
isdir = os.path.isdir(test_path)
plt = platform.system()

if plt == "Linux" or plt == "Linux2":
  clear = 'clear'
else:
  clear = "cls"  

if isdir == True:
  pass
elif isdir == False or db_count == "0":
  os.system("mkdir db")
  print(red + "Error: No Databases detected please put them in db file (first launch ?)")
  input("\n\nPress enter to back to the menu....")
else:
  pass

discord = "\nDiscord : https://discord.gg/pXc3xeCBVm\n"
mypath = path + "/db"
shein_path = path +"/db_shein"
db = [f for f in listdir(mypath) if isfile(join(mypath, f))]

try:
  shein_db = [f for f in listdir(shein_path) if isfile(join(shein_path, f))]
except:
  os.system("mkdir db_shein")
  shein_db = [f for f in listdir(shein_path) if isfile(join(shein_path, f))]

title = "Made by Laughing Coffin Team"
db_count = len(db) + len(shein_db) 
titled = "\n      " + red + title + "\n" + reset 
nbdb = "             Databases[" + red + str(db_count) + reset + "]\n\n\n"
info = titled + nbdb + discord
motd = """ 
█     ▄█▄        ▄████  ▄█    ▄   ██▄   ▄███▄   █▄▄▄▄ 
█     █▀ ▀▄      █▀   ▀ ██     █  █  █  █▀   ▀  █  ▄▀ 
█     █   ▀      █▀▀    ██ ██   █ █   █ ██▄▄    █▀▀▌  
███▄  █▄  ▄▀     █      ▐█ █ █  █ █  █  █▄   ▄▀ █  █  
    ▀ ▀███▀       █      ▐ █  █ █ ███▀  ▀███▀     █   
                   ▀       █   ██                ▀    
                                                      
                 """

def results(data, file):
  os.system(clear)
  print(blue + motd)
  print(info)
  cell_phone = data[0]
  cell_phone = "+" + cell_phone
  print(green + "Phone Number: " + red +  cell_phone, end="\n")
  print(green + "Facebook ID: " + red + data[1], end="\n")
  print(green + "Name: " + red + data[2] + " " + data[3], end="\n")
  print(green + "Gender " + red + data[4], end="\n")
  print(green + "Location: " + red + data[5] + ", " + data[6], end="\n")
  print(reset)

def mailsearch():
  os.system(clear)
  print(blue + motd)
  print(info)
  mail = input("Mail : ")
  for files in shein_db:
    with open(shein_path + "/" + files, "r",  encoding="utf8", errors='ignore') as f1:
      for lines in f1:
        lines = lines.split(":")
        if lines[0] == mail:
          print(green + dim + "Data Found in : " + files + "!!!!" + reset)
          print(green + dim + "mail: " + lines[0] + " mdp: " + lines[1] + reset)
          input("\n\nPress enter to back to the menu....")
          f1.close()
          del f1
          main()
        else:
          pass
      print("No data found in :" + files)
      f1.close()
      del f1  

def idsearch():
  os.system(clear)
  print(blue + motd)
  print(info)
  fb_id = input("Facebook ID : ")
  for files in db:
    with open(mypath + "/" + files, "r", encoding="utf8") as f1:
      for lines in f1:
        lines = lines.split(",")
        if lines[1] == fb_id:
          print(green + dim + "Data Found in : " + files + "!!!!" + reset)
          results(lines, files)
          input("\n\nPress enter to back to the menu....")
          f1.close()
          del f1
          main()
        else:
          pass
      print("No data found in :" + files)
      f1.close()
      del f1

def phonesearch():
  os.system(clear)
  print(blue + motd)
  print(info)
  fb_phone = input("Cell Phone (write national code example: +33): ")
  cell_phone = fb_phone.replace("+", "")
  for files in db:
    with open(mypath + "/" + files, "r", encoding="utf8") as f1:
      for lines in f1:
        lines = lines.split(",")
        if lines[0] == cell_phone:
          print(green + dim + "Data Found in : " + files + "!!!!" + reset)
          results(lines, files)
          input("\n\nPress enter to back to the menu....")
          f1.close()
          del f1
          main()
        else:
          pass
      print("No data found in :" + files)
      f1.close()
      del f1

def howtofind():
  os.system(clear)
  print(blue + motd)
  print(info)
  print("Go to :")
  print("\nhttps://lookup-id.com/")
  input("\n\nPress enter to back to the menu....")
  main()

def menu(Number, Text):
  number = red +"[" + green + Number + red + "]" + reset 
  render = number + " " + Text + "\n"
  print(render)

def main():
  os.system(clear)
  print(blue + motd)
  print(info)
  menu("1", "Search by Facebook ID")
  menu("2", "Search by cell number")
  menu("3", "Search by email (db with mail:pass format only)")
  menu("3", "How to find Facebook user ID ?")
  choice = int(input(red + "---->  "))
  if choice == 1:
    idsearch()
  elif choice == 2:
    phonesearch()
  elif choice == 3:
    mailsearch()
  elif choice == 3:
    howtofind()
  else:
    input("Please enter a correct option...")
    main()    
main()
