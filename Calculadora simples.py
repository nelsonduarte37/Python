num1= int(input("Digite o primeiro numero: \n"))
num2= int(input("Digite o segundo numero: \n"))
sinal= input("Qual operação deseja realizar? \n")
if sinal == ("+"):
    print("A soma é: ",(num1+num2))
elif sinal == ("-"):
    print("A subtração é: ",(num1-num2))
elif sinal == ("*"):
    print("A multiplicação é: ",(num1*num2))
elif sinal == ("/"):
    print("A divisão é: ",(num1/num2))
else:
    print("Sinal inválido!")
