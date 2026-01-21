#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    div = 0
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            result.append(div)
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except TypeError:
            if not isinstance(my_list_1[i], (int, float)):
                print("wrong type")
                result.append(0)
            elif not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
