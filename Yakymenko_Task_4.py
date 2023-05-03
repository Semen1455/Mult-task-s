# Multiparadigmatic  programming languages:Task_4
# Yakymenko Semen:IKM-221a

import math


print('Multiparadigmatic  programming languages:Task_4\nYakymenko Semen:IKM-221a, Twenty-third(23) on the list')

n = int(input('Input n: '))
for i in range(1, math.factorial(n)):
    if math.factorial(n) / i / (i+1) == i + 2:
        print('Program is working', ':',  i, ' * ', i+1, ' * ',  i+2, ' = ', i * (i + 1) * (i + 2))
        break
    else:
        print('There are no such numbers')
        break
