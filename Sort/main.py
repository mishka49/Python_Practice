import timeit
from mylist_sort import List

length = input("Enter length of list: ")
list_int = List.generate_list(length)

print("Befor sort: " + str(list_int))
time_exec = timeit.timeit("List.sort(list_int)", globals=globals(), number=1)
print("After sort: " + str(list_int))
print("\nTime: "+str(time_exec))