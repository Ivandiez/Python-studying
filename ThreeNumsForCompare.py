a = int(input())
b = int(input())
c = int(input())

if c <= b <= a:
    print(a)
    print(c)
    print(b)
elif b <= c <= a:
    print(a)
    print(b)
    print(c)
elif a <= c <= b:
    print(b)
    print(a)
    print(c)
elif c <= a <= b:
    print(b)
    print(c)
    print(a)
elif b <= a <= c:
    print(c)
    print(b)
    print(a)
elif a <= b <= c:
    print(c)
    print(a)
    print(b)
