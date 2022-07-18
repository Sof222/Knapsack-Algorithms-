import numpy as np
import matplotlib.pyplot as plt
import time
import random



def knapsack(rows, columns, values, weights, c):

    weights_c = []
    values_c = []

    for i in range(rows):
        for j in range(1,c+1):
            weights_c.append(weights[i] )
            values_c.append(values[i] )

    start = time.time()

    table = np.zeros((len(weights_c)+1, columns+1))

    for i in range(1, len(weights_c) + 1):
        for j in range(1, columns + 1):

            table[i, j] = table[i-1, j]

            if weights_c[i-1] <= j:
                
                table[i , j] = max(table[i-1, j], values_c[i-1] + table[i-1, j - weights_c[i-1]] )


    end = time.time()

    total_time = end - start

    return table[len(weights_c),columns], total_time

#print(knapsack( 5, 20, [10,8,12,14,20],  [2,3,1,4,9],  5))



def test_cases(cap, copies, max_num_values, max_val, max_weight, c):

    number_of_values = []

    times = []

    for i in range(copies):
        num_values = random.randrange(1,max_num_values)



        values = []
        weights = []
        capacity  = random.randrange(1,cap)
        for i in range(num_values):
            val = random.randrange(1,max_val) 
            weight = random.randrange(1,max_weight) 
            values.append(val)
            weights.append(weight)

        max_profit, time_taken = knapsack(len(values), capacity, values, weights, c)

        number_of_values.append(len(values))

        times.append(time_taken)

    plt.plot(number_of_values, times, 'o')

    plt.xlabel('Number of Items')

    plt.ylabel('Time')

    plt.show()

#test_cases(200, 1000, 3000, 400, 200, 4)


print(knapsack( 3, 200, [2,3,6],  [35,40,55],  3)[0])


