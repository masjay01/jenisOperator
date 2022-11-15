# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2
c = 3
# lebih besar dari >
print("=== lebih dari '>' ====")
hasil = b > c
print(b,'>',c,'=',hasil)

hasil = a > b
print(a,'>',b,'=',hasil)


# lebih kecil dari <
print("===Kurang dari '<'===")
hasil = c < a
print(c,'<',a,'=',hasil)

hasil = a < b
print(a,'<',b,'=',hasil)

# lebih besar sama dengan >=
print("===lebih besar sama dengan '>='===")
hasil = c >= a
print(c,'>=',a,'=',hasil)

hasil = a >= b
print(a,">=",b,'=',hasil)

# lebih kecil sama dengan <=
print("===lebih kecil sama dengan '<='")

hasil = a <= c
print(a,'<=',c,'=',hasil)

hasil = b <= a
print(b,'<=',a,'=',hasil)

# sama dengan ==
print("=== sama dengan '==' ====")

hasil = a == b
print(a,'==',b,'=',hasil)

hasil = a == c
print(a,'==',c,'=',hasil)

hasil = a == a
print(a,'==',a,'=',hasil)

# tidak sama dengan !=
print("===tidak sama dengan '!='===")

hasil = a != b
print(a,'!=',b,'=',hasil)

hasil = a != c
print(a,'!=',c,'=',hasil)

hasil = a != a
print(a,'!=',a,'=',hasil)

## is sebagai komparasi object indetity
print("=== is ====")
x = 5 # ini adalah assigment membuat object
y = 5
print("nilai x =",x,',id = ',hex(id(x)))
print("nilai y =",y,',id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil)


print("=== is not ====")
x = 5 # ini adalah assigment membuat object
y = 6
print("nilai x =",x,',id = ',hex(id(x)))
print("nilai y =",y,',id = ', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)