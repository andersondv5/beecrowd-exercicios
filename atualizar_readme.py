import os

# Caminhos importantes
pasta_exercicios = "Python"
readme_path = "README.md"
inicio = "<!-- inicio-progresso -->"
fim = "<!-- fim-progresso -->"

# Total de exercícios a acompanhar (ajuste se quiser mais ou menos)
numero_inicial = 1001
numero_final = 1010

# Lê os arquivos existentes e extrai os números resolvidos
resolvidos = set()

# Lê os arquivos da pasta e pega apenas os números válidos
for nome in os.listdir(pasta_exercicios):
    if nome.endswith(".py"):
        try:
            # Pega a parte antes do ponto para garantir que seja um número
            numero = int(nome.split(".")[0])
            resolvidos.add(numero)
        except ValueError:
            # Caso o arquivo não tenha o nome esperado (não seja um número), ignora
            continue

# Gera a lista de progresso com [x] ou [ ]
progresso = []
for numero in range(numero_inicial, numero_final + 1):
    check = "x" if numero in resolvidos else " "
    progresso.append(f"- [{check}] {numero}")

# Junta tudo num bloco de texto
progresso_texto = "\n".join(progresso)

# Lê o conteúdo atual do README
with open(readme_path, "r", encoding="utf-8") as f:
    conteudo = f.read()

# Atualiza apenas a parte entre os marcadores
novo_conteudo = (
    conteudo.split(inicio)[0]
    + inicio
    + "\n" + progresso_texto + "\n"
    + fim
    + conteudo.split(fim)[1]
)

# Escreve de volta no README.md
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(novo_conteudo)

print("✅ README.md atualizado com sucesso!")