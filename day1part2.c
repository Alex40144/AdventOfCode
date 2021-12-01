#include <stdio.h>
#include <stdlib.h>

int previous[3] = {0,0,0};
int previousSum = 999;
int sum;
int count = 0;
int current;

int main(void) {
    FILE *fp;

    fp=fopen("day1.txt", "r");

    while(fscanf(fp, "%d", &current) != EOF) {
        previous[2] = previous [1];
        previous[1] = previous[0];
        previous[0] = current;

        if (previous[2] == 0) {
            continue;
        }

        sum = previous[2] + previous[1] + previous[0];

        if (sum > previousSum) {
            count ++;
        }
        previousSum = sum;
    }

    fclose(fp);
    printf("%d", count);

    return 0;
}