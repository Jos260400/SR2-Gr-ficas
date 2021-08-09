#Universidad del Valle de Guatemala
#Graficas por Computadoras Seccion 20
#Fernando Jose Garavito Ovando 18071
#SR2 Lines
from Srgl import Renderer, V2
width = 500
height = 500

rend = Renderer(width, height)

rend.glLine(V2(300, 220), V2(200, 220))
rend.glLine(V2(200, 220), V2(210, 160))
rend.glLine(V2(300, 220), V2(290, 160))
rend.glLine(V2(290, 160), V2(210, 160))

rend.glLine(V2(150, 450), V2(350, 450))
rend.glLine(V2(150, 450), V2(150, 370))
rend.glLine(V2(150, 370), V2(350, 370))
rend.glLine(V2(350, 370), V2(350, 450))

rend.glLine(V2(80, 100), V2(130, 100))
rend.glLine(V2(80, 150), V2(130, 150))
rend.glLine(V2(80, 150), V2(80, 100))
rend.glLine(V2(130, 150), V2(130, 100))

rend.glLine(V2(80, 300), V2(140, 300))
rend.glLine(V2(80, 250), V2(160, 250))
rend.glLine(V2(80, 300), V2(80, 250))
rend.glLine(V2(140, 300), V2(160, 250))

rend.glLine(V2(420, 300), V2(460, 250))
rend.glLine(V2(380, 250), V2(460, 250))
rend.glLine(V2(420, 300), V2(380, 250))

rend.glFinish("SR2.bmp")

