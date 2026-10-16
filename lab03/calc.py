a = float(input('Введите первое число: '))
op = str(input('Введите операцию(+, -, *, /): '))
b = float(input('Введите второе число: '))

if op=='+':
    print(a + b)
elif op=='-':
    print(a - b)
elif op=='*':
    print(a * b)
elif op=='/':
    print(a / b)
