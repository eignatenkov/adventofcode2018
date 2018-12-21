def parse_input(filename):
    with open(filename) as f:
        input = f.readline().strip().split(' ')
    return input



if __name__ == "__main__":
    print (parse_input("data/day08_input.txt"))
