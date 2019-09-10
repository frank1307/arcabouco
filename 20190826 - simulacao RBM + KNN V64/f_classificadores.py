from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import BernoulliRBM


def RBM(TreinoX, TesteX, TreinoY, TesteY):
    numero_Clusters = 4# 10
    Qtde_Interacao = 200
    rs = 1 #-->> este parametro fixa sempre a mesma semente para gerar o mesmo resultado, caso não seja informado ele vai gerar aleatorio.
    lrRBM = 0.01
    model = BernoulliRBM(n_components=numero_Clusters, n_iter=Qtde_Interacao, random_state=rs, learning_rate=lrRBM)
    model.fit_transform(TreinoX, TreinoY)
    TreinoXS = model.transform(TreinoX)
    TesteXS  = model.transform(TesteX)

   # print("tipoX", type(TesteX))
  #  print("tipoXS", type(TesteXS))
   # print("X", TesteX)
   # print("XS", TesteXS)
   # exit(0)
    return TreinoXS, TesteXS

def KNN(TreinoX, TesteX,  TreinoY, TesteY):
    #clf = neighbors.KNeighborsClassifier(p=2, leaf_size=30, algorithm="fit",n_neighbors=5, weights='uniform', metric='minkowski')
    clf = neighbors.KNeighborsClassifier(n_neighbors=5)
    clf.fit(TreinoX, TreinoY)
    predicao = clf.predict(TesteX)
    return predicao

def svm(TreinoX, TesteX, TreinoY, TesteY):
    Qtde_Interacao2 = 200
    kernelSVM = 'linear' #'rbf'
    rs = 2
    gammaSVM = 0.3
    #clf = SVC(C=1, kernel=kernelSVM, decision_function_shape='ovo', max_iter= Qtde_Interacao2 , random_state=rs , gamma=gammaSVM)

    clf= SVC()
    clf.fit(TreinoX, TreinoY)
    predicao = clf.predict(TesteX)
    return predicao

def naiveBayes(TreinoX, TesteX, TreinoY, TesteY):
    clf = GaussianNB()
    clf.fit(TreinoX, TreinoY)
    predicao = clf.predict(TesteX)
    return predicao

def decisionTree(TreinoX, TesteX,  TreinoY, TesteY):
    clf = DecisionTreeClassifier()
    clf.fit(TreinoX, TreinoY)
    predicao = clf.predict(TesteX)
    return predicao
