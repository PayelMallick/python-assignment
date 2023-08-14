def are_arrays_equal(a, b):
    # If the arrays have different sizes, they cannot be equal
    if len(a) != len(b):
        return False
    
    count_A = {}
    count_B = {}
    
    # Count the occurrences of each element in array A
    for num in a:
        count_A[num] = count_A.get(num, 0) + 1
    
    # Count the occurrences of each element in array B
    for num in b:
        count_B[num] = count_B.get(num, 0) + 1
    
    # Compare the counts of elements in both arrays
    return count_A == count_B

n = int(input("Enter the size of array: "))

print("Enter array A elements")
a = list(map(int, input().split()))

print("Enter array B elements")
b = list(map(int, input().split()))

# Checking the length of both arrays with the given array size
if len(a)==len(b)==n:
    if are_arrays_equal(a,b):
        print("1")
    else:
        print("0")
else:
    print("Array size is not equal to the given size")