##
## Esta função gera o extrato de operação Por Código de Ativo
##
##
def ini(dataInicio, nomeAtivo, qtdeDiasTeste):
    import pandas as pd
    import f_util
    import f_grafico

    print("==>> P6_analisar:   ", f_util.imprimirHora()) ##, " Qtde de combinações", len(df))

    result = pd.concat([
    pd.io.parsers.read_csv("arqInicial/cabecalho2.csv", header=None),
    pd.io.parsers.read_csv("arqTotais/" + nomeAtivo + " D1 J2 N3 Totais.csv", header=None),
    ])

    df = pd.DataFrame(result)

    df.to_csv('arqTotais/' + nomeAtivo + ' operacao.csv', header=0, index=None)

    nomeArquivo      = "arqTotais/" + nomeAtivo + " operacao.csv"
    dadosTeste       = "arqTotais/" + nomeAtivo + " JanelaDesl.csv"
    dadosLog         = "arqTotais/" + nomeAtivo + " N3 D1 J2 log operacao.csv"
    cab              = "arqInicial/cabecalho3.csv"
    medidasDispersao = "arqTotais/" + nomeAtivo + " medidasDispersao.csv"


    result = pd.concat([
        # pd.io.parsers.read_csv(nomeArquivo1, header=-1),
        pd.io.parsers.read_csv(nomeArquivo, header=None),
        pd.io.parsers.read_csv(cab, header=None),
        pd.io.parsers.read_csv(dadosTeste, header=None),
        pd.io.parsers.read_csv(dadosLog, header=None),
        pd.io.parsers.read_csv(medidasDispersao, header=None)

    ])

    df = pd.DataFrame(result)

    df.to_csv('Result/' + str(dataInicio) + " " + nomeAtivo + " Extrato " + str(qtdeDiasTeste) + " dias.csv", header=0,
              index=-1)


    f_grafico.f_graficoRetornoAcumulado(nomeAtivo, dataInicio, qtdeDiasTeste)

    return


def gerarGraficosConsolidados():

    import pandas as pd
    import f_grafico


    df = pd.read_csv("Result/Extrato consolidadoAux.csv", header=-0)

    SVM     = df[df["classificador"] == 1]["RetornoLiquido"]
    NB      = df[df["classificador"] == 2]["RetornoLiquido"]
    KNN     = df[df["classificador"] == 3]["RetornoLiquido"]
    DT      = df[df["classificador"] == 4]["RetornoLiquido"]
    RBM_SVM = df[df["classificador"] == 5]["RetornoLiquido"]
    RBM_NB  = df[df["classificador"] == 6]["RetornoLiquido"]
    RBM_KNN = df[df["classificador"] == 7]["RetornoLiquido"]
    RBM_DT  = df[df["classificador"] == 8]["RetornoLiquido"]
    #oraculo = df[df["classificador"] == 9]["RetornoLiquido"]

    tecnicasTradicionais = pd.concat([SVM, KNN, NB, DT])
    tecnicasCombinadas   = pd.concat([RBM_SVM, RBM_NB, RBM_KNN, RBM_DT])

    f_grafico.f_graficoBoxPlotFinancConsolidados(tecnicasTradicionais, tecnicasCombinadas)
    f_grafico.f_graficoBoxPlotEstrategia_Classif(KNN, SVM, NB, DT, RBM_KNN, RBM_SVM, RBM_NB, RBM_DT)

    SVM      = df[df["classificador"] == 1]["precisao"]
    NB       = df[df["classificador"] == 2]["precisao"]
    KNN      = df[df["classificador"] == 3]["precisao"]
    DT       = df[df["classificador"] == 4]["precisao"]
    RBM_SVM  = df[df["classificador"] == 5]["precisao"]
    RBM_NB   = df[df["classificador"] == 6]["precisao"]
    RBM_KNN  = df[df["classificador"] == 7]["precisao"]
    RBM_DT   = df[df["classificador"] == 8]["precisao"]
    #oraculo = df[df["classificador"] == 9]["precisao"]

    tecnicasTradicionais = pd.concat([SVM, KNN, NB, DT])
    tecnicasCombinadas   = pd.concat([RBM_SVM, RBM_NB, RBM_KNN, RBM_DT])

    f_grafico.f_graficoBoxPlotPrecisaoConsolidados(tecnicasTradicionais, tecnicasCombinadas)
    f_grafico.f_graficoBoxPlotAcuraciaClassif(KNN, SVM, NB, DT, RBM_KNN, RBM_SVM, RBM_NB, RBM_DT)

    SVM     = df[df["classificador"] == 1]["acuracia"]
    NB      = df[df["classificador"] == 2]["acuracia"]
    KNN     = df[df["classificador"] == 3]["acuracia"]
    DT      = df[df["classificador"] == 4]["acuracia"]
    RBM_SVM = df[df["classificador"] == 5]["acuracia"]
    RBM_NB  = df[df["classificador"] == 6]["acuracia"]
    RBM_KNN = df[df["classificador"] == 7]["acuracia"]
    RBM_DT  = df[df["classificador"] == 8]["acuracia"]
   # oraculo = df[df["classificador"] == 9]["acuracia"]

    tecnicasTradicionais = pd.concat([SVM, KNN, NB, DT])
    tecnicasCombinadas = pd.concat([RBM_SVM, RBM_NB, RBM_KNN, RBM_DT])

    f_grafico.f_graficoBoxPlotAcuraciaConsolidados(tecnicasTradicionais, tecnicasCombinadas)
    f_grafico.f_graficoBoxPlotPrecisaoClassif(KNN, SVM, NB, DT, RBM_KNN, RBM_SVM, RBM_NB, RBM_DT)

    return


def gerarTabelaConsolidada(qtdeDiasTeste, nomeAtivo):
    ##
    ## Esta função gera o Extrato Consolidado de Todos os Ativos
    ##
    ##
    import pandas as pd
    import f_grafico

    data = [pd.io.parsers.read_csv("arqTotais/" + nomeAtivo[i] + " operacao.csv", header=-0) for i in range(len(nomeAtivo))]
    result = pd.concat(data)

    df = pd.DataFrame(result)
    df.to_csv("Result/Extrato consolidado" + str(qtdeDiasTeste) + " dias.csv", header=0, index=None)

    result2 = pd.concat([
       pd.io.parsers.read_csv("arqInicial/cabecalho2.csv", header=None, sep=";"),
       pd.io.parsers.read_csv("Result/Extrato consolidado" + str(qtdeDiasTeste) + " dias.csv", header=None, sep=";")])

    df = pd.DataFrame(result2)
    df.to_csv("Result/Extrato consolidadoAux.csv", header=0, index=None)

    df = pd.read_csv("Result/Extrato consolidadoAux.csv")

    ##==>> Seleciona somente os resultados do Modelo Combinado (RBM+KNN)
    df3 = df[df["classificador"] == 7.0]


    f_grafico.f_graficoBoxPlotEstrategiasTodosAtivos(df3['RetornoBruto'], df3['BuyAndHoldP'],
                                                     df3['comprarSempreP'], df3['IndInversoP'],
                                                     df3['IndAleatorioP'], df3['indAlvo05P'],
                                                     df3['indAlvo1P'], df3['indAlvo2P'])


    f_grafico.f_graficoBoxPlotMedidasDesempenho(df3['precisao'],
                                                df3['acuracia'],
                                                df3['f1score'],
                                                df3['recall'],
                                                df3['specificity'])

    ###===>> Realizando a Transposta da Tabela de Resultados consolidada.
    df3 = df3.T

    ###===>> Gravado a Tabela de Resultados consolidada já formatada e pendente somente a inclusão do cabeçalho formatado.
    df3.to_csv("Result/Extrato consolidadoAuxSort.csv", header=0, index=None, sep=";")


    ##==>> Gerar Graficos Consolidados de todos os Ativos Avaliados (Estratégia, Acurácia e Precisão)
    gerarGraficosConsolidados()

    return