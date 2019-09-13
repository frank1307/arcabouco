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


entryFile= "arqInicial/tudao_Selecionado_2008_a_2018.txt"


horaInicio          = f_util.imprimirHora()

dataInicio          = 20170601  #OK
qtdeDiasTreino      = 21
qtdeDiasTeste       = 30 
# 30
# 132
# 243
# 729

tipoEstrategia      = 1   
# 1 = compra Open e vende em Close 
# 2 = Alvo de 1%

volumeNegociado     = 1000
janelaTreino        = 20
janelaTeste         = 1   
#Fixo em 1 ok

tipoJanela          = 2   
# 1 = Janela Fixa
# 2 = Janela Deslizante


tipoNormalizacao    = 3   
# 0 = serie original 
# 1 = serie logaritmo
# 2 = serie logaritmo sem outlier
# 3 = serieclusterizada


qtdeClassificadores = 10  
# quantidade de classiciadores

periodoTotal        = qtdeDiasTreino + qtdeDiasTeste +1 
# Segundo comentário original, esse 1 era pra tratar algum tipo de erro do próximo campo 

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



dataFinal = (P1_coletar.separarAtivo( assetsList,        #lista de ativos
                                      int(dataInicio),   #A partir de que data os testes serão realizado
                                      periodoTotal,      # Tempo total do teste
                                      entryFile)         # Nome do arquivo onde serão separados os dados
                                    )
#data final é uma string no formato "ano"+"mes"
#   separarAtivo pega os dados iniciais de um arquivo com entradas
#   data;ativo;openPrice;maxPrice;minPrice;avgPrice;closePrice;bestPrice;bestBidPrice;numTrader;amountTrader;volumeFinanc
#   e os coloca separados por ativo/arquivo na pasta arqTotais 




if tipoJanela == 2:
        periodoTotal = qtdeDiasTreino - janelaTreino

for asset in assetsList:
    print("Nome Ativo:", asset)
    print("==>> Menu Principal:", f_util.imprimirHora())

    dataset  = [asset + " D01 Bov.csv"]
    dataset2 = [asset + " PD D01 Bov.csv"]
    dataset3 = [asset + " MD D01 Bov.csv"]

    retornoP2 = P2_transformar.ini( asset,                  # ativo a ser analisado
    								dataset,                # nome do arquivo modificado
    								tipoJanela,             #ver acima
    								periodoTotal,           # o tempo total de testes
    								janelaTreino,           #tamanho da janela de treino
    								tipoNormalizacao,       # ver acima
    								str(dataInicio),        # data de início
    								qtdeDiasTeste           #quantidade de dias de teste
    							) 
    #lê os dados de asset.csv, os normaliza e coloca em "arqTotais/"+ asset+ "D01 Bov.csv"
    # Parara cada dia, uma entrada com 
    #       Preço de abertura
    #       Preço Máximo
    #       Preço Médio
    #       Preço de fechamento
    #       Melhor preço
    #       Melhor preço(bid)
    #       Número de trades
    #       Volume de trade
    #       Volume financeiro 
    #       Atributo classe definido no começo do arquivo P2_transformar


    # no caso de janela deslizante, coloca os dados da janela em "arqTotais/" + asset + " JanelaDesl.csv"
        # Mesma configuração anterior, mas com a data na frente pra janela

    P3_classificar.ini( dataset,            #VER CONFIGURAÇÃO ACIMA
    					dataset2,           #VER CONFIGURAÇÃO ACIMA
    					dataset3,           #VER CONFIGURAÇÃO ACIMA
    					qtdeDiasTreino,     #QUANTIDADE DE DIAS DE TREINO
    					tipoJanela,         #VER ACIMA
    					janelaTreino,       #TAMANHO DA JANELA DE TREINO
    					janelaTeste         #TAMANHO DA JANELA DE TESTE
    				)
    #Grava em "asset" + " PD D01 Bov.csv" as previsões de 12 classificadores
    #Grava em "asset" + " MD D01 Bov.csv" as medidas de desempenho   


    P4_operar.ini(  asset,
    				dataset2, 
    				tipoJanela,  
    				tipoNormalizacao, 
    				str(dataInicio), 
    				int(str(dataInicio)[:6]), 
    				int(dataFinal[:6]), 
    				qtdeClassificadores, 
                    tipoEstrategia, 
    				volumeNegociado, 
    				retornoP2)

    # Coloca as operações na pasta arqtotais em alguns arquivos

    P5_analisar.ini(dataInicio, asset, qtdeDiasTeste)

    #analise e gera o extrato das operações na pasta resultados

P5_analisar.gerarTabelaConsolidada(qtdeDiasTeste, assetsList)
    #gera as imagens na pasta img
'''
print("==>> Término Menu Principal <<===")
print("Hora Início: ", horaInicio)
print("Hora Fim   : ", f_util.imprimirHora())
