from random import random


import random
ketthuc = False
diem = 0
socau = 0
while ketthuc == False:
    socau += 1
    b = random.randrange(1,20)
    a = random.randrange(b,30)
    cong = str(a) + " + " + str(b)
    tru =  str(a) + " - " + str(b)
    nhan = str(a) + " * " + str(b)
    chia =  str(a) + " : " + str(b)
    print("---------------Toán học vui-----------------")
    print("Câu số: "+str(socau)+" Điểm: "+ str(diem)+"\nMời bạn chọn phép tính: ")
    print("1: cộng")
    print("2: trừ")
    print("3: nhan")
    print("4: chia")
    chon = input("Bạn chọn số: ")
    if chon == "1": #phép cộng
        ketqua = int(input(cong + " = "))
        if ketqua == (a+b):
            print("Đúng rồi! Bạn khá lắm!")
            diem += 1
        else:
            print("Ối giồi ôi, sai rôi! Cố lên bạn ơi!")
    elif chon == "2": #phép trừ
        ketqua = int(input(tru + " = "))
        if ketqua == (a-b):
            print("Đúng rồi! Bạn khá lắm!")
            diem += 1
        else:
            print("Ối giồi ôi, sai rôi! Cố lên bạn ơi!")
    elif chon == "3": #phép nhân
        ketqua = int(input(nhan + " = "))
        if ketqua == (a*b):
            print("Đúng rồi! Bạn khá lắm!")
            diem += 1
        else:
            print("Ối giồi ôi, sai rôi! Cố lên bạn ơi!")
    elif chon == "4": #phép chia
        ketqua = int(input(chia + " = "))
        if ketqua == int((a/b)):
            print("Đúng rồi! Bạn khá lắm!")
            diem += 1
        else:
            print("Ối giồi ôi, sai rôi! Cố lên bạn ơi!")
    else:
        print("Điểm số cuối cùng: "+str(diem)+"/"+str(socau-1)+" câu")
        print("Cảm ơn bạn! Nghỉ thôi nào!")
        ketthuc = True
