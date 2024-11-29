"""
 A000225 from OEIS https://oeis.org/A000225 :
    Hibbard, Thomas N. (1963). "An Empirical Study of Minimal Storage Sorting".
    Communications of the ACM. 6 (5): 206–213. doi:10.1145/366552.366557. S2CID 12146844.

"""

import math

def a000225_gen(n):
    for i in range(int(math.log2(n)), 0, -1):
        yield 2**i - 1


def a000225_list(n):
    return list(a000225_gen(n))
