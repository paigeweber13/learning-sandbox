using Plots

# example code taken from
# https://docs.juliaplots.org/latest/tutorial/#Changing-the-Plotting-Series-1

x = 1:10
y = rand(10)

gr() # We will continue onward using the GR backend
p = plot(x, y, seriestype = :scatter, title = "My Scatter Plot")
savefig(p, "tutorial_plot.png")

# animated plot. Code taken from:
# 

p = plot([sin, cos], zeros(0), leg = false)
anim = Animation()
for x = range(0, stop = 10π, length = 100)
    push!(p, x, Float64[sin(x), cos(x)])
    frame(anim)
end
gif(anim, "anim_sine.gif", fps=15)
