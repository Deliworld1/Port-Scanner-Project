# First four lines is importing libraries that used.
import socket
import subprocess
import sys
from datetime import datetime

# This line clears the terminal screen based on the operating system used.
subprocess.call('clear' if sys.platform == 'linux' or sys.platform == 'darwin' else 'cls', shell=True)

# To input the target IP address for scanning.
server = input("Enter IP address to scan: ")
serverIP = socket.gethostbyname(server)

# Captures the start time of the scanning process.
start = datetime.now()

# Print a nice banner with the scanning started and the start time information.
print("_" * 60)
print("Scanning target IP address...")
print("Scanning started at: " + str(datetime.now().strftime("%H:%M:%S")))
print("_" * 60)

# Scanning through each port to check ports are open.
# Also handles any error to exit out with no issue.
try:
    for port in range(1, 1000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((serverIP, port))
        if result == 0:
            try:
                service = socket.getservbyport(port, 'tcp')
            except OSError:
                service = 'Unknown service'
            print(f"Port {port} is open ({service})")
        sock.close()
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()
except socket.error:
    print("Connection to Server error")
    sys.exit()

# Capture the time scanning proceess is finished.
end = datetime.now()

# Print how long it took to scan.
total = end - start
print("_" * 60)
print("Scanning completed in " + str(total) + " seconds")
