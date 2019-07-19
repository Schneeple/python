import solarCalculations as sC
import numpy as np


d = np.linspace(1,366,366)
j = []
for i in d:
    

    x = sC.earth(i , -115.6637 , np.deg2rad(40.793919))
    print(i , x.groundRadiation())



    
    
