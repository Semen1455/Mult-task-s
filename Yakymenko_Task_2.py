# Multiparadigmatic  programming languages:Task_2
# Yakymenko Semen:IKM-221a


print('Multiparadigmatic  programming languages:Task_2\nSemen Yakymenko:IKM-221a')
TEMPLATE = 'Please Enter {} : '
TEMPLATE1 = 'You wrote a letter in {} ,try number'
try:
    a = float(input(TEMPLATE.format('a')))
    b = float(input(TEMPLATE.format('b')))
    c = float(input(TEMPLATE.format('c')))
    res = ((11 + 2 * a + 4.1) / (12.4 - b)) + c
    print(res)
except ValueError:
    print('You enter a letter,try to enter number')
