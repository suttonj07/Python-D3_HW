# Implement a function that will flatten and sort an array of integers 
# in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

print(flatten_and_sort([[19,67,0],[9,45,17],[92,55,2]]))
print(flatten_and_sort([[19,67,0],[9,45,17],[92,55,2]]))
print(flatten_and_sort([[19,67,0],[9,45,17],[92,55,2]]))


# Make sure to answer the following questions about your coding process:

# How does this solution ensure data immutability?
# Data immutability is the idea that information within a database cannot be deleted or changed. In immutable—or append-only—databases, data can only ever be added. Meaning the database will not overwrite or change an item when new information is made available. So even if a mistake is made, it is corrected with a subsequent entry and not overwritten.

# Is this solution a pure function? Why or why not?

# Returns the same result given the same arguments: flatten_and_sort always returns the same sorted array for a given input array.
# No side effects: The function does not modify any external state; it only operates on the input and returns a result.
# Thus, flatten_and_sort is a pure function.


# Is this solution a higher order function? Why or why not?
# flatten_and_sort does not take any functions as arguments.
# flatten_and_sort does not return a function as its result.
# Thus, flatten_and_sort is not a higher-order function.


# Would it have been easier to solve this problem using a different programming style?

# The flatten_and_sort function is written in an imperative style, which is clear and easy to understand. However, other programming styles, such as functional programming, can offer more concise and expressive solutions.

# Why in particular is functional programming a helpful paradigm when solving this problem?

# Functional programming enhances the conciseness, expressiveness, and readability of the solution. It abstracts away low-level details, allowing you to focus on the high-level logic of the problem.

class TestArray:
    def __init__(self):
        self.arr = []

    def flatten_and_sort(self, newArray):
        for item in newArray:
            for i in item:
                self.arr.append(i)
        return sorted(self.arr)

testOOP = TestArray()
testResult1 = testOOP.flatten_and_sort([[19,67,0],[9,45,17],[92,55,2]])
testResult2 = testOOP.flatten_and_sort([[19,67,0],[9,45,17],[92,55,2]])
testResult3 = testOOP.flatten_and_sort([[19,67,0],[9,45,17],[92,55,2]])
print(testResult1)
print(testResult2)
print(testResult3)