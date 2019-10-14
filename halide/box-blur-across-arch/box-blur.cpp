#include "Halide.h"
#include "halide_image_io.h"
#include <iostream>
#include <string>

using namespace Halide;
using namespace Halide::Tools;
using namespace std;

void blur_image(string input_filename, string output_filename){
  // taken from halide tutorial 7, available at
  // https://github.com/halide/Halide/blob/master/tutorial/lesson_07_multi_stage_pipelines.cpp
  Var x("x"), y("y"), c("c");

  {
    Buffer<uint8_t> input = load_image(input_filename);

    Func input_16("input_16");
    input_16(x, y, c) = cast<uint16_t>(input(x, y, c));

    Func blur_x("blur_x");
    blur_x(x, y, c) = (input_16(x-1, y, c) +
                       2 * input_16(x, y, c) +
                       input_16(x+1, y, c)) / 4;

    Func blur_y("blur_y");
    blur_y(x, y, c) = (blur_x(x, y-1, c) +
                       2 * blur_x(x, y, c) +
                       blur_x(x, y+1, c)) / 4;

    Func output("output");
    output(x, y, c) = cast<uint8_t>(blur_y(x, y, c));

    Buffer<uint8_t> result(input.width()-2, input.height()-2, 3);
    result.set_min(1, 1);
    output.realize(result);

    save_image(result, output_filename);
  }
}

int main(int argc, char **argv) {
  if (argc < 2) {
    cout << "usage: " << argv[0] << " path/to/image-to-blur" << endl;
    return 1;
  }

  string input_filename = argv[1];  
  std::size_t dot_i = input_filename.find_last_of(".");
  string ext = input_filename.substr(dot_i, input_filename.size());
  string output_filename = input_filename.substr(0, dot_i) + "-output" + ext;

  blur_image(input_filename, output_filename);
  cout << "blurred image " << input_filename << " and output to "
       << output_filename << endl;

  return 0;
}
