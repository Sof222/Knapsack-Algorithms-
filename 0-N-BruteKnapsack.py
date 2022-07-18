import numpy as np
import matplotlib.pyplot as plt
import time
import random



def brute_force(v, n, i, values, weights, t, w, profits, c):

    if i == n:
        if sum(t) <= w:
            return sum(v)
            
        return 0 


    for k in range(c+1):

        v[i] = (k * values[i])
        t[i] =(k * weights[i])

        profits.append(brute_force(v, n, i+1, values, weights, t, w, profits, c+1))

    return 0


profit = []  
brute_force([0 for i in range(5)], 5, 0, [10,8,12,14,20],  [2,3,1,4,9], [0 for i in range(5)], 20, profit, 6)

#print("max = ", max(profit))



def test_cases(cap, copies, max_num_values, max_val, max_weight, c):

    number_of_values = []

    times = []

    for i in range(copies):
        num_values = random.randrange(1,max_num_values)

        values = []
        weights = []
        capacity = cap
        for i in range(num_values):
            val = random.randrange(1,max_val) 
            weight = random.randrange(1,max_weight) 
            values.append(val)
            weights.append(weight)

        n = len(values)
        p=[]

        start = time.time()
        max_profit = brute_force([0 for i in range(n)], n, 0, values, weights, [0 for i in range(n)], capacity, p,  c )

        end = time.time()

        total_time = end - start

        number_of_values.append(len(values))

        times.append(total_time)

    plt.plot(number_of_values, times, 'o')

    plt.xlabel('Number of Items')

    plt.ylabel('Time')

    plt.show()

#test_cases(20, 20, 15, 5, 5, 3)

profit = []  
brute_force([0 for i in range(3)], 3, 0, [2,3,6],  [35,40,55], [0 for i in range(3)], 200, profit, 3)

print("max = ", max(profit))
