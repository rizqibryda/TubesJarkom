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

def func3():
    
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

def func4():
    
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

def func5():
    
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

def func6():
    
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

def func7():
    
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

def func8():
    
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

def func9():
    
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

def func10():
    
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

if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()

    p2 = Process(target=func2)
    p2.start()
    
    p3 = Process(target=func3)
    p3.start()

    p4 = Process(target=func4)
    p4.start()

    p5 = Process(target=func5)
    p5.start()

    p6 = Process(target=func6)
    p6.start()

    p7 = Process(target=func7)
    p7.start()

    p8 = Process(target=func8)
    p8.start()

    p9 = Process(target=func9)
    p9.start()

    p10 = Process(target=func10)
    p10.start()