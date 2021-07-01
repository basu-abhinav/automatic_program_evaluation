import sys

def merge(N1:int,N2:int,A1:list[int],A2:list[int]):
    ANS = []
    i = 0
    j = 0

    while i<N1 and j<N2:
        if A1[i] < A2[j]:
            ANS.append(A1[i])
            i = i + 1
        else:
            ANS.append(A2[j])
            j = j + 1
    
    while i<N1:
        ANS.append(A1[i])
        i = i + 1
    
    while j<N2:
        ANS.append(A2[j])
        j = j + 1
    
    return ANS



input_file = open(sys.argv[1],"r")

text = input_file.readlines()

N1 = int(text[0].strip().split()[0])
N2 = int(text[0].strip().split()[1])

A1 = [int(x.strip()) for x in text[1].split()[0:N1]]
A2 = [int(x.strip()) for x in text[1].split()[N1:N1+N2]]

print(merge(N1,N2,A1,A2))
