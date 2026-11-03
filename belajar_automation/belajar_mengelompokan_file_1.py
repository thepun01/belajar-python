# Mengelompokkan file berdasarkan ekstensi
from pathlib import Path
from shutil import move

folder_path = Path("latihan_2")

if not folder_path.exists():
    print(f"Folder '{folder_path}' tidak ditemukan.")
    exit()
    
item_document_pattern = (".txt", ".docx", ".pdf", ".csv", ".xlsx", ".pptx")
item_image_pattern = (".jpg", ".jpeg", ".png", ".gif")

for item in folder_path.iterdir():
    if item.is_file():
        if item.suffix.lower() in item_document_pattern:
            # Buat folder "Documents" jika belum ada
            document_folder = folder_path / "Documents"
            document_folder.mkdir(exist_ok=True) 
            
            # Alasan kode di atas dapat menggantikan pengecekan keberadaan folder dan membuat folder jika belum ada (Cara If - Else sederhana)
            # karena memanfaatkan fitur bawaan dari pathlib 
            # mkdir(exist_ok=True) yang akan membuat folder jika belum ada dan tidak akan menimbulkan error jika folder sudah ada.
            
            # Pindahkan file ke folder "Documents"
            move(str(item), str(document_folder / item.name))
        elif item.suffix.lower() in item_image_pattern:
            # Buat folder "Images" jika belum ada
            image_folder =  folder_path / "Images"
            image_folder.mkdir(exist_ok=True)
            
            # Pindahkan file ke folder "Images"
            move(str(item), str(image_folder / item.name))
        else:
            # Buat folder "Others" jika belum ada
            others_folder = folder_path / "Others"
            others_folder.mkdir(exist_ok=True)
            
            # Pindahkan file ke folder "Others"
            move(str(item), str(others_folder / item.name))

    