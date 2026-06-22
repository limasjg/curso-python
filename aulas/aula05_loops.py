import time

# --- AULA 05: LOOPS DE REPETIÇÃO ---

# 1. Loop FOR (Usado quando sabemos o limite ou iteramos sequências)
print("--- Loop FOR em Listas ---")
consoles = ["GBA", "PS1", "NES"]
for console in consoles:
    print(console, end=" | ") 
print("\n")

print("--- Loop FOR usando Range (1 a 5) ---")
for i in range(1, 6):
    print(i)

# 2. Loop WHILE (Executa enquanto uma condição for verdadeira)
print("\n--- Loop WHILE Controlado por Contador ---")
contador = 0
while contador < 4:
    print(f"Contador: {contador}")
    contador += 1

# 3. Loop WHILE com parada manual (break)
print("\n--- Menu Interativo com Break ---")
while True:
    opcao = input("Escolha um item (Digite 'n' para sair): ").lower()
    if opcao == "n":
        print("Saindo do menu...")
        break
