beasiswa_a = [101, 102, 103, 105]
beasiswa_b = [103, 104, 105, 106]

set_a = set(beasiswa_a)
set_b = set(beasiswa_b)

print("Menerima kedua beasiswa:", sorted(set_a & set_b))
print("Hanya menerima beasiswa A:", sorted(set_a - set_b))
print("Menerima beasiswa B tapi tidak A:", sorted(set_b - set_a))
print("Semua penerima beasiswa yang unik:", sorted(set_a | set_b))
