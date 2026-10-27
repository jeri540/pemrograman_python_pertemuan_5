masukan = input("Masukkan nilai mahasiswa, pisahkan dengan koma: ")

try:
    nilai = [
        float(item.strip())
        for item in masukan.split(",")
        if item.strip()
    ]
except ValueError:
    print("Input tidak valid. Masukkan angka yang dipisahkan dengan koma.")
else:
    if not nilai:
        print("Daftar nilai tidak boleh kosong.")
    elif any(angka < 0 or angka > 100 for angka in nilai):
        print("Setiap nilai harus berada dalam rentang 0 sampai 100.")
    else:
        frekuensi = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

        for angka in nilai:
            if angka >= 85:
                kategori = "A"
            elif angka >= 75:
                kategori = "B"
            elif angka >= 65:
                kategori = "C"
            elif angka >= 50:
                kategori = "D"
            else:
                kategori = "E"

            frekuensi[kategori] += 1

        rata_rata = sum(nilai) / len(nilai)
        print(f"Rata-rata: {rata_rata:.2f}")
        print("Nilai tertinggi:", max(nilai))
        print("Nilai terendah:", min(nilai))
        print("Frekuensi kategori:", frekuensi)
