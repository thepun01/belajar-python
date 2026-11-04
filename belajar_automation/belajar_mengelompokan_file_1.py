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
                
            document_extension = item.suffix[1:].upper()
            document_subfolder = document_folder / document_extension
            document_subfolder.mkdir(exist_ok=True) 
            
            # Alasan kode di atas dapat menggantikan pengecekan keberadaan folder dan membuat folder jika belum ada (Cara If - Else sederhana)
            # karena memanfaatkan fitur bawaan dari pathlib 
            # mkdir(exist_ok=True) yang akan membuat folder jika belum ada dan tidak akan menimbulkan error jika folder sudah ada.
            
            # Pindahkan file ke subfolder berdasarkan ekstensi
            try:    
                move(str(item), str(document_subfolder / item.name))
                print("Berhasil memindahkan file {} ke folder {}".format(item.name, document_subfolder))
            except Exception as e:
                print(f"Gagal memindahkan file {item.name}: {e}")
                
        elif item.suffix.lower() in item_image_pattern:
            # Buat folder "Images" jika belum ada
            image_folder =  folder_path / "Images"
            image_folder.mkdir(exist_ok=True)
            
            image_extension = item.suffix[1:].upper()
            image_subfolder = image_folder / image_extension
            image_subfolder.mkdir(exist_ok=True)
            
            # Pindahkan file gambar ke subfolder berdasarkan ekstensi
            try:
                move(str(item), str(image_subfolder / item.name))
                print("Berhasil memindahkan file {} ke folder {}".format(item.name, image_subfolder))
            except Exception as e:
                print(f"Gagal memindahkan file {item.name}: {e}")
        else:
            # Buat folder "Others" jika belum ada
            others_folder = folder_path / "Others"
            others_folder.mkdir(exist_ok=True)
            
            # Pindahkan file ke folder "Others"
            try:
                move(str(item), str(others_folder / item.name))
                print("Berhasil memindahkan file {} ke folder {}".format(item.name, others_folder))
            except Exception as e:
                print(f"Gagal memindahkan file {item.name}: {e}")
