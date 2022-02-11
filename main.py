#SUPER QUICKSORT
                                                                                            
import numpy as np
import termplotlib as tpl


#initialise array of randomised integers
randnums = np.random.randint(1, 101, 12)

#declare start and end values
start = randnums[0]
end = randnums[11]

#declare pivot
pivot = start

#print values to console
print("""███████╗██╗   ██╗██████╗ ███████╗██████╗      ██████╗ ██╗   ██╗██╗ ██████╗██╗  ██╗███████╗ ██████╗ ██████╗ ████████╗
██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗    ██╔═══██╗██║   ██║██║██╔════╝██║ ██╔╝██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝
███████╗██║   ██║██████╔╝█████╗  ██████╔╝    ██║   ██║██║   ██║██║██║     █████╔╝ ███████╗██║   ██║██████╔╝   ██║   
╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗    ██║▄▄ ██║██║   ██║██║██║     ██╔═██╗ ╚════██║██║   ██║██╔══██╗   ██║   
███████║╚██████╔╝██║     ███████╗██║  ██║    ╚██████╔╝╚██████╔╝██║╚██████╗██║  ██╗███████║╚██████╔╝██║  ██║   ██║   
╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝     ╚══▀▀═╝  ╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                                                                                    """)
print (randnums)
print("Pivot is " +str(pivot))
rng = np.random.default_rng(123)
sample = rng.standard_normal(size=1000)
counts, bin_edges = np.histogram(sample)

fig = tpl.figure()
fig.hist(counts, bin_edges, orientation="horizontal", force_ascii=False)
fig.show()


#move the element at the start of the array towards the end until it reaches a value greater or equal to the PIVOT
while start < end:
    while start < len(randnums) and randnums[start] <= pivot:
            start += 1

#move the end element towards the start of the array until it crosses the start bound or finds a value less than the pivot 
    while randnums[end] > pivot:
        end -= 1
         
             

