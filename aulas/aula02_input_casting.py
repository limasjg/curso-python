# --- AULA 02: INPUT E TYPE CASTING ---

# Capturando dados (Sempre vem como string!)
idade_texto = input("Qual a sua idade? ")
print(f"Tipo antes da conversão: {type(idade_texto)}")

# Conversão depois de capturar (Casting)
idade_convertida = int(idade_texto)
print(f"Sua idade convertida é {idade_convertida} | Tipo: {type(idade_convertida)}")

# Conversão direta na mesma linha (Melhor prática!)
altura = float(input("Qual a sua altura em metros (ex: 1.75)? "))
print(f"Sua altura é {altura}m | Tipo: {type(altura)}")
