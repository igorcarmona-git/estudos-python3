"""

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 

descrito, exiba a saudação apropriada. Ex. 

Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Que horas são: ")

#Usa-se try para tratar os erros que possam ocorrer
try: 
    int_hora = int(hora)

    if (int_hora >= 0) and (int_hora <= 11):
        print(f"Bom dia! Agora são: {hora} horas!")
    elif (int_hora >= 12) and (int_hora <= 17):
        print(f"Boa tarde! Agora são: {hora} horas!")
    elif (int_hora >= 18) and (int_hora <= 23):
        print(f"Boa noite! Agora são: {hora} horas!")
    else:
        print(f"Não conheço essa hora!")
except:
    print(f"Por favor, digite apenas números!")

