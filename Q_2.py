#  Q. Write a program to reverse an array in place? In place means you cannot create a new array. 
#       You have to update the original array.
def reversearray(A, start, end):
  while start < end:
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1
# Driver function to test above function
A = [10, 20, 30, 40, 50]
reversearray(A, 0, 4)
print(A)
