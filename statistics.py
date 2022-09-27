import math
import numpy as np


# How to calculate standard deviation
population = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]

mean = sum(population)/len(population)

deviation = [(x-mean) * (x-mean) for x in population]

standard_deviation_squared = sum(deviation)/len(deviation)

standard_deviation = math.sqrt(standard_deviation_squared)

print(standard_deviation)

print(np.std(population))


#tem = pow((20-mean), 2)
#print(tem)