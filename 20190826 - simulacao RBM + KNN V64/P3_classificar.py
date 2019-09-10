# Funções:
#   * Ler os arquivos gerados pelo programa P2_transformar;
#   * Separar o s arquivos em 2 (dois) conjuntos de dados (Treino e Teste)
#        ou utilizar uma Janela Deslizante
#
#   * Criar 8 classificadores:
#       - SVM
#       - NAIVE BAYES
#       - DECISION TREE
#       - NEIGBORS
#       - RBM + SVM
#       - RBM + NAIVE BAYES
#       - RBM + DECISION TREE
#       - RBM + NEIGBORS
#
#   * Calcular as medidas de desempenho (Predição, Acuracia,f1score e recall)
#
#   * Gravar em arquivos (.csv) as predições para cada dataset avaliado


import numpy as np

def gravarPrevisaoClassificadores(r1,r2,r3,r4,r5,r6,r7,r8, TesteY,saida1):  # -- Grava um arquivo com a previsão dos 12 classificadores
    i=0
    while i < len(TesteY):
       media = (int(r1[i]) + 
       			int(r2[i]) + 
       			int(r3[i]) + 
       			int(r4[i]) + 
       			int(r5[i]) + 
       			int(r6[i]) + 
       			int(r7[i]) + 
       			int(r8[i])
       			) /8  #==>>> calculo da média da predição dos classificadores
       
       if media >= 0.7:
           
           media = 1
       
       else:
           
           media = 0

       saida1.write(str(int(r1[i])) 	+ ";" + 
       				str(int(r2[i])) 	+ ";" + 
       				str(int(r3[i])) 	+ ";" + \
                    str(int(r4[i])) 	+ ";" + 
                    str(int(r5[i])) 	+ ";" + 
                    str(int(r6[i])) 	+ ";" + \
             		str(int(r7[i])) 	+ ";" + 
             		str(int(r8[i])) 	+ ";" + 
             		str(media)      	+ ";" + 
             		str(int(TesteY[i])) + "\n"
             		)
       i=i+1

    saida1.close()
    return

def f_janelaFixa(TreinoX, TesteX, Treinoy, TesteY):
    real = TesteY
    import f_classificadores
    r1 = f_classificadores.svm           (TreinoX, TesteX, Treinoy, TesteY)
    r2 = f_classificadores.naiveBayes    (TreinoX, TesteX, Treinoy, TesteY)
    r3 = f_classificadores.KNN     (TreinoX, TesteX, Treinoy, TesteY)
    r4 = f_classificadores.decisionTree  (TreinoX, TesteX, Treinoy, TesteY)

    retorno = f_classificadores.RBM(TreinoX, TesteX, Treinoy, TesteY)
    TreinoXS = retorno[0]
    TesteXS  = retorno[1]

    r5 = f_classificadores.svm         (TreinoXS, TesteXS, Treinoy, TesteY)    #"RBM+SVM"
    r6 = f_classificadores.naiveBayes  (TreinoXS, TesteXS, Treinoy, TesteY)    #"RBM+NAI"
    r7 = f_classificadores.KNN   (TreinoXS, TesteXS, Treinoy, TesteY)    #"RBM+Nei"
    r8 = f_classificadores.decisionTree(TreinoXS, TesteXS, Treinoy, TesteY)

    return r1, r2, r3, r4, r5, r6, r7, r8, real


def f_janelaDeslizante(janelaTreino, janelaPrevisao, dados, label):
    import numpy as np
    import f_classificadores

    arrayDados = dados.tolist()  # convertendo o tipo (numpy.ndarray) para o tipo (list)
    arrayLabel = label.tolist()
    passo = janelaPrevisao
    i = 0

    r1 = r2 = r3 = r4 = r5 = r6 = r7 = r8 = []
    real = label[janelaTreino:]

    while i < (len(arrayDados) - janelaTreino):
        fimTreino = i + janelaTreino
        iniPrevisao = fimTreino
        fimPrevisao = iniPrevisao + janelaPrevisao

        TreinoX = arrayDados[i:fimTreino]
        TreinoY = arrayLabel[i:fimTreino]
        TesteX = arrayDados[iniPrevisao: fimPrevisao]
        TesteY = arrayLabel[iniPrevisao: fimPrevisao]

        npTreinoX = np.asarray(TreinoX)
        npTreinoY = np.asarray(TreinoY)
        npTesteX = np.asarray(TesteX)
        npTesteY = np.asarray(TesteY)

        r1 = np.concatenate([r1, f_classificadores.svm(npTreinoX, npTesteX, npTreinoY, npTesteY)])
        r2 = np.concatenate([r2, f_classificadores.naiveBayes(npTreinoX, npTesteX, npTreinoY, npTesteY)])
        r3 = np.concatenate([r3, f_classificadores.KNN(npTreinoX, npTesteX, npTreinoY, npTesteY)])
        r4 = np.concatenate([r4, f_classificadores.decisionTree(npTreinoX, npTesteX, npTreinoY, npTesteY)])

        retorno = f_classificadores.RBM(npTreinoX, npTesteX, npTreinoY, npTesteY)
        TreinoXS = retorno[0]
        TesteXS = retorno[1]

        r5 = np.concatenate([r5, f_classificadores.svm(TreinoXS, TesteXS, npTreinoY, npTesteY)])  # "RBM+SVM"
        r6 = np.concatenate([r6, f_classificadores.naiveBayes(TreinoXS, TesteXS, npTreinoY, npTesteY)])  # "RBM+NAI"
        r7 = np.concatenate([r7, f_classificadores.KNN(TreinoXS, TesteXS, npTreinoY, npTesteY)])  # "RBM+Nei"
        r8 = np.concatenate([r8, f_classificadores.decisionTree(TreinoXS, TesteXS, npTreinoY, npTesteY)])

        i = i + passo

    return r1, r2, r3, r4, r5, r6, r7, r8, real



def ini(nome_arquivo, ssaida1, ssaida2, limite, tipoJanela, janelaTreino, janelaTeste):
    import f_util
    import f_metricas
    print("==>> P3_Classificar:", f_util.imprimirHora(), "J=", tipoJanela, "tamanho do arquivo ", len(nome_arquivo))

    qtde=0
    while qtde < len(nome_arquivo):
        saida1 = open("arqTotais/"+ ssaida1[qtde],"w")
        saida2 = open("arqTotais/"+ ssaida2[qtde],"w")

        dataset = np.loadtxt("arqTotais/"+ nome_arquivo[qtde], delimiter=";")

        if tipoJanela ==1:
            TreinoX = dataset[:limite, 0:-2]  # Pega da primeira até a penultima coluna dos dados
            Treinoy = dataset[:limite,   -1]  # Pega apenas a ultima coluna dos dados
            TesteX  = dataset[limite:, 0:-2]
            TesteY  = dataset[limite:,   -1]
            r       = f_janelaFixa(TreinoX, TesteX, Treinoy, TesteY)

        else:
           # import f_janelaDeslizante

            TesteX = dataset[:,0:-2] # Pega da primeira até a penultima coluna dos dados
            TesteY = dataset[:,  -1] # Pega apenas a ultima coluna dos dados
            r = f_janelaDeslizante(janelaTreino, janelaTeste, TesteX, TesteY)

        r1 = r[0]
        r2 = r[1]
        r3 = r[2]
        r4 = r[3]
        r5 = r[4]
        r6 = r[5]
        r7 = r[6]
        r8 = r[7]
        real = r[8]  #gabarito oraculo, ou seja, acertando todos os periodos de alta

        f_metricas.MDgravar(real, r1, "1", saida2)
        f_metricas.MDgravar(real, r2, "2", saida2)
        f_metricas.MDgravar(real, r3, "3", saida2)
        f_metricas.MDgravar(real, r4, "4", saida2)
        f_metricas.MDgravar(real, r5, "5", saida2)
        f_metricas.MDgravar(real, r6, "6", saida2)
        f_metricas.MDgravar(real, r7, "7", saida2)
        f_metricas.MDgravar(real, r8, "8", saida2)

        gravarPrevisaoClassificadores(r1,r2,r3,r4,r5,r6,r7,r8, real, saida1)

        saida2.close()

        qtde += 1