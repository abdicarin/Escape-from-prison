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
    print_slow("3. view instructions")

    while True:  # början 
        choice =  input("Choose an option (1,2,3): ")
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
                print_slow("hope you will comeback soon")
                time.sleep(1)
            exit()  

        elif choice=="3":
            print("\n")
            filename="readme.txt"

            try:
                with open(filename, "r",encoding="utf-8") as file:
                    inside=file.read()
                    print_slow(inside)
            except FileNotFoundError:
                print("the file ",file,"was not found")
            except Exception as e:
                print("something went wrong",e)




        else:
            print_slow("Invalid choice. Try again.")
    

setup_menu()

