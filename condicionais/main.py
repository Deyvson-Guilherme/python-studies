import os
import time

os.system("cls")

def GetValue(min, max, text):
    while True:
        try:
            value = float(input(text))
    
        except ValueError:
            print("Digite um nota válida.")
            time.sleep(2)
            os.system("cls")
            continue
        
        if not min <= value <= max:
            print(f"Digite uma valor entre {min} e {max}")
            time.sleep(2)
            os.system("cls")
            continue
        
        return value

nota_1 = GetValue(0, 10, "Insira a nota da N1: ")
nota_2 = GetValue(0, 10, "Insira a nota da N2: ")
frequencia = GetValue(0, 100, "Insira a frequência: ")

media = (nota_1 + nota_2) / 2

estado = None

if media >= 7:
    estado = "aprovado"
elif media >= 5:
    estado = "recuperação"
else:
    estado = "reprovado"

if estado == "aprovado" and frequencia >= 75:
    print(f"media {media}, frequência {frequencia}, aluno aprovado")
elif estado == "recuperação" and frequencia >= 75:
    print(f"media {media}, frequência {frequencia}, aluno de recuperação")
elif estado == "reprovado" and frequencia >= 75:
    print(f"media {media}, frequência {frequencia}, aluno reprovado por nota")
else:
    print(f"media {media}, frequência {frequencia}, aluno reprovado por frequência")