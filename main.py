#library imports
import paramiko

#file inports
from options import homeInitialization

def main():
    option1In = homeInitialization.homeScreenOption1()
    option1Out = homeInitialization.homeScreenInput(option1In)
    user = option1Out[0]
    userPort = 22
    hostname= option1Out[1]
    userPassword = option1Out[2]
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port = userPort, username=user,password=userPassword)
        while True:
            try:
                cmd = input("$> ")
                if cmd == "exit": break
                stdin, stdout, stderr = client.exec_command(cmd) 
                print(stdout.read().decode())
            except KeyboardInterrupt:
                break
        client.close()
    except:
        print("Invalid input")   
    print(type(stdin))
    print(type(stdout))
if __name__ == "__main__":
    main()