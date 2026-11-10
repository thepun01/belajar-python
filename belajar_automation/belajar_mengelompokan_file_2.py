# Mengelompokkan file berdasarkan ekstensi
from pathlib import Path
import shutil
    
def  create_folder(folder_name: str, subfolder_name: str = None):
    folder = folder_path / folder_name
    folder.mkdir(exist_ok=True)
    
    if subfolder_name:    
        subfolder = folder / subfolder_name
        subfolder.mkdir(exist_ok=True)
        return subfolder
    
    # Alasan kode di atas dapat menggantikan pengecekan keberadaan folder dan membuat folder jika belum ada (Cara If - Else sederhana)
    # karena memanfaatkan fitur bawaan dari pathlib 
    # mkdir(exist_ok=True) yang akan membuat folder jika belum ada dan tidak akan menimbulkan error jika folder sudah ada.
    
    return folder

def move_file(source_file: Path, destination_folder: Path):
    try:
        if (destination_folder / source_file.name).exists():
            print(f"File dengan nama {source_file.name} sudah ada di folder tujuan {destination_folder},")
            print(f"Mohon ganti nama file {source_file.name} atau pindahkan file tersebut ke folder lain.")
            return
        else:
            shutil.move(str(source_file), str(destination_folder / source_file.name))
            print(f"Berhasil memindahkan file {source_file.name} ke folder {destination_folder}")
    except FileNotFoundError as FNFError:
        print(f"Gagal memindahkan file {source_file.name}: {FNFError}")
    except PermissionError as permissionError:
        print(f"Gagal memindahkan file {source_file.name}: {permissionError}")
    except shutil.Error as shutilError:
        print(f"Gagal memindahkan file {source_file.name}: {shutilError}")
    except OSError as osError:
        print(f"Gagal memindahkan file {source_file.name}: {osError}")

file_categories = {
    ".txt": "Documents",
    ".docx": "Documents",
    ".odt": "Documents",
    ".pdf": "Documents",
    ".csv": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos"
}

folder_path = Path("latihan_2")

if not folder_path.exists():
    print(f"Folder '{folder_path}' tidak ditemukan.")
    exit()

if not any(item.is_file() for item in folder_path.iterdir()):
    print(f"Tidak ada file di folder '{folder_path}' untuk diproses.")
    exit()

for item in folder_path.iterdir():
    if item.is_file():
        category = file_categories.get(item.suffix.lower(), "Others")
        
        match category:
            case "Documents":
                # Buat folder "Documents" jika belum ada
                document_extension = item.suffix[1:].upper()
                document_folder = create_folder("Documents", document_extension)
                            
                # Pindahkan file ke subfolder berdasarkan ekstensi
                move_file(item, document_folder)
            case "Images":
                # Buat folder "Images" jika belum ada
                image_extension = item.suffix[1:].upper()
                image_folder = create_folder("Images", image_extension)
                
                # Pindahkan file gambar ke folder berdasarkan ekstensi
                move_file(item, image_folder)
            case "Videos":    
                # Buat folder "Videos" jika belum ada
                video_extension = item.suffix[1:].upper()
                video_folder = create_folder("Videos", video_extension)
    
                # Pindahkan file video ke folder berdasarkan ekstensi
                move_file(item, video_folder)
            case _:
                # Buat folder "Others" jika belum ada
                others_folder = create_folder("Others")
                    
                # Pindahkan file ke folder "Others"
                move_file(item, others_folder)
    
    
                
