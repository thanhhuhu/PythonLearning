#lấy toàn bộ nội dung của thư viện 
#từ thư viện decimal -> import mọi thứ (*) 
from decimal import*
#lấy tối đa 30 chữ số phần nguyên và phần thập phân 
getcontext().prec = 30
print(Decimal(10)/Decimal(3))

d =30
f =7
df = d/f

print(df)
from fractions import*
# tao mot phan so co tu la 6 va co mau la 9
frac1 = Fraction(6,9)
frac2 = Fraction(5,10)
frac3 = frac1 + frac2
print(frac3)
print(type(frac3))
