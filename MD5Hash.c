#include <stdio.h> 
 
unsigned char xyz[200] = { 
    0x41, 0x41, 0x41, 
    0x41, 0x41, 0x41, 
    0x41, 0x41, 0x41,
}; 
 
int main() 
{ 
  int i; 
  for (i=0; i<200; i++){ 
    printf("%x", xyz[i]); 
  } 
  printf("\n"); 
}