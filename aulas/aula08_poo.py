from abc import ABC, abstractmethod

# --- AULA 08: PROGRAMAÇÃO ORIENTADA A OBJETOS ---

# 1. Classe Base e Herança
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome     # Atributo público
        self.idade = idade

    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")

class Trabalhador(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade) # Estende o construtor da classe pai
        self.profissao = profissao

    def falar_profissao(self):
        print(f"Minha profissão é: {self.profissao}")

print("--- Testando Herança ---")
funcionario = Trabalhador("Ana", 20, "Médica")
funcionario.apresentar()
funcionario.falar_profissao()

# 2. Encapsulamento (Protegendo dados sensíveis com __)
class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial # __ torna o atributo privado

    def mostrar_saldo(self):
        print(f"Saldo seguro consultado: R$ {self.__saldo}")

print("\n--- Testando Encapsulamento ---")
minha_conta = ContaBancaria(5000)
minha_conta.mostrar_saldo()
# print(minha_conta.__saldo) # ERRO! Não pode ser acessado de fora diretamente

# 3. Polimorfismo e Abstração
class Animal(ABC): # Classe Abstrata (Serve de molde obrigatório)
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self): # Polimorfismo: implementa de forma específica
        print("Au Au!")

class Gato(Animal):
    def fazer_som(self): # Polimorfismo: implementa de forma específica
        print("Miau!")

print("\n--- Testando Abstração e Polimorfismo ---")
dog = Cachorro()
cat = Gato()
dog.fazer_som()
cat.fazer_som()
