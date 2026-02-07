# Question:
# Given an integer arry A of size N. In one second, you can increase the value of one element by 1.
# Find minimum time in seconds to make all elements of the array equal.
# Example:
# A = [2,4,1,3,2]
# Output = 8

# Code:
def time_to_eqality(A):
  count = 0
  maximum = max(A)

  for i in range(len(A)):
    if A[i] != maximum:
      count += (maximum - A[i])

  return count
