"""
    Gonnet, Gaston H.; Baeza-Yates, Ricardo (1991).
    "Shellsort". Handbook of Algorithms and Data Structures: In Pascal and C (2nd ed.).
    Reading, Massachusetts: Addison-Wesley. pp. 161–163. ISBN 978-0-201-41607-7.
    Extensive experiments indicate that the sequence defined by α = 0.45454 < 5/11 performs significantly
    better than other sequences.
    The easiest way to compute ⌊0.45454n⌋ is by (5 * n — 1)/11 using integer arithmetic.
"""

def gonnet_baeza_yates_1991_gen(n):
    x = n
    while (x := (5*x-1) // 11) > 2:
        yield x
    else:
        if x == 2:
            yield 2
        yield 1

def gonnet_baeza_yates_1991_list(n):
    return list(gonnet_baeza_yates_1991_gen(n))