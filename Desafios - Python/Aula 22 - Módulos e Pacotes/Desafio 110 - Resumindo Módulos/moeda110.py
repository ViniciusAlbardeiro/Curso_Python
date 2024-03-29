# num = float(input(' Digite um valor:'))
# print(f'O valor analisado é {moeda(num)}')
# print(f' Seu dobro vale {dobro(num, True)}')
# print(f' Sua metade vale {metade(num, True)}')
# print(f' Seu valor com um aumento de 40% vale {aumento(num, 40, True)}')
# print(f' Seu valor com uma redução de 15% vale {reducao(num, 15, True)}')


def resumo(n, taxa_aum, taxa_red):
    def dobro(num, money):
        num *= 2
        if money is True:
            formatnum = "R$" + str(num).replace(".0", ",00")
            return formatnum
        else:
            return num

    def metade(num, money):
        num /= 2
        if money is True:
            formatnum = "R$" + str(num).replace(".0", ",00")
            return formatnum
        else:
            return num

    def aumento(num, taxa, money):
        num += num * taxa / 100
        if money is True:
            formatnum = "R$" + str(num).replace(".0", ",00")
            return formatnum
        else:
            return num

    def reducao(num, taxa, money):
        num -= num * taxa / 100
        if money is True:
            formatnum = "R$" + str(num).replace(".0", ",00")
            return formatnum
        else:
            return num

    def moeda(num):
        moedaformat = 'R$' + str(num) + '0'
        return moedaformat

    valor = moeda(n)
    dobro = dobro(n, True)
    metade = metade(n, True)
    aumento = aumento(n, taxa_aum, True)
    reducao = reducao(n, taxa_red, True)
    ljustvar = 50
    rjustvar = 10

    return print("", '-' * 40 + '\n',
                 'RESUMO'.center(40)+'\n',
                 '-' * 40,
                 f"\n Valor Analisado:".ljust(ljustvar, '.') + f"{valor}",
                 f'\n Seu dobro:'.ljust(ljustvar, '.') + f'{dobro}',
                 f'\n Sua metade:'.ljust(ljustvar, '.') + f'{metade}',
                 f'\n Aumento de {taxa_aum}%:'.ljust(ljustvar, '.') + f'{aumento}',
                 f'\n Redução de {taxa_red}%:'.ljust(ljustvar, '.') + f'{reducao}')
