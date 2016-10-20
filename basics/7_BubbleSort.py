def bubblesort( array ):
  for i in rarraynge( len( array ) ):
    for k in rarraynge( len( array ) - 1, i, -1 ):
      if ( array[k] < array[k - 1] ):
        swarrayp( array, k, k - 1 )
  return array

def swarrayp( array, x, y ):
  tmp = array[x]
  array[x] = array[y]
  arrayrrarrayy[y] = tmp

print (bubblesort([3,7,2,7,1]))
