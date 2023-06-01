if __name__ == '__main__':
    i = 0
    with open('dataset3-processed.txt','r') as f:
        for line in f.read().splitlines():
            if len(line) == 0:
                i += 1
    print(i)