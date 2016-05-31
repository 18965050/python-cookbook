a = 4.2
b=2.1
print(a+b)

from decimal import Decimal
a=Decimal("4.2")
b=Decimal("2.1")
c=a+b
print(c)
print(round(c,2))

x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))
print(format(x, '0,.1f'))
print(format(x, 'e'))
print(format(x, '0.2E'))