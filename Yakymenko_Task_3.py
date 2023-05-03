# Multiparadigmatic  programming languages:Task_3
# Yakymenko Semen:IKM-221a


import math

print('Multiparadigmatic  programming languages:Task_3\nSemen Yakymenko:IKM-221a')

TEMPLATE = 'Please Enter {} : '
x = int(input(TEMPLATE.format('x')))
z = int(input(TEMPLATE.format('z')))
if z != 2:
    res = (x * math.atan(z)) + math.exp((x + 3) / (z - 2))
    print('Result is:', res)
else:
    print('Error,your function will not work,type something else')
