import sys

def solution(a:int, b:int, c:int):
    if a > c: 
	    t = c
	    c = a
	    a = t
    if b > c:
	    t = c
	    c = b
	    b = t

    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return -1
    elif c*c > a*a + b*b:
        return 3
    elif c*c < a*a + b*b:
        return 1
    else:
        return 2

print(solution(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))