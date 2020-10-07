using CSV
using DataFrames
using Plots

function visualize()
  data = DataFrame(
    CSV.File("pulitzer-circulation-data.csv", normalizenames = true))

  sort!(data, :Pulitzer_Prize_Winners_and_Finalists_1990_2014, rev = true)
  println(data)
  sort!(data, :Pulitzer_Prize_Winners_and_Finalists_1990_2014)

  x = data.Newspaper
  y = data.Pulitzer_Prize_Winners_and_Finalists_1990_2014
  # y = getproperty(data, 
  #   Symbol("Pulitzer Prize Winners and Finalists, 1990-2014"))

  p = plot(x, y, seriestype = :bar, direction = :h, size = (1000, 2000),
    legend = false)
  savefig(p, "plot.png")
end

visualize()

