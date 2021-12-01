from math import inf
from time import time


def max_alg(iteravel):  #algoritmo que retorna o maior valor
    max_number = -inf
    for number in iteravel:
        if number > max_number:
            max_number = number
    return max_number


if __name__ == '__main__':
    print(max_alg([1]))
    print(max_alg([1, 8]))
    print(max_alg([1, 100]))
    print(max_alg([-2, -3]))

    print('Estudo experimental sobre o tempo de execução da função max')

    init = 10_000_000
    for n in range(0, init * 20 + 1, init):
        inicio = time()
        max_alg(range(n))
        fim = time()

        exec_time_seconds = fim - inicio
        print('=' * int(exec_time_seconds * 10), n)
