import numpy

def AND(x1, x2):
    # input
    x = numpy.array([x1, x2])
    # weight
    w = numpy.array([0.5, 0.5])
    # bias
    b = -0.7
    val = numpy.sum(w*x) + b
    if val > 0:
        return 1
    else:
        return 0

def NAND(x1, x2):
    x = numpy.array([x1, x2])
    w = numpy.array([-0.5, -0.5])
    b = 0.7
    val = numpy.sum(w*x) + b
    if val > 0:
        return 1
    else:
        return 0

def OR(x1, x2):
    pass

raw_args = input()
args = raw_args.split()
if args[0] == 'AND':
    print(AND(int(args[1]), int(args[2])))
elif args[0] == 'NAND':
    print(NAND(int(args[1]), int(args[2])))
elif args[0] == 'OR':
    print(OR(int(args[1]), int(args[2])))
else:
    print('bye')
