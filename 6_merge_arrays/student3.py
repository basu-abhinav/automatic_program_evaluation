import sys


def func(N1: int, N2: int, A1: list[int], A2: list[int]) -> list[int]:
    ANS = []
    A1_index=0
    A2_index=0
    index_sum=0

    for x in A1:
        ANS.append(x)
    for x in A2:
        ANS.append(x)
    return ANS


input_file = open(sys.argv[1],"r")

text = input_file.readlines()

N1 = int(text[0].strip().split()[0])
N2 = int(text[0].strip().split()[1])

A1 = [int(x.strip()) for x in text[1].split()[0:N1]]
A2 = [int(x.strip()) for x in text[1].split()[N1:N1+N2]]

print(func(N1,N2,A1,A2))
