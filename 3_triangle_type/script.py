#   use extract_test_cases script to generate test cases
#   redirect output of above script to a file test_cases.txt
#   function uses only one input, an integer
import sys
import os

test_cases = open("testcases.txt","r")

all_cases = test_cases.readlines()

test_ints = {}
count = 1

for x in all_cases:
    test_ints[count] = [y.strip() for y in x.split()]
    count = count + 1

student = sys.argv[1]
score = 0
for x in test_ints:
    golden_command = "python3 golden.py " + " ".join(test_ints[x])
    student_command = "python3 " + str(student) + " " + " ".join(test_ints[x])
    golden_out = os.popen(golden_command).read()
    student_out = os.popen(student_command).read()
    if golden_out == student_out:
        score = score + 1

print("Score :",int(score/len(test_ints)*100),"out of 100")




