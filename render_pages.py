import os

# Cấu hình số lượng ảnh trên mỗi trang
images_per_page = 20

# Thư mục chứa các file ảnh
image_folder = 'public/images'
output_folder = 'public/pages'

# Lấy danh sách tất cả các file ảnh trong thư mục
image_filenames = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Tạo thư mục đầu ra nếu chưa tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Tạo các trang HTML với phân trang
total_images = len(image_filenames)
total_pages = (total_images // images_per_page) + (1 if total_images % images_per_page != 0 else 0)

for page in range(total_pages):
    start_index = page * images_per_page
    end_index = start_index + images_per_page
    page_filenames = image_filenames[start_index:end_index]

    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toramonline Avatar - Page {}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <h1 id="avatarLink">Toram Online Avatar</h1>
    <div class="gallery">
'''.format(page + 1, page + 1)

    for filename in page_filenames:
        html_content += f'''
        <div class="img-container">
            <img src="../images/{filename}" alt="{filename}">
            <div class="caption">{filename}</div>
        </div>
    '''

    html_content += '''
    </div>
    <div class="pagination">
        <div class="page-info">Page {} of {}</div>
'''.format(page + 1, total_pages)

    if page > 0:
        html_content += f'<a href="page{page}.html" class="prev-next-button">Previous</a>'
    if page < total_pages - 1:
        html_content += f'<a href="page{page + 2}.html" class="prev-next-button">Next</a>'

    html_content += '''
    </div>
    <script>
    document.getElementById("avatarLink").onclick = function() {
        location.href = "../index.html";
    };
</script>
</body>
</html>
'''

    with open(os.path.join(output_folder, f'page{page + 1}.html'), 'w', encoding='utf-8') as file:
        file.write(html_content)

print(f'{total_pages} pages have been created with {total_images} images.')
