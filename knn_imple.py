vp = 0
vn = 0
fp = 0
fn = 0
flor = "Iris-versicolor"
neg = "Não é Iris-versicolor"


class rosinha:
    def __init__(self, tam_sepala_h, tam_sepala_w, tam_petala_h, tam_petala_w, classe, distancia):

        self.tam_sepala_h = tam_sepala_h
        self.tam_sepala_w = tam_sepala_w
        self.tam_petala_h = tam_petala_h
        self.tam_petala_w = tam_petala_w
        self.classe = classe
        self.distancia = distancia 


lis_treinamento = []
arquivo = open('treinamento.txt', 'r')
lista = arquivo.readlines()
arquivo.close()
for item in lista:
    par = item.split(',')
    ex = rosinha(float(par[0]), float(par[1]), float(par[2]), float(par[3]), par[4], 0)
    lis_treinamento.append(ex)


def atualiza_dist(ex):
    global lis_treinamento
    for x in lis_treinamento:
        dist = (x.tam_petala_h-ex.tam_petala_h)**2
        dist = dist+(x.tam_petala_w-ex.tam_petala_w)**2
        dist = dist+(x.tam_sepala_w-ex.tam_sepala_w)**2
        dist = dist+(x.tam_sepala_h-ex.tam_sepala_h)**2
        x.distancia = dist ** 0.5


def atualiza_classe(lista):
    global flor
    global neg
    copia = []
    for i in range(9):
        copia.append(lista[i].classe.replace('\n', ''))   
    q1 = copia.count(flor)
    q2 = 9-q1
    if(q1 > q2):
        return (flor)
    else:
        return(neg)
    

arquivo_classificador = open('classificar.txt', 'r')
lista_classificar = arquivo_classificador.readlines()
arquivo_classificador.close()
lista_classificadas = []
for item in lista_classificar:
    par = item.split(',')
    ex = rosinha(float(par[0]), float(par[1]), float(par[2]), float(par[3]), 'desconhecido', 0)
    atualiza_dist(ex)
    lis_treinamento.sort(key=lambda s: s.distancia)
    ex.classe = atualiza_classe(lis_treinamento)
    lista_classificadas.append(ex)


def calculos(lista_classificadas):
    lis_classificados = []
    global vp, vn, fp, fn, flor, neg
    arquivo_ver = open('iris.txt', 'r')
    lis_classificados = arquivo_ver.readlines()
    arquivo_ver.close()
    comparacao = []
    for item in lis_classificados:
        par = item.split(',')
        comparacao.append(par[4].replace('\n', ''))
    for i in range(75):
        if((lista_classificadas[i].classe == flor)and(comparacao[i] == flor)):
            vp = vp+1
        elif((lista_classificadas[i].classe == neg)and(comparacao[i] == flor)):
            fn = fn + 1
        elif((lista_classificadas[i].classe == neg)and(comparacao[i] != flor)):
            vn = vn+1
        elif((lista_classificadas[i].classe == flor)and(comparacao[i] != flor)):
            fp = fp+1


'''calculos(lista_classificadas)
print('Verificacao')
print(vp)
print(fp)
print(vn)
print(fn)
print('Taxa véa:')
print((vp+vn)/75 * 100)
print('Sensibilidade:')
print(vp/(vp+fn) * 100)
print('Especificidade')
print(vn/(vn+fp) * 100)
for i in lista_classificadas:
    print(i.classe)'''
'A parte comentada em cima se refere a todo o arquivo teste, olhando todas as linhas. Já o sem comentario, abaixo, você coloca só uma rosa para teste'
ex = rosinha(5.8, 2.7, 5.1, 1.9, 'desconhecido', 0)
atualiza_dist(ex)
lis_treinamento.sort(key=lambda s: s.distancia)
ex.classe = atualiza_classe(lis_treinamento)
print(ex.classe)