# Get the highest repettive number from an array
unique_array = {}
big_array = [1,1,1,1,1,3,2,4,2,3,3,4,2,2,3,5,6,7,7,8,6,5,5,4,2,3,2,2]
for row in big_array:
    if not row in unique_array:
        unique_array[row] = 1
    else:
        unique_array[row] += 1

print(unique_array)
print(max(unique_array.items(), key = lambda x: x[1])[0]) # this will return the key for highest value