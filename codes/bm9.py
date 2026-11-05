from statistics import mean, median
#Given data
data=[-5, 1, 3, 5, 11]

print("Data: ",data)
print("Mean: ",mean(data))
print("Median: ", median(data))

#Veify
if mean(data)==3 and median(data)==3:
   print("Therefore, a=3 and b=11")
