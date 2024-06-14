from socket import *
# creating an ip address input to display in terminal
# pass in a valid ip address 54.205.142.17
ip = input("Enter the ip address :")
# Start the ip address with number 1
port_start = int(input("Enter the number of port to start the scanning e.g 1 :"))
# pass in the number of ip you want to scan example 1 to 300
port_stop = int (input("Enter the port to stop the scan on e.g 500 :"))
# create a main_array=[]
main_array=[]
#use a for loop for the port in range the pass in the starting port and end port
for port in range(port_start,port_stop+1):
    addr = (ip,port)
    s = socket(AF_INET,SOCK_STREAM)
    s.connect_ex(addr)
    result = s.connect_ex(addr)
    setdefaulttimeout(0.01)
    s.close()
    if (result == 0):
        print("The port number {} is not open".format(port))
        main_array.append(port)
    else:
        print("The port number {} is not open".format(port))
print("_"*40)
print("The scanning is done...")
print("The ports which are open are:...")
print(main_array)
