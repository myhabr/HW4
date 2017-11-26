'''Составить описание класса многочленов от одной переменной, задаваемых сте­пенью многочлена
и массивом коэффициентов. Предусмотреть методы для вы­числения значения многочлена для заданного
аргумента, операции сложения, вычитания и умножения многочленов с получением нового объекта-многочлена,
вывод на экран описания многочлена.'''


class Polinom:
    def __init__(self, n, koef_lst):
        self.n = n
        self.koef_lst = koef_lst

    # блок вычислений
    def __add__(self, other):
        new_other = [0 for x in range(abs(len(self.koef_lst) - len(other.koef_lst)))]
        if len(self.koef_lst) > len(other.koef_lst):
            new_other.extend(other.koef_lst)
        else:
            new_other.extend(self.koef_lst)
        new_lst = list(map(lambda x, y: x + y, self.koef_lst, new_other))
        return Polinom(len(new_lst) - 1, new_lst)

    def __sub__(self, other):
        new_other = [0 for x in range(abs(len(self.koef_lst) - len(other.koef_lst)))]
        if len(self.koef_lst) > len(other.koef_lst):
            new_other.extend(other.koef_lst)
        else:
            new_other.extend(self.koef_lst)
        new_lst = list(map(lambda x, y: x - y, self.koef_lst, new_other))
        return Polinom(len(new_lst) - 1, new_lst)

    def __mul__(self, other):
        n1 = self.n  # формируем 1-й многочлен
        lst_1 = self.koef_lst
        lst_1_1 = []
        for el in lst_1:
            empty1 = [n1, el]
            lst_1_1.append(empty1)
            n1 = n1 - 1

        n2 = other.n  # формируем 2-й многочлен
        lst_2 = other.koef_lst
        lst_2_2 = []
        for el in lst_2:
            empty2 = [n2, el]
            lst_2_2.append(empty2)
            n2 = n2 - 1

        lst = []
        for el in lst_1_1:
            for el2 in lst_2_2:
                lst.append([el[0] + el2[0], el[1] * el2[1]])  # складываем степени, коэфф-ты перемножаем

        dict_x = {}  # приводим коэфф-ты при одинаковых степенях
        for elem in lst:
            if elem[0] not in dict_x:
                dict_x.update([elem])
            else:
                dict_x[elem[0]] = dict_x[elem[0]] + elem[1]

        lst3 = []
        for k in sorted(dict_x.keys(), reverse=True):
            lst3.append(dict_x[k])

        return Polinom(len(dict_x) - 1, lst3)


    def solve(self, x):
        sum1 = 0
        power = self.n
        for elem_lst in self.koef_lst:
            sum1 += (x ** power) * elem_lst
            power -= 1
        return sum1

    # перегрузка вывода
    def __str__(self):
        n = self.n
        if self.koef_lst[0] != 0:  # отдельно обрабатываем первый элемент
            result = '{}x^{} '.format(self.koef_lst[0], n)
        else:
            result = ''
        n -= 1

        for k in self.koef_lst[1:-1]:  # все элементы, кроме первого и последнего
            if k > 0:
                result += '+ {}x^{} '.format(k, n)
            elif k < 0:
                result += '- {}x^{} '.format(abs(k), n)
            n -= 1

        if self.koef_lst[len(self.koef_lst)-1] > 0:  # последний элемент
            result += '+ ' + str(self.koef_lst[len(self.koef_lst)-1])
        elif self.koef_lst[len(self.koef_lst)-1] < 0:
            result += '- ' + str(abs(self.koef_lst[len(self.koef_lst) - 1]))
        return result


if __name__ == '__main__':
    a = Polinom(5, [1,-2, 3,4,-5, 6])
    b = Polinom(3, [-3,-4,-5,-6])
    c = a + b
    print("Сложение: ")
    print(c)
    a1 = Polinom(3, [1, 2, 3, 4])
    b1 = Polinom(2, [4, 5, 6])
    print("Вычитание: ")
    c1 = a1 - b1
    print(c1)
    a2 = Polinom(2, [2, -1, 1])
    c2 = a2.solve(5)
    print("Значение многочлена для заданного аргумента: ")
    print(c2)

    z1 = Polinom(2, [10,-3,-1])
    z2 = Polinom(1, [9, -9])
    z = z1 * z2
    print("Умножение:", z)