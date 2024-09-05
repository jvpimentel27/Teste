try:
    num = int(input("Informe um número inteiro: "))
    seq_fib = [0, 1]
    
    while seq_fib[-1] < num:
        
        seq_fib.append(seq_fib[-1] + seq_fib[-2])
    
    
    if num in seq_fib:
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
except ValueError:
    print("Erro na digitação de dados. Por favor, informe um número inteiro válido.")