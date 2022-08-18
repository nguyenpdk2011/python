dem = 0
chuoi = ""
for x in range(1,100,2): #x = 1,3,5,..., 100
    chuoi += str(x) + " "  
    dem = dem + 1 
print(chuoi)
print("số lượng số lẻ từ 1 đến 100 là: " + str(dem))