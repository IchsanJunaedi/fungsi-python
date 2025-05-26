'''args'''

# memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ekel",180,92)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["otong",150,50])

# *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung",180,62)

# studi kasus

def tambah(*data): # *data = *args juga
    # data typenya adalah tuple, dan dia bisa diiterasikan
    output = 0
    for angka in data:
        output += angka
    
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = tambah(10,5,10)
print(f"hasil = {hasil}")