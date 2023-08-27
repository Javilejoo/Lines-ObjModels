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

def normalize_color(color):
    return [max(0, min(1, channel)) for channel in color]

def blinnPhongShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0
    

    if texture is not None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]
        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal = [
        u * nA[0] + v * nB[0] + w * nC[0],
        u * nA[1] + v * nB[1] + w * nC[1],
        u * nA[2] + v * nB[2] + w * nC[2]
    ]

    # Calcular la intesidad de la luz
    intensity = normal[0] * -dLight[0] + normal[1] * -dLight[1] + normal[2] * -dLight[2]
    intensity = max(intensity, 0)  

    # calcular la direccion de angulo
    viewDir = [0, 0, -1]  
    viewDir_len = (viewDir[0]**2 + viewDir[1]**2 + viewDir[2]**2)**0.5
    viewDir = [viewDir[0] / viewDir_len, viewDir[1] / viewDir_len, viewDir[2] / viewDir_len]

    # calcular la mitad del vector
    halfVec = [
        viewDir[0] + (-dLight[0]),
        viewDir[1] + (-dLight[1]),
        viewDir[2] + (-dLight[2])
    ]
    halfVec_len = (halfVec[0]**2 + halfVec[1]**2 + halfVec[2]**2)**0.5
    halfVec = [halfVec[0] / halfVec_len, halfVec[1] / halfVec_len, halfVec[2] / halfVec_len]

    # calcular el spcereclect
    specReflect = max(0, (normal[0] * halfVec[0] + normal[1] * halfVec[1] + normal[2] * halfVec[2])**16)

    # modificar la reflexion
    r *= intensity + specReflect
    g *= intensity + specReflect
    b *= intensity + specReflect
    r, g, b = normalize_color([r, g, b])



    return r, g, b


def flatShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    dLight = kwargs["dLight"]
    normal = kwargs["normals"]

    b = 1.0
    g = 1.0
    r = 1.0

    color = [1, 1, 1]

    if texture is not None:
        tU = texCoords[0]
        tV = texCoords[1]
        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    intensity = dot_product(normal, [-dLight[0], -dLight[1], -dLight[2]])

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]



def gouradShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture is not None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]
        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal = [
        u * nA[0] + v * nB[0] + w * nC[0],
        u * nA[1] + v * nB[1] + w * nC[1],
        u * nA[2] + v * nB[2] + w * nC[2]
    ]

    intensity = dot_product(normal, [-dLight[0], -dLight[1], -dLight[2]])

    b *= intensity
    g *= intensity
    r *= intensity

    r, g, b = normalize_color([r, g, b])

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]



def mosaicShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    # Definir el tamaño del mosaico
    mosaic_size = 20  # Tamaño de cada celda del mosaico

    # Calcular las coordenadas de la celda actual
    cell_u = int(u * mosaic_size) / mosaic_size
    cell_v = int(v * mosaic_size) / mosaic_size

    # Calcular los colores basados en las coordenadas de la celda
    r = cell_u
    g = cell_v
    b = (cell_u + cell_v) / 2
    normal = [
        u * nA[0] + v * nB[0] + w * nC[0],
        u * nA[1] + v * nB[1] + w * nC[1],
        u * nA[2] + v * nB[2] + w * nC[2]
    ]

    # Calcular intensidad de la luz
    intensity = dot_product(normal, [-dLight[0], -dLight[1], -dLight[2]])

    # Aplicar intensidad de luz a los colores
    r *= intensity
    g *= intensity
    b *= intensity
    r, g, b = normalize_color([r, g, b])

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]


def pixelArtShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture is not None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]
        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2]]

    # Calcula la intensidad de la luz
    intensity = normal[0] * -dLight[0] + normal[1] * -dLight[1] + normal[2] * -dLight[2]

    # Aplica el efecto de estilo de juegos de píxeles
    color_steps = 4  # Número de pasos de color
    r = round(r * color_steps) / color_steps
    g = round(g * color_steps) / color_steps
    b = round(b * color_steps) / color_steps

    r, g, b = normalize_color([r, g, b])

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]
   
def shaderNuevo(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture is not None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]
        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    # Crear gradiantes en base a las baricentricas
    gradient_factor = u + v  

    # colores gradiantrs
    r *= gradient_factor
    g *= gradient_factor
    b *= gradient_factor

    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2]]

    # intensidad de la luz
    intensity = normal[0] * -dLight[0] + normal[1] * -dLight[1] + normal[2] * -dLight[2]

    # Modificar la intensidad
    r *= intensity
    g *= intensity
    b *= intensity
    r, g, b = normalize_color([r, g, b])

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]

def metallicShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture is not None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]
        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2]]

    # Calcula la intensidad de la luz
    intensity = dot_product(normal, [-dLight[0], -dLight[1], -dLight[2]])

    # Aplica efectos de un material metálico
    fresnel = math.pow((1 - intensity), 5)  # Efecto de Fresnel
    halfway_dir = division_vector_escalar([0, 0, -1], normalizar([-dLight[0], -dLight[1], -dLight[2]]))
    specular = math.pow(max(dot_product(normal, halfway_dir), 0), 16)  # Término especular

    # Mezcla el color base con el color especular
    metallic = 0.2  # Ajusta el valor de metalicidad
    r = (1 - metallic) * r + metallic * (specular + fresnel)
    g = (1 - metallic) * g + metallic * (specular + fresnel)
    b = (1 - metallic) * b + metallic * (specular + fresnel)

    r, g, b = normalize_color([r, g, b])

    if intensity > 0:
        return r, g, b
    else:
        return [0, 0, 0]

def lightingShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w = kwargs["bCoords"]

    b = 1.0
    g = 1.0
    r = 1.0

    if texture is not None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]
        textureColor = texture.getColor(tU, tV)
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal = [u * nA[0] + v * nB[0] + w * nC[0],
              u * nA[1] + v * nB[1] + w * nC[1],
              u * nA[2] + v * nB[2] + w * nC[2]]

    # Calcular la intensidad de la luz basada en el modelo de Lambert
    intensity = max(0, normal[0] * -dLight[0] + normal[1] * -dLight[1] + normal[2] * -dLight[2])

    # Aplicar intensidad de luz al color
    r *= intensity
    g *= intensity
    b *= intensity
    r, g, b = normalize_color([r, g, b])

    return r, g, b

