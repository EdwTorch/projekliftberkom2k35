import time
lantai = ["B","LG","G","UG","1","2","3","5","7","8","9","10","11","12","15"]
cek_indexlantaiawal = 0
validasi_inputlantaiawal = False
input_lantaiawal = 0
masukan_lantaiawal = ""

def tampilan_pilihanlantai():
    for l in lantai: #Menyajikan data lantai
        print("┌───┐", end=" ")
    print()

    for l in lantai:
        print(f"│{l:^3}│", end=" ")
    print()

    for l in lantai:
        print("└───┘", end=" ")
    print()
    return 0

def fungsi_validasi_inputlantaiawal_withoutglobal(masukan_lantaiawal_lokal,lantaidatabase,validasi_inputlantaiawal_lokal,cek_indexlantaiawal_lokal):
    masukan_lantaiawal_lokal = input("Masukkan Lantai awal : ")
    masukan_lantaiawal_lokal = masukan_lantaiawal_lokal.upper()
    
    while cek_indexlantaiawal_lokal < len(lantaidatabase) and validasi_inputlantaiawal_lokal == False: #Cek Inputan apakah ada dalam database
        
        if masukan_lantaiawal_lokal == lantaidatabase[cek_indexlantaiawal_lokal]:
            validasi_inputlantaiawal_lokal = True #inputan ada di database
        
        else: 
            cek_indexlantaiawal_lokal +=1 #cek indeks selanjutnya

    if validasi_inputlantaiawal_lokal == True: 
        print(masukan_lantaiawal_lokal)
        return masukan_lantaiawal_lokal
    
    else: 
        cek_indexlantaiawal_lokal = 0
        print("Lantai yang anda masukkan tidak sesuai")
        return fungsi_validasi_inputlantaiawal_withoutglobal(masukan_lantaiawal_lokal,lantaidatabase,validasi_inputlantaiawal_lokal,cek_indexlantaiawal_lokal)

def fungsi_validasi_inputlantaiawal_withglobal():
    global masukan_lantaiawal
    global cek_indexlantaiawal
    global lantai
    global validasi_inputlantaiawal
    global input_lantaiawal
    masukan_lantaiawal = input("Masukkan Lantai awal : ")
    masukan_lantaiawal = masukan_lantaiawal.upper()
    
    while cek_indexlantaiawal < len(lantai) and validasi_inputlantaiawal == False: #Cek Inputan apakah ada dalam database
        
        if masukan_lantaiawal == lantai[cek_indexlantaiawal]:
            validasi_inputlantaiawal = True #inputan ada di database
        
        else: 
            cek_indexlantaiawal +=1 #cek indeks selanjutnya
    
    if validasi_inputlantaiawal == True: 
        input_lantaiawal = True
    
    else: 
        cek_indexlantaiawal = 0
        print("Lantai yang anda masukkan tidak sesuai")


tampilan_pilihanlantai()
masukan_lantaiawal = fungsi_validasi_inputlantaiawal_withoutglobal(masukan_lantaiawal,lantai,validasi_inputlantaiawal,cek_indexlantaiawal)
print(masukan_lantaiawal)