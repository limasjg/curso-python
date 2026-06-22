# --- AULA 07: FUNÇÕES (BLOCOS REUTILIZÁVEIS) ---

# 1. Função com Retorno (Envia o resultado de volta)
def somar(num1, num2):
    return num1 + num2

resultado = somar(15, 25)
print(f"Resultado da soma: {resultado}")

# 2. Função de ação simples (Apenas executa um print)
def exibir_mensagem():
    print("Olá, bem-vindo ao curso de Python!")

exibir_mensagem()

# 3. Função que recebe parâmetros e interage com o usuário
def saudar_usuario(nome):
    print(f"Olá, {nome}! É um prazer ter você aqui.")

usuario = input("Digite seu nome para ser saudado: ")
saudar_usuario(usuario)
