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

def save_peminjaman():
    pass
def cek_denda():
    pass
def pembayaran():
    pass

def tampilkan_genre(datagenre):
    global database_buku
    print("Berikut adalah genre yang tersedia: ")
    for i in range(len(datagenre)):
        print(f"{i+1}. {datagenre[i]} ")

def tampilandanketersediaan_buku(genre, page_lokal, indexgenre): #Status ketersediaan buku dan status buku sisa (per 15 judul) jadi next harus ada 
    global database_buku
    global list_jumlahbuku
    input_ulang_valid = "False"
    totalbukusaatini = list_jumlahbuku[indexgenre][1]
    listbuku = [isibuku for isibuku in database_buku[genre].values()]
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
                state = int(input(f"Apakah anda ingin melihat daftar lanjutan dari {genre} {counttotalbuku+1}- {totalbukusaatini}? : (ketik 0 untuk tidak, 1 untuk ya) : "))
                if state == 0 or state == 1:
                    input_ulang_valid = "True"
                else:
                    print("Masukkan tidak valid tolong masukkan ulang")
            
    if state == 1:
        page_lokal +=1
        tampilandanketersediaan_buku(genre, page_lokal)

    elif state == 0:
        pass

def add_peminjaman_buku():
    pass

def status_peminjaman_buku():
    pass

def pengembalian_buku():
    pass

def searchbuku():
    global database_buku
    global datagenre 
    global list_jumlahbuku

    print("1. Cari berdasarkan kategori")
    print("2. Cari berdasarkan judul")
    pilihan_pencarian = input("Masukkan pilihan (1/2): ")

    #Pencarian berdasarkan kategori 
    if (pilihan_pencarian == "1"): 
        print("\nKategori yang tersedia: ")
        for i, j in enumerate(datagenre): 
            print(f"{i+1}. {j}")
        
        pilih_kategori = input("Masukkan nomor kategori: ")
        try: 
            index_kategori = int(pilih_kategori) - 1
            kategori = datagenre[index_kategori]
        except: 
            print("Input tidak valid")
            return 
        
        print(f"\nDaftar Buku dalam Kategori {kategori}")
        for id_buku, info_buku in database_buku[kategori].items():
            judul = info_buku[0]
            stok = info_buku[1]
            print(f"{id_buku}. {judul} (stok: {stok})") 

    #Pencarian berdasarkan judul 
    elif (pilihan_pencarian == "2"): 
        keyword = input("Masukkan judul/keyword: ").lower()
        print("\nHasil Pencarian")
        found = False 

        for kategori, daftar_buku in database_buku.items():
            for id_buku, info_buku in daftar_buku.items():
                judul = info_buku[0]
                stok = info_buku[1]

                if keyword in judul.lower():
                    print(f"[{kategori}] {id_buku}. {judul} (stok: {stok})")
                    found = True 
            
            if not found: 
                print("Buku dengan judul tersebut tidak ditemukan")
    
    else: 
        print("Pilihan tidak valid")

def redo():
    pass

def selector(): 
    global datagenre
    global database_buku
    global list_jumlahbuku
    access_and_read_json()

    datagenre = [key for key in database_buku]
    print(datagenre)

    list_jumlahbuku = [[datagenre[i],0] for i in range(len(datagenre))]
    for i in range(len(list_jumlahbuku)):
        list_jumlahbuku[i][1] = len(database_buku[datagenre[i]].values())
        print(list_jumlahbuku)
    tampilkan_genre(datagenre)
    
    tampilandanketersediaan_buku(genre,page,i) #nanti ganti i nya pake variabel buat indexgenrenya
        

    
    

selector()

