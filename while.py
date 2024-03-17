k =5
while k > 0:
	print('k = ',k )
	k-=1
s = 'How Kteam'
idx =0
lenght = len(s)

while idx < lenght:
	print(idx, 'stands for', s[idx])
	idx += 1

five_even_numbers =[]
k_number = 1
while True:
	if k_number %2 ==0:
		five_even_numbers.append(k_number)
	if len(five_even_numbers) ==5:
		break
	k_number +=1

#continue
k_number =1
while k_number < 10:
	if k_number%2 ==0:
		k_number +=1
		continue
	print(k_number,'is odd number')
	k_number +=1

#pass
#while expression:
#pass

a =3
b =4
while a > 0:
	a -=1
	pass
	b +=1
print (b)
print (a)

#while - else
#while expression:
#while-block
#else:
#else-block

while k < 3:
	print ('value of k is', k )
	k+=1
else:
	print ('k is not less than 3 anymore')

#infinite loop
a = 5
while a !=0:
	a -=2





































