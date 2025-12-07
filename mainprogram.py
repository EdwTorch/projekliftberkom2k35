"""Nama Program: Sistem dalam Perpustakaan 

Nama/NIM Anggota Kelompok:
Khasya Nurul Amini/19625007
Kezia Josephine Manik/19625015
Raya Medina Farrelin/19625183
Edward Terrance Lie/19625187

Deskripsi Program : 
Program ini merupakan sistem perpustakaan sederhana yang memungkinkan pengguna mencari buku, meminjam, dan mengembalikannya. 
Seluruh proses seperti pengecekan stok, pencatatan peminjaman, perhitungan denda, 
hingga pembayaran ditangani otomatis oleh program, dengan data disimpan dan diperbarui melalui file JSON.

Kamus : 
database_buku = nested dictionary of array of dictionary
database_peminjamanbuku = nested dictionary of array of dictionary
datagenre = array of string
list_jumlahbuku = nested array of array int and string
page = int
genre = str
judul_pinjaman = str
lastindex = int
programselesai = boolean
state = str
cek_genre = boolean
validasi_genre = boolean
formattgl = class of datetime.datetime
tgl_hariini = str
pagelokal = int
pilihan =  int
"""
import json
from datetime import datetime
from datetime import timedelta
#contoh : 
database_buku = {}
database_peminjamanbuku = {}
datagenre = ["" for i in range (5)]
list_jumlahbuku = [["",0] for i in range(5)]
page = 1
genre = ""
judulpinjaman = ""
lastindex = 0
def access_and_read_json():
    """
    Kamus Lokal : 
    fileinput = class
    """
    global database_buku
    global list_jumlahbuku

    try:
        with open(f"Database_buku.json", "r") as fileinput:
            database_buku = json.load(fileinput)
            
    except FileNotFoundError: 
        print("Salah kode")

def save_peminjaman(files):
    """
    Kamus Lokal :
    filesavepinjaman = class
    filedatabase = class
    """
    global database_buku
    with open(f"database_peminjaman.json","w") as filesavepeminjaman:
        json.dump(files,filesavepeminjaman, indent=4)
    with open(f"Database_buku.json","w") as filedatabase:
        json.dump(database_buku,filedatabase, indent=4)

def access_peminjaman():
    """
    Kamus Lokal :
    filepinjam = class
    """
    global database_peminjamanbuku
    with open(f"database_peminjaman.json","r") as filepinjam:
        database_peminjamanbuku = json.load(filepinjam)
        
def cek_genre_buku_pinjaman(): 
    global judulpinjaman
    global database_buku
    global genrebuku 
    global genre
    """ 
    Kamus Lokal :
    cek_judul = boolean
    genre = str
    daftarbuku = array of dictionary
    buku = str
    genrebuku = str
    """
    cek_judul = False

    for genre, daftarbuku in database_buku.items(): #ngecek genre buku
        for buku in daftarbuku:
            if judulpinjaman.upper() == buku["Judul"].upper():
                cek_judul = True
                genrebuku = genre
    if cek_judul == True:
        print(f"Buku '{judulpinjaman} termasuk kedalam genre: {genrebuku}")
        return True
    else: 
        print("Buku tidak ada dalam koleksi")
        return False

def pengembalian_buku(): #Pengembalian Buku dan Kondisi buku diinput manual 
    global database_peminjamanbuku
    global judulpinjaman
    global formattgl
    """
    Kamus Lokal :
    validasinama = boolean
    cek_nama = boolean
    j = int
    namapeminjam = str
    namapinjam = str
    tgl_peminjaman = str
    tgl_peminjamanformat = class of datetime.datetime
    tgl_pengembalian = class of datetime.datetime
    tgl_pengembalian_str = str
    tgl_pengembalianformat = class of datetime.datetime
    kondisi = str
    bukuada = boolean
    dendarusak = int
    deltahariint = int
    deltahari = class of timedela
    pengembalian_selesai = dictionary
    found = Boolean
    daftar = array of dictionary
    genrebukuyangdicari = dictionary of array
    found_genre = str
    found_index =int
    """
    validasinama = False
    cek_nama = False
    j = 0

    #Cari nama peminjam
    while validasinama == False:
        namapeminjam = input("Masukkan nama peminjam : ")
        while cek_nama == False and j < len(database_peminjamanbuku["listpeminjambuku"]):
            if namapeminjam == (database_peminjamanbuku["listpeminjambuku"][j]["nama"]):
                cek_nama = True
            else:
                j+= 1
        if cek_nama == True:
            validasinama = True
        else:
            print("Nama peminjam tidak ditemukan.")
            j = 0

    #Menampilkan data pinjaman peminjam
    print("Data Pinjaman:\n")
    print("=======================================================") 
    print("{:<10} {:<10} {:<15} {:<15}".format("NAMA", "JUDUL", "TGL PEMINJAMAN", "TGL PENGEMBALIAN "))
    print("=======================================================")

    namapinjam = (database_peminjamanbuku["listpeminjambuku"][j]["nama"])
    judulpinjaman = (database_peminjamanbuku["listpeminjambuku"][j]["judul"])
    tgl_peminjam = (database_peminjamanbuku["listpeminjambuku"][j]["tgl_peminjam"])
    tgl_peminjamformat = datetime.strptime(tgl_peminjam, "%d-%m-%Y")
    tgl_pengembalian = tgl_peminjamformat + timedelta(days=7)
    tgl_pengembalian_str = tgl_pengembalian.strftime("%d-%m-%Y")
    tgl_pengembalianformat = datetime.strptime(tgl_pengembalian_str,"%d-%m-%Y")
    print(f"{namapinjam:<10} {judulpinjaman:<10} {tgl_peminjam:^15} {tgl_pengembalian_str:^15}\n")
    
    kondisi = input("Masukkan kondisi buku yang dikembalikan (BAIK/RUSAK): ").upper()
    if formattgl <= tgl_pengembalianformat and kondisi != "RUSAK" : #Kondisi ideal
        print("Pengembalian buku tepat waktu dan kondisi buku baik.")
        print("Pengembalian buku selesai")

    elif formattgl <= tgl_pengembalianformat and kondisi == "RUSAK": #kondisi tidak terlambat tapi rusak
        print("Pengembalian buku tepat waktu. Namun kondisi buku rusak")
        bukuada = cek_genre_buku_pinjaman()
        if bukuada == True: 
            if genrebuku == "TEXTBOOK":
                dendarusak = 70000
            elif genrebuku == "NOVEL":
                dendarusak = 80000
            elif genrebuku == "ANAK":
                dendarusak = 50000
            elif genrebuku == "ENSIKLOPEDIA":
                dendarusak = 100000
            else:
                dendarusak = 50000
            print(f"Anda dikenakan denda sebesar Rp{dendarusak}")
            pembayaran(namapinjam,judulpinjaman,tgl_peminjam,tgl_pengembalian_str,0,0,dendarusak,dendarusak)
        else:
            print("Database bermasalah")
            exit()

    elif formattgl >= tgl_pengembalianformat and kondisi == "RUSAK": #kondisi terlambat dan rusak
        deltahari = formattgl - tgl_pengembalianformat
        print(f"Anda terlambat mengembalikan buku selama {deltahari.days} hari dan kondisi buku rusak.")
        deltahariint = deltahari.days
        denda_telat = 2000 * deltahariint
        bukuada = cek_genre_buku_pinjaman()
        if bukuada == True:
            if genrebuku == "TEXTBOOK":
                dendarusak = 70000
            elif genrebuku == "NOVEL":
                dendarusak = 80000
            elif genrebuku == "ANAK":
                dendarusak = 50000
            elif genrebuku == "ENSIKLOPEDIA":
                dendarusak = 100000
            else:
                dendarusak = 50000
            totaldenda = denda_telat + dendarusak
            print(f"Anda dikenakan denda sebesar Rp{totaldenda}")
            pembayaran(namapinjam,judulpinjaman,tgl_peminjam,tgl_pengembalian_str,deltahariint,denda_telat,dendarusak,totaldenda)
        else: 
            print("Database bermasalah")
            exit()
    else: #kondisi hanya terlambat
        deltahari = formattgl - tgl_pengembalianformat
        print(f"Anda terlambat mengembalikan buku selama {deltahari.days} hari.")
        deltahariint = deltahari.days
        denda = 2000 * deltahariint
        print(f"Anda dikenakan denda sebesar Rp{denda}")
        pembayaran(namapinjam,judulpinjaman,tgl_peminjam,tgl_pengembalian_str,deltahariint,denda,0,denda)
    

    found = False
    while found == False: #nyari genre dan index buku nya
        for genrebukuyangdicari, daftar in database_buku.items():
            i = 0
            while i < len(daftar):
                buku = daftar[i]
                if buku.get("Judul").upper() == judulpinjaman.upper():
                    found = True 
                    found_genre = genrebukuyangdicari
                    found_index = i
                i += 1
    database_buku[found_genre][found_index]["Jumlah"] +=1
    database_peminjamanbuku["listpeminjambuku"][j] = {
        
    }
    geserisi(j) #fungsi remove
    database_peminjamanbuku["lastindex"] -=1
    save_peminjaman(database_peminjamanbuku)

def geserisi(kosongke):
    global database_peminjamanbuku
    """ 
    Kamus Lokal :
    i = int 
    kosongke = int
    """
    i= kosongke
    while i<database_peminjamanbuku["lastindex"]:
        database_peminjamanbuku["listpeminjambuku"][i] = database_peminjamanbuku["listpeminjambuku"][i+1]
        i+=1
    
def pembayaran(nama,judul,tgl_pinjam,tgl_deadline,terlambat,denda_telat,denda_rusak,total_denda):
    global database_peminjamanbuku
    global database_buku 
    global formattgl 
    global judulpinjaman 
    """ 
    Kamus Lokal : 
    nama = str
    judul = str
    tgl_pinjam = str
    tgl_deadline = str
    terlambat = str
    denda_telat= int
    denda_rusak = int
    total_denda = int
    valid = boolean
    kembalian = int
    bayar = str
    bayar_int = int
    
    """
    print("\n===== RINCIAN PEMBAYARAN =====")
    print(f"Nama Peminjam       : {nama}")
    print(f"Judul Buku          : {judul}")
    print(f"Tanggal Pinjam      : {tgl_pinjam}")
    print(f"Tenggat Pengembalian: {tgl_deadline}")
    print(f"Terlambat           : {terlambat} hari")
    print(f"Denda Telat         : Rp{denda_telat}")
    print(f"Denda Kerusakan     : Rp{denda_rusak}")
    print(f"TOTAL PEMBAYARAN    : Rp{total_denda}")
    print("================================")

    valid = False 
    while valid == False: #Pembayaran
        bayar = input("Masukkan nominal pembayaran: ")
        if bayar.isdigit():
            bayar_int = int(bayar)
            if bayar_int >= total_denda:
                valid = True 
            else: 
                print("Nominal kurang. Lakukan pembayaran kembali.")
        else: 
            print("Input tidak valid. Masukkan angka.")
    
    kembalian = bayar_int - total_denda

    print("\n===== PEMBAYARAN SELESAI =====")
    print(f"Total Denda : Rp{total_denda}")
    print(f"Uang Dibayar: Rp{bayar_int}")
    print(f"Kembalian   : Rp{kembalian}")
    print("================================")


def tampilkan_genre(datagenre):
    global database_buku
    """ 
    Kamus Lokal : 
    i = int
    """
    print("Berikut adalah genre yang tersedia: ")
    for i in range(len(datagenre)): #Nampilin Genre
        print(f"{i+1}. {datagenre[i]} ")

def tampilandanketersediaan_buku(genre, page_lokal, indexgenre,database,jmlbuku): 
    """  
    Kamus Lokal : 
    input_ulang_valid = str
    totalbukusaatini = int
    i = int
    state = int
    counttotalbuku = int
    genre = str
    page_lokal = int
    index_genre = int
    database = dictionary of array of dictionary
    jmlbuku = nested list of str and int
    
    """
    input_ulang_valid = "False"
    totalbukusaatini = jmlbuku[indexgenre][1]
    i =0
    listbuku = [["",0]for i in range(totalbukusaatini)]
    for i in range(totalbukusaatini): #salin databasebuku dengan genre yg sudah diinput ke listbuku
        listbuku[i][0] = database[genre][i]["Judul"]
        listbuku[i][1] = database[genre][i]["Jumlah"]
    
    state = 0 
    #page dibagi 2 untuk menampilkan list buku
    if page_lokal == 1:
        counttotalbuku = totalbukusaatini//2
        for i in range(counttotalbuku):
            print(f"{i+1}. {listbuku[i][0]} tersedia sejumlah {listbuku[i][1]}\n\n")


    else: 
        counttotalbuku = totalbukusaatini - totalbukusaatini//2
        for i in range(counttotalbuku,totalbukusaatini):
            print(f"{i+1}. {listbuku[i][0]} tersedia sejumlah {listbuku[i][1]}\n\n")


    if page_lokal == 1:
        while input_ulang_valid == "False":
                state = int(input(f"Apakah anda ingin melihat daftar lanjutan dari {genre} {counttotalbuku+1}-{totalbukusaatini}? (ketik 0 untuk tidak, 1 untuk ya) : "))
                if state == 0 or state == 1:
                    input_ulang_valid = "True"
                else:
                    print("Masukkan tidak valid tolong masukkan ulang")
                    
    if state == 1:
        page_lokal +=1
        tampilandanketersediaan_buku(genre, page_lokal, indexgenre,database_buku,list_jumlahbuku)

    elif state == 0:
        return

def add_peminjaman_buku():
    global database_buku 
    global database_peminjamanbuku
    global formattgl
    global judulpinjaman
    global lastindex
    """ 
    Kamus Lokal : 
    found = boolean
    found_stok = boolean
    found_genre = str
    found_index = int
    judul = str
    judulpinjaman = str
    genrebukuyangdicari = str
    daftar = list of dictionary
    buku = dictionary
    lihatjudul = int
    tgl_str = str
    tgl_balik = str
    new_record = dictionary
    """
    #Input nama peminjam dan judul buku 
    nama = input("Masukkan nama peminjam: ").strip()
    found = False 
    found_genre = ""
    found_index = 0
    while found == False:
        judul = input("Masukkan judul buku: ").strip()
        judulpinjaman = judul
        found_stok = True
        #Mencari judul buku yang ingin dipinjam 
        for genrebukuyangdicari, daftar in database_buku.items():
            i = 0
            while i < len(daftar):
                buku = daftar[i]
                if buku.get("Judul").upper() == judul.upper():
                    found = True 
                    found_genre = genrebukuyangdicari
                    found_index = i
                i += 1

        if found == False: 
            print(f"Buku dengan judul '{judul}' tidak ditemukan dalam database.")
            found_stok = False
        elif found == True:
            jumlah = database_buku[found_genre][found_index].get("Jumlah", 0)
            if jumlah == 0:
                print(f"Maaf, stok buku '{judul}' sedang habis. Silahkan pinjam buku lain")
                found_stok = False
                found = False
        
        if found_stok == False: #Liat list judul
            lihatjudul = int(input("Lihat daftar judul buku ? (Masukkan 1 jika ya, 0 jika tidak) : "))
            if lihatjudul == 0: 
                print()
            elif lihatjudul ==1: 
                searchbuku()
    
    if not ("listpeminjambuku" in database_peminjamanbuku):
        database_peminjamanbuku["listpeminjambuku"] = []
    
    if isinstance(formattgl, datetime):
        tgl_str = formattgl.strftime("%d-%m-%Y")
        tgl_balik = (formattgl + timedelta(days=7)).strftime("%d-%m-%Y")    
    if found_stok == True:
        new_record = {
            "nama": nama, 
            "judul": judul,
            "tgl_peminjam": tgl_str,
            "tgl_balik" : tgl_balik
        }
        database_peminjamanbuku["listpeminjambuku"][lastindex] = new_record
        database_peminjamanbuku["lastindex"]+=1
        #Mengurangi stok buku 
        database_buku[found_genre][found_index]["Jumlah"] = jumlah - 1
        print("")
        save_peminjaman(database_peminjamanbuku)
        print("===============================================")
        print(f"Nama Peminjam : {nama}")
        print(f"Judul Buku    : {judul}")
        print(f"Tanggal Pinjam: {tgl_str}")
        print(f"Tanggal Pengembalian : {tgl_balik}")
        print("===============================================")


    
def status_peminjaman_buku(): 
    global database_buku 
    global database_peminjamanbuku
    """ 
    Kamus Lokal : 
    isipinjam = boolean
    i = int
    nama = str
    judul = str
    tanggal_peminjam = str
    tanggal_peminjam1 = class of datetime.datetime
    tanggal_pengembalian1 = str
    tanggal_pengembalian = class of datetime.datetime
    """
    if len(database_peminjamanbuku["listpeminjambuku"]) == 0: #baca database peminjam 
        print("[Data tidak tersedia]")
    else: 
        print("=======================================================") 
        print("{:<10} {:<10} {:<15} {:<15}".format("NAMA", "JUDUL", "TGL PEMINJAMAN", "TGL PENGEMBALIAN ")) #Format
        print("=======================================================")
        i=0
        isipinjam = True
        while i< (len(database_peminjamanbuku["listpeminjambuku"])) and isipinjam == True:
            if database_peminjamanbuku["listpeminjambuku"][i]=={}:
                isipinjam = False
            else:
                nama = (database_peminjamanbuku["listpeminjambuku"][i]["nama"])
                judul = (database_peminjamanbuku["listpeminjambuku"][i]["judul"])
                tanggal_peminjam = (database_peminjamanbuku["listpeminjambuku"][i]["tgl_peminjam"])
                #menghitung tanggal pengembalian
                tanggal_peminjam1 = datetime.strptime(tanggal_peminjam, "%d-%m-%Y")
                tanggal_pengembalian = tanggal_peminjam1 + timedelta(days=7)
                tanggal_pengembalian1 = tanggal_pengembalian.strftime("%d-%m-%Y")

                print(f"{nama:<10} {judul:<10} {tanggal_peminjam:^15} {tanggal_pengembalian1:^15}")
            i+=1


def searchbuku():
    global database_buku
    global datagenre 
    global list_jumlahbuku
    global genre
    """ 
    pilihan_pencarian = str
    indexgenre = int
    page_lokal = int
    keyword = str
    k = int
    searchketemu = boolean
    namagenre = str
    listbuku = nested list 
    satubuku = list
    lihatdaftar = str
    selesailooptampilan = boolean
    validasi_lanjut = int
    """
    j=0
    print("1. Cari berdasarkan genre")
    print("2. Cari berdasarkan judul")
    pilihan_pencarian = input("Masukkan pilihan (1/2): ")

    #Pencarian berdasarkan genre 
    if (pilihan_pencarian == "1"): #Cari berdasarkan genre
        tampilkan_genre(datagenre)
        
        pilih_genre, indexgenre=prosedur_validasi_genre()
        print()
        print(f"Daftar Buku dalam Genre {pilih_genre}")
        indexgenre = j 
        page_lokal = 1
        tampilandanketersediaan_buku(pilih_genre, page_lokal, indexgenre,database_buku,list_jumlahbuku)

    #Pencarian berdasarkan judul 
    elif (pilihan_pencarian == "2"): 
        keyword = input("Masukkan keyword judul: ").upper().strip()
        k = 0
        searchketemu = False
        for indexgenre, namagenre in enumerate(datagenre):
            listbuku = [[] for i in range(list_jumlahbuku[indexgenre][1])]
            while k<len(database_buku[namagenre]):
                satubuku = [isibuku for isibuku in database_buku[namagenre][k].values()]
                listbuku[k] = satubuku
                k+=1
            for j in range(len(listbuku)):
                if keyword in listbuku[j][0].upper():
                    print(f"Buku ditemukan pada genre {namagenre} dengan judul {listbuku[j][0]} dengan ketersediaan {listbuku[j][1]}")
                    searchketemu = True
                elif keyword in listbuku[j][0].upper() and searchketemu == True:
                    print()
    
            k = 0
        if searchketemu == False:            
            print(f"\nBuku dengan judul '{keyword}' tidak ditemukan")
            lihatdaftar = input("Apakah Anda ingin melihat daftar buku per genre? (ketik 0 untuk tidak, 1 untuk ya) : ")

            if lihatdaftar != "1":
                print("Pencarian selesai")
                return 
            
            indexgenre=0
            selesailooptampilan = False
            while indexgenre <5 and selesailooptampilan == False:
                print(f"Genre {datagenre[indexgenre]}")
                tampilandanketersediaan_buku(datagenre[indexgenre],1,indexgenre,database_buku,list_jumlahbuku)
                validasi_lanjut = int(input("Apakah anda ingin melihat genre selanjutnya? (0 untuk tidak, 1 untuk iya) : "))
                if validasi_lanjut == 1: 
                    indexgenre+=1
                elif validasi_lanjut ==0:
                    selesailooptampilan = True
    else: 
        return
        
        
def next_action():
    global datagenre
    global database_buku
    global list_jumlahbuku
    """ 
    pilihan = int
    """
    pilihan=int(input("Apakah ada hal yang ingin dilakukan lagi? (Iya ketik 1, tidak ketik 0): "))
    if pilihan== 1:
        return "Ulang"
    elif pilihan== 0:
        print("Terima kasih telah menggunakan program ini!")
        return 0
    else:
        print("Input tidak valid, masukkan angka 0/1")
        next_action()
def prosedur_validasi_genre():
    
    """
    j = int
    validasi_genre = boolean
    cek_genre = boolean
    genre = str
    """
    j = 0 
    validasi_genre = False
    cek_genre = False
    while validasi_genre == False: 
        genre = input("Masukkan nama genre: ")
        genre = genre.upper()
        while cek_genre == False and j < len(datagenre): 
            if (genre == datagenre[j]): 
                cek_genre = True
            else: 
                j += 1

        if (cek_genre == True): 
            validasi_genre = True 
        else:
            j = 0 
            print("Genre tidak ditemukan")
            
    return genre,j
    

programselesai = False
access_and_read_json()
access_peminjaman()
pagelokal= page
#jangan lupa input tanggal
tgl_hariini = input("Masukkan tanggal hari ini dengan format 'hari-bulan-tahun': ")
formattgl = datetime.strptime(tgl_hariini, "%d-%m-%Y")
datagenre = [key for key in database_buku]
validasi_genre = False
cek_genre = False
list_jumlahbuku = [[datagenre[i],0] for i in range(len(datagenre))]

for i in range(len(list_jumlahbuku)):
    list_jumlahbuku[i][1] = len(database_buku[datagenre[i]])
state = ""
while programselesai == False:
    lastindex = database_peminjamanbuku["lastindex"]
    print("""Selamat Datang di Program Perpustakaan WI1001
        Halo! Ingin melakukan apa?
        1. Mencari buku
        2. Peminjaman buku
        3. Status peminjaman buku
        4. Pengembalian buku
        5. Ganti tanggal
        6. Exit
        """)
    pilihan=int(input("Masukkan pilihan: "))
    if pilihan==1:
        searchbuku()
        state = next_action()
            
    elif pilihan==2:
        add_peminjaman_buku()
        state= next_action()
            
    elif pilihan==3:
        status_peminjaman_buku()
        state = next_action()
            
    elif pilihan==4:
        pengembalian_buku()
        state= next_action()
            
    elif pilihan==5:
        tgl_hariini = input("Masukkan tanggal hari ini dengan format 'hari-bulan-tahun': ")
        formattgl = datetime.strptime(tgl_hariini, "%d-%m-%Y")
        state = next_action()
    elif pilihan==6: 
        programselesai= True
    else :
        print("Input anda tidak valid, silahkan masukkan input berupa angka dari 1--6")
    if state == "Ulang":
        print()
    else: 
        programselesai = True
