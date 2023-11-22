from src.utils import parse_packet, create_packet
def test_idempotency():
    IP_packet_v1 = "127.0.0.1;8881;4;hola".encode()
    parsed_IP_packet = parse_packet(IP_packet_v1)
    assert parsed_IP_packet.ip == "127.0.0.1" and parsed_IP_packet.msg == b"hola" and \
        parsed_IP_packet.port == 8881 and parsed_IP_packet.ttl == 4
    IP_packet_v2 = create_packet(parsed_IP_packet)
    assert IP_packet_v1 == IP_packet_v2
