import itertools
import math


def main():
    input = open("input", "r").read().splitlines()
    points = [tuple(map(int, line.split(','))) for line in input]
    n = len(input)
    k = 1000
    edges = []

    for i, j in itertools.combinations(range(n), 2):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        d2 = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        edges.append((d2, i, j))

    edges.sort(key=lambda e: e[0])

    parent = list(range(n))
    size = [1] * n
    components = n

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        nonlocal components
        a, b = find(a), find(b)
        if a == b:
            return False
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
        components -= 1
        return True

    for dist, a, b in edges[:k]:
        union(a, b)

    comps = {}
    for i in range(n):
        r = find(i)
        comps[r] = comps.get(r, 0) + 1

    biggest = sorted(comps.values(), reverse=True)[:3]
    print(f'Part 1 answer: {math.prod(biggest)}')

    last_i = last_j = None
    for _, i, j in edges[k:]:
        if union(i, j):
            last_i, last_j = i, j
            if components == 1:
                break

    x1 = points[last_i][0]
    x2 = points[last_j][0]
    print(f'Part 2 answer: {x1 * x2}')

if __name__ == '__main__':
    main()
