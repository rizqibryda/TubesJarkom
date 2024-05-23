from socket import *
import sys

# Menentukan nama host dan nomor port
serverName = "localhost"
serverPort = 8080

# Membuat Tcp Socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Menghubungi Server
clientSocket.connect((serverName, serverPort))
print("Server Connected")

# Meminta input dari user
fileName = input("Masukkan nama file (harus diawali dengan \"/\"): ")
request = "GET " + str(fileName)+ " HTTP/1.1"

# Mengirim pesan ke server
clientSocket.send(request.encode())

# Menerima pesan dari server
returnFromServer = clientSocket.recv(4096)

while (len(returnFromServer)> 0):
    print(returnFromServer.decode())
    returnFromServer = clientSocket.recv(4096)

# Menutup koneksi dengan server
clientSocket.close()