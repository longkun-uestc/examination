

if __name__ == '__main__':
    N = int(input())
    box = list(map(int, input().split()))
    box.sort()
    count = 0
    while box:
        new_box = []
        for i in range(1, len(box)):
            if box[i] == box[i-1]:
                new_box.append(box[i])
        count += 1
        if len(list(set(new_box))) > 1:
            box = new_box
        else:
            count += len(new_box)
            break
    print(count)
