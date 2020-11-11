"""
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them.

Notice that multiple kids can have the greatest number of candies.
"""

def kidsWithCandies(candies, extraCandies):
    if len(candies) == 0:
        return []
    maxCandies = max(candies)
    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxCandies:
            candies[i] = True
        else:
            candies[i] = False
    return candies
    # Time Complexity: O(N)
    # Space Complexity: O(1)


print(kidsWithCandies([], 3))
print(kidsWithCandies([1,2,3,4,5], 2))
