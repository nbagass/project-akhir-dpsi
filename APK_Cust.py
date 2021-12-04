from numpy import left_shift
import pandas as pd


doctor ={
    'NAMA' :[
        'Dr.Faiz Ramadhan',
        'Dr.Amelia Putri',
        'Dr.Alifian Reza'
    ],
    'SPESIALIS' :[
        'Anak',
        'Ibu Hamil',
        'Umum'
    ]
}

jadwal_0 ={
    'HARI' :[
        'Senin',
        'Rabu',
        'Jumat'
    ],
    'Jam':[
        '08.00 - 17.00 WIB',
        '08.00 - 17.00 WIB',
        '08.00 - 11.00 WIB'
    ],
}

jadwal_1 ={
    'HARI' :[
        'Selasa',
        'Kamis',
        'Jumat'
    ],
    'Jam':[
        '08.00 - 17.00 WIB',
        '08.00 - 17.00 WIB',
        '08.00 - 11.00 WIB'
    ],
}

jadwal_2 ={
    'HARI' :[
        'Senin',
        'Selasa',
        'Rabu',
        'Kamis',
        'Jumat'
    ],
    'Jam':[
        '08.00 - 17.00 WIB',
        '08.00 - 17.00 WIB',
        '08.00 - 17.00 WIB',
        '08.00 - 17.00 WIB',
        '08.00 - 11.00 WIB'
    ],
}

doctor_table = pd.DataFrame(doctor)
jadwal0_table = pd.DataFrame(jadwal_0)
jadwal1_table = pd.DataFrame(jadwal_1)
jadwal2_table = pd.DataFrame(jadwal_2)
account_table = pd.DataFrame(account)



username ='proto'
password = 'password'

print("="*20)
usernameInput = input("Username :")
passwordInput = input("Password :")
print("="*20)

if(passwordInput==password and usernameInput==username):

    print("\nSelamat Mengakses Layanan Aplikasi dari Klinik X")

    print("================================================\n")
    print("Daftar layanan yang akan digunakan\n"+
        "1. Daftar & Jadwal Doktor\n"+
        "2. Pelayanan\n"+
        "3. Reservasi Doktor\n"+
        "4. Kontak\n\n")
    print("Silahkan pilih opsi: ")
    choice=input()
    print("\n")

    if(choice == "1"):
        print("\n===List Doktor Klinik X===")
        print(doctor_table.head())
        print("\nPilih untuk mengetahui jadwal praktik doktor")
        choice = input()

        if(choice == "0"):
            print(jadwal0_table)
        elif (choice =="1"):
            print(jadwal1_table)
        elif (choice =="2"):
            print(jadwal2_table)
    elif(choice == "2"):
        print("Daftar layanan yang tersedia :")
        print("\n1. Konsultasi\n"+
            "2. Pengobatan\n"+
            "3. Donor Darah\n"+
            "4. Perawatan Gigi\n"+
            "5. Medical Check Up\n"+
            "6. Kehamilan\n")
    elif(choice == "3"):
        nama =input( "Nama lengkap :\n" )
        email =input( "Email :\n" )
        noTelp =input( "No telp :\n" )
        alamat =input( "Alamat :\n" )
        tglRes =input( "Tanggal Reservasi :\n" )
        dokter =input( "Pilih Dokter :\n" )
        pesam =input( "Pesan (opsional) :\n" )
    elif(choice == "4"):
        nama =input( "Nama lengkap :\n" )
        noTelp =input( "No telp :\n" )
        subjek = input("Subjek :\n")
        pesan = input ("Pesan :\n")
    else:
        print("Input yang anda masukkan salah!")
else :
    print("Mohon maaf username atau password anda salah, Silahkan coba kembali")
