CXX=g++
# CXXFLAGS=-g -Wall -std=c++17 -I$(INC_DIR)
# LDFLAGS=-L$(LIB_DIR) $(LIBS) -march=native -mtune=native -fopenmp
CXXFLAGS=-g -Wall -std=c++17 $(INC_DIRS)
LDFLAGS=$(LIBS) -march=native -mtune=native -fopenmp
CXXASSEMBLYFLAGS=-S -g -fverbose-asm

# PREFIX=/usr/local
# LIB_DIR=$(PREFIX)/lib
INC_DIRS=-I$(shell pwd)/lib
LIBS=-lGL -lglfw -lGLEW

MAIN_DIR=src
SRC_DIR=lib
OBJ_DIR=obj
ASM_DIR=asm
EXEC_DIR=bin

SOURCES=$(wildcard lib/*.cpp)
HEADERS=$(wildcard lib/*.h)
OBJS=$(SOURCES:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)
ASM=$(SOURCES:$(SRC_DIR)/%.cpp=$(ASM_DIR)/%.s)
EXEC_NAME=gl
EXEC=$(EXEC_DIR)/$(EXEC_NAME)

build: $(EXEC)

test: $(EXEC)
	./$(EXEC)

init:
	@mkdir -p $(EXEC_DIR);
	@mkdir -p $(OBJ_DIR);
	# @mkdir -p $(EXEC_DIR)/tests;

debug:
	@echo "sources:  $(SOURCES)";
	@echo "objects:  $(OBJS)";
	@echo "exec:     $(EXEC)";
	@echo "INC_DIRS: $(INC_DIRS)";
# debug: LDFLAGS += -Q --help=target
# debug: clean build

$(EXEC): $(OBJS) $(MAIN_DIR)/first.cpp
	$(CXX) $(OBJS) $(INC_DIRS) $(MAIN_DIR)/first.cpp $(LDFLAGS) -o $@

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp init
	$(CXX) $(CXXFLAGS) -c $< -o $@

assembly: $(ASM)

$(ASM_DIR)/%.s: $(SRC_DIR)/%.cpp
	@mkdir -p $(ASM_DIR);
	$(CXX) $(CXXFLAGS) $(CXXASSEMBLYFLAGS) $< -o $@

clean:
	rm -f $(OBJS) $(EXEC)
