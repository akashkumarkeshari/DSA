# here we need to replace the c1 character from c2 in string s
def solve(s, output, c1, c2):
    if len(s) == 0:
        print(output)
        return

    temp = s[0]
    s = s[1:]

    if temp == c1:
        solve(s, output+c2, c1, c2)
    else:
        solve(s, output+temp, c1, c2)


s = "abca"
c1, c2 = "a", "b"
output = str()
index = 0
solve(s, output, c1, c2)


"""
Think of it as we are taking one character at a time and adding it
one by one into output string.
    During this process we can perform any operation according to our
usecase and manipulate that particular character or perform some other 
operations.
"""