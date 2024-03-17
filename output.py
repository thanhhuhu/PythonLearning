#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#*object
packing = 1,2,3,4
print(packing)

print('Kteam'+str(823))
print(123,[12312,12], '233')

#sep separate chia ra phan ra

print('thanh','dep','trai',sep='----')
print('Kteam', 'Python', 'Course', sep='\n')

#end kết thúc bằng

print ('a line without newline', end ='')
print('a line without newline', end='|||')


from time import sleep
#Khi chạy chương trình, bạn sẽ thấy xuất hiện dòng t ... sau đó 3 giây sau sẽ xuất hiện tới dòng end
print ('star....')
sleep(3)
print('end...')

print('start...',end ='')#in ra nội dung và kết thúc bằng một chuỗi rỗng
sleep(3)
print('end...')

#file

with open ('kteam.txt','w') as f: 
	print('printed',file = f)
with open ('kteam.txt') as f:
	f.read()
	




























