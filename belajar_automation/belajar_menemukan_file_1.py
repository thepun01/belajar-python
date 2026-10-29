import pathlib as p

folder_path = p.Path("file")
files = folder_path.glob("*.txt")

count_file = 0

for file in files:
    count_file += 1

print(f"Jumlah file txt di folder '{folder_path}': {count_file}")
