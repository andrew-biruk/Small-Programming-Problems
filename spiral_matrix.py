import numpy

# creates spiral square matrix of side n:
n = int(input("Matrix size > "))
length = iter(list(range(1, n**2+1)))
mtx = numpy.zeros((n, n), dtype=int)
k = 0
while k != (n//2) + 1:
    for ln in mtx:
        for i in range(len(mtx[k])):
            if not mtx[k][i]:
                mtx[k][i] = next(length)
        mtx = numpy.rot90(mtx)
    while not mtx[0][0] == 1:
        mtx = numpy.rot90(mtx)
    k += 1
print(mtx, sep="\n")