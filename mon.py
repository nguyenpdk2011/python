dem = 0
chuoi2 = ""
for x in range(7,101,7):#x = 2,4,6,...,100
    chuoi2 += str(x) + " "
    dem = dem + 1
print(chuoi2)
print("số lượng bội số của 7 từ 1 đến 100 là: " + str(dem))