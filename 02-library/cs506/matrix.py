def get_minor(m, j):
   return [row[: j] + row[j + 1: ]
      for row in (m[: 0] + m[ 1: ])
   ]

def get_deternminant(M):
   #base case for 2 x2 matrix
    if len(M) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]

    determinant = 0
    for i in range(len(M)):
      f = [row[: i] + row[i + 1: ] for row in (M[: 0] + M[ 1: ])]
      determinant += ((-1) ** i) * M[0][i] * get_deternminant(f)
    return determinant