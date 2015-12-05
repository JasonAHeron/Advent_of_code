import PuzzleLib
from operator import mul


def get_clean_dimensions(dimensions):
    return map(int, dimensions.split('x'))


def calculate_total_paper():
    return sum([calculate_paper(dimensions) for dimensions in PuzzleLib.get_puzzle('2').split('\n')])


def calculate_paper(dimensions):
    if not dimensions:
        return 0
    dimensions = get_clean_dimensions(dimensions)
    l, w, h = dimensions
    extra = mul(*sorted(dimensions)[:2])
    return (2*l*w) + (2*w*h) + (2*h*l) + extra


#print "Total paper needed is: {}".format(calculate_total_paper())


def calculate_total_ribbon():
    return sum([calculate_ribbon(dimensions) for dimensions in PuzzleLib.get_puzzle('2').split('\n')])


def calculate_ribbon(dimensions):
    if not dimensions:
        return 0
    dimensions = get_clean_dimensions(dimensions)
    extra = sum(sorted(dimensions)[:2]) * 2
    return reduce(mul, dimensions) + extra


print "Total Ribbon Needed is: {}".format(calculate_total_ribbon())
