p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        print hit
        print pHit
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
        print q
    return q

print sense(p, Z)
