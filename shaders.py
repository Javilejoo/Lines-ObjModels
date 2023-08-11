import random
from mathLib import *

def vertexShader(vertex, **kwargs):
    
    # El Vertex Shader se lleva a cabo por cada v�rtice

    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]

    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]
    # Se aplica la secuencia de transformaciones: 
    #vt = vpMatrix * projectionMatrix * viewMatrix * modelMatrix @ vt
    temp = multiplicar_matrices(vpMatrix, projectionMatrix)
    temp = multiplicar_matrices(temp, viewMatrix)
    temp = multiplicar_matrices(temp, modelMatrix)
    #Vector transformacion al vertices
    vt = multiplicar_matriz_vector(temp, vt)
    #vt = vt.tolist()[0]

    vt = [vt[0]/vt[3],
          vt[1]/vt[3],
          vt[2]/vt[3]]

    return vt

def fragmentShader(**kwargs):

    # El Fragment Shader se lleva a cabo por cada pixel
    # que se renderizar� en la pantalla.

    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]

    if texture != None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1,1,1)


    return color
