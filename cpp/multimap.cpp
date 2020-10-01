#include <iostream>
#include <map>
#include <string>

template<class M>
void print(const M& mmap)
{
    for (auto & e : mmap)
        std::cout << "{" << e.first << "," << e.second << "} ";
    std::cout << '\n';
}

// template<class M>
// void print_unique_keys(const M& mmap)
// {
//   for( typename M::iterator it = mmap.begin(); it != mmap.end();
//     it = mmap.upper_bound(it->first))
//   {
//     std::cout << "{" << it->first << "," << it->second << "} ";
//   }
//   std::cout << '\n';
// }

void print_unique_keys(const std::multimap<std::string, int>& mmap)
{
  for( auto it = mmap.begin(); it != mmap.end();
    it = mmap.upper_bound(it->first))
  {
    std::cout << "{" << it->first << "," << it->second << "} ";
  }
  std::cout << '\n';
}

int main() {
  std::multimap<std::string, int> mm;
  mm.insert({"test", 2});
  mm.insert({"test", 9});
  mm.insert({"test", 1});
  mm.insert({"test", 20});
  mm.insert({"test", 49});
  
  print(mm);
  print_unique_keys(mm);
}
