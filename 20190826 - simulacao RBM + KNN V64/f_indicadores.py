def bloomberg(nome_ativo, dataProcurada):
    import numpy as np

    dataset = np.loadtxt(open("arqInicial/dadosbloomberg/"+ nome_ativo+ "C.csv", "r"), delimiter=";")
    data    = dataset[:, 0:1]
    mini     = dataset[:, 1:2]  # //PREÇO DE ABERTURA
    media   = dataset[:, 2:3]  # //PREÇO MÁX
    maxi     = dataset[:, 3:4]  # //PREÇO MÁX
    indicador = 0

    dataList= []
    dataList.append(dataProcurada)

    if dataList in data.tolist():
        i = data.tolist().index(dataList)
        soma = mini[i] + media[i] + maxi[i]

        if soma != 0:
            indicador = 1

    return indicador

def mfi(periodo,lidos, closePrice, i, minPrice, maxPrice, numTrader):
        ptAnt=0
        mfi = 0
        #periodo =14
        if lidos < periodo:
                mfi = 0
        else:
                h=i
                j=0
                negativoT=0
                positivoT=0

                while j <periodo:
                        pt = (float(closePrice[h-1]) + float(minPrice[h-1]) + float(maxPrice[h-1]))/3

                        if pt > ptAnt:
                                positivoT= positivoT + (pt * int(numTrader[h-1]))
                        else:
                                negativoT= negativoT + (pt * int(numTrader[h-1]))

                        h=h-1
                        ptAnt=pt
                        j=j+1

                if negativoT != 0:
                         mfi = 100 - (100/(1+ (positivoT/negativoT)))

                if float(mfi) > 70:
                   mfi=0
                else:
                    if float(mfi) <35:
                            mfi=1
                    else:
                            mfi=0

        return mfi

def sma(periodo, lidos, closePrice, i):
        #periodo =14
        smaPrice=0
        if lidos < periodo:
                smaPrice=0
        else:
                h=i
                j=0

                while j <periodo:
                        smaPrice = smaPrice  + float(closePrice[h-1])
                        h=h-1
                        j=j+1

                smaPrice  = smaPrice /14

                if smaPrice < closePrice[i-1]:
                         smaPrice=1
                else:
                         smaPrice=0


        return smaPrice

def obv(lidos, numTrader, i):
        obv=0
        if lidos ==1:
                obv=0
        else:
                obv = (float(numTrader[i-1]) - float(numTrader[i-2]))
                if obv > 0:
                        obv =1
                else:
                        obv =0
        return obv

# *************************************************************************************************************************
#  Este indicador realiza o calculo dos indicadores das Ondas de Elliott através dos
#  movimentos de Rompimento, Contra Tendencia e Correção
#  at = atributo avaliado
def elliottWave(at, i):
        correcao        =0
        contraTendencia =0
        rompimento      =0

        if i > 2: #==>> indice do arquivo avalaido
                if (float(at[i-2]) < float(at[i-1])) and (float(at[i]) < float(at[i-1])) and (float(at[i])> float(at[i-2])):
                        rompimento  = 1
                else:
                        rompimento  = 0

                if (float(at[i-2]) > float(at[i-1])) and (float(at[i]) > float(at[i-1])) and (float(at[i]) < float(at[i-2])):
                        contraTendencia  = 1
                else:
                        contraTendencia = 0

        if i > 3:
                if (float(at[i-3]) < float(at[i-2])) and float(at[i-2]) > float(at[i-1]) and float(at[i-1])> float(at[i-3]) and float(at[i]) > float(at[i-2]):
                        correcao = 1
                else:
                        correcao = 0

        return (correcao, contraTendencia, rompimento)


#
# Indicador de Defasagem de três dias (D3)
#
def defasagemD3(atrib, i):
        defasagem_3_subiu   = 0
        defasagem_3_caiu    = 0
        defasagem_3_estavel = 0

        if i > 2: #==>> indice do arquivo avalaido
                if float(atrib[i]) > float(atrib[i-1])  and float(atrib[i-1]) > float(atrib[i-2]):
                        defasagem_3_subiu  = 1
                else:
                        defasagem_3_subiu  = 0

                if float(atrib[i]) < float(atrib[i-1])  and  float(atrib[i-1]) < float(atrib[-2]):
                        defasagem_3_caiu  = 1
                else:
                        defasagem_3_caiu  = 0

                if float(atrib[i]) == float(atrib[i-1])  and float(atrib[i-1]) == float(atrib[i-2]):
                        defasagem_3_estavel  = 1
                else:
                        defasagem_3_estavel  = 0

        return (defasagem_3_subiu, defasagem_3_caiu, defasagem_3_estavel)