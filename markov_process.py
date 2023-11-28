import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# TODO: for question 1b, print out the sequence of states we visit over n simulation steps

def sim_markov_step(transition_matrix, current_state):
    """Simulate one step of a markov process

    Args:
        transition_matrix: matrix of transition probabilities
        current_state: the current state of the process

    Returns:
        next_state: the next state selected in the process

    """
    next_state = np.random.choice([1, 2, 3], p = transition_matrix[current_state - 1])

    return next_state


def t_arrival(transition_matrix, X_0, X_end):
    """Count the waiting time to go from X_0 to X_end given transition matrix P

    Args:
        transition_matrix: matrix of transition probabilities
        current_state: the current state of the process

    Returns:
        t_arrive: time to arrive to X_end

    """
    t_arrive = 0
    while X_0 != X_end:
        X_0 = sim_markov_step(transition_matrix, X_0)
        t_arrive += 1

    return t_arrive

def main():

    # seed for consistency in results
    np.random.seed(342)

    # input our parameters
    P = np.array([[0.2, 0.7, 0.1], [0.2, 0.5, 0.3], [0.2, 0.4, 0.4]])
    X_01 = 1
    X_02 = 2
    X_end = 3
    t_arrive_1 = []
    t_arrive_2 = []
    n_sims = 10000

    # perform simulations
    for n in range(n_sims):
        t_arrive_1.append(t_arrival(P, X_01, X_end))
        t_arrive_2.append(t_arrival(P, X_02, X_end)) 

    # display results of simulation
    print("X_0 = 1 Mean arrival time: {}".format(np.mean(t_arrive_1)))
    print("X_0 = 2 Mean arrival time: {}".format(np.mean(t_arrive_2)))
    
    # plotting
    n_bins = 20

    plt.hist(t_arrive_1, bins = n_bins, alpha = 0.8, label = "$X_0 = 1$", color = "lightskyblue")
    plt.hist(t_arrive_2, bins = n_bins, alpha = 0.4, label = "$X_0 = 2$", color = "violet")
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.title("Time to arrive at $X_n = 3$ starting at $X_0 = 1$ or 2")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()
