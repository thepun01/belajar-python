# Mengelompokkan file berdasarkan ekstensi
from pathlib import Path
from shutil import move
import shutil

folder_path = Path("latihan_2")

if not folder_path.exists():
    print(f"Folder '{folder_path}' tidak ditemukan.")
    exit()
    
def  create_folder(folder_name: str):
    folder = folder_path / folder_name
    folder.mkdir(exist_ok=True)
    
    # Alasan kode di atas dapat menggantikan pengecekan keberadaan folder dan membuat folder jika belum ada (Cara If - Else sederhana)
    # karena memanfaatkan fitur bawaan dari pathlib 
    # mkdir(exist_ok=True) yang akan membuat folder jika belum ada dan tidak akan menimbulkan error jika folder sudah ada.
    
    return folder

def create_subfolder(parent_folder: Path, subfolder_name: str):
    subfolder = parent_folder / subfolder_name
    subfolder.mkdir(exist_ok=True)
    return subfolder

def move_file(source_file: Path, destination_folder: Path):
    try:
        if (destination_folder / source_file.name).exists():
            print(f"File dengan nama {source_file.name} sudah ada di folder tujuan {destination_folder},")
            print(f"Mohon ganti nama file {source_file.name} atau pindahkan file tersebut ke folder lain.")
            exit()
        else:
            move(str(source_file), str(destination_folder / source_file.name))
            print(f"Berhasil memindahkan file {source_file.name} ke folder {destination_folder}")
    except FileNotFoundError as FNFError:
        print(f"Gagal memindahkan file {source_file.name}: {FNFError}")
    except shutil.Error as shutilError:
        print(f"Gagal memindahkan file {source_file.name}: {shutilError}")
    except PermissionError as permissionError:
        print(f"Gagal memindahkan file {source_file.name}: {permissionError}")

item_document_pattern = (".txt", ".docx", ".pdf", ".csv", ".xlsx", ".pptx")
item_image_pattern = (".jpg", ".jpeg", ".png", ".gif")
item_video_pattern = (".mp4", ".mkv", ".avi", ".mov")

for item in folder_path.iterdir():
    if item.is_file():
        if item.suffix.lower() in item_document_pattern:
            # Buat folder "Documents" jika belum ada
            document_folder = create_folder("Documents")
            # print(document_folder)
            
            document_extension = item.suffix[1:].upper()
            document_subfolder = create_subfolder(document_folder, document_extension)
            # print(document_subfolder)
            
            # Pindahkan file ke subfolder berdasarkan ekstensi
            move_file(item, document_subfolder)
                
        elif item.suffix.lower() in item_image_pattern:
            # Buat folder "Images" jika belum ada
            image_folder = create_folder("Images")
            # print(image_folder)
            
            image_extension = item.suffix[1:].upper()
            image_subfolder = create_subfolder(image_folder, image_extension)
            # print(image_subfolder)
            
            # Pindahkan file gambar ke subfolder berdasarkan ekstensi
            move_file(item, image_subfolder)
        else:
            # Buat folder "Others" jika belum ada
            others_folder = create_folder("Others")
            
            # Pindahkan file ke folder "Others"
            move_file(item, others_folder)
