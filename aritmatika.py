# aritmatika

a = 10
b = 3

# operasi tambah
hasil = a + b
print(a,'+',b,'=', hasil)

# operasi pengurangan
hasil = a - b
print(a,'-',b,'=', hasil)

# operasi perkalian
hasil = a * b
print(a,'*',b,'=', hasil)

# operasi pembagian
hasil = a / b
print(a,'/',b,'=', hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=', hasil)

# operasi modulus (%)
hasil = a % b
print(a,'%',b,'=', hasil)

# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

## prioritas operasi, operational precedence

'''
 1. ()
 2. exponen **
 3. perkalian dan teman teman * / ** % //
 4. pertambahan dan pengurangan
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(z,'+',y,'*.',z,'=',hasil)
## kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(',x,'+',y,')*',z,'=',hasil)


### LATIHAN PERHITUNGAN

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('masukan suhu dalam celcius : '))
print("suhu adalah ",celcius, "Celcius")

# REAMUR
# (4/5) * C
reamur = (4/5)*celcius
print("suhu dalam reamur adalah ",reamur, "Reamur")

# Fahrenheit
# 9/5 * C + 32
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit ",fahrenheit, "Fahrenheit")

# Kelvin
# Celcius + 273
kelvin = celcius + 32
print("suhu dalam kelvin adalah ",kelvin,"Kelvin")

