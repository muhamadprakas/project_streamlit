nama_karyawan = input('Nama Karyawan\t\t\t: ')
golongan = int(input('Golongan Jabatan (1/2/3)\t: '))
pendidikan = input('Tingkat Pendidikan (SMA/S1)\t: ').upper()
jam_kerja = float(input('Total Jam Kerja\t\t\t: '))

gaji_pokok = 5500000

if golongan == 1:
  tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
  tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
  tunjangan_jabatan = 0.15 * gaji_pokok
else:
  tunjangan_jabatan = 0

if pendidikan == "SMA":
  tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "S1":
  tunjangan_pendidikan = 0.30 * gaji_pokok
else:
  tunjangan_pendidikan = 0

if jam_kerja > 8:
  jam_lembur = jam_kerja - 8
  honor_lembur = jam_lembur * 3500
else:
  honor_lembur = 0

total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

print("=====STRUK GAJI KARYAWAN=====")
print("Nama Karyawan\t\t : ", nama_karyawan)
print("Gaji Pokok\t\t : Rp. ", int(gaji_pokok))
print("Tunjangan Jabatan\t : Rp. ", int(tunjangan_jabatan))
print("Tunjangan Pendidikan\t : Rp. ", int(tunjangan_pendidikan))
print("Honor Lembur\t\t : Rp. ", int(honor_lembur))
print("Total Gaji\t\t : Rp. ", int(total_gaji))
