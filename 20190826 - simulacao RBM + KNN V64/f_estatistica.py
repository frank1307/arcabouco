#
#  Este programa realiza a estrategia de operação e grava a tabela de Totais e a tabela de ganho mensal.
# Funções:


import f_util

def calcularClasse (arquivo, classeProcurada):

    j=0
    qtdeClasse =0

    while j < len(arquivo):
        if arquivo[j] == classeProcurada:
            qtdeClasse +=1
        j+=1

    percentualClasse = (qtdeClasse * 100) / len(arquivo)
    return qtdeClasse, percentualClasse

    return qtdeClasse, percentualClasse



def ini(nomeAtivo,  dataInicio, avaliacaoIndices):
    #print("nome", nomeAtivo)
   # print(" data", dataInicio, "tipo", type(dataInicio))
   # print( "===>>> Estatistica")
    import numpy as np
    import f_util
    import f_metricas
    import f_medidaRisco

    dados = []
    tipoJanela=2
    if tipoJanela ==1:
        entrada1 = open("arqInicial/"+ nomeAtivo + " - dados agrupados de 2010 a 2016.csv","r")
        dataset = np.loadtxt(entrada1, delimiter=";")
        Valid_X     = dataset[limite:, 1:-2] # Pega da primeira até a penultima coluna dos dados
        data        = dataset[limite:,0:1]
        openPrice   = dataset[limite:,1:2] # //PREÇO DE ABERTURA
        maxPrice    = dataset[limite:,2:3]  #//PREÇO MÁXIMO
        minPrice    = dataset[limite:,3:4]  #//PREÇO MÍNIMO
        avgPrice    = dataset[limite:,4:5] # //PREÇO MÉDIO
        closePrice  = dataset[limite:,5:6] #  //PREÇO DO ÚLTIMO NEGÓCIO

    else:
        entrada1 = open("arqTotais/"+ nomeAtivo + " JanelaDesl.csv","r")
        dataset = np.loadtxt(entrada1, delimiter=";")
        Valid_X     = dataset[:, 1:-2] # Pega da primeira até a penultima coluna dos dados
        data        = dataset[:,0:1]
        openPrice   = dataset[:,1:2] # //PREÇO DE ABERTURA
        maxPrice    = dataset[:,2:3]  #//PREÇO MÁXIMO
        minPrice    = dataset[:,3:4]  #//PREÇO MÍNIMO
        avgPrice    = dataset[:,4:5] # //PREÇO MÉDIO
        closePrice  = dataset[:,5:6] #  //PREÇO DO ÚLTIMO NEGÓCIO
        bestPrice     = dataset[:,6:7]
        bestBidPrice  = dataset[:,7:8]
        numTrader     = dataset[:,8:9]
        amountTrader  = dataset[:,9:10]
        volumeFinanc  = dataset[:,10:11]
        classe        = dataset[:,11:12]
        closePrice2  = dataset[:,5:6]

    if avaliacaoIndices == 1:
        # avgPrice    = dataset[:,4:5] # //PREÇO MÉDIO
        closePrice = dataset[:, 4:5]  # //PREÇO DO ÚLTIMO NEGÓCIO
        #  bestPrice     = dataset[:,6:7]
        #  bestBidPrice  = dataset[:,7:8]
        numTrader = dataset[:, 5:6]
        #  amountTrader  = dataset[:,9:10]
        #  volumeFinanc  = dataset[:,10:11]
        classe = dataset[:, 6:7]
        # closePrice2  = dataset[:,5:6]




     ####################### >>>> Gravando a caracterização da amostra <<<< ######################

   # if avaliacaoIndices ==0: ###==>> Somente para dados de ações, esceto indices Globais
    saida22 = open("arqTotais/" + nomeAtivo + " Resultados.csv","w")
    saida33 = open("arqTotais/" + nomeAtivo + " medidasDispersao.csv", "w")
    amostra = "AMOSTRA"
    saida22.write(amostra +"\n")
    amostra="Dados; DataInicial; DataFinal; QtdeDias; PrecoInicial; PrecoFinal; Classe0; Classe1; Classe0; Classe1"
    saida22.write(amostra +"\n")


    dtInicio   = data[0]
    dtFim      = data[len(dataset)-1]

    # => formatando as datas
    dtInicioF = f_util.dataddmmaaaaa(str(int(dtInicio)))
    dtFimF = f_util.dataddmmaaaaa(str(int(dtFim)))

    qtdeDias = len(dataset)
    precoIni = openPrice[0]
    precoFim = closePrice[len(dataset)-1]

    qtdeClasse0 = calcularClasse(classe, 0)[0]
    qtdeClasse1 = calcularClasse(classe, 1)[0]
    percentualClasse0 = calcularClasse(classe, 0)[1]
    percentualClasse1 = calcularClasse(classe, 1)[1]

    #amostra="Dados; Dt. Inicial; Dt. Final; Qtde Dias; Preço Inicial; Preço Final; Classe 0; Classe 1; Classe 0; Classe 1"
    amostra = "janelaDeslizante;" + str(dtInicioF) + ";" + str(dtFimF) + ";" + str(qtdeDias) + ";" +  str("%.2f" %precoIni) + ";"+ str("%.2f" %precoFim) + ";" + str("%.2f" %percentualClasse0) + ";" + str("%.2f" %percentualClasse1) + ";" + str(qtdeClasse0) + ";" + str(qtdeClasse1)
    saida22.write(amostra +"\n")
    saida22.write(" " +"\n")

    #print('vou chamar medidasDispesao=', avaliacaoIndices)
   # amostra = "MEDIDASDISPERSAOTENDENCIA"

    #saida33.write(amostra +"\n")

    amostra = "Serie; media; desvioPadrao; desvioAbsoluto; mediana; quantil; minimo; maximo; amplitude; variancia"
    saida33.write(amostra +"\n")


    rt1 = f_metricas.medidasDispersaotendencia(openPrice)
    amostra = "PrecoAbertura;" + str("%.2f" %rt1[0]) + ";" + str("%.2f" %rt1[1]) + ";" + str("%.2f" %rt1[2]) + ";" + str("%.2f" %rt1[3]) + ";" +str("%.2f" %rt1[4]) +";"+ str("%.2f" %rt1[5]) + ";"+str("%.2f" %rt1[6])  +";"+ str("%.2f" %rt1[7]) +";"+ str("%.2f" %rt1[8])
    saida33.write(amostra +"\n")

    rt1 = f_metricas.medidasDispersaotendencia(closePrice)
    amostra = "PrecoFechamento;" + str("%.2f" %rt1[0]) + ";" + str("%.2f" %rt1[1]) + ";" + str("%.2f" %rt1[2]) + ";" + str("%.2f" %rt1[3]) + ";" +str("%.2f" %rt1[4]) +";"+ str("%.2f" %rt1[5]) + ";"+str("%.2f" %rt1[6])  +";"+ str("%.2f" %rt1[7]) +";"+ str("%.2f" %rt1[8])
    saida33.write(amostra +"\n")

    rt1 = f_metricas.medidasDispersaotendencia(maxPrice)
    amostra = "PrecoMaximo;" + str("%.2f" %rt1[0]) + ";" + str("%.2f" %rt1[1]) + ";" + str("%.2f" %rt1[2]) + ";" + str("%.2f" %rt1[3]) + ";" +str("%.2f" %rt1[4]) +";"+ str("%.2f" %rt1[5]) + ";"+str("%.2f" %rt1[6])  +";"+ str("%.2f" %rt1[7]) +";"+ str("%.2f" %rt1[8])
    saida33.write(amostra +"\n")

    rt1 = f_metricas.medidasDispersaotendencia(minPrice)
    amostra = "PrecoMinimo;" + str("%.2f" %rt1[0]) + ";" + str("%.2f" %rt1[1]) + ";" + str("%.2f" %rt1[2]) + ";" + str("%.2f" %rt1[3]) + ";" +str("%.2f" %rt1[4]) +";"+ str("%.2f" %rt1[5]) + ";"+str("%.2f" %rt1[6])  +";"+ str("%.2f" %rt1[7]) +";"+ str("%.2f" %rt1[8])
    saida33.write(amostra +"\n")


    if avaliacaoIndices == 0:
        rt1 = f_metricas.medidasDispersaotendencia(avgPrice)
        amostra = "PrecoMedio;" + str("%.2f" %rt1[0]) + ";" + str("%.2f" %rt1[1]) + ";" + str("%.2f" %rt1[2]) + ";" + str("%.2f" %rt1[3]) + ";" +str("%.2f" %rt1[4]) +";"+ str("%.2f" %rt1[5]) + ";"+str("%.2f" %rt1[6])  +";"+ str("%.2f" %rt1[7]) +";"+ str("%.2f" %rt1[8])
        saida33.write(amostra +"\n")

        rt1 = f_metricas.medidasDispersaotendencia(bestBidPrice)
        amostra = "PrecoMelhorCompra;" + str("%.2f" %rt1[0]) + ";" + str("%.2f" %rt1[1]) + ";" + str("%.2f" %rt1[2]) + ";" + str("%.2f" %rt1[3]) + ";" +str("%.2f" %rt1[4]) +";"+ str("%.2f" %rt1[5]) + ";"+str("%.2f" %rt1[6])  +";"+ str("%.2f" %rt1[7]) +";"+ str("%.2f" %rt1[8])
        saida33.write(amostra +"\n")

        rt1 = f_metricas.medidasDispersaotendencia(bestPrice)
        amostra = "PrecoMelhor;" + str("%.2f" %rt1[0]) + ";" + str("%.2f" %rt1[1]) + ";" + str("%.2f" %rt1[2]) + ";" + str("%.2f" %rt1[3]) + ";" +str("%.2f" %rt1[4]) +";"+ str("%.2f" %rt1[5]) + ";"+str("%.2f" %rt1[6])  +";"+ str("%.2f" %rt1[7]) +";"+ str("%.2f" %rt1[8])
        saida33.write(amostra +"\n")


    saida33.write("" + "\n")

    amostra = "BASELINE"
    saida22.write(amostra +"\n")

    amostra = "OraculoGabarito; BuyAndHold; BuyAndHoldP; CDI;	Selic;	Ibovespa;	IGPM; QtdeMeses"
    saida22.write(amostra +"\n")


    buyAndHoldF = precoFim - precoIni
    buyAndHold = (buyAndHoldF *100) / precoIni
    buyAndHold = buyAndHold - (buyAndHold * 0.17)

    retornoBaseline = f_util.baseline(int(str(int(dtInicio))[:6]), int(str(int(dtFim))[:6]), 'arqInicial/ipeadata CDI SELIC IBOVESPA.xls')
    cdi = retornoBaseline[0]
    selic = str("%.2f" %retornoBaseline[1])
    ibovespa = str("%.2f" %retornoBaseline[2])
    igpm = str("%.2f" %retornoBaseline[3])
    qtdeMeses = str(retornoBaseline[4])

    amostra = "pendente;" + str("%.2f" %buyAndHoldF) + ";" + str("%.2f" %buyAndHold) + ";" + str("%.2f" %cdi) +";"+ selic+";" + ibovespa+";" + igpm+";" + qtdeMeses
    saida22.write(amostra +"\n")
    saida22.write(" " +"\n")

    #dados.append(str(dtInicioF) + ";" + str(dtFimF) + ";" + str(qtdeDias) + ";" +  str("%.2f" %precoIni) + ";"+ str("%.2f" %precoFim) + ";" + str("%.2f" %percentualClasse0) + ";" + str("%.2f" %percentualClasse1) + ";" + str(qtdeClasse0) + ";" + str(qtdeClasse1)+ ";" + str("%.2f" %buyAndHoldF) + ";" + str("%.2f" %buyAndHold) + ";" + str("%.2f" %cdi) +";"+ selic+";" + ibovespa+";" + igpm+";" + qtdeMeses)
    dados.append(str(dtInicioF) + ";" + str(dtFimF) + ";" + str(qtdeDias) + ";" +  str("%.2f" %precoIni) + ";"+ str("%.2f" %precoFim) + ";" + str("%.2f" %percentualClasse0) + ";" + str("%.2f" %percentualClasse1) + ";" + str(qtdeClasse0) + ";" + str(qtdeClasse1)) #+ ";" + str("%.2f" %buyAndHoldF) + ";" + str("%.2f" %cdi) +";"+ selic+";" + ibovespa+";" + igpm+";" + qtdeMeses)

    amostra = "MEDIDASRISCO"
    saida22.write(amostra +"\n")
    amostra = "Serie; Volatilidade; DesvioPadrao; Sharpe; Volatilidade Downside; DpDownside; Sortino;" # VAR; CVAR"
    saida22.write(amostra +"\n")

    rt = f_medidaRisco.medidaVolatilidade(classe, closePrice, openPrice)
    volatilidade = rt[0]
    dvPadrao = rt[2]
    indiceSharpe = f_medidaRisco.medidaSharpeRadio(cdi, volatilidade, buyAndHold)

    rt = f_medidaRisco.medidaVolatilidadeDownside(classe, closePrice, openPrice)
    volatilidadeDownside = rt[0]
    dvPadraoDownside = rt[2]
    indiceSortino = f_medidaRisco.medidaSortinoRadio(cdi, volatilidadeDownside, buyAndHold)


    # Gravando dados
    amostra = "RetornoFechamento-Abertura;" + str("%.2f" %volatilidade) + ";" + str("%.2f" %dvPadrao) + ";" +str("%.2f" %indiceSharpe) + ";" + str("%.2f" %volatilidadeDownside) + ";" + str("%.2f" %dvPadraoDownside) + ";" + str("%.2f" %indiceSortino)
    saida22.write(amostra +"\n")

    return dados, str("%.2f" %buyAndHold)
