#include <stdio.h>
#include <stdlib.h>

int main()
{
    char buf[64];
    long sum = 0;

    // loop through input line-by-line
    while (fgets(buf, sizeof(buf), stdin) != NULL) {
        char num_string[3] = "";

        // loop through chars on current line
        for (int i=0; i<sizeof(buf); i++) {
            if ('0' <= buf[i] && buf[i] <= '9') {
                if (num_string[0] == '\0') {
                    // first found number
                    num_string[0] = buf[i];
                }
                // update last found number
                num_string[1] = buf[i];
            } else if (buf[i] == '\0') {
                break;
            }
        }
        // print the number for the line, sum it
        printf("%s\n", num_string);
        sum += atoi(num_string);
    }
    printf("Sum of calibration values: %ld\n", sum);
    return 0;
}
