#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed = 0  # Variable to keep track of the number of elements printed

    try:
        for i in range(x):
            print(my_list[i], end="")  # Printing elements from the list without a newline
            printed += 1  # Increment the count of printed elements
    except IndexError:
        pass  # Catching the IndexError when the index is out of range

    print()  # Print a newline after printing elements
    return printed  # Return the number of elements printed

