import f_util
import P1_coletar
import P2_transformar
import P3_classificar
import P4_operar
import P5_analisar

assetsList = [  'PETR4', 'VALE3', 'BBDC4', 'BBAS3', 'PETR3', 'ITSA4', 'GGBR4', 
				'USIM5', 'LREN3', 'RENT3', 'CMIG4', 'GOAU4', 'CCRO3', 'LAME4', 
				'CSNA3', 'JBSS3','BRKM5', 'EMBR3', 'ELET3', 'BRAP4', 'BBDC3', 
				'GOLL4', 'NATU3', 'CSAN3','BVMF3', 'ELET6', 'SBSP3', 'MRVE3', 
				'ENBR3', 'CYRE3', 'PSSA3', 'BRSR6', 'CESP6', 'MRFG3', 'CPLE6'
				]



horaInicio          = f_util.imprimirHora()

dataInicio          = 20170601  #OK
qtdeDiasTreino      = 21
qtdeDiasTeste       = 30  #745 #486   # 30  ou 132 ou 243  729
tipoEstrategia      = 1   #=> 1=compra Open e vende em Close  ///// 2= alvo de 1%

volumeNegociado     = 1000
janelaTreino        = 20
janelaTeste         = 1   #Fixo em 1 ok

tipoJanela          = 2   ###  1=Janela Fixa e 2=Janela Deslizante
tipoNormalizacao    = 3   ##=>> 0=serie original , 1=serie logaritmo, 2=serie logaritmo sem outlier , 3=serieclusterizada
qtdeClassificadores = 10  # quantidade de classiciadores

periodoTotal        = qtdeDiasTreino + qtdeDiasTeste +1 #=>> o 1 é para tratar o erro do proximo campo

print("===================================================")
print("              configuração Inicial ")
print("===================================================")
print("Data Início    =", dataInicio)
print("Qtde Dias Treino=", qtdeDiasTreino)
print("Qtde Dias Teste =", qtdeDiasTeste)
print("Período Total Avaliado  =", qtdeDiasTreino + qtdeDiasTeste)
print("===================================================")
print("==>> Menu Inicial:", f_util.imprimirHora())
print("periodo total=", periodoTotal)



dataFinal = (P1_coletar.ini(assetsList, int(dataInicio), periodoTotal))

if tipoJanela == 2:
        periodoTotal = qtdeDiasTreino - janelaTreino

for asset in assetsList:
    print("Nome Ativo:", asset)
    print("==>> Menu Principal:", f_util.imprimirHora())

    dataset  = [asset + " D01 Bov.csv"]
    dataset2 = [asset + " PD D01 Bov.csv"]
    dataset3 = [asset + " MD D01 Bov.csv"]

    retornoP2 = P2_transformar.ini( asset, 
    								dataset, 
    								tipoJanela, 
    								periodoTotal, 
    								janelaTreino, 
    								tipoNormalizacao, 
    								str(dataInicio),  
    								qtdeDiasTeste
    							) 
    P3_classificar.ini( dataset, 
    					dataset2, 
    					dataset3, 
    					qtdeDiasTreino, 
    					tipoJanela, 
    					janelaTreino, 
    					janelaTeste
    				)
    P4_operar.ini(  asset,
    				dataset2, 
    				tipoJanela,  
    				tipoNormalizacao, 
    				str(dataInicio), 
    				int(str(dataInicio)[:6]), 
    				int(dataFinal[:6]), 
    				qtdeClassificadores, 
    				0, tipoEstrategia, 
    				volumeNegociado, 
    				retornoP2)
    
    P5_analisar.ini(dataInicio, asset, qtdeDiasTeste)


#P5_analisar.gerarTabelaConsolidada(qtdeDiasTeste, assetsList)


print("==>> Término Menu Principal <<===")
print("Hora Início: ", horaInicio)
print("Hora Fim   : ", f_util.imprimirHora())
