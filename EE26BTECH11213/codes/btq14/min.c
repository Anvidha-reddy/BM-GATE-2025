// The implementation and plotting scripts are adapted from: 
// {https://github.com/Chamarthikrishnamadhur/ID1063/tree/master/07-09-26/Minimize}


#include <stdio.h>
double des(double x){
	return (x-0.3*(1-(4/(x*x)))); //apt function for gradient descent 
}
double func(double x){return x+4/x;} 
int main(){
	double x=5;
	for (int i=0;i<200;i++){
		x=des(x); //iterative gradient descent to change the guesses
	}
	printf(":%lf\n",func(x));
}
