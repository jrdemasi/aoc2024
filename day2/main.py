#!/usr/bin/env python3

def parse_input():
    inputs = []
    with open("input", 'r') as f:
        for line in f:
            report = list(map(int, line.strip().split()))
            inputs.append(report)
    return inputs


def generate_alt_reports(report):
    alt_reports = []
    i = 0
    while i < len(report):
        alt_report = report[:i] + report[i + 1:]
        alt_reports.append(alt_report)
        i = i + 1
    return alt_reports

def check_report(report):
    i = 0 
    safe = True
    if report[i] > int(report[i+1]): # decreasing
        while i < (len(report) - 1):
            if report[i] > report[i+1] and 1 <= abs(report[i] - report[i+1]) <= 3:
                pass
            else:
                safe = False
            i = i + 1
    elif report[i] < int(report[i+1]): # increasing
        while i < (len(report) - 1):
            if report[i] < report[i+1] and 1 <= abs(report[i] - report[i+1]) <= 3:
                pass
            else:
                safe = False
            i = i + 1
    else:
        safe = False
    return safe
    
def main():
    reports = parse_input()
    safe_reports = []
    for report in reports:
        safe = check_report(report)
        if safe:
            safe_reports.append(report)
        else:
            alt_reports = generate_alt_reports(report)
            alt_safe = False
            for alt_report in alt_reports:
                if check_report(alt_report):
                    alt_safe = True
            if alt_safe:
                safe_reports.append(report)
    print("There are {} safe reports".format(len(safe_reports)))
    
if __name__ == "__main__":
    main()
