# PROGRAM MESIN PEMBELIAN MINUMAN 

import os
sistem_operasi=os.name

#Database dari minuman yang dijual
database_menu= [['kopi',[['kopi americano',10000],['kopi espresso',12000],['capuccino',14000],['mocha latte',16000],['long black',18000]]],
                ['jus',[['jus jeruk',5000],['jus apel',6000],['jus mangga',7000],['jus buah naga',8000],['jus jambu',9000]]],
                ['teh',[['lemon tea',6000],['black tea',7000],['teh oolong',8000],['teh melati',9000],['white tea',10000]]],
                ['boba',[['taro boba Milk tea',10000],['thai milk tea',11000],['green tea boba',12000],['matcha latte boba',13000],['hazelnut milk boba',14000]]],
                ['susu',[['milo',9000],['indomilk cream',11000],['pink milk',13000],['australian cow milk',15000],['breeze almond',17000]]]]

match sistem_operasi:
    case "posix": os.system('clear')
    case "nt": os.system('cls')


# Fungsi untuk memilih menu
def pilih_menu():
    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'DI PYTHON DRINKING SHOP':^30}\n")
    print(f"{'SILAHKAN PILIH MENU':^30}")
    print('='*30)
    print(f"{'no |':10} {'menu':20}")
    print('-'*30)
    for index,menu in enumerate(database_menu): # Perulangan untuk mencetak daftar menu yang ada didatabase
        print(f"{f'{index+1}  |':10} {menu[0]:20}")
    print('-'*30)
    menu_pesanan= int(input('masukkan nomor menu: '))
    match sistem_operasi: # Percabangan untuk menyesuaikan sistem operasi yang ada diperangkat user
        case "posix": os.system('clear')
        case "nt": os.system('cls')
    return menu_pesanan-1


# Fungsi untuk memilih varian
def pilih_varian():
    try: # Percabangan untuk menguji apakah inputan yang diberikan user bisa dieksekusi
        print(f"{f'DAFTAR {database_menu[menu_minuman][0].upper()}':^40}")
        print(f"{'PYTHON DRINKING SHOP':^40}\n")
        print(f"{'SILAHKAN PILIH VARIAN':^40}")
        print('='*40)
        print(f"{'no |':10}  {'varian':20} {'harga':10}")
        print('-'*40)
        for index,varian in enumerate(database_menu[menu_minuman][1]):
            print(f"{f'{index+1}  |':<10} {varian[0]:20} {f'Rp {varian[1]}':10}")
        print('-'*40)
        varian_pesanan= int(input('masukkan nomor varian: '))
        return varian_pesanan
    except:
        return False
    

# Fungsi untuk konfirmasi pesanan
def konfirmasi_pesanan():
    if varian_menu==False: # Percabangan untuk memilih tindakan pada output fungsi sebelumnya
        match sistem_operasi:
            case "posix": os.system('clear')
            case "nt": os.system('cls')
        print('tidak ditemukan nomor menu yang sesuai')
        
    else:
        try:
            pesanan=database_menu[menu_minuman][1][varian_menu-1][0] 
            harga= database_menu[menu_minuman][1][varian_menu-1][1]
            jumlah_pesanan= int(input('jumlah pesanan: '))
            match sistem_operasi:
                case "posix": os.system('clear')
                case "nt": os.system('cls')
            print('terimakasih telah memesan, berikut detail pesanan anda:')
            print(f"pesanan       : {pesanan} \nharga         : Rp {harga} \njumlah pesanan: {jumlah_pesanan} \ntotal harga   : Rp {harga*jumlah_pesanan}")

        except:
            match sistem_operasi:
                case "posix": os.system('clear')
                case "nt": os.system('cls')
            print('tidak ditemukan nomor varian yang sesuai')

        


# ketiga fungsi tersebut dipanggil didalam perulangan untuk menjalankan program
pesan_lagi='y'
while pesan_lagi=='y':
    menu_minuman=pilih_menu()
    varian_menu=pilih_varian()
    konfirmasi_pesanan()
    pesan_lagi= input('apakah anda ingin memesan lagi (y/n)?: ')
    match sistem_operasi:
        case "posix": os.system('clear')
        case "nt": os.system('cls')

print('terimakasih telah berbelanja disini')
