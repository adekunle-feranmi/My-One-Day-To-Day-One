import socket

def banner_grabbing(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except (socket.timeout, ConnectionRefusedError):
        return None

def scan_ports(target, ports):
    results = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            service_banner = banner_grabbing(target, port)
            if service_banner:
                state = "Open"
                results.append((port, state, service_banner))
            else:
                state = "Open (Cannot determine service)"
                results.append((port, state))
        else:
            state = "Closed"
            results.append((port, state))

        sock.close()

    return results

def main():
    target = input("Enter the IP address to scan: ")
    port_range = input("Enter the range of ports to scan (e.g., 1-100): ")

    start_port, end_port = map(int, port_range.split('-'))
    ports_to_scan = range(start_port, end_port + 1)

    scan_results = scan_ports(target, ports_to_scan)

    for port, state, *service in scan_results:
        if service:
            service_info = f"({service[0]})"
        else:
            service_info = ""
        print(f"Port {port}: {state} {service_info}")

if __name__ == "__main__":
    main()
