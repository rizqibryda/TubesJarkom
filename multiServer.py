from socket import *  # Import semua modul socket
import sys  # Import modul sys untuk mengakhiri program
import threading  # Import modul threading untuk multithreading

# Membuat soket TCP (AF_INET untuk IPv4, SOCK_STREAM untuk streaming data)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Mengikat soket ke alamat IP "" (semua antarmuka) dan port 8080
serverSocket.bind(("", 8080))

# Mengatur soket untuk mendengarkan koneksi masuk, dengan backlog 5 (jumlah maksimum koneksi yang antri)
serverSocket.listen(5)

while True:
    # Mencetak pesan yang menunjukkan server siap menerima koneksi
    print('Siap diterima...')

    # Menerima koneksi dari klien, mengembalikan soket baru untuk komunikasi dan alamat klien di addr
    connectionSocket, addr = serverSocket.accept()

    # Membuat thread baru untuk menangani klien
    client_thread = threading.Thread(args=(connectionSocket, addr))
    client_thread.start()

    try:
        # Menerima data (hingga 1024 byte) dari klien, menerjemahkannya sebagai string
        message = connectionSocket.recv(1024).decode()

        # Mengekstrak nama file yang diminta dengan membagi pesan pada spasi putih dan mengambil elemen kedua (dengan asumsi formatnya adalah "GET /filename HTTP/1.1")
        filename = message.split()[1]

        try:
            # Membuka file yang diminta (tidak termasuk garis miring awal, jika ada)
            with open(filename[1:]) as openfile:
                # Membaca seluruh konten file ke outputdata
                outputdata = openfile.read()

                # Membuat baris header respons HTTP yang menunjukkan keberhasilan (200 OK) dan jenis konten (text/html)
                responseline = "HTTP/1.1 200 OK\nContent-Type: text/html\r\n\r\n"

                # Mengirim header respons ke klien
                connectionSocket.send(responseline.encode())

                # Mengirim seluruh konten file ke klien dengan sekali panggil
                connectionSocket.sendall(outputdata.encode())

                # Mencetak permintaan yang diterima dan respons yang dikirim untuk debugging
                print("Dari klien: " + responseline + message)

        except FileNotFoundError:  # Menangani kasus file tidak ditemukan
            # Membuat baris header respons HTTP yang menunjukkan "404 Not Found"
            responseline = "HTTP/1.1 404 Not Found\n\r\n"

            # Mengirim header respons error dan pesan error HTML sederhana ke klien
            connectionSocket.send(responseline.encode())
            connectionSocket.send("<html><head></head><body><h1>404 NOT FOUND</h1></body></html>".encode())

            # Mencetak permintaan yang diterima dan respons error yang dikirim untuk debugging
            print("Dari klien: " + responseline + message)

    except Exception as e:  # Menangani semua jenis error lain
        # Mencetak pesan error dan informasi detailnya
        print("Error:", e)

        # Membuat baris header respons HTTP yang menunjukkan "500 Internal Server Error"
        responseline = "HTTP/1.1 500 Internal Server Error\n\r\n"

        # Mengirim header respons error dan pesan error HTML sederhana ke klien
        connectionSocket.send(responseline.encode())
        connectionSocket.send("<html><head></head><body><h1>500 Internal Server Error</h1></body></html>".encode())

        # Mencetak permintaan yang diterima dan respons error yang dikirim untuk debugging
        print("Dari klien: " + responseline + message)

    # Menutup soket klien
    connectionSocket.close()

# Menutup soket server (tidak akan tercapai karena loop while True di atas)
serverSocket.close()

# Menghentikan program (tidak akan tercapai karena loop while True di atas)
sys.exit()