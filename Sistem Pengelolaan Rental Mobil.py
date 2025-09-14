# Mini Project CRUD

data_mobil = [
    ('Toyota', 'Avanza', 2022, 350000, 'Tersedia'),
    ('Honda', 'Civic', 2023, 500000, 'Tersedia'),
    ('Suzuki', 'Ertiga', 2021, 300000, 'Tersedia')
]

print("--- Sistem Penyewaan Mobil Sederhana ---")
print("1. Tambah Mobil (Create)")
print("2. Lihat Daftar Mobil (Read)")
print("3. Update Data Mobil (Update)")
print("4. Hapus Mobil (Delete)")
print("5. Keluar")
pilihan = input("Masukkan pilihan Anda (1-5): ")

if pilihan == '1':
    print("\n--- Tambah Mobil Baru ---")
    if data_mobil[0:4] == data_mobil:
        merk = input("Masukkan merk mobil: ")
        model = input("Masukkan model mobil: ")
        tahun = int(input("Masukkan tahun mobil: "))
        harga = int(input("Masukkan harga sewa per hari: "))
        status = 'Tersedia'

        mobil_baru = (merk, model, tahun, harga, status)
        data_mobil.append(mobil_baru)
        
        print("Mobil berhasil ditambahkan!")
        print("Data mobil yang ditambahkan:", mobil_baru)
    else:
        print("kapasitas penyimpanan penuh (maksimal 4 data). Tidak bisa menambah mobil baru.")

# Lihat daftar mobil (READ)
elif pilihan == '2':
    print("\n--- Daftar Mobil ---")
    print("--- No. Merk, Model, Tahun, Harga/hari, Status ---")

    if data_mobil[0:1]:
        mobil = data_mobil[0]
        print(f"1. {mobil[0]}, {mobil[1]}, {mobil[2]}, Rp {mobil[3]:,}, {mobil[4]}")
    if data_mobil[1:2]:
        mobil = data_mobil[1]
        print(f"2. {mobil[0]}, {mobil[1]}, {mobil[2]}, Rp {mobil[3]:,}, {mobil[4]}")
    if data_mobil[2:3]:
        mobil = data_mobil[2]
        print(f"3. {mobil[0]}, {mobil[1]}, {mobil[2]}, Rp {mobil[3]:,}, {mobil[4]}")
    if data_mobil[3:4]:
        mobil = data_mobil[3]
        print(f"4. {mobil[0]}, {mobil[1]}, {mobil[2]}, Rp {mobil[3]:,}, {mobil[4]}")

# mengubah data mobil (UPDATE)
elif pilihan == '3':
    print("\n--- Update Data Mobil ---")
    if data_mobil[0:1]:
        print(f"1. {data_mobil[0][0]} {data_mobil[0][1]}")
    if data_mobil[1:2]:
        print(f"2. {data_mobil[1][0]} {data_mobil[1][1]}")
    if data_mobil[2:3]:
        print(f"3. {data_mobil[2][0]} {data_mobil[2][1]}")
    if data_mobil[3:4]:
        print(f"4. {data_mobil[3][0]} {data_mobil[3][1]}")
        
    nomor_update = input("Masukkan nomor mobil yang ingin di-update (1-4): ")
    

    if nomor_update == '1' and data_mobil[0:1]:
        data_lama = data_mobil[0]
        print(f"Data lama: {data_lama}")
        merk_baru = input(f"Masukkan merk baru ({data_lama[0]}): ") or data_lama[0]
        model_baru = input(f"Masukkan model baru ({data_lama[1]}): ") or data_lama[1]
        tahun_baru = int(input(f"Masukkan tahun baru ({data_lama[2]}): ") or data_lama[2])
        harga_baru = int(input(f"Masukkan harga baru ({data_lama[3]}): ") or data_lama[3])
        status_baru = input(f"Masukkan status baru ({data_lama[4]}): ") or data_lama[4]
        
        data_mobil[0] = (merk_baru, model_baru, tahun_baru, harga_baru, status_baru)
        print(" Data mobil berhasil di-update!")
        print("Data baru:", data_mobil[0])

    elif nomor_update == '2' and data_mobil[1:2]:
        data_lama = data_mobil[1]
        print(f"Data lama: {data_lama}")
        merk_baru = input(f"Masukkan merk baru ({data_lama[0]}): ") or data_lama[0]
        model_baru = input(f"Masukkan model baru ({data_lama[1]}): ") or data_lama[1]
        tahun_baru = int(input(f"Masukkan tahun baru ({data_lama[2]}): ") or data_lama[2])
        harga_baru = int(input(f"Masukkan harga baru ({data_lama[3]}): ") or data_lama[3])
        status_baru = input(f"Masukkan status baru ({data_lama[4]}): ") or data_lama[4]
        
        data_mobil[1] = (merk_baru, model_baru, tahun_baru, harga_baru, status_baru)
        print("Data mobil berhasil di-update!")
        print("Data baru:", data_mobil[1])
        
    elif nomor_update == '3' and data_mobil[2:3]:
        data_lama = data_mobil[2]
        print(f"Data lama: {data_lama}")
        merk_baru = input(f"Masukkan merk baru ({data_lama[0]}): ") or data_lama[0]
        model_baru = input(f"Masukkan model baru ({data_lama[1]}): ") or data_lama[1]
        tahun_baru = int(input(f"Masukkan tahun baru ({data_lama[2]}): ") or data_lama[2])
        harga_baru = int(input(f"Masukkan harga baru ({data_lama[3]}): ") or data_lama[3])
        status_baru = input(f"Masukkan status baru ({data_lama[4]}): ") or data_lama[4]
        
        data_mobil[2] = (merk_baru, model_baru, tahun_baru, harga_baru, status_baru)
        print("Data mobil berhasil di-update!")
        print("Data baru:", data_mobil[2])

    elif nomor_update == '4' and data_mobil[3:4]:
        data_lama = data_mobil[3]
        print(f"Data lama: {data_lama}")
        merk_baru = input(f"Masukkan merk baru ({data_lama[0]}): ") or data_lama[0]
        model_baru = input(f"Masukkan model baru ({data_lama[1]}): ") or data_lama[1]
        tahun_baru = int(input(f"Masukkan tahun baru ({data_lama[2]}): ") or data_lama[2])
        harga_baru = int(input(f"Masukkan harga baru ({data_lama[3]}): ") or data_lama[3])
        status_baru = input(f"Masukkan status baru ({data_lama[4]}): ") or data_lama[4]
        
        data_mobil[3] = (merk_baru, model_baru, tahun_baru, harga_baru, status_baru)
        print("Data mobil berhasil di-update!")
        print("Data baru:", data_mobil[3])

    else:
        print("Pilihan tidak valid atau data tidak ditemukan.")

# Menghapus mobil (DELETE)

elif pilihan == '4':
    print("\n--- Hapus Mobil ---")
    
    if data_mobil[0:1]:
        print(f"1. {data_mobil[0][0]} {data_mobil[0][1]}")
    if data_mobil[1:2]:
        print(f"2. {data_mobil[1][0]} {data_mobil[1][1]}")
    if data_mobil[2:3]:
        print(f"3. {data_mobil[2][0]} {data_mobil[2][1]}")
    if data_mobil[3:4]:
        print(f"4. {data_mobil[3][0]} {data_mobil[3][1]}")

    nomor_hapus = input("Masukkan nomor mobil yang ingin dihapus (1-4): ")

    if nomor_hapus == '1' and data_mobil[0:1]:
        del data_mobil[0]
        print("\n--- Mobil berhasil dihapus! ---")
    elif nomor_hapus == '2' and data_mobil[1:2]:
        del data_mobil[1]
        print("\n--- Mobil berhasil dihapus! ---")
    elif nomor_hapus == '3' and data_mobil[2:3]:
        del data_mobil[2]
        print("\n--- Mobil berhasil dihapus! ---")
    elif nomor_hapus == '4' and data_mobil[3:4]:
        del data_mobil[3]
        print("\n--- Mobil berhasil dihapus!")
    else:
        print("Pilihan tidak valid atau data tidak ditemukan.")
        print("Daftar mobil setelah penghapusan:", data_mobil)

elif pilihan == '5':
    print("\n--- Telah Keluar Dari Sistem ---")

else:
    print("Pilihan tidak valid")