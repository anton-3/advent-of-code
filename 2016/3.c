#include <stdlib.h>
#include <stdio.h>
#include <string.h>

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

int main(int argc, char **argv) {
  char *filename = "3.txt";
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
  for (int i = 0; i < numLines/3; i++) {
    for (int j = 0; j < 3; j++) {
      int a = atoi(lines[3*i]+5*j);
      int b = atoi(lines[3*i+1]+5*j);
      int c = atoi(lines[3*i+2]+5*j);
      if (a+b>c && a+c>b && b+c>a) {
        count++;
      }
    }
  }
  printf("%d\n", count);
  return 0;
}
