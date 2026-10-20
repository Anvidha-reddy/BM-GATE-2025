//code by GVV Sharma
//April 30 2025
//find the pivot index and median of given data
//using the quicksort algorithm
#include <stdio.h>

//Declaring functions 
int Pindex(int *a, int low, int high);
void swap(int *a,int *b);//swap two numbers
void printData(int *a, int n);
void median(int *a, int n);
void quicksort(int data[], int low, int high); 

//begin main function
int main() {
int data[]={130, 137, 138, 138, 144,160, 146,149,154,156};
    int n = sizeof(data)/sizeof(data[0]);

    printf("Original data:\n");
    printData(data, n);

    quicksort(data, 0, n - 1);

    printf("\nSorted data:\n");
    printData(data, n);

    //print median
    printf("\n%lf\n",(double)(data[n/2-1]+data[n/2])/2);
    
    return 0;
}

//end main function

//Swap two numbers
void swap(int *a,int *b){
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}
void printData(int *a, int n){
  for (int i = 0; i < n; i++){
	  printf("%d ",a[i]);
  }
}

//pivot index function
int Pindex(int *a, int low, int high){
	int i;
  for ( i = low; i < high; i++){
	  if(a[i] > a[high]){
		  swap(&a[i], &a[high]);
	  }
  }
  return i; //returning the pivot index  
  }
//end pivot index function

// Quicksort function
void quicksort(int data[], int low, int high) {
    if (low < high) {
        // Partition index
   	int pi = Pindex(data, low, high);

        // Recursively sort elements before and after partition
        quicksort(data, low, pi - 1);
        quicksort(data, pi + 1, high);
    }
}


