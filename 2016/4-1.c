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
    int sum = 0;
    for (int i = 0; i < numLines; i++) {
        char *line = lines[i];
        int lineLen = strlen(line);
        int sectorID = atoi(line+lineLen-10);
        line[lineLen-11] = '\0';
        line[lineLen-1] = '\0';
        char *checksum = &line[lineLen-6];
        int alphaCount[26+97];
        for (int j = 97; j < 26+97; j++) {
            alphaCount[j] = 0;
        }
        int nameLen = strlen(line);
        for (int j = 0; j < nameLen; j++) {
            char c = line[j];
            if (c == '-') continue;
            alphaCount[(int) c]++;
        }

        printf("%s %s %d\n", line, checksum, sectorID);
        int real = 1;
        for (int j = 0; j < 4; j++) {
            char c1 = checksum[j];
            char c2 = checksum[j+1];
            int count1 = alphaCount[(int) c1];
            int count2 = alphaCount[(int) c2];
            printf("%d->%d ", count1, count2);
            if (count1 < count2) {
                real = 0;
                break;
            } else if (count1 == count2 && checksum[j] > checksum[j+1]) {
                real = 0;
                break;
            }
        }
        char *top5 = (char *) malloc(27 * sizeof(char));
        for (int j = 0; j < 27; j++) {
            top5[j] = '\0';
        }
        int currentTop5 = 0;
        for (int j = 97; j < 26+97; j++) {
            int lessCount = 0;
            for (int k = 97; k < 26+97; k++) {
                if (j == k) continue;
                if (alphaCount[j] < alphaCount[k]) lessCount++;
            }
            if (lessCount < 5) {
                top5[currentTop5] = (char) j;
                currentTop5++;
            }
        }
        printf("\n%s %s\n", top5, checksum);

        int top5Len = strlen(top5);
        int allTop5 = 1;
        for (int j = 0; j < 5; j++) {
            int jInTop5 = 0;
            for (int k = 0; k < top5Len; k++) {
                if (checksum[j] == top5[k]) {
                    jInTop5 = 1;
                    break;
                }
            }
            if (jInTop5 == 0) {
                allTop5 = 0;
                break;
            }
        }

        for (int j = 97; j < 26+97; j++) {
            printf("%c-%d ", j, alphaCount[j]);
        }
        printf("\n");
        if (real && allTop5) {
            printf("YES REAL\n\n");
            sum += sectorID;
        } else {
            printf("NOT REAL\n\n");
        }
    }
    printf("%d\n", sum);
    return 0;
}
