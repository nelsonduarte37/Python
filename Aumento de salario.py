sal=float(input("Digite seu salario: "))
if (sal > 1250):
        sal=sal.replace("."),(",")
        sal=sal*0.10
        print("Seu salario será:  R$%.2f"%sal)
        
