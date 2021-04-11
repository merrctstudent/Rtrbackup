import netmiko,getpass,datetime

from netmiko import ConnectHandler

from datetime import datetime

sdnrtrlab = {
     'device_type' : 'cisco_ios',
     'host' : '192.168.81.10',
     'username' : input("Username for Cisco Appliance:"),
     'password' : getpass.getpass(),
}

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
