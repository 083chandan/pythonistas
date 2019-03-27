# Using incremental recursion
str1 = "NAGARRO"
str2 = "abcNjhgAhGjhfhAljhRkhgRbhjbevfhO"

lenStr1 = len(str1)
lenStr2 = len(str2)
def recursiveIncCheck(str1, str2, x, y):
    if x == lenStr1:
        return True
    elif y == lenStr2:
        return False
    if(str1[x] == str2[y]):
        return recursiveIncCheck(str1, str2, x+1, y+1)
    return recursiveIncCheck(str1, str2, x, y+1)

print(recursiveIncCheck(str1, str2, 0, 0))



# Using decrememntal recursion

# str1 = "chandan"
# str2 = "mynameischandan"

# lenStr1 = len(str1)
# lenStr2 = len(str2)
# def recursiveDecCheck(str1, str2, x, y):
#     if x==0: return True
#     if y==0: return False
#     if(str1[x-1] == str2[y-1]):
#         return(recursiveDecCheck(str1, str2, x-1, y-1))
#     return recursiveDecCheck(str1, str2, x, y-1)

# print(recursiveDecCheck(str1, str2, lenStr1, lenStr2))


# Using incremntal method

# str1 = "chandan"
# str2 = "mynameischandan"

# lenStr1=len(str1)
# lenStr2=len(str2)

# i=0
# j=0
# while i<lenStr1 and  j<lenStr2:
#     if(str1[i]==str2[j]):
#         print(str1[i])
#         i+=1
#     j+=1

# if(i==lenStr1):
#     print(True)
