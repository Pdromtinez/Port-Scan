import socket 

ip = input("Ingrese la direccion IP a escanear")

for port in range(1, 65535):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    
    result = sock.connect_ex((ip, port))
    
    if result == 0:
        print("Puerto abierto" + str(port))
        sock.close()
    else:
        print("puerto cerrado " + str(port))
    