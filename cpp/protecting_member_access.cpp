#include <iostream>

class A {
  public:
    A(int first, int second) : test_const(442) {
      this->first_value = first;
      this->second_value = second;
      this->first = &(this->first_value);
    }

    const int * first;
    const int * second;
    const int test_const;

  private:
    int first_value;
    int second_value;
};

class B {
  public:
    B(int first, int second) {
      this->first = first;
      this->second = second;
    }

    int first;
    int second;
};

int main() {
  A a(1, 2);
  // this way you can still access with the dot syntax... but since everything
  // is a pointer you have to dereference it which could quickly get messy
  std::cout << "a.first: " << *(a.first) << std::endl;
  std::cout << "the const: " << a.test_const << std::endl;

  const B b(3, 4);
  // errors with "Cannot assign to variable 'b' with const-qualified type 'const
  // B'
  //b.first = 5;
  std::cout << "b.first: " << b.first << std::endl;
}
