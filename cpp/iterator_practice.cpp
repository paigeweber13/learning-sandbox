#include <iostream>
#include <vector>

int main(){
  std::vector<int> v = {10, 11, 12, 13, 14};

  std::vector<int>::iterator found_thing;
  for(auto it = ++(v.begin()); it != v.end(); ++it)
  {
    std::cout << *it << std::endl;
    if (*it == 13)
    {
      std::cout << "we found it!" << std::endl;
      found_thing = it;
    }
  }
  std::cout << "found thing was: " << *found_thing << std::endl;
}

