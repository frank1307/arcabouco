##
##  Funções:
#  * Ler o arquivos gerado pelo programa P1_coletar;
#  * Calcular o atributo "Classe", onde a Classe =1 caso a diferença entre o ClosePrice(D+1) e o OpenPrice(D+1) seja maior do que o valor "0".
#    Caso contrario a Classe =0;
#  * Calcular o atributo "ClasseAnterior", onde a ClasseAnterior =1 caso a diferença entre o ClosePrice(D-1) e o OpenPrice(D-1) seja maior
#   do que o valor "0". Caso contrario a ClasseAnterior =0;
#
#  * Calcular Indicadores Técnicos de Volume (MFI, SMA Volume, SMA Preço, OBV)
#  * Calcular Indicadores de Defasagem (D3): (caiu, subiu e estavel)
#  * Calcular Indicadores Elliott Wave: (Rompimento, Correção e ContraTendencia)
#
#  * Normalização da série temporal em "0" e "1"
#  * Normalização da série temporal em "Retorno de Log"
#  * Normalização da série temporal em "Retorno de Log com retiradas de ruídos (outliers)"
#  * Normalização da série temporal em "Retorno de Log com retiradas de ruídos (outliers) clsterizada"
#
#  * Gravação da série temporal consolidada (todos os atributos) no formato "0" e "1"
#  * Gravação da série temporal consolidada (todos os atributos) no "Retorno de Log"
#  * Gravação da série temporal consolidada (todos os atributos) no "Retorno de Log com retiradas de ruídos (outliers)"
#  * Gravação da série temporal consolidada (todos os atributos) no "Retorno de Log com retiradas de ruídos (outliers) clsterizada"
#
#  * Gravação da série temporal por categoria de dados:
#  *     somente com dados de preço;
#  *     somente com dados de volume;
#  *     somente com indicadores Bloomberg;
#  *     somente com dados de defasagem D3;
#  *     somente com indicadores Técnicos;
#  *     somente com indicadores Elliott Wave;
#  * Gravação da série temporal completa (preço, volume, Bloomberg, defasagem, indicadores tecnicos, Elliott Wave)
#
#  * Calculo e gravação de dados estatisticos (caracterização da amostra):
#        * Período avaliado (Treino, Teste e Total);
#        * Qtde de classe 0
#        * Qtde de classe 1
#        * data
#        * Qtde de dias
#        * Preços (inicial, medio e final)f
#        * Percentual de classe 0 e 1
##


def ini(asset, nome_arquivo, tipoJanela, periodoTotal, janelaTreino, tipoNormalizacao, dataInicio, qtdeDiasTreino):
        import numpy as np
        import f_util
        import  f_grafico

        print("==>> P2_transformar:", f_util.imprimirHora(), "N=", tipoNormalizacao, "J=", tipoJanela)

        entrada1 = open("arqTotais/" + asset + ".csv", 'r')  # + " - dados agrupados de 2010 a 2016.csv","r")
        saida0   = open("arqTotais/"+nome_arquivo[0],"w")
        dataset  = np.loadtxt(entrada1, delimiter=";")

        if tipoJanela==2:
                dataset = dataset[periodoTotal:]


        dateBovespa   = dataset[:,0:1]
        openPrice     = dataset[:,1:2] # //PREÇO DE ABERTURA
        maxPrice      = dataset[:,2:3]  #//PREÇO MÁXIMO
        minPrice      = dataset[:,3:4]  #//PREÇO MÍNIMO
        avgPrice      = dataset[:,4:5] # //PREÇO MÉDIO
        closePrice    = dataset[:,5:6]  # //PREÇO DO ÚLTIMO NEGÓCIO
        bestPrice     = dataset[:,6:7] #  //PREÇO DA MELHOR OFERTA DE COMPRA
        bestBidPrice  = dataset[:,7:8] # //PREÇO DA MELHOR OFERTA DE VENDA
        numTrader     = dataset[:,8:9]  #//NÚMERO DE NEGÓCIOS EFETUADOS
        amountTrader  = dataset[:,9:10]  #//QUANTIDADE TOTAL DE TÍTULOS NEGOCIADOS
        volumeFinanc  = dataset[:,10:11]  #// (R$)
        retornoFinanc = dataset[:,16:17]


        lidos = qtdeRompimento = qtdeCorrecao = qtdeContraTendencia = 0
        qtdeD3_subiu = qtdeD3_caiu = qtdeD3_estavel = 0

        saida30 = open("arqTotais/" + asset + " JanelaDesl.csv", "w")

        atrib = openPrice

        # Tratamento dos dados de preço

        #tipoNormalizacao = 0
        #kl=0  ##=>> 0=serie original , 1=serie logaritm0, 2=serie logaritmo sem oytilier , 3=serieclusterizada

        openPriceC   = f_util.normalizarPreco(asset, " - Preço Abertura.", openPrice, qtdeDiasTreino, dataInicio)[tipoNormalizacao]
        maxPriceC    = f_util.normalizarPreco(asset, " - Preço Máximo.", maxPrice, qtdeDiasTreino, dataInicio)[tipoNormalizacao]
        minPriceC    = f_util.normalizarPreco(asset, " - Preço Mínimo.", minPrice, qtdeDiasTreino, dataInicio)[tipoNormalizacao]

        closePriceC  = f_util.normalizarPreco(asset, " - Preço Fechamento.", closePrice, qtdeDiasTreino, dataInicio)[tipoNormalizacao]
        numTraderC   = f_util.normalizarPreco(asset, " - Número de Negociações.", numTrader, qtdeDiasTreino, dataInicio)[tipoNormalizacao]

        
        avgPriceC     = f_util.normalizarPreco(asset, " - Preço Médio.", avgPrice, qtdeDiasTreino, dataInicio)[tipoNormalizacao]
        bestPriceC    = f_util.normalizarPreco(asset, " - Melhor Preço", bestPrice, qtdeDiasTreino, dataInicio)[tipoNormalizacao]
        bestBidPriceC = f_util.normalizarPreco(asset, " - Melhor Preco de Compra.", bestBidPrice, qtdeDiasTreino, dataInicio)[tipoNormalizacao]
        amountTraderC = f_util.normalizarPreco(asset, " - Quantidade de Negociações.", amountTrader, qtdeDiasTreino, dataInicio)[tipoNormalizacao]
        volumeFinancC = f_util.normalizarPreco(asset, " - Volume Financeiro.", volumeFinanc, qtdeDiasTreino, dataInicio)[tipoNormalizacao]
#

##==>>> Inicio gerarGraficoVolume(numTrader): ======
##
        numTraderAux =[]
        for cell in numTrader:
                numTraderAux.append(int(cell))

        f_grafico.f_graficoClosePrice(asset, dataInicio, qtdeDiasTreino, closePrice)
##
##==>>> Fim gerarGraficoVolume(numTrader): =====


        i=0
        while i < len(dataset)-1:
                lidos+=1

                
                if (closePrice[i+1] - openPrice[i+1]) > 0:
                #Calculando o Valor de Variação, o Percentual de Variação e o Indicador de Variação  em relação ao Preço de abertura e o Preço de fechamento
                	classe = 1
                else:                                      
                
                	classe = 0


                classeAnterior = closePrice[i-1] - openPrice[i-1] 
                #Calculando o Valor de Variação da classe anterior
                
                if classeAnterior > 0: 

                	classeAnterior = 1
                
                else:                  

                	classeAnterior = 0


                import f_indicadores
                
                if asset != "BOVA1": ### Tratamento para o BOVA11 pois possui mais de 4 caracteres na sua nomenclatura
                        mfi       = f_indicadores.mfi(14, lidos, closePrice, i, minPrice, maxPrice, numTrader)
                        smaPrice  = f_indicadores.sma(14, lidos, atrib, i)
                        smaVolume = f_indicadores.sma(14, lidos, numTrader, i)
                        obv       = f_indicadores.obv(lidos, numTrader, i)

               
                d3 = f_indicadores.defasagemD3(atrib, i)
                d3_subiu   = d3[0]
                d3_caiu    = d3[1]
                d3_estavel = d3[2]

                qtdeD3_caiu    += d3_caiu
                qtdeD3_estavel += d3_estavel
                qtdeD3_subiu   += d3_subiu

                ew = f_indicadores.elliottWave(atrib, i)
                correcao        = ew[0]
                contraTendencia = ew[1]
                rompimento      = ew[2]

                qtdeRompimento      += rompimento
                qtdeCorrecao        += correcao
                qtdeContraTendencia += contraTendencia

                dadosBovespa= ( 
                	str(float(openPriceC[i])) 		+ ";" + 
                	str(float(maxPriceC[i]))  		+ ";" + 
                	str(float(minPriceC[i]))  		+ ";" + \
                	str(float(avgPriceC[i]))  		+ ";" + 
                	str(float(closePriceC[i]))		+ ";" + 
                	str(float(bestPriceC[i])) 		+ ";" + 
                	str(float(bestBidPriceC[i])) 	+ ";" + \
                	str(int(numTraderC[i]))   		+ ";" + 
                	str(int(amountTraderC[i])) 		+ ";" + 
                	str(int(volumeFinancC[i])) 
                	)
                
                dadosBovespa = dadosBovespa.replace(",", ".")
                saida0.write(dadosBovespa + ";" + str(classe) + "\n")



                if (tipoJanela ==2) and (i >= janelaTreino):
                        ##=>> Tratamento dos dados da janela deslizante
                        dadosBovespa= ( 
                        	str(float(openPrice[i]))    + ";" + 
                        	str(float(maxPrice[i]))  	+ ";" + 
                        	str(float(minPrice[i]))     + ";" + \
                        	str(float(avgPrice[i]))    	+ ";" + 
                        	str(float(closePrice[i]))   + ";" + 
                        	str(float(bestPrice[i])) 	+ ";" + 
                        	str(float(bestBidPrice[i])) + ";" + \
                        	str(int(numTrader[i]))   	+ ";" + 
                        	str(int(amountTrader[i])) 	+ ";" + 
                        	str(int(volumeFinanc[i])) 
                        	)

                        dadosBovespa = dadosBovespa.replace(",",".")
                        saida30.write(str(int(dateBovespa[i]))+ ";" +dadosBovespa + ";" + str(classe) + "\n")

                i+=1 #controle de leitura

        entrada1.close()
        saida0.close()
        return qtdeD3_caiu, qtdeD3_estavel, qtdeD3_subiu, qtdeRompimento, qtdeCorrecao, qtdeContraTendencia