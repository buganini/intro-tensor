from tester_numpy import *

def f(np):
    a = np.ascontiguousarray(np.stack([np.array([[1,2,3],[4,5,6]]), np.array([[7,8,9],[10,11,12]])], axis=0))
    return a + 1

test_func("contiguous", f)
