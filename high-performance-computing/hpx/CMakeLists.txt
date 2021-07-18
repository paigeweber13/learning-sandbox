set(TCMALLOC_LIBRARY /usr/lib/x86_64-linux-gnu/libtcmalloc.so.4.5.3)

cmake_minimum_required(VERSION 3.17)
project(test_hpx_project CXX)
find_package(HPX REQUIRED)
add_executable(test_hpx_program main.cpp)
target_link_libraries(test_hpx_program HPX::hpx HPX::wrap_main 
  HPX::iostreams_component)
