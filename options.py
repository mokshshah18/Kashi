import os #used to remove a file
import getpass #used for password
from sys import exit #used to exit the program on option 4

class homeInitialization:
    
    def __init__(self):
        pass

    def homeScreenOption1():
        print("Welcome to Kashi")
        print("Choose an option")
        print("1. Create a new local file")
        print("2. To use a previously saved file")
        print("3. Delete and create a new local file")
        print("4. Exit")
        option1In = input()
        return option1In
    
    def homeScreenOption2():
        file = open("../Creds.txt","a")
        print("Enter in a username:", end=" ")
        username = input()
        print("Enter in the hostname:", end=" ")
        hostname = input()
        password = getpass.getpass()
        file.write(username+"\n")
        file.write(hostname+"\n")
        file.write(password+"\n")
        return homeInitialization.return_Creds()
    
    def homeScreenInput(option1):
        if(option1=="1"):
            return homeInitialization.homeScreenOption2()
        elif(option1=="2"):
            return homeInitialization.return_Creds()
        elif(option1=="3"):
            os.remove("../Creds.txt")
            return homeInitialization.homeScreenOption2()
        elif(option1=="4"):
            print("Cya soon!")
            exit()
    
    def return_Creds():
        file = open("../Creds.txt","r")
        retList = []
        for i in file:
            retList.append(i.rstrip('\n'))
        return retList
