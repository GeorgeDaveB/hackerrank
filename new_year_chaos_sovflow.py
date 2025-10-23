def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        print ("my q[i] is:", q[i])
        print ("my i + 1 is:", i+1)
        print ("im substracting", i+1, "from", q[i])
        print ("my result is:", (q[i] - (i+1)), "\n")
        if (q[i]- (i + 1)) > 2:
            print('Too chaotic')
            print (q[i] - (i+1))
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1
    print("my bribes", bribes)


    print(chaos)

q = [1, 2, 5, 3, 7, 8 ,6 ,4]
     0  1  2  3  4  5  6  7

     

#minimumBribes(q)
minimumBribes2(q)


q = [1, 2, 3, 4, 5, 6, 7, 8]
q = [1, 2, 3, 4, 5, 6, 8, 7]
q = [1, 2, 3, 4, 5, 8, 6, 7]
