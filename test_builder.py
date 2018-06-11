from imageio import imread
from matplotlib import pyplot as plt
from numpy import *
import util

filepath = "dom_sm.jpg"
M = imread(filepath)
N1, N2 = M.shape
n1, n2 = 8, 8
s, t = 100, 100
R = util.build_r(N1, N2, n1, n2, s, t)
M.reshape(N1*N2)

