// The implementation and plotting scripts are adapted from: 
// {https://github.com/Chamarthikrishnamadhur/ID1063/tree/master/10-09-2026}

#include<stdio.h>
#include<math.h>
int main(){
	double x=1;
	//Newton raphson iteration
	for (int i=0;i<50;i++){
		//printf("%lf\n",x);
		
		x=x-1+2*exp(-1*x); //using Difference eqn to find subsequent values of x
	}
	printf("Newton raphson gave %lf\n",x);
}
