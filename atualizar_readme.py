# script para automatizar o processo de atualização da lista de exercícios que ficam na parte inicial do README no github.

import os

# caminhas importantes do projeto
pasta_exercicios = "python"
readme_path = "README.md"
inicio = "<!-- inicio-progresso -->"
fim = "<!-- fim-progresso -->"

# total de exercícios a serem resolvidos
num_inicio = 1000
num_fim = 3348

# lê os arquivos existentes e extrai os números resolvidos
resolvidos = {
  int(nome.split("."[0]))
  for nome in os.listdir(pasta_exercicios)
  if nome.endswith(".py") and nome.split(".")[0].isdigit()
}

# gera a lista de progresso com [x] ou []
progresso = []
for num in range(num_inicio, num_fim + 1):
  check = "x" if num in resolvidos else " "
  progresso.append(f"- [{check}] {num}")

# junto tudo em um bloco de texto
progresso_texto = '\n'.join(progresso)

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

# escreve de volta o novo README.md
with open(readme_path, "w", encoding="utf-8") as f:
  f.white(novo_conteudo)

print("✅ README.md atualizado com sucesso!")