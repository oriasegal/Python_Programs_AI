"""
Oria Segal, 209338193
Exercise 5
"""
import math
import csv

# FUNCTIONS: (Functions that'll get called from the main part of the program according to the given questions)

# A function that's calculating the euclidean distance between two points- two rows sent from the file
# by using the sent length. Euclidean distance is equal to the square of the first index raised to the power of
# the second, that's what this function is calculating and returning the distance.
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        distance += pow(num1-num2, 2)  # (num1-num2)^2
    return math.sqrt(distance)

# A function that's calculating the manhattan distance between two points- two rows sent from the file
# by using the sent length. Manhattan distance is equal to the absolute value of the first index minus the second,
# that's what this function is calculating and returning the distance.
def manhattanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        distance += abs(num1 - num2)  # |(num1-num2)|
    return distance

# A function that's calculating the hamming distance between two points- two rows sent from the file
# by using the sent length. Hamming distance is calculated with a counter that's counting the number of not equal parts
# of the sent points, that's what this function is calculating and returning the distance.
def hammingDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        num1 = float(instance1[x])
        num2 = float(instance2[x])
        if num1 != num2:
            distance += 1
    return distance

# A function that is opening a file by a sent name, an operation to read or write and c - the number of rows in the file.
# The function returns a list of the data from the file without the first row (only the values from the file) and makes
# sure that all integers are written as floats.
def openFile(name, rw, c):
    with open(name, rw) as myCsvfile:
        lines = csv.reader(myCsvfile)
        dataWithHeader = list(lines)
    myCsvfile.close()
    dataset = dataWithHeader[1:]

    for j in range(len(dataset)):
        for i in range(c):
            dataset[j][i] = float(dataset[j][i])
    return dataset

# A function that gets called when we need to calculate the euclidean distance between one point and a file with a lot
# of different points in it. In the function we're saving a vector from the file and using the euclidean calculation
# function to return the distance between them. The function is printing the distance and marking the new lable.
def euclidean(p, ds):
    for i in range(len(ds)):
        temp = ds[i]
        label = temp[-1]
        d = euclideanDistance(p, temp, 3)
        obj = distClass()  # one record's distance and tag
        obj.dist = d
        obj.tag = label
        eucDistances.append(obj)

        # question 7:
        print("The euclidean distances between " + str(p) + " and " + str(temp) + " is " + str(d) + " and the label is " + label)

    return eucDistances

# A function that is calculating the knn algorithm- by using a given value if k, the function is searching for the label
# of the nearest k neighbors and setting the new label of the sent point by counting how many 'M' labels and 'F' labels
# are there in all k neighbors of point in the sent data-set list.
def knn(k, distList, p):
    F = 0  # counter for females
    M = 0  # counter for males
    for i in range(k):
        if distList[i][-1] == 'F':
            F += 1
        elif distList[i][-1] == 'M':
            M += 1
    if M > F:
        print("\nIf k=" + str(k) + " the tag on " + str(p) + " is: M")
        return "M"
    elif F > M:
        print("\nIf k=" + str(k) + " the tag on " + str(p) + " is: F")
        return "F"

# A function that is opening a file by using it's sent name and inserting the new values of labels by the sent values
# K1 and K2. The function is writing back into the file the new labels and adding the first top row.
def writeToFile(name, rw, K1, K2):
    with open('myFile_test.csv', 'r') as myCsvfile2:
        lines = csv.reader(myCsvfile2)
        dataWithHeader = list(lines)

    dataWithHeader[1][3] = K1
    dataWithHeader[2][3] = K2

    with open('myFile_test.csv ', 'w', newline='') as myCSVtest:
        writer = csv.writer(myCSVtest)
        writer.writerows([dataWithHeader[0]] + dataWithHeader)

# A function that is similar to the previous one but is built for the second part of the exercise- to write into a file
# that doesn't exists and writing the whole data plus the new labels (and not only the labels like before).
def writeToFile1(name, K, i, data):
    data[i][-1] = K

    with open(name, 'w', newline='') as myCSVtest:
        writer = csv.writer(myCSVtest)
        writer.writerows(data)

# A function that is getting called when needed to calculate the knn value by using a given k number of neighbors.
# The function is calling the previous knn function with a sorted list of the data list that is sent to the function,
# named distList. The function returns the value of the new label for the sent point- p.
def calc(p, distances, j):
    for i in range(len(dataset)):
        distList.append([dataset[i][:-1], distances[i].dist, distances[i].tag])
    distList.sort(key=itemgetter(1))

    K = knn(j, distList, p)
    return K

# A function that gets called when we need to calculate the manhattan distance between one point and a file with a lot
# of different points in it. In the function we're saving a vector from the file and using the manhattan calculation
# function to return the distance between them. The function is printing the distance and marking the new label.
def manhattan(p, ds):
    for i in range(len(ds)):
        temp = ds[i]
        label = temp[-1]
        d = manhattanDistance(p, temp, 3)
        obj = distClass()  # one record's distance and tag
        obj.dist = d
        obj.tag = label
        manDistances.append(obj)

        print("The manhattan distances between " + str(p) + " and " + str(temp) + " is " + str(d) + " and the label is " + label)

    return manDistances

# A function that gets called when we need to calculate the hamming distance between one point and a file with a lot
# of different points in it. In the function we're saving a vector from the file and using the hamming calculation
# function to return the distance between them. The function is printing the distance and marking the new label.
def hamming(p, ds):
    for i in range(len(ds)):
        temp = ds[i]
        label = temp[-1]
        d = hammingDistance(p, temp, 3)
        obj = distClass()  # one record's distance and tag
        obj.dist = d
        obj.tag = label
        hamDistances.append(obj)

        print("The hamming distances between " + str(p) + " and " + str(temp) + " is " + str(d) + " and the label is " + label)

    return hamDistances


# MAIN: (The main part of the program- calling and using all the previous functions)
from operator import itemgetter  # for future use (part 1, question 6)

class distClass:
    dist = -1  # distance of current point from test point
    tag = '-'  # tag of current point


distList = []  # a global list that'll be used in the functions
eucDistances = []  # a global list that'll be used in the functions
manDistances = []  # a global list that'll be used in the functions
hamDistances = []  # a global list that'll be used in the functions
dataset = []


# part 1, question 1:
point = [1, 0, 0, '?']  # an unknown tag
data1 = [1, 1, 1, 'M']
data2 = [1, 2, 0, 'F']

# part 1, question 2:
print("The vector", data1[:-1], "has tag ", data1[-1])
print("The vector", data2[:-1], "has tag ", data2[-1])

# part 1, question 3:
print("The euclidean distance between " + str(data1) + " and " + str(data2) + " is: " + str(euclideanDistance(data1, data2, 3)))

# part 1, question 4:
dataset = openFile('myFile.csv', 'r', 3)
print("\nFirst vector from file is: " + str(dataset[0]))
print("Second vector from file is: " + str(dataset[1]))
print("The euclidean distance between " + str(dataset[0]) + " and " + str(dataset[1]) + " is: "
      + str(euclideanDistance(dataset[0], dataset[1], 3)) + "\n")

# part 1, question 5:
eucDistances = euclidean(point, dataset)

# part 1, question 6:
for i in range(len(eucDistances)):
    distList.append([dataset[i][:-1], eucDistances[i].dist, eucDistances[i].tag])
distList.sort(key=itemgetter(1))

# part 1, question 7:
# is in the euclidean(point) function

# part 1, question 8:
knn(1, distList, point)

# part 1, question 9:
knn(3, distList, point)


# part 2, question 1:
data = openFile('myFile_test.csv', 'r', 3)
dataset = openFile('myFile.csv', 'r', 3)

point1 = data[0]  # first vector from the file
point2 = data[1]  # second vector from the file

eucDistances1 = euclidean(point1, dataset)
K1 = calc(point1, eucDistances1, 3)
eucDistances2 = euclidean(point2, dataset)
K2 = calc(point2, eucDistances2, 3)

writeToFile('myFile_test.csv', 'w', K1, K2)

# part 2, question 2:
data = openFile('mytest.csv', 'r', 29)
dataset = openFile('mytrain.csv', 'r', 29)

# All next are initialized for future use (all part 2 questions)
accE1 = 0  # Value of the accuracy when using euclidean distance and when k=1
accE7 = 0  # Value of the accuracy when using euclidean distance and when k=7
accE19 = 0  # Value of the accuracy when using euclidean distance and when k=19
accM1 = 0  # Value of the accuracy when using manhattan distance and when k=1
accM7 = 0  # Value of the accuracy when using manhattan distance and when k=7
accM19 = 0  # Value of the accuracy when using manhattan distance and when k=19
accH1 = 0  # Value of the accuracy when using hamming distance and when k=1
accH7 = 0  # Value of the accuracy when using hamming distance and when k=7
accH19 = 0  # Value of the accuracy when using hamming distance and when k=19

biggestE = 0  # The biggest value of accuracy when calculating with euclidean distance
biggestM = 0  # The biggest value of accuracy when calculating with manhattan distance
biggestH = 0  # The biggest value of accuracy when calculating with hamming distance

# part 2, question 2, a:
a = 0

for i in range(len(data)):
    p = data[i]
    eucDistances = euclidean(p, dataset)
    K = calc(p, eucDistances, 1)

    writeToFile1('mytest1e.csv', K, i, data)

    if dataset[i][-1] == K:
        a += 1
    accE1 = abs(a / len(dataset))
print("The accuracy when k=1 is: " + str(accE1))

# part 2, question 2, b:
a = 0

for i in range(len(data)):
    p = data[i]
    eucDistances = euclidean(p, dataset)
    K = calc(p, eucDistances, 7)

    writeToFile1('mytest7e.csv', K, i, data)

    if dataset[i][-1] == K:
        a += 1
    accE7 = abs(a / len(dataset))
print("The accuracy when k=7 is: " + str(accE7))

# part 2, question 2, c:
a = 0

for i in range(len(data)):
    p = data[i]
    eucDistances = euclidean(p, dataset)
    K = calc(p, eucDistances, 19)

    writeToFile1('mytest19e.csv', K, i, data)

    if dataset[i][-1] == K:
        a += 1
    accE19 = abs(a / len(dataset))
print("The accuracy when k=19 is: " + str(accE19))

# part 2, question 2, d:
if accE1 > accE7:
    if accE1 > accE19:
        biggestE = accE1
        print("The accuracy when k = 1 is the best.")
if accE7 > accE1:
    if accE7 > accE19:
        biggestE = accE7
        print("The accuracy when k = 7 is the best.")
if accE19 > accE7:
    if accE19 > accE1:
        biggestE = accE19
        print("The accuracy when k = 19 is the best.")

# part 2, question 2, e:
# k = 1
a = 0

for i in range(len(data)):
    p = data[i]
    manDistances = manhattan(p, dataset)
    K = calc(p, manDistances, 1)

    writeToFile1('mytest1m.csv', K, i, data)
    
    if dataset[i][-1] == K:
        a += 1
    accM1 = abs(a / len(dataset))

# k = 7
a = 0

for i in range(len(data)):
    p = data[i]
    manDistances = manhattan(p, dataset)
    K = calc(p, manDistances, 7)

    writeToFile1('mytest7m.csv', K, i, data)
    
    if dataset[i][-1] == K:
        a += 1
    accM7 = abs(a / len(dataset))
    
# k = 19
a = 0

for i in range(len(data)):
    p = data[i]
    manDistances = manhattan(p, dataset)
    K = calc(p, manDistances, 19)

    writeToFile1('mytest19m.csv', K, i, data)
    
    if dataset[i][-1] == K:
        a += 1
    accM19 = abs(a / len(dataset))

# part 2, question 2, f:
#k = 1
a = 0

for i in range(len(data)):
    p = data[i]
    hamDistances = hamming(p, dataset)
    K = calc(p, hamDistances, 1)

    writeToFile1('mytest1h.csv', K, i, data)

    if dataset[i][-1] == K:
        a += 1
    accH1 = abs(a / len(dataset))

# k = 7
a = 0

for i in range(len(data)):
    p = data[i]
    hamDistances = hamming(p, dataset)
    K = calc(p, hamDistances, 7)

    writeToFile1('mytest7h.csv', K, i, data)

    if dataset[i][-1] == K:
        a += 1
    accH7 = abs(a / len(dataset))

# k = 19
a = 0

for i in range(len(data)):
    p = data[i]
    hamDistances = hamming(p, dataset)
    K = calc(p, hamDistances, 19)

    writeToFile1('mytest19h.csv', K, i, data)

    if dataset[i][-1] == K:
        a += 1
    accH19 = abs(a / len(dataset))

# part 2, question 2, g:

# After calculating the biggest accuracy value out of the euclidean distances by the k values, we'll calculate the
# biggest out of the manhattan and hamming distances and also the biggest- the best accuracy combination of all
# distances and k values.

if accM1 > accM7:
    if accM1 > accM19:
        biggestM = accM1
if accM7 > accM1:
    if accM7 > accM19:
        biggestM = accM7
if accM19 > accM7:
    if accM19 > accM1:
        biggestM = accM19

if accH1 > accH7:
    if accH1 > accH19:
        biggestH = accH1
if accH7 > accH1:
    if accH7 > accH19:
        biggestH = accH7
if accH19 > accH7:
    if accH19 > accH1:
        biggestH = accH19

if biggestE > biggestM:
    if biggestE > biggestH:
        if biggestE == accE1:
            i = 1
            print("The best accuracy is " + str(biggestE) + " when using the euclidean function and k=" + str(i))
        if biggestE == accE7:
            i = 7
            print("The best accuracy is " + str(biggestE) + " when using the euclidean function and k=" + str(i))
        if biggestE == accE19:
            i = 19
            print("The best accuracy is " + str(biggestE) + " when using the euclidean function and k=" + str(i))

if biggestM > biggestE:
    if biggestM > biggestH:
        if biggestM == accM1:
            i = 1
            print("The best accuracy is " + str(biggestM) + " when using the manhattan function and k=" + str(i))
        if biggestM == accM7:
            i = 7
            print("The best accuracy is " + str(biggestM) + " when using the manhattan function and k=" + str(i))
        if biggestM == accM19:
            i = 19
            print("The best accuracy is " + str(biggestM) + " when using the manhattan function and k=" + str(i))

if biggestH > biggestE:
    if biggestH > biggestM:
        if biggestH == accH1:
            i = 1
            print("The best accuracy is " + str(biggestH) + " when using the hamming function and k=" + str(i))
        if biggestH == accH7:
            i = 7
            print("The best accuracy is " + str(biggestH) + " when using the hamming function and k=" + str(i))
        if biggestH == accH19:
            i = 19
            print("The best accuracy is " + str(biggestH) + " when using the hamming function and k=" + str(i))
