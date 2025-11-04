from PIL import Image, ImageDraw, ImageFont
import os

# Papka yo'li
path = r"c:\Users\Comp-MIR\Desktop\yangi tizm"

def create_project_image(filename, title, bg_color, accent_color):
    # Rasm o'lchamlari
    width, height = 300, 200
    
    # Asosiy rasm
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Dizayn elementlari
    # - Header qismi
    draw.rectangle([0, 0, width, 40], fill=accent_color)
    # - Asosiy matn
    draw.text((20, 60), title, fill="white")
    # - Dekorativ chiziq
    draw.line([(20, 100), (280, 100)], fill=accent_color, width=2)
    
    # Saqlash
    img.save(os.path.join(path, filename))

# Loyihalar uchun rasmlarni yaratish
create_project_image("project1.jpg", "Web Dizayn", "#1E1E1E", "#FF4444")
create_project_image("project2.jpg", "Mobile App", "#1E1E1E", "#44FF44")
create_project_image("project3.jpg", "Desktop App", "#1E1E1E", "#4444FF")