print (" Program Menampilkan Bilangan Terbesar dari N Bilangan ")

n = 1
max = 0
while n != 0 :
    if n > max :
        max = n
    n = int(input(" Masukan Bilangan : "))
    if n == 0:
        break
print ("Bilangan Terbesar Adalah : ", max)
