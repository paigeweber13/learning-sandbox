#include "bootstrap.hpp"

int bootstrap_init(GLFWwindow** window, string windowTitle)
{
  // Initialise GLFW
  if (!glfwInit())
  {
    fprintf(stderr, "Failed to initialize GLFW\n");
    getchar();
    return -1;
  }

  glfwWindowHint(GLFW_SAMPLES, 4);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
  glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy; should not be needed
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

  // Open a window and create its OpenGL context
  *window = glfwCreateWindow(1024, 768, windowTitle.c_str(), NULL, NULL);
  if (*window == NULL)
  {
    fprintf(stderr, "Failed to open GLFW window. If you have an Intel GPU, they are not 3.3 compatible.\n");
    getchar();
    glfwTerminate();
    return -1;
  }
  glfwMakeContextCurrent(*window);

  // Initialize GLEW
  if (glewInit() != GLEW_OK)
  {
    fprintf(stderr, "Failed to initialize GLEW\n");
    getchar();
    glfwTerminate();
    return -1;
  }

  // Ensure we can capture the escape key being pressed below
  glfwSetInputMode(*window, GLFW_STICKY_KEYS, GL_TRUE);
  return 0;
}

int bootstrap_close()
{
  // Close OpenGL window and terminate GLFW
  glfwTerminate();
  return 0;
}
