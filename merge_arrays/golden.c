int func(int N1, int N2, int A1[], int A2[])
{
	int ANS[N1+N2];
	int A1_index=0, A2_index=0, index_sum=0;
	while(index_sum<N1+N2){
		if (A1_index>=N1){					// Array A1 is completely merged
			ANS[index_sum] = A2[A2_index];
			A2_index++;
			index_sum++;
		}else if (A2_index>=N2){		    // Array A2 is completely merged
			ANS[index_sum] = A1[A1_index];
			A1_index++;
			index_sum++;
		}else{
			if (A1[A1_index] < A2[A2_index]){	// A1 contains smaller element
				ANS[index_sum] = A1[A1_index];
				A1_index++;
				index_sum++;
			}else{						// A2 contains smaller element
				ANS[index_sum] = A2[A2_index];
				A2_index++;
				index_sum++;
			}
		}
	}
	return 0;
}

int main()
{
	int n1=10,n2=10;
    int p1[n1];
    int p2[n2];

    for (int i = 0; i < n1; i++)
    {
        p1[i] = nondet_int();
        __CPROVER_input("", p1[i]);
    }
	__CPROVER_assume(p1[1] >= p1[0]);
	__CPROVER_assume(p1[2] >= p1[1]);
	__CPROVER_assume(p1[3] >= p1[2]);
	__CPROVER_assume(p1[4] >= p1[3]);
	__CPROVER_assume(p1[5] >= p1[4]);
	__CPROVER_assume(p1[6] >= p1[5]);
	__CPROVER_assume(p1[7] >= p1[6]);
	__CPROVER_assume(p1[8] >= p1[7]);
	__CPROVER_assume(p1[9] >= p1[8]);

    for (int i = 0; i < n2; i++)
    {
        p2[i] = nondet_int();
        __CPROVER_input("", p2[i]);
    }

	__CPROVER_assume(p2[1] >= p2[0]);
	__CPROVER_assume(p2[2] >= p2[1]);
	__CPROVER_assume(p2[3] >= p2[2]);
	__CPROVER_assume(p2[4] >= p2[3]);
	__CPROVER_assume(p2[5] >= p2[4]);
	__CPROVER_assume(p2[6] >= p2[5]);
	__CPROVER_assume(p2[7] >= p2[6]);
	__CPROVER_assume(p2[8] >= p2[7]);
	__CPROVER_assume(p2[9] >= p2[8]);

    func(n1,n2,p1,p2);
    return 0;
}