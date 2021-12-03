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


print("\nSelamat Mengakses Layanan Aplikasi dari Klinik X")

print("================================================\n")
print("Daftar layanan yang akan digunakan\n"+
    "1. Daftar & Jadwal Doktor\n"+
    "2. Booking jadwal praktik\n\n")
print("Silahkan pilih opsi: ")
choice=input()

