import os
import json
import csv

# --- AULA 10: MANIPULAÇÃO DE ARQUIVOS E PASTAS ---

# 1. Módulo OS: Interação com o Sistema Operacional e Caminhos
print("--- Testando Módulo OS ---")
file_path_relativo = "aulas/teste.txt"

# Verifica se o caminho existe
if os.path.exists(file_path_relativo):
    print(f"O caminho '{file_path_relativo}' existe!")
    if os.path.isfile(file_path_relativo):
        print("É um arquivo.")
    elif os.path.isdir(file_path_relativo):
        print("É uma pasta.")
else:
    print(f"O caminho '{file_path_relativo}' não existe.")

# Listar itens no diretório atual
print("\nArquivos na pasta atual:")
for item in os.listdir("."):
    print(f"- {item}")


# 2. Escrita e Leitura de Arquivo de Texto (TXT)
print("\n--- Escrevendo e Lendo TXT ---")
personagens = ["Naruto", "Ichigo", "Goku", "Edward"]
txt_path = "aulas/output_personagens.txt"

# Escrevendo (Modo 'w' cria ou sobrescreve, Modo 'a' adiciona ao final)
with open(txt_path, "w", encoding="utf-8") as file:
    for personagem in personagens:
        file.write(personagem + "\n")
print(f"Lista de personagens escrita em {txt_path}!")

# Lendo o arquivo TXT criado
with open(txt_path, "r", encoding="utf-8") as file:
    conteudo_txt = file.read()
    print("Conteúdo lido do arquivo TXT:")
    print(conteudo_txt)


# 3. Escrita e Leitura de JSON (Dicionários estruturados)
print("\n--- Escrevendo e Lendo JSON ---")
ninja = {
    "Nome": "Naruto Uzumaki",
    "idade": 33,
    "profissão": "Hokage"
}
json_path = "aulas/output_ninja.json"

# Escrevendo JSON
with open(json_path, "w", encoding="utf-8") as file:
    json.dump(ninja, file, indent=4, ensure_ascii=False)
print(f"Dados estruturados salvos em {json_path}!")

# Lendo JSON
with open(json_path, "r", encoding="utf-8") as file:
    dados_ninja = json.load(file)
    print(f"Chave 'Nome' lida do JSON: {dados_ninja['Nome']}")


# 4. Escrita e Leitura de CSV (Planilhas de Dados)
print("\n--- Escrevendo e Lendo CSV ---")
protagonistas = [
    ["nome", "idade", "Profissão"],
    ["Naruto", 33, "Ninja"],
    ["Rengoku", 16, "Hashira"],
    ["Goku", 40, "Artista Marcial"]
]
csv_path = "aulas/output_protagonistas.csv"

# Escrevendo CSV
with open(csv_path, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for row in protagonistas:
        writer.writerow(row)
print(f"Tabela de protagonistas salva em {csv_path}!")

# Lendo CSV
with open(csv_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("Dados lidos do CSV:")
    for row in reader:
        print(row)
