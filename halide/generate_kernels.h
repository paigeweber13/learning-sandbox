#pragma once

#include <iostream>
#include <math.h>
#include <vector>

#include "kernel.h"

#define _USE_MATH_DEFINES

float bivariate_gaussian(float std_dev, float x, float y);
Kernel generate_blur_kernel(size_t k);
vector<Kernel> generate_blur_kernels(size_t max_k);
