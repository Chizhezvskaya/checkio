from operator import and_, or_, xor, eq
​
​
def implication(x, y):
    return not x or y
​
OPERATIONS = {"conjunction": and_,
              "disjunction": or_,
              "implication": implication,
              "exclusive": xor,
              "equivalence": eq}
​
​
def boolean(x, y, operation):
    return OPERATIONS[operation](x, y)
    
    
    
def boolean(x, y, operation):
    return {'conjunction': x & y, 'disjunction': x | y, 'implication': (x + y - 1) if x else 1,
    'exclusive': not(x + y - 1), 'equivalence': x == y}[operation]
