#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP  20

// if you don't explicitly declare a return type, it defaults to int
main() {
  // memory allocation on the stack happens here
  float fahr;

  for (fahr = LOWER; fahr <= UPPER; fahr += STEP){
    // 3.0f: 3 total characters, 0 are after decimal place
    // 6.1f: 6 total characters, 1 is after decimal place
    printf("%3.0f %6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32));
  }
}