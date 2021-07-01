clang -emit-llvm -c solution.c
klee solution.bc
python3 extract_test_cases.py klee-out-0 > testcases.txt
python3 script.py $1
rm -r klee-out-0
rm testcases.txt
rm solution.bc
rm -r klee-last