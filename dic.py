
#{<key_1: value_1>, <key_2: value_2>, .., <key_n: value_n>}

dic = {'name': 'Kteam', 'member': 69}
print (dic)
empty_dict ={}
print(empty_dict)
print(type(dic))
#sử dụng dict comprehension

dic = {key: value for key, value in [('name', 'Kteam'), ('member', 69)]}
print(dic)

#Sử dụng constructor Dict
#Khởi tạo một Dict rỗng
#dict()

dic = dict()
print (dic)

name ='SpaceX'
member = 3234234
dic = dict(name ='Twitter', member ='233')
print(dic)
print (name)
print (member)

iter_ =('name', 'number')
dic_none = dict.fromkeys(iter_)
print(dic_none)

dic = dict.fromkeys(iter_, 'non None value')
print (dic)

{'name' : 'Kteam', 'member' :69}
dic['slogan']='Free education'
print (dic)

file_object = open('kteam.txt')
print(file_object)
file_object.close()
file_object.read()