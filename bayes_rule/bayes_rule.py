# Probability for P(C|Pos)
# P(C) = 0.1
# P(Pos|C) = 0.9
# P(Neg|C) = 0.8

def f(p0, p1, p2):
    return p0 * p1 / (p0 * p1 + (1 - p0) * (1 - p2))

print f(0.1, 0.9, 0.8)