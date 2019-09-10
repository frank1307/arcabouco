## Exemplo leitura EXCel

def f_graficoRetornoAcumulado(nomeAtivo, dataInicio, qtdeDiasTreino):

    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.read_csv("arqTotais/" + nomeAtivo + " N3 D1 J2 log operacao.csv", sep=";")

    i = 0
    listaAltas = []
    listaBaixas = []

    #calculo do separação das altas e das baixas
    while i < len(df['lucroliquidoAcumuladoP']) :
        if float(df['lucroliquidoAcumuladoP'][i]) <= 0:
            listaBaixas.append(df['lucroliquidoAcumuladoP'][i])
        else:
            listaAltas.append(df['lucroliquidoAcumuladoP'][i])
        i+=1


    plt.grid(True)

    plt.plot(df['lucroliquidoAcumuladoP'], color="green" ,label="Retorno Líquido")
    plt.plot(df['lucrobrutoAcumuladoP'], color="blue", label="Retorno Bruto")
    plt.plot(df['custotransacaoAcumuladoP'], label="Custo Operacional", color="red")
    plt.legend(loc='upper left')

    plt.xlabel("Quantidade de dias")
    plt.ylabel("Acumulados em (%)")
    plt.title(nomeAtivo)  # + titulo)
    plt.savefig('img/' + str(nomeAtivo) + '_retornoAcumulado.png')  ####===>> gravandos a imagem dos graficos
    plt.close()
    return


def f_graficoPlotarSerie(nomeAtivo, dataInicio, qtdeDiasTreino, serie, nome, legenda):
   import matplotlib.pyplot as plt
   plt.ylabel(nome)
   plt.xlabel(u'Quantidade de Dias')
   plt.title(nomeAtivo)#+ titulo)

   tamanho = range(len(serie))

   plt.plot(serie, label=nome)
   if legenda == "s":
     plt.legend(loc='upper left')
   plt.savefig('img/' + dataInicio + "_" + nomeAtivo + "_D" + str(qtdeDiasTreino) + nome +'.png')  ####===>> gravandos a imagem dos graficos
   plt.close()

   return

def f_graficoPlotarSerieMaxMin(nomeAtivo, dataInicio, qtdeDiasTreino, serieMax, serieMin, nome, legenda):

   import matplotlib.pyplot as plt
   plt.ylabel(u'Preço em (R$)')
   plt.xlabel(u'Quantidade de Dias')
   plt.title(nomeAtivo)#+ titulo)

   tamanho = range(len(serieMax))

   plt.plot(serieMin, label="Preço Mínimo")
   plt.plot(serieMax, label="Preço Máximo")
   plt.legend(loc='upper left')
   plt.savefig('img/' + dataInicio + "_" + nomeAtivo + "_D" + str(qtdeDiasTreino) + nome +'.png')  ####===>> gravandos a imagem dos graficos
   plt.close()

   return

def f_graficoPlotarSerieT(nomeAtivo, dataInicio, qtdeDiasTreino, serie, volume, open, close, min, max, retornoMinMax, retornoOpenClose):
    import matplotlib.pyplot as plt
    # plt.ylabel(u'Preço de Fechamento (R$)')
    nome=""
    plt.ylabel(nome)
    plt.xlabel(u'Quantidade de Dias')
    plt.title(nomeAtivo)  # + titulo)

    tamanho = range(len(serie))

    plt.subplot(3, 1, 1)
    plt.plot(max, label="Max")
    plt.legend(loc='upper left')

    plt.subplot(3, 1, 2)
    plt.bar(tamanho, volume, width=0.5, color="purple", label="Volume")
    plt.legend(loc='upper left')

    plt.subplot(3, 1, 3)
    plt.plot(retornoMinMax, label="Retorno MinMax")
    plt.legend(loc='upper left')

    plt.savefig('img/' + dataInicio + "_" + nomeAtivo + "_D" + str(
        qtdeDiasTreino) + nome + 'jabb.png')  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

def f_graficoPlotarSerieTeste(nomeAtivo, dataInicio, qtdeDiasTreino, volume, open, close):
    import matplotlib.pyplot as plt

    nome = ""
    tamanho = range(len(volume))

    plt.ylabel("Preço de Fechamento")
    plt.xlabel(u'Quantidade de Dias')
    plt.grid(True)

    plt.title(nomeAtivo)  # + titulo)
    plt.subplot(2, 1, 1)
    plt.plot(close, label="Close Price")
    plt.subplot(2, 1, 2)
    plt.bar(tamanho, volume, width=0.5, color="purple", label="Volume" , align ="center")
    plt.savefig('img/' + dataInicio + "_" + nomeAtivo + "_D" + str(
        qtdeDiasTreino) + nome + 'jabbteste.png')  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

def f_graficoPlotarSerieOpenClose(nomeAtivo, dataInicio, qtdeDiasTreino, serieOpen, serieClose, nome, legenda):
   import matplotlib.pyplot as plt
   plt.ylabel(u'Preço em (R$)')
   plt.xlabel(u'Quantidade de Dias')
   plt.title(nomeAtivo)#+ titulo)
   plt.grid(True)
   plt.plot(serieOpen, label="Preço Abertura")
   plt.plot(serieClose, label="Preço Fechamento")
   plt.legend(loc='upper left')
   plt.savefig('img/' + nomeAtivo +  nome +'.png')  ####===>> gravandos a imagem dos graficos
   plt.close()
   return

def teste(serie):
    import matplotlib.pyplot as plt
    y_axis = serie
    x_axis = range(len(y_axis))
    width_n = 0.2
    bar_color = 'yellow'

    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    return

def f_graficoPlotarSerieBarra(nomeAtivo, dataInicio, qtdeDiasTreino, serie, nome, legenda):
   import matplotlib.pyplot as plt
   plt.ylabel(nome)
   plt.xlabel(u'Quantidade de Dias')
   plt.title(nomeAtivo)#+ titulo)
   tamanho = range(len(serie))
   plt.bar(tamanho, serie, width=0.4, color="purple")
   plt.grid(True)

   if legenda == "s":
     plt.legend(loc='upper left')
   plt.savefig('img/' + nomeAtivo + nome +'.png')  ####===>> gravandos a imagem dos graficos
   plt.close()
   return


### Exemplo leitura TXT
def leituraTXT ():
    import matplotlib.pyplot as plt
    x = []
    y = []
    dataset = open('arqInicial/evo.txt', 'r')

    for line in dataset:
        line = line.strip()
        Y, X = line.split(',')
        x.append(X)
        y.append(Y)
    dataset.close()
    plt.plot(x,y)

    plt.title("Example")
    plt.xlabel("x label")
    plt.ylabel("y label")
    return

##==>> Gráficos dos Retornos ****
def f_graficoRetornos(nomeAtivo, serieRetornos, dataInicio):
    import matplotlib.pyplot as plt
    plt.ylabel(u'Retornos (%')
    plt.xlabel(u'Quantidade de Dias')
    plt.grid(True)

    plt.title(nomeAtivo)  # + titulo)
    tamanho = range(len(serieRetornos))
    plt.plot(serieRetornos, label="Retornos (%)")
    plt.legend(loc='upper left')
    plt.savefig('img/' + nomeAtivo + 'Retornos.png')  ####===>> gravando a imagem dos graficos
    return


def f_graficoBoxPlot():
    import matplotlib.pyplot as plt
    import pandas as pd

    retornos = [5.0, -3, 1.2, 2.5, -1.2, 10, 3, 1, 2]
    retornos2 = [10.0, -6, 2.4, 5, -2.4, 20, 6, 2, 4]

    #df = pd.read_csv("arqTotais/" + nomeAtivo + " N3 D1 J2 log operacao.csv", sep=";")
    BBAS3  = pd.read_csv("arqTotais/BBAS3 N3 D1 J2 log operacao.csv", sep=";")
    JBSS3 = pd.read_csv("arqTotais/JBSS3 N3 D1 J2 log operacao.csv", sep=";")
    KROT3 = pd.read_csv("arqTotais/KROT3 N3 D1 J2 log operacao.csv", sep=";")
    LAME4 = pd.read_csv("arqTotais/LAME4 N3 D1 J2 log operacao.csv", sep=";")
    MRVE3 = pd.read_csv("arqTotais/MRVE3 N3 D1 J2 log operacao.csv", sep=";")
    NATU3 = pd.read_csv("arqTotais/NATU3 N3 D1 J2 log operacao.csv", sep=";")
    PETR4 = pd.read_csv("arqTotais/PETR4 N3 D1 J2 log operacao.csv", sep=";")
    RADL3 = pd.read_csv("arqTotais/RADL3 N3 D1 J2 log operacao.csv", sep=";")
    TIMP3 = pd.read_csv("arqTotais/TIMP3 N3 D1 J2 log operacao.csv", sep=";")

    dados = [BBAS3['lucrobrutoP'], JBSS3['lucrobrutoP'], KROT3['lucrobrutoP'], LAME4['lucrobrutoP'], MRVE3['lucrobrutoP'], NATU3['lucrobrutoP'], PETR4['lucrobrutoP'], RADL3['lucrobrutoP'], TIMP3['lucrobrutoP']] #, MGLU3['lucrobrutoP'], BOVA11['lucrobrutoP']]
    #plt.boxplot(dados, labels=("BBAS3", "JBSS3", "KROT3", "LAME4", "MRVE3", "NATU3", "PETR4", "RADL3", "TIMP3", "MGLU3", "BOVA11"))
    plt.boxplot(dados, labels=("BBAS3", "JBSS3", "KROT3", "LAME4", "MRVE3", "NATU3", "PETR4", "RADL3", "TIMP3"))
    plt.title('Retorno Financeiro Bruto em Percentual (%)')
    plt.ylabel(u'Ganhos Financeiros (%)')
    plt.xticks(rotation=20)
    plt.grid(True)
    plt.savefig('img/' + "_BoxPlotRetornoFinanceiroGeral.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return


def f_graficoSerieClosePrice(nomeAtivo):
    import matplotlib.pyplot as plt
    import pandas as pd

    origem  = [pd.read_csv("arqTotais/"+nomeAtivo[i] + " N3 D1 J2 log operacao.csv", sep=";") for i in range(len(nomeAtivo))]

    for i in range(len(nomeAtivo)):
        plt.plot(origem[i]['closeprice'], label=nomeAtivo[i])

    plt.legend(loc='upper left')
    plt.grid(True)
    plt.savefig("img/ClosePriceGeral.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return


def f_graficoSerieClosePrice2(nomeAtivo, serie, data):
    import matplotlib.pyplot as plt
    plt.plot(data, serie, label=nomeAtivo)

    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()
    plt.savefig("img/ClosePriceGeral.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

def f_graficoBoxPlotEstrategias(dataInicio, nomeAtivo, lucroBrutoP,
    indComprarSemprePd,
    indAlvo2Pd,
    indAlvo05Pd,
    indAlvo1Pd,
    indAleatorioPd,
    indInversoPd):

    import matplotlib.pyplot as plt

    dados = [lucroBrutoP, indComprarSemprePd, indAlvo05Pd, indAlvo1Pd, indAlvo2Pd, indAleatorioPd, indInversoPd]
    plt.boxplot(dados, labels=("RBM+KNN", "CompraDiária", "Alvo 0,5%", "Alvo 1,0%", "Alvo 2,0%", "Aleatório", "Inverso"))
    plt.xticks(rotation=20)
    plt.grid(True)
    plt.title(nomeAtivo + ' - Retorno Financeiro das Estratégias (%)')
    plt.ylabel(u'Ganhos Financeiros (%)')
    plt.savefig('img/'+nomeAtivo + "_BoxPlotEstategias.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

def f_graficoBoxPlotEstrategiasTodosAtivos(lucroBrutoP, buyAndHoldPd,
    indComprarSemprePd,
    indInversoPd,
    indAleatorioPd,
    indAlvo05Pd,
    indAlvo1Pd,
    indAlvo2Pd):

    import matplotlib.pyplot as plt

    dados = [buyAndHoldPd, lucroBrutoP, indComprarSemprePd, indAlvo05Pd, indAlvo1Pd, indAlvo2Pd, indAleatorioPd, indInversoPd]
    plt.boxplot(dados, labels=("BuyAndHold", "RBM+KNN", "CompraDiária", "Alvo 0,5%", "Alvo 1,0%", "Alvo 2,0%", "Aleatório", "Inverso"))
    plt.xticks(rotation=20)
    plt.grid(True)
    plt.title('Retorno Financeiro das Estratégias (%) de todos os Ativos')
    plt.ylabel(u'Ganhos Financeiros (%)')
    plt.savefig('img/'+"TodosAtivos_BoxPlotEstategias.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return



def f_graficoBoxPlotMedidasDesempenho (precisao, acuracia, f1score, recall, especifidade):

    import matplotlib.pyplot as plt

    dados = [precisao, acuracia, f1score, recall, especifidade]
    plt.boxplot(dados, labels=("precisao", "acuracia", "f1score", "recall", "especifidade"))
    plt.xticks(rotation=20)
    plt.grid(True)
    plt.title('Medidas de Desempenho (%) de todos os Ativos')
    plt.ylabel(u'Percentual (%)')
    plt.savefig('img/'+"TodosAtivos_BoxPlotMedidasDesempenho.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return


def f_graficoBoxPlotEstrategia_Classif(SVM, NB, KNN, DT, RBM_SVM, RBM_NB, RBM_KNN, RBM_DT):
    import matplotlib.pyplot as plt

    dados = [SVM, NB, KNN, DT, RBM_SVM, RBM_NB, RBM_KNN, RBM_DT]
    #plt.boxplot(dados, labels=("SVM", "Naive Bayes(NB)", "KNN", "Decision Tree(DT)", "RBM+SVM", "RBM+NB", "RBM+KNN", "RBM+DT", "Oráculo"))
    plt.boxplot(dados, labels=("SVM", "NaiveBayes", "KNN", "DecisionTree", "RBM+SVM", "RBM+NB", "RBM+KNN", "RBM+DT"))

    plt.xticks(rotation=20)
    plt.grid(True)
    plt.title('30 Códigos de Ativos Avaliados Por Classificador')
    plt.ylabel(u'Retorno Financeiro Líquido em (%)')
    plt.savefig('img/'+"TodosAtivos_BoxPlotEstategiaRBM_Classif.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

def f_graficoBoxPlotPrecisaoClassif(SVM, NB, KNN, DT, RBM_SVM, RBM_NB, RBM_KNN, RBM_DT):
    import matplotlib.pyplot as plt

    dados = [SVM, NB, KNN, DT, RBM_SVM, RBM_NB, RBM_KNN, RBM_DT]
    #plt.boxplot(dados, labels=("SVM", "Naive Bayes(NB)", "KNN", "Decision Tree(DT)", "RBM+SVM", "RBM+NB", "RBM+KNN", "RBM+DT", "Oráculo"))
    plt.boxplot(dados, labels=("SVM", "NaiveBayes", "KNN", "DecisionTree", "RBM+SVM", "RBM+NB", "RBM+KNN", "RBM+DT"))

    plt.xticks(rotation=20)
    plt.grid(True)
    plt.title('30 Códigos de Ativos Avaliados Por Classificador')
    plt.ylabel(u'Precisão em (%)')
    plt.savefig('img/'+"TodosAtivos_BoxPlotPrecisaoClassifi.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

def f_graficoBoxPlotAcuraciaClassif(SVM, NB, KNN, DT, RBM_SVM, RBM_NB, RBM_KNN, RBM_DT):
    import matplotlib.pyplot as plt

    dados = [SVM, NB, KNN, DT, RBM_SVM, RBM_NB, RBM_KNN, RBM_DT]
    #plt.boxplot(dados, labels=("SVM", "Naive Bayes(NB)", "KNN", "Decision Tree(DT)", "RBM+SVM", "RBM+NB", "RBM+KNN", "RBM+DT", "Oráculo"))
    plt.boxplot(dados, labels=("SVM", "NaiveBayes", "KNN", "DecisionTree", "RBM+SVM", "RBM+NB", "RBM+KNN", "RBM+DT"))

    plt.xticks(rotation=20)
    plt.grid(True)
    plt.title('30 Códigos de Ativos Avaliados Por Classificador')
    plt.ylabel(u'Acurácia em (%)')
    plt.savefig('img/'+"TodosAtivos_BoxPlotAcuraciaClassifi.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

def f_graficoBoxPlotDrawdownClassif(SVM, NB, KNN, DT, RBM_SVM, RBM_NB, RBM_KNN, RBM_DT):
    import matplotlib.pyplot as plt
    dados = [SVM, NB, KNN, DT, RBM_SVM, RBM_NB, RBM_KNN, RBM_DT]
    plt.boxplot(dados, labels=("SVM", "NaiveBayes", "KNN", "DecisionTree", "RBM+SVM", "RBM+NB", "RBM+KNN", "RBM+DT"))
    plt.xticks(rotation=20)
    plt.grid(True)
    plt.title('30 Códigos de Ativos Avaliados Por Classificador')
    plt.ylabel(u'Acurácia em (%)')
    plt.savefig('img/'+"TodosAtivos_BoxPlotDrawndownClassifi.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return


def f_graficoBoxPlotPrecisaoConsolidados(tecnicasTradicionais, tecnicasCombinadas):
    import matplotlib.pyplot as plt
    dados = [tecnicasTradicionais, tecnicasCombinadas]
    plt.boxplot(dados, labels=("4 Técnicas Isoladas", "4 Técnicas Combinadas"))
#    plt.xticks(rotation=20)
    plt.grid(True)
    plt.title('30 Códigos de Ativos Avaliados Por Técnica de Classificação')
    plt.ylabel(u'Precisão em (%)')
    plt.savefig('img/'+"TodosAtivos_BoxPlotTipoTecnicaPrecisao.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

def f_graficoBoxPlotAcuraciaConsolidados(tecnicasTradicionais, tecnicasCombinadas):
    import matplotlib.pyplot as plt
    dados = [tecnicasTradicionais, tecnicasCombinadas]
    plt.boxplot(dados, labels=("4 Técnicas Isoladas", "4 Técnicas Combinadas"))
   # plt.xticks(rotation=20)
    plt.grid(True)
    plt.title('30 Códigos de Ativos Avaliados Por Técnica de Classificação')
    plt.ylabel(u'Acurácia em (%)')
    plt.savefig('img/'+"TodosAtivos_BoxPlotTipoTecnicaAcuracia.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

def f_graficoBoxPlotFinancConsolidados(tecnicasTradicionais, tecnicasCombinadas):
    import matplotlib.pyplot as plt
    dados = [tecnicasTradicionais, tecnicasCombinadas]
    plt.boxplot(dados, labels=("4 Técnicas Isoladas", "4 Técnicas Combinadas"))
    #plt.xticks(rotation=20)
    plt.grid(True)
    plt.title('30 Códigos de Ativos Avaliados Por Técnica de Classificação')
    plt.ylabel(u'Retorno Financeiro Líquido em (%)')
    plt.savefig('img/'+"TodosAtivos_BoxPlotTipoTecnicaFinanc.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

def f_graficoBoxPlotDrawdownConsolidados(tecnicasTradicionais, tecnicasCombinadas):
    import matplotlib.pyplot as plt
    dados = [tecnicasTradicionais, tecnicasCombinadas]
    plt.boxplot(dados, labels=("4 Técnicas Isoladas", "4 Técnicas Combinadas"))
    plt.grid(True)
    plt.title('30 Códigos de Ativos Avaliados Por Técnica de Classificação')
    plt.ylabel(u'DrawnDown em (%)')
    plt.savefig('img/'+"TodosAtivos_BoxPlotTipoTecnicaDrawndown.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

## ==>> Grafico de Linhas
def f_graficoDrawDown(dataInicio, nomeAtivo,retornoDrawArr):
    import matplotlib.pyplot as plt
    plt.ylabel(u'DrawDown (%)')
    plt.xlabel(u'Quantidade de Dias')
    plt.title(nomeAtivo)  # + titulo)
    plt.plot(retornoDrawArr)
    plt.savefig('img/' + nomeAtivo + "_drawdown2.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

## ==>> Grafico de Barras
def f_graficoDrawDown2(dataInicio, nomeAtivo,retornoDrawArr):
    import matplotlib.pyplot as plt
    plt.ylabel(u'DrawDown (%)')
    plt.xlabel(u'Quantidade de Dias')
    plt.title(nomeAtivo)  # + titulo)
    y_axis = retornoDrawArr
    x_axis = range(len(y_axis))
    width_n = 1
    bar_color = 'red'
    plt.grid(True)

    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.savefig('img/' + nomeAtivo + "_drawdown.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return

def f_graficoClosePrice(nomeAtivo, dataInicio, qtdeDiasTreino, serieClose):
    import matplotlib.pyplot as plt
    plt.ylabel(u'Preço de Fechamento em (R$)')
    plt.xlabel(u'Quantidade de Dias')
    plt.title(nomeAtivo)#+ titulo)
    plt.plot(serieClose, label="Preço Fechamento")
    plt.grid(True)

    plt.savefig('img/' + nomeAtivo + "_closePrice.png")  ####===>> gravandos a imagem dos graficos
    plt.close()
    return