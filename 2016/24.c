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
    int size;
};

struct queue *createQueue() {
    struct queue *q = (struct queue *) malloc(sizeof(struct queue));
    q->head = NULL;
    q->tail = NULL;
    q->size = 0;
    return q;
}

int enqueue(struct queue *q, int value) {
    struct node *n = (struct node *) malloc(sizeof(struct node));
    if (n == NULL) return q->size;

    n->value = value;
    n->next = NULL;
    if (q->head == NULL) {
        q->head = n;
        q->tail = n;
        return q->size;
    }
    q->tail->next = n;
    q->tail = n;
    q->size += 1;
    return q->size;
}

int dequeue(struct queue *q) {
    struct node *tmp = q->head;
    int value = tmp->value;
    q->head = q->head->next;
    free(tmp);
    q->size -= 1;
    return value;
}

void freeQueue(struct queue *q) {
    if (q == NULL) return;

    while (q->head != NULL) {
        struct node *tmp = q->head;
        q->head = q->head->next;
        free(tmp);
    }

    free(q);
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
    fclose(f);
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
        if (square != '.') {
            /* printf("FOUND DISTANCE %d FOR %c AT SQUARE x=%d, y=%d\n", distance, square, x, y); */
            distances[square - 48] = distance;
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
    freeQueue(qx);
    freeQueue(qy);
    freeQueue(qd);
    for (int i = 0; i < numRows; i++) {
        free(visited[i]);
    }
    free(visited);
    return distances;
}

int findMinTourLength(char **grid, int **d, int current, int numNodes, bool *visited, int distance) {
    bool visitedAll = true;
    for (int i = 0; i < numNodes; i++) {
        visitedAll = visitedAll && visited[i];
    }
    int *distances = d[current];
    if (visitedAll) return distance + distances[0];

    int minTourLength = 999999999;
    for (int i = 0; i < numNodes; i++) {
        if (visited[i] || i == current) continue;
        visited[i] = true;
        int tourLength = findMinTourLength(grid, d, i, numNodes, visited, distance + distances[i]);
        visited[i] = false;
        if (tourLength < minTourLength) {
            minTourLength = tourLength;
        }
    }
    return minTourLength;
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
    int numGoalNodes = 0;
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

    bool visited[numGoalNodes] = {};
    visited[0] = true;
    int **distances = (int **) malloc(numGoalNodes * sizeof(int *));
    for (int i = 0; i < numGoalNodes; i++) {
        distances[i] = getDistancesBFS(lines, goalsX[i], goalsY[i], numGoalNodes);
    }
    int minTourLength = findMinTourLength(lines, distances, 0, numGoalNodes, visited, 0);
    printf("minimum tour length: %d\n", minTourLength);
    for (int i = 0; i < numLines; i++) {
        free(lines[i]);
    }
    for (int i = 0; i < numGoalNodes; i++) {
        free(distances[i]);
    }
    free(lines);
    free(distances);
    return 0;
}
