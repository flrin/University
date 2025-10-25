#include <stdio.h>

int to_int(char sir[]);

int main(){
    char text[100];
    for(;;){
        scanf("%s", text);
        if(text[0] == '0'){
            break;
        }
        int n = to_int(text);
        printf("%d\n", n);
    }
    return 0;
}