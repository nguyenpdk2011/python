import colorsys
#def colored(r, g, b, text):
#    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  
#text = 'Hello, World'
#colored_text = colored(255, 0, 0, text)
#print(colored_text)

#or

#print(colored(255, 0, 0, 'Hello, World'))
#print(colored('hello', 'red'), colored('world', 'green'))
print("---------------cơm nhà ngoại nấu-----------------")
print( "Mời bạn chọn món ")
print("1: cơm thịt kho")
print("2: cơm thịt nước tương")
print("3: cơm trứng chiên")
print("4: cơm canh khổ qua")
chon = input("Bạn chọn số: ")
if chon == "1": #cơm thịt kho
    print("cơm thịt kho")
    traloi = input("thịt kho có ngon ko? C/K")
    if(traloi=="C" or traloi=="c"):
        print("cảm ơn bạn ")
    else:
        print ("đừng tới quán này nữa nhé !!!")
elif chon == "2": #cơm thịt nước tương
    print("cơm thịt nước tương")
    traloi = input("thịt nước tương có ngon ko? C/K")
    if(traloi=="C" or traloi=="c"):
        print("cảm ơn bạn ")
    else:
        print ("đừng tới quán này nữa nhé !!!")
elif chon == "3": #cơm trứng chiên
    print("cơm trứng chiên")
    traloi = input("cơm trứng chiên có ngon ko? C/K")
    if(traloi=="C" or traloi=="c"):
        print("cảm ơn bạn ")
    else:
        print ("đừng tới quán này nữa nhé !!!")
elif chon == "4": #cơm canh khổ qua
    print("cơm canh khổ qua")
    traloi = input("cơm canh khổ qua có ngon ko? C/K")
    if(traloi=="C" or traloi=="c"):
        print("cảm ơn bạn ")
    else:
        print ("đừng tới quán này nữa nhé !!!")
else:
    print ("bạn chọn sai rồi! mời sang quán kế bên.")
