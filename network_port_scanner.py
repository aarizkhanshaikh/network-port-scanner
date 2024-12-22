import socket
import ipaddress
import sys
from datetime import datetime
from termcolor import colored
from threading import Thread, Lock
from queue import Queue

lock = Lock()  # To prevent print overlapping
open_ports = []  # Shared list for storing open ports
queue = Queue()  # Queue for managing port tasks


def print_title():
    title = r"""
////////////////////////////////////////////////////////////////////////
//   _   _      _                      _                              //
//  | \ | | ___| |___      _____  _ __| | __                          //
//  |  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /                          //
//  | |\  |  __/ |_ \ V  V / (_) | |  |   <                           //
//  |_|_\_|\___|\__| \_/\_/ \___/|_|  |_|\_\                          //
//  |  _ \ ___  _ __| |_     / ___|  ___ __ _ _ __  _ __   ___ _ __   //
//  | |_) / _ \| '__| __|    \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|  //
//  |  __/ (_) | |  | |_      ___) | (_| (_| | | | | | | |  __/ |     //
//  |_|   \___/|_|   \__|    |____/ \___\__,_|_| |_|_| |_|\___|_|     //
//                                                                    //
////////////////////////////////////////////////////////////////////////
    
    Made by - Aariz S
"""
    print(colored(title, "green"))


def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET6 if ":" in ip else socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                with lock:
                    open_ports.append(port)
                    print(colored(f"Port {port}: Open", "green"))
            else:
                with lock:
                    print(f"Port {port}: Closed")
    except Exception:
        pass


def worker(ip):
    while not queue.empty():
        port = queue.get()
        scan_port(ip, port)
        queue.task_done()


def scan_ports(ip, ports, thread_count=100):
    for port in ports:
        queue.put(port)

    threads = []
    for _ in range(thread_count):
        thread = Thread(target=worker, args=(ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def get_scan_options():
    print(colored("\n--- Port Scanner Options ---", "cyan"))
    
    # Get target IP or Hostname
    target = input(colored("Enter target (IP or Hostname): ", "blue"))
    if not validate_ip(target):
        print(colored("Invalid IP address or hostname! Exiting.", "red"))
        sys.exit(1)

    # Select port scanning options
    print(colored("\nSelect Scan Option:", "cyan"))
    print("1. Common ports (21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 8080)")
    print("2. Top 100 ports")
    print("3. All ports (Extensive Scan: 1-65535)")

    try:
        option = int(input(colored("Enter your choice (1/2/3): ", "blue")))
        if option == 1:
            ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 8080]
        elif option == 2:
            ports = list(range(1, 101))
        elif option == 3:
            ports = list(range(1, 65536))
        else:
            print(colored("Invalid option selected! Exiting.", "red"))
            sys.exit(1)
    except ValueError:
        print(colored("Invalid input! Please enter a number (1/2/3).", "red"))
        sys.exit(1)

    return target, ports


def generate_report(ip, open_ports, report_file):
    with open(report_file, "w") as file:
        file.write(f"Scan Report for {ip}\n")
        file.write(f"Time: {datetime.now()}\n\n")
        if open_ports:
            file.write("Open Ports:\n")
            file.write("\n".join(str(port) for port in open_ports))
        else:
            file.write("No open ports found.")


def main():
    print_title()

    # Get target and selected ports
    ip, ports = get_scan_options()

    print(colored(f"\nStarting scan on {ip}...", "yellow"))
    scan_ports(ip, ports)

    if not open_ports:
        print(colored("No open ports found. Possible reasons:", "red"))
        print("- Device may be turned off.")
        print("- Firewall is blocking connections.")
        print("- Ports are filtered or closed.")
    else:
        print(colored(f"\nFound {len(open_ports)} open ports!", "green"))

    # Save report
    save_report = input(colored("\nDo you want to save the report to a file? (y/n): ", "cyan"))
    if save_report.lower() == 'y':
        report_file = f"scan_report_{ip.replace(':', '_')}.txt"
        generate_report(ip, open_ports, report_file)
        print(colored(f"Report saved to {report_file}", "green"))


if __name__ == "__main__":
    main()
