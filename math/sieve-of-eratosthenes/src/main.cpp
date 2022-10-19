#include <chrono>
#include <iostream>

#include "sieve-of-eratosthenes.hpp"
#include "vector-utilities.hpp"

void printTimingHeader() {
  std::cout << "max_value,time_taken,values_checked_per_second" << std::endl;
}

double timeSieveOfEratosthenes(uint64_t maxValue) {
  using std::chrono::high_resolution_clock;
  using std::chrono::nanoseconds;
  using std::chrono::duration_cast;

  std::vector<uint64_t> primes;

  auto start = high_resolution_clock::now();
  primes = findPrimes(100);
  auto end = high_resolution_clock::now();

  auto time_taken_nanoseconds = duration_cast<nanoseconds>(end - start);
  double time_taken_seconds = time_taken_nanoseconds.count() / 1e9;

  std::cout << maxValue << "," << time_taken_seconds << "," 
            << maxValue / time_taken_seconds << std::endl;
}

void timeSieveOfEratosthenesManySizes(uint64_t startValue, uint64_t endValue) {
  for (auto maxValue = startValue; maxValue <= endValue; maxValue *= 10) {
    timeSieveOfEratosthenes(maxValue);
  }
}

int main(int argc, char** argv) {
  std::cout << "Timing sieve of Eratosthenes" << std::endl;
  std::cout << std::endl;

  printTimingHeader();
  timeSieveOfEratosthenesManySizes(1000, 1000000000000000000ull);
  timeSieveOfEratosthenes(UINT64_MAX);

  return 0;
}
