print("Calculadora média notas\nDitite as notas entre [0-25]")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
total = (nota1+nota2+nota3+nota4)
media = (total/4)
if nota1 < 0 or nota1 > 25 or nota2 < 0 or nota2 > 25 or nota3 < 0 or nota3 > 25 or nota4 < 0 or nota4 > 25:
    print("Valor inválido")
if total >= 80:
    print("ALUNO APROVADO - EXCELENTE")
elif total >= 60 and media <= 79:
    print("ALUNO APROVADO")
elif total >= 40 and media <= 59:
    print("ALUNO EM RECUPERAÇÃO")
else:
    print("ALUNO REPROVADO")

print("Sua média foi: %.2f "%media)

