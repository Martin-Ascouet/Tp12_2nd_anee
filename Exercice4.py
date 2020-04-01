def listSum(l):
    if len(l) != 0:
        a = l[0]
        del l[0]
        return a+listSum(l)
    return 0

print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11
