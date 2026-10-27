# Latihan Soal Teori dan Praktik Python — Struktur Data

## Identitas

- **Nama:** Jeri Aries
- **NIM:** 20241320007
- **Kelas:** A1-Sistem Informasi

## Soal Teori

### 1. Perbedaan list dan tuple

**List** dan **tuple** sama-sama dapat menyimpan beberapa nilai secara berurutan dan mendukung pengindeksan. Perbedaan mendasarnya adalah list bersifat **mutable** (isinya dapat diubah setelah dibuat), sedangkan tuple bersifat **immutable** (isinya tidak dapat diubah setelah dibuat).

```python
daftar_belanja = ["beras", "telur"]
daftar_belanja.append("gula")  # List dapat diubah

titik_koordinat = (10, 20)  # Tuple cocok untuk data yang tetap
```

Tuple lebih tepat untuk data yang mewakili satu kesatuan tetap, misalnya koordinat `(x, y)`, tanggal `(tahun, bulan, hari)`, atau pasangan nilai yang tidak seharusnya berubah. Selain itu, tuple yang seluruh elemennya hashable dapat digunakan sebagai kunci dictionary atau elemen set. List lebih tepat untuk kumpulan yang perlu ditambah, dihapus, atau diperbarui, seperti daftar belanja atau daftar nilai.

### 2. Mengapa set tidak mendukung pengindeksan?

Set dirancang untuk menyimpan elemen-elemen **unik** dan tidak menjanjikan urutan posisi seperti list atau tuple. Implementasi set menggunakan **hash table**: hash suatu elemen digunakan untuk menentukan lokasi penyimpanannya. Karena lokasi penyimpanan tidak merepresentasikan posisi urut yang stabil, operasi seperti `set_data[0]` tidak memiliki arti yang konsisten.

Set menyediakan operasi berdasarkan keanggotaan dan himpunan, seperti `in`, gabungan, irisan, dan selisih, bukan akses berdasarkan indeks. Jika urutan atau posisi elemen diperlukan, gunakan list atau tuple.

### 3. Hashable dan kunci dictionary

Suatu objek disebut **hashable** apabila memiliki nilai hash yang tetap selama masa hidupnya dan dapat dibandingkan untuk kesamaan. Objek hashable dapat digunakan sebagai elemen set dan kunci dictionary.

Contoh tipe yang umumnya hashable:

- `int`, misalnya `10`
- `str`, misalnya `"apel"`
- `tuple`, jika semua elemennya hashable, misalnya `(1, "A")`

Contoh tipe yang tidak hashable:

- `list`, misalnya `[1, 2]`
- `dict`, misalnya `{"a": 1}`
- `set`, misalnya `{1, 2}`

Kunci dictionary harus hashable karena dictionary menggunakan hash table untuk menentukan lokasi nilai berdasarkan kunci. Hash yang stabil memungkinkan Python menemukan nilai yang terkait dengan kunci secara efisien. Objek mutable seperti list tidak cocok menjadi kunci karena perubahan isinya dapat mengubah hash atau kesetaraan objek dan mengganggu pencarian.

### 4. Kompleksitas `in` pada set dan list

Pada set, operator `in` menggunakan hash elemen untuk langsung mencari lokasi kandidat di hash table. Karena itu, pencarian keanggotaan memiliki kompleksitas **rata-rata O(1)**. Pada list, Python memeriksa elemen satu per satu sampai menemukan nilai yang cocok atau mencapai akhir list, sehingga kompleksitasnya **O(n)**.

Untuk data besar dengan banyak pemeriksaan keanggotaan, set biasanya jauh lebih efisien daripada list. Namun, set memerlukan elemen hashable dan tidak mempertahankan urutan. Dalam kasus terburuk akibat banyak tabrakan hash, pencarian set dapat lebih lambat daripada O(1), tetapi kompleksitas rata-ratanya tetap O(1).

### 5. Perbedaan `sort()` dan `sorted()`

- **`list.sort()`** mengurutkan list secara langsung (**in-place**) dan mengembalikan `None`. Gunakan saat list asal boleh berubah dan tidak diperlukan salinan sebelum pengurutan.
- **`sorted(iterable)`** mengembalikan list baru yang sudah diurutkan dan tidak mengubah iterable asal. Fungsi ini dapat menerima berbagai iterable, misalnya list, tuple, atau set. Gunakan saat data asli perlu dipertahankan.

Keduanya menerima parameter seperti `reverse=True` dan `key=...`.

```python
angka = [3, 1, 2]

hasil_baru = sorted(angka)  # angka tetap [3, 1, 2]
angka.sort()                # angka berubah menjadi [1, 2, 3]
```
