"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
    diffs = [] 
    for i, x in enumerate(q): 
        for j, y in enumerate(q): 
            if i != j:  
                diffs.append(abs(x-y))     
    return int(sum(diffs)/2) 