string = input("Digite uma palavra: ")
numletras = int(input("Quantas letras você deseja separar? "))
parte1 = string[:numletras]
parte2 = string[numletras:]
print("Parte 1:", parte1)
print("Parte 2:", parte2)
