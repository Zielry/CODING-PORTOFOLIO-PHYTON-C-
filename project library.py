Daftar_Buku = [
    {"Judul": "Laskar Pelangi", 
     "Penulis": "Andrea Hirata", "Tersedia": True},
    {"Judul": "Harry Potter",
    "Penulis": "J.K. Rowling", "Tersedia": True},
    {"Judul": "The Lord of the Rings", 
    "Penulis": "J.R.R. Tolkien", "Tersedia": True},
]

while True:
    print("\n ===== MENU MANAJEMEN PERPUSTAKAAN ===== ")
    print("1. Daftar Buku")
    print("2. Tambah Buku")
    print("3. Kurangi / Hapus Buku")
    print("4. Cari Buku Berdasarkan Judul")
    print("5. Cari Buku Berdasarkan Penulis")
    print("6. Edit Buku")
    print("7. Pinjam Buku")
    print("8. Kembalikan Buku")
    print("9. Keluar")
    pilihan = input("Pilih menu (1-9): ")
    print("-" * 30)

    if pilihan == "1":
        print("--- DAFTAR BUKU SAAT INI ---")
        for urutan, buku in enumerate(Daftar_Buku, 1):
            status = "Tersedia" if buku["Tersedia"] else "Dipinjam"
            print(f"{urutan}. Buku: {buku['Judul']}, Penulis: {buku['Penulis']} - {status}")
        print(f"Total buku: {len(Daftar_Buku)} buah")

    elif pilihan == "2":
        print("--- TAMBAH BUKU BARU ---")
        judul_baru = input("Masukkan judul buku: ")
        penulis_baru = input("Masukkan nama penulis: ")
        Daftar_Buku.append({"Judul": judul_baru, "Penulis": penulis_baru, "Tersedia": True})

    elif pilihan == "3":
        print("--- KURANGI / HAPUS BUKU ---")
        if len(Daftar_Buku) == 0:
            print("Daftar buku masih kosong, tidak ada yang bisa dihapus.")
        else:
            judul_dihapus = input("Masukkan judul buku yang ingin dihapus: ")
            buku_dihapus = next((buku for buku in Daftar_Buku if buku["Judul"].lower() == judul_dihapus.lower()), None)
            if buku_dihapus:
                Daftar_Buku.remove(buku_dihapus)
                print(f"Berhasil! Buku '{judul_dihapus}' telah dihapus.")
            else:
                print(f"Buku dengan judul '{judul_dihapus}' tidak ditemukan!")

    elif pilihan == "4":
        print("--- CARI BUKU BERDASARKAN JUDUL ---")
        if len(Daftar_Buku) == 0:
            print("Daftar buku masih kosong.")
        else:
            cari_judul = input("Masukkan judul buku yang dicari: ")
            buku_ditemukan = next((buku for buku in Daftar_Buku if buku["Judul"].lower() == cari_judul.lower()), None)
            if buku_ditemukan:
                status = "Tersedia" if buku_ditemukan["Tersedia"] else "Dipinjam"
                print(f"Buku '{cari_judul}' DITEMUKAN - Penulis: {buku_ditemukan['Penulis']} - {status}.")
            else:
                print(f"Buku dengan judul '{cari_judul}' tidak ditemukan!")

    elif pilihan == "5":
        print("--- CARI BUKU BERDASARKAN PENULIS ---")
        if len(Daftar_Buku) == 0:
            print("Daftar buku masih kosong.")
        else:
            cari_penulis = input("Masukkan nama penulis yang dicari: ")
            buku_ditemukan = [buku for buku in Daftar_Buku if buku["Penulis"].lower() == cari_penulis.lower()]
            if buku_ditemukan:
                print(f"Buku karya '{cari_penulis}' DITEMUKAN:")
                for buku in buku_ditemukan:
                    status = "Tersedia" if buku["Tersedia"] else "Dipinjam"
                    print(f"- {buku['Judul']} - {status}")
            else:
                print(f"Buku dengan penulis '{cari_penulis}' tidak ditemukan!")

    elif pilihan == "6":
        print("--- EDIT BUKU ---")
        if len(Daftar_Buku) == 0:
            print("Daftar buku masih kosong.")
        else:
            judul_diedit = input("Masukkan judul buku yang ingin diedit: ")
            buku_diedit = next((buku for buku in Daftar_Buku if buku["Judul"].lower() == judul_diedit.lower()), None)
            if buku_diedit:
                print(f"Buku '{judul_diedit}' DITEMUKAN. Silakan masukkan data baru.")
                judul_baru = input("Masukkan judul baru (tekan Enter untuk tidak mengubah): ")
                penulis_baru = input("Masukkan nama penulis baru (tekan Enter untuk tidak mengubah): ")
                if judul_baru:
                    buku_diedit["Judul"] = judul_baru
                if penulis_baru:
                    buku_diedit["Penulis"] = penulis_baru
                print(f"Berhasil! Buku '{judul_diedit}' telah diperbarui.")
            else:
                print(f"Buku dengan judul '{judul_diedit}' tidak ditemukan!")

    elif pilihan == "7":
        print("--- PINJAM BUKU ---")
        if len(Daftar_Buku) == 0:
            print("Daftar buku masih kosong.")
        else:
            judul_dipinjam = input("Masukkan judul buku yang ingin dipinjam: ")
            buku_dipinjam = next((buku for buku in Daftar_Buku if buku["Judul"].lower() == judul_dipinjam.lower()), None)
            if buku_dipinjam:
                if buku_dipinjam["Tersedia"]:
                    buku_dipinjam["Tersedia"] = False
                    print(f"Berhasil! Buku '{judul_dipinjam}' telah dipinjam.")
                else:
                    print(f"Maaf, buku '{judul_dipinjam}' sedang dipinjam oleh orang lain.")
            else:
                print(f"Buku dengan judul '{judul_dipinjam}' tidak ditemukan!")

    elif pilihan == "8":
        print("--- KEMBALIKAN BUKU ---")
        if len(Daftar_Buku) == 0:
            print("Daftar buku masih kosong.")
        else:
            judul_dikembalikan = input("Masukkan judul buku yang ingin dikembalikan: ")
            buku_dikembalikan = next((buku for buku in Daftar_Buku if buku["Judul"].lower() == judul_dikembalikan.lower()), None)
            if buku_dikembalikan:
                if not buku_dikembalikan["Tersedia"]:
                    buku_dikembalikan["Tersedia"] = True
                    print(f"Berhasil! Buku '{judul_dikembalikan}' telah dikembalikan.")
                else:
                    print(f"Buku '{judul_dikembalikan}' tidak sedang dipinjam, tidak perlu dikembalikan.")
            else:
                print(f"Buku dengan judul '{judul_dikembalikan}' tidak ditemukan!")

    elif pilihan == "9":
        print("Terima kasih telah menggunakan menu perpustakaan. See you soon!")
        break