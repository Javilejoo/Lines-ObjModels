from gl import Renderer,  V3, color
import shaders


width = 1024
height = 1024

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader # type: ignore
rend.fragmentShader = shaders.fragmentShader # type: ignore

#rend.glLoadModel("Stone.obj", translate = (width/2, height/6, 0), scale = (85,85,85))

poligono1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), 
             (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

poligono4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
(750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
(597, 215), (552, 214), (517, 144) ,(466, 180)]

rend.poligonos(poligono1)
rend.poligonos(poligono4) 
rend.glRender()

rend.glFinish('output.bmp')