import sys
import socket

if len(sys.argv) != 4:
    print("Usage: python3 router.py <ip> <port> <table>")
    exit(0)

ip = sys.argv[1]
port = int(sys.argv[2])
ADDRESS = (ip,port)

router_sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
router_sock.bind(ADDRESS)

if __name__ == "__main__":
    while True:
        msg, _ = router_sock.recvfrom(1024)