#SUPER QUICKSORT 

#select pivot (random or median element)
#move pivot to the end of the array
#move the element at the start of the array towards the end until it reaches a value greater or equal to the PIVOT
#move the end element towards the start of the array until it crosses the start bound or finds a value less than the pivot 


import numpy as np


#initialise array of randomised integers
randnums = np.random.randint(1, 101, 12)

#declare start and end values
start = randnums[0]
end = randnums[11]

#declare pivot
pivot = start


print (randnums)
print(end)
print("Pivot is " +str(pivot))