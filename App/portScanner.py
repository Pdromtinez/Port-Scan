import socket
import threading


def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Puerto abierto: {port}")
    sock.close()


def scan_ports(ip, num_threads):
    threads = []
    for port in range(1, 65536):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    
        if len(threads) >= num_threads:
            for thread in threads:
                thread.join()
            threads = []

  
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    ip = input("Ingrese la dirección IP a escanear: ")
    num_threads = int(input("Ingrese el número de hilos a usar: "))
    
    scan_ports(ip, num_threads)