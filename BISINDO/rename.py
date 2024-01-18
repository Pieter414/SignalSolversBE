import os

def ubah_nama_file_png(dir):
    if not os.path.isdir(dir):
        print("Direktori tidak valid")
        return

    count = 0
    for nama_file in os.listdir(dir):
        path_file_lama = os.path.join(dir, nama_file)

        if os.path.isfile(path_file_lama) and nama_file.lower().endswith('.png'):
            nama_file_baru = f"{count}.png"
            path_file_baru = os.path.join(dir, nama_file_baru)

            os.rename(path_file_lama, path_file_baru)
            print(f"Nama file diubah: {nama_file} -> {nama_file_baru}")
            count += 1

if __name__ == "__main__":
    direktori_target = 'BISINDO/Image/'
    ubah_nama_file_png(direktori_target)
