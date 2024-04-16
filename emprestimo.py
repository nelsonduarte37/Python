valorcasa = float(input("Valor da casa: R$"))
salario = float(input("Salário: R$"))
anos = int(input("Anos a pagar: "))
prestacaomensal = valorcasa / (anos * 12)
limiteprestacao = salario * 0.3
if prestacaomensal > limiteprestacao:
    print("Empréstimo negado. Prestação mensal excede 30% do salário.")
else:
    print("Empréstimo aprovado. Prestação mensal: R$%.2f" % prestacaomensal)

