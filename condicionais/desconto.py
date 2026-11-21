import os
import time

os.system("cls") 

def GetValue(min, text):
    while True:
        try:
            value = int(input(text))
    
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

print("Seja bem vindo a loja do super soldado.")
print("Compras acima de 3 itens e R$150 recebem desconto e frete grátis")
print("Quantas camisas camufladas você gostia de comprar? (R$50 cada)\n")

quantidade = GetValue(0, "Insira a quantidade de camisas: ")
valor = quantidade * 50

print(f"Quantidade de produtos: {quantidade}, valor total: {valor}")
print(f"Direito ao benefício? {valor > 150}")