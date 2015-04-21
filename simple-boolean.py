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
    return OPERATIONS[operation](x, y
