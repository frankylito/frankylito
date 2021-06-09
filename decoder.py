### decoder.py
### Frank Lapolito, Shawn Barlow


import numpy as np
import matplotlib.pyplot as plt


#file name INPUT
name=input("Enter full matrix file name: ")
#name="secret.coo" -- Test Code

###FILE TO list of rows
file = open(name,"r") ### opening the file
lines = file.readlines() ###line by line reading
list_row=[] ### Empty list to hold rows
###Counters:
m=0
i=0
b=0


### breaks list of rows into list of row list [x , y, z]
for line in lines: ### for each line in the list of lines
    m = m+1
    #list_row.append(line[m].split())
    #print(line,m)
    for i in line: ### for each element in line
        row = line.split() #### creating a list of elements in line
        for i in range(0,len(row)): ### for each element in row
            row[i]=int(row[i]) ### setting values to ints
        list_row.append(row)   ### adding list of int values to list of rows
        #print(row)
        b=b+1

arr = np.array(list_row) ### creating an array of the values of the file
list1 = arr[:,0] ### making a list of the first col.
j=-1
max_value1=0
for i in list1: ### finding max value of list
    j=j+1
    if max_value1 > list1[j]:
        max_value1 = max_value1
    else:
        max_value1 = list1[j]

list2 = arr[:,1]  ### making a list of the second col.
j=-1
max_value2 = 0
for i in list2: ### finding max value of list
    j=j+1
    if max_value2 > list1[j]:
        max_value2 = max_value2
    else:
        max_value2 = list2[j]



###padding
img_h, img_w = max_value1+(max_value1//40), max_value2+(max_value2//30) ###adding width to the image array
img_arr = np.zeros((img_h, img_w)) ### making an array with valiues of zero the size of the image
c=1
for val in list_row: # for every element in list of rows
    c=c+1
    row = val ### row = list_row[val] = [x , y , z]
    img_arr[row[0]+(max_value1//80),row[1]+(max_value2//60)] = row[2] ### replacing zero values with z of corr. cordinate




### Displaying and saving img
plt.matshow(img_arr,cmap="binary")
plt.savefig('secret.jpg')
plt.show()


