#include <stdio.h>

// if you don't explicitly declare a return type, it defaults to int
main() {
  // memory allocation on the stack happens here
  float fahr, celsius;
  int lower, upper, step;

  // writing values to memmory happens here
  lower = 0;
  upper = 300;
  step = 20;

  fahr = lower;
  while (fahr <= upper){
    celsius = (5.0 / 9.0) * (fahr - 32);
    // 3.0f: 3 total characters, 0 are after decimal place
    // 6.1f: 6 total characters, 1 is after decimal place
    printf("%3.0f %6.1f\n", fahr, celsius);
    fahr = fahr + step;
  }
}