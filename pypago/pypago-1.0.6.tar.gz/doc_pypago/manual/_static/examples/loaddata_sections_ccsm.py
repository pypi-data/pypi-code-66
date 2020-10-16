import pypago.pyio
import pypago.data
import numpy as np

modelsec = pypago.pyio.load('data/natl_gridsec.pygo')

filenameU = 'data/dyna_grid_U.nc'
filenameV = 'data/dyna_grid_V.nc'

# loading data on U/V points
dirvarUV = {'vel':['vozocrtx', 'vomecrty']}
modelsec = pypago.data.loaddata_sec_uv_ccsm(modelsec, filenameU, filenameV, dirvarUV)

# Loop over all the sections and convert transports back into 
# velocities
for m in modelsec[:]:
    m.vel = m.vel / m.areavect[np.newaxis, :]
