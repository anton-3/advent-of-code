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

int main(int argc, char **argv) {
    char *filename = "18.txt";
    /* if (argc >= 2) { */
    /*     filename = argv[1]; */
    /* } */
    int numLines;
    char **lines = getfilelines(filename, &numLines);
    if (lines == NULL) {
        printf("couldn't read the file dumbass\n");
        exit(1);
    }
    char *line = lines[0];
    int lineLen = strlen(line);
    int numRows = 400000;
    int **map = (int **) malloc(numRows * sizeof(int *));
    for (int i = 0; i < numRows; i++) {
        map[i] = (int *) malloc(lineLen * sizeof(int));
    }
    /* printf(" 0 "); */
    for (int i = 0; i < lineLen; i++) {
        map[0][i] = 0;
        if (line[i] == '^') map[0][i] = 1;
        /* printf("%c", line[i]); */
    }
    /* printf("\n"); */
    for (int i = 1; i < numRows; i++) {
        /* printf("%2d ", i); */
        map[i][0] = 0;
        map[i][lineLen-1] = 0;
        if ((map[i-1][0] && map[i-1][1]) || (map[i-1][1] && !map[i-1][0])) {
            map[i][0] = 1;
        }
        /* printf("%c", map[i][0] ? '^' : '.'); */
        if ((map[i-1][lineLen-1] && map[i-1][lineLen-2]) || (map[i-1][lineLen-2] && !map[i-1][lineLen-1])) {
            map[i][lineLen-1] = 1;
        }
        for (int j = 1; j < lineLen-1; j++) {
            map[i][j] = 0;
            if ((map[i-1][j-1] && map[i-1][j] && !map[i-1][j+1]) || (!map[i-1][j-1] && map[i-1][j] && map[i-1][j+1]) || (map[i-1][j-1] && !map[i-1][j] && !map[i-1][j+1]) || (!map[i-1][j-1] && !map[i-1][j] && map[i-1][j+1])) {
                map[i][j] = 1;
            }
            /* printf("%c", map[i][j] ? '^' : '.'); */
        }
        /* printf("%c", map[i][lineLen-1] ? '^' : '.'); */
        /* printf("\n"); */
    }
    int count = 0;
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < lineLen; j++) {
            if (!map[i][j]) count++;
        }
    }
    printf("%d\n", count);
    return 0;
}
