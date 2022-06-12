import timeit
from List import List

length = input("Enter length of list: ")
list = List.generate_list(length)

print("Befor sort: " + str(list))
time_exec = timeit.timeit("List.sort(list)", globals=globals(), number=1)
print("After sort: " + str(list))
print("\nTime: "+str(time_exec))