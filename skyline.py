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

    def add(self, a):
        self.pares.append(a)

    def qtd(self):
        return len(self.pares)


def cmpReta(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return 0

    if a[0] < b[0]:
        return -1

    if a[1] > b[1]:
        return -1

    return 1


# skyline(edificios): recebe uma lista de triplas e devolve a lista de pares da silhueta, usando Divisão e Conquista.
def skyline(edificios):
    if len(edificios) == 0:
        return None

    if len(edificios) == 1:
        return silhuetaEdificio(edificios[0])

    mid = len(edificios // 2)

    esq = edificios[:mid]
    dir = edificios[mid + 1 :]

    le = skyline(esq)
    ld = skyline(dir)

    return unirSilhuetas(le, ld)


# unirSilhuetas(s1, s2): recebe duas silhuetas e devolve sua união.
def unirSilhuetas(s1, s2):
    i = j = 0
    s3 = Silhueta()

    cmp = cmpReta(s1.pares[0], s2.pares[0])

    if cmp == -1:
        atual = s1.pares[0]
        i += 1
    elif cmp == 1:
        atual = s2.pares[0]
        j += 1
    else:
        atual = s1.pares[0]
        i += 1
        j += 1

    s3.add(atual)

    while 1:
        while i < s1.qtd() and (s1.pares[i][0] < atual[0] or s1.pares[i][1] < atual[1]):
            i += 1

        while j < s2.qtd() and (s2.pares[j][0] < atual[0] or s2.pares[j][1] < atual[1]):
            j += 1

        if j >= s2.qtd() or s1.pares[i][0] > s2.pares[j][0]:
            atual = s1.pares[i][0]
            i += 1
            s3.add(atual)
        elif j < s2.qtd():
            atual = s2.pares[j][0]
            j += 1
            s3.add(atual)

    return s3


# silhuetaEdificio(edificio): devolve a silhueta de um único edifício.


def silhuetaEdificio(ed):
    s = Silhueta()

    s.pares.append((ed.e, ed.h))
    s.pares.append((ed.d, 0))

    return s


def gerarSVG(silhueta, arquivo_imagem):
    # dimensão total da tela (canvas SVG)
    largura_canvas = 800
    altura_canvas = 450

    margem_borda = 50
    margem_inferior = 50

    # posição Y da linha de base (chão)
    y_base = altura_canvas - margem_inferior

    # linha de base centralizada
    x1_base = margem_borda
    x2_base = largura_canvas - margem_borda

    conteudo_svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{largura_canvas}" height="{altura_canvas}">',
        f'<rect width="100%" height="100%" fill="white" />',
    ]

    # constrói os pontos do polígono
    if len(silhueta) > 0:
        pontos = []
        pontos.insert(0, (silhueta[0][0], y_base))

        for i, ponto in enumerate(silhueta):
            x = ponto[0]
            h = ponto[1]
            y = y_base - h

            if i > 0:
                h_anterior = silhueta[i - 1][1]  # altura do ponto anterior
                # adiciona a quina horizontal
                pontos.append((x, y_base - h_anterior))

            pontos.append((x, y))

        pontos_svg = " ".join(f"{x},{y}" for x, y in pontos)
        conteudo_svg.extend(
            [
                f'<polygon points="{pontos_svg}" fill="peachpuff" stroke="none" />',
                f'<polyline points="{pontos_svg}" fill="none" stroke="black" stroke-width="3" />',
            ]
        )

    conteudo_svg.extend(
        [
            f'<line x1="{x1_base}" y1="{y_base}" x2="{x2_base}" y2="{y_base}" stroke="black" stroke-width="1" />',
            "</svg>",
        ]
    )

    with open(arquivo_imagem, "w", encoding="utf-8") as f:
        f.write("\n".join(conteudo_svg))

    return f


if __name__ == "__main__":
    """
    python skyline.py entrada.txt saida.txt
    python skyline.py entrada.txt saida.txt imagem.svg
    """

    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]
    arquivo_imagem = sys.argv[3] if len(sys.argv) == 4 else None

    silhueta = [(100, 150), (200, 250), (300, 100), (400, 0)]

    if arquivo_imagem is not None:
        gerarSVG(silhueta, arquivo_imagem)

    print(f"SVG salvo em '{arquivo_imagem}'.")

