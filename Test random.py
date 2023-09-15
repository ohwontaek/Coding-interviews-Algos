from card_conv import card_conv


if __name__ == '__main__':

    print('10진수를 n진수로 변환합니다')

    while True:
        while True:
            no = int(input("변환할 값으로 음이 아닌 정수 입력:  "))
            if no > 0:
                break

        while True:
            cd = int(input('어떤 진수로 변환할까요? : '))
            if 2 <= cd <= 36:
                break
        print(f'{cd}진수로는 {card_conv(no,cd)}입니다')


