from dataclasses import dataclass

@dataclass
class Packet:
    ip: str
    port: int
    msg: bytes

def parse_packet(msg: bytes):
    ip, port, msg = msg.split(b";")
    ip = ip.decode()
    port = int(port)
    return Packet(ip, port, msg)


def create_packet(packet: Packet):
    l = [packet.ip.encode(), str(packet.port).encode(), packet.msg]
    return b";".join(l)
