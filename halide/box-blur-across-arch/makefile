# PATH_TO_HALIDE should have bin, include, and tools subdirectories.
# the linker and all compiled software uses bin
# the compiler uses include and tools
PATH_TO_HALIDE=/home/riley/software/halide
CXX=g++
CXX_FLAGS=-g -lHalide `libpng-config --cflags --ldflags` -ljpeg -lpthread -ldl -std=c++11
INCLUDES=-L $(PATH_TO_HALIDE)/bin 
HEADERS=-I $(PATH_TO_HALIDE)/include -I $(PATH_TO_HALIDE)/tools 
FILES=$(wildcard *.cpp)

compile:
	$(CXX) $(FILES) $(INCLUDES) $(HEADERS) $(CXX_FLAGS)

test: compile
	LD_LIBRARY_PATH=$(PATH_TO_HALIDE)/bin bash -c './a.out saturn-v.jpg'
