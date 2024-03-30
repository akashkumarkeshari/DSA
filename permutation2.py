def solve(input, output, d):
    if len(output) == len(input):
        print(output)
        return

    i = 0
    while i < len(input):
        if d[i] == 1:
            output.append(input[i])
            d[i] = 0
            solve(input, output, d)
            output.pop()
            d[i] = 1
        i += 1

l = [1, 2, 3]
output = []
d = list()
for x in l:
    d.append(1)
solve(l, output, d)

"""Here we took a list of same size as of input and iterating recursively over
that list on basis of which if that number has not been used in the
combination then we are appending that number into output."""
