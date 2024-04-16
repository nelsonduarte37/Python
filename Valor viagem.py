dist = float(input("Qual a distancia que deseja percorrer? "))

if dist <= 200:
    val = dist * 0.5
    valstr = str("Você vai pagar R$%.2f" % val).replace(".", ",")
else:
    val = dist * 0.45
    valstr = str("Você vai pagar R$%.2f" % val).replace(".", ",")

print(valstr)
