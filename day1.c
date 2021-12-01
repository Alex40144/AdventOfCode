#include <stdio.h>
#include <stdlib.h>

int previous = 9999;
int count = 0;
int current;

int main(void) {
    FILE *fp;

    fp=fopen("day1.txt", "r");

    while(fscanf(fp, "%d", &current) != EOF) {
        //printf("%d\n", current);
        if (current > previous) {
            count ++;
        }
        previous = current;
    }

    fclose(fp);
    printf("%d", count);

    return 0;
}