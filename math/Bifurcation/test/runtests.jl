using Test
using Bifurcation

### Tests

function test_decimal_round()
  @test Bifurcation.decimal_round(0.001422, convert(Unsigned, 3)) == 0.001
  @test Bifurcation.decimal_round(0.000037, convert(Unsigned, 5)) == 0.00004
  @test Bifurcation.decimal_round(0.895, convert(Unsigned, 0)) == 1.0
  println("all decimal_round tests passed!")
end

function test_logistic_map()
  @test Bifurcation.logistic_map(.4, 2.6) == 0.624
  @test Bifurcation.logistic_map(.3, 1.0) == 0.21
  @test Bifurcation.decimal_round(
    Bifurcation.logistic_map(.2, 1.1),
    convert(Unsigned, 3)
    ) == 0.176
  @test Bifurcation.decimal_round(
    Bifurcation.logistic_map(.374, .7),
    convert(Unsigned, 4)
    ) == 0.1639
  println("all logistic_map tests passed!")
end

function test_logistic_map_series()
  s = Bifurcation.logistic_map_series(1, 2, 100, 100)
  @test size(s, 1) == 100

  # fancy broadcast syntax
  @test Bifurcation.decimal_round.(
    Bifurcation.logistic_map_series(0.77, 1.33, 100, 10), 
    convert(Unsigned, 3)
   ) == fill(0.248, (10))
  println("all logistic_map_series tests passed!")
end

function run_tests()
  test_decimal_round();
  test_logistic_map();
  test_logistic_map_series();
end

run_tests()
