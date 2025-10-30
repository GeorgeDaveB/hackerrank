def birthday(s, d, m):
    l = len(s)
    subset = [0] * l
    subset[0] = s[0]
    count = 0
    for i in range(1,l):
        subset[i] = subset[i-1] + s[i]
    print(f'Subset length: {len(subset)}.')
    print(f'Original arr.: {s}')
    print(f'Our subset is: {subset}')
    if subset[m-1] == d:
         count+=1
    print(f"We checked if subset at position {m-1} which equals {subset[m-1]} would equal to 10")
    for j in range(m,l): 
        result = subset[j] - subset[j-m]
        print(f'We took {subset[j]}, at position {j}, and substracted it with {subset[j-m]} at position {j-m}, to get result {result}')
        if result == d:
            count+=1
    return count


if __name__ == '__main__':
    s = [2, 2, 2, 1, 3, 2, 2, 3, 3, 1, 4, 1, 3, 2, 2, 1, 2, 2, 4, 2, 2, 3, 5, 3, 4, 3, 2, 1, 4, 5, 4]
    d = 10
    m = 4
    print(birthday(s, d, m))