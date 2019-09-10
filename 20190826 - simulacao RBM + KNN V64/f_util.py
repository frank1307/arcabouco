def unirArquivosAno_01():

    caminho = "C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/COTAHIST_A"

    import pandas as pd
    df2 = pd.read_csv(caminho + "2008.txt", header=0)
    print(df2)
    exit(0)

    df1 = pd.concat([pd.read_csv(caminho + "2008.txt", header=0),
                     pd.read_csv(caminho + "2009.txt", header=0),
                     pd.read_csv(caminho + "2010.txt", header=0),
                     pd.read_csv(caminho + "2011.txt", header=0),
                     pd.read_csv(caminho + "2012.txt", header=0),
                     pd.read_csv(caminho + "2013.txt", header=0),
                     pd.read_csv(caminho + "2014.txt", header=0),
                     pd.read_csv(caminho + "2015.txt", header=0),
                     pd.read_csv(caminho + "2016.txt", header=0),
                     pd.read_csv(caminho + "2017.txt", header=0),
                     pd.read_csv(caminho + "2018.txt", header=0)])

    df1.to_csv(caminho + "inicial_2008_a_2018.txt")
  #  print(df1.head(2))

    return

#unirArquivosAno_01()
#exit(0)

def unirArquivos():
    i = 0
    periodo = 2008
    lidosT = 0
    gravadosT = 0

    saida = open("C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/tudao.txt", "w")
    saida.write("data;ativo;openPrice;maxPrice;minPrice;avgPrice;closePrice;bestPrice;bestBidPrice;numTrader;amountTrader;volumeFinanc" + "\n")

    while i <= 10:

        arquivo = open("C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/COTAHIST_A" + str(periodo) + ".txt", "r")

        gravados = 0
        lidos = 0

        for line in arquivo: # lendo o arquivo de entrada inicial
            lidos += 1
            lidosT += 1

            tipo_Mercado = line[25:27]
            cod_ativo = line[12:17]

            #print("linha = ", line, " ativo = ", cod_ativo, " tipo mercado=", tipo_Mercado)


            if tipo_Mercado == '10' and (line[2:6] != "COTA"): #mercado de ações exceto fracionário
             #   print("line", line[2:6])
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

        print(periodo, " Lidos = ", lidos, " Lidos T = ", lidosT, " Gravados = ", gravados, " Gravados T=", gravadosT)
        periodo += 1
        arquivo.close()
       # saida.close()
        i += 1
    saida.close()
    return

def selecionarMercadoAcoes_01():
    i = 0
    periodo = 2008
    lidosT = 0
    gravadosT = 0
    caminho = "C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/"

    while i <= 10:
        saida = open(caminho + str(periodo) + ".txt", "w")
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

        print(periodo, " Lidos = ", lidos, " Lidos T = ", lidosT, " Gravados = ", gravados, " Gravados T=", gravadosT)
        periodo += 1
        arquivo.close()
        saida.close()
        i += 1

    print("==>> Caracterizacao 1")

    return

def selecionarAcoesPorAno_02():
    anos = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]
    caminho = "C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/"
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
            #print(anos[j], df3["ativo"][i], df3["volumeFinanc"][i], float(df4["openPrice"].head(1)), float(df4["closePrice"].tail(1)),  round(variacaoAnoOpenClose,2), "%", round(variacaoAnoMinMax,2), "%")
            saida.write(anos[j] + ";" + df2["ativo"][i] + ";" + str(df2["volumeFinanc"][i]) + ";" + str(float(df4["openPrice"].head(1))) + ";" + str(float(df4["closePrice"].tail(1))) + ";" + str(float(df4["minPrice"].head(1))) + ";" + str(float(df4["maxPrice"].tail(1))) + ";" +  str(round(variacaoAnoOpenClose,2)) + ";" + str(round(variacaoAnoMinMax,2)) + "\n")
            i+=1
        j+=1
    saida.close


    df5 = pd.read_csv(caminho + "caracterizacao1.csv",  sep=";")
    ativosSel = []
    l=0

    while l < len(df2):
        if len(df5.query("ativo =='" + df2["ativo"][l] + "'")) > 10: ## ==>> Selecionando todos os ativos com negociações de 2008 a 2018, ou seja, acima de 10 ocorrências (anos) na lista de ativos
            ativosSel.append(df2["ativo"][l])
        l+=1

    print("total de lidos = ", len(df2))
    print("total de aceitos = ", len(ativosSel))
    print("ativos selecionados= ", ativosSel)


    df9 = [df5[df5["ativo"] == ativosSel[i]].values for i in range(len(ativosSel))]
    arq = open(caminho + "caracterzacao2.csv", "w")
    arq.write("ano;ativo;volumeFinanc;openPrice;closePrice;minPrice;maxPrice;variacaoAnoOpenClose;variacaoAnoMinMax" + "\n")

    for linha in df9:
        for item in linha:
            item = str(item)
            item = item[1:-1]
            item = item.replace("'","")
            item = item.split()
            arq.write("{};{};{};{};{};{};{};{};{}\n".format(*item))

    arq.close()

    print("==>> Caracterizacao 2")
    #df = pd.DataFrame(my_list)#(), columns=list("ativos"))

    #consolidarAcoes_03(pd.DataFrame(ativosSel))
    consolidarAcoes_03(ativosSel)

    return ativosSel


def consolidarAcoes_03(ativosSelecionados):


    print(ativosSelecionados)
    #print("tipo ativos 1", type(ativosSelecionados))
   # exit(0)
   # anos = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"] #, "2018"]
    caminho = "C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/"

    import pandas as pd

    df1 = pd.concat([pd.read_csv(caminho + "2008.txt", parse_dates=["data"], header=0, sep=";"),
                     pd.read_csv(caminho + "2009.txt", parse_dates=["data"], header=0, sep=";"),
                     pd.read_csv(caminho + "2010.txt", parse_dates=["data"], header=0, sep=";"),
                     pd.read_csv(caminho + "2011.txt", parse_dates=["data"], header=0, sep=";"),
                     pd.read_csv(caminho + "2012.txt", parse_dates=["data"], header=0, sep=";"),
                     pd.read_csv(caminho + "2013.txt", parse_dates=["data"], header=0, sep=";"),
                     pd.read_csv(caminho + "2014.txt", parse_dates=["data"], header=0, sep=";"),
                     pd.read_csv(caminho + "2015.txt", parse_dates=["data"], header=0, sep=";"),
                     pd.read_csv(caminho + "2016.txt", parse_dates=["data"], header=0, sep=";"),
                     pd.read_csv(caminho + "2017.txt", parse_dates=["data"], header=0, sep=";"),
                     pd.read_csv(caminho + "2018.txt", parse_dates=["data"], header=0, sep=";")])

    df1["anoMesDia"] = pd.to_datetime(df1["data"]).dt.strftime('%Y%m%d')
    df2 = df1[["anoMesDia", "openPrice"]]
    print(df2.head(4))
    #exit(0)
    df2.to_csv(caminho + "tudao2008a2018.txt", header=1, sep=";")
    #print(df1.head(2))

    #print("tamanho df1=", len(df1))
    exit(0)
    ativosSelecionados = pd.DataFrame(ativosSelecionados)

    #df2 = [df1[df1["ativo"] == ativosSelecionados[0][i]] for i in range(len(ativosSelecionados))]
    #"ativo =='" + df2["ativo"][l] + "'"
    #df3 = (df1.query("ativo =='" + ativosSelecionados[0][i]+ "'" for i in range(len(ativosSelecionados))))
    #df3 = df1.query("ativo =='" + ativosSelecionados[0][i] + "'" for i in range(len(ativosSelecionados)))
    #df3 = pd.DataFrame(df2)

    df1.to_csv(caminho + "tudao2008a2018.csv", header=1, sep=";")
    #print("tipo df3=", df3)
    exit(0)

    #print(df2)
    #df2.to_csv(caminho + "detalhes.csv", header=1, sep=";")
    #print("tam df2=", len(df2))
    #print("tipo df2=", type(df2))
    #import numpy as np
    #df2 = pd.DataFrame(np.array(df2))
    #print("tipo df2 convertido=", type(df2))
    print(df2[1])

    #df2 = pd.DataFrame(df2)
    #print(df2.head(2))

    exit(0)
    #a = ["PETR4",
    #b = pd.DataFrame(a)
    i=0
    #while i < len(df2):
   # teste = df1["ativo"] == ativosSelecionados
  #  print(teste)
    exit(0)
    print("ativos selecionados tipo =", type(ativosSelecionados[1]))
    print("ativos selecionados =", ativosSelecionados[1])
#    df2 = [df1[df1["ativo"] == ativosSelecionados[1]]]
    # ativosSelecionados]] #for i in range(len(ativosSelecionados))]
    #df2 = [df1[df1["ativo"] == a]] #ativosSelecionados]] #for i in range(len(ativosSelecionados))]
    print(df2)
    exit(0)
    df2.to_csv(caminho + "caracterizacao3.csv", header=1, sep=";")
    print("==>> Caracterizacao 3")

    exit(0)

    ## ==>>> Close Price
    import f_grafico
    f_grafico.f_graficoSerieClosePrice2("", df3["closePrice"], df3["data"])
    exit(0)
    return

# print(item)
# print(item[:4], item[6:11], item[12:25], item[26:31], item[31:36], item[36:41], item[41:46], item[46:51])
# item.replace("", ";")
##  arq.write("{}\n".format(item))

#selecionarMercadoAcoes_01()

def jab():
    import  pandas as pd
    my_list = ["ABC", "CDE", "DEF"]
    df = pd.DataFrame(my_list)#(), columns=list("ativos"))
    print(df)

#jab()
#exit(0)
#selecionarAcoesPorAno_02()
#exit(0)
#unirArquivosAcoes_02()

#consolidarAcoesPorAno_03()

#unirArquivos2()
#exit(0)


def selecionarAtivosBovespa():
    import pandas as pd

    caminho = "C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/result/"

    df1 = pd.read_csv(caminho + "dados_2008_a_2018.txt", parse_dates=["data"], header=0, sep=";")

    print(df1[df1["ativo"]=="ABEV3"])
    exit(0)
    df2 = df1.groupby(["ativo"]).sum()
    df2 = df2.sort_values(by="volumeFinanc", ascending=False)
    df2["volumeFinanc"].head(100).to_csv(caminho + "Lista_100_ativos_mais_negociados.csv", header=1, sep=";")
    df3 = pd.read_csv(caminho + "Lista_100_ativos_mais_negociados.csv", sep=";")
    df4 = [df1[df1["ativo"] == df3["ativo"][i]] for i in range(len(df3))]
    pd.concat(df4).to_csv(caminho + "Detalhes_100_ativos_mais_negociados.csv", header=1, sep=";")


    print("Tamanho arq1=", len(df1))
    print("Tamanho arq2=", len(df2))
    print("Tamanho arq3=", len(df3))
    print("Tamanho arq4=", len(df4))

    return



def tratarDados():

    import pandas as pd
    ano = 2008
    caminho = "C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/"
    df = pd.read_csv(caminho + "tudao.txt", parse_dates=["data"], header=0, sep=";")

    print("tam=", len(df))
    df = df.groupby(["ativo"]).sum()

    print("tam=", len(df))
    df = df.sort_values(by="volumeFinanc", ascending=False)

    saida = df["volumeFinanc"].head(100)
    saida.to_csv(caminho + "ativosSelecionados.csv", header=1, sep=";")
    df2 = pd.read_csv(caminho + "ativosSelecionados.csv", sep=";")
    print(df2["ativo"])

    exit(0)

    df["diferenca"] = (df["closePrice"] - df["openPrice"])
    df["percentual"] = (df["diferenca"] *100) / df["closePrice"]
    df["variacao"] = (df["maxPrice"] - df["minPrice"]) / df["maxPrice"]
    df["ano"] = pd.to_datetime(df["data"]).dt.strftime('%Y')
    df["anoMes"] = pd.to_datetime(df["data"]).dt.strftime('%Y%m')

   # round(df,2).to_csv(caminho + str(ano)+ "_dados.csv", header=1, sep=";")

    i=0
    while i <= 10:
        df2 = df[df["ano"] == str(ano)]
        df2 = df2[["ativo", "volumeFinanc", "variacao", "percentual", "ano"]]
        df2 = df2.groupby(["ativo"]).sum()
        df2 = df2.sort_values(by="volumeFinanc", ascending=False)

        ## == >> arredondando com 2 casas decimais
        round(df,2).to_csv(caminho + str(ano) + "_dados.csv", header=1, sep=";")
        round(df2, 2).head(100).to_csv(caminho + str(ano) + ".csv", header=1, sep=";")
        print(str(ano))
        ano += 1
        i += 1
    return

def unirDados ():
    caminho = "C:/Users/dti-01/Desktop/Doutorado 2018/Dados Bovespa/tratados/"
    import pandas as pd

    r = pd.concat([pd.read_csv(caminho + "2008.csv", sep=";"),
     pd.read_csv(caminho + "2009.csv", sep=";"),
     pd.read_csv(caminho + "2010.csv", sep=";"),
     pd.read_csv(caminho + "2011.csv", sep=";"),
     pd.read_csv(caminho + "2012.csv", sep=";"),
     pd.read_csv(caminho + "2013.csv", sep=";"),
     pd.read_csv(caminho + "2014.csv", sep=";"),
     pd.read_csv(caminho + "2015.csv", sep=";"),
     pd.read_csv(caminho + "2016.csv", sep=";"),
     pd.read_csv(caminho + "2017.csv", sep=";"),
     pd.read_csv(caminho + "2018.csv", sep=";")])

    r.to_csv(caminho + "total.csv", header=1, sep=";")
    print("Qtde de ativos duplicados: ", len(r["ativo"]))

    r = r.groupby(["ativo"]).sum()
    r = r.sort_values(by="volumeFinanc", ascending=False)


    print(r.head(20))

    #r = r["ativo"].drop_duplicates()
    return



#unirDados()
#tratarDados()



#unirArquivos()

def tratarArquivoInicial( ):

##
##  Funções:
#  * Selecionar o tipo de mercado de interesse;
#  * Selecionar os códigos de ativos de interesse;
#  * Agrupar os dados da Bovespa / Bloomberg através do atributo (data);e
#  * Gravar um novo arquivo consolidado.
##

    entrada1 = open("arqInicial/tudao2015a2018.txt", "r")
    saida = open("arqInicial/2016a2018.txt", "w")

    lidos = gravados = rejeitados = 0

    for line in entrada1: # lendo o arquivo de entrada inicial
        tipo_Mercado = line[25:27]
        cod_ativo = line [12:17]
        indiceBovespa = line[12:18]
        mesTeste = line[2:6]

        lidos+=1

        if tipo_Mercado == "10":
            if indiceBovespa == "BOVA11":
                line = line.replace("BOVA11","BOVA1 ")
                saida.write(line)  # Grava somente dados coletados da Bovespa
                print (line)
                gravados+=1

            if cod_ativo == "MGLU3" or cod_ativo == "RADL3" or cod_ativo == "KROT3" \
                    or cod_ativo == "MRVE3" or cod_ativo == "BBAS3" \
                    or cod_ativo == "USIM5" or cod_ativo == "PETR4" or cod_ativo == "NATU3" \
                    or cod_ativo == "JBSS3" or cod_ativo == "LAME4" or cod_ativo == "TIMP3" \
                    or cod_ativo=="MGLU3" or cod_ativo=="CMIG3" or cod_ativo=="GGBR4"  :
                saida.write(line)  # Grava somente dados coletados da Bovespa
                gravados+=1
            else:
                rejeitados+=1
        else:
                rejeitados+=1


    entrada1.close()
    saida.close()

    print("  Lidos Bovespa  :", lidos)
    print("  Rejeitados     :", rejeitados)
    print("  Gravados       :", gravados)
    return



def testeDeHipotese(EstrategiaRBM_KNN, EstrategiaComprarSempre, EstrategiaAleatorio, EstrategiaInversa, EstrategiaAlvo05P, EstrategiaAlvo1P, EstrategiaAlvo2P):
    # http://cleverowl.uk/2015/07/01/using-one-way-anova-and-tukeys-test-to-compare-data-sets/
    # O pacote Scipy, oferece dentro de seu submódulo stats, a função pearsonr, que recebe as duas variáveis de interesse como argumentos e retorna o coeficiente de correlação, também conhecido como r e o p-value indicando a probabilidade de que duas variáveis não correlacionadas assumam, ao acaso, valores ao menos tão correlacionados como os de interesses.
    # http://pyscience-brasil.wikidot.com/scipy-stats-pearsonr

    from scipy import stats

    ShapiroWilk = 0.00
    KolmogorovSmirnov = 0.00
    Tstudent = 0.00
    Anova = 0.00
    kruskal = 0.00

    if len(EstrategiaRBM_KNN) >= 3:
        ShapiroWilk       = stats.shapiro(EstrategiaRBM_KNN)[1]
        KolmogorovSmirnov = stats.kstest(EstrategiaRBM_KNN, cdf='norm')[1]
        Tstudent          = stats.ttest_ind(EstrategiaRBM_KNN, EstrategiaComprarSempre)[1]
        Anova             = stats.f_oneway(EstrategiaRBM_KNN, EstrategiaComprarSempre, EstrategiaAleatorio, EstrategiaInversa, EstrategiaAlvo05P, EstrategiaAlvo1P, EstrategiaAlvo2P)[1]
        kruskal           = stats.kruskal(EstrategiaRBM_KNN, EstrategiaComprarSempre, EstrategiaAleatorio, EstrategiaInversa, EstrategiaAlvo05P, EstrategiaAlvo1P, EstrategiaAlvo2P)[1]



    return ShapiroWilk, KolmogorovSmirnov, Tstudent, Anova, kruskal



def testeDeHipoteseAux():
    # http://cleverowl.uk/2015/07/01/using-one-way-anova-and-tukeys-test-to-compare-data-sets/
    # O pacote Scipy, oferece dentro de seu submódulo stats, a função pearsonr, que recebe as duas variáveis de interesse como argumentos e retorna o coeficiente de correlação, também conhecido como r e o p-value indicando a probabilidade de que duas variáveis não correlacionadas assumam, ao acaso, valores ao menos tão correlacionados como os de interesses.
    # http://pyscience-brasil.wikidot.com/scipy-stats-pearsonr

    from scipy import stats

    #### retorno em Percentual de cada Estratégia
    retornoEstrategiaRBM_KNN    =[ 3.85,    0.32,	 1.16,	 0.05,	-0.75,	-0.78,	0.71,  -1.16,  -1.09,	0.40,	 0.23,	0.72]
    retornoEstrategiaInversa    =[-0.51,   -1.47,	 2.87,	-2.98,	 1.20,	-0.53,	2.80,  -0.81,	0.18,	1.14,	 1.49,	1.50]
    retornoEstrategiaAleatoria  =[-0.11,    1.00,	-0.08,	 0.40,	-0.14,	 0.75,  0.50,   1.14,  -2.41,  -2.81,	-2.20,	3.53]
    retornoEstrategiaBuyAndHold =[-1.32,   -1.63,	-2.02,	 2.62,	 0.59,	 0.03, -0.75,  -0.53,	2.80,  -0.81,	 0.18,  2.87]


    print("tipo da variavel = ", type(retornoEstrategiaAleatoria))

    print("T-student             =", stats.ttest_ind(retornoEstrategiaRBM_KNN, retornoEstrategiaBuyAndHold))
    print("Teste Anova           =", stats.f_oneway(retornoEstrategiaRBM_KNN, retornoEstrategiaInversa, retornoEstrategiaAleatoria, retornoEstrategiaBuyAndHold))
    print("Correlação de Pearson =", stats.pearsonr(retornoEstrategiaRBM_KNN, retornoEstrategiaInversa))
    print("Shapiro Wilk          =", stats.shapiro(retornoEstrategiaRBM_KNN))
    print("Kolmogorov-Smirnov    =", stats.kstest(retornoEstrategiaRBM_KNN, 'norm'))

    print("kruskal = ", stats.kruskal(retornoEstrategiaRBM_KNN, retornoEstrategiaAleatoria))
    print("kruskal = ", stats.kruskal(retornoEstrategiaRBM_KNN, retornoEstrategiaBuyAndHold))
    print("kruskal = ", stats.kruskal(retornoEstrategiaRBM_KNN, retornoEstrategiaInversa))
    print("kruskal = ", stats.kruskal(retornoEstrategiaRBM_KNN, retornoEstrategiaRBM_KNN))
    print("kruskal = ", stats.kruskal(retornoEstrategiaBuyAndHold, retornoEstrategiaRBM_KNN, retornoEstrategiaInversa, retornoEstrategiaAleatoria))

    return
#testeDeHipoteseAux()

def f_deletarArquivosTemporarios ():
    import os
    folder = 'arqTotais'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    return



def calcularCustoOperacional (quantidade, precoCompra, precoVenda, precoMaximo, acertou, tipoEstrategia, tipoOperacao, alvo, evolucaoCapitalBruto):

    taxaCorretagem        = 2.49  #fixo em R$
    taxaISS               = 0.12  # 0,12% sobre a taxa de corretagem - R$0,30

    taxaEmolumentos       = 0.0000476
    taxaImpostoRendaFonte = 0.00005
    taxaImpostoRendaVenda = 0.15
    taxaLiquidacao        = 0.000275


    if tipoOperacao == 1: ##=>> Daytrade=1 e Swing=2
     #   print("operacao daytrade")
        taxaEmolumentos       = 0.0000476
        taxaImpostoRendaFonte = 0.00005
        taxaImpostoRendaVenda = 0.2
    else:
        taxaEmolumentos       = 0.0000476
        taxaImpostoRendaFonte = 0.00005
        taxaImpostoRendaVenda = 0.15


    valorCompra = precoCompra * quantidade
    valorVenda  = precoVenda  * quantidade

    ###==>>> Estrategia alvo 1% de ganho
    if tipoEstrategia ==2 and (precoCompra + (precoCompra * alvo) <= precoMaximo):
        valorVenda = valorCompra + (valorCompra * alvo)
        precoVenda = precoCompra + (precoCompra * alvo)


    taxaCorretagem    = taxaCorretagem  + taxaISS

    custoCompraR = taxaEmolumentos  + taxaCorretagem
    taxaEmolumentos = taxaEmolumentos * valorVenda
    taxaLiquidacao = taxaLiquidacao * valorVenda
    taxaImpostoRendaFonte = taxaImpostoRendaFonte * valorVenda
    custoVendaR  = taxaEmolumentos + taxaLiquidacao + taxaCorretagem + taxaImpostoRendaFonte

    if valorVenda > valorCompra:
        acertou ="S"

    custoCompraP     = custoCompraR *100 / valorCompra
    precoMedioCompra = (valorCompra + custoCompraR) / quantidade

    lucroBrutoR = valorVenda - valorCompra


    if lucroBrutoR > 0:

        ##==> Quando a soma do lucro das negociações é menor do que "0", não é cobrado IR
        if evolucaoCapitalBruto > 0:
            impostoRendaF = (lucroBrutoR - (custoCompraR + custoVendaR)) * taxaImpostoRendaVenda
        else:
            diferenca = evolucaoCapitalBruto + lucroBrutoR
            if diferenca >0:
                impostoRendaF = (diferenca - (custoCompraR + custoVendaR )) * taxaImpostoRendaVenda
            else:
                impostoRendaF=0

    else:
        impostoRendaF = 0

    precoMedioVenda = (valorVenda + custoVendaR) / quantidade

    custoOperacionalR = custoCompraR + custoVendaR + impostoRendaF
    custoSemIR = custoCompraR + custoVendaR
    lucroLiquidoR = lucroBrutoR - custoOperacionalR




    ###==>> alterando o lucro bruto pelo liquido quando ocorre prejuízo

    lucroBrutoP       = lucroBrutoR       * 100 / valorCompra
    lucroLiquidoP     = lucroLiquidoR     * 100 / valorCompra
    custoOperacionalP = custoOperacionalR * 100 / valorCompra
    custoSemIRP = custoSemIR * 100/ valorCompra

    if lucroBrutoR <= 0:
        custoOperacionalR = custoOperacionalP = 0

    imprimir=1
    if imprimir ==2:
        print("Valor")

        print("Vlr Compra", str("%.2f" % valorCompra))
        print("Vlr  Venda", str("%.2f" % valorVenda))
        print("")
        print("Preço Compra", str("%.2f" % precoCompra))
        print("Preço  venda", str("%.2f" % precoVenda))
        print("")

        print("taxa de emolumentos", taxaEmolumentos)
        print("taxaImpostoRendafonte =", taxaImpostoRendaFonte )
        print("taxa liquidacao =", taxaLiquidacao)

        print("taxa de corretagem IR R$", str("%.2f" % (taxaCorretagem)))
        print("custo compra R$", str("%.2f" % custoCompraR))
        print("custo  venda R$", str("%.2f" % custoVendaR))
        print("custo IR R$", str("%.2f" % (impostoRendaF)))
        print("custo operacional R$", str("%.2f" % custoOperacionalR))

        print("  ")
        print("lucro bruto   R$", str("%.2f" % lucroBrutoR))
        print("lucro liquido R$", str("%.2f" % lucroLiquidoR))

        print(" ")
        print("lucro bruto %", str("%.2f" % lucroBrutoP))
        print("lucro liquido %", str("%.2f" % lucroLiquidoP))
        print("custo operacional %", str("%.2f" % custoOperacionalP))
    return valorCompra, valorVenda, impostoRendaF, custoOperacionalP, lucroBrutoP,lucroBrutoR,  lucroLiquidoP, lucroLiquidoR, acertou, custoOperacionalR


def normalizarPreco(nomeAtivo, titulo, serieOriginal, qtdeDiasTreino, dataInicio):

##  Tratamento de Dados de Preço
##
##  Este programa recebe uma variável do tipo "numpy array" e realiza a o tratamento da série, retornando 4 variáveis do tipo "listas"
##  da (serieOriginal) (serieLogaritmo) (serieSemOutlier) (serieClusterLogaritmo). Este programa também gera um grafico contendo todas
##  as 4 (quatro) series de preço calculadas.
##

    import f_metricas
    import math
    import numpy as np

    retorno           = f_metricas.medidasDispersaotendencia(serieOriginal)
    serieConvertArray = retorno[10]
    serieLogaritmo    = []

    for i in serieConvertArray:
        if i <=0: # Tratamento e dados <= 0 (print("zero", i))
            i=1

        serieLogaritmo.append(math.log(i,10))

    retorno      = f_metricas.medidasDispersaotendencia(serieLogaritmo)
    media        = retorno[0]
    desvioPadrao = retorno[1]

    serieSemOutlier = []
    for i in serieLogaritmo:
        serieSemOutlier.append((i - media) / desvioPadrao)


    serieClusterLogaritmo = []
    ini             =  0
    fimJanela       = 22

    qtdeCluster = len(serieOriginal) / fimJanela

    j=0
    while j < qtdeCluster:
     #   print("chamando=", serieLogaritmo[ini:fimJanela])
        retorno      = f_metricas.medidasDispersaotendencia(serieLogaritmo[ini:fimJanela])
        media        = retorno[0]
        desvioPadrao = retorno[1]

        for i in serieLogaritmo[ini:fimJanela]:
            if desvioPadrao ==0:
                desvioPadrao=1

            serieClusterLogaritmo.append((i - media) / desvioPadrao)

        ini+=22
        fimJanela+=22
        j+=1

    serieOriginal        = (np.array(serieOriginal))
    serieOriginal.shape  = (len((serieOriginal)),1)

    serieLogaritmo        = (np.array(serieLogaritmo))
    serieLogaritmo.shape  = (len((serieLogaritmo)),1)

    serieSemOutlier       = (np.array(serieSemOutlier))
    serieSemOutlier.shape = (len((serieSemOutlier)),1)

    return (serieOriginal, serieLogaritmo, serieSemOutlier, serieClusterLogaritmo)





def exemploDatas ():
    from datetime import datetime, timedelta
    data1 = "20171231"
    data2 = "20161231"

    ## Converte String em datetime
    a=int(data1[0:4])
    m=int(data1[4:6])
    d=int(data1[6:8])
    data1 = datetime(day=d, month=m, year=a)

    a=int(data2[0:4])
    m=int(data2[4:6])
    d=int(data2[6:8])
    data2 = datetime(day=d, month=m, year=a)

    diferenca = data1-data2

    #hoje = date.today()
    hoje = data1
    intervalo = timedelta(diferenca.days)
    passado = hoje - intervalo

    dataStr1 = passado.strftime('%m/%d/%Y')
    dataStr2 = passado.strftime('%d/%m/%Y')
    dataStr3 = passado.strftime('%Y%m%d')

    print("**** Exemplo de Calculo de Datas*****")
    print("DATA1", data1)
    print("DATA2", data2)
    print("Qtde dias", diferenca.days)
    print("Data atual", hoje)
    print("Data calculada", passado)
    print("DataStr1 ", dataStr1)
    print("DataStr1 ", dataStr2)
    print("DataStr1 ", dataStr3)
    return dataStr1, dataStr2, dataStr3

#exemploDatas()

def diferencaDatas (data1, data2):
    from datetime import datetime

    a=int(data1[0:4]) ## Converte String em datetime
    m=int(data1[4:6])
    d=int(data1[6:8])
    data1 = datetime(day=d, month=m, year=a)

    a=int(data2[0:4])
    m=int(data2[4:6])
    d=int(data2[6:8])
    data2 = datetime(day=d, month=m, year=a)

    diferenca = data1-data2

    print("**** Diferença de Datas *****")
    print("DATA1", data1)
    print("DATA2", data2)
    print("Qtde dias diferença", diferenca.days)

    return diferenca.days

def dataAnterior (data1, qtdeDias):
    from datetime import datetime, timedelta
    print("tipo data" , type(data1))
    a=int(data1[0:4])     ## Converte String em datetime
    m=int(data1[4:6])
    d=int(data1[6:8])
    data1 = datetime(day=d, month=m, year=a)

    hoje = data1

    intervalo = timedelta(qtdeDias)
    passado = hoje - intervalo

    dataStr1 = passado.strftime('%m/%d/%Y')
    dataStr2 = passado.strftime('%d/%m/%Y')
    dataStr3 = passado.strftime('%Y%m%d')

    return dataStr1, dataStr2, dataStr3

def dataPosterior (data1, qtdeDias):
    from datetime import datetime, timedelta
    print("tipo data" , type(data1))
    a=int(data1[0:4])     ## Converte String em datetime
    m=int(data1[4:6])
    d=int(data1[6:8])
    data1 = datetime(day=d, month=m, year=a)

    hoje = data1

    intervalo = timedelta(qtdeDias)
    print( "intervalo", intervalo)
    passado = hoje + intervalo

    dataStr1 = passado.strftime('%m/%d/%Y')
    dataStr2 = passado.strftime('%d/%m/%Y')
    dataStr3 = passado.strftime('%Y%m%d')


    return dataStr1, dataStr2, dataStr3


def dataddmmaaaaa(data1):
    from datetime import datetime, timedelta
   # print("tipo data" , type(data1))
    a=int(data1[0:4])     ## Converte String em datetime
    m=int(data1[4:6])
    d=int(data1[6:8])
    data1 = datetime(day=d, month=m, year=a)
    dataStr2 = data1.strftime('%d/%m/%Y')
    return dataStr2

def imprimirHora():
    from datetime import datetime
    now = datetime.now()
    datahora = str(now.day) + "/" + str(now.month) + "/"+ str(now.year) + "  " + str(now.hour)+ ":"+ str(now.minute)+ ":"+str(now.second)
    return datahora


def baseline( dataInicial, dataFinal, nomeArquivo):
    nomeArquivo = 'arqInicial/ipeadata CDI SELIC IBOVESPA.xls'
    total    =0
    cdi      =0
    selic    =0
    ibovespa =0
    igpm     =0

   # print ("valor ", type(dataInicial), "data final", type(dataFinal))



    for linha in xlread(nomeArquivo):

        if total >0:# controle para retirar o titulo

            if int(linha[0]) >= dataInicial and int(linha[0]) <= dataFinal:
                    cdi      = cdi + float(linha[1])
                    selic    = selic + float(linha[2])
                    ibovespa = ibovespa + float(linha[3])
                    igpm     = igpm + float(linha[4])

        total+=1 # controle para retirar o titulo

    #print("=================")
    qtdeMeses = dataFinal-dataInicial+1
    #print(" Baseline => Período de :", dataInicial, " ate ", dataFinal, " Qtde de Meses:", qtdeMeses)#Data	CDI - (% a.m.)	 Selic - (% a.m.)	Ibovespa (% a.m.)	Inflação - IGP-M - (% a.m.)
   # print("CDI:",cdi)
   # print("SELIC:",selic)
   # print("Ibovespa:",ibovespa)
   # print("IGP-M:",igpm)

    return (cdi, selic, ibovespa, igpm, qtdeMeses)

def xlread(arq_xls):
    import xlrd

    # Abre o arquivo
    xls = xlrd.open_workbook(arq_xls)
    # Pega a primeira planilha do arquivo
    plan = xls.sheets()[0]

    # Para i de zero ao numero de linhas da planilha
    for i in range(plan.nrows):
        # Le os valores nas linhas da planilha
        yield plan.row_values(i)

def tratarData():

    from datetime import datetime

    str_date = '20190623'
    date = datetime.strptime(str_date, '%Y%m%d').date()

    print(date)

    dataLimite = date.fromordinal(date.toordinal() + 30)  # hoje + 45 dias
    print("datalimite=", dataLimite, type(dataLimite))


    #dateAux = datetime.strptime(dataLimite, '%Y-%m-%d').date()
    data2 = date.strftime('%Y%m%d')

    #data2 = datetime.strptime(dataLimite, "%d/%m/%Y")

    print(data2)

    return