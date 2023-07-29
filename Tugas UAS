# menghitung biaya sewa 
def hitung_biaya_sewa(durasi):
    harga_per_jam = 20000
    harga_per_5_jam = 100000
    harga_per_hari = 500000

    if durasi == 1:
        return harga_per_jam
    elif durasi == 5:
        return harga_per_5_jam
    elif durasi == 24:
        return harga_per_hari
    else:
        return 0


# menu utama
def main():
    daftar_barang = ["laptop", "PS 5", "proyektor", "printer"]

    print("Selamat datang di Rental Laptop & PS 5")
    print("======================================")

    #  data penyewa
    nama_penyewa = input("Masukkan nama penyewa: ")
    umur_penyewa = int(input("Masukkan umur penyewa: "))
    alamat_penyewa = input("Masukkan alamat penyewa: ")

    print("\nDaftar Barang:")
    for index, barang in enumerate(daftar_barang, 1):
        print(f"{index}. {barang}")

    # Pilih barang yang akan disewa
    while True:
        pilihan_barang = int(input("Masukkan nomor barang yang ingin disewa: "))

        if 1 <= pilihan_barang <= len(daftar_barang):
            barang_sewa = daftar_barang[pilihan_barang - 1]
            break
        else:
            print("Pilihan barang. Silakan pilih lagi.")

    # durasi penyewaan
    while True:
        print("\nDurasi Penyewaan:")
        print("1. 1 jam")
        print("2. 5 jam")
        print("3. 1 hari")

        pilihan_durasi = int(input("Masukan durasi penyewaan: "))

        if pilihan_durasi in [1, 2, 3]:
            if pilihan_durasi == 1:
                durasi = 1
            elif pilihan_durasi == 2:
                durasi = 5
            else:
                durasi = 24

            break
        else:
            print("Pilihan durasi tidak sesuai. Silakan pilih lagi.")

    # biaya sewa berdasarkan durasi
    biaya_sewa = hitung_biaya_sewa(durasi)
    if biaya_sewa == 0:
    
        print("Durasi penyewaan tidak sesuai. Pembatalan penyewaan.")
        return
    if biaya_sewa >= 250000:
        diskon= biaya_sewa*0.1
    else :
        diskon =0

    th= biaya_sewa - diskon
        
     
    print("\n---- Invoice ----")
    print(f"Nama Penyewa: {nama_penyewa}")
    print(f"Umur Penyewa: {umur_penyewa}")
    print(f"Alamat Penyewa: {alamat_penyewa}")
    print(f"Barang yang Disewa: {barang_sewa}")
    print(f"Durasi Penyewaan: {durasi} {'jam' if durasi < 24 else 'Jam'}")
    print(f"Harga Sewa per {durasi} {'jam' if durasi < 24 else 'Jam'}: {biaya_sewa}")
    print(f"Diskon : {diskon}")
    print(f"total yang harus di bayar : ", th)
    
    total_biaya = biaya_sewa 

    # Cek apakah penyewa berusia di atas 18 tahun boolean
    if umur_penyewa > 18:
        print("Anda mendapatkan diskon 10% karena berusia di atas 18 tahun.")
        diskon = total_biaya * 0.1
        total_biaya -= diskon

    print(f"Total Biaya : {total_biaya}")


if __name__ == "__main__":
    main()
