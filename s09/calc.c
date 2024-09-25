#include <stdio.h>

int main(void)
{
    int x, y;
    printf("x = ");
    scanf("%d", &x); // try 2 billion
    printf("y = ");
    scanf("%d", &y); // try 2 billion

    printf("sum = %d", x + y);

    // long x, y;
    // printf("x = ");
    // scanf("%ld", &x); // try 2 billion
    // printf("y = ");
    // scanf("%ld", &y); // try 2 billion

    // printf("sum = %lld", x + y);
}