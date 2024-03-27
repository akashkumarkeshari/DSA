def solve(s, output):
    if len(s) == 0:
        print(output)
        return

    temp = s[0]
    current = output[-1] if len(output) > 0 else ""
    s = s[1:]

    if current == temp:
        solve(s, output)
    else:
        solve(s, output+temp)


s = "aabccba"
solve(s, output="")
