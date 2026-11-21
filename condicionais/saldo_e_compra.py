import os
import time

os.system("cls")

def GetValue(min, text):
    while True:
        try:
            value = float(input(text))
    
        except ValueError:
            print("Digite um valor numérico.")
            time.sleep(2)
            os.system("cls")
            continue
        
        if not min == None: 
            if value <= min:
                print(f"Digite um valor maior que {min}.")
                time.sleep(2)
                os.system("cls")
                continue
        
        return value

print("Seja bem vindo a loja do super soldado!")
print("Você recebeu um cartão com saldo de R$200,00. Aproveite como quiser!\n")

saldo = 200
valor = GetValue(0, "Insira o valor da compra: ")

if valor > saldo:
    print("Saldo insuficiente")
else:
    print(f"Compra aprovada. Saldo restante R${saldo - valor}")
    