

#1 - Verificar se um número pertence à sequência de Fibonacci

def pertence_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

# Número a ser verificado (pode ser modificado ou recebido via entrada)
numero = 21

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")




