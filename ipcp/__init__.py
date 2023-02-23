import socket
import struct
import fcntl
import psutil
import pyperclip
from sys import argv

def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack("256s", ifname[:15].encode())
    )[20:24])


def main():
    if len(argv)<2:
        print("Usage: ipcp <interface>")
        exit()

    intf = argv[1]
    intfs = psutil.net_if_addrs()

    for i in intfs:
        if i == intf:
            ip = get_ip(intf)
            print("Address: " + ip)
            pyperclip.copy(ip)
            print("Copied to clipboard")
            exit()

    print("Interface not found")
    exit()


if __name__ == "__main__":
    main()
