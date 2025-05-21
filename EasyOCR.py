import easyocr
import os

# ตั้งค่า path สำหรับ input และ output
input_folder = 'image/input'
output_folder = 'image/output'

# สร้าง reader สำหรับภาษาไทยและอังกฤษ
reader = easyocr.Reader(['th', 'en'])

# ตรวจสอบให้แน่ใจว่า output folder มีอยู่
os.makedirs(output_folder, exist_ok=True)

# วนลูปอ่านไฟล์ทั้งหมดใน input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        image_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')

        # ทำ OCR
        results = reader.readtext(image_path)

        # รวมข้อความที่อ่านได้
        text_lines = [text for (_, text, _) in results]

        # เขียนข้อความลงใน .txt
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(text_lines))

        print(f"✅ OCR complete: {filename} → {os.path.basename(output_path)}")