#1
def find_inter(first, second):
    """Return intersection of two lists"""
    return set(first) & set(second)

a = [1, 3, 2]
b = [4, 3, 2]
print(find_inter(a, b)) 

#2
