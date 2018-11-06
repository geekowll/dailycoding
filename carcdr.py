"""
cons(a,b) constructs a pair
car(pair) and cdr(pair) returns first and last element of the pair.

car(cons(3,4)) => 3
cdr(cons(3,4)) => 4

"""

def cons(a,b):
    def pair(f):
	retrn f(a,b)

    return pair

