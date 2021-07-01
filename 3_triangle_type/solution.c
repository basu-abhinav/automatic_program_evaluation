#include <stdio.h>

// return -1 for Invalid Triangle
// return 1 for Acute Triangle
// return 2 for Right Triangle
// return 3 for Obtuse Triangle 
int golden_solution(int a,int b,int c)
{
	int t; 

	if (a > c)  //swap a & c
	{	t = c;
		c = a;
		a = t;
	}

	if (b > c)  //swap b & c
	{
		t = c;
		c = b;
		b = t;
	}
	// now c is the longest side

	if ( a + b <= c || b + c <= a || a + c <= b)
		return -1;

	else if (c*c > a*a + b*b)
		return 3;

	else if (c*c < a*a + b*b)
		return 1;

	else if(c*c == a*a + b*b)
	{
		return 2;
	}
	else
		return -1;
}


int main()
{
	int a,b,c;	
	klee_make_symbolic(&a,sizeof(a),"a");
	klee_make_symbolic(&b,sizeof(b),"b");
	klee_make_symbolic(&c,sizeof(c),"c");
	klee_assume(a>0);
	klee_assume(b>0);
	klee_assume(c>0);
	golden_solution(a,b,c);
	return 0;
}