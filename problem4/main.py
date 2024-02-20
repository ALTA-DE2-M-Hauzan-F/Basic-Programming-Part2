'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

Harga=input("Masukkan harga: ")
Diskon=input("Masukkan diskon (dalam %): ")

pay=float(Harga)*(1-float(Diskon)/100)
print("harga yang harus dibayar adalah Rp.",pay)