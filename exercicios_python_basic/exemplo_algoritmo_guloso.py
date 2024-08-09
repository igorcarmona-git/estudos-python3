"""
Exemplo de Algoritmo Guloso

Um algoritmo guloso pode ser utilizado para resolver problemas que não possuem um algoritmo que resolveria de forma rápida.

Esse algoritmo, tem como objetivo, quando se é necessário fazer uma escolha durante o processo de otimização em que cada iteração, 
irá fazer a escolha que parece ser a melhor no momento para chegar na melhor solução final que ele consegue.

Faz uma ótima escolha local, mas não é eficiente fazendo a melhor escolha global. 
"""
tasks = [1, 3, 6, 7, 10]

MAX_TIME = 10

current_time = 0
current_tasks = 0

for task_time in tasks:
    current_time += task_time

    if current_time > MAX_TIME:
        break

    current_tasks += 1


# Aqui estão alguns cenários em que esse código pode ser útil:

# Agendamento de tarefas: Se você tiver uma lista de tarefas com durações conhecidas e quiser agendar o máximo possível dessas tarefas dentro de um determinado período de 
# tempo, o código pode ajudar a determinar quantas tarefas podem ser executadas dentro do limite de tempo.

# Processamento de recursos limitados: Se você estiver trabalhando com recursos limitados, como CPU ou tempo de execução em um sistema, e quiser executar o máximo possível 
# de tarefas dentro desses limites, o código pode ajudar a determinar quantas tarefas podem ser concluídas dentro do tempo ou recursos disponíveis.

# Otimização de processos: Ao otimizar processos que têm restrições de tempo, você pode usar esse código para identificar quantas tarefas podem ser realizadas dentro do 
# tempo máximo permitido. Isso pode ajudar a ajustar a programação de tarefas ou priorizar as mais importantes dentro de um limite de tempo.

# Simulações: Em simulações ou modelos em que você precisa executar etapas sequenciais de tarefas com durações conhecidas, esse código pode ser usado para acompanhar o 
# tempo total acumulado e determinar quantas tarefas podem ser realizadas dentro do tempo máximo especificado.