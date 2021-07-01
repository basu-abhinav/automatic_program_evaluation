import sys

def triangle_type(a:int, b:int, c:int) -> int:   
    if a >= b:
        if a >= c:
            temp = a
            a = c
            c = temp
    else:
        if b >= c:
            temp = b
            b = c
            c = temp

    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return -1
    elif c*c > a*a + b*b:
        return 3
    elif c*c < a*a + b*b:
        return 1
    else:
        return 2


print(triangle_type(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
