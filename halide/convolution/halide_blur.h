#pragma once

// third-party:
#include <iostream>
#include <vector>
#include "Halide.h"
#include "halide_image_io.h"

// mine:
#include "kernel.h"
#include "generate_kernels.h"

void blur(size_t kernel_size, std::string input_image_filename);
