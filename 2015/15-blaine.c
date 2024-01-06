#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <openssl/evp.h>

int ten[10] = {1,      10,      100,      1000,      10000,
               100000, 1000000, 10000000, 100000000, 1000000000};

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
 * read integers from a single string and return as an array
 */
int *readints(char *str, int *numInts) {
    bool negative = true;
    *numInts = 0;
    int strLen = strlen(str);
    int currNum = 0;
    int currNumLen = 0;
    bool prevNum = false;
    for (int i = 0; i < strLen; i++) {
        char c = str[i];
        int index = c - '0';
        if (index >= 0 && index <= 9) {
            if (!prevNum) {
                prevNum = true;
                (*numInts)++;
            }
        } else {
            prevNum = false;
        }
    }
    int *ints = (int *)malloc(*numInts * sizeof(int));
    int foundInts = 0;
    for (int i = strLen - 1; i >= 0; i--) {
        char c = str[i];
        int index = c - '0';
        if (index >= 0 && index <= 9) {
            currNum += index * ten[currNumLen++];
        } else if (negative && c == '-' && currNum > 0) {
            currNum *= -1;
        } else if (currNumLen != 0) {
            ints[*numInts - ++foundInts] = currNum;
            currNum = 0, currNumLen = 0;
        }
    }
    if (currNum != 0) {
        ints[0] = currNum;
    }
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

int ingredients[4][5] = {{}};
int scoreCookie(int cookie[5]) {
    if (cookie[0] < 0 || cookie[1] < 0 || cookie[2] < 0 || cookie[3] < 0) {
        return 0;
    }
    return cookie[0] * cookie[1] * cookie[2] * cookie[3];
}
int highestScore = INT_MIN;

int main(int argc, char **argv) {
    char *filename = "15.txt";
    if (argc == 2) {
        filename = argv[1];
    }
    int numLines;
    char **lines = getfilelines(filename, &numLines);
    if (lines == NULL) {
        printf("couldn't read the file\n");
        exit(1);
    }
    printf("SET TO: %s\n", filename);
    int numInts = 0;
    for (int i = 0; i < numLines; i++) {
        char *line = lines[i];
        int numChars = strlen(line);
        int *ints = readints(line, &numInts);
        for (int j = 0; j < 5; j++) {
            ingredients[i][j] = ints[j];
        }
        free(line);
    }
    free(lines);
    for (int i1 = 0; i1 <= 100; i1++) {
        for (int i2 = 0; i2 <= 100; i2++) {
            if (i1 + i2 > 100) {
                break;
            }
            for (int i3 = 0; i3 <= 100; i3++) {
                if (i1 + i2 + i3 > 100) {
                    break;
                }
                for (int i4 = 0; i4 <= 100; i4++) {
                    if (i1 + i2 + i3 + i4 > 100) {
                        break;
                    }
                    int cookie[5] = {};
                    for (int j = 0; j < numInts; j++) {
                        cookie[j] += (ingredients[0][j] * i1) +
                                     (ingredients[1][j] * i2) +
                                     (ingredients[2][j] * i3) +
                                     (ingredients[3][j] * i4);
                    }
                    if (cookie[4] == 500) {
                        int cookieScore = scoreCookie(cookie);
                        if (cookieScore > highestScore) {
                            highestScore = cookieScore;
                            /* printf("NEW HIGH SCORE: %d\n", highestScore); */
                        }
                    }
                }
            }
        }
    }
    printf("FINAL HIGH SCORE: %d\n", highestScore);
    return 0;
}
