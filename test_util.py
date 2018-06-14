from imageio import imread
from matplotlib import pyplot as plt
from numpy import *
from util import *

filepath = "dom_sm.jpg"
cat = Image.from_file(filepath)
patch = Patch(cat,100,100,8)
patch.show()

