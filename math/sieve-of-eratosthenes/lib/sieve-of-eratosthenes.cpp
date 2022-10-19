#include "sieve-of-eratosthenes.hpp"
#include "vector-utilities.hpp"

std::vector<int> findPrimes(int maxValue){
  auto primes = std::vector<int>();

  // add all values <= maxValue to array
  for (int x = 2; x < maxValue + 1; x++) {
    primes.push_back(x);
  }

  size_t i = 0;
  while (i < primes.size()) {
    // consider a number x. We know in the first case, x == 2, which is prime.
    int x = primes[i];
    
    size_t j = i + 1;
    while (j < primes.size()) {
      if (primes[j] % x == 0) { // if this number is a multiple of x, eliminate it.
        primes.erase(primes.begin() + j);
      }
      else j++; // else, move on to the next number
    }

    i++;
  }

  return primes;
}
