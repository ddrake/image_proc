from numpy import zeros

def build_r(N1, N2, n1, n2, s, t):
    # N1, N2: rows, cols of image
    # n1, n1: rows, cols of patch
    # s , t : start row, start col of patch
    # return a matrix which can be used to extract
    # a vectorized patch from a vectorized image.

    # get a list of indices of the patch elements
    inds = []
    for row in range(n1):
        for col in range(n2):
            inds.append(N2*(s + row) + t + col)

    R = zeros((n1*n2, N1*N2))
    for i in range(n1*n2):
        R[i,inds[i]] = 1.0
        print("i = {}, inds[i] = {}".format(i, inds[i]))
    return R 

