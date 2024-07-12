## creating set

my_set = {1,2,3,5}
my_set.add(6)

print("My set",my_set)

my_set.discard(2)
print("After discarding element",my_set)

set1 = {1,2,3,4,5,6,7}
set2 = {5,3,8,9,11}

print("after union : ",set1.union(set2))

print("after difference : ",set1.difference(set2))

print("after intersection : ",set1.intersection(set2))

print("after symmetric_difference : ",set1.symmetric_difference(set2))

