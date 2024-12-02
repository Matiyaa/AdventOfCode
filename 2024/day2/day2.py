def main():
    with open("input") as f:
        data = f.readlines()

    def is_safe(report: list[int]) -> bool:
        if report[0] - report[1] < 0:
            diffs = [-1, -2, -3]
        else:
            diffs = [1, 2, 3]
        for i in range(len(report) - 1):
            if (not report[i] - report[i + 1] in diffs) or report[i] - report[i + 1] == 0:
                return False
        return True

    def dampened(report: list[int]) -> bool:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i + 1:]):
                return True
        return False

    safe_reports = 0
    dampened_reports = 0

    for report in data:
        report = report.strip().split()
        report = list(map(int, report))

        if is_safe(report):
            safe_reports += 1
        else:
            if dampened(report):
                dampened_reports += 1

    print(f"Part 1 answer: {safe_reports}")
    print(f"Part 2 answer: {dampened_reports + safe_reports}")


if __name__ == "__main__":
    main()
