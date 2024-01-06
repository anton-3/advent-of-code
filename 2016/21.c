#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <openssl/evp.h>

/**
 * read all lines from a file and return as an array of strings
 */
char **getfilelines(char *filename, int *numLines) {
    FILE *f = fopen(filename, "r");
    if (f == NULL) {
        return NULL;
    }
    int n = 1000; // max line length, increase this if it breaks
    char buffer[n];
    char *line = fgets(buffer, n, f);
    *numLines = 0;
    while (line != NULL) {
        (*numLines)++;
        line = fgets(buffer, n, f);
    }
    char **lines = (char **) malloc((*numLines) * sizeof(char *));
    rewind(f);
    line = fgets(buffer, n, f);
    int currentLine = 0;
    while (line != NULL) {
        int lineLen = strlen(line);
        lines[currentLine] = (char *) malloc(lineLen * sizeof(char) + 1);
        strcpy(lines[currentLine], line);
        // remove newline character at the end of each line
        if (lines[currentLine][lineLen-1] == '\n') {
            lines[currentLine][lineLen-1] = '\0';
        }
        currentLine++;
        line = fgets(buffer, n, f);
    }
    return lines;
}

/**
 * print an array of integers
 */
void printArray(int *array, int size) {
    printf("{ ");
    for (int i = 0; i < size; i++) {
        printf("%d", array[i]);
        if (i < size-1) printf(", ");
    }
    printf(" }\n");
}

/**
 * read doubles from a single string and return as an array
 */
double *readdoubles(char *str, int *numDoubles) {
    char *s1 = (char *) malloc((strlen(str)+1) * sizeof(char));
    char *s2 = (char *) malloc((strlen(str)+1) * sizeof(char));
    strcpy(s1, str);
    strcpy(s2, str);
    *numDoubles = 0;
    char delim[] = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char *token = strtok(s1, delim);
    while (token != NULL) {
        (*numDoubles)++;
        token = strtok(NULL, delim);
    }
    double *doubles = (double *) malloc((*numDoubles) * sizeof(double));
    int i = 0;
    token = strtok(s2, delim);
    while (token != NULL) {
        doubles[i] = atof(token);
        i++;
        token = strtok(NULL, delim);
    }
    free(s1);
    free(s2);
    return doubles;
}

/**
 * read integers from a single string and return as an array
 */
int *readints(char *str, int *numInts) {
    double *doubles = readdoubles(str, numInts);
    int *ints = (int *) malloc((*numInts) * sizeof(int));
    for (int i = 0; i < *numInts; i++) {
        ints[i] = (int) doubles[i];
    }
    free(doubles);
    return ints;
}

/**
 * converts an integer to a string
 */
char *itoa(int value, char *result, int base) {
    if (base < 2 || base > 36) {
        *result = '\0';
        return result;
    }

    char *ptr = result;
    char *ptr1 = result;
    char tmp_char;
    int tmp_value;
    bool is_negative = false;

    if (value < 0 && base == 10) {
        is_negative = true;
        value = -value;
    }

    do {
        tmp_value = value;
        value /= base;
        *ptr++ = "0123456789abcdefghijklmnopqrstuvwxyz"[tmp_value % base];
    } while (value);

    if (is_negative) {
        *ptr++ = '-';
    }

    *ptr = '\0';

    // Reverse the string
    for (ptr--; ptr1 < ptr; ptr1++, ptr--) {
        tmp_char = *ptr;
        *ptr = *ptr1;
        *ptr1 = tmp_char;
    }

    return result;
}

/**
 * return hex digest of md5 hash of a string
 */
char *md5(char *string) {
    EVP_MD_CTX *mdctx;
    unsigned char result[EVP_MAX_MD_SIZE];
    unsigned int result_len = EVP_MAX_MD_SIZE;

    mdctx = EVP_MD_CTX_new();
    EVP_DigestInit_ex(mdctx, EVP_md5(), NULL);
    EVP_DigestUpdate(mdctx, string, strlen(string));
    EVP_DigestFinal_ex(mdctx, result, &result_len);
    EVP_MD_CTX_free(mdctx);

    char *hash = (char *)malloc((result_len * 2) + 1);
    hash[result_len * 2] = '\0';
    for (unsigned int i = 0; i < result_len; i++) {
        sprintf(hash + (i * 2), "%02x", result[i]);
    }

    return hash;
}

void swapPositions(char *s, int x, int y) {
    char temp = s[x];
    s[x] = s[y];
    s[y] = temp;
}

void swapLetters(char *s, char a, char b) {
    int x = 0;
    int y = 0;
    while (s[x] != a) x++;
    while (s[y] != b) y++;
    swapPositions(s, x, y);
}

void reverse(char *s, int left, int right) {
    right++;
    for (int i = left; i < (left+right)/2; i++) {
        char temp = s[i];
        s[i] = s[right-i-1+left];
        s[right-i-1+left] = temp;
    }
}

void rotate(char *s, int n) {
    int l = strlen(s);
    for (int i = 0; i < n; i++) {
        char last = s[l-1];
        for (int j = l-1; j > 0; j--) {
            s[j] = s[j-1];
        }
        s[0] = last;
    }
}

void rotatePosition(char *s, char a) {
    int n = 1;
    int index = 0;
    while (s[index] != a) index++;
    n += index;
    if (index >= 4) n++;
    rotate(s, n);
}

void move(char *s, int x, int y) {
    int l = strlen(s);
    char c = s[x];
    for (int i = x; i < l-1; i++) {
        s[i] = s[i+1];
    }
    for (int i = l-1; i > y; i--) {
        s[i] = s[i-1];
    }
    s[y] = c;
}

int main(int argc, char **argv) {
    char *filename = "i.txt";
    int numLines;
    char **lines = getfilelines(filename, &numLines);
    if (lines == NULL) {
        printf("couldn't read the file dumbass\n");
        exit(1);
    }

    int numLines2;
    char **lines2 = getfilelines("wordlist.txt", &numLines2);

    for (int j = 0; j < numLines2; j++) {
        char s[9];
        strcpy(s, lines2[j]);
        char original[9];
        strcpy(original, s);
        int l = strlen(s);

        for (int i = 0; i < numLines; i++) {
            int numInts;
            char *line = lines[i];
            if (line[0] == 's') {
                if (line[5] == 'p') {
                    int *ints = readints(line, &numInts);
                    swapPositions(s, ints[0], ints[1]);
                } else {
                    char a = line[12];
                    char b = line[26];
                    swapLetters(s, a, b);
                }
            } else if (line[6] == ' ') {
                // rotate
                if (line[7] == 'r') {
                    int *ints = readints(line, &numInts);
                    rotate(s, ints[0]);
                } else if (line[7] == 'l') {
                    int *ints = readints(line, &numInts);
                    rotate(s, l-ints[0]);
                } else {
                    char c = line[strlen(line)-1];
                    rotatePosition(s, c);
                }
            } else if (line[7] == ' ') {
                // reverse
                int *ints = readints(line, &numInts);
                reverse(s, ints[0], ints[1]);
            } else {
                int *ints = readints(line, &numInts);
                move(s, ints[0], ints[1]);
            }
            /* printf("%s - %s\n", s, line); */
        }
        printf("%s -> %s\n", original, s);
    }
    return 0;
}
