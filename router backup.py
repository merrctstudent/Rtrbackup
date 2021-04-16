import netmiko,getpass,datetime

from netmiko import ConnectHandler

from netmiko.ssh_exception import NetMikoTimeoutException

from paramiko.ssh_exception import SSHException

from netmiko.ssh_exception import AuthenticationException

from datetime import datetime

sdnrtrlab = {
     'device_type' : 'cisco_ios',
     'host' : '192.168.81.10',
     'username' : input("Username for Cisco Appliance:"),
     'password' : getpass.getpass(),
}

try:
    net_connect = ConnectHandler(**sdnrtrlab)
    output = net_connect.send_command("show run")
    net_connect.disconnect()
    current_date = datetime.now()
    current_date_string = str(current_date)
    extension = ".txt"
    file_name = current_date_string + extension
    with open(file_name, "w") as ciscofile:
        ciscofile.write(output)
        ciscofile.close()

except (NetMikoTimeoutException):
     print("Netmiko timed out when connecting to " + sdnrtrlab['host'])

except (AuthenticationException):
     print("Netmiko has experienced an authentication error connecting to " + sdnrtrlab['host'])

except (SSHException):
     print("Netmiko has experienced an SSH error when connecting to " + sdnrtrlab['host'])

print("End of Script")
