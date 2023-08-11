import random
from mathLib import *
import numpy as np

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

def flatShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    dLight = kwargs["dLight"]
    normal = kwargs["triangleNormal"]

    b = 1.0
    g = 1.0
    r = 1.0

    color = [1,1,1]

    if texture != None:
        texureColor = texture.getColor(texCoords[0], texCoords[1])
        b *= texureColor[2]
        g *= texureColor[1]
        r *= texureColor[0]
    
    
    dLight = np.array(dLight)
    intensity = np.dot(normal, -dLight)

   
    b *= intensity
    g *= intensity
    r *= intensity
    
 

    if intensity > 0:
        return r,g,b
    else:
        return [0,0,0]
    
def shaderNuevo(**kwargs):
    
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    dLight = kwargs["dLight"]
    normal = kwargs["triangleNormal"]

    b = 1.0
    g = 1.0
    r = 1.0

    # Obtener las coordenadas de textura
    u, v = texCoords

    # Modificar colores basados en las coordenadas de textura
    r *= u
    g *= v
    b *= (u + v) / 2

    # Calcular intensidad de la luz
    dLight = np.array(dLight)
    intensity = np.dot(normal, -dLight)

    # Aplicar intensidad de luz a los colores
    r *= intensity
    g *= intensity
    b *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]
    
def shaderNuevos(**kwargs):
    
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    dLight = kwargs["dLight"]
    normal = kwargs["triangleNormal"]

    b = 1.0
    g = 1.0
    r = 1.0

    # Obtener las coordenadas de textura
    u, v = texCoords

    # Modificar colores basados en las coordenadas de textura
    r *= u
    g *= v
    b *= (u + v) / 2

    # Calcular intensidad de la luz
    dLight = dLight
    intensity = dot_product(normal, [-d for d in dLight])  # Multiplicar por -1 para invertir la dirección de la luz

    # Aplicar intensidad de luz a los colores
    r *= intensity
    g *= intensity
    b *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]


