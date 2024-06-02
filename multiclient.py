import subprocess

# Daftar nama file program klien
client_files = [
    "clientt.py", 
    "client5.py",
    "client6.py", 
    "client4.py",
    "client2.py",
    "clientt.py", 
    "client10.py",
    "clientt.py", 
    "client9.py",
    "clientt.py", 
    "client4.py",
    "clientt.py", 
    "client8.py",
    "client3.py", 
    "client2.py",
    "client1.py", 
    "client7.py",
    ]

# Jalankan setiap program klien dalam proses terpisah
for client_file in client_files:
    subprocess.Popen(["python", client_file])

print("Semua program klien telah dimulai.")