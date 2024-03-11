# Dictionary - mutable
# Contains key-value pair

d1 = {}
d2 = {"name": "diya", "surname": "lad"}

d = dict()

d3 = {"j":1, "j":2, "k":3}
print(d3)

for k in d3:
    print(d3[k])

d4 = {(1,2,3):5}
print(d4)

d5 = {"j":2, "k":3}
print(d3==d5) # as dictionary is ordered

del d5["j"]

# Sets - collection of unique elements

s = {} # defines empty dictionary
#  To create empty set use set constructor

s = set()

s1 = set("hello")
print(s1)

s2 = set([1,2,3,4,2])
print(s2)

s3 = {1,2,5,3,2,1}
print(s3)

#  Sets are unordered, mutable
s3.add(5)

s3.add((1,2,3,34))
print(s3)

for i in s3:
    print(i)