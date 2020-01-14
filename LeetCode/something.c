#include "stdio.h"

int main(int argc, char const *argv[])
{
    int a[5] = {1, 2, 3, 4, 5};
    printf("%d\n", a);
    printf("%d\n", a+1);
    printf("%d\n", &a[0]);
    printf("%d\n", &a[1]);
    return 0;
}
