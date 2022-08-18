dem = 0
chuoi2 = ""
for x in range(6,101,6):#x = 6,12,18,...,100
    chuoi2 += str(x) + " "
    dem = dem + 1
print(chuoi2)
print("số lượng bội số của 2 và 3 từ 1 đến 100 là: " + str(dem))