def solution(A,B):

    sortA = sorted(A)
    revsortB = sorted(B, reverse=True)

    revsortA = sorted(A, reverse=True)
    sortB = sorted(B)

    temp, temp2 = 0, 0
    for i in range(len(A)):
        temp += (sortA[i] * revsortB[i])
        temp2 += (revsortA[i] * sortB[i])

    return min(temp, temp2)

a = [1,4,2]
b = [5,4,4]

print(solution(a, b))