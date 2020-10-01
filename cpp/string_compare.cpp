#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

void print_vector(std::vector<std::string> &v){
  for (size_t i = 0; i < v.size(); i++){
    std::cout << "v[" << i << "]: " << v[i] << std::endl;
  }
}

int main(){
  std::string s1 = "bbbb";
  std::string s2 = "abbb";
  std::string s3 = "bbab";

  std::vector<std::string> string_list = {s1, s2, s3};

  print_vector(string_list);
  std::cout << std::endl;

  std::sort(string_list.begin(), string_list.end());

  print_vector(string_list);

  std::cout << "s1 < s2: " << (s1 < s2) << std::endl;
  std::cout << "s2 < s1: " << (s2 < s1) << std::endl;

  std::string s4 = "bbbb";
  std::cout << "s1 == s4: " << (s1 == s4) << std::endl;
}

