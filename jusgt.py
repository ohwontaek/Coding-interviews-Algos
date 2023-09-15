from max import max_of

print("베열의 최대값을 구한다")
print("end를 입력하면 종료")

number = 0
x =[]


while True:
    s = input(f'x[{number}] 값을 입력하세요 :  ')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(f'{number} 게를 입력했습니다')
print(f'최대값은 {max_of(x)} 입니다')