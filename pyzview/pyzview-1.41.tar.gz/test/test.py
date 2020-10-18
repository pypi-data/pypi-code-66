#%%
import numpy as np

from pyzview import Pyzview

zv = Pyzview()
# zv.loadFile("../../models/horse.stl")
for i in range(10):
    pts = np.random.randint(-100,100,size=[100,4]).astype(np.float32)/100
    zv.update_points("pytestX",pts)
