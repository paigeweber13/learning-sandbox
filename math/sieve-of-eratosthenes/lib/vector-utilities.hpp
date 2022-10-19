#include <iostream>
#include <vector>

template<class T>
void printVector(std::vector<T> vec){
  for (auto x : vec) {
    std::cout << x << " ";
  }
  std::cout << std::endl;
}
