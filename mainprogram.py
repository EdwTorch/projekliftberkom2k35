"""Nama Program: Sistem dalam Perpustakaan 

Nama/NIM Anggota Kelompok:
Khasya Nurul Amini/19625007
Kezia Josephine Manik/19625015
Raya Medina Farrelin/19625183
Edward Terrance Lie/19625187

Deskripsi Program : 

Kamus : 

"""
import time
import json
from datetime import datetime
from datetime import timedelta
#contoh : 
database_buku = {}
database_peminjamanbuku = {}
datagenre = ["" for i in range (5)]
list_jumlahbuku = [["",0] for i in range(5)]
counter = 1
page = 1
genre = "TEXTBOOK"

def access_and_read_json():
    global database_buku
    global list_jumlahbuku

    try:
        with open(f"Database_buku.json", "r") as fileinput:
            database_buku = json.load(fileinput)
            
    except FileNotFoundError: 
        print("Salah kode")

def save_peminjaman(files):
    with open(f"database_peminjaman.json","w") as filesavepeminjaman:
        json.dump(files,filesavepeminjaman, indent=4)
        
def cek_denda():
    pass

def pembayaran():
    pass

def tampilkan_genre(datagenre):
    global database_buku
    print("Berikut adalah genre yang tersedia: ")
    for i in range(len(datagenre)):
        print(f"{i+1}. {datagenre[i]} ")

 #Status ketersediaan buku dan status buku sisa (per 15 judul) jadi next harus ada 
def tampilandanketersediaan_buku(genre, page_lokal, indexgenre,database,jmlbuku): 
    input_ulang_valid = "False"
    totalbukusaatini = jmlbuku[indexgenre][1]
    i =0
    listbuku = [["",0]for i in range(totalbukusaatini)]
    for i in range(totalbukusaatini):
        listbuku[i][0] = database[genre][i]["Judul"]
        listbuku[i][1] = database[genre][i]["Jumlah"]
    
    state = 0 

    if page_lokal == 1:
        counttotalbuku = totalbukusaatini//2
        for i in range(counttotalbuku):
            print(f"{i+1}. {listbuku[i][0]} tersedia sejumlah {listbuku[i][1]}")
            print()
            print()

    else: 
        counttotalbuku = totalbukusaatini - totalbukusaatini//2
        for i in range(counttotalbuku,totalbukusaatini):
            print(f"{i+1}. {listbuku[i][0]} tersedia sejumlah {listbuku[i][1]}")
            print()
            print()

    if page_lokal == 1:
        while input_ulang_valid == "False":
                state = int(input(f"Apakah anda ingin melihat daftar lanjutan dari {genre} {counttotalbuku+1}-{totalbukusaatini}? (ketik 0 untuk tidak, 1 untuk ya) : "))
                if state == 0 or state == 1:
                    input_ulang_valid = "True"
                else:
                    print("Masukkan tidak valid tolong masukkan ulang")

    if state == 1:
        page_lokal +=1
        tampilandanketersediaan_buku(genre, page_lokal, indexgenre)
        return 

    elif state == 0:
        pass

def add_peminjaman_buku():
    pass

def status_peminjaman_buku(): 
    global database_buku 
    global database_peminjamanbuku

    if len(database_peminjamanbuku["listpeminjambuku"]) == 0: #baca database peminjam 
        print()
        print("[Data tidak tersedia]")
    else: 
        print()
        print("=======================================================") 
        print("{:<10} {:<10} {:<15} {:<15}".format("NAMA", "JUDUL", "TGL PEMINJAMAN", "TGL PENGEMBALIAN ")) #Format
        print("=======================================================")
        i=0
        for i in range (len(database_peminjamanbuku["listpeminjambuku"])):
            nama = (database_peminjamanbuku["listpeminjambuku"][i]["nama"])
            judul = (database_peminjamanbuku["listpeminjambuku"][i]["judul"])
            tanggal_peminjam = (database_peminjamanbuku["listpeminjambuku"][i]["tgl_peminjam"])
            #menghitung tanggal pengembalian
            tanggal_peminjam1 = datetime.strptime(tanggal_peminjam, "%d-%m-%Y")
            tanggal_pengembalian = tanggal_peminjam1 + timedelta(days=7)
            tanggal_pengembalian1 = tanggal_pengembalian.strftime("%d-%m-%Y")

            print(f"{nama:<10} {judul:<10} {tanggal_peminjam:^15} {tanggal_pengembalian1:^15}")

def pengembalian_buku():
    pass

def searchbuku():
    global database_buku
    global datagenre 
    global list_jumlahbuku
    global genre
    validasi_genre = False
    cek_genre = False 

    print("1. Cari berdasarkan genre")
    print("2. Cari berdasarkan judul")
    pilihan_pencarian = input("Masukkan pilihan (1/2): ")

    #Pencarian berdasarkan genre 
    if (pilihan_pencarian == "1"): 
        tampilkan_genre(datagenre)
        
        j = 0 
        while validasi_genre == False: 
            pilih_genre = input("Masukkan nama genre: ")
            pilih_genre = pilih_genre.upper()
            while cek_genre == False and j < len(datagenre): 
                if (pilih_genre == datagenre[j]): 
                    cek_genre = True
                else: 
                    j += 1

            if (cek_genre == True): 
                validasi_genre = True 

            else:
                j = 0 
                print("Genre tidak ditemukan")
        print()
        print(f"Daftar Buku dalam Genre {pilih_genre}")
        indexgenre = j 
        page_lokal = 1
        tampilandanketersediaan_buku(pilih_genre, page_lokal, indexgenre,database_buku,list_jumlahbuku)

    #Pencarian berdasarkan judul 
    elif (pilihan_pencarian == "2"): 
        keyword = input("Masukkan keyword judul: ").upper().strip()
        
        for indexgenre, namagenre in enumerate(datagenre):
            listbuku = [isibuku for isibuku in database_buku[namagenre].values()]

            for buku in listbuku:
                if keyword in buku[0].upper():
                    print(f"Buku ditemukan pada genre {namagenre}")
                    return 
            
        print(f"\nBuku dengan judul '{keyword}' tidak ditemukan")
        lihatdaftar = input("Apakah Anda ingin melihat daftar buku per genre? (ketik 0 untuk tidak, 1 untuk ya) : ")

        if lihatdaftar != "1":
            print("Pencarian selesai")
            return 
            
        for indexgenre, namagenre in enumerate(datagenre):
            print(f"\nGenre {namagenre}")
            tampilandanketersediaan_buku(namagenre, 1, indexgenre)

def redo():
    pass

def next_action():
    global datagenre
    global database_buku
    global list_jumlahbuku
    access_and_read_json()
    pilihan=input(print("Apakah ada hal yang ingin dilakukan lagi? (Iya ketik 1, tidak ketik 0): "))
    if pilihan==1:
        selector()
    if pilihan==0:
        print("Terima kasih telah menggunakan program ini!")
    else:
        print("Input tidak valid, masukkan angka 0/1")
        next_action()

def selector(): 
    global datagenre
    global database_buku
    global list_jumlahbuku
    access_and_read_json()
    #jangan lupa input tanggal
    datagenre = [key for key in database_buku]
    print(datagenre)

    list_jumlahbuku = [[datagenre[i],0] for i in range(len(datagenre))]
    for i in range(len(list_jumlahbuku)):
        list_jumlahbuku[i][1] = len(database_buku[datagenre[i]])
        print(list_jumlahbuku)
    searchbuku()

    print("""Selamat Datang di Program Perpustakaan WI1001
    Halo! Ingin melakukan apa?
    1. Tampilkan ketersediaan buku
    2. Mencari buku
    3. Peminjaman buku
    4. Status peminjaman buku
    5. Pengembalian buku
    6. Exit
    """)

    pilihan=print("Masukkan pilihan: ")
    if pilihan==1:
        tampilkan_genre(datagenre)
        genre=input("Genre yang ingin dilihat: ")
        indexgenre=genre.index[genre]
        tampilandanketersediaan_buku(genre, page_lokal, indexgenre)
        next_action()
        
    elif pilihan==2:
        searchbuku()
        next_action()
        
    elif pilihan==3:
        add_peminjaman_buku()
        next_action()
        
    elif pilihan==4:
        status_peminjaman_buku()
        next_action()
        
    elif pilihan==5:
        pengembalian_buku()
        next_action()
        
    elif pilihan==6: 
        exit
    else :
        print("Input anda tidak valid, silahkan masukkan input berupa angka dari 1--6")
        selector()

print(selector())
