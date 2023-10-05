class Person:
    def __init__(self, name, gender, no_hp) -> None:
        self.name = name
        self.gender = gender
        self.no_hp = no_hp
    
    def cetak(self, jb):
        print(f"| {f'Nama {jb}':<20}{':':^6}{self.name:>15} |")

class Mahasiswa(Person):
    def __init__(self, NIM, name, gender, no_hp) -> None:
        self.__NIM = NIM
        super().__init__(name, gender, no_hp)

    def cetak(self):
        print(f"| {'NIM':<20}{':':^6}{self.__NIM:>15} |")
        super().cetak('Mahasiswa')
        print(f"{'-'*43:^45}")

class Dosen(Person):
    def __init__(self, NIM, name, gender, no_hp) -> None:
        self.__NIP = NIM
        super().__init__(name, gender, no_hp)

    def cetak(self):
        super().cetak('Dosen')
        print(f"| {'No. HP':<20}{':':^6}{self.no_hp:>15} |")
        print(f"{'-'*43:^45}")

if __name__ == "__main__":
    arr_mhs = []
    arr_dsn = []
    jml = int(input('Ingin input berapa data? : '))
    for i in range(jml):
        print()
        jb = input('Ingin input data Mahasiswa(1)/Dosen(2)? : ').lower()
        if jb == 'mahasiswa' or jb == '1':
            print()
            nim = input('Masukkan NIM : ')
            nama = input('Masukkan Nama Mahasiswa : ')
            gender = input('Masukkan Jenis Kelamin Mahasiswa : ')
            no_hp = input('Masukkan No HP Mahasiswa : ')
            arr_mhs.append(Mahasiswa(nim, nama, gender, no_hp))
        elif jb == 'dosen' or jb == '2':
            print()
            nip = input('Masukkan NIP : ')
            nama = input('Masukkan Nama Dosen : ')
            gender = input('Masukkan Jenis Kelamin Dosen : ')
            no_hp = input('Masukkan No HP Dosen : ')
            arr_dsn.append(Dosen(nip, nama, gender, no_hp))

    print()
    print(f"{'-'*43:^45}")
    print(f"|{'Absensi':^43}|")
    print(f"{'-'*43:^45}")
    if len(arr_dsn) > 0:
        print(f"|{'Dosen':^43}|")
        print(f"{'-'*43:^45}")
        for i, dsn in enumerate(arr_dsn):
            print(f"| {f'Dosen ke-{i+1}':<42}|")
            dsn.cetak()
    if len(arr_mhs) > 0:
        print(f"|{'Mahasiswa':^43}|")
        print(f"{'-'*43:^45}")
        for i, mhs in enumerate(arr_mhs):
            print(f"| {f'Mahasiswa ke-{i+1}':<42}|")
            mhs.cetak()
    print(f"| {'Jumlah Pengunjung':<20}{':':^6}{jml:>15} |")
    print(f"{'-'*43:^45}")
    print()
