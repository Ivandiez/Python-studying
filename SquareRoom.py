s = input()
Pi = 3.14

if s == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())

    p = (a + b + c) / 2
    result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(result)

elif s == 'прямоугольник':
    a = int(input())
    b = int(input())

    result = a * b
    print(result)

elif s == 'круг':
    r = int(input())

    result = Pi * (r ** 2)
    print(result)
