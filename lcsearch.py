import os
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

discord = "\nDiscord : https://discord.gg/pXc3xeCBVm\n"
path = os.getcwd()
mypath = path + "/db"
shein_path = path +"/db_shein"
db = [f for f in listdir(mypath) if isfile(join(mypath, f))]
shein_db = [f for f in listdir(shein_path) if isfile(join(shein_path, f))]
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
dim = Style.DIM
reset = Style.RESET_ALL
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
test_path = path + "//db"
isdir = os.path.isdir(test_path)
if isdir == True:
  print("")
elif isdir == False or db_count == "0":
  os.system("mkdir db")
  print(red + "Error: No Databases detected please put them in db file (first launch ?)")
  input("\n\nPress enter to back to the menu....")
else:
  pass

def results(data, file):
  os.system("clear")
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
  os.system("clear")
  print(blue + motd)
  print(info)
  mail = input("Mail : ")
  for files in shein_db:
    f = open(shein_path + "/" + files, "r", errors='ignore')
    f1 = f.readlines()
    for x in f1:
      x = x.split(":")
      if x[0] == mail:
        print(green + dim + "Data Found in : " + files + "!!!!" + reset)
        print(green + dim + "mail: " + x[0] + " mdp: " + x[1] + reset)
        input("\n\nPress enter to back to the menu....")
        f.close()
        del f, f1
        main()
      else:
        pass
    print("No data found in :" + files)
    f.close()
    del f, f1  

def idsearch():
  os.system("clear")
  print(blue + motd)
  print(info)
  fb_id = input("Facebook ID : ")
  for files in db:
    f = open(mypath + "/" + files, "r")
    f1 = f.readlines()
    for x in f1:
      x = x.split(",")
      if x[1] == fb_id:
        print(green + dim + "Data Found in : " + files + "!!!!" + reset)
        results(x, files)
        input("\n\nPress enter to back to the menu....")
        f.close()
        del f, f1
        main()
      else:
        pass
    print("No data found in :" + files)
    f.close()
    del f, f1

def phonesearch():
  os.system("clear")
  print(blue + motd)
  print(info)
  fb_phone = input("Cell Phone (write national code example: +33): ")
  cell_phone = fb_phone.replace("+", "")
  for files in db:
    f = open(mypath + "/" + files, "r")
    f1 = f.readlines()
    for x in f1:
      x = x.split(",")
      if x[0] == cell_phone:
        print(green + dim + "Data Found in : " + files + "!!!!" + reset)
        results(x, files)
        input("\n\nPress enter to back to the menu....")
        f.close()
        del f, f1
        main()
      else:
        pass
    print("No data found in :" + files)
    f.close()
    del f, f1

def howtofind():
  os.system("clear")
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
  os.system("clear")
  print(blue + motd)
  print(info)
  menu("1", "Search by Facebook ID")
  menu("2", "Search by cell number")
  menu("3", "Search by email")
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
