def bubblesort( A ):
  for i in range( len( A ) ):
    for k in range( len( A ) - 1, i, -1 ):
      if ( A[k] < A[k - 1] ):
        swap( A, k, k - 1 )
  return A

def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

print (bubblesort([3,7,2,7,1]))
