valorCasa = float(input("Digite o valor da casa a ser financiado: "))
salarioComprador = float(input('Digite seu salario: '))
anosPagando = int(input("Em quantos anos deseja pagar: "))
prestacao = valorCasa / (anosPagando * 12)
salarioAprovado = salarioComprador  * 0.30
print(f"O financiamento de uma casa no valor de {valorCasa:.2f} em {anosPagando} anos, a prestação da casa fica em {prestacao:.2f} ")

if prestacao <= salarioAprovado:
    print("Financiamento APROVADO")
else:
    print("Financiamento RECUSADO")