// The implementation and plotting scripts are adapted from: 
// {https://github.com/Chamarthikrishnamadhur/ID1063/tree/master/07-09-26/BACTERIA}
#include<stdio.h>
#include<math.h>
double euler(double y){
	return (y+0.01*(log(2)*(y+2))); //using given expression
}
int main(){
	double y=1;
	double h=0.01; //initial input for dat files
	double x=0;
	FILE *fp1=fopen("y.dat","w"); //creating dat files for plotting in python
	FILE *fp2=fopen("x.dat","w");
	for (int i=0;i<200;i++){	
	fprintf(fp1,"%lf\n",euler(y)); //writing on the dat files 
	y=euler(y);
	fprintf(fp2,"%lf\n",x);
	x+=h;

	}
}

