from numpy import *
import sys
import matplotlib.pyplot as plt

def powers(lista, arg1, arg2):
    li_len = len(lista)
    m_list = []
    new_list = []
    if arg2 < arg1:
        return [[]]
    for num in range(arg1, arg2 + 1):
        a_list = []
        for val in lista:
            a_list.append(val ** num)
        m_list.append(a_list)
        
    return array([list(row) for row in (zip(*m_list))]) # converting to array format
def poly(a, x):
    n = len(a)
    value = 0
    # calculation corresponding to the formula: a0 + a1*x + a2*x2...    
    for i in range(n):
        value += a[i] * (x ** i)
    return value

def main():
    
    data = loadtxt(sys.argv[1])
    n = int(sys.argv[2])
    
    X = transpose(data)[0]
    Y = transpose(data)[1]
    
    Xp  = powers(X,0,n)
    Yp  = powers(Y,1,1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]
    
    n = int((max(X) - min(X)) / 0.2)

    X2 = linspace(min(X), max(X), n).tolist()
    Y2 = [poly(a, x) for x in X2]
        
    plt.plot(X,Y, 'ro')
    plt.plot(X2, Y2) 
    plt.show()

if __name__ == "__main__":
    main()



