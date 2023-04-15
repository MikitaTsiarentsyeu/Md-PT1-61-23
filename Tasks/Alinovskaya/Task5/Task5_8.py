# 8. Write a recursive function to count the number of occurrences of a given character in a string.
str = 'aaaafaafcvmv,mcvkdjskajaaaaaaaaaaddddddsaasaaaa'
def count_occur(charter, str, index = 0, count = 0):
    l = list(str)
    if len(l) == index:
        return count
    elif l[index] == charter:
        count +=1    
    return count_occur(charter, str, index + 1, count)
print(count_occur('a', str))