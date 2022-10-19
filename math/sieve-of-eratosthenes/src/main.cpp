#include <iostream>

#include "sieve-of-eratosthenes.hpp"
#include "vector-utilities.hpp"

int main(int argc, char** argv) {
  auto primes = findPrimes(100);

  printVector(primes);

  return 0;
}
