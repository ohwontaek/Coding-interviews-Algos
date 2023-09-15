def card_conv(x: int, r: int) -> str:

    d = ''
    dchar = '01234567889900asdgwrgfwgef'

    while x > 0 :
        d += dchar[x % r]
        x //= r

    return d[::-1]
