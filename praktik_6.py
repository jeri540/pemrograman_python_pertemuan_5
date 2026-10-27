kalimat = input("Masukkan sebuah kalimat: ")
kata_kata = kalimat.split()

print("Jumlah kata:", len(kata_kata))
print("Jumlah karakter:", len(kalimat))

if kata_kata:
    kata_terpanjang = max(kata_kata, key=len)
    print("Kata terpanjang:", kata_terpanjang)
else:
    print("Kata terpanjang: tidak ada")

print("Kalimat dalam title case:", kalimat.title())
