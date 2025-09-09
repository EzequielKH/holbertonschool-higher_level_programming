#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    val_a_0 = tuple_a[0] if len(tuple_a) >= 1 else 0
    val_a_1 = tuple_a[1] if len(tuple_a) >= 2 else 0

    val_b_0 = tuple_b[0] if len(tuple_b) >= 1 else 0
    val_b_1 = tuple_b[1] if len(tuple_b) >= 2 else 0

    sum_0 = val_a_0 + val_b_0
    sum_1 = val_a_1 + val_b_1

    return (sum_0, sum_1)
