# --- AULA 04: ESTRUTURAS CONDICIONAIS ---

num1 = 100
num2 = 200

# Exemplo 1: Bloco condicional encadeado (if, elif, else)
print("--- Comparando dois números ---")
if num1 > num2:
    print(f"Número 1 ({num1}) é maior que o número 2 ({num2})")
elif num1 < num2:
    print(f"Número 2 ({num2}) é maior que o número 1 ({num1})")
else:
    print(f"Os números são iguais ({num1})")

# Exemplo 2: Múltiplos IFs independentes (Testa todas as condições)
print("\n--- Verificação de Fruta ---")
fruta = "maçã"
cor = "vermelha"

if fruta == "maçã":
    print("✓ A fruta é maçã")
if cor == "vermelha":
    print("✓ A cor é vermelha")
else:
    print("✗ Não atendeu às condições de cor")
