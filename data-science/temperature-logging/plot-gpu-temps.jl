using CSV
using Plots

function plot_gpu_temps(filename)
  data = CSV.File(filename, comment="#", delim=" ", ignorerepeated=true)

  x = size(data)[1]
  y = hcat(data.gtemp, data.pwr)

  p = plot(x, y,
    title = "GPU temperatures and power consumptions during idle and stress test",
    xlabel = "Seconds after start",
    ylabel = "Temp (C) and Power (W)",
    size = (1200, 800),
    label = ["Temperature", "Power"],
    )

  show(p)
  #display(p)
end

