import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
    except socket.error as e:
        print(f"Couldn't connect to server: {e}")
        sock.close()

ip_address = input("Enter the IP address to scan: ")
for port in range(1, 1025):
    scan_port(ip_address, port)
192.168