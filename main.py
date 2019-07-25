""" This is a simple program, to get user credentials and write them to a file ie. contacts file."""
from send_notification import notifications
from db_utils import db_connect, get_data
from plot_data import graph
from colorama import Fore, Back, Style
import time

#from soilmoisture import read_soil_moisture

file_containing_data = 'contacts.txt'
water_level = []

def add_users():
    #Function to write data to an external file for storage.
    file_containing_data = "contacts.txt"
    fullname = input("Enter your full name: ")
    email_address = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")

    #Writing user data to file NB:Will implement databases later.
    file = open(file_containing_data, "a+")

    #Writing to file.
    file.write(fullname + "," + email_address + "," + phone_number + "\r\n")
    file.close()


def remove_users():
    #Function to remove user data from external file storage.
    """This can be achieved by reading the lines in the file and
    then rewriting it provided it does not have match a given condition."""

    name = input(Fore.RED + "Enter name of user you want to remove: ")

    with open(file_containing_data, "r") as file:
        lines = file.readlines()

    with open(file_containing_data, "w") as file:
        for line in lines:
            if name not in line:
                file.write(line)


def menu():
    print(Fore.YELLOW + "==============MENU=============")
    print(Fore.GREEN + "(1) Add or Remove Users.      !")
    print(Fore.GREEN + "(2) Current Tank Data.        !")
    print(Fore.GREEN + "(3) Settings & Configuration  !")
    print(Fore.YELLOW + "===============================")
    print("")
    return(int(input(Fore.YELLOW + "Choice: ")))



def get_tank_data():
    """ Retrieving data from the tank."""
    results = get_data(db_connect())
    dates = []
    for row in results:
        dates.append(row['data'])
        water_level.append(int(row['water_level']))
    
    graph(water_level, dates)    


def setting_and_configuration():
    print("settings and let user decide what to do.\n\r")


def interface():
    if choice == 1:
        print(Fore.YELLOW + "\n\r============OPTIONS=============")
        print(Fore.GREEN + "(1) Add user. ")
        print(Fore.GREEN + "(2) Remove user.")
        print(Fore.YELLOW + "================================")
        
        print("")
        
        sub_choice = int(input("Choice: "))
        if (sub_choice == 1):
            #Adding new user information.
            add_users()
        elif (sub_choice == 2):
            #Removing exisiting user information
            print(Fore.RED + "Typing a users name will remove them from data file.\n\r")
            time.sleep(2)
            
            print("")
            remove_users()
        else:
            print(Fore.RED + "Input not recognised. \r\nTry again.")
            
        print("")

    elif choice == 2:
        print(Fore.GREEN + "Graphing water levels...\n\r")
        
        time.sleep(2)
        get_tank_data()
        print("Current Water Level Is: " + str(water_level[len(water_level)-1]))
        print("")
        
        print(Fore.GREEN + "Sending SMS & EMAIL notificationss.\n\r")
        time.sleep(2)
        
        notifications()
    elif choice == 3:
        print("")      
        setting_and_configuration()
        print("")
    else:
        print(Fore.RED + "Input not recognised. \r\nTry again")


while True:
    choice = menu()
    interface()