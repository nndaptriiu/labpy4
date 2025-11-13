# Program Input Data Mahasiswa
# Menghitung Nilai Akhir berdasarkan bobot Tugas 30%, UTS 35%, dan UAS 35%

mahasiswa = []  # list untuk menyimpan data mahasiswa

while True:
    print("\n=== Input Data Mahasiswa ===")
    nama = input("Nama Mahasiswa: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    # Hitung nilai akhir
    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    # Tambahkan data ke list
    mahasiswa.append({
        "Nama": nama,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": round(nilai_akhir, 2)
    })

    # Tanya apakah ingin menambah data lagi
    lanjut = input("Tambah data lagi? (y/t): ").lower()
    if lanjut == 't':
        break

# Tampilkan semua data
print("\n=== Daftar Nilai Mahasiswa ===")
print("No | Nama\t | Tugas | UTS | UAS | Nilai Akhir")
print("-" * 55)
for i, mhs in enumerate(mahasiswa, start=1):
    print(f"{i}. {mhs['Nama']}\t | {mhs['Tugas']} | {mhs['UTS']} | {mhs['UAS']} | {mhs['Nilai Akhir']}")

