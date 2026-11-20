import os
import time

os.system("cls")

def GetValue(min, text):
    while True:
        try:
            value = float(input(text))
    
        except ValueError:
            print("Digite um valor válido.")
            time.sleep(2)
            os.system("cls")
            continue
        
        if not min == None: 
            if value <= min:
                print(f"Digite uma valor maior que {min}")
                time.sleep(2)
                os.system("cls")
                continue
        
        return value


print("Bem vindo a loja do super soldado!\n")

ValorDeCompras = GetValue(0, "Insira o valor em compras: ")
ValorPago = GetValue(None, "Insira o valor pago ao caixa: ")

troco = ValorPago - ValorDeCompras

if ValorPago < ValorDeCompras:
    print("Volte quando tiver dinheiro.")
elif ValorPago == ValorDeCompras:
    print("Valor exato, volte sempre!")
else:
    print(f"Aqui está seus R${troco} de troco, volte sempre")