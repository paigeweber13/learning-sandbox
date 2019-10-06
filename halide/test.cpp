// based on this tutorial: 
// https://halide-lang.org/tutorials/tutorial_lesson_02_input_image.html

// The only Halide header file you need is Halide.h. It includes all of Halide.
#include "Halide.h"

// Include some support code for loading pngs.
#include "halide_image_io.h"
using namespace Halide::Tools;

int main(int argc, char **argv) {
  // load an image
  Halide::Buffer<uint8_t> input = load_image("saturn-v-2048x2048-bw.jpg");

  // declare variables and function
  Halide::Var x, y, c;
  Halide::Func brighter;

  // define a function in memory
  brighter(x, y) = Halide::cast<uint8_t>(min(input(x, y) * 1.5f, 255));

  // run that function
  Halide::Buffer<uint8_t> output =
    brighter.realize(input.width(), input.height());

  // Save the output for inspection. It should look like a bright rocket.
  save_image(output, "out/brighter.png");

  printf("Success!\n");
  return 0;
}
