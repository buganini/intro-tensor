from .functor import Functor

def transpose(functor, dims):
    iexpr = [f"i{axis}" for axis in dims]
    shape = [functor.shape[dims[i]] for i in range(len(functor.shape))]
    return Functor(
        shape,
        iexpr = iexpr,
        desc = f"transposed_{functor.desc}",
        subs = [functor]
    )

def stack(array, axis=0):
    if axis < 0:
        axis = len(array[0].shape) + axis
    iexpr = [f"i{i}" for i in range(len(array[0].shape))]
    iexpr.insert(axis, 0)
    shape = list(array[0].shape)
    shape.insert(axis, list(range(0,len(array)+1)))
    return Functor(
        shape,
        iexpr = iexpr,
        desc = f"stack_{axis}",
        subs = array
    )

def concatenate(array, axis=0):
    iexpr = [f"i{i}" for i in range(len(array[0].shape))]
    shape = list(array[0].shape)
    shape[axis] = [shape[axis]*(i) for i in range(len(array)+1)]
    return Functor(
        shape,
        iexpr = iexpr,
        desc = "concatenate",
        subs = array
    )

def expand_dims(a, axis):
    iexpr = [f"i{i}" for i in range(len(a.shape))]
    iexpr.insert(axis, 0)
    shape = list(a.shape)
    shape.insert(axis, 1)
    return Functor(
        shape,
        iexpr = iexpr,
        desc = f"expand_dims_{axis}_{a.desc}",
        subs = [a]
    )
