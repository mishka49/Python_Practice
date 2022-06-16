import timeit
from random import randint
from typing import List


class ListSorting:
    @staticmethod
    def generate_list(length: int) -> List[int]:
        return [randint(1, 100) for _ in range(int(length))]

    @staticmethod
    def sort(list_for_sort: List[int]) -> None:
        step = 0
        while True:
            min_index = step
            max_index = step

            for index in range(step, len(list_for_sort) - step):
                if list_for_sort[index] > list_for_sort[max_index]:
                    max_index = index
                if list_for_sort[index] < list_for_sort[min_index]:
                    min_index = index

            if list_for_sort[min_index] == list_for_sort[max_index]:
                break

            if max_index == step and min_index == len(list_for_sort) - step - 1:
                list_for_sort[max_index], list_for_sort[min_index] = list_for_sort[min_index], list_for_sort[max_index]
            elif max_index == step:
                list_for_sort[max_index], list_for_sort[-step - 1] = list_for_sort[-step - 1], list_for_sort[max_index]
                list_for_sort[step], list_for_sort[min_index] = list_for_sort[min_index], list_for_sort[step]
            else:
                list_for_sort[step], list_for_sort[min_index] = list_for_sort[min_index], list_for_sort[step]
                list_for_sort[max_index], list_for_sort[-step - 1] = list_for_sort[-step - 1], list_for_sort[max_index]
                step += 1


if __name__ == "__main__":
    length = input("Enter length of list: ")
    list_int = List.generate_list(length)

    print(f"Befor sort: {str(list_int)}")
    time_exec = timeit.timeit("List.sort(list_int)", globals=globals(), number=1)
    print(f"After sort: {str(list_int)}")
    print(f"\nTime: {str(time_exec)}")
