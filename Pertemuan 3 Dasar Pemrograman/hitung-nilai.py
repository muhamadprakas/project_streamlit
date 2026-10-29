print('===PROGRAM PENILAIAN MAHASISWA===')

nama = input('Masukan Nama\t\t\t: ')
kelas = input ('Masukan Kelas\t\t\t: ')
absensi = int(input('Masukan Nilai Absensi (1-16)\t: '))
tugas = int(input('Masukan Nilai Tugas (0-100)\t: '))
projek = int(input('Masukan Nilai Projek (0-100)\t: '))

#OPERATOR ARITMATIKA
nilai_akhir = (absensi/16*100*0.2)+(0.25*tugas)+(0.55*projek)

#OPERATOR PERBANDINGAN
if nilai_akhir >= 80:
    grade = 'A'
elif nilai_akhir >= 70:
    grade = 'B'
elif nilai_akhir >= 60:
    grade = 'C'
elif nilai_akhir >= 40:
    grade = 'D'
else:
    grade = 'E'

# OPERATOR LOGIKA DAN IDENTITAS
lulus = grade == 'A' or grade == 'B' or grade == 'C'
if lulus is True:
    status = 'LULUS'
else:
    status = 'TIDAK LULUS'

# OPERATOR KEANGGOTAAN
if '17' in kelas:
    jurusan = 'Teknologi Informasi'
elif '15' in kelas:
    jurusan = 'Informatika'
else:
    jurusan = 'Kosong'

print('='*40)
print('\tHASIL PENILAIAN MAHASISWA')
print('='*40)
print(f'Nama\t\t: {nama}')
print(f'Kelas\t\t: {kelas}')
print(f'Jurusan\t\t: {jurusan}')
print(f'Nilai Akhir\t: {nilai_akhir}')
print(f'Grade\t\t: {grade}')
print(f'Status\t\t: {status}')
print('='*40)

