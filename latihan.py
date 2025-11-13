# Buat list sebanyak 5 elemen dengan nilai bebas
A = [10, 20, 30, 40, 50]
print("List A awal:", A)

# --- AKSES LIST ---
# Tampilkan elemen ke-3
print("Elemen ke-3:", A[2])

# Ambil nilai elemen ke-2 sampai ke-4
print("Elemen ke-2 sampai ke-4:", A[1:4])

# Ambil elemen terakhir
print("Elemen terakhir:", A[-1])

# --- UBAH ELEMEN LIST ---
# Ubah elemen ke-4 dengan nilai lainnya
A[3] = 100
print("Setelah ubah elemen ke-4:", A)

# Ubah elemen ke-4 sampai dengan elemen terakhir
A[3:] = [100, 200]
print("Setelah ubah elemen ke-4 sampai terakhir:", A)

# --- TAMBAH ELEMEN LIST ---
# Ambil 2 bagian dari list pertama (A) dan jadikan list kedua (B)
B = A[0:2]
print("List B hasil ambil 2 elemen dari A:", B)

# Tambah list B dengan nilai string
B.append("Python")
print("List B setelah ditambah string:", B)

# Tambah list B dengan 3 nilai
B.extend([300, 400, 500])
print("List B setelah ditambah 3 nilai:", B)

# Gabungkan list B dengan list A
C = B + A
print("Gabungan list B dan A:", C)
