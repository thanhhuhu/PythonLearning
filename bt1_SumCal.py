#bt1 tính tổng 2 số nguyên nhập 
# num1 = int(input())
# num2 = int(input())
# tong = num1 + num2 
# print("tong 2 so la ", tong)

#bt2 tính tổng 2 số nguyên nhập vào , có xử lý ngoại lệ 
# num1 = input()
# num2 = input()

# try:
# 	num1 = int(num1)
# 	num2 = int(num2)
# 	tong = num1 + num2
# 	print ("tong cua 2 so la ", tong)
# except:
# 	print("dinh dang dau vao khong hop le!!")

# num1 = input()
# num2 = input()

# if num1 == int(num1) && num2 == int(num2):
# 	tong = num1 + num2
# 	print ("tong cua 2 so la : " + tong)
# else:
# 	print("dinh dang dau vao khong hop le ")

#bt3 hiển thị từ cách nhau bởi ký tự -- ra màn hình

# ten = input()
# print('Xin', 'chao!', 'Toi', 'ten', 'la', ten, sep='--')

#bt4 Nhập số bất kỳ ở hệ thập phân và hiển thị ra ở hệ bát phân

num = input("Enter a number: ")
num = float(num)  # Convert the input string to a float
print("The number you entered is:", num)
decimal = num ** 2  # Square the number
print("So thap phan " + str(num) + " trong he bat phan la " + str(decimal))
