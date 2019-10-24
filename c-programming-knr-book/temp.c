#include <stdio.h>

// if you don't explicitly declare a return type, it defaults to int
main() {
  // memory allocation on the stack happens here
  int fahr, celsius;
  int lower, upper, step;

  // writing values to memmory happens here
  lower = 0;
  upper = 300;
  step = 20;

  fahr = lower;
  while (fahr <= upper){
    celsius = 5 * (fahr - 32) / 9;
    printf("%3d %6d\n", fahr, celsius);
    fahr = fahr + step;
  }
}