import re


def main():
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    mult_results_p1 = 0
    mult_results_p2 = 0
    enabled = True

    def mul(a, b):
        return a * b


    with open("input") as file:
        lines = file.readlines()
        for line in lines:
            matches = re.findall(pattern, line)
            for match in matches:
                mult_results_p1 += eval(match)

            segments = re.split(f"({do_pattern}|{dont_pattern})", line)
            for segment in segments:
                if re.match(do_pattern, segment):
                    enabled = True
                elif re.match(dont_pattern, segment):
                    enabled = False
                elif enabled:
                    matches = re.findall(pattern, segment)
                    for match in matches:
                        mult_results_p2 += eval(match)


    print(f"Part 1 answer: {mult_results_p1}")
    print(f"Part 2 answer: {mult_results_p2}")

if __name__ == "__main__":
    main()
