import csv
import math

with open('data(1).csv', newline='') as f:
    reader=csv.reader(f)
    #reads row, returns current row,moves on to next

    file_data=list(reader)
    #sorting
    data=file_data[0]
#step one find mean
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean

#step 2 squaring and getting values
square_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    square_list.append(a)

#get sum of all elements from square list
sum=0
for i in square_list:
    sum=sum+i

#step4:divide by total value
result=sum/(len(data)-1)

#step5:square root
final_ans=math.sqrt(result)

print("your final answer:"+str(final_ans))
