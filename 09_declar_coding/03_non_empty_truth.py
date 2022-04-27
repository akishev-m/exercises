#!/usr/bin/env python

def non_empty_truth(lst):
    result = [el for el in [[el_i for j, el_i in enumerate(el) if el_i] for el in lst if el] if el]
    return result

#res = [el for i, el in [el_i for el_i in lst if el_i] if el]
    

def temp(lst):
    res = [[el_i for j, el_i in enumerate(el) if el_i] for i, el in enumerate(lst) if el]
    return res



def main():
    a = [[0, 1, 2], [], [], [False, True, 42]]
    b = [[0, ""], [False, None]]
    c = [[0]]
    d = [[], []]
    e = []
    lst = e 
    print(non_empty_truth(lst))

if __name__ == '__main__':
    main()
