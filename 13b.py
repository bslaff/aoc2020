import math

f = open('input/13a_input.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

ids = lines[1].split(',')

def extended_euclidean(n1, n2):
    rr = [n1, n2]
    ss = [1, 0]
    tt = [0, 1]
    while True:
        q = int(rr[0] / rr[1])
        rr = [rr[1], rr[0] - q*rr[1]]
        ss = [ss[1], ss[0] - q*ss[1]]
        tt = [tt[1], tt[0] - q*tt[1]]
        if rr[1] == 0:
            break

    return (ss[0], tt[0])

# y mod z
# (y, z)
conditions = [((- i) % int(ids[i]), int(ids[i])) for i in range(len(ids)) if ids[i] != 'x']
conditions.sort(key = lambda x: x[1], reverse = True) # guarantees moduli input to extended euclidean alg in descending order

# General case of CRT / inductive proof by construction
(a1, n1) = conditions[0]
(a2, n2) = conditions[1]
for idx in range(1, len(conditions)):
    (a2, n2) = conditions[idx]
    (m1, m2) = extended_euclidean(n1, n2)
    x = a1*n2*m2 + a2*n1*m1
    if x < 0:
        q = abs(int(x / (n1*n2)))
        x += (q + 1) * n1 * n2
    a1 = x % (n1*n2)
    n1 = n1 * n2

print(f"Solution is {x}")
