class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        res = []
        count = 0
        for i in self.list1:
            if i in self.list2:
                res.append(i)
                count +=1
        if len(res) == 0:
            print('Совпадающих чисел нет.')
        else:
            print(f'Совпадающие числа: {res}\nКоличество совпадающих чисел: {count}')
