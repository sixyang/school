import matplotlib.pyplot as plt
import numpy as np

def formula(x):
    return 2*x**3 + x ** 2 + x

def Romberg(a, b, e, formula, k=1):
    '''
    龙贝尔格算法
    '''
    h = b - a
    T1 = h/2*(formula(a) + formula(b))

    while True:
        S = 0
        x = a + h/2

        while x < b:
            S = S + formula(x)
            x = x + h

        T2 = 1/2*(T1 + S*h)
        S2 = T2 + 1/3*(T2 - T1)
        
        if k != 1:
            C2 = S2 + 1/15*(S2 - S1)
            if k == 2:
                C1 = C2

            else:
                R2 = C2 + 1/63*(C2 - C1)
                R1 = R2
                if abs(R2 - R1) >= e:
                    R1 = R2 
                    C1 = C2
                else:
                    return R1
            
        T1 = T2
        S1 = S2
        h /= 2
        k += 1
        continue

def trapezoid(a, b, e, formula):
    h = b - a
    T1 = h/2 * (formula(a) + formula(b))
    # T2 = 0

    while True:
        S = 0 
        x = a + h/2
        while x < b:
            S += formula(x)
            x += h
        else:
            T2 = T1/2 + h*S / 2

        
        if abs(T2 - T1) >= e:
            h /= 2
            T1 = T2
            continue
    
        return T2

def draw(a, b):
    ax = plt.gca()
    ax.spines['bottom'].set_position(('data',0))  #data表示通过值来设置x轴的位置，将x轴绑定在y=0的位置
    ax.spines['left'].set_position(('axes',0.5))  #axes表示以百分比的形式设置轴的位置，即将y轴绑定在x轴50%的位置，也就是x轴的中点

    X = np.linspace(a, b)
    Y = [formula(i) for i in X]
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.plot(X, Y, color='green',scalex=True)
    xf = X[np.where((X>a)&(X<b))]
    plt.fill_between(xf,formula(xf),color='blue',alpha=0.25)
    plt.show() 

def main(a, b):
    ret_r = Romberg(a, b, 0.0001, formula)
    ret_t = trapezoid(a, b, 0.0001, formula)
    print("梯形法递推化的结果为： ",ret_t)
    print("龙贝格算法的结果未： ", ret_r)
    draw(a, b)

if __name__ == "__main__":
    main(-5, 5)
