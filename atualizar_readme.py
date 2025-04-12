# script para atualizar automaticamente a lista de exercícios no README do repositório à medida que crio novos arquivos.py

import os
import re

CAMINHO_PASTA = "python"
CAMINHO_README = "README.md"

def gerar_link(numero):
    caminho_arquivo = os.path.join(CAMINHO_PASTA, f"{numero}.py")
    if os.path.isfile(caminho_arquivo):
        return f"[{numero}](./{CAMINHO_PASTA}/{numero}.py)"
    else:
        return f"`{numero}`"

def agrupar_blocos(inicio, fim):
    todos_links = [gerar_link(i) for i in range(inicio, fim + 1)]

    blocos = [todos_links[i:i+12] for i in range(0, len(todos_links), 12)]

    linhas = []
    for bloco in blocos:
        while len(bloco) < 12:
            bloco.append("`----`")
        linhas.append(bloco)

    resultado = []

    for i in range(0, len(linhas), 2):
        bloco1 = linhas[i]
        bloco2 = linhas[i+1] if i + 1 < len(linhas) else ["`----`"] * 12

        titulo_inicio = int(re.search(r"\d+", bloco1[0]).group()) if re.search(r"\d+", bloco1[0]) else "----"
        titulo_fim = int(re.search(r"\d+", bloco1[-1]).group()) if re.search(r"\d+", bloco1[-1]) else "----"
        titulo2_inicio = int(re.search(r"\d+", bloco2[0]).group()) if re.search(r"\d+", bloco2[0]) else "----"
        titulo2_fim = int(re.search(r"\d+", bloco2[-1]).group()) if re.search(r"\d+", bloco2[-1]) else "----"

        resultado.append(f"### Exercícios {titulo_inicio:04}-{titulo_fim:04} / {titulo2_inicio:04}-{titulo2_fim:04}")
        resultado.append(f"| {' | '.join(bloco1)} |  | {' | '.join(bloco2)} |")
        resultado.append("|" + "------------------------|" * 13)

    return "\n".join(resultado)

def atualizar_readme():
    with open(CAMINHO_README, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    padrao = r"(<!-- inicio-progresso -->)(.*?)(<!-- fim-progresso -->)"
    novo_conteudo = gerar_blocos_progresso()
    novo_texto = re.sub(padrao, rf"\1\n{novo_conteudo}\n\3", conteudo, flags=re.DOTALL)

    with open(CAMINHO_README, "w", encoding="utf-8") as arquivo:
        arquivo.write(novo_texto)

def gerar_blocos_progresso():
    return agrupar_blocos(1000, 1047)

if __name__ == "__main__":
    atualizar_readme()
    print("✅ README.md atualizado com sucesso!")
