import os
import json

# Thư mục chứa các file ảnh
image_folder = 'public/images'
output_folder = 'public/pages'

# Lấy danh sách tất cả các file ảnh trong thư mục
image_filenames = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Tạo thư mục đầu ra nếu chưa tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Tạo file JSON chứa danh sách các file ảnh
with open('public/images.json', 'w', encoding='utf-8') as json_file:
    json.dump(image_filenames, json_file, ensure_ascii=False, indent=4)

print(f'{len(image_filenames)} images found and saved to images.json.')
