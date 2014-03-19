#It is a well known fact that of all numbers, the number 4 is the most relevant.
# Patterns related to the number 4 tend to appear everywhere.
# For example, the numerical perfection level is closely related to the number 4.
# We define the perfection level of a positive integer N as k if N can be expressed as a product of 4 positive integers,
# each with a perfection level of at least (k-1), and cannot be expressed as a product of 4 positive integers,
# each with a perfection level greater than (k-1).
# There is one exception - if it is not possible to express N as a product of 4 positive integers all greater than 1,
# then the perfection level of N is 0.  Given a long N, return its perfection level.
from copy import deepcopy


class NumericalPerfectionLevel:
    def getLevel(self, N):
        self.determine_k(N)

    def factors(self, n):
        return set(reduce(list.__add__,
                          ([i, n // i] for i in range(2, int(n ** 0.5) + 1) if n % i == 0)))


    def determine_k(self, number):
        factors = sorted(self.factors(number))
        print factors
        self.return_all4(factors, [], number)
        print self.list4


    list4 = []  

    def return_all4(self, factors, l, number):
        if number < 1: return
        if len(l) > 4: return

        if number == 1:
            self.list4.append(l)

        if len(factors) == 0:
            return

        f = deepcopy(factors)
        first_val = f.pop(0)
        li = deepcopy(l)
        li.append(first_val)
        self.return_all4(f, li, float(number) / float(first_val))
        self.return_all4(factors, li, float(number) / float(first_val))
        self.return_all4(f, l, number)


f = NumericalPerfectionLevel()
f.getLevel(1679616)
