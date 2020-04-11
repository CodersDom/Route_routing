def probability(num, den):
    if den == 0:
        return 0
    return num / den


def matrixEdges(matrx, n):
    edges = dict()
    mylist = []
    for i in range(n):
        for j in range(n):
            var = matrix[i][j]
            if var not in edges:
                edges[var] = []
            if i - 1 >= 0:
                edges[var].append(matrix[i - 1][j])
            if i + 1 < n:
                edges[var].append(matrix[i + 1][j])
            if j - 1 >= 0:
                edges[var].append(matrix[i][j - 1])
            if j + 1 < n:
                edges[var].append(matrix[i][j + 1])
    prob = dict()
    for pt1 in edges:
        if pt1 not in prob:
            prob[pt1] = dict()
        den1 = len(edges[pt1])
        for pt2 in edges[pt1]:
            if pt2 not in prob:
                prob[pt2] = dict()
            den2 = len(edges[pt2])
            temp = (probability(1, den1) + probability(1, den2)) / 2
            prob[pt1][pt2] = temp
            prob[pt2][pt1] = temp
    for pt1 in prob:
        for pt2 in prob[pt1]:
            # print(pt1,"-",pt2,"Probability :",prob[pt1][pt2])
            edges = {"pt1": pt1, "pt2": pt2, "weight": prob[pt1][pt2]}
            mylist.append(edges)
    return mylist
    # print(edges)


# n = int(input("Enter N (Graph will be in N*N Format) : "))
n = 16
matrix = []
val = 0
for i in range(n):
    matrix.append([])
    for _ in range(n):
        matrix[i].append(val)
        val += 1
# matrixEdges(matrix,n)

# print("test")
# print(matrixEdges(matrix,n))
