##  Medidas de Dispersão e Tendências
##  1º) Este programa em python recebe um variável do tipo "numpy" e realiza a conversão da mesma para o tipo "array".
##  2º) Importa a biblioteca "Pandas" e realiza os seguintes cálculos:
##      media, desvioPadrao, desvioAbsoluto, mediana, quantil, moda, minimo, maximo, amplitude, variancia, tabAux , dadosNump
##
def medidasDispersaotendencia (serieOriginal):
    #print ("tam serie=", len(serieOriginal))
    import pandas as pd
    serieConvertArray = []
    #print("serieOriginal=", serieOriginal)
    for item in serieOriginal:
        serieConvertArray.append(float(item))

    serie          = pd.Series(serieConvertArray)
    media          = serie.mean()
    mediana        = serie.median()
    quantil        = serie.quantile()
    moda           = serie.mode()
    minimo         = serie.min()
    maximo         = serie.max()
    amplitude      = maximo - minimo
    variancia      = serie.var()
    desvioPadrao   = serie.std()
    desvioAbsoluto = serie.mad()



    from numpy import array
    serieNump = array(serieConvertArray)

   # print("metricas", media, desvioPadrao, desvioAbsoluto, mediana, quantil) #, moda, minimo, maximo, amplitude, variancia)
   # print("min", minimo, "max", maximo, "ampli", amplitude, "var",variancia)
    #exit()
    return media, desvioPadrao, desvioAbsoluto, mediana, quantil, minimo, maximo, amplitude, variancia, serieConvertArray , serieNump , moda


#   Medias de Tendência
#   ===================
# Média   : medida de tendência central que indica o valor onde estão concentrados os dados de um conjunto de valores;
# Mediana : valor que separa a metade superior da metade inferior de uma distribuição de dados, ou o valor no centro da distribuição. Caso o número de observações na distribuição é ímpar, ele é o valor central, e se o número de observações é par, ele será a média das duas observações mais centrais.
# Quantil : é uma generalização da mediana, valor abaixo do qual está um certo percentual dos dados. No caso da mediana, esse percentual é de 50%
# Moda    : é que o valor que mais se repete dentro de um conjunto.

#   Medidas de Dispersão
#   ====================
# Amplitude       : é a diferença entre o maior e o menor valor de um conjunto de dados.
# Variância       : é uma medida que expressa quanto os dados de um conjunto estão afastados de seu valor esperado.
# Desvio Padrão   : é uma medida de dispersão, que indica quanto os dados estão afastados da média. Um valor de desvio padrão alto indica que os valores estão mais espalhados, mais longe da média, e um desvio padrão baixo indica que os valores estão mais próximos da média.
# Desvio Absoluto : primeiro, encontramos a média dos valores; depois, calculamos a distância de cada ponto desta média; somamos as distâncias e dividimos o resultado pela média destas distâncias.

    # Fonte: http://felipegalvao.com.br/blog/2016/03/31/estatistica-descritiva-com-python/


def MD(serieReal, seriePrevista):
    from sklearn import metrics
    acuracia = metrics.accuracy_score (serieReal,seriePrevista) * 100
    f1scores = metrics.f1_score       (serieReal,seriePrevista) * 100
    recalls  = metrics.recall_score   (serieReal,seriePrevista) * 100
    precision= metrics.precision_score(serieReal,seriePrevista) * 100

    return precision, acuracia, f1scores, recalls

# Medidas de Desempenho (Gravando)
def MDgravar(TesteY, predicao , algoritmo , saida2):
    from sklearn import metrics
    acuracia = metrics.accuracy_score(TesteY,predicao)
    f1scores = metrics.f1_score(TesteY,predicao)
    recalls  = metrics.recall_score(TesteY,predicao)
    precision= metrics.precision_score(TesteY,predicao)

    acuracia = round(float(acuracia),2)
    f1scores = round(float(f1scores),2)
    recalls  = round(float(recalls),2)

    #print("saida 2 =", saida2)
    #exit()
    saida2.write(str(algoritmo) + ";" + str(acuracia) + ";"  + str(f1scores) + ";"  + str(recalls) + ";"  + str(precision)+ "\n")
    return


def calculado(serieRealA, seriePrevistaA):
    qtdePositivo=0
    qtdeNegativo=0
    truePositivo=0
    falsePositivo=0
    trueNegativo=0
    falseNegativo=0

    precisao=0
    acuracia=0
    f1score =0
    recall  =0
    specificity =0

    serieReal = []
    seriePrevista = []

    for item in serieRealA:  #==>> Convertendo numpy array to List
        serieReal.append(int(item))

    for item in seriePrevistaA:
        seriePrevista.append(int(item))

    i=0
    while i< len(serieReal):
        if seriePrevista[i]==0:
            qtdeNegativo+=1
            if seriePrevista[i]==serieReal[i]:
                trueNegativo+=1
            else:
                falseNegativo+=1

        if seriePrevista[i]==1:
            qtdePositivo+=1
            if seriePrevista[i]==serieReal[i]:
                truePositivo+=1
            else:
                falsePositivo+=1

        i+=1

 #   print("qtdeTotal   :", len(serieReal))
  #  print("qtdeNegativo:", qtdeNegativo)
  #  print("qtdePositivo:", qtdePositivo)
   # print("qtde FN:", falseNegativo)
   # print("qtde TN:", trueNegativo)
   # print("qtde FP:", falsePositivo)
   # print("qtde TP:", truePositivo)

    if (truePositivo + trueNegativo) !=0:
        acuracia = (truePositivo + trueNegativo) / ( truePositivo + trueNegativo + falsePositivo + falseNegativo)

    if truePositivo !=0:
        precisao = truePositivo / (truePositivo + falsePositivo)

    if truePositivo !=0:
        recall   = truePositivo / (truePositivo + falseNegativo)


    if precisao !=0:
        f1score  = 2*precisao*recall / (precisao+recall)

    if trueNegativo !=0:
        specificity = trueNegativo / (trueNegativo + falsePositivo)

    return precisao*100, acuracia*100, f1score*100, recall*100, specificity*100


# Fonte: http://felipegalvao.com.br/blog/2016/03/31/estatistica-descritiva-com-python/
#
#  Medidas de Tendência Central
#
# As medidas de tendência central definem valores significativos, representativos e adequados para um conjunto de dados,
# dependendo do que se deseja analisar. São elas a média, mediana, quantis e a moda.
#
#
def medidastendencia(tab):
    import pandas as pd
    #tab =[22,23,21,28,10,30,38,16, 38]
    serie =  pd.Series(tab)

# Média
# A média é uma medida de tendência central que indica o valor onde estão concentrados os dados de um conjunto de valores,
# representando um valor significativo para o mesmo.
    media = serie.mean()

# Mediana e Quantil
# A mediana é o valor que separa a metade superior da metade inferior de uma distribuição de dados, ou o valor no centro da distribuição.
# Na prática, se o número de observações na distribuição é ímpar, ele é o valor central, e se o número de observações é par, ele será a
# média das duas observações mais centrais.
    mediana = serie.median()

# Já o quantil pode ser entendido como uma generalização da mediana. O quantil é o valor abaixo do qual está um certo percentual dos dados.
# No caso da mediana, esse percentual é de 50%
    quantil = serie.quantile()

# Moda
# A moda é simples. Nada mais é que o valor que mais se repete dentro de um conjunto.
    moda = serie.mode()


    print("media=", media)
    print("mediana=", mediana)
    print("quantil=", quantil)
    print("moda=", moda)
#25.11111111111111
    return media, mediana, quantil, moda