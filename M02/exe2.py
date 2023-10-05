class Barang:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def cetak(self, kode, harga):
        print(f"| {'Kode Produk':<20}{':':^6}{kode:>20} |")
        print(f"| {'Nama Produk':<20}{':':^6}{self.nama:>20} |")
        print(f"| {'Qty Produk':<20}{':':^6}{self.jumlah:>20} |")
        print(f"| {'Harga Produk':<20}{':':^6}{harga:>20} |")
        print(f'{"-"*48}:^50')


class HandSanitizer(Barang):
    def __init__(self, jumlah):
        self.kode = 'H0001'
        self.price = 20000

        super().__init__('Hand Sanitizer', jumlah)

    def cetak(self):
        super().cetak(self.kode, self.price)

class BanMobil(Barang):
    def __init__(self, jumlah):
        self.kode = 'B0001'
        self.price = 200000

        super().__init__('Ban Mobil', jumlah)

    def cetak(self):
        super().cetak(self.kode, self.price)


class Buah(Barang):
    def __init__(self, jumlah):
        self.kode = 'B0123'
        self.price = 30000

        super().__init__('Buah-Buahan', jumlah)

    def cetak(self):
        super().cetak(self.kode, self.price)


class BotolBayi(Barang):
    def __init__(self, jumlah):
        self.kode = 'B0987'
        self.price = 40000

        super().__init__('Botol Minuman Bayi', jumlah)

    def cetak(self):
        super().cetak(self.kode, self.price)

if __name__ == "__main__":
    hs = int(input('Masukkan jumlah hand sanitizer yang terjual bulan ini : '))
    bm = int(input('Masukkan jumlah ban mobil yang terjual bulan ini : '))
    bb = int(input('Masukkan jumlah buah-buahan yang terjual bulan ini : '))
    bmb = int(input('Masukkan jumlah botol minuman bayi yang terjual bulan ini : '))
    hand_sanitizer = HandSanitizer(hs)
    ban_mobil = BanMobil(bm)
    buah_buahan = Buah(bb)
    botol_bayi = BotolBayi(bmb)

    print()
    print(f"{'Laporan Bulanan E-Commerce':^50}")
    print(f'{"-"*48}:^50')
    hand_sanitizer.cetak()
    ban_mobil.cetak()
    buah_buahan.cetak()
    botol_bayi.cetak()
    print()
    
