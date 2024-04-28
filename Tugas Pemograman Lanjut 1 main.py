print ("Selamat datang di Aplikasi perhitungan nilai mahasiswa")
tugas = float(input("Silahkan memasukan nilai Tugas anda : "))
uts = float(input("Silahkan memasukan nilai UTS anda : "))
uas = float(input("Silahkan memasukan nilai UAS anda : "))

# Variabel menentukan nilai
nilai = (0.25 * tugas) + (0.35 * uts) + (0.40 * uas)

# Menentukan grade dari nilai
if nilai > 85 :
    grade = "A"
elif nilai > 80 : 
    grade = "A -"
elif nilai >= 75 : 
    grade = "B +"
elif nilai >= 70 : 
   grade = "B"
elif nilai >= 65 : 
    grade = "B -"
elif nilai >= 60 : 
    grade = "C +"
elif nilai >= 55 : 
    grade = "C"
elif nilai >= 50 : 
    grade = "C -"
elif nilai >= 30 : 
    grade = "D"
elif nilai == 30 : 
    grade = "E"
    
print ("Nilai Akhir Anda: ",nilai)
print ("Dalam Huruf: ",format(grade))