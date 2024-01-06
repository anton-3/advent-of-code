#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "md5.h"

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
 * read doubles from a single string and return as an array
 */
double *readdoubles(char *str, int *numDoubles) {
    char *s1 = (char *) malloc(strlen(str) * sizeof(char));
    char *s2 = (char *) malloc(strlen(str) * sizeof(char));
    strcpy(s1, str);
    strcpy(s2, str);
    *numDoubles = 0;
    char *token = strtok(s1, " ");
    while (token != NULL) {
        (*numDoubles)++;
        token = strtok(NULL, " ");
    }
    double *doubles = (double *) malloc((*numDoubles) * sizeof(double));
    int i = 0;
    token = strtok(s2, " ");
    while (token != NULL) {
        doubles[i] = atof(token);
        i++;
        token = strtok(NULL, " ");
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

char *md5(char *str) {
    uint8_t result[16];
    md5String(str, result);
    char *hash = (char *) malloc(33 * sizeof(char));
    hash[32] = '\0';
    char *pHash = hash;
    for (int i = 0; i < 16; i++) {
        pHash += sprintf(pHash, "%02X", result[i]);
    }
    return hash;
}

int main(int argc, char **argv) {
    char password[9] = {'\0'};
    char input[] = "abc";
    char temp[100];
    int j = 0;
    int validPass = 0;
    for (int i = 0; i < 999; i++) {
        while (1) {
            strcpy(temp, input);
            char intStr[20];
            snprintf(intStr, 20, "%d", j);
            strcat(temp, intStr);
            char *hash = md5(temp);
            int valid = 1;
            for (int k = 0; k < 5; k++) {
                if (hash[k] != '0') {
                    valid = 0;
                    break;
                }
            }
            j++;
            if (valid) {
                char c = hash[5];
                //printf("%c\n", c);
                if (c == '8' || c == '9' || c == 'A' || c == 'B' || c == 'C' || c == 'D' || c == 'E' || c == 'F') {
                    //printf("skipping\n");
                    continue;
                }
                //printf("FOUND: %s %s\n", temp, hash);
                char d = hash[6];
                hash[6] = '\0';
                if (password[hash[5]-'0'] == '\0') password[hash[5]-'0'] = d;
                if (strlen(password) == 8) validPass = 1;
                break;
            }
        }
        if (validPass) break;
    }
    printf(password);
    return 0;
}
