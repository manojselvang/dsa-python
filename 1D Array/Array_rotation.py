# Question:
# Given an integer array A of size N and an integer B, you have to return the same array after rotating it B timetowards the right.

# Example:
# A = [1,2,3,4]
# B = 1
# Output = [3,4,1,2]

Code:
def array_rotate(A,B):
  N = len(A)              # finding length of A
  B = B%N                 # if B is larger than N then finding the remainder to rotate A

  A[:] = A[-B:] + A[:-B]  # rotation
  return A
