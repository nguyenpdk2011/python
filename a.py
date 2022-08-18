print("Chào mừng bạn đến với thế giới vi tính\n")
print("Bạn mấy tuổi?")
age = int(input())
if age < 12:
    print("Bạn là một thiếu niên")
else:
    print("Bạn là người trưởng thành")
    kethon = input("Bạn đã kết hôn chưa? Nhập Y/N: ")
    if kethon == "Y":
        print("Chúc bạn tạo dựng được một gia đình hạnh phúc")
    else:
        print("Hãy sống vui vẻ, tận hưởng nhiều niềm vui!")
