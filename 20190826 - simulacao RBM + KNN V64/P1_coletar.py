##
##  Funções:
#  * Selecionar o tipo de mercado de interesse;
#  * Selecionar os códigos de ativos de interesse;
#  * Agrupar os dados da Bovespa / Bloomberg através do atributo (data);e
#  * Gravar um novo arquivo consolidado.
##


def selecionarMercadoAcoes_01():
    i = 0
    periodo = 2008
    lidosT = 0
    gravadosT = 0
    caminho = "C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/"

    saida2 = open(caminho + "result/tudao_2008_a_2018.txt", "w")
    saida2.write("data;ativo;openPrice;maxPrice;minPrice;avgPrice;closePrice;bestPrice;bestBidPrice;numTrader;amountTrader;volumeFinanc" + "\n")

    while i <= 10:
        saida = open(caminho + "result/" + str(periodo) + ".txt", "w")
        saida.write("data;ativo;openPrice;maxPrice;minPrice;avgPrice;closePrice;bestPrice;bestBidPrice;numTrader;amountTrader;volumeFinanc" + "\n")

        arquivo = open(caminho + "COTAHIST_A" + str(periodo) + ".txt", "r")

        gravados = 0
        lidos = 0

        for line in arquivo: # lendo o arquivo de entrada inicial
            lidos += 1
            lidosT += 1

            tipo_Mercado = line[25:27]
            cod_ativo = line[12:17]

            if tipo_Mercado == '10' and (line[2:6] != "COTA"): #mercado de ações exceto fracionário
                gravados += 1
                gravadosT += 1

                dateBovespa = line[2:10]
                openPrice = int(line[57:69]) / 100  # //PREÇO DE ABERTURA
                maxPrice = int(line[70:82]) / 100  # //PREÇO MÁXIMO
                minPrice = int(line[83:95]) / 100  # //PREÇO MÍNIMO
                avgPrice = int(line[96:108]) / 100  # //PREÇO MÉDIO
                closePrice = int(line[109:121]) / 100  # //PREÇO DO ÚLTIMO NEGÓCIO
                bestPrice = int(line[122:134]) / 100  # //PREÇO DA MELHOR OFERTA DE COMPRA
                bestBidPrice = int(line[135:147]) / 100  # //PREÇO DA MELHOR OFERTA DE VENDA
                numTrader = int(line[148:152])  # //NÚMERO DE NEGÓCIOS EFETUADOS
                amountTrader = int(line[153:170])  # //QUANTIDADE TOTAL DE TÍTULOS NEGOCIADOS
                volumeFinanc = int(line[171:188])  # // (R$)

                dadosBovespa = (dateBovespa + ";" + cod_ativo + ";" +
                str(openPrice) + ";" + str(maxPrice) + ";" + str(minPrice) + ";" + str(
                avgPrice) + ";" + str(closePrice) + ";" + str(bestPrice) + ";" + str(bestBidPrice) + ";" + str(
                numTrader) + ";" + str(amountTrader) + ";" + str(volumeFinanc))
                saida.write(dadosBovespa + "\n")
                saida2.write(dadosBovespa + "\n")

        print(periodo, " Lidos = ", lidos, " Lidos T = ", lidosT, " Gravados = ", gravados, " Gravados T=", gravadosT)
        periodo += 1
        arquivo.close()
        saida.close()
        i += 1

    saida2.close()
    print("==>> Caracterizacao 1")
    print("lidos= ", lidosT)
    print("gravados = ", gravadosT)

    return

def selecionarAcoesPorAno_02():
    anos = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]
    caminho = "C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/result/"

    saida = open(caminho + "caracterizacao1.csv", "w")
    saida.write("ano;ativo;volumeFinanc;openPrice;closePrice;minPrice;maxPrice;variacaoAnoOpenClose;variacaoAnoMinMax" + "\n")

    import pandas as pd
    j=0

    while j < len(anos): ##==>> Para cada 1 dos 11 anos
        df1 = pd.read_csv(caminho + anos[j] + ".txt", parse_dates=["data"], header=0, sep=";")
        df2 = df1.groupby(["ativo"]).sum().sort_values(by="volumeFinanc", ascending=False).head(100)
        df2["ativo"] = df2.index

        i=0
        while i < len(df2):
            df4 = df1[(df1["ativo"] == df2["ativo"][i])]
            variacaoAnoOpenClose = (float(df4["closePrice"].tail(1)) - float(df4["openPrice"].head(1))) * 100 / float(df4["openPrice"].head(1))
            variacaoAnoMinMax = (float(df4["maxPrice"].tail(1)) - float(df4["minPrice"].head(1))) * 100 / float(df4["minPrice"].head(1))
            saida.write(anos[j] + ";" + df2["ativo"][i] + ";" + str(df2["volumeFinanc"][i]) + ";" + str(float(df4["openPrice"].head(1))) + ";" + str(float(df4["closePrice"].tail(1))) + ";" + str(float(df4["minPrice"].head(1))) + ";" + str(float(df4["maxPrice"].tail(1))) + ";" +  str(round(variacaoAnoOpenClose,2)) + ";" + str(round(variacaoAnoMinMax,2)) + "\n")
            i+=1
        j+=1
    saida.close


    df5 = pd.read_csv(caminho + "caracterizacao1.csv", sep=";")
    print("==>> Caracterizacao 1 (Gravando todos os ativos)")

    ativosSel = []
    l=0

    while l < len(df2):
        if len(df5.query("ativo =='" + df2["ativo"][l] + "'")) > 10: ## ==>> Selecionando todos os ativos com negociações de 2008 a 2018, ou seja, acima de 10 ocorrências (anos) na lista de ativos
            ativosSel.append(df2["ativo"][l])
        l+=1


    df9 = [df5[df5["ativo"] == ativosSel[i]].values for i in range(len(ativosSel))]
    arq = open(caminho + "caracterizacao2.csv", "w")
    arq.write("ano;ativo;volumeFinanc;openPrice;closePrice;minPrice;maxPrice;variacaoAnoOpenClose;variacaoAnoMinMax" + "\n")

    for linha in df9:
        for item in linha:
            item = str(item)
            item = item[1:-1]
            item = item.replace("'","")
            item = item.split()
            arq.write("{};{};{};{};{};{};{};{};{}\n".format(*item))

    arq.close()

    print("==>> Caracterizacao 2 (Gravando ativos selecionados de 2008 a 2018")
    print("total de lidos = ", len(df2))
    print("total de aceitos = ", len(ativosSel))
    print("ativos selecionados= ", ativosSel)
    print("tipo ativos selecionados= ", type(ativosSel))    #df = pd.DataFrame(my_list)#(), columns=list("ativos"))
    return ativosSel

def consolidarAtivos_03(assetsList):
    caminho = "C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/result/"
    saida   = open(caminho + "tudao_Selecionado_2008_a_2018.txt", 'w')
    saida.write("data;ativo;openPrice;maxPrice;minPrice;avgPrice;closePrice;bestPrice;bestBidPrice;numTrader;amountTrader;volumeFinanc" + "\n")
    gravados = rejeitados = lidos = 0
    k = 0

    while k < len(assetsList):
        print(k+1, "-", assetsList[k])

        ref_arquivo = open(caminho + "tudao_2008_a_2018.txt","r")
        linha = ref_arquivo.readline()

        while linha:
            line = linha.split(";")
            lidos += 1

            if line[1] == assetsList[k]:
                dateBovespa = line[0]
                ativo = line[1]
                openPrice = line[2]
                maxPrice = line[3]
                minPrice = line[4]
                avgPrice = line[5]
                closePrice = line[6]
                bestPrice = line[7]
                bestBidPrice = line[8]
                numTrader = line[9]
                amountTrader = line[10]
                volumeFinanc = line[11]
                dadosBovespa = (dateBovespa + ";" + ativo + ";" + str(openPrice) + ";" +  str(maxPrice) + ";" +  str(minPrice) + ";" +  str(avgPrice) + ";" +  str(closePrice) + ";" + str(bestPrice) + ";" + str(bestBidPrice) + ";" + str(numTrader) + ";" + str(amountTrader) + ";" +  str(volumeFinanc))
                saida.write(dadosBovespa) # +"\n")  # Grava somente dados coletados da Bovespa

                gravados += 1
            else:
                rejeitados += 1

            linha = ref_arquivo.readline()

        k += 1

    print("lidos = ", lidos)
    print("rejeitados = ", rejeitados)
    print("gravados = ", gravados)

    return

def separarAtivo_04(assetsList, dataInicio, periodoTotal):

    print("==>> Relação de Ativos que serão avaliados:")

    k = lidos = gravados = 0

    for asset in assetsList:
        
        print(asset)
        saida    = open("arqTotais/"+ asset + ".csv", 'w')
        entrada1 = open("arqInicial/tudao_Selecionado_2008_a_2018.txt", 'r')
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
                if cod_ativo == assetsList[k]:
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
                    dadosBovespa = (dateBovespa + ";" + str(openPrice) + ";" +  str(maxPrice) + ";" +  str(minPrice) + ";" +  str(avgPrice) + ";" +  str(closePrice) + ";" + str(bestPrice) + ";" + str(bestBidPrice) + ";" + str(numTrader) + ";" + str(amountTrader) + ";" +  str(volumeFinanc))
                    saida.write(dadosBovespa)  # Grava somente dados coletados da Bovespa
                    gravados +=1


        entrada1.close()
        saida.close()

    saida.close()

    print("Quantidade de Ativos que serão avaliados: ", len(assetsList))

    dataFinal = dadosBovespa[:6]

    return dataFinal

# Esse método abre o arquivo tudao_selecionado.csv e separa os ativos e os coloca na pasta arqTotais
# Ao final, retorna o número total de ativos a serem avaliados e a data final

def coletarDadosMetatrader(assetsList, dataInicio, qtdeDiasTreino, qtdeDiasTeste):
    import pandas as pd
    i=0
    while i < len(assetsList):
        df = pd.read_csv("arqInicial/"+assetsList[i]+"Daily.csv", header=None, encoding='utf-16')
        df['Data'] = pd.to_datetime(df[0]).dt.strftime('%Y%m%d')
        df = df.drop(0, axis=1)
        df['r2'] = df[5] * df[6]
        df = df[['Data',1,2,3,4,4,4,4,5,6,'r2']]  #ordenando as colunas e formatando(data,open,hight,low,close,close,close,close,qtde,negoc,volume)
        df = df[(df["Data"] >= str(dataInicio)) & (df['Data'] <= df.iloc[qtdeDiasTreino + qtdeDiasTeste,0]) ]
        df.to_csv("arqTotais/"+assetsList[i]+".csv", header=0, index=None, sep=";")
        i += 1

    dataFinal = "20190225"
    return dataFinal

def coletarDadosIndices(assetsList, dataInicio, qtdeDiasTreino, qtdeDiasTeste):
    import pandas as pd
    i=0
    while i < len(assetsList):
        df = pd.read_csv("arqInicial/"+assetsList[i]+".csv", sep=";")


        from datetime import datetime

        date = datetime.strptime(str(dataInicio), '%Y%m%d').date()

        dataFinal = date.fromordinal(date.toordinal() + (qtdeDiasTeste + qtdeDiasTreino))  # hoje + 45 dias

        dataFinal = dataFinal.strftime('%Y%m%d')

        df = df[(df["Dates"] >= int(str(dataInicio))) & (df['Dates'] <= int(dataFinal)) ]

        df.to_csv("arqTotais/"+assetsList[i]+".csv", header=0, index=None, sep=";")

        i += 1

    return dataFinal


def ini(assetsList, dataInicio, periodoTotal):
    return separarAtivo_04(assetsList, dataInicio, periodoTotal)
    


