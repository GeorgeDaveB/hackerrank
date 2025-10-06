### BEGIN
# This is definitely not the most pythonic way...
# But I AM proud of coming up with it on my own.

#This shifts all values of an array to the left.
#It catches negative values too. We are safe from arr[-1] as a scenario
#And neither would abs() work, because absolutes would cause different loop iterations
#... to loop at the same array position.

def rotateLeft(d,arr):
    a_len = len(arr)
    arr_r = [0] * a_len
    for i in range (a_len):
         rotated = (a_len + (i - (d % a_len))) % a_len
         arr_r[rotated] = arr[i]
    return arr_r


if __name__ == '__main__':
    d = 16
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(rotateLeft(d,arr))
    
### END