from multiprocessing import Process, Pool
import copy
import numpy

res = 0

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]


def element(index, A, B):
    result = copy.copy(B)
    i, j = index
    global res
    # get a middle dimension
    N = len(A[0]) or len(B)
    # iterate through rows of X
    for i in range(N):
      # iterate through columns of Y
      for j in range(N):
          # iterate through rows of Y
          for k in range(N):

              result[i][j] += int(A[i][k]) * int(B[k][j])
    print (result)

    print (res, "done")
    with open ('file.txt', 'a') as f:
        f.write(str(result) + " this is the result\n\n")

    return res


with open('file.txt', 'w+') as f:
    pass


p1 = Process(target=element, args=[(0, 0), matrix1, matrix2])
p1.start()
p1.join()

with open ("matr.txt", "r") as f:
    matrix1=f.readline()

matrix1=matrix1.split()
matrix1=numpy.array(matrix1)
matrix1=numpy.resize(matrix1,(2,2))
print(matrix1)
matrix2=numpy.copy(matrix1)
matrix1=matrix1.astype(int)
matrix2=matrix2.astype(int)

p1 = Process(target=element, args=[(0, 0), matrix1, matrix2])
p1.start()
p1.join()

print(res)



