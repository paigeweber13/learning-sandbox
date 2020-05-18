using Images

function lerp(v0, v1, t)
  v0 + t * (v1 - v0)
end

function make_color_scale(
    color1::Tuple{Int, Int, Int}, 
    color2::Tuple{Int, Int, Int}, 
    steps::Int,
    step_size::Int,
    height::Int)

  img = Array{RGB}(undef, height, step_size * steps)
  println("generated empty image of size ", size(img))

  for i = 1:steps
    println("step ", i)
    println("calculating color...")
    this_color = RGB(
      lerp(color1[1], color2[1], 1.0/convert(AbstractFloat, step_size)),
      lerp(color1[2], color2[2], 1.0/convert(AbstractFloat, step_size)),
      lerp(color1[3], color2[3], 1.0/convert(AbstractFloat, step_size))
    )

    println("assigning color to section of image")
    # this line causes problems. Perhaps I don't understand array indexing in
    # julia
    img[1:height][(i-1)*step_size+1:i*step_size] .= this_color

    println()
  end
end

