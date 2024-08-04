def apply_all_func(int_list, *functions):
    results = {}
    try:
        for func in functions:
            res = func(int_list)
            results[func.__name__] = res
    except TypeError:
        print(f'Проверьте, что бы в списке были только числа')
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
