## Brute Force Approach--------------------------------------------



def missing_number(a, N):
    # Outer loop that runs from 1 to N:
    for i in range(1, N + 1):
        # flag variable to check if an element exists
        flag = 0

        # Search the element using linear search:
        for j in range(len(a)):
            if a[j] == i:
                # i is present in the array:
                flag = 1
                break

        # check if the element is missing (i.e., flag == 0):
        if flag == 0:
            return i

    # The following line will never execute.
    # It is just to avoid warnings.
    return -1

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missing_number(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()








## Better Approach---------------------------------------------------------



def missingNumber(a, N):
    hash = [0] * (N + 1)  # hash array

    # storing the frequencies:
    for i in range(N - 1):
        hash[a[i]] += 1

    # checking the frequencies for numbers 1 to N:
    for i in range(1, N + 1):
        if hash[i] == 0:
            return i

    # The following line will never execute.
    # It is just to avoid warnings.
    return -1

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()





## Optimal Approach---------------------------------------------------



def missingNumber(a, N):
    # Summation of first N numbers:
    summation = (N * (N + 1)) // 2

    # Summation of all array elements:
    s2 = sum(a)

    missingNum = summation - s2
    return missingNum

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()


## Optimal Approach---------------------------------------------------



def missingNumber(a, N):
    xor1 = 0
    xor2 = 0

    for i in range(N - 1):
        xor2 = xor2 ^ a[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]
    
    xor1 = xor1 ^ N  # XOR up to [1...N]

    return xor1 ^ xor2  # the missing number


def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)


if __name__ == '__main__':
    main()




















# Complexity Analysis

# Time Complexity: O(N2), where N = size of the array+1.
# Reason: In the worst case i.e. if the missing number is N itself, the outer loop will run for N times, and for every single number the inner loop will also run for approximately N times. So, the total time complexity will be O(N2).

# Space Complexity: O(1)  as we are not using any extra space.