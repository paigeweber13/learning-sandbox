/* demos io, arrays, functions */

#include <stdio.h>

// ASCII C requires that identifiers have a max length of 8 characters
// later extensions to the c language removed this restriction
#define MAX_LINE_LENGTH 1000

// function declarations
int getline(char line[], int maxline);
void copy(char to[], char from[]);

main(){

}

// function implementations
int getline(char line[], int maxline){
  int c, i; 
   for (i = 0; i < maxline - 1 && ;)
}

void copy(char to[], char from[]){
  int i; // memory allocation
  i = 0; // write to memory

  // this is a clever little loop that sets to[i] equal to from[i] before
  // checking the condition in the loop
  while ((to[i] = from[i]) != '\0')
    ++i;
}
