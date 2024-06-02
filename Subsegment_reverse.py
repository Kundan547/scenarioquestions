"""You are given positive integers 
N, 
L, and 
R.
For a sequence 
A=(1,2,…,N) of length 
N, an operation of reversing the 
L-th through 
R-th elements was performed once.
Print the sequence after this operation."""

def reverse_sequence(N,L,R):
  A = list(range(1,N+1))
  
  for i in range((R-L+1)//2):
    temp = A[L-1+i]
    A[L-1+i] = A[R-1+i]
    A[R-1+i] = temp
  
  return A
  

N = int(input())
L = int(input())
R = int(input())

result =  reverse_sequence(N,L,R)
print(result)