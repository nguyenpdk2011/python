import random
import os
if os.name == 'nt':
    os.system("")
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
#    print("\x1b[1;32;40mCâu số: "+str(socau)+" Điểm: "+ str(diem))
    print("Câu số: "+str(socau)+" Điểm: "+ str(diem))
    chon = str(random.randrange(1,5))
    if chon == "1": #phép cộng
        ketqua = int(input(cong + " = "))
        if ketqua == (a+b):
            print("Đúng rồi! Bạn khá lắm!")
            diem += 1
        else:
            print("Ối giồi ôi, sai rôi! Bạn đã kết thúc cuộc thi!")
            ketthuc = True
    elif chon == "2": #phép trừ
        ketqua = int(input(tru + " = "))
        if ketqua == (a-b):
            print("Đúng rồi! Bạn khá lắm!")
            diem += 1
        else:
            print("Ối giồi ôi, sai rôi! Bạn đã kết thúc cuộc thi!")
            ketthuc = True
    elif chon == "3": #phép nhân
        ketqua = int(input(nhan + " = "))
        if ketqua == (a*b):
            print("Đúng rồi! Bạn khá lắm!")
            diem += 1
        else:
            print("Ối giồi ôi, sai rôi! Bạn đã kết thúc cuộc thi!")
            ketthuc = True
    elif chon == "4": #phép chia
        ketqua = int(input(chia + " = "))
        if ketqua == int((a/b)):
            print("Đúng rồi! Bạn khá lắm!")
            diem += 1
        else:
            print("Ối giồi ôi, sai rôi! Bạn đã kết thúc cuộc thi!")
            ketthuc = True
print("Điểm số cuối cùng: "+str(diem)+"/"+str(socau)+" câu")
print("Cảm ơn bạn! Nghỉ thôi nào!")
print("-----------------------------------------------")