import re
from collections import Counter


def analisis_file(nama_file):
    with open(nama_file, "r", encoding="utf-8") as file:
        teks = file.read()

    kata_kata = re.findall(r"\b\w+\b", teks.lower())

    if not kata_kata:
        print("File tidak berisi kata yang dapat dihitung.")
        return

    frekuensi = Counter(kata_kata)
    kata_unik = set(kata_kata)
    sepuluh_teratas = frekuensi.most_common(10)
    hapax = sorted(kata for kata, jumlah in frekuensi.items() if jumlah == 1)
    rasio_type_token = len(kata_unik) / len(kata_kata)

    print("Frekuensi setiap kata:", dict(frekuensi))
    print("10 kata paling sering muncul:", sepuluh_teratas)
    print("Kata yang hanya muncul sekali:", hapax)
    print(f"Rasio kata unik terhadap total kata: {rasio_type_token:.4f}")


if __name__ == "__main__":
    nama_file = input("Masukkan nama file teks: ")

    try:
        analisis_file(nama_file)
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
    except OSError as error:
        print(f"File tidak dapat dibaca: {error}")
