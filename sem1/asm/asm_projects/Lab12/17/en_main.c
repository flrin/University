#include <stdio.h>

int to_int(char text[]);
char* str_max(char text[]);

int main(){
    char text[100];
    FILE *fptr;
    fptr = fopen("max.txt", "w");

    scanf("%s", text);

    fprintf(fptr,"%x",to_int(str_max(text)));

    fclose(fptr);

    return 0;
}