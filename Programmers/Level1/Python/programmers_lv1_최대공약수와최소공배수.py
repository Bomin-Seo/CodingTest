def solution(n, m):
    answer = []
    x, y = n, m
    while y:
        x, y = y, x%y

    answer.append(x)

    answer.append(n*m // x )
    return answer

print(solution(2, 5))