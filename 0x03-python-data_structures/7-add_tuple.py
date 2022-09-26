def add_tuple(tuple_a=(), tuple_b=()):
    i = 0
    b = ()
    while(tuple_a):
        if (tuple_b[i] != None):
            b[i] = tuple_a[i] + tuple_b[i]
        else:
            b[i] = tuple_a[i] + 0
        i += 1
    return b
