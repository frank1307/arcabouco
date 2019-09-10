

def ini (predicao, openPrice, closePrice, tipoEstrategia, reajuste):
    import f_indicadores
    i=0
    print ("valor", len(predicao))
    while i < len(predicao):
        if predicao[i] > 0:
            if tipoEstrategia ==1:
                estrategia01(openPrice, closePrice)

            if tipoEstrategia ==2:
                estrategia02(openPrice, reajuste)

            if tipoEstrategia ==3:
                if (f_indicadores.sma(periodo, lidos, closePrice, i) < openPrice):
                    estrategia01(openPrice, closePrice)

            if tipoEstrategia ==4:
                if (f_indicadores.sma(periodo, lidos, closePrice, i) < openPrice):
                    estrategia02(openPrice, reajuste)

def estrategia01 (openPrice, closePrice):
    diferenca = closePrice - openPrice
    percentual = (diferenca *100)/openPrice
    return (diferenca, percentual)

def estrategia02 (openPrice, reajuste):
    diferenca = (openPrice * reajuste) - openPrice
    percentual = (diferenca *100)/openPrice
    return (diferenca, percentual)


ini([1],20.20, 21.00, 1, 0)