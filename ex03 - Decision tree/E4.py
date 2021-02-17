"""
Oria Segal, 209338193
Ex. 4
"""
from sklearn import tree

from sklearn.model_selection import cross_val_score

import matplotlib.pyplot as plt

from sklearn import datasets
import warnings
warnings.filterwarnings("ignore")


def main(D):
    # to switch between datasets
    if D == 'iris':
        D = datasets.load_iris()
    elif D == 'wine':
        D = datasets.load_wine()
    elif D == 'digits':
        D = datasets.load_digits()

    clf = tree.DecisionTreeClassifier()
    clf.criterion = 'entropy'
    clf = clf.fit(D.data, D.target)

    print("Decision Tree: ")

    accList = []
    for i in range(1, 11):
        clf.max_depth = i
        accuracy = cross_val_score(clf, D.data, D.target, scoring='accuracy', cv=10)
        accList.append(accuracy.mean())
        print("Average Accuracy of DT with depth ", clf.max_depth, " is: ", round(accuracy.mean(), 3))
    X = range(10)
    plt.plot(X, [accList[x] for x in X])
    plt.xlabel("Depth")
    plt.ylabel("Accuracy")
    plt.show()

    preList = []
    for i in range(1, 11):
        clf.max_depth = i
        precision = cross_val_score(clf, D.data, D.target, scoring='precision_weighted', cv=10)
        preList.append(precision.mean())
        print("Average precision_weighted of DT with depth ", clf.max_depth, " is: ", round(precision.mean(), 3))
    X = range(10)
    plt.plot(X, [preList[x] for x in X])
    plt.xlabel("Depth")
    plt.ylabel("Precision")
    plt.show()

    f1List = []
    for i in range(1, 11):
        clf.max_depth = i
        f1 = cross_val_score(clf, D.data, D.target, scoring='f1_weighted', cv=10)
        f1List.append(f1.mean())
        print("Average f1_weighted of DT with depth ", clf.max_depth, " is: ", round(f1.mean(), 3))
    X = range(10)
    plt.plot(X, [f1List[x] for x in X])
    plt.xlabel("Depth")
    plt.ylabel("f1scoure")
    plt.show()

    reList = []
    for i in range(1, 11):
        clf.max_depth = i
        recall = cross_val_score(clf, D.data, D.target, scoring='recall_weighted', cv=10)
        reList.append(recall.mean())
        print("Average recall_weighted of DT with depth ", clf.max_depth, " is: ", round(recall.mean(), 3))
    X = range(10)
    plt.plot(X, [reList[x] for x in X])
    plt.xlabel("Depth")
    plt.ylabel("Recall")
    plt.show()

    print(accList)
    print("The depth(s) with the best accuracy is (are): ")
    m = max(accList)
    print([i for i, j in enumerate(accList) if j == m])


I = 'iris'
W = 'wine'
D = 'digits'

main(D)
