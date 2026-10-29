# perulangan for
for i in range(1,11):
    print('No Urut', i)

mapel = ['Matematika', 'Kimia', 'fisika']
for i in range(len(mapel)):
    print('Saya suka', mapel[i])

# perulangan while
i = 0
while i < 10:
    print('No', i)
    i = i+1
else:
    print('No urut tidak sesuai')

# fungsi break
nama = ['Andi', 'Budi', 'Cintia', 'Dedi', 'Edi']
for i in range(len(nama)):
    print('Ini adalah', nama[i])
    if nama[i] == 'Cintia':
        print('Cintia ditemukan!')
        break

# fungsi continue
nama = ['Andi', 'Budi', 'Cintia', 'Dedi', 'Edi']
for i in range(len(nama)):
    if nama[i] == 'Cintia':
        continue
    print('Ini adalah', nama[i])

