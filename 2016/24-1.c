#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <openssl/evp.h>

struct node {
    int value;
    struct node *next;
};

struct queue {
    struct node *head;
    struct node *tail;
};

struct queue *createQueue() {
    struct queue *q = (struct queue *) malloc(sizeof(struct queue));
    q->head = NULL;
    q->tail = NULL;
    return q;
}

void enqueue(struct queue *q, int value) {
    struct node *n = (struct node *) malloc(sizeof(struct node));
    n->value = value;
    n->next = NULL;
    if (q->head == NULL) {
        q->head = n;
        q->tail = n;
        return;
    }
    q->tail->next = n;
    q->tail = n;
}

int dequeue(struct queue *q) {
    struct node *tmp = q->head;
    int value = tmp->value;
    q->head = q->head->next;
    free(tmp);
    return value;
}

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

/**
 * Returns the distances to each goal node from 1 to numGoalNodes
 * in an array, using BFS
 */
int *getDistancesBFS(char **grid, int startX, int startY, int numGoalNodes) {
    int numRows = 37;
    int numCols = 179;
    bool **visited = (bool **) malloc(numRows * sizeof(bool *));
    for (int i = 0; i < numRows; i++) {
        visited[i] = (bool *) malloc(numCols * sizeof(bool));
        for (int j = 0; j < numCols; j++) {
            visited[i][j] = false;
        }
    }

    int *distances = (int *) malloc(numGoalNodes * sizeof(int));
    visited[startX][startY] = true;
    struct queue *qx = createQueue();
    struct queue *qy = createQueue();
    struct queue *qd = createQueue();
    enqueue(qx, startX);
    enqueue(qy, startY);
    enqueue(qd, 0);

    while (numGoalNodes) {
        int x = dequeue(qx);
        int y = dequeue(qy);
        int distance = dequeue(qd);
        char square = grid[x][y];
        if (square != '.' && square != '0') {
            /* printf("FOUND DISTANCE %d FOR %c AT SQUARE x=%d, y=%d\n", distance, square, x, y); */
            distances[square - 49] = distance;
            numGoalNodes--;
        }
        int neighborXs[] = {x-1, x, x+1, x};
        int neighborYs[] = {y, y-1, y, y+1};
        for (int i = 0; i < 4; i++) {
            int nX = neighborXs[i];
            int nY = neighborYs[i];
            char nSquare = grid[nX][nY];
            if (nSquare != '#' && !visited[nX][nY]) {
                enqueue(qx, nX);
                enqueue(qy, nY);
                enqueue(qd, distance+1);
                visited[nX][nY] = true;
            }
        }
    }
    return distances;
}

int main(int argc, char **argv) {
    char *filename = "24.txt";
    if (argc >= 2) {
        filename = argv[1];
    }
    int numLines;
    char **lines = getfilelines(filename, &numLines);
    if (lines == NULL) {
        printf("couldn't read the file dumbass\n");
        exit(1);
    }

    int lineLength = strlen(lines[0]);
    int goalsX[10];
    int goalsY[10];
    int numGoalNodes = -1;
    for (int i = 0; i < numLines; i++) {
        for (int j = 0; j < lineLength; j++) {
            char square = lines[i][j];
            if (square != '.' && square != '#') {
                int num = square - 48;
                goalsX[num] = i;
                goalsY[num] = j;
                numGoalNodes++;
            }
        }
    }
    int startX = goalsX[0];
    int startY = goalsY[0];
    printf("starting at x=%d, y=%d, and searching for %d locations\n", startX, startY, numGoalNodes);

    bool found[numGoalNodes] = {};
    int totalDistance = 0;
    int last = 0;
    int lastX = goalsX[0];
    int lastY = goalsY[0];
    for (int i = 0; i < numGoalNodes; i++) {
        printf("searching from %d, distances array:\n", last);
        int *distances = getDistancesBFS(lines, lastX, lastY, numGoalNodes);
        printArray(distances, numGoalNodes);
        // min distance to a node that HASN'T been found yet
        int minDistance = 999999;
        int closestNode = -1;
        for (int j = 0; j < numGoalNodes; j++) {
            if (!found[j] && j != last && distances[j] < minDistance) {
                minDistance = distances[j];
                closestNode = j;
            }
        }
        printf("closest goal is %d\n", closestNode);
        found[closestNode] = true;
        last = closestNode;
        lastX = goalsX[last+1];
        lastY = goalsY[last+1];
        totalDistance += minDistance;
    }
    printf("total distance traveled: %d\n", totalDistance);
    return 0;
}
