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
    
    Y_predicted = [b + m * y for y in Y]
    
    plt.plot(X, Y, 'ro', label='Data')
    plt.plot(X, Y_predicted, 'b-', label='Linear Regression Line')
    plt.legend()
    plt.show()

    if __name__ == "__main__":
        main()



