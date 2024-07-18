import os

# Thư mục chứa các file ảnh
image_folder = 'public/images'
output_folder = 'public/pages'

# Lấy danh sách tất cả các file ảnh trong thư mục
image_filenames = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Tạo thư mục đầu ra nếu chưa tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Tạo trang HTML hiển thị tất cả các ảnh
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toramonline Avatar - All Images</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <h1 id="avatarLink">Toram Online Avatar</h1>
    <div class="gallery">
'''

for filename in image_filenames:
    html_content += f'''
    <div class="img-container">
        <img src="../images/{filename}" alt="{filename}">
        <div class="caption">{filename}</div>
    </div>
'''

html_content += '''
    </div>
    <div class="pagination">
        <div class="page-info">Page 1 of 1</div>
    </div>
    <script>
    document.getElementById("avatarLink").onclick = function() {
        location.href = "../index.html";
    };
    </script>
</body>
</html>
'''

with open(os.path.join(output_folder, 'all.html'), 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f'1 page has been created with {len(image_filenames)} images.')
