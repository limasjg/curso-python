# --- AULA 09: TRATAMENTO DE ERROS (TRY / EXCEPT) ---

# 1. Tratando Divisão por Zero
try:
    numero = 10
    resultado = numero / 0
except ZeroDivisionError:
    print("✗ Erro: Não é possível dividir um número por zero!")

# 2. Tratando Erro de Digitação (ValueError)
try:
    idade = int(input("Digite sua idade (apenas números): "))
    print(f"Sua idade é {idade} anos.")
except ValueError:
    print("✗ Erro: Você não digitou um número inteiro válido!")

# 3. Capturando detalhes do erro com Exception as e
try:
    numero_invalido = float("Texto Qualquer")
except Exception as erro:
    print(f"✗ Erro Geral detectado: {erro}")

# 4. Desafio Prático: Tabuada Segura que não trava
print("\n--- DESAFIO: TABUADA SEGURA ---")
try:
    num_tabuada = int(input("Qual tabuada de 1 a 10 você quer gerar? "))
    if 1 <= num_tabuada <= 10:
        for i in range(1, 11):
            print(f"{num_tabuada} x {i:2} = {num_tabuada * i}")
    else:
        print("Digite apenas números entre 1 e 10.")
except Exception as e:
    print(f"Não foi possível gerar a tabuada. Detalhe: {e}")
