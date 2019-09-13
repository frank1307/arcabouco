#
#  Este programa realiza a estrategia de operação e grava a tabela de Totais e a tabela de ganho mensal.
# Funções:
#   * Ler os arquivos (previsão) gerados pelo programa P3_classificar;
#   * Ler o dataset completo com os dados originais para a realização da operação com os dados de teste
#   * Calcular a diferença entre o ClosePrice(D+1) e o OpenPrice(D+1)
#   * Calcular o Percentual de variação Percentual= (diferença * 100) / OpenPrice(D+1)
#
#   * Verifica no arquivo de previsao
#     se o (sinal da previsão) for > 0
#         então calcula o total de Altas (%) e (R$)
#     Senão
#         calcula o total de Baixas (%) e (R$)
#
#   * Grava um novo dataset com  log de toda a operação realizada
#
#   * Grava um novo dataser contendo os totalizadores da operação:
#       Nome do algoritmo
#       retorno financeiro total (R$)
#       total de baixa (R$)
#       total de altas (R$)
#       Ganho (%)
#       total de acertos (%)
#       total de erros (%)
#       qtde de erros
#       qtde de acertos
#       qtde total de gatilhos
#       total classe 0
#       total classe 1
#       precisao
#       acuracia
#       f1score
#       recall
##
#   * Grava 1 novo dataset contendo a Previsao de todos os datasets avaliados para os 8 classificadores para a escolha do melhor dataset
#
from random import randint
import f_indicadores
import f_util


def ini(nomeAtivo, entrada2, tipoJanela, tipoNormalizacao, dataInicio, dtIni, dtFim, qtdeClassificadores, tipoEstrategia,  volumeNegociado, retornoP2):

    import numpy as np
    import f_util

    print("==>> P4_Operar:     ", f_util.imprimirHora(), "D1", "N=", tipoNormalizacao, "J=", tipoJanela)

    entrada1 = open("arqTotais/" + nomeAtivo + " JanelaDesl.csv", "r")
    dataset = np.loadtxt(entrada1, delimiter=";")

    qtdeD3_caiu         = retornoP2[0]
    qtdeD3_estavel      = retornoP2[1]
    qtdeD3_subiu        = retornoP2[2]
    qtdeRompimento      = retornoP2[3]
    qtdeCorrecao        = retornoP2[4]
    qtdeContraTendencia = retornoP2[5]

    Valid_X     = dataset[:, 1:-2] # Pega da primeira até a penultima coluna dos dados
    data        = dataset[:,0:1]
    openPrice   = dataset[:,1:2] # //PREÇO DE ABERTURA
    maxPrice    = dataset[:,2:3]  #//PREÇO MÁXIMO
    minPrice    = dataset[:,3:4]  #//PREÇO MÍNIMO
    avgPrice    = dataset[:,4:5] # //PREÇO MÉDIO
    closePrice  = dataset[:,5:6] #  //PREÇO DO ÚLTIMO NEGÓCIO
    classe = dataset[:,11:12]



    dataset2 = np.loadtxt("arqTotais/"+ entrada2[0], delimiter=";")
    ini      = 0
    fim      = 1

    retornoBaseline = f_util.baseline(dtIni, dtFim, 'arqInicial/ipeadata CDI SELIC IBOVESPA.xls')
    cdi             = retornoBaseline[0]

    import f_medidaRisco
    rt                   = f_medidaRisco.medidaVolatilidade(classe, closePrice, openPrice)
    volatilidade         = rt[0]
    rt                   = f_medidaRisco.medidaVolatilidadeDownside(classe, closePrice, openPrice)
    volatilidadeDownside = rt[0]

    saida3 = open("arqTotais/" + nomeAtivo + " N" + str(tipoNormalizacao) + " D1" + " J" + str(tipoJanela) + " log operacao.csv","w")

    log = "classificador;data;sinalcompra;acertou;openprice;closeprice;vlrcompra;vlrvenda;lucrobrutoR;impostorendaR;custotransacaoR;lucroliquidoR;lucrobrutoP;lucroliquidoP;custotransacaoP;custotransacaoAcumuladoP;lucrobrutoAcumuladoP;lucroliquidoAcumuladoP;evolucaoCapitalR;impostoRendaAcumuladoR"



    saida3.write(log + "\n")

    saida1 = open("arqTotais/" + nomeAtivo + " D1" + " J" + str(tipoJanela) + " N" + str(tipoNormalizacao) + " Totais.csv","w")

    import f_metricas

    j = sumPrecision =sumGanho = 0


    while j < qtdeClassificadores: # => é a quantidade de classificadores / Previsões

        i = qtdeAcertos2 = qtdeErros = totBaixas = totClasse0 = totClasse1 = drawdown = totBaixasF = totAltasF = valorMaximo = 0

        predicao = dataset2[:,ini:fim]

        serieReal = dataset2[:,9:10]
        serieReal = serieReal[:len(serieReal)-1] ## Ajuste da serie
        predicao = predicao[:len(predicao)-1]   ## Ajuste da serie

        rt = f_metricas.calculado(serieReal, predicao)

        indComprarSempreP = 0
        indComprarSemprePd = []
        indInversoP = 0
        indInversoPd = []
        indAleatorioP = 0
        indAleatorioPd = []
        indAlvo1P = 0
        indAlvo1Pd = []
        indAlvo05P = 0
        indAlvo05Pd = []
        indAlvo2P = 0
        indAlvo2Pd = []
        evolucaoCapital = 0
        evolucaoCapitalBruto = 0

        custoAcumulado = 0
        lucroLiquidoAcumulado = 0
        lucroBrutoAcumulado = 0
        impostoRendaAcumulado = 0

        totAltas = 0
        retornoArr = []
        retornoDrawArr = []

        while i < len(predicao):                                #--> Qtde (dias) de previsões]

            indComprarSempreP = indComprarSempreP + ((closePrice[i + 1] - openPrice[i + 1])*100) / openPrice[i + 1]

            a = ((closePrice[i + 1] - openPrice[i + 1]) * 100) / openPrice[i + 1]
            indComprarSemprePd.append(float(str("%.2f" % a)))

            ##==> Calculando Indicador Aleatório (Naive)
            if (randint(0,1)) == 1:
                indAleatorioP = indAleatorioP + ((closePrice[i + 1] - openPrice[i + 1])*100) / openPrice[i + 1]
                a = ((closePrice[i + 1] - openPrice[i + 1]) * 100) / openPrice[i + 1]
                indAleatorioPd.append(float(str("%.2f" % a)))


            sinal = (dataset2[:,ini:fim][i])


            ##==> Calculando Indicador Inverso
            if int(sinal) <= 0:
                totClasse0 += 1
                indInversoP = indInversoP + ((closePrice[i + 1] - openPrice[i + 1])*100) / openPrice[i + 1]
                a = ((closePrice[i + 1] - openPrice[i + 1]) * 100) / openPrice[i + 1]
                if a > 0:
                    a = a - (a * 0.22)
                indInversoPd.append(float(str("%.2f" % a)))
            else:
                indInversoPd.append(0)


            if int(sinal) > 0:

               ##==> Calculando Indicador Alvo 0.5%
                alvo =0.005 * openPrice[i + 1]
                if (alvo + openPrice[i + 1]) <= maxPrice[i + 1]:
                    indAlvo05P += 0.5
                    indAlvo05Pd.append(0.5)
                else:
                    indAlvo05P = indAlvo05P + ((closePrice[i + 1] - openPrice[i + 1])*100) / openPrice[i + 1]
                    a = ((closePrice[i + 1] - openPrice[i + 1]) * 100) / openPrice[i + 1]
                    indAlvo05Pd.append(float(str("%.2f" % a)))

                ##==> Calculando Indicador Alvo 1%
                alvo = 0.01 * openPrice[i + 1]
                if (alvo + openPrice[i + 1]) <= maxPrice[i + 1]:
                    indAlvo1P += 1
                    indAlvo1Pd.append(1)

                else:
                    indAlvo1P = indAlvo1P + ((closePrice[i + 1] - openPrice[i + 1])*100) / openPrice[i + 1]
                    a = ((closePrice[i + 1] - openPrice[i + 1]) * 100) / openPrice[i + 1]
                    indAlvo1Pd.append(float(str("%.2f" % a)))

               ##==> Calculando Indicador Alvo 2%
                alvo = 0.02 * openPrice[i + 1]
                if (alvo + openPrice[i + 1]) <= maxPrice[i + 1]:
                    indAlvo2P += 2.00
                    indAlvo2Pd.append(2)
                else:
                    indAlvo2P = indAlvo2P + ((closePrice[i + 1] - openPrice[i + 1])*100) / openPrice[i + 1]
                    a = ((closePrice[i + 1] - openPrice[i + 1]) * 100) / openPrice[i + 1]
                    indAlvo2Pd.append(float(str("%.2f" % a)))


            if int(sinal) > 0:
                totClasse1 += 1



            ## -- Calculo da Evolução de Capital e Custo Operacional

                acertou = "N"
                import f_util
                r = f_util.calcularCustoOperacional(volumeNegociado, openPrice[i + 1], closePrice[i + 1], maxPrice[i + 1], acertou, tipoEstrategia, 1, 1, evolucaoCapitalBruto)
                valorCompra    = r[0]
                valorVenda     = r[1]
                impostoRenda   = r[2]
                lucroBrutoP    = r[4]
                lucroBrutoF    = r[5]
                #lucroLiquidoP  = r[6]
                lucroLiquidoP = lucroBrutoP - (lucroBrutoP * 0.22)
                lucroLiquidoF  = r[7]
                acertou        = r[8]
                custoTransacaoF = r[9]
                custoTransacao = r[3]
                custoTransacao = lucroBrutoP - lucroLiquidoP

                evolucaoCapitalBruto  += lucroBrutoF
                evolucaoCapital       += lucroLiquidoF
                custoAcumulado        += custoTransacao
                lucroBrutoAcumulado   += lucroBrutoP
                lucroLiquidoAcumulado += lucroLiquidoP
                impostoRendaAcumulado += impostoRenda

                if lucroBrutoP > 0:
                    totAltas = totAltas + lucroBrutoP  # ==>> Financeiro
                    totAltasF = totAltasF + lucroBrutoF  # ==> Percentual
                    qtdeAcertos2 += 1
                else:
                    totBaixas = totBaixas + lucroBrutoP
                    totBaixasF = totBaixasF + lucroBrutoF
                    qtdeErros += 1

                # => calculando do drawdown
                if drawdown > lucroBrutoP:
                   drawdown = lucroBrutoP


                if valorMaximo < lucroBrutoP:
                    valorMaximo = lucroBrutoP

                if j == 6:
                    if lucroBrutoP >= 0:
                        retornoDrawArr.append(0)
                    else:
                        retornoDrawArr.append(float(str("%.2f" % lucroBrutoP)))

                retornoArr.append(float(str("%.2f" % lucroBrutoP)))


                log = str(j + 1) + ";" + str(int(data[i])) + ";" + str(int(sinal)) + ";" + str(acertou)  + ";" + str(
                "%.2f" % openPrice[i + 1]) + ";" + str("%.2f" % closePrice[i + 1]) + ";"   + str(
                "%.2f" % valorCompra) + ";" + str("%.2f" % valorVenda) + ";" + str("%.2f" % lucroBrutoF) + ";" + str("%.2f" % impostoRenda) + ";" + str(
                "%.2f" % custoTransacaoF) + ";" + str("%.2f" % lucroLiquidoF) + ";"+ str("%.2f" % lucroBrutoP) + ";" + str("%.2f" % lucroLiquidoP) + ";" + str(
                "%.2f" % custoTransacao) + ";" + str("%.2f" % custoAcumulado) + ";" + str(
                "%.2f" % lucroBrutoAcumulado) + ";" + str("%.2f" % lucroLiquidoAcumulado) + ";" + str(
                "%.2f" % evolucaoCapital)  + ";" + str("%.2f" % impostoRendaAcumulado)

                ## -- gravando somente o log do modelo de clasificação RBM + KNN / obs: classificador numero 7
                if (j == 6):  # or j==0 :
                    saida3.write(log + "\n")


            i += 1

        ini += 1
        fim += 1

        if j==6:
            import f_grafico
            f_grafico.f_graficoDrawDown2(dataInicio, nomeAtivo, retornoDrawArr)
            retornoDrawArr.clear()

        totGatilhos   = qtdeAcertos2 + qtdeErros
        Ganho         = totAltas + totBaixas
        retornoF      = totAltasF + totBaixasF
        nomeAlgoritmo = ini
        retornoMedio  = 0
        perdaMedia    = 0
        ganhoMedio    = 0

        if totGatilhos >0:
            retornoMedio = Ganho/totGatilhos
        if qtdeErros >0:
            perdaMedia = totBaixas/qtdeErros
        if qtdeAcertos2 > 0:
            ganhoMedio = totAltas/qtdeAcertos2

        indiceSharpe  = f_medidaRisco.medidaSharpeRadio(cdi, volatilidade, Ganho)
        indiceSortino = f_medidaRisco.medidaSortinoRadio(cdi, volatilidadeDownside, Ganho)


        import f_metricas
        ret             = f_metricas.medidasDispersaotendencia(retornoArr)
        media           = ret[0]
        desvioPadrao    = ret[1]
        desvioAbsoluto  = ret[2]
        mediana         = ret[3]
        quantil         = ret[4]
        minimo          = ret[5]
        maximo          = ret[6]
        amplitude       = ret[7]
        variancia       = ret[8]


        import f_estatistica
        r999        = f_estatistica.ini(nomeAtivo, dataInicio, 0)
        buyAndholdP = r999[1]
        consol      = str(r999[0])
        consol      = consol.replace("['","")
        consol      = consol.replace("']","")

        import f_util
        hip               = f_util.testeDeHipotese(retornoArr, indComprarSemprePd, indAleatorioPd, indInversoPd, indAlvo05Pd, indAlvo1Pd, indAlvo2Pd)
        ShapiroWilk       = hip[0]
        KolmogorovSmirnov = hip[1]
        Tstudent          = hip[2]
        Anova             = hip[3]
        kruskal           = hip[4]

        ##==>> Gravando os indicadores da Tabela Consolidada
        s = (str(nomeAtivo) + ";" + str(nomeAlgoritmo) + ";" + str(("%.2f" % lucroBrutoAcumulado)) + ";"
             + str(("%.2f" % lucroLiquidoAcumulado)) + ";" + str(("%.2f" % custoAcumulado)) + ";"
             + str(buyAndholdP) + ";"
             + str("%.2f" % indComprarSempreP) + ";"
             + str("%.2f" % indInversoP) + ";"
             + str("%.2f" % indAleatorioP)
              +";"+  str("%.2f" %indAlvo05P)
             +";"+  str("%.2f" %indAlvo1P)
             +";"+  str("%.2f" %indAlvo2P)
             + ";"+ str(("%.2f" %totBaixas))+ ";" + str(("%.2f" %totAltas)) + ";" + str(("%.2f" %retornoMedio)) + ";"
            + str(("%.2f" %perdaMedia)) + ";" + str(("%.2f" %ganhoMedio)) + ";" + str(qtdeErros) + ";" + str(qtdeAcertos2) + ";" + str(totGatilhos) + ";" + str(totClasse0) + ";" +str(totClasse1)
             + ";" + str("%.2f" %rt[0]) + ";" + str("%.2f" %rt[1]) + ";" + str("%.2f" %rt[2]) + ";" +str("%.2f" %rt[3]) + ";" +str("%.2f" %rt[4]) + ";"+ str("%.2f" %indiceSharpe) + ";"
                 + str("%.2f" %indiceSortino)
             +";"+  str("%.2f" %media) +";"+  str("%.2f" %desvioPadrao) +";"+  str("%.2f" %desvioAbsoluto) +";"+  str("%.2f" %mediana) +";"+  str("%.2f" %quantil) +";"+  str("%.2f" %minimo)
             +";"+  str("%.2f" %maximo) +";"+  str("%.2f" %amplitude) +";"+  str("%.2f" %variancia) + ";"
             + consol + ";"
             + str("%.2f" %volatilidade) + ";" + str("%.2f" %volatilidadeDownside)


             + ";" + str(qtdeD3_caiu) +";"+  str(qtdeD3_estavel) +";"+  str(qtdeD3_subiu) +";"+  str(qtdeRompimento) +";"+  str(qtdeCorrecao) +";"+  str(qtdeContraTendencia)

             +";"+ str("%.2f" %ShapiroWilk) +";"+ str("%.2f" %KolmogorovSmirnov) +";"+  str("%.2f" %Tstudent) +";"+ str("%.2f" %Anova) +";"+ str("%.2f" %kruskal) + "\n" )



        if j <= 7:
            sumPrecision += rt[0]
            sumGanho     += Ganho

        s = s.replace("]","")
        s = s.replace("[","")
        s = s.replace(" ","")

        saida1.write(s)
        saida3.close

        j = j + 1
    saida1.close()
    saida3.close()

    avgPrecision = sumPrecision / 8
    avgGanho     = sumGanho / 8

    import f_grafico
    f_grafico.f_graficoBoxPlotEstrategias(dataInicio, nomeAtivo, retornoArr,
                                    indComprarSemprePd,
                                    indAlvo2Pd,
                                    indAlvo05Pd,
                                    indAlvo1Pd,
                                    indAleatorioPd,
                                    indInversoPd)


    retornoArr.clear()

    return avgPrecision, avgGanho

