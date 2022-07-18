from logging import root
import numpy as np
import math
import matplotlib.pyplot as plt
import time
import random


class Node:

    def __init__(self, total_value,  tree_level, weight):
        self.tot_v  = total_value
        self.tl = tree_level
        self.w = weight

    def add_ub(self, ub):
        self.ub  = ub


def knapsack(rows, values, weights, c, cap):

    weights_c = []
    values_c = []

    for i in range(rows):
        for j in range(1,c+1):
            weights_c.append(weights[i] )
            values_c.append(values[i] )

    comb_list = list(zip(values_c, weights_c))

    comb_list.sort(reverse=True, key=lambda comb_list:comb_list[0]/comb_list[1])

    queue = []
    root = Node(0,-1,0)

    queue.append(root)

    max_p = 0

    while(len(queue) >0):
        n1 = queue.pop()

        next_level = n1.tl + 1 

        if next_level >= len(comb_list):
            break

        new_weight = n1.w + comb_list[next_level][1]
        new_profit = n1.tot_v + comb_list[next_level][0]

        if new_weight <= cap and new_profit > max_p:
            max_p  = new_profit

        n2 = Node(new_profit, next_level, new_weight)

        n2.add_ub( upper_bound(n2, comb_list, cap))

        n3 = Node(n1.tot_v, n1.tl+1, n1.w)

        n3.add_ub( upper_bound(n1, comb_list, cap))

        if n2.ub > max_p :
            queue.insert(0,n2)
 

        if n3.ub > max_p:
            queue.insert(0,n3)


    return max_p


def upper_bound(node, list_v, capacity):

    if node.w > capacity:
        return 0 

    total_weight = node.w
    total_prof  = node.tot_v


    for i in range(node.tl+1, len(list_v)):

        if list_v[i][1] + total_weight > capacity:
            if i < len(list_v):

                total_prof += math.floor( (capacity - total_weight) * list_v[i][0] / list_v[i][1])
            break
        else:
            total_weight += list_v[i][1]
            total_prof += list_v[i][0]

    return total_prof        

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

        start = time.time()

        max_profit = knapsack(len(values), values, weights, c,  capacity)

        end = time.time()

        time_taken = end - start

        number_of_values.append(len(values))

        times.append(time_taken)

    plt.plot(number_of_values, times, 'o')

    plt.xlabel('Number of Items')

    plt.ylabel('Time')

    plt.show()

test_cases(10, 100, 200, 10, 10, 4)


#print(knapsack( 5,  [40,50,100,95,30],  [2,3.14,1.98,5,3], 1, 10))

#print(knapsack( 5, [10,8,12,14,20],  [2,3,1,4,9],  5, 20))


#print(knapsack( 3,  [2,3,6],  [35,40,55],  3, 200))



    