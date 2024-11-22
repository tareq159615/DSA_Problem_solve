## Brute Force Approach--------------------------------------------

import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum

    for i in range(n):
        for j in range(i, n):
            # subarray = arr[i.....j]
            summ = 0

            # add all the elements of subarray:
            for k in range(i, j+1):
                summ += arr[k]

            maxi = max(maxi, summ)

    return maxi

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(arr)
    maxSum = maxSubarraySum(arr, n)
    print("The maximum subarray sum is:", maxSum)

# Time Complexity: O(N3), where N = size of the array.
# Reason: We are using three nested loops, each running approximately N times.

# Space Complexity: O(1) as we are not using any extra space.



## Better Approach---------------------------------------------------------

import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize-1 # maximum sum
    sum = 0

    for i in range(n):
        sum += arr[i]

        if sum > maxi:
            maxi = sum

        # If sum < 0: discard the sum calculated
        if sum < 0:
            sum = 0

    # To consider the sum of the empty subarray
    # uncomment the following check:

    #if maxi < 0: maxi = 0

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)

# Time Complexity: O(N), where N = size of the array.
# Reason: We are using a single loop running N times.

# Space Complexity: O(1) as we are not using any extra space.


## Optimal Approach---------------------------------------------------


import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum
    sum = 0

    start = 0
    ansStart, ansEnd = -1, -1
    for i in range(n):

        if sum == 0:
            start = i  # starting index

        sum += arr[i]

        if sum > maxi:
            maxi = sum

            ansStart = start
            ansEnd = i

        # If sum < 0: discard the sum calculated
        if sum < 0:
            sum = 0

    # printing the subarray:
    print("The subarray is: [", end="")
    for i in range(ansStart, ansEnd + 1):
        print(arr[i], end=" ")
    print("]")

    # To consider the sum of the empty subarray
    # uncomment the following check:

    # if maxi < 0:
    #     maxi = 0

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)

# Time Complexity: O(N), where N = size of the array.
# Reason: We are using a single loop running N times.

# Space Complexity: O(1) as we are not using any extra space.