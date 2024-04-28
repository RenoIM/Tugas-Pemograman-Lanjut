month = -1
while (month < 1) or (month > 12):
    month = int(input("Masukan Bulan Lahir (1 - 12): "))
    if (month < 1) or (month > 12):
        print("Bulan harus bernilai sekitaran dari 1 - 12")

if (month in (1,3,5,7,8,10,12)):
    day = -1
    while (day < 1) or (day > 31):
        day = int(input("Masukan Hari lahir (1 - 31): "))
        if (day < 1) or (day > 31):
            print("Hari harus bernilai sekitaran dari 1 - 31")

elif (month in (4,6,9,11)):
    day = -1
    while (day < 1) or (day > 30):
        day = int(input("Masukan Hari lahir (1 - 30): "))
        if (day < 1) or (day > 30):
            print("Hari harus bernilai sekitaran dari 1 - 30")

elif (month == 2):
    day = -1
    while (day < 1) or (day > 29):
        day = int(input("Masukan Hari lahir (1 - 29): "))
        if (day < 1) or (day > 29):
            print("Hari harus bernilai sekitaran dari 1 - 29")

print()
print("Informasi Tanggal Lahir")
print("Bulan : ", month)
print("Hari : ", day)