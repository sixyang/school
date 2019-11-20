import matplotlib.pyplot as plt
import numpy as np


def formula(x, y):
    return -y - x * y ** 2

def r_formula(x):
    return 1/(2 * np.exp(x) - x - 1)

def euler(x, y, h, N, formula ,n=1):
    '''欧拉公式'''
    while n <= N:
        x1 = x + h
        y1 = y + h * formula(x, y)
        yield (x1, y1)
        n += 1
        x = x1
        y = y1

def improved_euler(x, y, h, N, formula, n=1):
    '''改进欧拉法'''
    while n <= N:
        x1 = x + h
        yp = y + h * formula(x, y)
        yc = y + h * formula(x1, yp)
        y1 = 1/2 * (yp + yc)
        yield (x1, y1)
        n += 1
        x = x1
        y = y1

def longku(x, y, h, N, formula, n=1):
    '''四阶龙格库塔法'''
    while n <= N:
        x1 = x + h
        K1 = formula(x, y)
        K2 = formula(x+h/2, y+h/2*K1)
        K3 = formula(x+h/2, y+h/2*K2)
        K4 = formula(x1, y+h*K3)
        y1 = y + h/6*(K1 + 2*K2 + 2*K3 + K4)
        yield x1, y1
        n += 1
        x = x1
        y = y1



def main(a, b):

    #欧拉法
    X = []
    Y = []
    for i in euler(a, 1, 0.1, 10*b, formula):
        X.append(i[0])
        Y.append(i[1])
    plt.plot(X, Y, color='black')

    #改进欧拉法
    X1 = []
    Y1 = []
    for i in improved_euler(a, 1, 0.1, 10*b, formula):
        X1.append(i[0])
        Y1.append(i[1])
    plt.plot(X1, Y1, color='red')

    #四阶龙格库塔法
    X2 = []
    Y2 = []
    for i in improved_euler(a, 1, 0.1, 10*b, formula):
        X2.append(i[0]+0.1)             #为了方便观看，特地每个值加0.1！
        Y2.append(i[1])
    plt.plot(X2, Y2, color='green')

    #标准公式
    X3 = np.linspace(a, b)
    Y3 = [r_formula(x) for x in X3]
    plt.plot(X3, Y3, color='yellow')

    plt.show()

if __name__ == "__main__":
    main(0, 5)
