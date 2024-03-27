# recursive program of subset sum.
# here we are optimizing code by using only getting whether sum exists or not.


def isSubSetSum(input, sum, k):
    if len(input) == 0:
        if sum == k:
            return 1
        return 0

    temp = input[0]
    input = input[1:]

    # first we do not consider the element
    if isSubSetSum(input, sum, k) == 1:
        return 1

    # here we considered the element
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
