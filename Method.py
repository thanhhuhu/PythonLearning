
print('Haizz,\neu mot ngay')
a = r'\neu mot ngay'
print(a);
s ='hello'
s +=' python'
print(s);
s2 =', good bye'
s3 = s + s2;
print(s3);

s ='abc xyz'
s = 'k' +s[1:]
print(s)
# lấy các kí tự từ vị trí 1 đến hết chuỗi

'My name is %s.' %('Luca')


f'abc' #đây là một f-string

s =f'xyz'# vẫn chưa có gì khác biệt so với chuỗi thông 
print (s)
print(f'a\tb')

variable = 'three'
f'1:{{one}},2:{{two}}, 3:{variable}'
#‘1: {one}, 2: {two}, 3: three’
# nháy đơn 
''
# nháy kép
""

# bất cứ gì bên trong dấu nháy được gọi là một chuỗi 
strHowKteam ='strHowKteam'
print (strHowKteam);
print (strHowKteam);
print(type (strHowKteam));# kiểu chuỗi 

HowKteam ="I''m " " Beginner"

#tạo ra chuỗi bằng cách lặp lại chuỗi nhân 3
s='a'*3
print(s)

'ă' < 'â' 
# vì ‘ă’ đứng sau ‘â’ trong bảng mã Unicode

#sthing 
#Đây là __repr__
#print(sthing)
#Đây là __str__

'{:^10}'.format('aaaa')
# căn giữa
print('{:^10}'.format('aaaa') )
#căn lề trái 
print (('{:<10}'.format('aaaa')))
#căn lề phải 
print(('{:>10}'.format('aaaa')))

row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Kteam', 'TP HCM')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Kquiz', 'Da Lat')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

print(row_1);
print(row_2);
print(row_3);
print(row_4);
print(row_5);

#capitalize
#Trả về một chuỗi với kí tự đầu tiên được viết hoa và viết thường tất cả những kí tự còn lại.
a ='howkteam'.capitalize();
print (a)

#upper
a= 'kter'.upper();
print(a);

#lower 
a= 'kter'.lower();
print(a);

#swapcase
a ='hello EVERYONE'.swapcase();
print(a);
a ='HeLle eweEE'.swapcase();
print(a);

#TITLE
a ='eeee eweEE'.title();
print(a);

#CENTER
a ='abc'.center(12)
print(a)
a ='abc'.center(12,'*')
print(a)

#rjust
#Cách hoạt động tương tự như phương thức center, có điều là căn lề phải
a ='kteam'.rjust(12)
print(a)

#split
#Trả về một list (kiểu dữ liệu sẽ được Kteam giới thiệu ở bài KIỂU DỮ LIỆU LIST) bằng cách chia các phần tử bằng kí tự sep.
a='how k team '.split()
print(a);
a='How Kteam K9'.split(maxsplit=1)
print(a);
