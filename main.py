def recursive_counter(lst):
    if len(lst) == 0:
        return 0
    return 1 + recursive_counter(lst[1:])


lst = input('Введите, пожалуйста, элементы для списка через пробел').split()
print('Количество элементов в списке:', recursive_counter(lst))