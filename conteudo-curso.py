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

#Funções são blocos de código que só executam quando chamados. Podem receber argumentos e são reutilizáveis.
# def soma(num1, num2):
#     return num1 + num2

# print(soma(2, 2)) # saída: 4

# def mensagem():
#     print("Olá, mundo!")

# mensagem()

# def saudacoes(nome):
#     print(f"Olá, {nome}")

# saudacoes("João")

# def saudacoes(nome):
#     print(f"Olá, {nome}")

# user = input("Digite seu nome: ")
# saudacoes(user)

# def saudacao():
#     nome = input("digite seu nome: ")
#     print(f"Olá, {nome}")

# saudacao()

# def soma():
#     num1 = int(input("Difite o numero 1: "))
#     num2 = int(input("Difite o numero 2: "))
#     total = num1 + num2
#     print(f"A soma do {num1} + {num2} = {total}")

# soma()

#Classes - classes são moldes de encapsulamento de atributos e metodos, e aparti dela ciramos objetos. Instancias que usam o molde

# class Pessoa: #Aqui quando eu declaro a classe eu posso passar algum parametro?
#     def __init__(self, nome, idade): #Eu sou obrigado a toda vez que crio um classe usar esse metodo contrutor __init__ e passar o self referencia ao futuro objeto que ira usar essa classe.
#         self.nome = nome # Atributo da classe, sempre sou obrigado a passar.
#         self.idade = idade

#     def saudacao(self): # Aqui mesma coisa, preciso sempre passar o self?
#         print(f"O {self.nome} tem {self.idade} anos") # Aqui no print também o self é referencia aos valores do objeto certo?

# pessoa1 = Pessoa("João",25)

# pessoa1.saudacao()
# class Viculos("modelo", "cor", "ano"):

# class Teste:
#     def saudacao(self):
#         print(f"Olá, mundo")

# teste = Teste()
# teste.saudacao()

# class Veiculo:
#     def __init__(self, modelo, cor, ano):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano

#     def acelerar(self):
#         print(f"O {self.modelo} {self.cor} ano {self.ano} está acelerando!!!")

# # Coletando os dados do usuário
# modelo = input("Digite o modelo do veículo: ")
# cor = input("Digite a cor do veículo: ")
# ano = int(input("Digite o ano do veículo: "))

# # Criando o objeto com os valores informados
# carro = Veiculo(modelo, cor, ano) #Ou passo aqui direto.
# carro.acelerar()

