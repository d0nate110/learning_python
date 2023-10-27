def transpose(m):
    return [list(row) for row in zip(*m)]
def powers(lista, arg1, arg2):
    li_len = len(lista)
    m_list = []
    new_list = []
    if arg2 < arg1:
        return [[]]
    for num in range(arg1, arg2 + 1):
        a_list = []
        for val in lista:
            a_list.append(val ** num)
        m_list.append(a_list)
        
    return [list(row) for row in (zip(*m_list))]
def matmul(A, B):

    if not A or not B:
        return []
    if len(A[0]) != len(B):
        raise ValueError("The number of columns in matrix A must match the number of rows of matrix B")
    
    A_len = len(A)
    B_len = len(B[0])
    result = []
    
    for i in range(A_len):
        row = []
        for j in range(B_len):
            value = 0
            for k in range(len(B)):
                value = A[i][k] * B[k][j] + value
            row.append(value)
        result.append(row)
    return result
def invert(A):
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    det = a * d - b * c
    return [[d/det, -b/det], [-c/det, a/det]]
def loadtxt(f):
    matrix = []
    with open(f, 'r') as file:
        for line in file:
            row = [float(value) for value in line.strip().split()]
            matrix.append(row)
    file.close()
    return matrix
        
        
