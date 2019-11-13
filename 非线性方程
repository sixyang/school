import matplotlib.pyplot as plt
import numpy as np


def raw_formula(x):
    return x**3 - x - 1

def derivatives(x):
    return 3*x ** 2 -1


def dichotomy(left, right, eps):
    middle = (left+right)/2
    count = 0
    while abs(raw_formula(middle)) > eps:
        middle = (left+right)/2
        if raw_formula(left)*raw_formula(middle) <= 0:
            right = middle
        else:
            left = middle
        count = count+1
    return count, middle


def Newton(x,eps):
    count=0
    while abs(raw_formula(x))>eps:
        x=x-raw_formula(x)/derivatives(x)
        count=count+1
    return count,x

def xian(x0):
    # x0 = 1
    # x1 = 1.655889
    x1 = 0
    f0 = raw_formula(x0)
    f1 = raw_formula(x1)
    times = 0
    while(np.abs(x1-x0)>1e-5):
        times += 1
        x2 = x1 - f1*(x1-x0)/(f1-f0)
        x0,x1 = x1,x2
        f0,f1 = f1,raw_formula(x1)
    return times, x2


def main(a, b):

    #使用二分法求解
    count, value = dichotomy(a, b, 0.00001)
    print("二分法 得到根为 {}".format(value))

    #使用牛顿迭代法求解
    count1, value1 = Newton(a, 0.00001)
    print("牛顿迭代法 得到根为 {}".format(value1))

    #使用弦截法求解
    count2, value2 = xian(0.5)
    print("弦截法 得到的根为 {}".format(value2))

    X = np.linspace(a, b)
    Y = [raw_formula(x) for x in X]
    plt.plot(X, Y, color='blue')
    plt.show()

if __name__ == "__main__":
    main(0, 10)
