import os

peminjaman_buku_Adilah = {
    '001': {'judul': 'Tenggelamnya Kapal Van Der Wijck', 'status': 'tersedia', 'peminjam': None},
    '002': {'judul': 'Buya Hamka', 'status': 'tersedia', 'peminjam': None},
    '003': {'judul': 'Bad Romance', 'status': 'tersedia', 'peminjam': None},
    '004': {'judul': 'Dikta dan Hukum', 'status': 'tersedia', 'peminjam': None}
}

def tampilkan_daftar_buku(peminjaman_buku_Adilah):
    print("Daftar Buku:")
    for kode, buku in peminjaman_buku_Adilah.items():
        if buku['status'] == 'tersedia':
            print(f"Kode: {kode} - Judul: {buku['judul']} - Status: {buku['status']}")
        if buku['status'] == 'dipinjam':
            print(f"Kode: {kode} - Judul: {buku['judul']} - Status: {buku['status']} - Peminjam: {buku['peminjam']}")

def pinjam_buku(peminjaman_buku_Adilah, kode_buku_Adilah, peminjam):
    if kode_buku_Adilah in peminjaman_buku_Adilah:
        if peminjaman_buku_Adilah[kode_buku_Adilah]['status'] == 'tersedia':
            peminjaman_buku_Adilah[kode_buku_Adilah]['status'] = 'dipinjam'
            peminjaman_buku_Adilah[kode_buku_Adilah]['peminjam'] = peminjam
            print(f"Buku dengan kode {kode_buku_Adilah} berhasil dipinjam oleh {peminjam}.")
        else:
            print("Maaf, buku tersebut sudah dipinjam.")
    else:
        print("Maaf, buku dengan kode tersebut tidak tersedia.")

def kembalikan_buku(peminjaman_buku_Adilah, kode_buku_Adilah):
    if kode_buku_Adilah in peminjaman_buku_Adilah:
        if peminjaman_buku_Adilah[kode_buku_Adilah]['status'] == 'dipinjam':
            peminjaman_buku_Adilah[kode_buku_Adilah]['status'] = 'tersedia'
            peminjaman_buku_Adilah[kode_buku_Adilah]['peminjam'] = None
            print(f"Buku dengan kode {kode_buku_Adilah} berhasil dikembalikan.")
        else:
            print("Maaf, buku tersebut tidak dalam daftar yang dipinjam.")
    else:
        print("Maaf, buku dengan kode tersebut tidak tersedia.")

def menu_utama():
    while True:
        print("\nPilihan Menu:")
        print("1. Tampilkan Daftar Buku Tersedia")
        print("2. Pinjam Buku")
        print("3. Kembalikan Buku")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

        if pilihan == '1':
            tampilkan_daftar_buku(peminjaman_buku_Adilah)
        elif pilihan == '2':
            kode = input("Masukkan kode buku yang ingin dipinjam: ")
            peminjam = input("Masukkan nama peminjam: ")
            pinjam_buku(peminjaman_buku_Adilah, kode, peminjam)
        elif pilihan == '3':
            kode = input("Masukkan kode buku yang ingin dikembalikan: ")
            kembalikan_buku(peminjaman_buku_Adilah, kode)
        elif pilihan == '4':
            os.system("cls")
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

os.system("cls")
menu_utama()
