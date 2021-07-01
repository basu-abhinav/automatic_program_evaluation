import sys
import re

input_filename = sys.argv[1]
#input_filename = "testcases.txt"
output_filename = sys.argv[2]
#output_filename = "input.txt"
value_count = int(sys.argv[3])


input_file = open(input_filename,"r")

lines = input_file.readlines()

test_cases = {}

count = 1
for i in range(len(lines)):
    if lines[i].strip() == "Test suite:":
        for j in range(i+1,len(lines)):
            if len(lines[j].split()) == value_count:
                test_cases[count] = lines[j].split()
                count = count + 1
        break

output_file = open(output_filename,"a+")

for x in test_cases:
    temp = []
    for y in test_cases[x]:
        temp.append(int(y.removeprefix("=").removesuffix(",")))
    test_cases[x] = temp
    for y in test_cases[x]:
        output_file.write(str(y) + " ")
    output_file.write("\n")

print(len(test_cases))
