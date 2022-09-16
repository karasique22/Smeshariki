from func import *
from cloud import Cloud

def setup():
    size(1024, 576)
    
def draw():
    set_gradient()
    set_grass_field()
    set_sand()
    
    
    draw_ezhik()
    draw_krosh()

    # cloud = Cloud(0, 0, 1)
    # cloud.display()
    
    noLoop()
    
