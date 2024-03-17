
#if expression:
#if- block
#else:
#else-block

a=0
b=3
if a - 1 < 0:
	print('a nhỏ hơn 1')
if b - 1 < 0:
	print('b nhỏ hơn 1')

a=3
if a - 1 < 0:
	print('a nhỏ hơn 1')
elif a - 2 < 0:
	print('a nhỏ hơn 2 ')
elif a - 3 < 0:
	print('a nhỏ hơn 3 ')
elif a - 4 < 0:
	print('a nhỏ hơn 4 ')
elif a - 5 < 0:
	print('a nhỏ hơn 5 ')

a=2
b=3
if a - 1 < 0:
	print('a nhỏ hơn 1')
else:
	print('a lớn hơn hoặc bằng 1')


if b - 1 < 0: 
   print('b nhỏ hơn 1')
else:
   print('b lớn hơn hoặc bằng 1')

#shorthand if else
#điều kiện ? giá trị 1 : giá trị 2 

a = 0
if a - 1 < 0:
    print('a nhỏ hơn 1')
elif a - 1 > 0:
     print('a lớn hơn 1')
else:
	  print('a bằng 1')
#cấu trúc điều kiện match - case 
t =5 
match t:
	case 1:
		print('t =1')
	case 2:
		print('t =2')
	case 5:
		print('t =5')

















