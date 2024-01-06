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
  char filename[] = "2.txt";
  int numLines;
  char **lines = getfilelines(filename, &numLines);
  if (lines == NULL) {
    printf("couldn't read the file dumbass\n");
    exit(1);
  }
  char code[] = "XXXXX";
  char keypad[5][5] = {{' ', ' ', '1', ' ', ' '}, {' ', '2', '3', '4', ' '}, {'5', '6', '7', '8', '9'}, {' ', 'A', 'B', 'C', ' '}, {' ', ' ', 'D', ' ', ' '}};

  int x = 0, y = -2;
  for (int i = 0; i < numLines; i++) {
    char *line = lines[i];
    int lineLen = strlen(line);
    for (int j = 0; j < lineLen; j++) {
      int oldx = x, oldy = y;
      switch(line[j]) {
        case 'R':
          y += 1;
          break;
        case 'L':
          y -= 1;
          break;
        case 'U':
          x -= 1;
          break;
        case 'D':
          x += 1;
          break;
      }
      if (abs(x)+abs(y) > 2) {
        x = oldx;
        y = oldy;
      }
    }
    printf("x=%d, y=%d\n", x+2, y+2);
    code[i] = keypad[x+2][y+2];
  }

  printf("%s\n", code);
  return 0;
}
