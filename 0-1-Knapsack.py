import numpy as np
import matplotlib.pyplot as plt
import time
import random

def knapsack(rows, columns, values, weights ):
    start = time.time()

    table = np.zeros((rows+1, columns+1))

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):

            table[i, j] = table[i-1, j]

            if weights[i-1] <= j:

                table[i , j] = max(table[i-1, j], values[i-1] + table[i-1, j - weights[i-1]] )

    end = time.time()

    total_time = end - start
    return table[rows,columns], total_time


def test_cases(cap, copies, max_num_values, max_val, max_weight):

    number_of_values = []

    times = []
    capacitties = []

    for i in range(copies):
        capacity  = random.randrange(1,cap)
        num_values = random.randrange(1,max_num_values)

        capacitties.append(capacity)

        values = []
        weights = []
    
        for i in range(num_values):
            val = random.randrange(1,max_val) 
            weight = random.randrange(1,max_weight) 
            values.append(val)
            weights.append(weight)

        max_profit, time_taken = knapsack(len(values), capacity, values, weights)

        number_of_values.append(len(values))

        times.append(time_taken)

    plt.plot(number_of_values, times, 'o')

    plt.xlabel('Number of Items')

    plt.ylabel('Time')

 

    plt.show()

#test_cases(200, 1000, 3000, 400, 200)

#print(knapsack(6,60,[20,1,4,13,40,6],[15,12,5,6,20,10])[0])


    