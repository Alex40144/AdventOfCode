#include <stdio.h>
#include <stdlib.h>

int forward = 0;
int depth = 0;
int aim = 0;
char line[20];

int strlen(char str[]) {
    int i = 0;
    for (i = 0; str[i] != '\0'; ++i);
    return i -1;
}

int main(void) {
    FILE *fp;

    fp=fopen("day2.txt", "r");

    while(fgets(line, 20, fp)) {
        int value = (int)line[strlen(line)-1] -48;
        printf("%d\n",value );
        if (line[0] == 'f') {
            forward += value;
            depth += aim * value;
        } else if (line[0] == 'u') {
            aim -= value;
        } else if (line[0] == 'd') {
            aim += value;
        }
    }

    fclose(fp);
    printf("%d\n", forward);
    printf("%d\n", depth);
    printf("%d\n", forward*depth);

    return 0;
}