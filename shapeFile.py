import numpy as np

class Shape_Saving_type:
    #Chunk_Shape_Saving;              
    
    def __init__(self):
        self.val_curve = np.empty([64], dtype='float')          #fill with 0 to 1
        self.val_EnvX = np.empty([64], dtype='float')           #fill with 0 to 388.0 range
        self.val_EnvY = np.empty([64], dtype='float')           #fill with 0 to 240.0 range
        self.reserved = np.array([0.0 for x in range(64)])      #fill with 0.0
        self.CurrentNumPoints = 0   
        self.Shapeversion = 1                                   #fill with 1, well, good for 255 versions ;)
        self.padding = np.array([0.0 for x in range(6)])        #fill with 0.0 - padding[0] set to 1 indicates LFOTOol 1.5 (vector) sizes

    def addPoint(x, y, curve):
        self.val_curve

example = Shape_Saving_type()
