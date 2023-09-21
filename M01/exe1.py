'''
import class buku dari file blueprint.py
'''
from blueprint import Mahasiswa, Dosen, LenData, Person


if __name__ == '__main__':

    obj_mhs = []
    obj_dsn = []
    list_mahasiswa = []
    jlh_mhs = 0
    list_dosen = []
    jlh_dsn = 0

    N = int(input('Jumlah data absensi : '))
    print()

    for i in range(N):
        print(f'Data absensi ke {i + 1}')
        posisi = input('Data Mahasiswa / Dosen? : ').lower()
        if posisi == "mahasiswa":
            nim = input('NIM : ')
            nama = input('Nama : ')
            jurusan = input('Jurusan : ')
            gender = input('Jenis Kelamin : ')
            no_hp = input('No HP : ')
            mahasiswa = Mahasiswa(nim, nama, jurusan, gender, no_hp)
            list_mahasiswa.append(mahasiswa.data())
            obj_mhs.append(mahasiswa)
            jlh_mhs += 1
            print()

        elif posisi == 'dosen':
            nip = input('NIP : ')
            nama = input('Nama : ')
            jabatan = input('Jabatan : ')
            gender = input('Jenis Kelamin : ')
            no_hp = input('No HP : ')
            dosen = Dosen(nip, nama, jabatan, gender, no_hp)
            list_dosen.append(dosen.data())
            obj_dsn.append(dosen)
            jlh_dsn += 1
            print()

    if len(obj_mhs) > 0:
        justify_mhs = LenData(list_mahasiswa)
        m1 = justify_mhs.i_d if justify_mhs.i_d >= 3 else 3
        m2 = justify_mhs.nama if justify_mhs.nama >= 4 else 4
        m3 = justify_mhs.j if justify_mhs.j >= 7 else 7
        m4 = justify_mhs.gender if justify_mhs.gender >= 6 else 6
        m5 = justify_mhs.no_hp if justify_mhs.no_hp >= 5 else 5
        length_mhs = m1+m2+m3+m4+m5+16

        print('Table Data Mahasiswa')
        print('-'*length_mhs)
        print(
            f"| {'NIM':<{m1}} | {'Nama':<{m2}} | {'Jurusan':<{m3}} | {'Gender':<{m4}} | {'No HP':<{m5}} |")
        print('-'*length_mhs)
        for i, data in enumerate(obj_mhs):
            print(
                f"| {data.nim:<{m1}} | {data.nama:<{m2}} | {data.jurusan:<{m3}} | {data.gender:<{m4}} | {data.no_hp:<{m5}} |")
        print('-'*length_mhs)

    print()

    if len(obj_dsn) > 0:
        justify_dsn = LenData(list_dosen)

        d1 = justify_dsn.i_d if justify_dsn.i_d >= 3 else 3
        d2 = justify_dsn.nama if justify_dsn.nama >= 4 else 4
        d3 = justify_dsn.j if justify_dsn.j >= 7 else 7
        d4 = justify_dsn.gender if justify_dsn.gender >= 6 else 6
        d5 = justify_dsn.no_hp if justify_dsn.no_hp >= 5 else 5

        length_dsn = d1+d2+d3+d4+d5+16

        print('Table Data Dosen')
        print('-'*length_dsn)
        print(
            f"| {'NIP':<{d1}} | {'Nama':<{d2}} | {'Jabatan':<{d3}} | {'Gender':<{d4}} | {'No HP':<{d5}} |")
        print('-'*length_dsn)
        for i, data in enumerate(obj_dsn):
            print(
                f"| {data.nip:<{d1}} | {data.nama:<{d2}} | {data.jabatan:<{d3}} | {data.gender:<{d4}} | {data.no_hp:<{d5}} |")
        print('-'*length_dsn)

    print(f'\nJumlah pengunjung : {Person.jml}')
    print(f'Dosen : {jlh_dsn}')
    print(f'Mahasiswa : {jlh_mhs}')
