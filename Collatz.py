#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>

    assert i > 0 and j > 0

    a,b = (min(i, j), max(i, j))
    count = []
    for n in range(a, b + 1):
        num = n
        cnt = 1
        while True:
            if  num == 1:
                break
            elif num % 2 == 0:
                num = num >> 1
                cnt = cnt + 1
            else:
                assert num % 2 == 1
                num = num + (num >> 1) + 1
                cnt = cnt + 2
        count.append(cnt)
    assert max(count) >= 1
    return max(count)


# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
