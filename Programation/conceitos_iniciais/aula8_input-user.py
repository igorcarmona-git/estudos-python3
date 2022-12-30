nome = input("Qual o seu nome? ")
print(f"O seu nome é {nome}") #Se você quiser ver nome da variável, basta colocar {nome=}
print(f"O seu nome é {nome=}") # Exemplo...

n1 = input("Digite um número: ")
n2 = input("Digite outro número: ")

# Fazer o type casting assim, é uma boa prática pois permite fazer a checagem do que o usuário digita
# Bloqueando o usuário de digitar letras e quebrar o programa.

int_n1 = int(n1)
int_n2 = int(n2)

print(f"A soma dos números são: {int_n1 + int_n2}")