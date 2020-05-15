module BifurcationLib

# a demonstration of bifurcation using the logistic map

# equation: x_n+1 = r x_n (1-x_n)

# how does equilibrium change as the parameter r changes?

using Plots
# using ArgParse

### utility functions:

# rounds x to an aribtrary number of decimal places
function decimal_round(x::AbstractFloat, num_decimal_places::Unsigned)::AbstractFloat
  rounding_factor = 10^num_decimal_places
  round(rounding_factor * x)/rounding_factor
end

### Logistic map stuff

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
  for i = 1:m
    mth_x = logistic_map(mth_x, r)
    append!(series, [mth_x])
  end
  series
end

### Plotting things

# r0: first r to use

# r_inc: amount to increment r by each time 

# r_final: final r (if r_final-r0 is not divisibible by r_inc then the actual
# final r will be slightly less than r_final)

function generate_points(x0, r0, n, m, r_inc, r_final)
  x = []
  y = []

  for r = r0:r_inc:r_final
    this_x = fill(r, (m))
    this_y = logistic_map_series(x0, r, n, m)
    append!(x, this_x)
    append!(y, this_y)
  end

  x, y
end

function plot_points(x, y, n, m)
  # set backend
  gr()

  # create plot
  plot(x, y,
    seriestype = :scatter, 
    title = "Values of recursive iterations of logistic map for various r",
    xlabel = "r",
    ylabel = string("next ", m, " values after first ", n, " iterations"),
    dpi = 1000,
    markersize = 1,
    markeralpha = 0.5,
    # markeralpha = 0.1,
    # markerstrokestyle = :dot,
    # markerstrokecolor = :blue,
    markerstrokewidth = 0,
    markerfillcolor = :blue,
  )
end

function generate_and_plot(x0, r0, n, m, r_inc, r_final)
  println("generating points for plot with the following parameters:")
  println("x0      = ", x0)
  println("r0      = ", r0)
  println("n       = ", n)
  println("m       = ", m)
  println("r_inc   = ", r_inc)
  println("r_final = ", r_final)
  println()

  println("total number of poins to generate: ",
    floor( (r_final-r0) * r_inc ) * (n + m)
  )
  println()

  println("generating...")
  x, y = generate_points(x0, r0, n, m, r_inc, r_final)

  println("points generated. Plotting...")
  p = plot_points(x, y, n, m)
  # display(p)
  filename = string(
      "x0=", x0, ",",
      "r0=", r0, ",",
      "n=", n, ",",
      "m=", m, ",",
      "r_inc=", r_inc, ",",
      "r_final=", r_final, ".png")
  println("saving figure to ", filename)
  savefig(p, filename)
  println("done.")
  # p
end

function example_plot()
  x0 = 0.5
  r0 = 0.0
  n = 100
  m = 100
  r_inc = 0.01
  r_final = 4.0 # seems like anything higher than this diverges quickly to -inf

  generate_and_plot(x0, r0, n, m, r_inc, r_final)
end

end # module
