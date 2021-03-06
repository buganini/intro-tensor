# Notice
* Still in pre-alpha development
* Runtime axis operations are not supported by design, such as:
    * Dynamic shape
    * Dynamic transpose

# Supported operations
* creation
    * array
    * zeros
    * ones
    * full
    * arange
    * meshgrid (xy)
* manipulation
    * transpose
    * stack
    * expand_dims
    * reshape
    * concatenate
    * repeat
* slicing
    * [n]
    * [m:n]

# Todo
* elementwise operations (with value)
* elementwise operations (with NDArray)
* buffer wrapping
* slicing
    * [m:n,s]
    * [m:n,p:q]
    * [m:n:s,p:q:t]
* slice assignment

# Example
```
>>> import ndafunctor.numpy as nf
>>> s = nf.meshgrid([1,2],[3,4,5])
>>> s.eval()
array([[[1., 2.],
        [1., 2.],
        [1., 2.]],

       [[3., 3.],
        [4., 4.],
        [5., 5.]]])
>>> f = s.jit()
>>> f()
array([[[1., 2.],
        [1., 2.],
        [1., 2.]],

       [[3., 3.],
        [4., 4.],
        [5., 5.]]], dtype=float32)
>>> s.print()
Functor: #3
    transposed_raw_meshgrid
    shape=((0, 2, 1), (0, 3, 1), (0, 2, 1))
    partitions=[[(0, 2, 1), (0, 2, 1), (0, 3, 1)]]
    vexpr=v0
    iexpr=[
            i0
            i2
            i1
    ]
    Functor[0]: #2
        raw_meshgrid
        shape=((0, 2, 1), (0, 2, 1), (0, 3, 1))
        partitions=[[(0, 2, 1), (0, 3, 1)], [(0, 2, 1), (0, 3, 1)]]
        iexpr=[
                si
                i0
                i1
        ]
        Functor[0]: #0
            raw_meshgrid[0]
            shape=((0, 2, 1), (0, 3, 1))
            vexpr=['ref', ['d', 'i0']]
            data=[1, 2]
        Functor[1]: #1
            raw_meshgrid[1]
            shape=((0, 2, 1), (0, 3, 1))
            vexpr=['ref', ['d', 'i1']]
            data=[3, 4, 5]
>>> print(open(f.source).read())
#include <stdio.h>
#include <math.h>

// Data
int d_meshgrid_0[] = {1,2};
int d_meshgrid_1[] = {3,4,5};

void gen_tensor3(float * tensor3)
{
    for(int i0=0;i0<2;i0+=1)
      for(int i1=0;i1<3;i1+=1)
    {
        int i0_0_1 = 0;
        int i1_0_1 = i0;
        int i2_0_1 = i1;
        int i0_0_2 = i0_0_1;
        int i1_0_2 = i2_0_1;
        int i2_0_2 = i1_0_1;
        tensor3[i0_0_2*3*2 + i1_0_2*2 + i2_0_2] = d_meshgrid_0[i0];
    }
    for(int i0=0;i0<2;i0+=1)
      for(int i1=0;i1<3;i1+=1)
    {
        int i0_0_1 = 1;
        int i1_0_1 = i0;
        int i2_0_1 = i1;
        int i0_0_2 = i0_0_1;
        int i1_0_2 = i2_0_1;
        int i2_0_2 = i1_0_1;
        tensor3[i0_0_2*3*2 + i1_0_2*2 + i2_0_2] = d_meshgrid_1[i1];
    }
}
```

# To be investigated:
* CUDA
* OpenMP
* LLIR
* Rust