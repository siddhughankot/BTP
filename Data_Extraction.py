from matplotlib import pyplot as plt
import numpy as np
f=open("/content/conc1.txt")

t=[]
current=[]
content=f.readlines()
for line in content:
    row=line.split()
    if len(row)==0:
        continue
    t.append(float(row[1]))
    current.append(float(row[3]))
    #print(t,current)
    #print(len(row))

Rref=1/(np.array(current))

plt.plot(t[1000:],Rref[1000:])
plt.ylabel("Resistance")
plt.xlabel("Time")
plt.show()

f.close()