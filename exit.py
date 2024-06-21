import socket

def stop_server(server_ip, server_port):
    # Membuat objek socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Menghubungkan ke server
        client_socket.connect((server_ip, server_port))

        # Mengirim perintah untuk memberhentikan server
        client_socket.sendall(b'STOP')

    finally:
        # Menutup koneksi
        client_socket.close()

# Panggil fungsi untuk memberhentikan server
stop_server('127.0.0.1', 8080)