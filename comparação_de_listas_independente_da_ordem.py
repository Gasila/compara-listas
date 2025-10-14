import os

def comparar_listas_de_texto(texto1, texto2):
    # Divide o texto em linhas e remove espaços extras
    lista1 = [linha.strip() for linha in texto1.strip().splitlines() if linha.strip()]
    lista2 = [linha.strip() for linha in texto2.strip().splitlines() if linha.strip()]
    
    # Transforma em conjuntos para comparar independentemente da ordem
    set1 = set(lista1)
    set2 = set(lista2)

    # Nomes repetidos
    repetidos = set1 & set2

    # Nomes exclusivos de cada lista
    unicos_lista1 = set1 - set2
    unicos_lista2 = set2 - set1

    return repetidos, unicos_lista1, unicos_lista2

# Cole aqui os textos com os nomes (um por linha)
texto1 = """

LISTA 1

"""

texto2 = """

LISTA 2

"""

# Chamar a função
repetidos, apenas_lista1, apenas_lista2 = comparar_listas_de_texto(texto1, texto2)

# Criar conteúdo para salvar no arquivo
conteudo = []

conteudo.append("✅ Nomes em comum:")
conteudo.extend(f"- {nome}" for nome in sorted(repetidos))

conteudo.append("\n❌ Nomes só na lista 1:")
conteudo.extend(f"- {nome}" for nome in sorted(apenas_lista1))

conteudo.append("\n❌ Nomes só na lista 2:")
conteudo.extend(f"- {nome}" for nome in sorted(apenas_lista2))

# Junta o conteúdo em uma única string
conteudo_final = "\n".join(conteudo)

# Define o caminho para a área de trabalho do usuário
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
caminho_arquivo = os.path.join(desktop, "comparacao_de_listas.txt")

# Escreve o arquivo
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_final)

print(f"📁 Resultado salvo com sucesso em: {caminho_arquivo}")