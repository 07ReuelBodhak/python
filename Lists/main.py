## List 

my_list = [1,2,3,4,5]

## adding element

my_list.append(11)
print("after appending",my_list)

my_list.extend([4,5,6,7])
print("List after extending",my_list)

my_list.insert(3,45) 
print("list after inserting element at specified position",my_list)

## removing element

my_list1 = [1,2,3,4,5,6,7]

my_list1.remove(3) 
print("after removing element from a list ",my_list1)

ele = my_list1.pop(5)
print("after poping element at index 5 and storing it in variable ",ele)

my_list1.clear() ## clearing entire list

## Finding element 

ele1 = my_list.index(3)
print("returns the index number of the first occurrence of element 3", ele1)

total = my_list.count(2)
print("total occurrences of element 2 in the list",total)

## Sorting list
my_list.sort()
print("sorting list in ascending order ", my_list)
my_list.reverse()
print("sorting list in descending order", my_list)

## Copy

copy_list = my_list.copy()
print("copied list ",copy_list)