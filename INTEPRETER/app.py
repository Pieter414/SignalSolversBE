from PIL import Image
import os

def display_images(folder_path, list):
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')) and f[:2] in list]
    if not image_files:
        print("Tidak ada file gambar dalam folder.")
        return
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        img = Image.open(image_path)
        img.show()


def f1(text, input):
    new_text = [c+input for c in text if c.isalpha()]
    return new_text
            

def main():
    while True:
        user = str(input("BISINDO atau SIBI (B/S) : ")).upper()
        text = str(input("Masukkan teks : ")).upper()
        if user == 'B':
            display_images(folder_path, f1(text, "1"))
        elif user == 'S':
            display_images(folder_path, f1(text, "2"))
        else:
            break

folder_path = 'INTEPRETER/src'
main()