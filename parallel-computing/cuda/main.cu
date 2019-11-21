#include <cstdio>

#define ARR_SIZE 10

void __global__ sum_array(int* d_arr, int* res){
  printf("inside sum_array\n");
  for(int i = 0; i < ARR_SIZE; i++){
    res += d_arr[i];
  }
}

int main(){
  int arr[ARR_SIZE] = {1, 0, 3, 5, 0, 0, 0, 6, 7, 10};
  int expected_sum = 32;
  int actual_sum = 0;

  int *d_sum, *d_arr;

  cudaMalloc(&d_sum, sizeof(int));
  cudaMalloc(&d_arr, sizeof(int)*ARR_SIZE);
  cudaMemcpy(d_sum, &actual_sum, sizeof(int), cudaMemcpyDefault);
  cudaMemcpy(d_arr, &arr, sizeof(int)*ARR_SIZE, cudaMemcpyDefault);
  sum_array<<<1, 1>>>(d_arr, d_sum);
  cudaDeviceSynchronize();
  cudaMemcpy(&actual_sum, d_sum, sizeof(int), cudaMemcpyDefault);

  printf("actual_sum: %i\n", actual_sum);
  printf("expected_sum: %i\n", expected_sum);
}

