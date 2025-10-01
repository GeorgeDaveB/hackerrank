def isSubsetSum(arr, sum):
    runs = 0
    n = len(arr)
    prev = [False] * (sum + 1)
    curr = [False] * (sum + 1)


    prev[0] = True

    for i in range(1, n + 1):
        for j in range(0,sum + 1):
            if j < arr[i - 1]:
                curr[j] = prev[j]

            else:
                curr[j] = prev[j] or prev[j - arr[i - 1]]

        runs+=1
        print(f"run:{runs}")
        print(prev)
        print(curr)
        prev = curr.copy() 

    return prev[sum]

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum_value = 9
    if isSubsetSum(arr, sum_value):
        print("True")
    else:
        print("False")