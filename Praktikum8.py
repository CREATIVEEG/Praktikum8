#Rhendy Diki Nugraha
class mahasiswa():
    def __init__(self, nama, nim, tugas, uts, uas):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def tambah(self, nama, nim, tugas, uts, uas):
        data.nama.append(nama)
        data.nim.append(nim)
        data.tugas.append(tugas)
        data.uts.append(uts)
        data.uas.append(uas)

    def lihat(self):
        for i in range(len(data.nama)):
            print("|", i + 1, "  |", end="")
            print('{0:<25}'.format(self.nama[i]), end=" ")
            print("|", self.nim[i], end="")
            print(" |", self.tugas[i], end="")
            print("    |", self.uts[i], end="")
            print("  |", self.uas[i], " | ", end="")
            print(f'{((self.tugas[i] * 30 / 100) + (self.uts[i] * 35 / 100) + (self.uas[i] * 35 / 100)) :.2f}', " |")

    def hapus(self):
        del self.nama[no]
        del self.nim[no]
        del self.tugas[no]
        del self.uts[no]
        del self.uas[no]

    def ubah(self, nama, nim, tugas, uts, uas):
        self.nama[no] = nama
        self.nim[no] = nim
        self.tugas[no] = tugas
        self.uts[no] = uts
        self.uas[no] = uas

data = mahasiswa([],[],[],[],[])

while True:
    print("\nPilih menu dibawah, untuk menjalankan program ini.")
    menu = input("(T)ambah, (L)ihat, (H)apus, (U)bah, (K)eluar : ")
    if menu == "t" or menu == "T":
        print("\nTambahkan Data Mahasiswa")
        print("==================================================")
        data.tambah(
            input("Masukkan Nama : "),
            input("Masukkan NIM  : "),
            int(input("Nilai Tugas : ")),
            int(input("Nilai UTS   : ")),
            int(input("Nilai UAS   : "))
        )
        print("\nData berhasil ditambahkan")

    elif menu == "l" or menu == "L":
        print("\nMenampilkan data Mahasiswa")
        print("===========================================================================")
        print("|  No |          Nama            |    NIM    | TUGAS | UTS | UAS |  AKHIR |")
        print("===========================================================================")
        if len(data.nama) != 0:
            data.lihat()
        else:
            print("|                        TIDAK ADA DATA                                   |")
        print("===========================================================================")

    elif menu == "h" or menu == "H":
        print("\nMenghapus data Mahasiswa")
        print("==================================================")
        hapus = input("Masukkan Nama : ")
        if hapus in data.nama:
            no = data.nama.index(hapus)
            data.hapus()
            print("Data ", hapus, " berhasil dihapus")
        else:
            print("Nama ", hapus, " tidak terdaftar")

    elif menu == "u" or menu == "U":
        print("\nMengubah data Mahasiswa")
        print("==================================================")
        ubah = input("Masukkan Nama : ")
        if ubah in data.nama:
            no = data.nama.index(ubah)
            print("Masukkan Data Yang Baru : ")
            data.ubah(
                input("Nama : "),
                input("NIM  : "),
                int(input("Nilai Tugas : ")),
                int(input("Nilai UTS   : ")),
                int(input("Nilai UAS   : "))
            )
        else:
            print("Nama ", ubah, " tidak terdaftar")

    elif menu == "k" or menu == "K":
        print("\nAnda telah berhasil keluar dari program.\n")
        break

    else:
        print("\nMenu pilihan yang dimasukkan tidak ada")
        print("Masukkan pilihan yang valid!")