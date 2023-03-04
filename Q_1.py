# Write a program to find all pairs of an integer array whose sum is equal to a given number?

def sum_from_array():
    array = [1,2,4,5,7,8,3,6]
    sum = int(input("Enter the sum  : "))
    for i in array:
        for j in array:
            if i + j == sum:
                print(f"({i},{j})",end=" ")
            

sum_from_array()