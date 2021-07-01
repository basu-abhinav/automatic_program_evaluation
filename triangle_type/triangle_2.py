import sys

def triangle_type(a:int, b:int, c:int) -> int:
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return -1
    elif c*c > a*a + b*b:
        return 3
    elif c*c < a*a + b*b:
        return 1
    else:
        return 2


print(triangle_type(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
