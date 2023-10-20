dataset = [4,5,8,9,10,17]

avg = (sum(dataset))/len(dataset)
print("The average is ", avg)

dataset.sort()
mid = len(dataset) // 2
print(mid)
median = dataset[mid]
print("The median is ", median)
print("Whats this ", dataset[~mid])
