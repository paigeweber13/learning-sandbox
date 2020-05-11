# a demonstration of bifurcation using the logistic map

# equation: x_n+1 = r x_n (1-x_n)

# how does equilibrium change as the parameter r changes?

using Test
# using ArgParse

### utility functions:

# rounds x to an aribtrary number of decimal places
function decimal_round(x::AbstractFloat, num_decimal_places::Unsigned)::AbstractFloat
  rounding_factor = 10^num_decimal_places
  round(rounding_factor * x)/rounding_factor
end

### Population growth stuff

# gives logistic map of a value x and parameter (growth rate) r
logistic_map(x, r) = r*x*(1-x)

# gives many results of logistic map, starting with nth iteration and returning
# the results of m iterations after the nth
function logistic_map_series(x, r, n, m)
  nth_x = x
  for i = 1:n
    nth_x = logistic_map(nth_x, r)
  end

  mth_x = nth_x
  series = []
  for i = (n+1):m
    mth_x = logistic_map(mth_x, r)
    series.append(mth_x)
  end
  series
end

### Tests

function test_decimal_round()
  @test decimal_round(0.001422, convert(Unsigned, 3)) == 0.001
  @test decimal_round(0.000037, convert(Unsigned, 5)) == 0.00004
  @test decimal_round(0.895, convert(Unsigned, 0)) == 1.0
  println("all decimal_round tests passed!")
end

function test_population_growth()
  @test logistic_map(.4, 2.6) == 0.624
  @test logistic_map(.3, 1.0) == 0.21
  @test decimal_round(logistic_map(.2, 1.1), convert(Unsigned, 3)) == 0.176
  @test decimal_round(logistic_map(.374, .7), convert(Unsigned, 4)) == 0.1639
  println("all population_growth tests passed!")
end

function test_population_growth_long_term()
  # TODO: implement
end

function run_tests()
  test_decimal_round();
  test_population_growth();
end

run_tests()
