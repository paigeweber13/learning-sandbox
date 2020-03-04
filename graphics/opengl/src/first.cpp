#include <bootstrap.hpp>

int main()
{
   GLFWwindow *window;
   bootstrap_init(&window);

   glClearColor(0.0f, 0.0f, 0.4f, 0.0f);
   // glClearColor(0.0, 0.0, 0.0, 0.0);
   // glClear(GL_COLOR_BUFFER_BIT);
   // glColor3f(1.0, 1.0, 1.0);
   // glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0);
   // glBegin(GL_POLYGON);
   // glVertex3f(0.25, 0.25, 0.0);
   // glVertex3f(0.75, 0.25, 0.0);
   // glVertex3f(0.75, 0.75, 0.0);
   // glVertex3f(0.25, 0.75, 0.0);
   // glEnd();
   // glFlush();

   do
   {
      // Clear the screen. It's not mentioned before Tutorial 02, but it can cause flickering, so it's there nonetheless.
      glClear(GL_COLOR_BUFFER_BIT);

      // Draw nothing, see you in tutorial 2 !

      // Swap buffers
      glfwSwapBuffers(window);
      glfwPollEvents();

   } // Check if the ESC key was pressed or the window was closed
   while (glfwGetKey(window, GLFW_KEY_ESCAPE) != GLFW_PRESS &&
          glfwWindowShouldClose(window) == 0);

   bootstrap_close();
}