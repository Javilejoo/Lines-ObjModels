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

rend.glBackgroundTexture("textures/fondoDragonBall.bmp")
rend.glClearBackground()

 #Thousand Sunny
# Le damos los shaders que se utilizarán
rend.glDirectionLight(0,0,-1)
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.metallicShader
# Cargamos los modelos que renderizaremos
rend.glLoadModel(filename="models/ThousandSunny.obj",
                 textureName="textures/tex.bmp",
                 translate=(0, 0, 1),
                 rotate=(0, 0, 0),
                 scale=(1,1, 1)) 
rend.glRender()  

# GOING MERRY
# Le damos los shaders que se utilizarán
rend.glDirectionLight(0,0,-0.9)
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.blinnPhongShader
# Cargamos los modelos que renderizaremos
rend.glLoadModel(filename="models/GoingMerry.obj",
                 textureName="textures/Onepiece.bmp",
                 translate=(0,0,0),
                 rotate=(0, 0, 0),
                 scale=(1,1, 1))
rend.glRender() 

#Pokeball
# # Le damos los shaders que se utilizarán
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.pixelArtShader
# Cargamos los modelos que renderizaremos
rend.glLoadModel(filename = "models/pokebola.obj",
                 textureName="textures/pokeball.bmp",
                 translate=(-2,2,0),
                 rotate=(0,0,0),
                 scale=(1,1,1))
rend.glRender()  

#Goku
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.gokuShader
# Cargamos los modelos que renderizaremos
rend.glLoadModel(filename = "models/goku.obj",
                 textureName="textures/DBOkidgoku2.bmp",
                 translate=(-2,2,0),
                 rotate=(0,0,0),
                 scale=(1,1,1))
rend.glRender()

rend.glDirectionLight(0,0,1)
#Squirtle
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.squirtleShader
# Cargamos los modelos que renderizaremos
rend.glLoadModel(filename = "models/squirtlepie.obj",
                 textureName="textures/Squirtle_base.bmp",
                 translate=(0,0,0),
                 rotate=(0,0,0),
                 scale=(1,1,1))
rend.glRender()



# Se crea el FrameBuffer con la escena renderizada
rend.glFinish("OnePieceXDragonBallXPokemon.bmp")

end_time = time.time()
print(f"Execution took {end_time - start_time:.2f} seconds to run.")




