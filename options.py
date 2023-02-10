import os #used to remove a file
import getpass #used for password
from sys import exit #used to exit the program on option 4

#file imports
from transferProtocols import cSftp

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
        option1In = "2"
        return option1In
    
    def homeScreenOption2():
        file = open("Creds.txt","a")
        print("Enter in a username:", end=" ")
        username = input()
        print("Enter in the hostname:", end=" ")
        hostname = input()
        password = getpass.getpass()
        file.write(username+"\n")
        file.write(hostname+"\n")
        file.write(password+"\n")
        file.close() #important because the strings may not be rendered till the file is not closed
        retLi = homeInitialization.return_Creds()
        return retLi
    def homeScreenInput(option1):
        if(option1=="1"):
            return homeInitialization.homeScreenOption2()
        elif(option1=="2"):
            return homeInitialization.return_Creds()
        elif(option1=="3"):
            os.remove("Creds.txt")
            return homeInitialization.homeScreenOption2()
        elif(option1=="4"):
            print("Cya soon!")
            exit()
    
    def return_Creds():
        file = open("Creds.txt","r")
        retList = []
        for i in file:
            retList.append(i.rstrip('\n'))
        return retList
    
class cmdOptions:
    def __init__(self,command,sftp) -> None:
        self.command = command
        self.sftp = sftp

    def commandLineIfs(self):
        cmd = self.command
        sftpClient = self.sftp
        if cmd == "cd" : 
            sftpClient = cSftp.cd(sftpClient, "./Desktop")#a function that changes the directory
            print(sftpClient.getcwd())
        return cmd