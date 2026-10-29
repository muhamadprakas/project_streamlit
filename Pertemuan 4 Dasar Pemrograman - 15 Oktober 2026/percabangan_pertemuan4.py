print('=====TOKO SEPATU ABC======')
print('AD = Adidas')
print('NK = Nike')
print('PM = Puma')

kode = input('Masukan Kode Sepatu\t\t: ').upper()
ukuran = int(input('Masukan Ukuran Sepatu (36-44)\t: '))
jumlah = int(input('Masukan Jumlah Sepatu\t\t: '))

if kode == 'AD':
    nama_sepatu = 'Adidas'
    if ukuran >=36 and ukuran <=41:
     harga = 700000
    elif ukuran >=42 and ukuran <=44:
     harga = 750000
    else:
     harga = 0
elif kode == 'NK':
    nama_sepatu = 'Niki'
    if ukuran >=36 and ukuran <=41:
     harga = 600000
    elif ukuran >=42 and ukuran <=44:
     harga = 650000
    else:
     harga = 0
elif kode == 'PM':
    nama_sepatu = 'Puma'
    if ukuran >=36 and ukuran <=41:
     harga = 550000
    elif ukuran >=42 and ukuran <=44:
     harga = 550000
    else:
     harga = 0
else:
     nama_sepatu = 'Kode Tidak Sesuai'
     harga = 0

total = harga*jumlah
if total >=1000000:
  diskon = 10/100*total
else:
  diskon = 0

total_bayar = total-diskon
print('\n===== STRUCK PEMBELIAN SEPATU======')
print(f'Kode Sepatu\t: {kode}')
print(f'Nama Sepatu\t: {nama_sepatu}')
print(f'Ukuran Sepatu\t: {ukuran}')
print(f'Jumlah Sepatu\t: {jumlah}')
print(f'Harga Sepatu\t: {harga}')
print(f'Total Harga\t: {total}')
print(f'Diskon Sepatu\t: {diskon}')
print(f'Total Bayar\t: {total_bayar}')
