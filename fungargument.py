'''Fungsi dengan argument (input)'''


# def nama_fungsi(argument):
#    Badan Fungsi


def hello_world(nama):
    '''fungsi hellow world menerima input dengan variable nama'''
    print(f"Selamat datang dunia wahai {nama}")


hello_world("ucup")
hello_world("asyep")

# program tambah

def tambah(angka_1, angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,2)
tambah(10000,5)

# program absen

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")

    
anggota_boyband = ["ican","ekel","karung"]

say_hi(anggota_boyband)


    