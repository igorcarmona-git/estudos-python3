"""
Introdução ao desempacotamento

OBS:    1. Caso coloque mais variáveis do que valores, ocorre erro. (O mesmo vale, se for ao contrário)
        2. Muito usado '_' entre os desenvolvedores para indicar que uma variável está criada, mas não vai ser utilizada
        3. Utiliza-se '*' para pegar e armazenar o restante dos itens que não forem usados na desempacotação
"""

nome1, nome2, nome3 = ["Maria", "Helena", "Luiz"]
print(nome2)

nome1, *_ = ["Maria", "Helena", "Luiz"]
print(nome1, _) #'_' --> printa uma nova lista com o restante não desempacotado

_, nome2, *_ = ["Maria", "Helena", "Luiz"]
print(nome2, _)