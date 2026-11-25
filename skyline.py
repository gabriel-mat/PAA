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

def cmpReta(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return 0

    if a[0] < b[0]:
        return -1

    if a[1] > b[1]:
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
    mid = len(edificios) // 2 # divisão inteira por 2 

    # divide a lista em duas partes 
    esq = edificios[:mid] # do início até mid-1
    dir = edificios[mid:] # de mid até o final

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


def silhuetaEdificio(ed: Edificio) -> Silhueta: 
    # Devolve a silhueta de um único edifício -> [(e, h),(d, 0)]

    s = Silhueta()
    s.add((ed.e, ed.h))
    s.add((ed.d, 0))

    return s

def gerarSVG(silhueta: list, arquivo_imagem: str):
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
        conteudo_svg.extend([
                f'<polygon points="{pontos_svg}" fill="peachpuff" stroke="none" />',
                f'<polyline points="{pontos_svg}" fill="none" stroke="black" stroke-width="3" />',
        ])

    conteudo_svg.extend(
        [
            f'<line x1="{x1_base}" y1="{y_base}" x2="{x2_base}" y2="{y_base}" stroke="black" stroke-width="1" />',
            "</svg>",
        ]
    )

    with open(arquivo_imagem, "w", encoding="utf-8") as f:
        f.write("\n".join(conteudo_svg))

def ler_entrada(nome_arquivo: str) -> tuple[list[Edificio], int]:
    # 1ª linha: número n ≥ 0 de edifícios
    # cada uma das n linhas seguintes contém 3 inteiros separados por espaços, na ordem e h d

    edificios = []

    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        n = int(f.readline())
        
        for linha in f:
            e, h, d = map(int, linha.split()) # map converte cada número de texto para inteiro
            ed = Edificio(e, h, d)
            edificios.append(ed)

    return edificios, n

def escrever_saida(silhueta: Silhueta, nome_arquivo: str) -> None:
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(str(silhueta.qtd()) + '\n')

        for x, h in silhueta.pares:
            f.write(f'{x} {h}\n')

if __name__ == "__main__":
    """
    python skyline.py entrada.txt saida.txt
    python skyline.py entrada.txt saida.txt imagem.svg
    """

    if (len(sys.argv) < 3): 
        print("O comando deve ser no formato 'python skyline.py <entrada.txt> <saida.txt>'")
        exit(0)
        
    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]
    arquivo_imagem = sys.argv[3] if len(sys.argv) == 4 else None

    edificios, n = ler_entrada(arquivo_entrada)

    silhueta = skyline(edificios)

    escrever_saida(silhueta, arquivo_saida)

    if arquivo_imagem is not None:
        gerarSVG(silhueta.pares, arquivo_imagem)
        print(f"SVG salvo em '{arquivo_imagem}'.")