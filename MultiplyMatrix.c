// C program to multiply two square matrices. 
#include <stdio.h> 
#define N 64
// 64X64 matrixes of int type 4 bytes each 64 bits
#include <stdlib.h> 
#include <time.h>
// This function multiplies mat1[][] and mat2[][], 
// and stores the result in res[][] 
void multiply(int mat1[][N], int mat2[][N], int res[][N]) 
{ 
	int i, j, k; 
	for (i = 0; i < N; i++) 
	{ 
		for (j = 0; j < N; j++) 
		{ 
			res[i][j] = 0; 
			for (k = 0; k < N; k++) 
				res[i][j] += mat1[i][k]*mat2[k][j]; 
		} 
	} 
} 

int main() 
{ 
	int res[N][N]; // To store result 
	int i, j; 
	int mat1[N][N], mat2[N][N];
	// initialize matrix 1
	for (i = 0; i<N; i++){
		for(j=0;j<N;j++){
			mat1[i][j] = rand()%256;
			mat2[i][j] = rand()%256;
		}
	}
	//print matrix 1
/*	for (i = 0; i<N; i++){
		for(j=0;j<N;j++){
			printf("%d ", mat1[i][j]);
		}
		printf("\n");
	}

	//print matrix 2
		for (i = 0; i<N; i++){
		for(j=0;j<N;j++){
			printf("%d ", mat2[i][j] );
		}
		printf("\n");
	}
*/
	multiply(mat1, mat2, res); 
/*	printf("Result matrix is \n"); 
	for (i = 0; i < N; i++) 
	{ 
		for (j = 0; j < N; j++) 
		printf("%d ", res[i][j]); 
		printf("\n"); 
	} 
*/	
	return 0; 
} 
