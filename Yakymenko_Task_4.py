import math

print('Multiparadigmatic  programming languages:Task_4\nYakymenko Semen:IKM-221a, Twenty-third(23) on the list')


found = False
while not found:
    def validate_inp():
        while True:
            try:
                return int(input('Enter n: '))
            except ValueError:
                print('You wrote a letter,try to enter number')
    n = validate_inp()
    if n > 0:
        if n <= 12:
            for i in range(1, math.factorial(n)):
                if math.factorial(n) / i / (i + 1) == i + 2:
                    print(f'Program is working | {i} * {i + 1} * {i+2} = {(i * (i + 1) * (i + 2))}')
                    print(f'Job Check | {n}! is {math.factorial(n)} ')
                    found = True
                    break
            else:
                print('There are no such a numbers')
        else:
            print(f'Your number is too big | Try to enter something less than {n}')
    else:
        print(f'Your number is negative or equals 0 | Try yo enter something more than {n}')
