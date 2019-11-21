#include <stdio.h>

int x = 1;
char y = 'a';

void p(){
  double x = 25;
  printf("%c\n", y);
  {
    int y[10];
  }
}

void q(){
  int y = 42;
  printf("%d\n", x);
  p();
}

main() {
  char x = 'b';
  q();
  return 0;
}