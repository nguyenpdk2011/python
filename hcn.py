print("Hình chữ nhật của bạn")
dai = int(input("Chiều dài: "))
rong = int(input("Chiều rộng: "))
dientich = dai * rong
chuvi = (dai + rong)*2
print("Hình chữ nhật của bạn có Dài = "+ str(dai) +" Rộng = "+ str(rong))
print("Chu vi = " + str(chuvi))
print("Diện tích = ")
print(dientich)
print("Hình hộp chữ nhật cần thêm chiều cao")
cao = int(input("Chiều cao: "))
thetich = dai * rong * cao
dtxq = chuvi * cao
dttp = dtxq + 2*dientich
print("Hình hộp của bạn có kích thước: "+ str(dai)+ " x " + str(rong) + " x " + str(cao) )
print("Thể tích = " + str(thetich))
print("Diện tích xung quanh = "+str(dtxq))
print("Diện tích toàn phần = " + str(dttp))