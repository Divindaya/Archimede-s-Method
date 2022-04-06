import math

def archimethod(n0, side1, n, m):
    radius = 1
    a = math.sqrt(radius - (side1/2)**2)
    b = radius - a
    s2 = math.sqrt(b**2 + (side1/2)**2)
    p = n0 * side1
    d = 2
    print('n =', n0)
    print('lower limit ratio is ', p/d)

    n1 = n0 * 2
    p1 = n1 * s2

    k = radius/a
    p2 = p * k

    print('upper limit ratio is ', p2/d)

    mean = (p/d + p2/d)/2
    print('mean value is', mean)
    print('difference is', p2/d - p/d)
    print('------------------------------------------')

    if n1 <= 2**m*n:
        archimethod(n1, s2, n, m)


def main():
    n0 = int(input('Enter n:'))
    m = int(input('Enter m:'))
    side1 = 1 ## length of one side of hexagon in unit circle
    archimethod(n0, side1, n0, m)

main()