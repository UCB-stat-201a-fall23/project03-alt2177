import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():

    P = np.array([[0.2, 0.7, 0.1], [0.2, 0.5, 0.3], [0.2, 0.4, 0.4]])
    X_0 = 1
    X_1 = np.random.choice([1, 2, 3], p = P[X_0])
    print("Next state: {}".format(X_1))


if __name__ == "__main__":
    main()
