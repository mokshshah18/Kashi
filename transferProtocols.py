#library imports
import paramiko

class cSftp:
    def __init__(self) -> None:
        pass
    def cd(sftpClient, addy):
        try:
            sftpClient.chdir(addy)
            return sftpClient
        except:
            print("invalid address")
        pass