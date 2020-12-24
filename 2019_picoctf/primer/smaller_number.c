#include <stdio.h>
int main(int argc, char **argv)
{
    int x=2;
    int y=5;
    int result=y^((x^y)&-(x<y));
    printf("this is the smallest number %d \n", result);
    return 0;
}
