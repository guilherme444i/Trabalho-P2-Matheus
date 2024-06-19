# Quantidade de números da sequência Fibonacci a gerar
n = 10

# Casos base
if n <= 0:
    fibonacci_sequence = []
elif n == 1:
    fibonacci_sequence = [0]
elif n == 2:
    fibonacci_sequence = [0, 1]
else:
    # Inicializa os dois primeiros números da sequência
    fibonacci_sequence = [0, 1]
    
    # Calcula os próximos números da sequência
    for i in range(2, n):
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)

# Exibe a sequência Fibonacci gerada
print(f"Sequência Fibonacci de {n} números:", fibonacci_sequence)