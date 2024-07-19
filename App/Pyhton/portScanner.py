import socket
import threading
import argparse

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Puerto abierto: {port}")
        else:
            print(f"Puerto cerrado: {port}")
        sock.close()
    except Exception as e:
        print(f"Error escaneado el puerto {port}: {e}")
    finally:
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
    parser = argparse.ArgumentParser(description="Escaner de Puertos")
    parser.add_argument("ip", help="Direccíon IP a escanear")
    parser.add_argument("-t", "--threads", type=int, default=7, help="Número de hilos a usar (7 por defecto )")
    
    args = parser.parse_args()
    
    scan_ports(args.ip, args.threads)