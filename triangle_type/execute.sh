clang -emit-llvm -c golden.c
klee golden.bc
python3 extract_test_cases.py klee-out-0 > testcases.txt
python3 script.py $1
rm -r klee-out-0
rm testcases.txt
rm golden.bc
rm -r klee-last