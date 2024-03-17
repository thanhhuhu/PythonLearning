
teo ='Teo'

#Cách khởi tạo List
print(teo)
print ([1,2,3,4,5])
print(['a','b','c','d'])
print([[1, 2], [3, 4]])
empty_list =[]
print(empty_list)

#Sử dụng List Comprehension
a=[kteam for kteam in range (3)]
print (a)
another_lst = [[n, n * 1, n * 2] for n in range(1, 4)]
print(another_lst)

#Sử dụng constructor List
lst = list([1,2,3])
print(lst)
str_lst = list('HOWKTEAM')
print( str_lst)

#toán tử *
lst = list('kter')*3
print(lst)

#toán tử in

print('a' in [1,2,3])
print('a' in ['a', 2, 3])

#toán tử so sánh

print([1,2,3] == [1,2,3])
print([1,2,3,4] == [1,2,3])
print([4] > [3, 4])

#ndexing và cắt List trong Python

lst = [1, 2, 'a', 'b', [3, 4]]
print(lst[0])
print(lst[-1])
print(lst[1:3])
print(lst[:2])
print(lst[2:])

#Thay đổi nội dung List trong Python

s= ['math', 'liter']
s[1] = 'i'
print(s[1])

#Không được phép gán List này qua List kia nếu không có chủ đích
# Nếu thay đổi phần tử của list 1 thì phần tử list 2 cũng sẽ thay đổi

#Toán tử is
#Kiểm tra xem hai biến A và B có cùng trỏ đến một đối tượng hay không. Nếu một trong hai biến được gán giá trị bằng biến còn lại, thì kết quả trả về là True.
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

a = [1, 2, 3]
a=b
print(a is b)

lst = [1, 2, 3]
lst_copy_1 = list(lst)
print(lst_copy_1 is lst)

#phuong thuc count

lst = [1, 2, 3]
print(lst.count(1))

# phuong thuc index

Kteam = [1, 2, 3]
print(Kteam.index(2))

# phuong thuc copy 
Kteam = [1, 2, 3]
another_lst = lst.copy();
another_lst[0] =3
print(another_lst)
#phuong thuc clear  <List>.clear()

#phuong thuc append <List>.append(x)
Kteam = [1, 2, 3]
Kteam.append(4)
print(Kteam)
#Đừng bao giờ append một list vào chính nó.

#phuong thuc extend <List>.extend(iterable)

Kteam = [1, 2, 3]
Kteam.extend([4, 5]) # xem sự khác biệt giữa append và extend
print (Kteam)
Kteam.extend([[6, 7], 8])
print (Kteam)

#Phương thức insert <List>.insert (i, x) Thêm phần x vào vị trí i ở trong List.

#Phương thức pop <List>.pop([i]) Bỏ đi phần tử thứ i trong List và trả về giá trị đó. Nếu vị trí i không được cung cấp, phương thức này sẽ tự bỏ đi phần tử cuối cùng của List và trả về giá trị đó.

#Phương thức remove

#Phương thức reverse

#Phương thức sort <List>.sort(key=None, reverse=False)

a = ['This', 'is', 'How', 'Kteam']
b = a.copy()
a.sort()
b.sort(key = len)
print (b)
print (a)



 






























