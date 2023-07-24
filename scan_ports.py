import socket

def scan_ports(target, ports):
    open_ports = []
    closed_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)

        sock.close()

    return open_ports, closed_ports

def main():
    target = input("Enter the website/domain to scan: ")
    port_range = input("Enter the range of ports to scan (e.g., 1-100): ")

    start_port, end_port = map(int, port_range.split('-'))
    ports_to_scan = range(start_port, end_port + 1)

    open_ports, closed_ports = scan_ports(target, ports_to_scan)

    print("\nOpen ports:")
    if open_ports:
        for port in open_ports:
            print(f"Port {port} is open.")
    else:
        print("No open ports found.")

    print("\nClosed ports:")
    if closed_ports:
        for port in closed_ports:
            print(f"Port {port} is closed.")
    else:
        print("All scanned ports are closed.")

if __name__ == "__main__":
    main()
