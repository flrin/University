import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.e ** (- (x ** 2))

def summ(n, a):
    suma = 0
    for i in range(1, n):
        suma += f(a + 2*i*a/n)

    return suma

def main():

    n = 10

    # define x and the exponential
    x = np.linspace(-3, 3, 100)
    exp_x = x/n * (f(x) + f(-x) + 2 * summ(n, x))
    pisq = np.sqrt(np.pi) * np.ones_like(x)



    # plot
    plt.plot(x, np.zeros(np.size(x)), '.', label=r"$x$")
    plt.plot(x, exp_x, ".-", label=r"$y=e^(-(x^2))$")
    plt.plot(x, pisq, ".-", label=r"$sqrt(pi)$")

    # tidy the plot
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    #plt.legend(fontsize=16)

    plt.show()

main()