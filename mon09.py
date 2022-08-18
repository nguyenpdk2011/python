import random
import os
if os.name == 'nt':
    os.system("")
ketthuc = False
diem = 0
socau = 0
while ketthuc == False:
#    dai = int(input("dai: "))
#    rong = int(input("rong: "))
#    cao = int(input("cao: "))
#    day = int(input("day: "))
#    day2 = int(input("day2: "))
#    bk = int(input("bk: "))
#    canh =int(input("canh: "))
#    hcn = dai * rong
#    htron  =  bk * bk * 3.14
#    hv  = canh * canh
#    htg  =  day * cao
#    hthang =  (day + day2) * cao / 2
    print("---------------Toán học vui-----------------")
#    print("Câu số: "+str(socau)+" Điểm: "+ str(diem)+"\nMời bạn chọn phép tính: ")
    print("1: hcn")
    print("2: htron")
    print("3: hv")
    print("4: htg")
    print("5: hthang")
    chon = input("Bạn chọn số: ")
    if chon == "1": #hcn
        dai = int(input("Nhập dài = "))
        rong = int(input("Nhập rộng = "))
        ketqua = dai * rong
        print("Diện tích hcn= ", ketqua)
    elif chon == "2": #htron
        bk = int(input("Nhập bk ="))
        ketqua = bk*bk * 3.14
        ketqua2 = (bk+bk) *3.14
        print("Diện tích htron = ", ketqua)
        print("chu vi htron = ", ketqua2)
    elif chon == "3": #hv
        canh = int(input("Nhập canh ="))
        ketqua = (canh*canh)
        ketqua2 = canh * 4
        print("Diện tích hv = ", ketqua)
        print("chu vi hv = ", ketqua2)
    elif chon == "4": #htg
        day = int(input("Nhập day ="))
        cao = int(input("Nhập cao ="))
        canhA = int(input("Nhập canhA = "))
        canhB = int(input("Nhập canhB = "))
        canhC = int(input("Nhập canhC = "))
        ketqua = day * cao / 2
        ketqua2 = canhA + canhB + canhC
        print("Diện tích htg= ", ketqua)
        print("chu vi htg= ", ketqua2)
    elif chon == "5": #hthang
        day = int(input("Nhập day ="))
        day2 = int(input("Nhập day2 ="))
        cao = int(input("Nhập cao ="))
        ketqua = (day + day2) * cao / 2
        print("Diện tích hthang= ", ketqua)
    else:
        print("Cảm ơn bạn! Nghỉ thôi nào!")
        ketthuc = True
