## Test of subset array problem to see if I remember
# This particular code tries to find which numbers of an array add up to a sum


def subsetSum(s,arr):
    diff = [0] * (s+1)
    
    for a,b,k in arr:
        diff[a-1] += k
        diff[b] -= k
    running_var = 0
    max_val = 0
    for x in diff:
        running_var += x
        if running_var > max_val:
            max_val = running_var
    return max_val


if  __name__ =='__main__':
    s = 5
    arr = [[1, 4, 100], [2,3,100], [3 , 5 , 100], [2, 5, 100], [1, 2 , 100]]
    print('Result is: ', subsetSum(s,arr))
