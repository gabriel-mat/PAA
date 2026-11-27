"""
Gabriel Mateus Souza - RA 832254
Letícia Ramos Fernandes - RA 834748
Otávio Inácio de Oliveira - RA 831718
"""

import sys


class Edificio:
    def __init__(self, e, h, d):
        self.e, self.h, self.d = e, h, d


class Silhueta:
    def __init__(self):
        self.pares = []

    def add(self, par):
        self.pares.append(par)

    def qtd(self):
        return len(self.pares)


def cmpReta(s1, s2, i, j):
    if i >= s1.qtd():
        return 1

    if j >= s2.qtd():
        return -1

    if s1.pares[i][0] == s2.pares[j][0]:
        if s1.pares[i][1] == s2.pares[j][1]:
            return 0

        if s1.pares[i][1] > s2.pares[j][1]:
            return -1

        return 1

    if s1.pares[i][0] < s2.pares[j][0]:
        return -1

    return 1


def skyline(edificios: list[Edificio]) -> Silhueta:
    # Recebe uma lista de Edifícios (com a tripla e,h,d)
    # e devolve a lista de pares da silhueta, usando Divisão e Conquista

    # Casos bases:
    #   nenhum edifício -> retorna um objeto Silhueta vazio
    #   um edifício -> chama a função que adiciona os 2 pares (e, h),(d, 0) à Silhueta

    if len(edificios) == 0:
        return Silhueta()

    if len(edificios) == 1:
        return silhuetaEdificio(edificios[0])

    # Divisão: particiona os edifícios em dois subconjuntos
    mid = len(edificios) // 2  # divisão inteira por 2

    # divide a lista em duas partes
    esq = edificios[:mid]  # do início até mid-1
    dir = edificios[mid:]  # de mid até o final

    # Conquista: determina recursivamente o skyline de cada subconjunto
    le = skyline(esq)
    ld = skyline(dir)

    # Combinação: une as duas silhuetas
    return unirSilhuetas(le, ld)


def unirSilhuetas(s1: Silhueta, s2: Silhueta) -> Silhueta:
    # Recebe duas silhuetas e devolve sua união,
    # considerando, em cada posição, a maior das alturas dos dois contornos

    i = j = 0
    s3 = Silhueta()
    hs1 = hs2 = 0
    ultimo = [-1, -1]
    atual = [-1, -1]

    while True:
        if i >= s1.qtd() and j >= s2.qtd():
            break

        if(j >= s2.qtd() or (i < s1.qtd() and s1.pares[i][0] < s2.pares[j][0])):
            atual[0] = s1.pares[i][0]
            hs1 = s1.pares[i][1]
            i += 1
        elif(i >= s1.qtd() or s1.pares[i][0] > s2.pares[j][0]):
            atual[0] = s2.pares[    ][0]
            hs2 = s2.pares[j][1]
            j += 1
        else:
            atual[0] = s1.pares[i][0]
            hs1 = s1.pares[i][1]
            hs2 = s2.pares[j][1]
            i += 1
            j += 1

        atual[1] = max(hs1, hs2)

        
        s3.add(atual.copy())
        ultimo = atual.copy

    return s3


def silhuetaEdificio(ed: Edificio) -> Silhueta:
    # Devolve a silhueta de um único edifício -> [(e, h),(d, 0)]

    s = Silhueta()
    s.add((ed.e, ed.h))
    s.add((ed.d, 0))

    return s


def gerarSVG(silhueta: list, arquivo_imagem: str):
    largura_canvas = 800
    altura_canvas = 450

    margem_esquerda = 60
    margem_direita = 40
    margem_superior = 40
    margem_inferior = 65

    y_base = altura_canvas - margem_inferior
    x_origem = margem_esquerda

    conteudo_svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{largura_canvas}" height="{altura_canvas}">',
        '<rect width="100%" height="100%" fill="white" />',
        '<defs><marker id="seta" markerWidth="8" markerHeight="8" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="black"/></marker></defs>',
    ]

    if len(silhueta) > 0:
        x_max = silhueta[-1][0]
        h_max = max(h for x, h in silhueta)

        # mesma escala para os dois eixos
        escala = min(
            (largura_canvas - margem_esquerda - margem_direita - 15) / x_max,
            (altura_canvas - margem_superior - margem_inferior) / h_max
        )

        # constrói os pontos do polígono
        pontos = [(x_origem + silhueta[0][0] * escala, y_base)]

        for i, (x, h) in enumerate(silhueta):
            x_svg = x_origem + x * escala
            y_svg = y_base - h * escala

            if i > 0:
                h_anterior = silhueta[i - 1][1]
                pontos.append((x_svg, y_base - h_anterior * escala))

            pontos.append((x_svg, y_svg))

        pontos_svg = " ".join(f"{x},{y}" for x, y in pontos)

        conteudo_svg.extend([
            f'<polygon points="{pontos_svg}" fill="peachpuff" stroke="none" />',
            f'<polyline points="{pontos_svg}" fill="none" stroke="black" stroke-width="2" />',
        ])

        # marcações e números do eixo X
        for x, h in silhueta:
            x_svg = x_origem + x * escala

            conteudo_svg.extend([
                f'<line x1="{x_svg}" y1="{y_base}" x2="{x_svg}" y2="{y_base + 5}" stroke="black" />',
                f'<text x="{x_svg}" y="{y_base + 22}" font-size="13" text-anchor="middle">{x}</text>',
            ])

        # marcações e números do eixo h
        alturas = sorted(set([0] + [h for x, h in silhueta]))

        for h in alturas:
            y_svg = y_base - h * escala

            conteudo_svg.extend([
                f'<line x1="{x_origem - 5}" y1="{y_svg}" x2="{x_origem}" y2="{y_svg}" stroke="black" />',
                f'<text x="{x_origem - 10}" y="{y_svg + 4}" font-size="13" text-anchor="end">{h}</text>',
            ])

    # desenha os eixos
    conteudo_svg.extend([
        f'<line x1="{x_origem}" y1="{y_base}" x2="{largura_canvas - margem_direita}" y2="{y_base}" stroke="black" stroke-width="1" marker-end="url(#seta)" />',
        f'<line x1="{x_origem}" y1="{y_base}" x2="{x_origem}" y2="{margem_superior}" stroke="black" stroke-width="1" marker-end="url(#seta)" />',
        f'<text x="{largura_canvas - margem_direita + 8}" y="{y_base + 5}" font-size="16" font-style="italic">x</text>',
        f'<text x="{x_origem - 5}" y="{margem_superior - 12}" font-size="16" font-style="italic">h</text>',
        '</svg>',
    ])

    with open(arquivo_imagem, "w", encoding="utf-8") as f:
        f.write("\n".join(conteudo_svg))


def ler_entrada(nome_arquivo: str) -> tuple[list[Edificio], int]:
    # 1ª linha: número n ≥ 0 de edifícios
    # cada uma das n linhas seguintes contém 3 inteiros separados por espaços, na ordem e h d

    edificios = []

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        n = int(f.readline())

        for linha in f:
            e, h, d = map(
                int, linha.split()
            )  # map converte cada número de texto para inteiro
            ed = Edificio(e, h, d)
            edificios.append(ed)

    return edificios, n


def escrever_saida(silhueta: Silhueta, nome_arquivo: str) -> None:
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(str(silhueta.qtd()) + "\n")

        for x, h in silhueta.pares:
            f.write(f"{x} {h}\n")


if __name__ == "__main__":
    """
    python skyline.py entrada.txt saida.txt
    python skyline.py entrada.txt saida.txt imagem.svg
    """

    if len(sys.argv) < 3:
        print(
            "O comando deve ser no formato 'python skyline.py <entrada.txt> <saida.txt>'"
        )
        exit(0)

    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]
    arquivo_imagem = sys.argv[3] if len(sys.argv) == 4 else None

    edificios, n = ler_entrada(arquivo_entrada)

    silhueta = skyline(edificios)

    #saída hard coded para testar
    #silhueta = Silhueta()

    #silhueta.add((2, 5))
    #silhueta.add((4, 8))
    #silhueta.add((10, 0))
    
    escrever_saida(silhueta, arquivo_saida)

    if arquivo_imagem is not None:
        gerarSVG(silhueta.pares, arquivo_imagem)
        print(f"SVG salvo em '{arquivo_imagem}'.")
