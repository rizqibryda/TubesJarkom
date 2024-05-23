from multiprocessing import Process
from socket import *
import sys

def func1():
    
    # Menentukan nama host dan nomor port
    serverName = "localhost"
    serverPort = 8080

    # Membuat Tcp Socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # Menghubungi Server
    clientSocket.connect((serverName, serverPort))
    print("Server Connected")

    # Meminta input dari user
    fileName = "/main.html"
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
    pass

def func2():
    # Menentukan nama host dan nomor port
    serverName = "localhost"
    serverPort = 8080

    # Membuat Tcp Socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # Menghubungi Server
    clientSocket.connect((serverName, serverPort))
    print("Server Connected")

    # Meminta input dari user
    fileName = "/main.html"
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

if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()

    p2 = Process(target=func2)
    p2.start()