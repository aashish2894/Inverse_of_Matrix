import random
import numpy as np

def mat(n,m,L,U,p):
	M = np.zeros((n,m))
	for i in range(n):
		for j in range(m):
			temp = random.uniform(0,1)
			if(temp<p):
				mul = 1
			else:
				mul = 0
			temp2 = random.uniform(L,U)
			M[i][j] = mul*temp2

	return M


def wrong(M,n,m):
	count = 0
	for i in range(n):
		count = 0
		for j in range(m):
			if(M[i][j]==0):
				count = count + 1;
				if(count==m):
					return 1

	for j in range(m):
		count = 0
		for i in range(n):
			if(M[i][j]==0):
				count = count + 1;
				if(count==n):
					return 1

	return 0



def Gauss_Jordan_Inv(M,n):
	# create Identity Matrix
	I = np.zeros((n,n))
	for i in range(n):
		I[i][i] = 1

	## Make diagonal elements as non zero
	for i in range(n):
		if(M[i][i]==0):
			for j in range(n):
				if(M[j][i]!=0):
					M[i,] = M[i,] + M[j,]
					I[i,] = I[i,] + I[j,]
					break;


	## perform Gauss Jordan elimination
	for i in range(n):
		for j in range(n):
			if(j!=i):
				I[j,] = I[j,] - M[j][i]*I[i,]/M[i][i]
				M[j,] = M[j,] - M[j][i]*M[i,]/M[i][i]
				

	## Normalize the M[i][i] values of Matrix M
	for i in range(n):
		I[i,] = I[i,]/M[i][i]
		M[i,] = M[i,]/M[i][i]
		
	## I is now the inverted matrix of M

	return I









## Construct B matrix
n = 10
m = 10
L = -10
U = 30
p = 0.6
B = mat(n,m,L,U,p)

while(wrong(B,n,m)):
	B = mat(n,m,L,U,p)

print("Matrix B is\n")
print(B)

## Construct b matrix

n_b = 10
m_b = 1
L_b = 0
U_b = 50
p_b = 0.8
b = mat(n_b,m_b,L_b,U_b,p_b)

print("\nMatrix b is\n")
print(b)


## Compute inverse of Matrix B

B_inv = Gauss_Jordan_Inv(B,n)
print("\nInverse of Matrix B\n")
print(B_inv)

## Compute x

x = np.dot(B_inv,b)
print("\nX vector solution\n")
print(x)

