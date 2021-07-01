import sys


def func(N1: int, N2: int, A1: list[int], A2: list[int]) -> list[int]:
    ANS = [0] * (N1 + N2)
    A1_index=0
    A2_index=0
    index_sum=0

    while index_sum < N1 + N2:
        if A1_index>=N1:
            ANS[index_sum] = A2[A2_index]
            A2_index = A2_index + 1
            index_sum = index_sum + 1
        elif A2_index >= N2:
            ANS[index_sum] = A1[A1_index]
            A1_index = A1_index + 1
            index_sum = index_sum + 1
        else:
            if A1[A1_index] > A2[A2_index]:
                ANS[index_sum] = A1[A1_index]
                A1_index = A1_index + 1
                index_sum = index_sum + 1
            else:
                ANS[index_sum] = A2[A2_index]
                A2_index = A2_index + 1
                index_sum = index_sum + 1    
    return ANS


input_file = open(sys.argv[1],"r")

text = input_file.readlines()

N1 = int(text[0].strip().split()[0])
N2 = int(text[0].strip().split()[1])

A1 = [int(x.strip()) for x in text[1].split()[0:N1]]
A2 = [int(x.strip()) for x in text[1].split()[N1:N1+N2]]

print(func(N1,N2,A1,A2))