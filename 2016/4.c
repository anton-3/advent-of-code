#include <stdlib.h>
#include <stdio.h>
#include <string.h>

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

int main(int argc, char **argv) {
    char *filename = "4.txt";
    if (argc >= 2) {
        filename = argv[1];
    }
    int numLines;
    char **lines = getfilelines(filename, &numLines);
    if (lines == NULL) {
        printf("couldn't read the file dumbass\n");
        exit(1);
    }
    for (int i = 0; i < numLines; i++) {
        char *line = lines[i];
        int lineLen = strlen(line);
        int sectorID = atoi(line+lineLen-10);
        line[lineLen-11] = '\0';
        int nameLen = strlen(line);

        for (int j = 0; j < nameLen; j++) line[j] = ((((int) line[j]) - 97) + sectorID) % 26 + 97;
        printf("%d: %s\n", sectorID, line);
    }
    return 0;
}
