# Matrix Algebra
import numpy as np

A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])
u = np.matrix([6, 2, -3, 5])
v = np.matrix([3, 5, -1, 4])
w = np.matrix([[1], [8], [0], [5]])

matrix_arr = [A, B, C, D, u, v, w]
# Matrix Dimensions
for mat in matrix_arr:
    print(mat.shape)


# Vector Operation
alpha = 6

print(u + v)
print(u - v)
print(alpha * u)
print(np.inner(u, v))
print(np.linalg.norm(u))

# Matrix Operation
f31 = lambda _: A + C
f32 = lambda _: A - C.transpose()
f33 = lambda _: C.transpose() + 3 * D
f34 = lambda _: B * A
f35 = lambda _: B * A.transpose()
f36 = lambda _: B * C
f37 = lambda _: C * B
f38 = lambda _: B ** 4
f39 = lambda _: A * A.transpose()
f40 = lambda _: D.transpose() * D
fs = [f31, f32, f33, f34, f35, f36, f37, f38, f39, f40]
keys = list(range(31,41))
for k, f in enumerate(fs):
    try:
        print('%d.%d)' % (keys[k] // 10, keys[k] % 10))
        print(f([]))
        print('\n')
    except ValueError:
        print('matrix sizes do not match\n')







