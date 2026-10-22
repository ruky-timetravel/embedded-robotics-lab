#include <stdio.h>

int main(void)
{
    int target_speed = 100;
    int actual_speed = 80;
    int error = target_speed - actual_speed;

    printf("Speed error: %d\n", error);
    return 0;
}