import paramiko
import os
import configuration
import time
import datetime
from datetime import timedelta


class Sshgstlaunch():

    def __init__(self,):
        self.make_connection()

    def make_connection(self,):
        print("runing")
        self.ssh_client =paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection = self.ssh_client.connect(hostname=configuration.ip,username=configuration.username,password=configuration.password)
        self.run_gst_launch()
        
    def run_gst_launch(self,):
        rendered_list = []
        current_list = []
        average_list = []
        stdin,stdout,stderr=self.ssh_client.exec_command('ps -aux | grep "modetest"')
        for i in stdout.readlines():
            if "modetest" in i:
                print("modetest already exists")
                break
            else:
                self.ssh_client.exec_command(configuration.modetest)
                print("modetest commnad is executed.")
        print("running..")
        print("starttime: ",datetime.datetime.now())
        stdin,stdout,stderr=self.ssh_client.exec_command(command = 'cd /media/card; pwd')
        for i in configuration.list_off_cmds:
            f= open('C:\\xxx\\xxxx\\xxx\\{0}.txt'.format(i.split("/usb")[1].split("!")[0].strip("/")),"a+")
            stdin,stdout,stderr=self.ssh_client.exec_command(command = i)
            for i in stdout.readlines():
                f.write(i)
            f.close()

    def run_display(self,):
        print("before execution time:")

    def run_playback(self,):
        pass

    def run_record(self,):
        pass

if __name__  == "__main__":
    ssh = Sshgstlaunch()
    
