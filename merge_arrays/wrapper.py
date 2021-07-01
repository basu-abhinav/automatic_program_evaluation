import os
import sys

student_solution_filename = sys.argv[1]

config_file = open("config.txt","r")
text = config_file.readlines()

scalar_values = [int(x.strip()) for x in text[0].strip().split()]
value_count = int(text[1].strip())
unwind = int(text[2].strip())

count = 0
unwind_count = 0
while count < 10:
    command = "cbmc golden.c --cover mcdc --unwind " + str(unwind + unwind_count) + " > temp.txt"
    os.system(command)
    command = "python3 script.py temp.txt dump.txt " + str(value_count)
    n = int(os.popen(command).read().strip())
    os.system("rm temp.txt")
    count = count + n
    unwind_count = unwind_count + 1

dump_file = open("dump.txt","r")
lines = dump_file.readlines()
test_case_filenames = []
for i in range(len(lines)):
    filename = "test_case_" + str(i+1) + ".txt"
    test_case_filenames.append(filename)
    test_file = open(filename,"a+")
    test_file.write(text[0].strip() + "\n")
    test_file.write(lines[i].strip())
    test_file.close()

os.system("rm dump.txt")
score = 0
for x in test_case_filenames:
    golden = os.popen("python3 golden.py " + x).read().strip()
    student = os.popen("python3 "+ student_solution_filename + " " + x).read().strip()
    if golden == student:
        score = score + 1

print("Score : " + str(int(score/len(test_case_filenames)*100)) + " out of " + str(100))

