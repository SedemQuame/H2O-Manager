""" This is a simple program, to get user credentials and write them to a file ie. contacts file."""
from send_notification import notifications
from db_utils import db_connect, get_data
from plot_data import graph
#from soilmoisture import read_soil_moisture

file_containing_data = 'contacts.txt'

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
    """This can be achieved by readding the lines in the file and
    then rewriting it provided it does not have match a given condition."""

    name = input("Enter name of user you want to remove: ")

    with open(file_containing_data, "r") as file:
        lines = file.readlines()

    with open(file_containing_data, "w") as file:
        for line in lines:
            if name not in line:
                file.write(line)


def menu():
    print("==============MENU=============")
    print("!1) Add or Remove Users.      !")
    print("!2) Current Tank Data.        !")
    print("!3) Settings & Configuration  !")
    print("===============================")
    return(int(input("Choice: ")))



def get_tank_data():
    notifications()

    """ Retrieving data from the tank."""
    results = get_data(db_connect())
    dates = []
    water_level = []
    for row in results:
        dates.append(row['data'])
        water_level.append(int(row['water_level']))
    
    graph(water_level, dates)    


def setting_and_configuration():
    print("settings and let user decide what to do.")


def interface():
    if choice == 1:
        print("Options.")
        print("1) Add user. ")
        print("2) Remove user.")
        sub_choice = int(input("Choice: "))
        if (sub_choice == 1):
            #Adding new user information.
            add_users()
        elif (sub_choice == 2):
            #Removing exisiting user information.s
            remove_users()
        else:
            print("Input not recognised. \r\nTry again.")
    elif choice == 2:
        get_tank_data()
    elif choice == 3:
        setting_and_configuration()
    else:
        print("Input not recognised. \r\nTry again")


while True:
    choice = menu()
    interface()