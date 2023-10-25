from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Packet:
    ip: str
    port: int
    msg: bytes

def get_address(packet: Packet) -> tuple[str,int]:
    return (packet.ip, packet.port)

def parse_packet(msg: bytes):
    ip, port, msg = msg.split(b";")
    ip = ip.decode()
    port = int(port)
    return Packet(ip, port, msg)


def create_packet(packet: Packet):
    l = [packet.ip.encode(), str(packet.port).encode(), packet.msg]
    return b";".join(l)


def check_routes(routes_file_name: str, dest_addr: tuple[str,int]) -> tuple[str,int] | None :
    dest_ip = dest_addr[0]
    dest_port = dest_addr[1]
    with open(routes_file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            network_ip, range_port_min, range_port_max, ip_para_llegar, puerto_para_llegar = line.split(" ")
            
            range_port_min = int(range_port_min)
            range_port_max = int(range_port_max)
            
            # TODO: checkear que dest_ip == network_ip
            if dest_port in range(range_port_min, range_port_max+1):
                return ip_para_llegar, int(puerto_para_llegar)
        
        return None