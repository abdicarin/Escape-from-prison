import random
import time  #så att inte alla text kommer samma tid
import os
import sys # jag behövde nånting så att alla text kommer inte till sammans. 
def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write("\n")  
    sys.stdout.flush()
def clear_terminal(): #tabort text som behövs inte längre
    if os.name == 'nt':
        os.system('cls')
game_name_asicii="""
 /$$$$$$$$                                                                         
| $$_____/                                                                  
| $$        /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$   
| $$$$$    /$$_____/ /$$_____/ |____  $$ /$$__  $$ /$$__  $$      
| $$__/   |  $$$$$$ | $$        /$$$$$$$| $$  \ $$| $$$$$$$$      
| $$       \____  $$| $$       /$$__  $$| $$  | $$| $$_____/      
| $$$$$$$$ /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$$$$$$/|  $$$$$$$      
|________/|_______/  \_______/ \_______/| $$____/  \_______/      
                                        | $$                                                               
                                        | $$                                                               
                                        |__/ 

 /$$$$$$$$ /$$                       /$$$$$$$           /$$                                                
|__  $$__/| $$                      | $$__  $$         |__/                                                
   | $$   | $$$$$$$   /$$$$$$       | $$  \ $$ /$$$$$$  /$$  /$$$$$$$  /$$$$$$  /$$$$$$$                   
   | $$   | $$__  $$ /$$__  $$      | $$$$$$$//$$__  $$| $$ /$$_____/ /$$__  $$| $$__  $$                  
   | $$   | $$  \ $$| $$$$$$$$      | $$____/| $$  \__/| $$|  $$$$$$ | $$  \ $$| $$  \ $$                  
   | $$   | $$  | $$| $$_____/      | $$     | $$      | $$ \____  $$| $$  | $$| $$  | $$                  
   | $$   | $$  | $$|  $$$$$$$      | $$     | $$      | $$ /$$$$$$$/|  $$$$$$/| $$  | $$                  
   |__/   |__/  |__/ \_______/      |__/     |__/      |__/|_______/  \______/ |__/  |__/       
"""

def setup_menu():

    print_slow("1. Start Game")
    print_slow("2. Exit")
    print_slow("3, view intruction")

    while True:  # början 
        choice =  input("Choose an option (1 or 2): ")
        if choice == "1":
            print_slow("Starting game:")
            time.sleep(1)
            for i in range(1,5):
                print_slow(".")
                time.sleep(1)
        
            clear_terminal()
            print(game_name_asicii)
            for i in range(1,5):
                print_slow(".")
                time.sleep(1)
            clear_terminal()
            
            break  
        elif choice == "2":
            print_slow("Exiting game:")
            for i in range(1,5):
                print_slow(".")
                time.sleep(1)
            exit()  

        # elif choice=="3":
        #     file="reeadme.txt"

        #     try:
        #         with open(file,"r", encoding="utf-8") as fil:
        #             inside=fil.read()
        #             print(inside)
        #     except FileNotFoundError:
        #         print("filen",file"file can not be found")
        #     except Exception as e:
        #         print("something went wrong",e)
            
        # else:
        #     print_slow("Invalid choice. Try again.")
    

setup_menu()
clear_terminal()
def rum1():
    print_slow("Du vaknar upp i en kall, mörk cell. Dörren är låst.")
    print_slow("Rummet är tomt förutom en säng, en toalett och några lösa stenar i väggen.")
    print_slow("Vad vill du undersöka?")
    
    while True:
        print_slow("1. Undersök sängen")
        print_slow("2. Undersök toaletten")
        print_slow("3. Undersök väggen")
        val = input("Välj 1, 2 eller 3: ")

        if val == "1":
            print_slow("Du lyfter på madrassen.")
            for i in range(1,5):
                print_slow(".")
                time.sleep(1)
            print_slow("du hittar ingenting")

        elif val == "2":
            print_slow("Du tittar försiktigt ner i toaletten... bara smutsigt vatten. Inget användbart.")
        elif val == "3":
            print_slow("Du trycker på en lös sten och hittaren **nyckelbit**!")
            print_slow("Du stoppar ner den i fickan.")
            break
        else:
            print_slow("Ogiltigt val. Försök igen.")

    print_slow("Du hör fotsteg i korridoren.det är vakten som kollar runt på cellen, \n du låtsas sova, efter han lämnar du, du försöker stoppa i nyckel för att låsa upp dörren till cellen.")




rum1()