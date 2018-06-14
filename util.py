from numpy import zeros
from matplotlib import pyplot as plt
from imageio import imread

def build_r(N1, N2, n1, n2, s, t):
    """ Return a matrix which can be used to extract
        a vectorized patch from a vectorized image.
        N1, N2: rows, cols of image
        n1, n1: rows, cols of patch
        s , t : start row, start col of patch
    """
    # get a list of indices of the patch elements
    inds = []
    for row in range(n1):
        for col in range(n2):
            inds.append(N2*(s + row) + t + col)

    R = zeros((n1*n2, N1*N2))
    for i in range(n1*n2):
        R[i,inds[i]] = 1.0
    return R 

def build_r2(img, patch):
    return build_r(img.rows, img.cols, patch.rows, patch.cols, patch.top, patch.left)

class Image:
    """ Image class makes it easy to load from a file,
        show, slice, and switch between vectorized and non-vectorized 
    """
    def __init__(self, M):
        self.M = M
        self.rows, self.cols = M.shape
        self.vec = M.reshape(self.rows * self.cols)

    def __getitem__(self, val):
        return self.M.__getitem__(val)

    @classmethod    
    def from_file(cls, path):
        """ Load an image from a file at a given path
        """
        return cls(imread(path).base)

    def unvec(self):
        """ Return an unvectorized version of the image
        """
        return self.M

    def show(self):
        """ Show the image as grayscale
        """
        plt.imshow(self.M, cmap='gray')
        plt.show()
    
class Patch:
    """ Lazy patch for an image.  R is not created until needed
    """
    def __init__(self, image, top, left, rows, cols=None):
        """ expects an image, a top left corner for the patch and the number of
        rows and columns for the patch.  If cols is omitted, assume square
        """
        self.base = image
        self.top = top
        self.left = left
        self.rows = rows
        self.cols = self.rows if cols is None else cols
        self.image = None
        self.R = None
        self.M = None
        self.vec = None

    def __getitem__(self, val):
        self.construct()
        return self.M.__getitem__(val)
    
    def build_r(self):
        if self.R is None:
            self.R = build_r2(self.base, self)
    
    def construct(self):
        if self.M is None:
            self.build_r()
            self.M = self.R.dot(self.base.vec)
            self.M.shape = (self.rows, self.cols)
            self.vec = self.M.reshape(self.rows*self.cols)

    def show(self):
        """ Show the patch using pyplot (assumes grayscale cmap)
        """
        self.construct()
        plt.imshow(self.M, cmap='gray')
        plt.show()
