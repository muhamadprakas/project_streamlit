daftar_karyawan = []
gapok = 5500000
total_gaji_perusahaan = 0

jumlah_karyawan = int(input('Masukan jumlah karyawan : '))
for i in range(jumlah_karyawan):
    print(f'\n=== Input Karyawan Ke-{i+1} ===')
    nama = input('Nama Karyawan\t: ')
    golongan = int(input('Golongan (1/2/3)\t: '))
    pendidikan = input('Pendidikam (SMA/S1)\t: ').upper()
    jam_kerja = float(input('Jumlah Jam Kerja\t: '))

    if golongan == 1:
        tj_golongan = 0.25/100 * gapok
    elif golongan == 2:
        tj_golongan = 5/100 * gapok
    elif golongan == 3:
        tj_golongan = 10/100 * gapok
    else:
        tj_golongan = 0

    if pendidikan == 'SMA':
        tj_pendidikan = 12/100 * gapok
    elif pendidikan == 'S1':
        tj_pendidikan = 20/100 * gapok
    else:
        tj_pendidikan = 0

    if jam_kerja>160:
        honor_lembur = (jam_kerja-160)*35000
    else:
        honor_lembur = 0

    total_gaji = gapok + tj_golongan + tj_pendidikan + honor_lembur
    total_gaji_perusahaan += total_gaji

    daftar_karyawan.append({
        'nama':nama,
        'golongan':tj_golongan,
        'pendidikan':tj_pendidikan,
        'lembur':honor_lembur,
        'total_gaji':total_gaji,
    })

print('='*50)
print(f"{'No':<5} | {'Nama Karyawan':<12} | {'Tj. golongan':<13} | {'Tj. Pendidikan':<14} | {'Honor Lembur':<12} | {'Total Gaji':<13}")
print('=' *90)
for i in range(len(daftar_karyawan)):
    k = daftar_karyawan[i]
    print(f"{i+1:<5"} | {k['nama']:<12} | Rp.{k['golongan']:<10,.0f} | Rp.{k['pendidikan']:<11,.0f} | Rp.{k['lembur']:<9,.0f} | Rp.{k['total_gaji']:<10,.0f}")
print('=' *90)
print(f"{'TOTAL GAJI YANG DIKELUARKAN PERUSAHAAN':<68} : Rp.{total_gaji_perusahaan:>10,.0f}")
