import os
import shutil

source_folder = "downloaded_images"

destination_folder = "public/images"

# Tạo thư mục đích nếu chưa tồn tại
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

tmp = 0
for filename in os.listdir(source_folder):
    if "toram_avatar" in filename:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        
        if not os.path.exists(destination_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied: {filename} to {destination_folder}")
            tmp += 1

print("Completed copying files ->", tmp)
