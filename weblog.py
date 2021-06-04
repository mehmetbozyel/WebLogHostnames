# Python3 code to display hostname of IP address
  
# Importing socket library
import socket
  
# Function to display hostname and
# IP address
def get_Host_name_IP(IP):
    try:
        host_name = socket.gethostbyaddr(IP.rstrip())
        print("IP: ", IP ,"  Hostname: ",host_name[0])
    except:
        print("Unable to get Hostname for ", IP)
    print("--------------------------------------")
 
# Driver code

print("Reading file...")
logfile = open ('logs.txt', 'r')
lines = logfile.readlines()

print("Getting hostnames... \n")
for line in lines:
  IP = line.split()[0] #Parsing file and taking ip address
  try:
    get_Host_name_IP(IP)
  except Exception as e:
    print(IP,"Unable to get Hostname")
    
logfile.close()
