#include <stdio.h>

const int b = 5;

int foo()
{
  int a = b + 5;
  return a;
}

int bar()
{
  int b = 2;
  return foo();
}

int main()
{
  printf("%d\n", foo());
  printf("%d\n", bar());
  return 0;
}

