
arr = [130, 137, 138, 138, 144,160, 146,149,154,156]
n = len(arr)
print('the original array is: ')
for val in arr:
    print(val,end=' ')
print('')
arr.sort()
print("The sorted array is")    
for val in arr:
    print(val, end=" ")
print('')
if n%2==0:
    print('The median is; ',(arr[int(n/2)]+arr[int(n/2)-1])/2)
elif n%2==1:
    print ('The median is: ',(arr[int((n-1)/2)]))
