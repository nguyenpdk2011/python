n = int(input("Nhập số: "))
print("Chương trình kiểm tra số nguyên tố trả lời bạn về số "+str(n))
snt = True
if n < 2:
    snt = False
elif n==2:
    snt = True
else:
    for x in range(2,n):
        if (n % x) == 0:
            snt = False
            print(str(n)+" chia hết cho "+str(x))
            break
if snt == True:
    print(str(n) + " là số nguyên tố")
else:
    print(str(n) + " không phải số nguyên tố")