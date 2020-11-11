"""
You have been asked to help study the population of birds migrating across the continent. 

Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, 

its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. 

Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number.

For example, assume your bird sightings are of types arr = [1,1,2,2,3].

There are two each of types and , and one sighting of type. 

Pick the lower of the two types seen twice: type . 
"""


def migratoryBirds(arr):
    dictionary = dict()
    types = []
    for x in arr:
        if x not in dictionary:
            dictionary[x] = arr.count(x)
    maximum = max(dictionary.values())
    for key, val in dictionary.items():
        if val == maximum:
            types.append(key)
    return min(types)


print(migratoryBirds([1, 1, 2, 2, 3]))  # => 1
print(migratoryBirds([3, 3, 2, 2, 1, 1]))  # => 1
print(migratoryBirds([3, 1, 2, 2]))  # => 2
