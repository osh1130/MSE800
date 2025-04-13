import numpy as np
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

i = 0
total = 0
hightest = 0
loweat=10000
for c in temperatures:
    total+=c
    hightest = max(c,hightest)
    loweat = min(c,loweat)
    f = c *9/5+32
    if c > 20:
        print(i)
    i+=1
print('average',total/7)
print('hightest',hightest)
print('loweat',loweat)