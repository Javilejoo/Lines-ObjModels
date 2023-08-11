from gl import Renderer
import shaders

# El tama�o del FrameBuffer
width = 960
height = 540
scale = 1

eyePositionX = 0
eyePositionY = 0
eyePositionZ = 0

# Se crea el renderizador
rend = Renderer(width, height)

# Le damos los shaders que se utilizar�s
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

#rend.glCamMatrix(translate = (0,0,0), rotate = (0,0,0))
# Cargamos los modelos que rederizaremos
#rend.glLoadModel(filename = "models/Onepiece.obj",
                 #textureName = "textures/Onepiece.bmp",
                 #translate = (0, 0, -10),
                 #rotate = (0, 45, 0),
                 #scale = (2,2,2))
def mediumShot():
    

    cameraPositionX = 1
    cameraPositionY = 0.5
    cameraPositionZ = 1

    rend.glLookAt(
        camPos = (cameraPositionX, cameraPositionY, cameraPositionZ), 
        eyePos= (eyePositionX, eyePositionY, eyePositionZ))

    rend.glLoadModel(filename = "models/Onepiece.obj",
                     textureName ="textures/Onepiece.bmp",
                     translate = (0, -0.2, 0),
                     rotate = (0, 45, 0),
                     scale = (scale, scale, scale))
    
    # Se renderiza la escena
    rend.glRender()

    # Se crea el FrameBuffer con la escena renderizada
    rend.glFinish("MediumShot.bmp")





