"""
 A003462 from OEIS https://oeis.org/A003462 :
    Knuth, Donald E. (1997). "Shell's method".
    The Art of Computer Programming. Volume 3: Sorting and Searching (2nd ed.).
    Reading, Massachusetts: Addison-Wesley. pp. 83–95. ISBN 978-0-201-89685-5.

    based on:

    Pratt, Vaughan Ronald (1979). Shellsort and Sorting Networks
    (Outstanding Dissertations in the Computer Sciences) (PDF).
    Garland. ISBN 978-0-8240-4406-0. Archived (PDF) from the original on 7 September 2021.

"""

def a003462_gen(n):
    x = 1
    while x < n:
        x = 3 * x + 1

    while (x := (x - 1) // 3) > 0:
        yield x


def a003462_list(n):
    return list(a003462_gen(n))
