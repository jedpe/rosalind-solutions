"""
Rabbits and Recurrence Relations
ID: FIB
Number: 004
URL: http://rosalind.info/problems/fib/
"""

import csv


def rabbit_pairs(n, k):

    # n = month number
    # k = number of rabbit pairs in each litter
    # Initial values of the sequence
    rp = [1, 1]

    for i in range(2, n):

        '''
        The number of rabbit pairs is the number of pairs from the previous generation
        plus the number of mature rabbit pairs (the number of rabbit pairs from two generations ago)
        multiplied by the number of pair rabbits in each litter
        '''
        rp.append(rp[-1] + rp[-2]*k)

    # Return the last month's rabbit pair count
    return rp[-1]


if __name__ == '__main__':

    with open('rosalind_fib.txt', 'r') as input_file:

        # Read the first line of the file
        n, k = next(csv.reader(input_file, delimiter=' '))

        # Compute number of rabbit pairs after n months
        n_r = rabbit_pairs(int(n), int(k))

        # Print result
        print(n_r)
