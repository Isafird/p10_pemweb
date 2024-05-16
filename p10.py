import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

list_data = []

def show_menu():
    clear_screen()
    print("====APLIKASI KONTAK====")
    print("[1] Lihat Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[5] Exit")
    print("\n")

    menu = input("Pilih Menu : ")

    if menu == '1':
        menu1()
    elif menu == '2':
        menu2()
    elif menu == '3':
        menu3()
    elif menu == '4':
        menu4()
    elif menu == '5':
        print("Terimakasih Telah Berkunjung")
        exit()
    else:
        print("Menu yang anda masukkan tidak ada, masukkan pilihan yang tersedia")
        kembali()

def menu1():
    print('NIM || Nama')
    if not list_data:
        print('Data Masih Kosong')
    else:
        for data in list_data:
            print(f"{data['NIM']} || {data['Nama']}")
    kembali()

def menu2():
    Nim = input("Masukkan Nim Anda : ")
    Nama = input("Masukkan Nama Anda : ")
    for data in list_data:
        if data['NIM'] == Nim:
            print("NIM sudah ada dalam database.")
            kembali()
            return
    list_data.append({"NIM": Nim, "Nama": Nama})
    print("Data Berhasil Ditambah")
    kembali()

def menu3():
    Nim = input("Masukkan Nim Anda : ")
    found = False
    for data in list_data:
        if data['NIM'] == Nim:
            found = True
            nama_baru = input("Masukkan Nama Baru : ")
            data['Nama'] = nama_baru
            print("Data berhasil dirubah")
            break
    if not found:
        print("NIM tidak ditemukan.")
    kembali()

def menu4():
    Nim = input("Masukkan Nim Anda : ")
    found = False
    for data in list_data:
        if data['NIM'] == Nim:
            found = True
            list_data.remove(data)
            print("Data berhasil dihapus")
            break
    if not found:
        print("NIM tidak ditemukan.")
    kembali()
    
def kembali():
    input("Tekan enter untuk kembali")
    show_menu()

while True:
    show_menu()
