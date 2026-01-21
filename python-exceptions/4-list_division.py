#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    temp_result = 0
    result = []
    div = 0
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            temp_result = div
        except ZeroDivisionError:
            temp_result = 0 
            print("division by 0")
        except TypeError:
            print("wrong type")
            temp_result = 0
        except IndexError:
            print("out of range")
            temp_result = 0
        finally:
            result.append(temp_result)
            temp_result = 0
    return result
