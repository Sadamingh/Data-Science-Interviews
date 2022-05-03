def mergeTwoSortedArray(list1, list2):
    result = []
    p1 = 0
    p2 = 0

    while True:
        if p1 == len(list1) and p2 == len(list2):
            return result
        elif p1 == len(list1):
            result.append(list2[p2])
            p2 += 1
        elif p2 == len(list2):
            result.append(list1[p1])
            p1 += 1
        else:
            if list1[p1] > list2[p2]:
                result.append(list2[p2])
                p2 += 1
            else:
                result.append(list1[p1])
                p1 += 1

    return result

def main():
    print(mergeTwoSortedArray([1,2], [3,4]))

if __name__ == '__main__':
    main()
