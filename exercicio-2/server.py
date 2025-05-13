import socket

"""
Servidor UDP que ecoa mensagens de volta para o cliente
Discentes: Arthur Abreu, Enzo Veloso, Josiney Junior
"""

def main():
    host = '127.0.0.1'
    port = 6000
    max_size = 64*1024  # Tamanho máximo permitido (64 KB - overhead)

    # Configura o socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Servidor UDP ouvindo na porta {port}...")

    try:
        while True:
            # Recebe dados e endereço do cliente
            data, addr = server_socket.recvfrom(max_size)  
            print(f"Recebido de {addr}: {data.decode()}")
            
            # Envia os dados de volta (eco)
            server_socket.sendto(data, addr)
    except KeyboardInterrupt:
        print("\nServidor encerrando...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()