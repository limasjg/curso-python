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

#6 Loops de repetição:
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

#7 Estrutura de dados
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

#8 Funções são blocos de código que só executam quando chamados. Podem receber argumentos e são reutilizáveis.
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

#9 Classes - classes são moldes de encapsulamento de atributos e metodos, e aparti dela criamos objetos. Instancias que usam o molde

# class Pessoa(): #Classe
#     def __init__(self, nome, idade): #Construtor__init__ não é obrigatório, mas necessário se quiser receber dados ao criar objetos e receber atributos
#         self.nome = nome #Atributo da classe
#         self.idade = idade

#     def apresentar(self): #Método
#         print(f"Olá, meu sou o {self.nome} e tenho {self.idade} anos")

# class Trabalho(Pessoa): #Classe filha
#     def __init__(self, nome, idade, profissao,):
#         super().__init__(nome, idade) #Super extende as funções da classe pai
#         self.profissao = profissao #Atributo

#     def falar_profissao(self):
#         print(f"Eu sou {self.profissao}")


# pessoa1 = Trabalho("Ana", "20", "Medica")
# pessoa1.apresentar()
# pessoa1.falar_profissao()

# 9.1 Encapsulamento é a maneira de proteger atributos de acesso direto ou conflitos de herança.
# podemos usar _atributo apenas para sinalizar ou __atributo para "esconder" o nome.
# class Conta():
#     def __init__(self, saldo):
#         self.__saldo = saldo # esse __ (underline/underscore) serve para dizer não mexa nisso.

#     def mostrar_saldo(self):
#         print(f"Saldo {self.__saldo}")

# class Banco(Conta):
#     def __init__(self, saldo, agencia):
#         super().__init__(saldo)
#         self.agencia = agencia

#     def local(self):
#         print(f"Na {self.agencia} meu saldo é {self.saldo}") # da erro, para acessar é necessário usar o _Conta__saldo.

# pessoa1 = Banco(3000, "Curitiba2")
# pessoa1.local()

# 9.2 Herança é a forma de reaproveitar classes,
# herdando atributos e métodos de outra classe.
#
# Isso permite extender funcionalidades
# sem precisar repetir código.
# class Veiculo():
#     def __init__(self, modelo, cor):
#         self.modelo = modelo
#         self.cor = cor
    
#     def informar_modelo(self):
#         print(f"O Veiculo é {self.modelo}")

# class Carro(Veiculo):
#     def __init__(self, modelo, cor, ano):
#         #self.modelo = modelo
#         #self.cor = cor
#         super().__init__(modelo, cor) #Melhor pática, pois podemos usar todos os atributos da classe pai, sem precisar definir um por um.
#         self.ano = ano

#     def informar_carro(self):
#         print(f"Meu carro é um {self.modelo} {self.cor} ano {self.ano}")

# carro1 = Carro("gol","azul", 2013)
# carro1.informar_carro()

# 9.3 Polimorfismo é a capacidade de um mesmo método
# ter comportamentos diferentes dependendo da classe.
# class Animal:
#     def fazer_som(self): # Método pai
#         print("Som do animal")

# class Cachorro(Animal):
#     def fazer_som(self): #Sobescreve o método pai
#         print("Au Au!")

# class Gato(Animal):
#     def fazer_som(self): #mesmo método da classe cachorro mas com comportamento diferente
#         print("miau!")

# cao1 = Cachorro()
# cao1.fazer_som()

# gato1 = Gato()
# gato1.fazer_som()

# 9.4 Abstração
#
# Abstração em POO serve para esconder complexidade
# e mostrar apenas o necessário para usar um objeto.
#
# Também pode ser usada para padronizar classes filhas.
# class Pagamento():
#     def metodo(self):
#         print("Você está pagando")
#         print("Processando...")
#         print("Pagamento realizado")

# pix = Pagamento()
# pix.metodo()#Chamamos apenas um metodo, que faz diversos prints.

# #Padroniza
# from abc import ABC, abstractmethod 

# class Animal(ABC):
#     @abstractmethod # A classe Animal funciona como um molde/regra. @abstractmethod obriga a classe filha implementar aquele método.
#     def fazer_som(self):
#         pass

# class Cao(Animal):
#     def fazer_som(self): # Toda classe filha precisa implementar o método fazer_som().
#         print("Au Au")

# dog = Cao()
# dog.fazer_som()

#explicação mais robusta
# POO (Programação Orientada a Objetos) é um paradigma da programação,
# ou seja, uma maneira de programar utilizando classes e objetos.
#
# Classes funcionam como moldes para criar objetos,
# contendo atributos e métodos.
#
# A POO possui 4 pilares principais:
#
# Encapsulamento:
# Protege e controla o acesso aos dados.
#
# Herança:
# Permite reaproveitar atributos e métodos de outras classes.
#
# Polimorfismo:
# Permite utilizar o mesmo método com comportamentos diferentes.
#
# Abstração:
# Esconde complexidades e pode padronizar comportamentos.

# Explicação simples:
# POO é uma forma de programar usando objetos e classes
# para organizar melhor o código.
#
# Classes funcionam como moldes para criar objetos.
#
# Os 4 pilares da POO são:
#
# Encapsulamento:
# proteger dados.
#
# Herança:
# reaproveitar código.
#
# Polimorfismo:
# usar o mesmo método de formas diferentes.
#
# Abstração:
# esconder complexidade.

# Tratamento de erros - Usamos tratamento de erros em python, para realizar troubleshoting com mmaior eficiencia bem como organizar e debugar melhor o código
# |Ou seja, usamos para previnir os erros, de forma que o código siga mesmo diante de um erro e esse erro fique fácil a visualização, ou caso paremos o fluxo, tenha
# uma mensagem clara para o usuário
# try:
#     numero = 10
#     resultado = numero / 0
#     print(f"Resultado igual a {resultado}")
# except ZeroDivisionError:
#     print("Não é possivel dividir por zero")

# try:
#     idade = int(input("Digite usa idade: "))
#     print(f"Sua idade é {idade} anos")
# except ValueError:
#     print(f"Valor é um valor inválido")
# try:
#     cpu = float(input("Quantos núcleos esse cpu tem: "))
#     print(f"Esse cpu tem {cpu} núcleos")
# except Exception as e:
#     print(f"Detalhe do erro: {e}")

#Tabuada
# try:
#     num = int(input("Qual tabuada de 1 a 9 você quer? "))

#     if 1 <= num <= 10:
#         for multi in range(1, 11):
#             print(f"{num} x {multi:2} = {num * multi}")
# except Exception as e:
#     print(f"Erro: {e}")

#Manipipulação de arquivos e pastas - Extremamente importante para infra estrutura e devops
# Detecção de caminhos
# import os #Muito importante saber lidar com esse import, pois operation sistem é a base de comunicação com a máquina.
#Exemplos

#file_path = "testes/teste.txt" # Caminho relativo
# file_path = "C:\\Users\\meu-user\\Desktop\\teste" # Caminho absoluto
# if os.path.exists(file_path):
#     print("O caminho existe!")
#     if os.path.isfile(file_path):
#         print("É um arquivo.")
#     elif os.path.isdir(file_path):
#         print("É uma pasta.")
# else:
#     print("O caminho Não existe.")

# import os
# local_path = "."
# local_list = os.listdir(local_path)
# print(local_list)

# import os
# local_path = "."
# for item in os.listdir(local_path):
#     print(item)

#Escrevendo em arquivos

# txt_data = "Novo arquivo!" #Variavel com o texto da mensagem
# file_path = "C:\\Users\\limas\\Desktop\\output.txt"

# with open(file_path, "a") as file: #Usamos o with como boa prática pois ele fecha o arquivo automáticamente (caminho, modo)
#     #mode "w" = Cria o arquivo e escreve nele, ou sobrescreve.
#     #modo "x" = Cria o arquivo se ele não existe, não sobrescreve
#     #modo "a" = append ou seja, adiciona ao arquivo. Tbm cria caso não exista
#     file.write(txt_data) #função de escrita
#     print("Mesagem escrita")

# # Escrevendo Listas
# personagens = ["Naruto", "Ichigo", "Goku", "Eduard"]
# file_path = "output.txt"

# with open(file_path, "a") as file:
#     for personagem in personagens:
#         file.write(personagem + "\n")
#     print("Lista escrita no arquivo.")

#Escrevendo Json
# import json
# ninja = {
#     "Nome": "Naruto",
#     "idade": 33,
#     "profissão": "Hokage"
# }
# file_path = "output.json"
# try:
#     with open(file_path, "w", encoding="utf-8") as file:
#         json.dump(ninja, file, indent=4, ensure_ascii=False)
#         print("Arquivo json pronto.")
# except Exception as e:
#     print(f"Erro: {e}")

#Escrevendo CSV
# import csv
# protagonista = [["nome", "idade", "Profissão"],
#                 ["naruto", 33, "Ninja"],
#                 ["Hengoku", 16, "Hashira"],
#                 ["Goku", 40, "Artista Marcial"]]
# file_path = "output.csv"

# with open(file_path, "w", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     for row in protagonista:
#         writer.writerow(row)
#     print("Arquivo csv pronto.")

# Lendo arquivos txt:
# Sem o with
# file = open("testes/output.txt", "r")
# print(file.read())
# file.close()  # precisa fechar manualmente


# Com with
# file_path ="testes/output.txt"

# with open(file_path, "r") as file:
#     # content = file.read()
#     print(file.read())

#Lendo json
# import json
# file_path = "testes/output.json"

# with open(file_path, "r") as file:
#     content = json.load(file) #salvar em variavel é melhor para poder pegar apenas via key depois
#     print(content["Nome"])

#Lendo CSV
#  
