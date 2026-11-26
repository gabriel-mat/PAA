# PAA

EP 1: Problema do Skyline

## TESTES

### Formato dos arquivos

Entrada:  primeira linha n (numero de edificios); depois n linhas
          "esquerda altura direita".
Saida:    primeira linha k (numero de pares); depois k linhas "x altura",
          com x estritamente crescente. O ultimo par tem altura 0.

### Arquivos

entrada.txt / saida.txt                   Exemplo do enunciado (7 edificios)
testes/entradaN.txt                       Entrada do teste N (N = 1..11)
testes/saida_esperadaN.txt                Saida esperada do teste N
testes.py                                 Executa todos os testes

### Casos cobertos

 0  Exemplo do enunciado
 1  Entrada vazia (n = 0)
 2  Um unico edificio
 3  Edificios separados (com espaco entre eles)
 4  Sobreposicao parcial
 5  Edificio inteiramente contido em outro
 6  Edificios de mesma altura (sobrepostos, a saida deve fundi-los)
 7  Mesma coordenada de inicio e mesma coordenada de fim
 8  Edificio comecando onde outro termina (alturas diferentes e iguais)
 9  Edificios repetidos
10  Entrada em ordem embaralhada
11  Entrada em ordem decrescente de coordenada esquerda

### Como executar

    python testes.py

O programa imprime "OK" ou "FALHOU" para cada teste e, em caso de falha,
mostra a saida esperada, a obtida e o problema encontrado. O codigo de
saida e 0 se tudo passou e 1 caso contrario.