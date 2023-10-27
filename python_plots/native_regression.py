from matrix import *
import sys
import matplotlib.pyplot as plt


def main():
    
    data = loadtxt(sys.argv[1])
    
    X = transpose(data)[0]
    Y = transpose(data)[1]
    
    Xp = powers(X, 0, 1)
    Yp = powers(Y, 1, 1)
    Xpt = transpose(Xp)
    
    [[b],[m]] = matmul(invert(matmul(Xpt, Xp)),matmul(Xpt, Yp))
    
    Y2 = [b + m * x for x in X]
    
    plt.plot(X,Y, 'ro')
    plt.plot(X, Y2) 
    plt.show()

if __name__ == "__main__":
    main()



