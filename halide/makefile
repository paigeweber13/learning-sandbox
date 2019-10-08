# PATH_TO_HALIDE should have bin, include, and tools subdirectories.
# the linker and all compiled software uses bin
# the compiler uses include and tools
PATH_TO_HALIDE=/home/riley/software/halide
CXX=g++
COMMON_FLAGS=
CXX_FLAGS=-c -g -lHalide `libpng-config --cflags --ldflags` -ljpeg -lpthread -ldl -std=c++11
LD_FLAGS=
INCLUDES=-L $(PATH_TO_HALIDE)/bin 
HEADERS=-I $(PATH_TO_HALIDE)/include -I $(PATH_TO_HALIDE)/tools 
# SOURCES=generate_kernels.cpp kernel.cpp halide_blur.cpp
SOURCES=kernel.cpp generate_kernels.cpp halide_blur.cpp test.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=a.out

# if you want to run g++ on the command line (for testing or whatever), use
# this command: 
# g++ test.cpp generate_kernels.cpp halide_blur.cpp kernel.cpp -I /home/riley/software/halide/include -I /home/riley/software/halide/tools -L /home/riley/software/halide/bin -g -lHalide `libpng-config --cflags --ldflags` -ljpeg -lpthread -ldl -std=c++11

# compile-test: SOURCES += test.cpp
# compile-speedtest: SOURCES += speedtest.cpp

compile-test compile-speedtest: $(EXECUTABLE)

speedtest: compile-speedtest
	LD_LIBRARY_PATH=$(PATH_TO_HALIDE)/bin bash -c '$(EXECUTABLE)'

test: compile-test
	LD_LIBRARY_PATH=$(PATH_TO_HALIDE)/bin bash -c '$(EXECUTABLE) blur 3'

clean:
	rm -f $(OBJECTS)

$(EXECUTABLE): $(OBJECTS) 
	# LD_LIBRARY_PATH=$(PATH_TO_HALIDE)/bin bash -c '$(CXX) $(LD_FLAGS) $(OBJECTS) -o $@'
	$(CXX) $(LD_FLAGS) $(PATH_TO_HALIDE)/bin/libHalide.so $(OBJECTS) -o $@

.cpp.o:
	$(CXX) $< $(INCLUDES) $(HEADERS) $(CXX_FLAGS) -o $@
