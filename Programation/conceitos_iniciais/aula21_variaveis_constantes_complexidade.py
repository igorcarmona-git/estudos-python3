"""
variaveis em letra maiuscula para dizer que são constantes

CONSTANTE = "Variáveis" que não vão mudar

Muitas condições no mesmo if (ruim)

    <- Contagem de complexidade (ruim)
"""

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 5  # A distância onde o radar pega

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

velocidade_acima_radar1 = (velocidade > RADAR_1)
dentro_distancia_radar = (local_carro >= (LOCAL_1 - RADAR_RANGE)) and (local_carro <= (LOCAL_1 + RADAR_RANGE)) #raio de distancia

if velocidade_acima_radar1:
    print("Velocidade do carro passou do RADAR 1")

if dentro_distancia_radar and velocidade_acima_radar1:
    print("Carro multado em RADAR 1")

# '\' permite continuar o código na outra linha
# É interessante você simplificar a complexidade do código, colocando grandes expressões em variáveis
