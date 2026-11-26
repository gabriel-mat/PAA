from skyline import skyline, Edificio


testes = [
    # 0. Exemplo fornecido
    {
        "nome": "Teste 0 - Exemplo",
        "entrada": "testes/entrada.txt",
        "saida_esperada": "testes/saida_esperada.txt"
    },
    # 1. Entrada vazia
    {
        "nome": "Teste 1 - Entrada vazia",
        "entrada": "testes/entrada1.txt",
        "saida_esperada": "testes/saida_esperada1.txt"
    },
    # 2. Um unico edificio
    {
        "nome": "Teste 2 - Um unico edificio",
        "entrada": "testes/entrada2.txt",
        "saida_esperada": "testes/saida_esperada2.txt"
    },
    # 3. Edificios separados
    {
        "nome": "Teste 3 - Edificios separados",
        "entrada": "testes/entrada3.txt",
        "saida_esperada": "testes/saida_esperada3.txt"
    },
    # 4. Sobreposicao parcial
    {
        "nome": "Teste 4 - Sobreposicao parcial",
        "entrada": "testes/entrada4.txt",
        "saida_esperada": "testes/saida_esperada4.txt"
    },
    # 5. Edificio contido em outro
    {
        "nome": "Teste 5 - Edificio contido em outro",
        "entrada": "testes/entrada5.txt",
        "saida_esperada": "testes/saida_esperada5.txt"
    },
    # 6. Mesma altura
    {
        "nome": "Teste 6 - Mesma altura",
        "entrada": "testes/entrada6.txt",
        "saida_esperada": "testes/saida_esperada6.txt"
    },
    # 7. Mesmo inicio ou mesmo fim
    {
        "nome": "Teste 7 - Mesmo inicio ou mesmo fim",
        "entrada": "testes/entrada7.txt",
        "saida_esperada": "testes/saida_esperada7.txt"
    },
    # 8. Comeca onde outro termina
    {
        "nome": "Teste 8 - Comeca onde outro termina",
        "entrada": "testes/entrada8.txt",
        "saida_esperada": "testes/saida_esperada8.txt"
    },
    # 9. Edificios repetidos
    {
        "nome": "Teste 9 - Edificios repetidos",
        "entrada": "testes/entrada9.txt",
        "saida_esperada": "testes/saida_esperada9.txt"
    },
    # 10. Ordem embaralhada
    {
        "nome": "Teste 10 - Ordem embaralhada",
        "entrada": "testes/entrada10.txt",
        "saida_esperada": "testes/saida_esperada10.txt"
    },
    # 11. Ordem decrescente
    {
        "nome": "Teste 11 - Ordem decrescente",
        "entrada": "testes/entrada11.txt",
        "saida_esperada": "testes/saida_esperada11.txt"
    },
]

def ler_edificios(arquivo):
    edificios = []

    with open(arquivo, 'r') as f:
        n = int(f.readline())

        for linha in f:
            e, h, d = map(int, linha.split())
            edificios.append(Edificio(e, h, d))

    return edificios

def ler_saida(arquivo):
    pares = []

    with open(arquivo, 'r') as f:
        k = int(f.readline())

        for linha in f:
            x, h = map(int, linha.split())
            pares.append((x, h))

    return pares

for teste in testes:
    edificios = ler_edificios(teste["entrada"])
    esperado = ler_saida(teste["saida_esperada"])

    resultado = skyline(edificios)

    if resultado.pares == esperado:
        print(f'{teste["nome"]}: OK')
    else:
        print(f'{teste["nome"]}: FALHOU')
        print("Esperado:", esperado)
        print("Obtido:  ", resultado.pares)