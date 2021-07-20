login = input("Log in to Kand: ")
import os
import time
kss = False
while True:
    x = input(login + "@KandOS>: ")
    if x == "kand --info":
        print("KandOS is a console-operating-system created by Marsden Cannon. It will be updated frequently.")
    elif x == 'kand --setC -r':
        os.system('color 0c')
    elif x == "kand --upgrade":
        os.system("start chrome.exe https://github.com/Algrythm/Kand")
    elif x == "vassoc":
        os.system('assoc')
    elif x == "kand --cpo":
        os.system('cls')
    elif x == "kand --installmodule --kss":
        print("Installing KSS Module!")
        time.sleep(5)
        print("Installed KSS module!")
        kss = True
    elif x == "kss::std::cout::nl":
        if kss == True:
            print("output: ")
            b = input("")
            print(str(b))
        else:
            print("Error: KANDOS STRING SERVICE (KSS) MODULE NOT FOUND.")
    else:
        print("Error: Command not recognized. Command specified: " + x)
