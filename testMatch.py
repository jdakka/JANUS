import openpiv.tools
import openpiv.process
import openpiv.scaling
import openpiv.validation 
#import matplotlib 
import numpy as np
import matplotlib.pyplot as plt

frame_a  = openpiv.tools.imread( 'exp1_001_a.bmp' )
frame_a =  np.int32(frame_a)
frame_b  = openpiv.tools.imread( 'exp1_001_b.bmp' )
frame_b = np.int32(frame_b)

#%%

u, v, sig2noise = openpiv.process.extended_search_area_piv( frame_a, frame_b, window_size=24, overlap=12, dt=0.02, search_area_size=64, sig2noise_method='peak2peak' )

#x, y = openpiv.process.get_coordinates( image_size=frame_a.shape, window_size=24, overlap=12 )

#u, v, mask = openpiv.validation.sig2noise_val( u, v, sig2noise, threshold = 1.3 )

#x, y, u, v = openpiv.scaling.uniform(x, y, u, v, scaling_factor = 3 )


image = plt.imshow(u)
image2 = plt.imshow(v)
plt.colorbar()

openpiv.tools.save(x, y, u, v, mask, 'exp1_001.txt' )
