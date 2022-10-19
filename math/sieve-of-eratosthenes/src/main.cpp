#include <chrono>
#include <iostream>

#include "sieve-of-eratosthenes.hpp"
#include "vector-utilities.hpp"

/*
 * returns: time taken (in seconds) to check all values
 */
double timeSieveOfEratosthenes(int maxValue) {
  using std::chrono::high_resolution_clock;
  using std::chrono::nanoseconds;
  using std::chrono::duration_cast;

  std::vector<int> primes;

  auto start = high_resolution_clock::now();
  primes = findPrimes(100);
  auto end = high_resolution_clock::now();

  auto time_taken_nanoseconds = duration_cast<nanoseconds>(end - start);
  double time_taken_seconds = time_taken_nanoseconds.count() / 1e9;

  return time_taken_seconds;
}

void printTimingHeader() {
  std::cout << "max_value,time_taken,values_checked_per_second" << std::endl;
}

void timeSieveOfEratosthenesManySizes(int startValue, int endValue) {
  for (auto maxValue = startValue; maxValue <= endValue; maxValue *= 10) {
    auto time_s = timeSieveOfEratosthenes(maxValue);
    std::cout << maxValue << "," << time_s << "," << maxValue / time_s 
              << std::endl;
  }
}

int main(int argc, char** argv) {
  std::cout << "Timing sieve of Eratosthenes" << std::endl;
  std::cout << std::endl;

  printTimingHeader();
  timeSieveOfEratosthenesManySizes(1000, 100000000);

  return 0;
}
