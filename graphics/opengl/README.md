# Prerequisites
 - **up-to-date grpahics drivers with opengl support** Instructions on how to
   install these are not supplied and are outside the scope of this readme
 - **GLEW** `sudo apt install libglew-dev`
 - **GLFW** `sudo apt install libglfw3-dev`
 - **GLM** `sudo apt install libglm-dev`

# Compiling and Linking
 - compile with `g++ -c first.cpp`
 - link with `g++ first.o -lGL -lglfw -lGLEW -o first`
