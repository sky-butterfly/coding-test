from ctypes import sizeof


def solution(s):
    answer = ''

    arr = ['ze', 'on', 'tw', 'th', 'fo', 'fi', 'si', 'se', 'ei', 'ni']
    complateArr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = ''

    while 'True':

        if len(s) == 0: 
            break;

        ss = s[0]
        if ss.isnumeric():
            answer += ss
            s = s[1:]
            continue

        ss = s[:2]
        idx = arr.index(ss)
        answer += str(idx)
        compateStr = complateArr[idx]
        s = s[len(compateStr):]   

    return int(answer)


print(solution('one4seveneight'))