def solve(l, index):
    if index == len(l):
        print(l)
        return

    i = index
    while i < len(l):
        l[i], l[index] = l[index], l[i]
        solve(l, index+1)
        l[i], l[index] = l[index], l[i]
        i += 1

l = [1, 2, 3]
solve(l, index=0)
"""this is swapping technique of getting all the permutation of
the list, we can think of it as that we are trying every element
at one position as in case of permutation calculation (3 X 2 X 1)"""
