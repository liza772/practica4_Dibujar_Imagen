#Yasmin Esqueda Muñoz
#Práctica 4

import cv2
import numpy as np
from matplotlib import pyplot as plt #parte visual
from matplotlib import pylab 
xa=120
xb=300
ya=100
yb=500

# Crea una imagen en negro
#img = np.zeros((512,512,3), np.uint8)

imagen=cv2.imread("harrypotter.jpg")
#De matriz BGR a RGB

area = imagen[xa:xb,ya:yb]
gris = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY) 
cambio = cv2.cvtColor(gris,cv2.COLOR_GRAY2BGR)
imagen[xa:xb,ya:yb] = cambio
fig = plt.figure(figsize=(10,7), constrained_layout=True)

#Círculo
imagen = cv2.circle(imagen,(300,300), 100, (0,0,255), -1)
#coordenadas del centro y el valor del radio, rojo, de radio igual a 100 px

#Texto
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,'HARRY POTTER',(40,90), font, 3,(255,255,255),2,cv2.LINE_AA)
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
plt.imshow(imagen)
plt.axis('off')
plt.title("Imagen 1")
plt.show()




