dem = 0
chuoi2 = ""
for x in range(5,101,5):#x = 5,10,15,...,100
    chuoi2 += str(x) + " "
    dem = dem + 1
print(chuoi2)
print("số lượng bội số của 5 từ 1 đến 100 là: " + str(dem))