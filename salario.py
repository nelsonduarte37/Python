saltot=float(input("Quanto voce recebe de salário: "))
hdia=float(input("Quantas horas trabalha por dia: "))
calculo=(saltot/(hdia*30))
print("Voce recerá R${:.2f}".format(calculo,"por hora trabalhada."))
