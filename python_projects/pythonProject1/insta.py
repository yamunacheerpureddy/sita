# find the max elements length in iven list
list=[3,5,7,9,3,2]
max = float()
for i in list:
    if i > max:
        max=i
        print("max elements",max)