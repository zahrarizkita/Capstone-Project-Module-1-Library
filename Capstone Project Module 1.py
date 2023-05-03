# Capstone Project Module 1 
# Nama    : Zahra Rizkita Putri
# Kelas   : JCDS-2004 On Campus Jakarta 
# Tema    : Program Pendataan Buku Perpustakaan dan Bisa Pinjam

import datetime

ListPerpus = [{
        'Nomor' : 101,
        'Judul' : 'Dune',
        'Penulis' : 'Frank Herbert',
        'Terbit' : 1965,
        'Jenis' : 'Novel Sci-Fi'
    },
    {
        'Nomor' : 102,
        'Judul' : 'Pokemon Adventures',
        'Penulis' : 'Hideori Kusaka',
        'Terbit' : 1997,
        'Jenis' : 'Komik'
    },
    {
        'Nomor' : 103,
        'Judul' : 'The Asian Kitchen',
        'Penulis' : 'Kong Foong lin',
        'Terbit' : 2014,
        'Jenis' : 'Buku Resep'
    },
    {
        'Nomor' : 104,
        'Judul' : 'Mr Standfast, A Novel',
        'Penulis' : 'John Buchan',
        'Terbit' : 2016,
        'Jenis' : 'Novel Thriller'
    },
    {
        'Nomor' : 105,
        'Judul' : 'The NY Magz Book Of Cartoon',
        'Penulis' : 'The W Magazine',
        'Terbit' : 2001,
        'Jenis' : 'Majalah'
    }]

ListPerpusBaru = ListPerpus.copy ()

# memasukkan nomor buku sebagai input
def NomorSebagaiInput():
    while True :
        global Nomor
        Nomor = input('    Masukkan Nomor Buku : ')
        if Nomor.isdigit() == True :
            Nomor = int(Nomor)
            break
        print('!!!!!! Menu yang Dimasukkan Adalah Angka !!!!!!')

# memasukkan tahun sebagai input
def InputTahun():
    while True :
        global Terbit
        Terbit = input('    Masukkan Tahun Terbit Buku : ')
        if Terbit.isdigit() == True :
            Terbit = int(Terbit)
            break
        else :
            print('!!!!!! Input yang Dimasukkan Adalah Angka !!!!!!')

# memasukkan umur sebagai input
def InputUmur():
    while True :
        global Umur
        Umur = input('    Masukkan Umur Anda : ')
        if Umur.isdigit() == True :
            Umur = int(Umur)
            break
        print('!!!!!! Input yang Dimasukkan Adalah Angka !!!!!!')

#masukkan tanggal untuk pinjam buku
def TanggalPinjam(date_str): 
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False
    
# menampilkan daftar buku yang ada di perpustakaan
def TampilkanDaftarBuku() :
    print('''

    Menu Untuk Tampilkan Daftar Buku :

    1. Seluruh Buku yang Tersedia
    2. Mencari Buku Tertentu Berdasarkan Nomor
    3. Kembali Ke Menu Utama

    ''')
    
    MenuParsial = input('    Pilihlah Sub Menu [1-3]: ')
    
    if MenuParsial == '1' :
        if len(ListPerpusBaru) == 0 :
            print('!!!!!! Data Tidak Tersedia !!!!!!')
            TampilkanDaftarBuku()

        else :
            print('\n    Daftar Buku :')
            for i, Update in enumerate(ListPerpusBaru) :
                print(f"\t{i + 1}. Nomor : {Update['Nomor']}, Judul : {Update['Judul']}, Penulis : {Update['Penulis']}, Terbit : {Update['Terbit']}, Jenis : {Update['Jenis']}")
            TampilkanDaftarBuku() 

    elif MenuParsial == '2' :
        if len(ListPerpusBaru) == 0 :
            print('!!!!!! Data Tidak Tersedia !!!!!!')
            TampilkanDaftarBuku()

        else :
            NomorSebagaiInput()
            for Update in ListPerpusBaru :
                if Update['Nomor'] == Nomor :
                    print(f'   Data Buku dengan Nomor {Nomor}')
                    print(f"    1. Nomor : {Update['Nomor']}, Judul : {Update['Judul']}, Penulis : {Update['Penulis']}, Terbit : {Update['Terbit']}, Jenis : {Update['Jenis']}")
                    break

            if Update['Nomor'] != Nomor :
                print('!!!!!! Data Tidak Tersedia !!!!!!')
            TampilkanDaftarBuku() 

    elif MenuParsial == '3' :
        ProgramPerpustakaan()
    else :
        print('!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
        TampilkanDaftarBuku()

# tampilkan detail buku : nomor buku, judul, penulis, tahun terbit, genre/jenis : komik novel dll

def AddDataBuku () :
# tambah buku dengan detail : nomor buku, judul, penulis, tahun terbit, genre/jenis : komik novel dll
    print('''

    Menu Untuk Menambah Daftar Buku :

    1. Tambahkan Daftar Buku
    2. Kembali Ke Menu Utama
   

    ''')
    
    MenuParsial = input('    Pilihlah Sub Menu [1-2]: ')
    
    if MenuParsial == '1' :
        NomorSebagaiInput()
        for Update in ListPerpusBaru :
            if Update['Nomor'] == Nomor :
                print("<<<<<< Data Anda Sudah Tersimpan>>>>>>")
                break

        if Update['Nomor'] != Nomor :
            Judul = input('    Masukkan Judul Buku : ')
            Penulis = input('    Masukkan Nama Penulis Buku : ')
            InputTahun()
            Jenis = input('    Masukkan Jenis Buku : ')

            simpan = input('    Apakah Data Akan Disimpan? (Y/N) : ').upper()

            if simpan == 'Y' :
                ListPerpusBaru.append(
                {
                    'Nomor': Nomor, 
                    'Judul': Judul, 
                    'Penulis': Penulis, 
                    'Terbit': Terbit, 
                    'Jenis': Jenis
                }
                )
                print('<<<<<< Data Anda Sudah Tersimpan>>>>>>')
        AddDataBuku()

    elif MenuParsial == '2' :
        ProgramPerpustakaan()

    else :
        print('!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
        AddDataBuku()

def DeleteDataBuku () :
# delete buku
    print('''

    Menu Untuk Menghapus Daftar Buku :

    1. Hapus Data
    2. Kembali Ke Menu Utama
    
    ''')
    
    MenuParsial = input('    Pilihlah Sub Menu [1-2]: ')
    
    if MenuParsial == '1' :
        NomorSebagaiInput()
        for j, Update in enumerate(ListPerpusBaru) :
            if Update['Nomor'] == Nomor :
                Delete = input('    Apakah Data Akan Dihapus (Y/N) : ').upper()
                if Delete  == 'Y' :
                    del ListPerpusBaru[j]
                    print('<<<<<< Data Anda Sudah Terhapus >>>>>>')
                break

        if Update['Nomor'] != Nomor :
            print('!!!!!! Data Tidak Tersedia !!!!!!')
        DeleteDataBuku()

    elif MenuParsial == '2' :
        ProgramPerpustakaan()

    else :
        print('!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
        DeleteDataBuku()

def UpdateDataBuku () :
# mengubah salah satu data di data detail buku
    print('''

    Menu Untuk Mengubah Data Buku :

    1. Ubah Data Buku
    2. Kembali Ke Menu Utama
    

    ''')
    
    MenuParsial = input('    Pilihlah Sub Menu [1-2]: ')
    
    if MenuParsial == '1' :
        NomorSebagaiInput()
        NomorPertama = Nomor
        Informasi = ''
        for Update in ListPerpusBaru :
            if Update['Nomor'] == NomorPertama :
                print(f"    1. Nomor : {Update['Nomor']}, Judul : {Update['Judul']}, Penulis : {Update['Penulis']}, Terbit : {Update['Terbit']}, Jenis : {Update['Jenis']}")
                
                # melanjutkan proses update               
                ContinueUpdate = input('    Apakah Anda Yakin Akan Mengubah Data Buku (Y/N) : ').upper()
                if ContinueUpdate == 'Y' :
                    Informasi = input('    Pilihlah Kategori yang Akan Anda Ubah [Pilihan : Nomor, Judul, Penulis, Terbit, Jenis]: ')
                    if Informasi in ListPerpusBaru[0].keys() :
                        if Informasi == 'Nomor':
                            NomorSebagaiInput()
                            NomorBaru = Nomor

                            # memastikan tidak ada duplikat
                            ListNomor = [Update['Nomor'] for Update in ListPerpusBaru]
                            while NomorBaru in ListNomor :
                                print("<<<<<< Nomor yang Anda Masukkan Sudah Terpakai >>>>>>")
                                NomorSebagaiInput()
                                NomorBaru = Nomor

                        else :
                            NomorBaru = input(f'    Masukkan {Informasi} baru : ')
                        
                        # tanya sekali lagi 
                        update = input('    Apakah Anda Yakin Akan Data yang Diubah (Y/N) : ').upper()
                        if update == 'Y' :
                            Update[Informasi] = NomorBaru
                            print('<<<<<< Data Anda Sudah Terbarui >>>>>>')
                    else :
                        print('!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
                break
        if Informasi != 'Nomor' :
            if Update['Nomor'] != NomorPertama :
                print('!!!!!! Data Tidak Tersedia !!!!!!')
                UpdateDataBuku()

    elif MenuParsial == '2' :
        ProgramPerpustakaan()

    else :
        print('!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
        UpdateDataBuku()

def PinjamBuku () :
# hanya terbatas untuk pinjam 1 buku
    print('''

    Menu Untuk Meminjam Buku :

    1. Pinjam Sebuah Buku
    2. Kembali Ke Menu Utama
    

    ''')
    
    MenuParsial = input('    Pilihlah Sub Menu [1-2]: ')
    
    if MenuParsial == '1' :
        NomorSebagaiInput()
        for Update in ListPerpusBaru :
            if Update['Nomor'] == Nomor :
                Nama = input('    Masukkan Nama Anda : ')
                InputUmur()
                Instansi = input('    Masukkan Instansi Anda : ')
                
                while True:
                    Tanggal = str(input('    Tanggal Hari ini : '))
                    if not TanggalPinjam(Tanggal):
                        print("!!!!!! Input yang Anda Masukkan Salah, Silahkan Input Kembali Tanggal Pinjam Dengan Format 'dd-mm-yyyy' !!!!!!")
                        continue
                    break

                print(f'''    Anda Telah Memilih Untuk Meminjam Buku Nomor {Nomor}
                1. Nomor : {Update['Nomor']}, Judul : {Update['Judul']}, Penulis : {Update['Penulis']}, Terbit : {Update['Terbit']}, Jenis : {Update['Jenis']}
                            Biodata Anda Telah Tersimpan Sebagai Peminjam :
                            Nama              : {Nama}
                            Umur              : {Umur}
                            Instansi          : {Instansi}
                            Tanggal Hari ini  : {Tanggal}
                            Terima Kasih Anda Telah Bertransaksi di THE LIBRARY
                            Silahkan Kembalikan Buku yang Anda Pinjam Dalam Rentang Waktu 14 Hari Setelah Waktu Pinjam
                ''')
                break

    elif MenuParsial == '2' :
        ProgramPerpustakaan()

    else :
        print('!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
        PinjamBuku()

def ProgramPerpustakaan () :
# tampilkan menu buku : data buku, tambah buku, delete buku, update buku, pinjam buku, keluar
    while True :
        MenuSelection = input('''

            :::::::::::::::::: Welcome to THE LIBRARY ::::::::::::::::::

            Daftar Menu yang Dapat Dipilih:

            1. Daftar Buku Di Perpustakaan
            2. Menambahkan Data Buku 
            3. Menghapus Data Buku
            4. Mengubah/Mengupdate Data Buku
            5. Meminjam Buku
            6. Keluar Dari Program
            
            Pilihlah Sebuah Nomor Dari Daftar Menu : ''')

        if(MenuSelection == '1') :
            TampilkanDaftarBuku()
            break

        elif(MenuSelection == '2') :
            AddDataBuku()
            break

        elif(MenuSelection == '3') :
            DeleteDataBuku()
            break

        elif(MenuSelection == '4') :
            UpdateDataBuku()

        elif(MenuSelection == '5') :
            PinjamBuku()
            break

        elif(MenuSelection == '6') :
            print('    Terima Kasih Anda Telah Bertransaksi di THE LIBRARY')
            break

        else : 
            print('!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
            ProgramPerpustakaan()

ProgramPerpustakaan()