# python-assignment
1. Add some sentences inside a text file. Read that file and show an array which contains
every word present in the file and their respective count.
Example = I am a developer.
output = [
{'I' => 1},
{'am' => 1},
{'a' => 1},
{'developer' => 1},
];

2. Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N.
Find the missing element.
Example 1:
Input:
N = 5
A[] = {1,2,3,5}
Output: 4
Example 2:
Input:
N = 10
A[] = {6,1,2,8,3,4,7,10,5}
Output: 9
Constraints:
1 ≤ N ≤ 10
6
1 ≤ A[i] ≤ 10
6

3.Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not.
Two arrays are said to be equal if both of them contain same set of elements, arrangements
(or permutation) of elements may be different though.
Note : If there are repetitions, then counts of repeated elements must also be same for two
array to be equal.
Example 1:
Input:
N = 5
A[] = {1,2,5,4,0}
B[] = {2,4,5,0,1}
Output: 1
Explanation: Both the array can be
rearranged to {0,1,2,4,5}
Example 2:
Input:
N = 3
A[] = {1,2,5}
B[] = {2,4,15}
Output: 0
Explanation: A[] and B[] have only
one common value.
Your Task:
Write a function which takes both the given array and their size as function arguments and
returns true if the arrays are equal else returns false. The 0 and 1 printing is done by the
driver code.
Constraints:
1<=N<=10
7
1<=A[],B[]<=10
