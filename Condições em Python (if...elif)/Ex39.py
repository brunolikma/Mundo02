import datetime
anoNascimento = int(input("Digite o ano que voce nasceu: "))
data = datetime.date.today()
ano = data.strftime("%Y")
anoAtual = int(ano)
idade = anoAtual - anoNascimento
if idade < 18:
    print(f"Voce é muito novo, \n"
          f"ainda falta {18 - idade} anos para se alistar")
elif idade == 18:
    print(f"Você tem {idade} anos, ja pode se alistar.")
else:
    print(f"Ja passou {idade - 18 } anos para se alisar ")
