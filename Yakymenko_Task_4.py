# Multiparadigmatic  programming languages:Task_4
# Yakymenko Semen:IKM-221a

import math

print('Multiparadigmatic  programming languages:Task_4\nYakymenko Semen:IKM-221a, Twenty-third(23) on the list')

try:
    n = int(input('Enter n: '))
    for i in range(1, math.factorial(n)):
        if math.factorial(n) / i / (i + 1) == i + 2:
            print('Program is working')
            break
        else:
            print('There are no such numbers')
    else:
        print('Try to enter something else')
except ValueError:
    print('You wrote a letter,try to enter number')
