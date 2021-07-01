# Takes the klee-out directory name as the only argument

import os
import sys
import re

directory = sys.argv[1]

command = "cd " + directory + "\ncat info"
output = os.popen(command).read()

n_tests = re.compile("KLEE: done: generated tests = [0-9][0-9]*")
out_list = n_tests.findall(output)[0].split(" ")

n = int(out_list[len(out_list)-1])

filenames = []
for i in range(n):
    temp = "test" + str(i+1).zfill(6) + ".ktest"
    filenames.append(temp)

test_cases_dump = []
for i in range(n):
    command = "cd "+ directory + "\nktest-tool " + filenames[i]
    temp = os.popen(command).read()
    test_cases_dump.append(temp)

test_case_re = re.compile("object [0-9][0-9]*: int : .*")
test_cases = {}
for i in range(n):
    temp = test_case_re.findall(test_cases_dump[i])
    for j in range(len(temp)):
        temp2 = temp[j].split(" ")
        temp[j] = int(temp2[len(temp2)-1])
    test_cases[i+1] = temp

for x in test_cases:
    for y in test_cases[x]:
        print(y,end=" ")
    print()



