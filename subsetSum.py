def isSubSetSum(input, sum, k):
    if len(input) == 0:
        if sum == k:
            return 1
        return 0

    temp = input[0]
    input = input[1:]

    if isSubSetSum(input, sum, k) == 1:
        return 1

    if isSubSetSum(input, sum+temp, k) == 1:
        return 1

    return 0


input = [3, 1, 5, 2, 6]
k = 7
ans = isSubSetSum(input, 0, k)
print("ans: ", ans)

k = 9
ans = isSubSetSum(input, 0, k)
print("ans: ", ans)

k = 19
ans = isSubSetSum(input, 0, k)
print("ans: ", ans)
