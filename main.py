import numpy as np
from time import time

n = np.array([[2, 2, 3, 2, 3], 
               [-1, 1, 1, 4, 5], 
               [-1, 3, 5, 8, 5],
               [4, 1, -5, 3, 1],
               [-4, 2, -5, 4, 2],
               ]);
m = np.array([[1], [0], [-4], [-3], [0]]);

print("n = ")
print(n);
print("m =")
print(m)

start_time = time()
x = np.linalg.solve(n, m);
end_time = time()
eleapse_time = end_time - start_time

print("x =")
print (x);

print("Elapsed time: %0.10f seconds." % eleapse_time)
print()