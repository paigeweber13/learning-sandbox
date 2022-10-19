#include <catch2/catch.hpp>

#include "sieve-of-eratosthenes.hpp"

TEST_CASE( "01: correctly finds primes below 100", "[primes]" ) {
  auto primes = findPrimes(100);
  REQUIRE( primes.size() == 25 );
  REQUIRE( primes[0] == 2 );
  REQUIRE( primes[1] == 3 );
  REQUIRE( primes[2] == 5 );
  // eh I got bored enumerating these
  REQUIRE( primes[19] == 71 );
  REQUIRE( primes[24] == 97 );
}
