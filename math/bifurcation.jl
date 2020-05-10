# a demonstration of bifurcation using equilibrium of a simple population
# growth function

# population equation: x_n+1 = r x_n (1-x_n)

# how does equilibrium population change as growth rate (r) changes?

# This creates a bifurcation diagram

using Test
# using ArgParse

### utility functions:

function decimal_round(x::AbstractFloat, num_decimal_places::Unsigned)::AbstractFloat
  rounding_factor = 10^num_decimal_places
  round(rounding_factor * x)/rounding_factor
end

### Population growth stuff

population_growth(x, r) = r*x*(1-x)

### Tests

function test_decimal_round()
  @test decimal_round(0.001422, convert(Unsigned, 3)) == 0.001
  @test decimal_round(0.000037, convert(Unsigned, 5)) == 0.00004
  @test decimal_round(0.895, convert(Unsigned, 0)) == 1.0
  println("all decimal_round tests passed!")
end

function test_population_growth()
  @test population_growth(.4, 2.6) == 0.624
  @test decimal_round(population_growth(.2, 1.1), convert(Unsigned, 3)) == 0.176
  println("all population_growth tests passed!")
end

run_tests() = (
  test_decimal_round();
  test_population_growth();
)

run_tests()
