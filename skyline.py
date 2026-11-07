class Edificio:
    def __init__(self, e, h, d):
        self.e, self.h, self.d = e, h, d

class Silhueta:
    def __init__(self):
        self.pares = []

    def add(self, a, b):
        self.pares.append((a, b))

    def qtd(self):
        return len(pares)


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
        return NULL

    if len(edificios) == 1:
        return silhuetaEdificio(edificios[0])

    mid = len(edificios // 2)

    esq = edificios[ : mid]
    dir = edificios[mid + 1 : ]

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
    else if cmp == 1:
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
        else if j < s2.qtd():
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

def merge_sort(arr):
    if len(arr) < 2:
        return
    
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]
    
    merge_sort(left_arr)
    merge_sort(right_arr)
    
    i = j = k = 0
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
        
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

if __name__ == '__main__':
    ed = Edificio(1, 2, 3)
    s1 = silhuetaEdificio(ed)

        print(i[0], i[1])
        print(i[0], i[1])
