"""
mehods:
add(value)
union(set)
intersection(set)
difference(set)
issuperset(set)
issubset(set)
"""

set_a = {10,15,20,25}

set_b = {10,20,30,45,50}

union_set = set_a.union(set_b)

print("union_set=",union_set)

intersection_set = set_a.intersection(set_b)

print("Intersection_set=",intersection_set)

diff_set = set_a.difference(set_b)

print("Diff_set=",diff_set)

superset = set_a.issuperset(set_b)

print("superset=",superset)

print(set_a.issubset(set_b))