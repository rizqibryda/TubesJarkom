#import socket module
from socket import * # Import semua modul socket
import sys # Import modul sys // In Order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Mempersiapkan stopkontak peladen // Prepare a server socket
serverSocket.bind(("", 8080)) #Fill in start
serverSocket.listen(1) #Fill in end

while True:
    # Buat koneksi // Establish the connection
    print('Siap diterima...')
    # menerima permintaan koneksi dari client
    connectionSocket, addr = serverSocket.accept()
    try:
        # menerima pesan dari client
        message = connectionSocket.recv(1024).decode()
        # Membagi pesan di setiap spasi, kemudian mengambil index kedua sebagai nama file
        filename = message.split()[1]
        # Membuka file dari filename dengan mengabaikan index pertama nama file
        openfile = open(filename[1:])
        f = open(filename[1:])
        # Membaca file yag telah dibuka dan disimpan di outputdata
        outputdata = openfile.read() #Send one HTTP header line into socket
        
        responseline = "HTTP/1.1 200 OK\n\r"
        responseline += "Content-Type : text/html\r\n\r\n"
        connectionSocket.send(responseline.encode())
        print("Dari klien: " + responseline + message)

        # Mengirimkan output data ke klien // Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        #connectionSocket.close()
    
    except IOError:
        #Send response message forfile not found
        responseline = "HTTP/1.1 404 Not Found\n\r"
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 NOT FOUND</h1></body></html>".encode())
        print("Dari klien: " + responseline + message)
        
        # Menutup koneksi // Close client socket
        connectionSocket.close()
    # Menutup server socket
    serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data