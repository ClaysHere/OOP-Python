'''
belum ada module/library
'''

# Exercise 1


class Person:
    ''' class pewaris '''
    jml = 0
    mhs = []
    dsn = []

    def __init__(self, nama, gender, no_hp):
        self.nama = nama
        self.gender = gender
        self.no_hp = no_hp


class Mahasiswa(Person):
    ''' prototype untuk class mahasiswa'''

    def __init__(self, nim, nama, jurusan, gender, no_hp):
        self.nim = nim
        self.jurusan = jurusan

        super().__init__(nama, gender, no_hp)
        super().jml += 1

    def data(self):
        ''' method untuk mengembalikan data keadalam bentuk list '''
        return [self.nim, self.nama, self.jurusan, self.gender, self.no_hp]


class Dosen(Person):
    ''' prototype untuk class dosen '''

    def __init__(self, nip, nama, jabatan, gender, no_hp):
        self.nip = nip
        self.jabatan = jabatan

        super().__init__(nama, gender, no_hp)
        super().jml += 1

    def data(self):
        ''' method untuk mengembalikan data keadalam bentuk list '''
        return [self.nip, self.nama, self.jabatan, self.gender, self.no_hp]


class LenData:
    ''' blueprint untuk menentukan panjang perataan teks '''

    def __init__(self, data):
        self.data = data
        self.i_d = self.get_max_len(0)
        self.nama = self.get_max_len(1)
        self.j = self.get_max_len(2)
        self.gender = self.get_max_len(3)
        self.no_hp = self.get_max_len(4)

    def get_max_len(self, index):
        ''' fungsi/method untuk mengembalikan panjang data terbesar '''
        return max([len(str(d[index])) for d in self.data])


# Exercise 2
class Barang:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def cetak(self, kode, harga, justify):
        j_1 = justify if justify >= 11 else 11
        j_2 = justify if justify >= 10 else 10
        j_3 = justify if justify >= 11 else 11
        j_4 = justify if justify >= 12 else 12

        print(
            f"| {kode:<{j_3}} | {self.nama:<{j_1}} | {self.jumlah:<{j_2}} | {harga:<{j_4}} |")


class HandSanitizer(Barang):
    def __init__(self, jumlah):
        self.kode = 'H0001'
        self.price = 20000

        super().__init__('Hand Sanitizer', jumlah)


class BanMobil(Barang):
    def __init__(self, jumlah):
        self.kode = 'B0001'
        self.price = 200000

        super().__init__('Ban Mobil', jumlah)


class Buah(Barang):
    def __init__(self, jumlah):
        self.kode = 'B0123'
        self.price = 30000

        super().__init__('Buah-Buahan', jumlah)


class BotolBayi(Barang):
    def __init__(self, jumlah):
        self.kode = 'B0987'
        self.price = 40000

        super().__init__('Botol Minuman Bayi', jumlah)

# Exercise 3


class Card:
    ''' blueprint kartu '''

    def __init__(self, nama, gender, jenis_les):
        self.nama = nama
        self.gender = gender
        self.les = jenis_les

    def cetak_kartu(self, tingkatan, jam, biaya):
        ''' fungsi untuk mencetak data '''
        length = max([18 + len(self.nama), 18 + len(tingkatan), 18 + len(str(jam)), 18 + len(str(biaya))]) + \
            2 if max([18 + len(self.nama), 18 + len(tingkatan), 18 +
                     len(str(jam)), 18 + len(str(biaya))]) >= 21 else 23

        max_len = max([len(self.nama), len(tingkatan),
                      len(str(jam)), len(str(biaya)), 3]) + 2

        print('='*length)
        print(f'| Kartu Tanda Pelajar{"|":>{length - 21}}')
        print(
            f'| Nama\t\t: {self.nama}{"|":>{max_len - len(self.nama)}}')
        print(
            f'| Tingkatan\t: {tingkatan}{"|":>{max_len - len(tingkatan)}}')
        print(
            f'| Jam Pengajaran: {jam}{"|":>{max_len - len(str(jam))}}')
        print(
            f'| Biaya Les\t: {biaya}{"|":>{max_len - len(str(biaya))}}')
        print('='*length)


class TK(Card):
    ''' bluprint untuk tingkatan tk '''

    def __init__(self, nama, gender, jenis_les):
        self.biaya = 300_000
        self.jam = 2

        super().__init__(nama, gender, jenis_les)

    def cetak(self):
        ''' fungsi untuk mencetak data '''
        super().cetak_kartu('TK', self.jam, self.biaya)


class SD(Card):
    ''' bluprint untuk tingkatan sd '''

    def __init__(self, nama, gender, jenis_les, kelas):
        self.biaya = 500_000
        self.jam = 2
        self.kelas = kelas

        super().__init__(nama, gender, jenis_les)

    def cetak(self):
        ''' fungsi untuk mencetak data '''
        super().cetak_kartu('SD', self.jam, self.biaya)


class SMP(Card):
    ''' bluprint untuk tingkatan smp '''

    def __init__(self, nama, gender, jenis_les, kelas):
        self.biaya = 700_000
        self.jam = 1
        self.kelas = kelas

        super().__init__(nama, gender, jenis_les)

    def cetak(self):
        ''' fungsi untuk mencetak data '''
        super().cetak_kartu('SMP', self.jam, self.biaya)


class SMA(Card):
    ''' bluprint untuk tingkatan sma '''

    def __init__(self, nama, gender, jenis_les, kelas):
        self.biaya = 1000_000
        self.jam = 1
        self.kelas = kelas

        super().__init__(nama, gender, jenis_les)

    def cetak(self):
        ''' fungsi untuk mencetak data '''
        super().cetak_kartu('SMA', self.jam, self.biaya)
