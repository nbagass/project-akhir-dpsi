import pandas as pd

pasien ={
    'ID Pasien':[
        '00001',
        '00002',
        '00003'
    ],
    'Nama':[
        'Lu bu',
        'Xiao ling',
        'Yun zhao'
    ],
    'Jenis kelamin':[
        'L',
        'P',
        'L'
    ],
    'Tanggal Lahir':[
        '13/01/1245',
        '15/11/1253',
        '16/03/1239'
    ]
}

penyimpanan ={
    'Barang':[
        'Kasur Pasien',
        'Stetoskop',
        'Termometer'
    ],
    'Jumlah':[
        '25',
        '50',
        '100',
    ]
}

pasien_table = pd.DataFrame(pasien)
penyimpanan_table = pd.DataFrame(penyimpanan)


username ='proto'
password = 'password'

print("="*20)
usernameInput = input("Username :")
passwordInput = input("Password :")
print("="*20)

if(passwordInput==password and usernameInput==username):

    print("="*35)
    print ("Layanan Sistem Informasi Klinik X :")
    print("="*35)
    print ("1. Pasien\n"+
            "2. Penyimpanan\n"+
            "3. Janji Temu\n"+
            "4. Daftar Obat\n"+
            "5. Profil\n")
    print("Silahkan pilih opsi : ")
    choice = input()

    if(choice == "1"):
        print(pasien_table)
    elif(choice == "2"):
        print(penyimpanan_table)
    else:
        print("Input yang anda masukkan salah")
else:
     print("Mohon maaf username atau password anda salah, Silahkan coba kembali")