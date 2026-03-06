def main():
    #1. Dictionary: Menyimpan data buku (Key: Judul, Value: Tahun Terbit)
    koleksi_buku = {
        "Struktur Data Dasar": 2021,
        "Pemrograman Python": 2022,
        "Logika Matematika": 2020,
        "Sistem Basis Data": 2023
    }

    #2. List: Menyimpan daftar buku yang dipinjam oleh mahasiswa
    keranjang_pinjam = []

    print("=== Sistem Informasi Perpustakaan Kampus ===")
    
    #3 Menampilkan koleksi yang tersedia dari Dictionary
    print("\nDaftar Koleksi Buku Tersedia:")
    for judul, tahun in koleksi_buku.items():
        print(f"- {judul} (Tahun: {tahun})")

    #4 Simulasi proses peminjaman (Menambahkan item ke List)
    print("\n--- Melakukan Peminjaman ---")
    buku_pilihan1 = "Struktur Data Dasar"
    buku_pilihan2 = "Sistem Basis Data"
    
    keranjang_pinjam.append(buku_pilihan1)
    keranjang_pinjam.append(buku_pilihan2)

    #5 Menampilkan isi List (Buku yang sedang dipinjam)
    print(f"Buku yang Anda pilih: {keranjang_pinjam}")

    #6 Validasi dan Ringkasan Peminjaman
    print("\nRingkasan Transaksi Peminjaman:")
    count = 1
    for item in keranjang_pinjam:
        if item in koleksi_buku:
            print(f"{count}. {item} - Berhasil dipinjam")
            count += 1

    print(f"\nTotal buku yang dipinjam: {len(keranjang_pinjam)} buku.")
    print("Harap dikembalikan dalam waktu 7 hari.")
    print("=== Selesai ===")

if __name__ == "__main__":
    main()