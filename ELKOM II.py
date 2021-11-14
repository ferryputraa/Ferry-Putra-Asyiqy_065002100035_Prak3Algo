a,b = (
    int(input("Masukkan total harga belanjaan Anda : ")),
    int(input("Masukkan jumlah uang anda : ")))
c = b-a
print ("Kembalian anda sejumlah",c,)
print ("Pecahan uang yang dibutuhkan : ")
d = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
for x in range (0, 7):
    i=0
while c >= d[x]:
    c=c-d[x]
    i=i+1
if (i>0):
    print ("Uang kertas %d sebanyak %d lembar" % (d[x], i))
