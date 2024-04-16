peso=float(input("Digite seu peso: "))
altura=float(input("Qual sua altura: "))
imc=(peso/(altura**2))
print("Seu imc é: {:.3f}".format(imc,"kg/m2."))
