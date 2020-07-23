#include <iostream>
#include <vector>

class A {
public:
  const std::vector<double>& getVect() const { return doubleVect; }                           

  std::vector<double> doubleVect;
};

class B {
  public:
    int first;
    int second;
    int third;
};

class C {
public:
  const std::vector<B>& getVect() const { return BVect; }                           

  std::vector<B> BVect;
};

int main(){
  A a;

  a.doubleVect.push_back(0.1);
  a.doubleVect.push_back(0.2);
  a.doubleVect.push_back(0.3);

  // fails with "error: assignment of read-only location"
  //a.getVect()[0] = 0.7;
  
  a.getVect().at(0);
  std::cout << "first entry of double vector: " << a.getVect()[0] << std::endl;

  for(const auto &num : a.getVect()){
    std::cout << "entry in a.doubleVect: " << num << std::endl;
  }

  // how do objects within the returned const vector behave?
  B b1;
  B b2;
  B b3;

  b1.first = 10;
  b1.second = 20;
  b1.third = 30;

  b2.first = 100;
  b2.second = 200;
  b2.third = 300;

  b3.first = 1000;
  b3.second = 2000;
  b3.third = 3000;

  C c;

  c.BVect.push_back(b1);
  c.BVect.push_back(b2);

  // fails with "error: assignment of member `B::first` in read-only object"
  // c.getVect()[0].first = 12;
  
  c.getVect().at(0);
  std::cout << "c[0].first: " << c.getVect()[0].first << std::endl;

  for(const auto &thing : c.getVect()){
    std::cout << "entry in c: " << std::endl;
    std::cout << "  entry.first: " << thing.first << std::endl;
    std::cout << "  entry.second: " << thing.second << std::endl;
    std::cout << "  entry.third: " << thing.third << std::endl;
  }

  return 0;
}

