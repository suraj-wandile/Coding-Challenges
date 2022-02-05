def countFreq(arr):
    n = len(arr)

    ne = dict()

    for i in range(n):
        if arr[i] in ne.keys():
            ne[arr[i]] += 1
        else:
            ne[arr[i]] = 1

    for j in ne:
        print(j, " ", ne[j])


arr = [1, 2, 2, 1, 1, 2, 5, 2]
countFreq(arr)
