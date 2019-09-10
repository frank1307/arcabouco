##
##
## Cálculo da volatilidade: é a medida da taxa de variação de um ativo num determinado período de tempo, ou seja,
##                          quanto este ativo variou em (%) num determinado período
##
## Período referencia: 252 dias = 1 ano
## Informar os preços de fechamento do período a ser avaliado e a quantidade de dias
## Refereência: Investpedia https://www.youtube.com/watch?v=1PybWYh0_NE
##
def medidaVolatilidade(retorno, closePrice, openPrice):
    import math
    import f_metricas
    import numpy as np

    i=0
    while i < len(closePrice):
        retorno [i] = closePrice [i] - openPrice[i]
        i+=1

    desvioPadrao = f_metricas.medidasDispersaotendencia(retorno)[1]
    volatilidade = (desvioPadrao*(math.sqrt(252)))
    # 252 dias = 1 ano

    #print ("volatilidade", volatilidade, "DP", desvioPadrao) # "tam da serie", len(log))
    return volatilidade, retorno, desvioPadrao


def medidaVolatilidadeDownside(retorno, closePrice, openPrice):
    import math
    import f_metricas
    import numpy as np

    i=0
    while i < len(closePrice):
        retorno [i] = closePrice [i] - openPrice[i]
        if retorno [i]>0:
            retorno[i] =0

        #retorno [i] = math.log(closePrice [i] - openPrice[i])
        #print ("open",openPrice[i],"close", closePrice[i], "retorno", retorno[i])

        i+=1

    desvioPadrao = f_metricas.medidasDispersaotendencia(retorno)[1]
    volatilidade = (desvioPadrao*(math.sqrt(252)))
    # 252 dias = 1 ano

    #print ("volatilidade Downside", volatilidade, "DP", desvioPadrao) # "tam da serie", len(log))
    return volatilidade, retorno, desvioPadrao


def medidaSharpeRadio(cdi, volatilidade, rendimentoFundo):
##    O Indice Sharpe Radio é uma media de eficiencia da relação do risco X retorno, ou seja,
##            quanto maior é o indice Sharpe mais eficiente é o meu fundo.
##
##   Variáveis necessárias para o período avaliado:
##      - Rendimento do CDI (%)
##      - Rendimento do Fundo (%)
##      - Volatilidade (%)
##
##   Calculo realizado:
##   Indice Sharpe = (Rendimento do Fundo(%) - Rendimento do CDI(%)) / volatilidade(%)
##
##   Referencia: https://www.youtube.com/watch?v=K3V_AZPMhvs
##   http://www.clubedospoupadores.com/investimentos/indice-sharpe.html
##

    indiceSharpe = (rendimentoFundo - cdi) / volatilidade
    return indiceSharpe


def medidaSortinoRadio(cdi, volatilidadeDownside, rendimentoFundo):

    indiceSortino = (rendimentoFundo - cdi) / volatilidadeDownside

    #print("indice Sortino=",indiceSortino)

    return indiceSortino

