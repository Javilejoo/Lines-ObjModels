from gl import Renderer
import shaders
import time
start_time = time.time()


# El tamaño del FrameBuffer
width = 960
height = 540



# Se crea el renderizador
rend = Renderer(width, height)
rend.glLookAt(camPos=(0,0,0),eyePos=(0,0,-1))

rend.glBackgroundTexture("textures/fondoOnePiece.bmp")
rend.glClearBackground()

# GOING MERRY
# Le damos los shaders que se utilizarán
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.shaderNuevo

rend.glDirectionLight(-1,0,-1)

#Thousand Sunny
# Le damos los shaders que se utilizarán
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.gouradShader
# Cargamos los modelos que renderizaremos
rend.glLoadModel(filename="models/ThousandSunny.obj",
                 textureName="textures/tex.bmp",
                 translate=(0, 0, 0),
                 rotate=(0, 0, 0),
                 scale=(1,1, 1)) 
rend.glRender() 


rend.glDirectionLight(0,0,-1)
# Cargamos los modelos que renderizaremos
rend.glLoadModel(filename="models/GoingMerry.obj",
                 textureName="textures/Onepiece.bmp",
                 translate=(0,0,0),
                 rotate=(0, 0, 0),
                 scale=(1,1, 1))
rend.glRender() 

#Pokeball
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.shaderNuevo
rend.glLoadModel(filename = "models/pokebola.obj",
                 textureName="textures/pokeball.bmp",
                 translate=(0,0,0),
                 rotate=(0,0,0),
                 scale=(1,1,1))
rend.glRender()  

 #Luffy
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.shaderNuevo
rend.glLoadModel(filename = "models/luffy.obj",
                 textureName="textures/Luffy1.bmp",
                 translate=(0,0,0),
                 rotate=(0,0,0),
                 scale=(1,1,1))
rend.glRender() 

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.shaderNuevo
rend.glLoadModel(filename = "models/zoro.obj",
                 textureName="textures/ZoroTex.bmp",
                 translate=(0,0,0),
                 rotate=(0,0,0),
                 scale=(1,1,1))
rend.glRender() 




# Se crea el FrameBuffer con la escena renderizada
rend.glFinish("Onepiece.bmp")

end_time = time.time()
print(f"Execution took {end_time - start_time:.2f} seconds to run.")




