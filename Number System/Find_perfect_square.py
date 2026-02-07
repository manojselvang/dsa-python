#Question:

#Given an Integer A. You have to tell if it is a perfect number or not.
#Perfect number is a positive inter which is equal to the sum of its proper positive divisors.

def if_perfect_square(A):

  total = 1                #initialising with 1 as all numbers are divisible by 1

  for num in range(2,A):   
    if A%num == 0:         # if num is a divisor we are adding to the total
      total += num

  if total == 1:            # if prime return zero
    return 0
  elif total == A:          # if equal its perfect square
    return 1
  else:                     # else its not perfect square
    return 0
  
