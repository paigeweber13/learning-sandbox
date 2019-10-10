#include "halide_blur.h"

using namespace Halide::Tools;

void blur(size_t kernel_size, std::string input_image_filename){
  std::vector<Kernel> kernels = generate_blur_kernels(9);

  for (size_t i = 3; i <= 9; i += 2){
    std::cout << kernels[i].to_string();
  }

  Halide::Buffer<uint8_t> input = load_image(input_image_filename);

  Halide::Var x, y, k;
  Halide::Func blur;

  auto convolution_matrix = generate_blur_kernel(kernel_size);

  // Func will equal value and value gets applied to every pixel (of location
  // (x,y)) in the image.
  Halide::Expr value = Halide::cast<float>(input(x, y));
  // numbering below is confusing because matrix is accessed with [row][column]
  // and x and y are like a cartesian plane
  // for(int i = 0; i <= k; i++)
  // value = input(x-1, y-1) * convolution_matrix[0][0]
  //       + input(x  , y-1) * convolution_matrix[0][0]
  //       + input(x+1, y-1) * convolution_matrix[0][0]
  //       + input(x-1, y  ) * convolution_matrix[0][0]
  //       + input(x  , y  ) * convolution_matrix[0][0]
  //       + input(x+1, y  ) * convolution_matrix[0][0]
  //       + input(x-1, y+1) * convolution_matrix[0][0]
  //       + input(x  , y+1) * convolution_matrix[0][0]
  //       + input(x+1, y+1) * convolution_matrix[0][0]

  blur(x, y) = value;

  Halide::Buffer<uint8_t> output =
    blur.realize(input.width(), output.width());
}