#include <bootstrap.hpp>

int main()
{
   GLFWwindow *window;
   bootstrap_init(&window, "Triangle");

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

   GLuint VertexArrayID;
   glGenVertexArrays(1, &VertexArrayID);
   glBindVertexArray(VertexArrayID);

   static const GLfloat g_vertex_buffer_data[] = {
      -1.0f, -1.0f, 0.0f,
      1.0f, -1.0f, 0.0f,
      0.0f, 1.0f, 0.0f, 
   };
   
   GLuint vertexBuffer;
   glGenBuffers(1, &vertexBuffer);
   glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer);
   glBufferData(GL_ARRAY_BUFFER, sizeof(g_vertex_buffer_data), 
      g_vertex_buffer_data, GL_STATIC_DRAW);

   do
   {
      glClear(GL_COLOR_BUFFER_BIT);

      glEnableVertexAttribArray(0);
      glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer);
      glVertexAttribPointer(
         0, // ??? Magic
         3, // size
         GL_FLOAT, // type
         GL_FALSE, // ???
         0, // stride
         (void*) 0 // ? offset maybe?
      );

      glDrawArrays(GL_TRIANGLES, 0, 3);

      glDisableVertexAttribArray(0);

      // Swap buffers
      glfwSwapBuffers(window);
      glfwPollEvents();

   } // Check if the ESC key was pressed or the window was closed
   while (glfwGetKey(window, GLFW_KEY_ESCAPE) != GLFW_PRESS &&
          glfwWindowShouldClose(window) == 0);

   bootstrap_close();
}