#!/usr/bin/env python3

def parse_input():
    list_a = []
    list_b = []
    with open("input", "r") as f:
        for line in f:
            cols = line.split()
            list_a.append(int(cols[0]))
            list_b.append(int(cols[1]))
    list_a.sort() # returns None
    list_b.sort()
    return list_a, list_b

def find_differences(list_a, list_b):
    difference = 0 
    for i in range(len(list_a)):
        diff = abs(list_a[i] - list_b[i])
        difference = difference + diff
    print("The difference between list A and list B is {}.".format(difference))
    
def calc_similarity_scores(list_a, list_b):
    total_sim = 0
    for location in list_a:
        appearances = 0 
        for a in list_b:
            if location == a:
                appearances = appearances + 1
        total_sim = total_sim + (location * appearances)
    print(total_sim)
    
def main():
    list_a, list_b = parse_input()
    find_differences(list_a, list_b)
    calc_similarity_scores(list_a, list_b)

if __name__ == "__main__":
    main()
