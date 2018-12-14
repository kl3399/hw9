def intersection_list(lst1, lst2):
    int_lst = [num for num in lst1 if num in lst2]
    return int_lst

def main():
    print(intersection_list([3, 9, 2, 7, 1], [4, 1, 8, 2]))

if __name__ == "__main__":
    main()