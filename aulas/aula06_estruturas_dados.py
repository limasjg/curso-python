# --- AULA 06: ESTRUTURAS DE DADOS ---

# 1. LISTAS [ ]: Ordenada, mutável e permite itens repetidos
lista_num = [1, 2, 3]
lista_num.append(3) # Permite duplicar
print(f"Lista: {lista_num}")

# 2. TUPLAS ( ): Ordenada, IMUTÁVEL (não altera após criada) e permite repetição
veiculos = ("carro", "moto", "van", "carro")
print(f"Tupla original: {veiculos}")
print(f"Primeiro elemento da Tupla: {veiculos[0]}")
# veiculos.append("avião") # ERRO! Tuplas não podem ser alteradas.

# 3. SETS { }: Não ordenada, mutável, mas NÃO permite elementos duplicados
eletronicos = {"TV", "Notebook", "Celular"}
eletronicos.add("Relógio")
eletronicos.add("TV") # Tentando duplicar TV (será ignorado)
print(f"Set (sem duplicados): {eletronicos}")

# 4. DICIONÁRIOS {chave: valor}: Estrutura de dados mapeada (Chave única)
pessoa = {"nome": "João", "idade": 25, "vivo": True}
pessoa.update({"cidade": "Curitiba"}) # Adicionando nova chave
print(f"Dicionário completo: {pessoa}")
print(f"Acessando chave 'nome': {pessoa['nome']}")
