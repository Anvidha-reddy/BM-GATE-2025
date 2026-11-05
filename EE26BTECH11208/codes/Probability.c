#include <stdio.h>
#include<stdlib.h>
#include <time.h>
void roll(int*b);
int main(void){
  int hit=0;
  int fail=0;
  srand(time(NULL));
  int a[]={0,0,0};
  for (int i=0;i<1000000;i++){
  roll(a);
  if ((a[0]==6 && a[1]!=6 && a[2]!=6)||(a[0]!=6 && a[1]!=6 && a[2]==6)||(a[0]!=6 && a[1]==6 && a[2]!=6)){
  //printf("hit");
  hit+=1;
  //printf("%d %d %d",a[0],a[1],a[2]);
  }
  else{
  fail+=1;
  }
  }
  printf("hits %d, Fail %d\n",hit,fail);
  printf("\nratio=%lf\n",(double)(hit)/(hit+fail)); 
  
  return 0;
}
void roll(int*b){
b[0]=rand()%6+1;
b[1]=rand()%6+1;
b[2]=rand()%6+1;
}

