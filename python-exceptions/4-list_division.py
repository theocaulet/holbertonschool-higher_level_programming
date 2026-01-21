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
            if isinstance(my_list_1[i], (int, float)):
                print("wrong type")
            elif isinstance(my_list_2[i], (int, float)):
                print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(div)
    return result
