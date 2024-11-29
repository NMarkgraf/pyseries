"""
Shell, D. L. (1959).
"A High-Speed Sorting Procedure" (PDF).
 Communications of the ACM. 2 (7): 30–32. doi:10.1145/368370.368387. S2CID 28572656.
 Archived from the original (PDF) on 30 August 2017. Retrieved 18 October 2011.
"""
import math

def shell_1959_gen(n):
    for i in range(1, 1+int(math.log2(n))):
        yield n // 2**i

def shell_1959_list(n):
    return list(shell_1959_gen(n))



