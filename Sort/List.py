from random import randint

class List:
    @staticmethod
    def generate_list(length):
        return [randint(1, 100) for x in range(int(length))]

    @staticmethod
    def sort(list):
        step=0
        while True:
            min=step
            max=step

            for index in range(step,len(list)-step):
                if list[index]>list[max]:
                    max=index
                if list[index]<list[min]:
                    min=index

            if list[min]!=list[max]:
                if max==step and min==len(list)-step-1:
                    list[max],list[min]=list[min],list[max]
                elif max==step:
                    list[max], list[-step - 1] = list[-step - 1], list[max]
                    list[step], list[min] = list[min], list[step]
                else:
                    list[step], list[min] = list[min], list[step]
                    list[max], list[-step - 1] = list[-step - 1], list[max]

                step +=1
                continue
            else:
                break
