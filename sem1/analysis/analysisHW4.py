import math as m
import numpy as np

def get_set_val(n):
    return float(pow(-1, n + 1))/float(n)

def partial_sum_neg(q):
    sum = 0
    for n in range(2, q, 2):
        sum += get_set_val(n)

    return sum

def partial_sum_pos(p):
    sum = 0
    for n in range(1, p, 2):
        sum += get_set_val(n)

    return sum

def main():
    p = int(input("p: "))
    q = int(input("q: "))

    pos_sum = partial_sum_pos(p)
    neg_sum = partial_sum_neg(p)

    print("positive sum: ", pos_sum)
    print("negative sum: ", neg_sum)
    print("whole sum: ", pos_sum + neg_sum)

    print("\nln 2 = ", m.log(2))

main()