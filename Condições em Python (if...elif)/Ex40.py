nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1 + nota2) / 2
if media < 5:
    print(f"Sua nota é de {media:.1f} e você esta REPROVADO")
elif media <=6.9:
    print(f"Sua nota é de {media:.1f} e você esta de RECUPERAÇÃO")
else:
    print(f"Sua nota é de {media:.1f} e você esta APROVADO")
