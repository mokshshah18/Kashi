#library imports
import paramiko
from tkinter import *
from tkinter import ttk

#file imports
from options import homeInitialization
from options import cmdOptions
from transferProtocols import cSftp
from uiElements import uiElements
def main():
    #gui elements
    root = Tk()
    guiClass = uiElements()

    #terminal elements
    option1In = homeInitialization.homeScreenOption1()
    option1Out = homeInitialization.homeScreenInput(option1In)

    user = option1Out[0]
    hostname= option1Out[1]
    userPassword = option1Out[2]

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=user, password=userPassword)

    sftpClient = client.open_sftp()

    while True:
        cmd = input("$*> ")
        if cmd == "exit": break
        cmdPaths = cmdOptions(cmd, sftpClient)#creates an object with the command as an argument and sftpClient as another
        cmd = cmdOptions.commandLineIfs(cmdPaths)
        stdin, stdout, stderr = client.exec_command(cmd) 
        print(stdout.read().decode())
        guiClass.render(root)

    sftpClient.close()
    client.close()

if __name__ == "__main__":
    main()