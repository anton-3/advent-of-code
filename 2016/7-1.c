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
    char *filename = "7.txt";
    if (argc >= 2) {
        filename = argv[1];
    }
    int numLines;
    char **lines = getfilelines(filename, &numLines);
    if (lines == NULL) {
        printf("couldn't read the file dumbass\n");
        exit(1);
    }
    int count = 0;
    for (int i = 0; i < numLines; i++) {
        char *line = lines[i];
        int len = strlen(line);
        int lefts[10] = {0};
        int numLefts = 0;
        int rights[10] = {0};
        int numRights = 0;
        for (int j = 0; j < len; j++) {
            char c = line[j];
            if (c == '[') {
                lefts[numLefts++] = j;
            } else if (c == ']') {
                rights[numRights++] = j;
            }
        }
        //printf("%s\n", line);
        char **outside = (char **) malloc(10 * sizeof(char*));
        char **inside = (char **) malloc(10 * sizeof(char*));
        outside[numRights] = line;
        for (int j = 0; j < numLefts; j++) {
            inside[j] = &line[lefts[j]+1];
            outside[j] = &line[rights[j]+1];
            line[lefts[j]] = '\0';
            line[rights[j]] = '\0';
        }
        int checkO = 0;
        int checkI = 1;
        // loop outsides
        for (int j = 0; j < numLefts+1; j++) {
            char *s = outside[j];
            char sLen = strlen(s);
            for (int k = 0; k < sLen-3; k++) {
                char c1 = s[k];
                char c2 = s[k+1];
                char c3 = s[k+2];
                char c4 = s[k+3];
                if (c1 != c2 && c2 == c3 && c1 == c4) checkO = 1;
            }
        }
        // loop insides
        for (int j = 0; j < numLefts; j++) {
            char *s = inside[j];
            char sLen = strlen(s);
            for (int k = 0; k < sLen-3; k++) {
                char c1 = s[k];
                char c2 = s[k+1];
                char c3 = s[k+2];
                char c4 = s[k+3];
                if (c1 != c2 && c2 == c3 && c1 == c4) checkI = 0;
            }
        }
        if (checkO && checkI) count++;
    }
    printf("%d\n", count);
    return 0;
}
