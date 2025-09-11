#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_length = len(my_list)

    if idx < 0 or idx >= list_length:
        return my_list
    new_list = my_list[:idx] + my_list[idx+1:]
    return new_list
    