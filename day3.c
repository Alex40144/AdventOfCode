#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int common[12];

char line[20];

int strlen(char str[]) {
    int i = 0;
    for (i = 0; str[i] != '\0'; ++i);
    return i -1;
}

int main(void) {
    FILE *fp;
    fp=fopen("day3.txt", "r");

    while(fgets(line, 20, fp)) {
        for (int i = 0; i < strlen(line); i++)
            if(line[i] == '1') {
                common[i]++;
            } else {
                common[i]--;
            }
    }
    fclose(fp);
    int gamma = 0b00000;
    int epsilon = 0b00000;
    for (int i = 0; i < strlen(line); i++) {
        if (common[i] > 0) {
            gamma |= (int)pow(2, strlen(line)-i -1);
        } else {
            epsilon |= (int)pow(2, strlen(line)-i -1);
        }
    }
    printf("%d", gamma * epsilon);

    return 0;
}