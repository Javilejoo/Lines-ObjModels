from gl import Renderer
import shaders


# El tamaño del FrameBuffer
width = 960
height = 540



# Se crea el renderizador
rend = Renderer(width, height)
rend.glBackgroundTexture("textures/fondoOnePiece.bmp")
rend.glClearBackground()


# Le damos los shaders que se utilizarán
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.shaderNuevo

# Cargamos los modelos que renderizaremos
rend.glLoadModel(filename="models/Onepiece.obj",
                 textureName="textures/Onepiece.bmp",
                 translate=(6, -4, -12),
                 rotate=(0, 35, 0),
                 scale=(1,1, 1))

# Se renderiza la escena
rend.glRender()

# Le damos los shaders que se utilizarán
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.gouradShader
# Cargamos los modelos que renderizaremos
rend.glLoadModel(filename="models/Thousand Sunny.obj",
                 textureName="textures/tex.bmp",
                 translate=(-10, -12, -25),
                 rotate=(0, 45, 0),
                 scale=(1,1, 1))


# Se renderiza la escena
rend.glRender()

# Se crea el FrameBuffer con la escena renderizada
rend.glFinish("Onepiece.bmp")




