def transpose_matrix(matrix):
    if not matrix:
        return []
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create the transposed matrix with dimensions (cols x rows)
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed