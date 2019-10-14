#include <iostream>
#include <string>

#include "Halide.h"
#include "halide_image_io.h"

using namespace Halide::Tools;
using namespace std;

Halide::Func halide_box_blur(Halide::Func in) {
  // variables
  Halide::Func blur_x, blur_y;
  Halide::Var x, y, xi, yi;

  // The algorithm
  blur_x(x, y) = (in(x - 1, y) + in(x, y) + in(x + 1, y)) / 3;
  blur_y(x, y) = (blur_x(x, y - 1) + blur_x(x, y) + blur_x(x, y + 1)) / 3;

  // The schedule
  blur_y.tile(x, y, xi, yi, 256, 32).vectorize(xi, 8).parallel(y);
  blur_x.compute_at(blur_y, x).vectorize(x, 8);
  return blur_y;
}

int main(int argc, char** argv){
  if (argc < 2) {
    cout << "usage: " << argv[0] << " path/to/image-to-blur" << endl;
    return 1;
  }

  Halide::Func blur = halide_box_blur(load_image(argv[1]));
  Halide::Buffer<uint8_t> output = blur.realize();
  string output_filename = argv[1];  
  std::size_t found = output_filename.find_last_of(".");
  string ext = output_filename.substr(found, output_filename.size());
  output_filename = output_filename.substr(0, found) + "-output" + ext;
  save_image(output, output_filename);
  return 0;
}