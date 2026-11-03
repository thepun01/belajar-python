# Identifikasi file dan folder
from pathlib import Path

folder_path = Path("latihan_2")

if not folder_path.exists():
    print(f"Folder '{folder_path}' tidak ditemukan.")
    exit()

items = folder_path.iterdir()

for item in items:
    if item.is_file():
        print(f"Nama: {item.name}\nJenis: File\nEkstensi: {item.suffix}")
        print("================================")
    elif item.is_dir():
        print(f"Nama: {item.name}\nJenis: Folder")
        print("================================")
    else:
        print(f"Nama: {item.name}\nJenis: Lainnya")
        print("================================")
