"""
    Frank, R. M.; Lazarus, R. B. (1960).
    "A High-Speed Sorting Procedure". Communications of the ACM. 3 (1): 20–22. doi:10.1145/366947.366957. S2CID 34066017.
"""

import math

def frank_lazarus_1960_gen(n):
    for i in range(1, 1+(int(math.log2(n)))):
        yield 2*(n // 2**(i+1)) + 1

def frank_lazarus_1960_list(n):
    return list(frank_lazarus_1960_gen(n))



