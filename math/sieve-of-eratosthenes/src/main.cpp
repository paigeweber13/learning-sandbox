#include <iostream>

#include "sieve-of-eratosthenes.hpp"

int main(int argc, char** argv) {
  auto primes = findPrimes(100);

  for (auto x : primes) {
    std::cout << x << " ";
  }
  std::cout << std::endl;

  return 0;
}
