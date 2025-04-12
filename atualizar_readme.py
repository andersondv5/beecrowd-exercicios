# script para atualizar automaticamente a lista de exercícios no README do repositório à medida que crio novos arquivos.py

import os

# caminhos importantes
pasta_exercicios = "Python"
readme_path = "README.md"
inicio = "<!-- inicio-progresso -->"
fim = "<!-- fim-progresso -->"

# total de exercícios a acompanhar
numero_inicial = 1000
numero_final = 1010

# lê os arquivos existentes e extrai os números resolvidos
resolvidos = set()

# lê os arquivos da pasta e pega apenas os números válidos
for nome in os.listdir(pasta_exercicios):
    if nome.endswith(".py"):
        try:
            numero = int(nome.split(".")[0])
            resolvidos.add(numero)
        except ValueError:
            continue

# gera a lista de progresso com [x] ou [ ]
progresso = []
for numero in range(numero_inicial, numero_final + 1):
    check = "x" if numero in resolvidos else " "
    progresso.append(f"- [{check}] {numero}")

# junta tudo num bloco de texto
progresso_texto = "\n".join(progresso)

# lê o conteúdo atual do README
with open(readme_path, "r", encoding="utf-8") as f:
    conteudo = f.read()

# atualiza apenas a parte entre os marcadores
novo_conteudo = (
    conteudo.split(inicio)[0]
    + inicio
    + "\n" + progresso_texto + "\n"
    + fim
    + conteudo.split(fim)[1]
)

# escreve de volta no README.md
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(novo_conteudo)

print("✅ README.md atualizado com sucesso!")
