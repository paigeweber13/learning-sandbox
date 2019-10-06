#include "kernel.h"

Kernel::Kernel(){
  Kernel(3);
}

Kernel::Kernel(size_t k){
  if (k % 2 == 0){
    throw "Unusable k. K must be odd.";
  } else if (k < 3){
    throw "Unusable k. K must be at least 3.";
  }

  for (size_t i = 0; i < k; i++){
    this->values.push_back(vector<float>(k));
  }

  this->k = k;
  this->midpoint = size_t(ceil(k/2));
  this->half = midpoint - 1;
}

Kernel::~Kernel(){
}

float Kernel::get(int x, int y){
  return values[midpoint+x][midpoint+y];
}

float Kernel::set(int x, int y, float value){
  values[midpoint+x][midpoint+y] = value;
}

string Kernel::to_string(){
  // todo: does setprecision do anything?
  // setprecision(4);
  stringstream ss;
  ss << "k: " << this->k << endl;
  ss << "Midpoint: " << this->midpoint << endl;
  ss << "Half: " << this->half << endl;
  ss << "Kernel:" << endl;
  for(int x = -half; x <= half; x++){
    for(int y = half; y >= -half; y--){
      ss << get(x, y) << "  ";
    }
    ss << endl;
  }
  ss << endl;
  return ss.str();
}
