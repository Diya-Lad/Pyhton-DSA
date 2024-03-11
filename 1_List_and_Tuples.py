# List
list1 = [1,2,"hello"]
print(list1)

list2 = list()

# list are ordered
# indexing is followed
print(list1[0])

list3 = [[1,2], 3,4]

# list are mutable
list3.append(5)
print(list3)

del list1[0]
print(list1)

# Iteration
for item in list3:
    print(item)

# Tuples
t1 = (1,2,3)
t2 = 1,"hello",3

print(t1)
print(t2)

t3 = tuple()
print(type(t3))

# t4 = tuple(2)  # consider as an integer
# print(type(t4))

# tuples are immutable. we can't modify it
# as tuple are immutable, it prevent us from accedental modification

for i in t1:
    print(i)
