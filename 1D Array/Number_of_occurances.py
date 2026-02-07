# Question:
# Given an array A and aninteger B, find the number of occurances of B in A.

# Example:
# A = [1,2,2]
# B = 2

# Code:

def number_of_occurances(A,B):
  count = 0
  for i in A:
    if i == B:
      count += 1      #increment everytime an occurance of B is found

  return count
