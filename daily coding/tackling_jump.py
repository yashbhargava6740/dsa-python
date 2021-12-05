"""
This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, 
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""

lst = list(map(int, input().split()))
i = maxReached = 0
while i < len(lst) and i <= maxReached:
    maxReached = max(i + lst[i], maxReached)
    # print(maxReached, i)
    i += 1
print(i == len(lst))

    
