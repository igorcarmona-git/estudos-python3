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