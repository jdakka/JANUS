import openpiv.tools
import openpiv.process
import openpiv.scaling

frame_a  = openpiv.tools.imread( 'Mackanzie1.jpg' )
frame_b  = openpiv.tools.imread( 'Mackanzie2.jpg' )

#%%

u, v, sig2noise = openpiv.process.extended_search_area_piv( frame_a, frame_b, window_size=24, overlap=12, dt=0.02, search_area_size=64, sig2noise_method='peak2peak' )

x, y = openpiv.process.get_coordinates( image_size=frame_a.shape, window_size=24, overlap=12 )

u, v, mask = openpiv.validation.sig2noise_val( u, v, sig2noise, threshold = 1.3 )

x, y, u, v = openpiv.scaling.uniform(x, y, u, v, scaling_factor = 3 )

openpiv.tools.save(x, y, u, v, mask, 'exp1_001.txt' )
