#1
def find_inter(first, second):
    """Return intersection of two lists"""
    return set(first) & set(second)

a = [1, 3, 2]
b = [4, 3, 2]
print(find_inter(a, b)) 

#2
def build_tree(data):
    """Словарь родитель -> ребенок"""
    parents = {}

    for line in data:
        parent, child = line.split()
        parents[child] = parent
    return parents

def get_ancestors(person, parents):
    ancestors = []
    current = person

    while current:
        ancestors.append(current)
        current = parents.get(current)
    return ancestors

def find_lca(person_1, person_2, parents):
    ancerstors_1 = get_ancestors(person_1, parents)
    current = person_2

    while current:
        if current in ancerstors_1:
            return current
        current = parents.get(current)
    return None

    input_data = [
        "Alex Peter",
        "Peter Ivan",
        "Ivan Maria",
        "Anna Maria",
        "Maria",
        "Alex Anna",
        "Alex Maria",
        "Anna Alex"
    ]