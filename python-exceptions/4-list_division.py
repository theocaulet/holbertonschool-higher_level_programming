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
            temp_result = 0
            print("wrong type")
        except IndexError:
            temp_result = 0
            print("out of range")
        finally:
            result.append(temp_result)
            temp_result = 0
    return result
