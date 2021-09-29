#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for item in my_list:
        try:
            print("{}".format(item), end="")
            i += 1
            if i >= x:
                raise
        except:
            break
    print("")
    return i
