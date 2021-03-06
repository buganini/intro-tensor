def ranger(rg):
    import itertools
    return itertools.product(*[range(base,base+num*step,step) for base,num,step in rg])

def rangel(a):
    return range(len(a))

def array_close(a, b):
    import numpy
    if tuple(a.shape) != tuple(b.shape):
        return False
    return numpy.allclose(a, b)

def list_dedup(l):
    ret = []
    for e in l:
        if e in ret:
            continue
        ret.append(e)
    return ret
