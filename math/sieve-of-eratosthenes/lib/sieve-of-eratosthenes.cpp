#include "sieve-of-eratosthenes.hpp"
#include "vector-utilities.hpp"

/* findPrimes
 * 
 * naive implementation of the sieve of eratosthenes
 * 
 * complexity: n^2
 * speed: on my machine (AMD Ryzen 5 3600), can check UINT64_MAX items for 
 *        primes in about 19 microseconds. This translates into about 9.5e+23 
 *        items checked per second
 * 
 */
std::vector<uint64_t> findPrimes(uint64_t maxValue){
  auto primes = std::vector<uint64_t>();

  // add all values <= maxValue to array
  for (uint64_t x = 2; x < maxValue + 1; x++) {
    primes.push_back(x);
  }

  size_t i = 0;
  while (i < primes.size()) {
    // consider a number x. We know in the first case, x == 2, which is prime.
    uint64_t x = primes[i];
    
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
