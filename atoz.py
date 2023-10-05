def solution(s, skip, index):
    atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in skip:
        atoz.remove(i)

    ans = ''
    for i in s:
        ans += atoz[(atoz.index(i) + index) % len(atoz)]

    return ans


s = list(input("s 입력: "))
skip = list(input("skip 입력: "))
index = int(input("index 입력: "))

print(solution(s, skip, index))
