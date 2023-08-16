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

def gouradShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB,nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:

        tU = u * tA[0] + v * tB[0] + w * tC[0] 
        tV = u * tA[1] + v * tB[1] + w * tC[1]
  
        texureColor = texture.getColor(tU, tV)
        b *= texureColor[2]
        g *= texureColor[1]
        r *= texureColor[0]

    normal = [u * nA[0] + v * nB[0] + w * nC[0],
            u * nA[1] + v * nB[1] + w * nC[1],
            u * nA[2] + v * nB[2] + w * nC[2]]
    
    dLight = np.array(dLight)
    intensity = np.dot(normal, -dLight)


   
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g,b
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
    
def gouradShaderVCV(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture != None:
        tU = u * tA[0] + v * tB[0] + w * tC[0] 
        tV = u * tA[1] + v * tB[1] + w * tC[1]
        texureColor = texture.getColor(tU, tV)
        b *= texureColor[2]
        g *= texureColor[1]
        r *= texureColor[0]

    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2]]

    dLight = np.array(dLight)
    intensity = np.dot(normal, -dLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        # Agregar un toque de color aleatorio en los vértices
        color_variation = random.uniform(0.8, 1.2)
        r *= color_variation
        g *= color_variation
        b *= color_variation
        
        # Añadir un toque de color azul a los bordes
        edge_threshold = 0.8
        if intensity < edge_threshold:
            b += (1 - intensity) * 0.5

        # Añadir un toque de color amarillo en los puntos de mayor intensidad
        highlight_threshold = 0.95
        if intensity > highlight_threshold:
            r += (intensity - highlight_threshold) * 0.5
            g += (intensity - highlight_threshold) * 0.5

        return r, g, b
    else:
        return [0, 0, 0]
    

def pixelationShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]

    pixel_size = 10  # Tamaño de los píxeles

    b = 1.0
    g = 1.0
    r = 1.0

    if texture is not None:
        tU = (tA[0] + tB[0] + tC[0]) / 3.0  # Usamos el promedio de las coordenadas
        tV = (tA[1] + tB[1] + tC[1]) / 3.0  # Usamos el promedio de las coordenadas
        textureColor = texture.getColor(tU, tV)
        if textureColor is not None:
            b *= textureColor[2]
            g *= textureColor[1]
            r *= textureColor[0]

    # Redondeamos las coordenadas UV para crear el efecto de pixelación
    tU = round(tU * pixel_size) / pixel_size
    tV = round(tV * pixel_size) / pixel_size

    if texture is not None:
        textureColor = texture.getColor(tU, tV)
        if textureColor is not None:
            b *= textureColor[2]
            g *= textureColor[1]
            r *= textureColor[0]

    return r, g, b
