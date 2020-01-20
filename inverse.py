# expected : square matrix, column vector of same length 

def prettyprint(Z):
	for i in range(len(Z)):
		for j in range(len(Z[i])):
			print("%10.2f" % (Z[i][j]), end = '\t')
		print()

def solve(A, B):
	nRows = len(A)
	nCols = len(A[0])
	if nRows != nCols or nRows != len(B) :
		return(-1)
	n = nRows

	# prepare augmented matrix 
	Z =[]
	for i in range(n):
		Z.append([]) 
		Z[i] += ( [A[i][j] for j in range(n)] ) 
		Z[i] += ( [ 0 for j in range(n)] ) 
		Z[i][i+n]  = 1
		Z[i] +=  [ B[i] ] 

	prettyprint(Z)
	for i in range(n):
		if ( Z[i][i] == 0 ):
			invertible = False
			for k in range (n):
				if (Z[k][i] != 0):
					invertible = True
					for j in range(2*n+1):
						temp = Z[i][j]
						Z[i][j] = Z[k][j]
						Z[k][j] = temp
					break
			if ( invertible == False ) :
				return -2	

		if ( Z[i][i] != 0 ):
			 # set pivot element / row to unity
			f = Z[i][i]
			for j in range(2*n+1):	
				Z[i][j] /= f
			for k in range(n):
				if ( k == i ):
					continue
				factor = Z[k][i]/1.0;
				for j in range( 2*n+1):
					Z[k][j] = Z[k][j] - factor*Z[i][j]

	prettyprint(Z)
	soln = [ Z[i][2*n] for i in range(n) ] 
	return soln 

A = [ [ 2,  1, 1 ], [ 3, 2 ,0 ], [ 4 , 7 , 1 ]]
B = [ 7, 7 ,7 ]

print ( solve(A, B) )
