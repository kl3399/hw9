from ChainingHashTableMap import ChainingHashTableMap

def intersection_list(lst1, lst2):
    c_hash = ChainingHashTableMap()
    for num in lst1:
        if num not in c_hash:
            c_hash[num] = 1
    int_lst = [num for num in lst2 if num in c_hash]
    return int_lst

def main():
    print(intersection_list([3, 9, 2, 7, 1], [4, 1, 8, 2]))

if __name__ == "__main__":
    main()