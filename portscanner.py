import pyfiglet
import sys
import socket
from datetime import datetime
import time

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def scan_ports(target, port_range):
    spinner = spinning_cursor()
    try:
        print("-" * 50)
        print("Scanning Target: " + target)
        print("Scanning started at:" + str(datetime.now()))
        print("-" * 50)

        for port in port_range:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Set timeout to 1 seconds
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                print(f"Port {port} ({service}) is open")
            s.close()
            print(next(spinner), end='\r')  # Print spinning cursor
            time.sleep(0.1)  # Adjust the speed of the spinning cursor
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    except socket.error:
        print("\nServer not responding.")
        sys.exit()

def main():
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)

    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        target = input("Enter target hostname or IP address: ")

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid hostname or IP address. Please try again.")
        sys.exit()

    port_range_input = input("Enter port range (e.g., '1-100', '80,443', or '22'): ")
    port_range = []
    for part in port_range_input.split(','):
        if '-' in part:
            start, end = part.split('-')
            port_range.extend(range(int(start), int(end)+1))
        else:
            port_range.append(int(part))

    scan_ports(target_ip, port_range)

if __name__ == "__main__":
    main()
