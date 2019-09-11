def separarAtivo(assetsList, dataInicio, periodoTotal,entryNane):

    print("==>> Relação de Ativos que serão avaliados:")

    k = lidos = gravados = 0

    for asset in assetsList:
        
        print(asset)
        saida    = open("arqTotais/"+ asset + ".csv", 'w')
        entrada1 = open(entryNane, 'r')
        gravados = 0

        iterlinha=iter(entrada1)
        next(iterlinha)    
        #Como a primeira entrada é inválida, então simplesmente pulo pra próxima 
        
        for linha in iterlinha: ###===>>>> lendo o arquivo de entrada inicial

            line = linha.split(";")
            cod_ativo = line[1]
            lidos += 1
            if gravados == periodoTotal:
                break

            if int(line[0]) >= dataInicio: #mesTeste=="2012":
                if cod_ativo == asset:
                    dateBovespa = line[0]
                    openPrice = line[2] # //PREÇO DE ABERTURA
                    maxPrice = line[3]  #//PREÇO MÁXIMO
                    minPrice = line[4]  #//PREÇO MÍNIMO
                    avgPrice = line[5] # //PREÇO MÉDIO
                    closePrice = line[6]#  //PREÇO DO ÚLTIMO NEGÓCIO
                    bestPrice = line[7] #  //PREÇO DA MELHOR OFERTA DE COMPRA
                    bestBidPrice = line[8] # //PREÇO DA MELHOR OFERTA DE VENDA
                    numTrader = line[9]  #//NÚMERO DE NEGÓCIOS EFETUADOS
                    amountTrader = line[10]  #//QUANTIDADE TOTAL DE TÍTULOS NEGOCIADOS
                    volumeFinanc = line[11]  #// (R$)
                    dadosBovespa = (dateBovespa         + ";" + 
                                    str(openPrice)      + ";" +  
                                    str(maxPrice)       + ";" +  
                                    str(minPrice)       + ";" +  
                                    str(avgPrice)       + ";" +  
                                    str(closePrice)     + ";" + 
                                    str(bestPrice)      + ";" + 
                                    str(bestBidPrice)   + ";" + 
                                    str(numTrader)      + ";" + 
                                    str(amountTrader)   + ";" +  
                                    str(volumeFinanc)
                                    )
                    saida.write(dadosBovespa)  # Grava somente dados coletados da Bovespa
                    gravados +=1


        entrada1.close()
        saida.close()

    saida.close()

    print("Quantidade de Ativos que serão avaliados: ", len(assetsList))

    dataFinal = dadosBovespa[:6]

    return dataFinal



    


