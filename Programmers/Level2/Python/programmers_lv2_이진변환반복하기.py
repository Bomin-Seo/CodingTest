def solution(s):
    answer = []
    temp = ''
    trans, remove_c = 0, 0
    while temp != '1':
        temp = ''
        for i in s:
            if i == '0':
                remove_c += 1
            else:
                temp += i

        temp = bin(len(temp))[2:]
        trans += 1
        s = temp

    answer.append(trans)
    answer.append(remove_c)
    return answer