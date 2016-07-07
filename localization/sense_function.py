p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        # print 0.2 * (hit * pHit)
        # print 0.2 * ((1-hit))
        print "----[Whole]----"
        print (0.2 * (hit * 0.6 + (1-hit) * 0.2))
        print "----[One]----"
        print (0.2 * (1 * 0.6 + (1-1) * 0.2))
        print "----[Zero]----"
        print (0.2 * (0 * 0.6 + (1-0) * 0.2))
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
        # print q
    return q

print sense(p, Z)
