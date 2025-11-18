"""Nama Program: Lift 

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
database_buku = {
    "genre": {
        1 : ["Judul",1],
        2 : ["Judul",1]
    }
    
}
database_peminjamanbuku = {}

counter = 1

def access_and_read_json():
    global database_buku
    try:
        with open(f"Database_buku.json","r") as fileinput:
            database_buku = json.load(fileinput)
            
    except FileNotFoundError: 
        pass
def save_peminjaman():
    pass
def cek_denda():
    pass
def pembayaran():
    pass
def tampilandanketersediaan_buku(): #Status ketersediaan buku dan Status buku sisa (Per 25 Judul) jadi next harus ada 
    pass

def add_peminjaman_buku():
    pass

def status_peminjaman_buku():
    pass

def pengembalian_buku():
    pass
def searchbuku():
    pass

def redo():
    pass

def selector(): 
    access_and_read_json()
    

selector()