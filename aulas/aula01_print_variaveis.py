# --- AULA 01: SAÍDA DE DADOS E VARIÁVEIS ---

# 1. Saída de Dados com f-strings
nome_gato = "Luke"
print(f"O nome do gato é {nome_gato}")

# Formatando casas decimais (.2f)
num = 12.5263
print(f"O valor do número é {num:.2f}")

# 2. Tipos de Variáveis fundamentais
nome = "João"      # String (Texto)
idade = 33         # Int (Inteiro)
peso = 65.23       # Float (Decimal)
vivo = True        # Bool (Booleano)

print("\nFicha Cadastral:")
print(f"Nome: {nome} | Tipo: {type(nome)}")
print(f"Idade: {idade} | Tipo: {type(idade)}")
print(f"Peso: {peso} | Tipo: {type(peso)}")
print(f"Vivo: {vivo} | Tipo: {type(vivo)}")
