#
#
#Problem Statement
#
#Constraints
#-
#luckySet will contain between 2 and 50 elements, inclusive.
#-
#Each element of luckySet will be between 1 and 1000, inclusive.
#-
#Each element of luckySet will be distinct.
#-
#n will be between 1 and the largest element in luckySet, inclusive.

#

#{1, 7, 14, 10}
#2
#Returns: 4
#4 unlucky intervals in total contain 2: [2,3], [2,4], [2,5] and [2, 6].

#{3, 7, 12, 18, 25, 100, 33, 1000}
#59
#Returns: 1065
#



class UnluckyNumbers:
    def getCount(self, luckyset, n):
        if n in luckyset:
            return 0
        self.permuteCount(n, n, luckyset)
        return len(self.a) -1


    a = set()

    def permuteCount(self, start, end, luckyset):
        if start in luckyset: return
        if end in luckyset: return
        if str(start)+"s"+str(end) in self.a:
            return
            #if start >= end: return
        if start == 0: return


        self.a.add(str(start)+"s"+str(end))

        self.permuteCount(start - 1, end, luckyset)
        self.permuteCount(start, end + 1, luckyset)


d = UnluckyNumbers()
d.getCount([4, 8, 13, 24, 30], 10)