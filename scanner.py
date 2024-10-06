import socket, sys
from datetime import datetime

#Define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip address>")
    
#Banner
print("-" * 50)
print("Scanning target" + target)
print("Time started: "+ str(datetime.now()))
print("-" * 50)

try:
    for port in range(0, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = ""
            if(service):
                print("Port {}-{} is open".format(port, service))
        s.close()

except KeyboardInterrupt:
    print("\nExiting")
    sys.exit()
    
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()