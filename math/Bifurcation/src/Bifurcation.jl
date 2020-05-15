module Bifurcation

using ArgParse

include("BifurcationLib.jl")

function main(args)

  s = ArgParseSettings("A demonstration of bifurcation and the resulting " *
    "chaos in the equilibrium points of the logistic map. This program " *
    "plots the equilibrium point of repeated evaluations of the logistic " *
    "map for various r.")

  @add_arg_table! s begin
    "x"
      arg_type = Float64
      default = 0.5
      help = "value to be used for first iteration of the logistic map"

    "r0"
      arg_type = Float64
      default = 0.0
      help = "initial r: the starting point for the plot"

    "n"
      arg_type = Int
      default = 100
      range_tester = (n->n>0)
      help = "number of iterations to execute logistic map before result is " *
        "considered to be at equilibrium"

    "m"
      arg_type = Int
      default = 100
      range_tester = (m->m>0)
      help = "number of iterations after equilibrium to plot"

    "r_inc"
      arg_type = Float64
      default = 0.01
      help = "amount to increment r by between tests"

    "r_final"
      arg_type = Float64
      default = 4.0
      help = "point at which we will stop testing and plotting"

  end

  parsed_args = parse_args(args, s)

  BifurcationLib.generate_and_plot(
    parsed_args["x"],
    parsed_args["r0"],
    parsed_args["n"],
    parsed_args["m"],
    parsed_args["r_inc"],
    parsed_args["r_final"],
  )
end

main(ARGS)

end # module
