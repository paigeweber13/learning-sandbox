#include <iostream>
#include <cstdlib>

void check_envvar(const char * envvar){
  if(const char* env_p = std::getenv(envvar))
    std::cout << "Your " << envvar << " is: " << env_p << '\n';
  else
    std::cout << envvar << " is unset" << std::endl;
}
 
int main()
{
  check_envvar("PATH");
  check_envvar("FHV_OUTPUT");
}

