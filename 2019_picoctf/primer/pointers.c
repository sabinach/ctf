#include <stdio.h>
int main()
{
    int arr[5];
    arr[0]=11;
    arr[1]=12;
    arr[2]=13;
    arr[3]=14;
    arr[4]=15;
    for(int i=0;i<5;i++)
    {
        printf("Array value at position %i: %i \n",i, arr[i]);
    }
    printf("Array value at position 7: %i \n", arr[6]);
}
