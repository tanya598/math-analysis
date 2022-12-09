import math
import matplotlib.pyplot as plt
import sys
import numpy as np
import sympy as sp

#sys.stdout = open("result.txt", "w")
avergex, avergey = 0, 0
def txt_file(nameoffile):
    inputdata = []
    input = open(nameoffile)
    input.seek(1)
    for line in input:
        inputdata.append(input.read(3))
        input.read(1)
        inputdata.append(input.read(2))
    for i in range(int(len(inputdata))):
        inputdata[i] = inputdata[i].replace(',', '.')
    data = [[0 for i in range(2)] for j in range(int(len(inputdata) / 2))]
    index0 = 0
    index1 = 0
    for i in range(int(len(inputdata))):
        if i % 2 == 0:
            data[index0][0] = float(inputdata[i])
            index0 += 1
        elif i % 2 != 0:
            data[index1][1] = int(inputdata[i])
            index1 += 1
    return data

nameoffile = input('Вкажіть імя файлу:')
data = txt_file(nameoffile)
data = sorted(data)
print("Послідовність:", data)
print('----------------Завдання 1----------------')
def dataX(data):
    inputdatadata = []
    for i in range(len(data)):
        inputdatadata.append(data[i][0])
    return inputdatadata

def dataY(data):
    inputdatadata = []
    for i in range(len(data)):
        inputdatadata.append(data[i][1])
    return inputdatadata

def trend(data):
    if max(data)==data[len(data)-1]:
        print("Тренд позитивний")
    elif min(data)==data[len(data)-1]:
        print("Тренд негативний")
    else:
        print("Дані не мають тренду")


#--------------Task 2--------------------------

def Task2(x, y):
    global avergex, avergey
    covarience = 0.0
    for i in range(len(x)):
        avergex += x[i]
        avergey += y[i]
    averagex = avergex / len(x)
    averagey = avergey / len(y)
    for i in range(len(x)):
        covarience += (x[i] - averagex) * (y[i] - averagey)
    covarience = covarience / (len(x)-1)
    print('------------------------------------------')
    print(' ')
    print('----------------Завдання 2----------------')
    print('Коваріація: ', covarience)
#-----------------------------------------------

#--------------Task 4--------------------------
def Task4(x, y):
    global avergex, avergey
    correlation, sum1, sum2, sum3 = 0.0, 0.0, 0.0, 0.0
    for i in range(len(X)):
        sum1 = (x[i] - avergex) * (y[i] - avergey)
        sum2 = (x[i] - avergex) * (x[i] - avergex)
        sum3 = (y[i] - avergey) * (y[i] - avergey)
    sum2 += sum2 * sum3
    correlation = sum1/math.sqrt(sum2)
    print('------------------------------------------')
    print(' ')
    print('----------------Завдання 4----------------')
    print("Кореляція: ", correlation)
    print('------------------------------------------')
#------------------------------------------------


#--------------Task 3--------------------------
def Task3(x, y ):
    global avergex, avergey
    byx, sumxy, sumx, sumy, sumx2, sumy2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

    for i in range(len(x)):
        sumx += x[i]
        sumy += y[i]
        sumxy += x[i] * y[i]
        sumx2 += x[i] * x[i]
        sumy2 += y[i] * y[i]
    byx = (len(x) * sumxy - (sumx * sumy)) / (len(x) * sumx2 - sumx2)
    x, y = sp.symbols("x, y")
    line = sp.Eq(y-avergey, byx * (x - avergex))
    linex = sp.solve(line, y)
    liney = sp.solve(line, x)
    print("x = ", linex)
    print("y = ", liney)
    return liney
#-------------------------------------------------

def line(data):
    dobXY = 0
    sumX = 0
    sumY = 0
    sumdobXX = 0
    for i in range(len(data)):
        dobXY += data[i][0]*data[i][1]
        sumX += data[i][0]
        sumY += data[i][1]
        sumdobXX += data[i][0] ** 2


    b = (len(data) * dobXY - (sumX * sumY)) / ((len(data) * sumdobXX) - sumX**2)

    x = np.linspace(0, 9)
    y = b*(x - np.mean(dataX(data))) + np.mean(dataY(data))

    X = dataX(data)
    Y = dataY(data)
    plt.scatter(X, Y, marker="*", s=100, color="gold", label="unit of data")
    plt.legend()
    plt.plot(x, y, color = "mediumslateblue")
X = dataX(data)
Y = dataY(data)

line(data)
plt.xlabel("вісь X")
plt.ylabel("вісь Y")
plt.title('Діаграма розкиду даних ')
plt.grid()
trend(data)
plt.show()
Task2(X, Y)
print('------------------------------------------')
print(' ')
print('----------------Завдання 3----------------')
Task3(X, Y)
Task4(X, Y)








































#sys.stdout.close()

# # sys.stdout = open("result3lab.txt", "w")
# avergex, avergey = 0, 0
# def connect_txt(nameoffile):
#     inputdata = []
#     input = open(nameoffile)
#     input.seek(1)
#     for line in input:
#         inputdata.append(input.read(3))
#         input.read(1)
#         inputdata.append(input.read(2))
#     for i in range(int(len(inputdata))):
#         inputdata[i] = inputdata[i].replace(',', '.')
#     data = [[0 for i in range(2)] for j in range(int(len(inputdata) / 2))]
#     index0 = 0
#     index1 = 0
#     for i in range(int(len(inputdata))):
#         if i % 2 == 0:
#             data[index0][0] = float(inputdata[i])
#             index0 += 1
#         elif i % 2 != 0:
#             data[index1][1] = int(inputdata[i])
#             index1 += 1
#     return data
#
# nameoffile = input('Name of file:')
# data = connect_txt(nameoffile)
# data= sorted(data)
# print('-------------Task 1--------------')
# def dataX(data):
#     inputdatadata = []
#     for i in range(len(data)):
#         inputdatadata.append(data[i][0])
#     return inputdatadata
#
# def dataY(data):
#     inputdatadata = []
#     for i in range(len(data)):
#         inputdatadata.append(data[i][1])
#     return inputdatadata
#
# def trend(data):
#     if max(data)==data[len(data)-1]:
#         print("trend positive")
#     elif min(data)==data[len(data)-1]:
#         print("trend negative")
#     else:
#         print("data does not trend")
#
# # print('----------------------------------')
#
# #-----------------------------------------------
# #2----------------------------------------------
# def task2(x, y):
#     global avergex, avergey
#     covarience = 0.0
#     for i in range(len(x)):
#         avergex += x[i]
#         avergey += y[i]
#     averagex = avergex / len(x)
#     averagey = avergey / len(y)
#     for i in range(len(x)):
#         covarience += (x[i] - averagex) * (y[i] - averagey)
#     covarience = covarience / (len(x)-1)
#     print(' ')
#     print('-------------Task 2--------------')
#     print('Covarince: ', covarience)
#
# def task4(x, y):
#     global avergex, avergey
#     correlation, sum1, sum2, sum3 = 0.0, 0.0, 0.0, 0.0
#     for i in range(len(X)):
#         sum1 = (x[i] - avergex) * (y[i] - avergey)
#         sum2 = (x[i] - avergex) * (x[i] - avergex)
#         sum3 = (y[i] - avergey) * (y[i] - avergey)
#     sum2 += sum2 * sum3
#     correlation = sum1/math.sqrt(sum2)
#     print("Correlation: ", correlation)
#
# def task3(x, y ):
#     global avergex, avergey
#     byx, sumxy, sumx, sumy, sumx2, sumy2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#
#     for i in range(len(x)):
#         sumx += x[i]
#         sumy += y[i]
#         sumxy += x[i] * y[i]
#         sumx2 += x[i] * x[i]
#         sumy2 += y[i] * y[i]
#     byx = (len(x) * sumxy - (sumx * sumy)) / (len(x) * sumx2 - sumx2)
#     x, y = sp.symbols("x, y")
#     line = sp.Eq(y-avergey, byx * (x - avergex))
#     linex = sp.solve(line, y)
#     liney = sp.solve(line, x)
#
#     print("x = ", liney)
#     print("y = ", linex)
#
#
#
#
#
# #input_100.txt
# X = dataX(data)
# Y = dataY(data)
# area = 100
# plt.scatter(X, Y, marker="*", s=area, color="purple" )
# plt.xlabel("вісь X")
# plt.ylabel("вісь Y")
# plt.title('Діаграма розкиду даних ')
# plt.grid()
# # plt.plot([min(X), min(Y)], [max(X), max(Y)],  color = 'r')
# trend(data)
# plt.show()
# task2(X, Y)
# task3(X, Y)
# task4(X, Y)
# # sys.stdout.close()

# ---------------------------------------------------------
# x = [2.50, 1.23, 4.02, 3.25, 5.00, 4.40, 1.5]
# y = [34, 62, 49, 22, 13, 19, 24]
# x1 = [1, 2, 4, 3.5, 4.7, 2.40, 2.7]
# y1 = [30, 50, 41, 28, 53, 39, 45]
# x2 = [1.5, 2.7, 4.6, 3.9, 1.2, 3.7, 4.5]
# y2 = [10, 22, 36, 46, 14, 44, 49]
# colors = (0,1,0)
# colors1 = (0,0,1)
# colors2 = (1,0,0)
# area = 100
# plt.scatter(x, y, marker="d", s=area, c=colors, label="d" )
# plt.scatter(x1, y1, marker="x", s=area, c=colors1,label="x" )
# plt.scatter(x2, y2, marker="*", s=area, c=colors2,label="*")
# leg = plt.legend(loc='center left')
# plt.xlabel("вісь X")
# plt.ylabel("вісь Y")
# plt.title('Task 6.4: Діаграма розкиду даних ')
# plt.show()