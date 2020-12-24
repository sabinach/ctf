#include <stdio.h>

// To view assembly:
// objdump --disassemble compare_to_five > compare_to_five.txt

// Dump specific function ie main():
// gdb -batch -ex 'file compare_to_five' -ex 'disassemble main'

int main( ) {
   int i;
   printf( "Enter a value :");
   scanf("%d", &i);
   if(i>5){
       printf("Greater than 5");
   }else {
       printf("Less or equal than 5");
   }
   return 0;
}
