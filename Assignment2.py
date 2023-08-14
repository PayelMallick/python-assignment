def find_distinct_integer(n, arr):
    sum_of_num = n * (n + 1) // 2
    sum_of_arr = sum(arr)
    integer = sum_of_num-sum_of_arr
    if integer==0:
        return "No integer is missing"
    return integer

n = int(input("Enter the range: "))
arr = list(map(int,input().split()))

distinct_integer = find_distinct_integer(n,arr)
print(distinct_integer)