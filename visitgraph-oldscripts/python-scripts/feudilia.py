#Feudalia's military is preparing a preemptive strike against Banania's military installations.
# Feudalia has two missile silos. Each silo has an unlimited number of missiles at its disposal,
# but can only fire a single missile at a time. When a missile is fired, it requires takeOffTime seconds before it can take off from its silo.
# Once it takes off, it requires distance/missileSpeed minutes to reach its target, where distance is the Euclidean distance between the silo and the target.
# When the missile reaches its target, the target is instantly destroyed. After a missile takes off, its silo requires rechargeTime minutes
# of preparation before it can launch another missile.
# Two missile silos may not seem like a lot, but Banania is also a small country with only two military bases.
# It takes a single missile to destroy a military base. The general has ordered you to destroy both of Banania's military bases in as little time as possible.
# You are given int[]s siloX, siloY, baseX and baseY. Your silos are located at (siloX[0], siloY[0]) and (siloX[1], siloY[1]),
# and the enemy bases are located at (baseX[0], baseY[0]) and (baseX[1], baseY[1]).
# Return the minimum time in minutes required to destroy both enemy bases.
#Definition
import operator


class FeudaliasBattle:
    def getMinimumTime(self, baseX, baseY, siloX, siloY, takeOffTime, rechargeTime, missileSpeed):

        dist = {}
        for i in range(2):
            for j in range(2):
                dist[str(i) + str(j)] = self.calctime(self.euclid(siloX[i], baseX[j], siloY[i], baseY[j]), takeOffTime,
                                                      rechargeTime,
                                                      missileSpeed)

        vals = sorted(dist.iteritems(), key=operator.itemgetter(1))
        first = vals[0]
        second = vals[1]
        third = vals[2]

        firstTime = first[1]
        secondTime = second[1]
        if first[0][0] == second[0][0]:
            t = second[1] + rechargeTime
            secondTime = third[1] if (t > third[1])else t + firstTime

        return max(firstTime, secondTime)

    def calctime(self, euc, takeOff, recharge, miss):
        transact = float(float(takeOff) / 60) + float(float(euc) / float(miss))
        return transact

    def euclid(self, a1, b1, a2, b2):
        return pow(pow(float(a1) - float(b1), 2) + pow(float(a2) - float(b2), 2), 0.5)


r = FeudaliasBattle()
r.getMinimumTime([100, 100],
[100, 500],
[100, 500],
[300, 300],
6,
20,
20)
