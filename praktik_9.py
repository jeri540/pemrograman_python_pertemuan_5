inventaris = {}


def tambah_barang(nama, harga, stok):
    if not nama.strip():
        raise ValueError("Nama barang tidak boleh kosong.")
    if nama in inventaris:
        raise ValueError(f"Barang '{nama}' sudah ada.")
    if harga < 0 or stok < 0:
        raise ValueError("Harga dan stok tidak boleh negatif.")

    inventaris[nama] = (harga, stok)


def update_stok(nama, stok_baru):
    if nama not in inventaris:
        raise KeyError(f"Barang '{nama}' tidak ditemukan.")
    if stok_baru < 0:
        raise ValueError("Stok tidak boleh negatif.")

    harga, _ = inventaris[nama]
    inventaris[nama] = (harga, stok_baru)


def cari_barang(rentang_min, rentang_maks):
    if rentang_min < 0 or rentang_maks < 0:
        raise ValueError("Rentang harga tidak boleh negatif.")
    if rentang_min > rentang_maks:
        raise ValueError("Harga minimum tidak boleh melebihi harga maksimum.")

    return {
        nama: (harga, stok)
        for nama, (harga, stok) in inventaris.items()
        if rentang_min <= harga <= rentang_maks
    }


def total_nilai_inventaris():
    return sum(harga * stok for harga, stok in inventaris.values())


if __name__ == "__main__":
    tambah_barang("Buku", 12000, 10)
    tambah_barang("Pensil", 3000, 25)
    tambah_barang("Penghapus", 2000, 15)

    update_stok("Buku", 12)

    print("Inventaris:", inventaris)
    print("Barang dengan harga Rp3.000–Rp15.000:", cari_barang(3000, 15000))
    print("Total nilai inventaris: Rp", total_nilai_inventaris())
