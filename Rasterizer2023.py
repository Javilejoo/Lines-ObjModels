from gl import Renderer
import shaders


# El tamaño del FrameBuffer
width = 960
height = 540

# Se crea el renderizador
rend = Renderer(width, height)

# Le damos los shaders que se utilizarán
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.shaderNuevo

# Cargamos los modelos que renderizaremos
rend.glLoadModel(filename="models/calamardo.obj",
                 textureName="textures/albedo.bmp",
                 translate=(0, 1, -7),
                 rotate=(0, 0, 0),
                 scale=(1.5,1.5, 1.5))


# Se renderiza la escena
rend.glRender()

# Se crea el FrameBuffer con la escena renderizada
rend.glFinish("shaderNuevo.bmp")




