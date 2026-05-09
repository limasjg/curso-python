# ESQUELETO DO CURSO

#1 - Saida de Dados
# nome = "Luke"
# print(f"O nome do gato é {nome}")

# num = 12.5263
# print(f"O valor do número é {num:.2f}")

#2 - Variaveis
# nome = "João"
# idade = 33
# peso = 65.23
# vivo = True

#3 Type casting
# idade = input("qual a sua idade? ")
# # idade = int(input("qual a sua idade? ")) -# Converte no input

# # idade = int(idade) # Converte depois
# print(type(idade))

# print(f"Sua idade é {idade}")

#4 Operações Aritimetricas
# div = 5 / 2 # Divisão Float 2.5
# div2 = 5 // 2 # Divisão int 2 

# resto = 5 % 2

# expo = 5 ** 2 # Int 

# print(type(resto))

# print(resto)

#5 struturas condicionais:
# num1 = 100
# num2 = 200

# Bloco condicional único, usamos o elif se queremos adicionar outras condições antes do else (condições gerais que não o if)
# if num1 > num2:
#     print(f"Numero 1 {num1} é maior que o número 2 {num2}")
# elif num1 < num2:
#     print(f"Numero 2 {num2} é maior que o número 1 {num1}")
# else:
#     print(f"Numero 2 {num2} éigual o número 1 {num1}")

#Usamos mais de um IF quando queremos testar mais de um bloco condicional:
# fruta = "maçã"
# cor = "vermelha"

# if fruta == "maçã":
#     print("A fruta é maça")
# if cor == "vermelha":
#     print("A cor é vermelha")
# else:
#     print("Não tem fruta")

#6 Loops de repetição while:
#For itera uma sequencia (lista, string, range, etc) forma mais comum.
# lista = ["GBA", "PS1", "NES"]

# for console in lista:
#     print(console, end=" ") 

# for i in range(1, 6):
#     print(i)

#While - Excuta enquanto uma condição booleana é verdadeira - caso de uso - quando não sabemos quantas repetições vamos precisar.

# num = 0
# while num < 5:
#     print(num)
#     num += 1

# import time

# ligado = True

# while ligado:
#     for num in range(1, 4):
#         print(num)
#         time.sleep(1)
#     ligado = False

# while True:
#     itens = input("Escolha um item (n para sair): ").lower()
#     if itens == "n":
#         break

# contador = 0
# while contador < 4:
#     print(contador)
#     contador = contador + 1

# Estrutura de dados
# Listas - organizada e pode repetir o valor [ ]
# lista = [1, 2, 3]
# lista.append(3)
# print(lista)

#Sets não ordenada e Não elementos repetidos { }

# eletronico = {"TV", "Notebook", "Celular"}
# eletronico.add("Relógio")
# eletronico.add("Monitor") # Não repete

# print(eletronico)

#Tuplas - Imutáveis , ordenadas e permite repetição.
# veiculos = ["carro", "moto", "Van", "carro", "onibus"]
# print(veiculos[0]) # Da pra usar indice
# transportes = veiculos + ["Avião"] # da pra concatenar
# print(transportes)

#Dicionario {k:v} Mutável, ordenado (py 3.7), não permite chave igual

# pessoa = {"nome":"João", "idade":25, "Vivo":True}
# pessoa.update({"Cidade":"Curitiba"})
# print(pessoa["nome"])