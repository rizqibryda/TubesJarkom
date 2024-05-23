import subprocess

# Daftar nama file program klien
client_files = ["clientt.py", "clientt2.py"]

# Jalankan setiap program klien dalam proses terpisah
for client_file in client_files:
    subprocess.Popen(["python", client_file])

print("Semua program klien telah dimulai.")