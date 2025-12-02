from typing import Set, List


def main():
    input = open("input", "r").read().split(',')
    ranges = [tuple(r.strip().split('-')) for r in input]
    all_invalids = set()
    actually_all_invalids = set()

    for start, end in ranges:
        all_invalids.update(invalids_ids(start, end))
        actually_all_invalids.update(invalids_ids_v2(start, end))

    print(f"Part 1 answer: {sum(all_invalids)}")
    print(f"Part 2 answer: {sum(actually_all_invalids)}")


def invalids_ids(start:str, end:str) -> Set[int]:
    invalids = set()
    len_start = len(start)
    len_end = len(end)

    for L in range(len_start, len_end + 1):
        if L % 2 != 0:
            continue

        half_len = L // 2
        min_half = 10**(half_len - 1)
        max_half = 10**half_len - 1
        pow_half = 10**half_len

        for half in range(min_half, max_half + 1):
            candidate = half * pow_half + half
            if int(start) <= candidate <= int(end):
                invalids.add(candidate)

    return invalids


def invalids_ids_v2(start:str, end:str) -> Set[int]:
    invalids = set()
    len_start = len(start)
    len_end = len(end)

    for L in range(len_start, len_end + 1):
        for k in divisors(L):
            m = L // k
            if m < 2:
                continue

            if k == 1:
                block_min = 1
            else:
                block_min = 10 ** (k - 1)

            block_max = 10 ** k - 1
            pow_k = 10 ** k

            for block in range(block_min, block_max + 1):
                candidate = 0

                for _ in range(m):
                    candidate = candidate * pow_k + block

                if int(start) <= candidate <= int(end):
                    invalids.add(candidate)

    return invalids


def divisors(n: int) -> List[int]:
    out = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            out.append(i)
            if i != n // i:
                out.append(n // i)
    return out


if __name__ == '__main__':
    main()