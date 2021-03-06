from math import sqrt

def soma_hipotenusas(n):
    soma = 1
    hipo = 0
    while soma <= n:
        if é_hipotenusa(soma):
            hipo += soma
        soma += 1
    return hipo


def é_hipotenusa(n):
    ca = 1
    co = 1
    hipo = False

    while ca <= n and not hipo:  # loop cateto adjacente
        while co <= n and not hipo:  # loop cateto oposto
            hipotenusa = sqrt(ca ** 2 + co ** 2)
            if n == hipotenusa:
                hipo = True
            co += 1
        co = 1
        ca += 1
    return hipo


def main():
    n = int(input('Número: '))
    print(soma_hipotenusas(n))


main()
