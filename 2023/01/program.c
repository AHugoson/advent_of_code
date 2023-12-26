#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* converts words to digits */
char num_from_str(char buf[])
{
    if (strncmp(buf, "zero", 4) == 0) {
        return '0';
    } else if (strncmp(buf, "one", 3) == 0) {
        return '1';
    } else if (strncmp(buf, "two", 3) == 0) {
        return '2';
    } else if (strncmp(buf, "three", 5) == 0) {
        return '3';
    } else if (strncmp(buf, "four", 4) == 0) {
        return '4';
    } else if (strncmp(buf, "five", 4) == 0) {
        return '5';
    } else if (strncmp(buf, "six", 3) == 0) {
        return '6';
    } else if (strncmp(buf, "seven", 5) == 0) {
        return '7';
    } else if (strncmp(buf, "eight", 5) == 0) {
        return '8';
    } else if (strncmp(buf, "nine", 4) == 0) {
        return '9';
    }
    return '\0';
}

int main()
{
    char buf[64];
    long sum_p1 = 0, sum_p2 = 0;

    // loop through input line-by-line
    while (fgets(buf, sizeof(buf), stdin) != NULL) {
        char num_string_p1[3] = "";
        char num_string_p2[3] = "";
        printf("-----=-----\n%s", buf);

        // loop through chars on current line
        for (int i=0; i<sizeof(buf); i++) {
            if (buf[i] == '\0') {
                break;
            } else if ('0' <= buf[i] && buf[i] <= '9') {
                // first found numerals
                if (num_string_p1[0] == '\0') {
                    num_string_p1[0] = buf[i];
                }
                if (num_string_p2[0] == '\0') {
                    num_string_p2[0] = buf[i];
                }
                // update last found number
                num_string_p1[1] = buf[i];
                num_string_p2[1] = buf[i];
            } else {
                // get numerals for 'one', 'two', ...
                char p2_found_num = num_from_str(buf+i);

                if (p2_found_num != '\0') {
                    // first found number()
                    if (num_string_p2[0] == '\0') {
                        num_string_p2[0] = p2_found_num;
                    }
                    // update last found number
                    num_string_p2[1] = p2_found_num;
                }
            } 
        }
        // print the number for the line, sum it
        printf("P1: %s | P2: %s\n", num_string_p1, num_string_p2);
        sum_p1 += atoi(num_string_p1);
        sum_p2 += atoi(num_string_p2);
    }
    printf("\nSum of calibration values: {P1: %ld} {P2: %ld}\n", sum_p1, sum_p2);
    return 0;
}
