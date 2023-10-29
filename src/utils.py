from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Packet:
    ip: str
    port: int
    msg: bytes

cache = dict()

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


def check_routes(routes_file_name: str, dest_addr: tuple[str,int], address_from) -> tuple[str,int] | None :
    global cache

    dest_ip, dest_port = dest_addr
    if cache.get(dest_addr) == None:
        cache[dest_addr] = 0
    with open(routes_file_name, "r") as f:
        lines = f.readlines()
        
        def filter_lines(line):
            network_ip, puerto_inicial, puerto_final, ip_para_llegar, puerto_para_llegar = line.split(" ")
            
            puerto_inicial = int(puerto_inicial)
            puerto_final = int(puerto_final)
            return dest_port in range(puerto_inicial, puerto_final+1) and address_from != int(puerto_para_llegar)
        
        lines = list(filter(filter_lines, lines))
        if len(lines) != 0:
            print(cache)
            _,_,_,ip_para_llegar, puerto_para_llegar = lines[cache[dest_addr]%len(lines)].split(" ")
            cache[dest_addr] +=1
            return ip_para_llegar, int(puerto_para_llegar)
        return None