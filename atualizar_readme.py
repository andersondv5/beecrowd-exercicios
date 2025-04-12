# script para atualizar automaticamente a lista de exercícios no README do repositório à medida que crio novos arquivos.py

import os

# Caminhos importantes
pasta_exercicios = "python"
readme_path = "README.md"
inicio = "<!-- inicio-progresso -->"
fim = "<!-- fim-progresso -->"

# Total de exercícios a acompanhar
numero_inicial = 1000
numero_final = 1023

# Lê os arquivos existentes e extrai os números resolvidos
resolvidos = set()
for nome in os.listdir(pasta_exercicios):
    if nome.endswith(".py"):
        try:
            numero = int(nome.split(".")[0])
            resolvidos.add(numero)
        except ValueError:
            continue

# Divide os números em dois blocos para formar as colunas
metade = (numero_final - numero_inicial + 1) // 2 + 1
coluna1 = list(range(numero_inicial, numero_inicial + metade))
coluna2 = list(range(numero_inicial + metade, numero_final + 1))

# Gera as linhas da tabela
linhas = []
for i in range(max(len(coluna1), len(coluna2))):
    c1 = coluna1[i] if i < len(coluna1) else ""
    c2 = coluna2[i] if i < len(coluna2) else ""

    def gerar_link(n):
        if n == "":
            return ""
        if n in resolvidos:
            return f"[{n}](./{pasta_exercicios}/{n}.py)"
        else:
            return f"<span style='color:gray'>{n}</span>"

    linhas.append(f"| {gerar_link(c1)} | {gerar_link(c2)} |")

# Cabeçalho da tabela
cabecalho = "| Exercícios - Lista 1 | Exercícios - Lista 1 |\n|-------------|-------------|"
tabela = cabecalho + "\n" + "\n".join(linhas)

# Atualiza apenas a parte entre os marcadores no README
with open(readme_path, "r", encoding="utf-8") as f:
    conteudo = f.read()

novo_conteudo = (
    conteudo.split(inicio)[0]
    + inicio
    + "\n" + tabela + "\n"
    + fim
    + conteudo.split(fim)[1]
)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(novo_conteudo)

print("✅ README.md atualizado com sucesso!")


