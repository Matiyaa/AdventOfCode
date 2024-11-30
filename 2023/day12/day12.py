def main():
    cache = {}

    def count(config, nums):
        if config == '':
            return 1 if nums == () else 0

        if nums == ():
            return 0 if '#' in config else 1

        key = (config, nums)

        if key in cache:
            return cache[key]

        result = 0

        if config[0] in ".?":
            result += count(config[1:], nums)

        if config[0] in '#?':
            if nums[0] <= len(config) and '.' not in config[:nums[0]] and (nums[0] == len(config) or config[nums[0]] != '#'):
                result += count(config[nums[0] + 1 :], nums[1:])

        cache[key] = result
        return result

    with open('day12_input.txt', 'r') as f:
        lines = f.readlines()

    possibilities_part1 = 0
    possibilities_part2 = 0

    for line in lines:
        config, nums = line.split()
        nums = tuple(map(int, nums.split(',')))
        possibilities_part1 += count(config, nums)

        config = '?'.join([config] * 5)
        nums *= 5
        possibilities_part2 += count(config, nums)

    print(f'Part 1 answer: {possibilities_part1}')
    print(f'Part 2 answer: {possibilities_part2}')

if __name__ == '__main__':
    main()