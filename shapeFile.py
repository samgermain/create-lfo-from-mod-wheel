import numpy as np
import pickle

class Shape_Saving_type:
    #Chunk_Shape_Saving;              
    
    def __init__(self):
        self.val_curve = []                                     #fill with 0 to 1
        self.val_EnvX = []                                      #fill with 0 to 388.0 range
        self.val_EnvY = []                                      #fill with 0 to 240.0 range
        self.reserved = np.array([0.0 for x in range(64)])      #fill with 0.0
        self.CurrentNumPoints = 0   
        self.Shapeversion = 1                                   #fill with 1, well, good for 255 versions ;)
        self.padding = np.array([0.0 for x in range(6)])        #fill with 0.0 - padding[0] set to 1 indicates LFOTOol 1.5 (vector) sizes

    def addPoint(self, x, y, curve):
        if self.CurrentNumPoints < 64:
            self.val_curve.append(curve)
            self.val_EnvX.append(x)
            self.val_EnvY.append(y)
            self.CurrentNumPoints += 1

    def save(self, fileName):
        
        saveObject = {
            'val_curve': self.val_curve,
            'val_EnvX': self.val_EnvX,
            'val_EnvY': self.val_EnvY,
            'reserved': self.reserved,
            'CurrentNumPoints': self.CurrentNumPoints,
            'Shapeversion': self.Shapeversion,
            'padding': self.padding
        }
        
        with open(fileName + '.shp', 'wb') as file: 
            pickle.dump(saveObject, file)
            #file.write(saveObject)

        with open(fileName + '.txt', 'w') as file:
            file.write(str(saveObject))

example = Shape_Saving_type()
example.addPoint(0,0,0.6)
example.addPoint(240,194,0.4)
example.addPoint(0,388,0.5)
example.save('shapeFile')