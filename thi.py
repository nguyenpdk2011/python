A = 0
chuoi = ""
for x in range(1,2024,2): #x = 1,3,5,..., 2005
    chuoi += str(x) + " "
    A += x
print(chuoi + " = " + str(A))
B = 0
chuoi2 = ""
for x in range(2,2023,2):#x = 2,4,6,...,2006 
    chuoi += str(x) + " "
    B += x
print(chuoi + " = " + str(B))
print("A - B = " + str(A - B))