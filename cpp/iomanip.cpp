#include <iostream>
#include <iomanip>
#include <sstream>

int main(){
    std::cout << "Right fill:\n" << std::setprecision(3) << std::fixed << std::right
              << std::setw(12) << -1.23  << '\n'
              << std::setw(12) << 42 << '\n'
              << std::setw(12) << 4232.33333333333 << '\n';

    std::stringstream ss;
    ss << "Right fill:\n" << std::setprecision(3) << std::fixed << std::right
       << std::setw(12) << -1.23  << '\n'
       << std::setw(12) << 42 << '\n'
       << std::setw(12) << 4232.33333333333 << '\n';

    std::cout << ss.str();
}

