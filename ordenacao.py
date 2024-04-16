import random
import time
import math
import heapq

#Geracao de numeros aleatorios
def gerar_sequencia_aleatoria(tamanho, limite_inferior, limite_superior):
    sequencia = []
    for _ in range(tamanho):
        numero = random.randint(limite_inferior, limite_superior)
        sequencia.append(numero)
    return sequencia
limite_inferior = -100000000
limite_superior = 100000000
#Final da geracao de numeros aleatorios

#inicio sqrtsort
    #Insertion sort para o primeiro metodo
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def sqrtsort(arr):
    n = len(arr)
    sqrt_n = int(math.sqrt(n))
    result = []

    # Divide o vetor em partes de tamanho sqrt(n)
    parts = [arr[i:i+sqrt_n] for i in range(0, n, sqrt_n)]

    while any(parts):
        max_val = float('-inf')
        max_idx = None

        # Ordena cada parte usando insertion sort, cada novo vetor e criado de forma decrescente
        for part in parts:
            insertion_sort(part)

        # Encontra o maior elemento de cada parte
        for i, part in enumerate(parts):
            if part:
                max_part = part[0]  # Maior elemento após a ordenação
                if max_part > max_val:
                    max_val = max_part
                    max_idx = i

        # Insere o maior elemento na solução e remove da parte
        result.append(max_val)
        parts[max_idx].remove(max_val)

    return result[::-1]  # Retorna a solução em ordem decrescente
#Fim do sqrtsort

#Inicio sqrtsort com heap
def sqrtsort_heap(arr):
    n = len(arr)
    sqrt_n = int(math.sqrt(n))
    result = []

    # Divide o vetor em partes de tamanho sqrt(n)
    parts = [arr[i:i+sqrt_n] for i in range(0, n, sqrt_n)]

    while any(parts):
        max_val = float('-inf')
        max_idx = None

        # Usar heap para encontrar o maior elemento de cada parte
        max_heap = []

        for i, part in enumerate(parts):
            if part:
                max_part = -max(part)  # Converte para negativo para simular uma max heap
                heapq.heappush(max_heap, (max_part, i))  # Insere uma tupla (elemento, índice da parte)

        # Encontra o maior elemento dentre todas as partes
        max_val, max_idx = heapq.heappop(max_heap)

        # Insere o maior elemento na solução e remove da parte
        result.append(-max_val)  # Converte de volta para o valor original
        parts[max_idx].remove(-max_val)  # Remove o elemento da parte

    return result[::-1]  # Retorna a solução em ordem decrescente
#final sqrtsort com heap

#Coleta dos dados
    #Geracao da sequencia aleatoria
sequencia_aleatoria10_4 = gerar_sequencia_aleatoria(10000, limite_inferior, limite_superior)
sequencia_aleatoria10_5 = gerar_sequencia_aleatoria(100000, limite_inferior, limite_superior)
sequencia_aleatoria10_6 = gerar_sequencia_aleatoria(1000000, limite_inferior, limite_superior)
sequencia_aleatoria10_7 = gerar_sequencia_aleatoria(10000000, limite_inferior, limite_superior)
sequencia_aleatoria10_8 = gerar_sequencia_aleatoria(100000000, limite_inferior, limite_superior)

# Exemplo de uso
inicio1 = time.time()
sqrtsort(sequencia_aleatoria10_4)
final1 = time.time()
print('Tempo ordenar sqrtsort: ', (final1-inicio1), ' segundos')

inicio2 = time.time()
sqrtsort_heap(sequencia_aleatoria10_4)
final2 = time.time()
print('Tempo ordenar sqrtsor_heap: ', (final2-inicio2), ' segundos')
