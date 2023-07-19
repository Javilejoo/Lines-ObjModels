from gl import Renderer,  V3, color
import shaders
import random


width = 1024
height = 1024

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader # type: ignore
rend.fragmentShader = shaders.fragmentShader # type: ignore

rend.glLoadModel("Stone.obj", translate = (width/2, height/6, 0), scale = (85,85,85))


rend.glRender()

rend.glFinish('output.bmp')