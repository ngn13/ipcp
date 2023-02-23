import socket
import psutil
import pyperclip
from sys import argv

def get_ip(intf):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def main():
    if len(argv)<2:
        print("Usage: ipcp <interface>")
        exit()

    intf = argv[1]
    intfs = psutil.net_if_addrs()

    for i in intfs:
        if i == intf:
            ip = get_ip(intf)
            print("Address: " + intf)
            pyperclip.copy(ip)
            print("Copied to clipboard")
            exit()

    print("Interface not found")
    exit()


if __name__ == "__main__":
    main()
