from src.utils import check_routes

TEXT_FOLDER = "./test/test_files"

## El test es 1 --to--> 2 --to--> 3
def test_check_route():
    # Supongamos que llega un paquete para 1 que dice que llega hasta 3
    address = ("127.0.0.1", 8882)
    #Esperamos que esto de la direccion de 2
    new_address = check_routes(TEXT_FOLDER+"/test_router1.txt", address)

    assert new_address == ("127.0.0.1", 8882)

    # De aqui, simulamos ahora que le llego el packet al 2
    address = ("127.0.0.1", 8883)
    #Esperamos que esto de la direccion de 2
    new_address = check_routes(TEXT_FOLDER+"/test_router2.txt", address)

    assert new_address == ("127.0.0.1", 8883)

def test_none_route():
    # Supongamos que llega un paquete para 1 que dice que llega hasta 4
    address = ("127.0.0.1", 8884)
    #Esperamos que de None
    new_address = check_routes(TEXT_FOLDER+"/test_router1.txt", address)

    assert new_address == None