import os
import time

os.system("cls")

def GetValue(min, max, text):
    while True:
        try:
            value = int(input(text))
    
        except ValueError:
            print("Digite um valor numérico.")
            time.sleep(2)
            os.system("cls")
            continue
        
        if not min == None or not max == None: 
            if  not min <= value <= max:
                print(f"Digite um valor entre {min} e {max}.")
                time.sleep(2)
                os.system("cls")
                continue
        
        return value

nascimento = GetValue(0, 2026, "Insira seu ano de nascimento: ")
idade = 2026 - nascimento

print(f"{idade} anos, maior de idade: {idade > 18}")